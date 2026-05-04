"""Terminal wizard for the check-in flow.

    iliad-checkin <path-or-url>

Walks the user through each step, asking yes/no or numeric choices. All the
heavy lifting lives in ``checkin.core``; this file is just glue + prompts.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from io import StringIO
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from .core import bblock_index, bblock_match, bblock_writer, profile as profile_mod
from .core import sniff as sniff_mod
from .core import transformer_runner, vocab_index, vocab_match

console = Console()


def _pick(prompt: str, options: list[str], default: int = 0) -> int:
    for i, opt in enumerate(options):
        console.print(f"  [{i}] {opt}")
    raw = input(f"{prompt} [{default}]: ").strip() or str(default)
    try:
        idx = int(raw)
    except ValueError:
        idx = default
    return max(0, min(idx, len(options) - 1))


def _yn(prompt: str, default: bool = True) -> bool:
    s = "Y/n" if default else "y/N"
    raw = input(f"{prompt} [{s}]: ").strip().lower()
    if not raw:
        return default
    return raw.startswith("y")


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9\-]+", "-", text.lower()).strip("-") or "bb"


@click.command()
@click.argument("source", required=True)
@click.option("--name", default=None, help="Target bblock id (folder name). Inferred if omitted.")
@click.option("--title", default=None, help="Human-readable title.")
@click.option("--non-interactive", is_flag=True, help="Accept defaults at every prompt.")
def main(source: str, name: str | None, title: str | None, non_interactive: bool) -> None:
    console.rule("[bold cyan]ILIAD check-in")

    # 1) Sniff
    sniff = sniff_mod.sniff(source)
    console.print(f"Detected format: [bold]{sniff.format}[/bold]  (url={sniff.is_url})")
    if sniff.format == "unknown":
        console.print("[red]Unable to classify source.[/red] Aborting.")
        sys.exit(2)

    # 2) Profile
    prof = profile_mod.profile(source, sniff.format)
    if prof.errors:
        console.print(f"[yellow]Profile warnings[/yellow]: {prof.errors}")
    console.print(f"Properties: {', '.join(p.name for p in prof.properties) or '(none)'}")
    if prof.dimensions:
        console.print(f"Dimensions: {', '.join(d.name for d in prof.dimensions)}")

    # 3) Match bblock
    bb_idx = bblock_index.load_index()
    matches = bblock_match.rank(prof, bb_idx)
    if matches:
        table = Table("score", "id", "title", "reason", "matches")
        for m in matches[:10]:   # table shows top 10; full list still selectable
            table.add_row(f"{m.score:.2f}", m.entry.id, m.entry.title, m.reason, ", ".join(m.matched_properties[:5]))
        console.print(table)
        console.print(f"[dim]({len(matches)} bblocks ranked total; full list available for selection)[/dim]")
    else:
        console.print("No bblocks in index.")

    options = [f"{m.entry.id} — {m.entry.title}" for m in matches] + ["(generate new)"]
    chosen_idx = 0 if non_interactive else _pick("Pick a target bblock", options, default=0)
    chosen_match = matches[chosen_idx] if chosen_idx < len(matches) else None
    target = chosen_match.entry if chosen_match else None

    # 4) Related bblocks
    if target:
        rel = bblock_match.related(target.id, bb_idx)
        if rel:
            console.print(f"Related by OGC standards: {', '.join(r.id for r in rel)}")

    # 5) Vocab mapping
    vidx = vocab_index.build_index()
    console.print(f"Vocab index: {vocab_index.summary(vidx)}")
    cands = vocab_match.match_properties([p.name for p in prof.properties], vidx, k=3)
    acks: list[bblock_writer.AcknowledgedMapping] = []
    for pname, clist in cands.items():
        if not clist:
            console.print(f"  {pname}: [dim]no local candidates[/dim]")
            continue
        console.print(f"  {pname}:")
        for i, c in enumerate(clist):
            console.print(f"    [{i}] {c.label or c.term} — {c.uri} (src={c.source}, score={c.score})")
        if non_interactive:
            pick = 0
        else:
            raw = input(f"    select [0-{len(clist)-1}] or 's' to skip: ").strip().lower()
            if raw == "s":
                continue
            try:
                pick = int(raw) if raw else 0
            except ValueError:
                pick = 0
        pc = clist[pick]
        acks.append(bblock_writer.AcknowledgedMapping(property_name=pname, uri=pc.uri, label=pc.label, source=pc.source))

    # 6) Transformer
    tf_lib = transformer_runner.load_library()
    target_out_hint = {
        "csv": "stac-item",
        "tsv": "stac-item",
        "json": "geojson",
        "geojson": "geojson",
    }.get(sniff.format)
    hits = transformer_runner.find_matching(sniff.format, target_out_hint, tf_lib)
    if not hits:
        console.print(f"[yellow]No library transformer for {sniff.format} → {target_out_hint}.[/yellow] A bblock-local one will be stubbed.")

    tf_spec = None
    params: dict = {}
    tf_run = None
    if hits:
        options = [f"{h.id} — {h.manifest.get('title', '')}" for h in hits]
        idx = 0 if non_interactive else _pick("Transformer", options, default=0)
        tf_spec = hits[idx]
        params = _collect_params(tf_spec, prof, non_interactive=non_interactive)
        sample = _prepare_sample(sniff.format, source, prof)
        tf_run = transformer_runner.run(tf_spec, sample, params)
        if tf_run.ok:
            console.print("[green]Transformer ran clean.[/green]")
        else:
            console.print(f"[red]Transformer issues:[/red] {tf_run.errors} / {tf_run.validation_errors}")
            if not non_interactive and not _yn("Continue despite failure?", default=False):
                sys.exit(3)

    # 7) Emit staged bblock
    bb_title = title or (f"Check-in from {Path(source).name}" if not sniff.is_url else f"Check-in from {source}")
    bb_id = _slug(name or bb_title)
    draft = bblock_writer.BBlockDraft(
        id=bb_id,
        title=bb_title,
        abstract=f"Auto-generated bblock from a {sniff.format} source.",
        tags=[sniff.format, "checkin"],
        standards=target.standards if target else [],
        depends_on=[target.id] if target else [],
        property_mappings=acks,
        source_property_mappings=acks,  # CLI doesn't resolve source→target names
        source_properties=[p.__dict__ for p in prof.properties],
        source_format=sniff.format,
        sample_feature=tf_run.output if tf_run and tf_run.ok else prof.sample,
        source_endpoint={"title": "source", "link": source} if sniff.is_url else {"title": "source", "local_path": source},
        transformer_kind="library" if tf_spec else "local",
        transformer=tf_spec,
        transformer_params=params,
    )
    src_out, tgt_out = bblock_writer.write_staged_pair(draft, overwrite=True)
    console.print(f"[bold green]Staged[/bold green] → {src_out}  (source)")
    console.print(f"[bold green]Staged[/bold green] → {tgt_out}  (target)")
    console.print("Next: review, then run [cyan]/validate-bblock _sources/_staging/%s[/cyan] and promote." % bb_id)


def _collect_params(spec: transformer_runner.TransformerSpec, prof: profile_mod.Profile, non_interactive: bool) -> dict:
    """Prompt for params listed in the transformer's params-schema, defaulting from the profile."""
    params: dict = {}
    schema = spec.params_schema
    required = schema.get("required", [])
    names = {p.name for p in prof.properties}

    def _leaf(name: str) -> str:
        """Return the last dotted/bracketed path segment, lowercased."""
        import re
        seg = re.split(r"[.\[\]]+", name)
        return next((s for s in reversed(seg) if s and not s.isdigit()), name).lower()

    def _first_match(targets: set[str]) -> str:
        return next((n for n in names if n.lower() in targets or _leaf(n) in targets), "")

    defaults = {
        "lon_field": _first_match({"lon", "long", "longitude", "decimallongitude", "x"}),
        "lat_field": _first_match({"lat", "latitude", "decimallatitude", "y"}),
        "time_field": _first_match({"time", "datetime", "date", "timestamp", "eventdate", "observedon"}),
        "id_field": _first_match({"id", "uuid", "identifier"}) or "id",
    }
    for key, psp in (schema.get("properties") or {}).items():
        default = defaults.get(key, psp.get("default", ""))
        if non_interactive:
            val = default
        else:
            val = input(f"  param {key} ({psp.get('description','')}) [{default}]: ").strip() or default
        if val != "" or key in required:
            params[key] = val
    return params


def _prepare_sample(fmt: str, source: str, prof: profile_mod.Profile):
    """Return a Python object the transformer can consume."""
    if fmt in {"csv", "tsv"}:
        text = _fetch_text_safe(source)
        if text is None:
            return []
        delim = "," if fmt == "csv" else "\t"
        rows = list(csv.DictReader(StringIO(text), delimiter=delim))
        return rows
    if fmt in {"json", "geojson"}:
        text = _fetch_text_safe(source)
        if text is None:
            return {}
        try:
            blob = json.loads(text)
        except json.JSONDecodeError:
            return {}
        if fmt == "geojson":
            return blob.get("features", [])
        return blob
    return prof.sample


def _fetch_text_safe(source: str) -> str | None:
    try:
        if source.startswith(("http://", "https://")):
            import httpx

            with httpx.Client(follow_redirects=True, timeout=30.0) as c:
                r = c.get(source)
                r.raise_for_status()
                return r.text
        return Path(source).expanduser().read_text()
    except Exception:  # noqa: BLE001
        return None


if __name__ == "__main__":  # pragma: no cover
    main()
