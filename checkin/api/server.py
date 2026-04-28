"""FastAPI backend for the check-in web wizard.

Session state is in-memory (dict keyed by session id). Replace with redis/sqlite
if you need multi-worker or restart-persistent wizards. Each wizard step has a
dedicated endpoint under `/api/`.
"""
from __future__ import annotations

import csv
import json
import re
import uuid
from io import StringIO
from pathlib import Path
from typing import Any

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import copy

from .. import STAGING_DIR
from ..core import (
    bblock_index,
    bblock_match,
    bblock_writer,
    profile as profile_mod,
    sniff as sniff_mod,
    transformer_runner,
    vocab_index,
    vocab_match,
)

app = FastAPI(title="ILIAD check-in", version="0.1.0")

_WEB_DIR = Path(__file__).resolve().parent.parent / "web"

app.mount("/static", StaticFiles(directory=_WEB_DIR / "static"), name="static")

# Sessions
_SESSIONS: dict[str, dict[str, Any]] = {}
# Lazy caches built on first use
_BB_INDEX: list[bblock_index.BBlockEntry] | None = None
_VOCAB: vocab_index.VocabIndex | None = None


def _bb() -> list[bblock_index.BBlockEntry]:
    global _BB_INDEX
    if _BB_INDEX is None:
        _BB_INDEX = bblock_index.load_index()
    return _BB_INDEX


def _vocab() -> vocab_index.VocabIndex:
    global _VOCAB
    if _VOCAB is None:
        _VOCAB = vocab_index.build_index()
    return _VOCAB


def _session_vocab(sess: dict[str, Any]) -> vocab_index.VocabIndex:
    if "vocab_index" not in sess:
        sess["vocab_index"] = copy.deepcopy(_vocab())
    return sess["vocab_index"]


def _load_declared_vocabularies(
    sess: dict[str, Any],
    entries: list[bblock_index.BBlockEntry],
) -> dict[str, list[str]]:
    loaded: list[str] = []
    failed: list[str] = []
    declared_urls: list[str] = []
    existing = {
        src.uri
        for src in sess.get("custom_vocab_sources", [])
        if getattr(src, "uri", "")
    }
    sess_vocab = None

    for entry in entries:
        for vocab_decl in entry.vocabularies:
            url = vocab_decl.get("url", "").strip()
            if not url.startswith(("http://", "https://")):
                continue
            if url in existing or url in declared_urls:
                continue
            declared_urls.append(url)
            try:
                sess_vocab = sess_vocab or _session_vocab(sess)
                source = vocab_index.add_custom_source(url, sess_vocab)
                sess.setdefault("custom_vocab_sources", []).append(source)
                existing.add(url)
                loaded.append(url)
            except Exception:
                failed.append(url)

    return {"loaded": loaded, "failed": failed}


@app.get("/", response_class=HTMLResponse)
def root() -> HTMLResponse:
    return HTMLResponse((_WEB_DIR / "index.html").read_text())


class RegisterIn(BaseModel):
    source: str


class RegisterOut(BaseModel):
    session_id: str
    sniff: dict
    profile: dict
    matches: list[dict]
    related: list[dict]


@app.post("/api/register", response_model=RegisterOut)
def register(body: RegisterIn) -> RegisterOut:
    s = sniff_mod.sniff(body.source)
    if s.format == "unknown":
        raise HTTPException(400, detail=f"cannot classify source: {s.hints}")
    p = profile_mod.profile(body.source, s.format)
    ranked = bblock_match.rank(p, _bb())  # all bblocks, sorted by score desc
    related = []  # populated after user picks a target
    sid = uuid.uuid4().hex[:12]
    _SESSIONS[sid] = {
        "source": body.source,
        "sniff": s.as_dict(),
        "profile": p.as_dict(),
        "matches": [
            {
                "id": m.entry.id,
                "title": m.entry.title,
                "score": m.score,
                "reason": m.reason,
                "matched_properties": m.matched_properties,
            }
            for m in ranked
        ],
    }
    return RegisterOut(
        session_id=sid,
        sniff=s.as_dict(),
        profile=p.as_dict(),
        matches=_SESSIONS[sid]["matches"],
        related=related,
    )


class ChooseBBlockIn(BaseModel):
    session_id: str
    bblock_id: str | None = None  # None => "generate new"


@app.post("/api/choose-bblock")
def choose_bblock(body: ChooseBBlockIn) -> dict:
    sess = _require_session(body.session_id)
    sess["chosen_bblock"] = body.bblock_id
    bb_index = _bb()
    related_entries = bblock_match.related(body.bblock_id, bb_index) if body.bblock_id else []
    sess["related"] = [{"id": r.id, "title": r.title} for r in related_entries]
    chosen_entry = next((entry for entry in bb_index if entry.id == body.bblock_id), None) if body.bblock_id else None
    vocab_load = _load_declared_vocabularies(
        sess,
        ([chosen_entry] if chosen_entry else []) + related_entries,
    )
    return {"ok": True, "related": sess["related"], "vocabularies": vocab_load}


@app.get("/api/vocab-sources/{session_id}")
def vocab_sources(session_id: str) -> dict:
    """Return ordered list of vocabulary sources for this session.

    Default order: local (0) → OIM (1) → imported (2) → custom (3).
    Session may override via /api/configure-vocab-sources.
    """
    sess = _require_session(session_id)
    vocab = _vocab()
    # Merge session custom sources into the global list
    session_sources = list(vocab.sources)
    for cs in sess.get("custom_vocab_sources", []):
        if not any(s.id == cs.id for s in session_sources):
            session_sources.append(cs)
    # Apply session priority override
    priority_order: list[str] = sess.get("vocab_source_priority", [])
    disabled: set[str] = set(sess.get("vocab_source_disabled", []))
    if priority_order:
        ordered = sorted(
            session_sources,
            key=lambda s: (
                priority_order.index(s.id) if s.id in priority_order else 9999,
                s.provenance_level,
            ),
        )
    else:
        ordered = sorted(session_sources, key=lambda s: (s.provenance_level, s.id))
    return {
        "sources": [
            {**s.as_dict(), "enabled": s.id not in disabled}
            for s in ordered
        ]
    }


class ConfigureVocabSourcesIn(BaseModel):
    session_id: str
    source_priority: list[str] = []   # ordered list of source ids (highest priority first)
    disabled: list[str] = []          # source ids to exclude from matching


@app.post("/api/configure-vocab-sources")
def configure_vocab_sources(body: ConfigureVocabSourcesIn) -> dict:
    sess = _require_session(body.session_id)
    sess["vocab_source_priority"] = body.source_priority
    sess["vocab_source_disabled"] = body.disabled
    return {"ok": True}


class AddCustomVocabIn(BaseModel):
    session_id: str
    url: str


@app.post("/api/add-custom-vocab")
def add_custom_vocab(body: AddCustomVocabIn) -> dict:
    """Fetch a TTL from *url*, add its terms to a session-local vocab index."""
    import re
    sess = _require_session(body.session_id)
    sess_vocab = _session_vocab(sess)
    try:
        source = vocab_index.add_custom_source(body.url, sess_vocab)
    except Exception as exc:
        raise HTTPException(400, f"failed to load vocabulary from {body.url}: {exc}") from exc
    sess.setdefault("custom_vocab_sources", []).append(source)
    slug = re.sub(r"[^a-z0-9]+", "-", body.url.lower().split("://", 1)[-1]).strip("-")[:48]
    return {
        "ok": True,
        "source": source.as_dict(),
        "suggested_bb_id": f"vocab-{slug}",
    }


@app.get("/api/vocab-search/{session_id}")
def vocab_search(session_id: str, q: str = "", limit: int = 200) -> dict:
    """Return all terms from enabled vocab sources, optionally filtered by *q*.

    Searches term name, label, and URI. Results are ordered by source priority
    then alphabetically by term. Intended for the browse-all popup in the UI.
    """
    sess = _require_session(session_id)
    vidx = sess.get("vocab_index") or _vocab()
    priority: list[str] = sess.get("vocab_source_priority") or []
    disabled: set[str] = set(sess.get("vocab_source_disabled") or [])
    q_lower = q.strip().lower()

    def _prio(source_id: str) -> int:
        try:
            return priority.index(source_id)
        except ValueError:
            return 9999

    seen_uris: set[str] = set()
    results: list[dict] = []
    # Iterate all unique terms in index order
    for term_str, terms in vidx.by_term.items():
        for t in terms:
            if t.source_id in disabled:
                continue
            if t.uri in seen_uris:
                continue
            if q_lower and not (
                q_lower in t.term.lower()
                or q_lower in (t.label or "").lower()
                or q_lower in t.uri.lower()
            ):
                continue
            seen_uris.add(t.uri)
            results.append({
                "term": t.term,
                "uri": t.uri,
                "label": t.label or t.term,
                "source": t.source,
                "source_id": t.source_id,
                "kind": t.kind,
                "_prio": _prio(t.source_id),
            })

    results.sort(key=lambda r: (r["_prio"], r["term"].lower()))
    for r in results:
        del r["_prio"]
    return {"terms": results[:limit], "total_matched": len(results)}


@app.get("/api/vocab-candidates/{session_id}")
def vocab_candidates(session_id: str) -> dict:
    sess = _require_session(session_id)
    profile = sess["profile"]
    props = [p["name"] for p in profile["properties"]]
    # Use session-local vocab index if one exists (has custom sources merged in)
    vidx = sess.get("vocab_index") or _vocab()
    priority = sess.get("vocab_source_priority") or None
    disabled = set(sess.get("vocab_source_disabled") or [])
    cands = vocab_match.match_properties(props, vidx, k=5,
                                         source_priority=priority,
                                         disabled_sources=disabled)
    return {p: [c.as_dict() for c in cs] for p, cs in cands.items()}


class AcknowledgeIn(BaseModel):
    session_id: str
    mappings: dict[str, dict[str, str]]   # property_name -> {uri, label, source}


@app.post("/api/acknowledge-vocab")
def acknowledge_vocab(body: AcknowledgeIn) -> dict:
    sess = _require_session(body.session_id)
    sess["acknowledged_vocab"] = body.mappings
    return {"ok": True, "count": len(body.mappings)}


class ExternalLookupIn(BaseModel):
    query: str


@app.post("/api/external-vocab")
def external_vocab(body: ExternalLookupIn) -> dict:
    return {"hints": vocab_match.external_hints(body.query)}


class TransformersOut(BaseModel):
    candidates: list[dict]
    target_output: str | None


@app.get("/api/transformers/{session_id}", response_model=TransformersOut)
def transformers(session_id: str) -> TransformersOut:
    sess = _require_session(session_id)
    fmt = sess["sniff"]["format"]
    target_out_hint = {
        "csv": "stac-item",
        "tsv": "stac-item",
        "json": "geojson",
        "geojson": "geojson",
    }.get(fmt)
    specs = transformer_runner.find_matching(fmt, target_out_hint)
    # json-to-nested-json is universally available; surface it too.
    all_specs = transformer_runner.load_library()
    nested = next((s for s in all_specs if s.id == "json-to-nested-json"), None)
    if nested and nested not in specs:
        specs.append(nested)
    return TransformersOut(
        candidates=[s.as_dict() for s in specs],
        target_output=target_out_hint,
    )


@app.get("/api/mapping-suggestion/{session_id}")
def mapping_suggestion(session_id: str) -> dict:
    """Return target-bblock fields, source fields, and a best-guess mapping.

    Also returns the set of source fields NOT covered by any suggestion, as
    ``extras`` — the user names them and maps them to vocabularies so they
    become additional properties on the generated bblock.
    """
    from rapidfuzz import fuzz

    sess = _require_session(session_id)
    target_bb_id = sess.get("chosen_bblock")
    target_fields: list[dict] = []
    if target_bb_id:
        target = next((e for e in _bb() if e.id == target_bb_id), None)
        if target:
            target_fields = [tf.as_dict() for tf in target.target_fields]

    source_fields = [
        {"path": p["name"], "type": p["dtype"], "sample": p["sample_values"]}
        for p in sess["profile"]["properties"]
    ]

    # Suggestions — exact then fuzzy on last-segment of each path
    def leaf(path: str) -> str:
        return re.sub(r"\[\d*\]$", "", path.rsplit(".", 1)[-1])

    suggestions: list[dict] = []
    used_sources: set[str] = set()
    tgt_leaves = {tf["path"]: leaf(tf["path"]).lower() for tf in target_fields}
    for src in source_fields:
        sleaf = leaf(src["path"]).lower()
        if not sleaf:
            continue
        best_path = ""
        best_score = 0
        for tpath, tleaf in tgt_leaves.items():
            if not tleaf:
                continue
            score = 100 if sleaf == tleaf else fuzz.token_set_ratio(sleaf, tleaf)
            if score > best_score:
                best_score = score
                best_path = tpath
        if best_score >= 80 and best_path:
            suggestions.append({"source": src["path"], "target": best_path, "confidence": best_score})
            used_sources.add(src["path"])

    extras = [s for s in source_fields if s["path"] not in used_sources]
    return {
        "target_bblock": target_bb_id,
        "target_fields": target_fields,
        "source_fields": source_fields,
        "suggestions": suggestions,
        "extras": extras,
    }


class ExtraProp(BaseModel):
    source: str = ""     # dotted path in source (empty when expression is set)
    expression: str = "" # expression template (alternative to source)
    name: str            # name in new bblock (user-editable)
    uri: str = ""        # selected vocab URI
    label: str = ""
    source_src: str = "" # bblock/ontology that defined the uri


class RunTransformerIn(BaseModel):
    session_id: str
    transformer_id: str
    params: dict[str, Any]


@app.post("/api/run-transformer")
def run_transformer(body: RunTransformerIn) -> dict:
    sess = _require_session(body.session_id)
    specs = transformer_runner.load_library()
    spec = next((s for s in specs if s.id == body.transformer_id), None)
    if spec is None:
        raise HTTPException(404, f"transformer {body.transformer_id} not found")
    sample = _prepare_sample(sess)
    result = transformer_runner.run(spec, sample, body.params)
    sess["transformer"] = {"id": spec.id, "params": body.params, "output": result.output}
    return {
        "ok": result.ok,
        "errors": result.errors,
        "validation_errors": result.validation_errors,
        "output_preview": _preview(result.output),
    }


class FinalizeIn(BaseModel):
    session_id: str
    bb_id: str
    title: str
    abstract: str = ""
    overwrite: bool = True
    extras: list[ExtraProp] = []   # user-named properties not in target bblock


@app.post("/api/finalize")
def finalize(body: FinalizeIn) -> dict:
    sess = _require_session(body.session_id)
    target_id = sess.get("chosen_bblock")
    target = next((e for e in _bb() if e.id == target_id), None) if target_id else None

    tf_state = sess.get("transformer") or {}
    tf_spec = None
    if tf_state.get("id"):
        specs = transformer_runner.load_library()
        tf_spec = next((s for s in specs if s.id == tf_state["id"]), None)

    # Build source-field → output-property-name lookup from the transformer mappings.
    # This lets us key context.jsonld by the transformed output name, not the raw source name.
    tf_mappings: list[dict] = (tf_state.get("params") or {}).get("mappings") or []

    def _output_leaf(path: str) -> str:
        seg = re.sub(r"\[\d*\]$", "", path.rsplit(".", 1)[-1])
        return seg

    def _is_structural(leaf: str) -> bool:
        # Numeric leaves (e.g. coordinates[0]) are positional, not semantic properties.
        return leaf.isdigit() or (len(leaf) <= 2 and leaf.lstrip("-").isdigit())

    # Map source path → output property leaf name.
    # For single-placeholder expressions (e.g. "${species_name}" → "species") also resolve.
    source_to_out: dict[str, str] = {}
    for m in tf_mappings:
        tgt = m.get("target", "")
        if not tgt:
            continue
        leaf = _output_leaf(tgt)
        if _is_structural(leaf):
            continue
        if "source" in m:
            source_to_out[m["source"]] = leaf
        elif "expression" in m:
            placeholders = re.findall(r"\$\{([^}]+)\}", m["expression"])
            if len(placeholders) == 1:
                source_to_out[placeholders[0]] = leaf

    # Build context mappings using transformed output names.
    ack = sess.get("acknowledged_vocab") or {}
    seen_out_names: set[str] = set()
    mappings: list[bblock_writer.AcknowledgedMapping] = []
    for src_name, info in ack.items():
        if not info.get("uri"):
            continue
        out_name = source_to_out.get(src_name, src_name)
        if out_name in seen_out_names:
            continue  # e.g. lon + lat both fold into geometry — keep first
        seen_out_names.add(out_name)
        mappings.append(
            bblock_writer.AcknowledgedMapping(
                property_name=out_name,
                uri=info["uri"],
                label=info.get("label", ""),
                source=info.get("source", ""),
            )
        )

    source_endpoint: dict[str, Any]
    source = sess["source"]
    source_endpoint = {"title": "source", "link": source} if sess["sniff"]["is_url"] else {
        "title": "source",
        "local_path": source,
    }

    # Add user-named extras as additional context + schema entries.
    extra_mappings = [
        bblock_writer.AcknowledgedMapping(
            property_name=e.name, uri=e.uri, label=e.label, source=e.source_src
        )
        for e in (body.extras or [])
        if e.name and e.uri
    ]

    extra_properties = [
        {
            "name": e.name,
            "source": e.source if e.source else None,
            "expression": e.expression if e.expression else None,
            "uri": e.uri,
        }
        for e in (body.extras or [])
    ]

    # Source bblock context: source field names → vocab URIs (pre-resolution)
    source_mappings = [
        bblock_writer.AcknowledgedMapping(
            property_name=src_name,
            uri=info.get("uri", ""),
            label=info.get("label", ""),
            source=info.get("source", ""),
        )
        for src_name, info in ack.items()
        if info.get("uri")
    ]

    # Vocab provenance metadata
    vidx = sess.get("vocab_index") or _vocab()
    vocab_versions = {s.id: f"{s.version} ({s.timestamp})" if s.version else s.timestamp
                      for s in vidx.sources if s.enabled}
    custom_vocab_urls = [cs.uri for cs in sess.get("custom_vocab_sources", [])]

    draft = bblock_writer.BBlockDraft(
        id=body.bb_id,
        title=body.title,
        abstract=body.abstract or f"Auto-generated bblock from a {sess['sniff']['format']} source.",
        tags=[sess["sniff"]["format"], "checkin"],
        standards=(target.standards if target else []),
        depends_on=([target.id] if target else []),
        property_mappings=mappings + extra_mappings,
        source_property_mappings=source_mappings,
        source_properties=sess["profile"].get("properties") or [],
        extra_properties=extra_properties,
        sample_feature=tf_state.get("output") or sess["profile"].get("sample"),
        source_endpoint=source_endpoint,
        source_format=sess["sniff"]["format"],
        transformer_kind="library" if tf_spec else "local",
        transformer=tf_spec,
        transformer_params=tf_state.get("params") or {},
        custom_vocab_urls=custom_vocab_urls,
        vocab_source_versions=vocab_versions,
    )
    src_path, tgt_path = bblock_writer.write_staged_pair(draft, overwrite=body.overwrite)
    sess["staged_source_id"] = f"{body.bb_id}-source"
    sess["staged_target_id"] = body.bb_id
    return {
        "ok": True,
        "source_id": f"{body.bb_id}-source",
        "target_id": body.bb_id,
        "source_path": str(src_path),
        "target_path": str(tgt_path),
    }


class PromoteIn(BaseModel):
    session_id: str
    bb_id: str


@app.post("/api/promote")
def promote(body: PromoteIn) -> dict:
    sess = _require_session(body.session_id)
    try:
        promoted = bblock_writer.promote(body.bb_id)
    except (FileNotFoundError, FileExistsError) as exc:
        raise HTTPException(400, str(exc)) from exc
    sess["promoted_paths"] = [str(p) for p in promoted]
    return {
        "ok": True,
        "promoted": [str(p) for p in promoted],
    }


# ---- helpers ----


def _require_session(sid: str) -> dict:
    sess = _SESSIONS.get(sid)
    if sess is None:
        raise HTTPException(404, f"unknown session {sid}")
    return sess


def _prepare_sample(sess: dict) -> Any:
    fmt = sess["sniff"]["format"]
    source = sess["source"]
    text = _fetch_text_safe(source)
    if fmt in {"csv", "tsv"} and text is not None:
        delim = "," if fmt == "csv" else "\t"
        return list(csv.DictReader(StringIO(text), delimiter=delim))
    if fmt in {"json", "geojson"} and text is not None:
        try:
            blob = json.loads(text)
        except json.JSONDecodeError:
            return {}
        if fmt == "geojson":
            return blob.get("features", [])
        return blob
    return sess["profile"].get("sample")


def _fetch_text_safe(source: str) -> str | None:
    try:
        if source.startswith(("http://", "https://")):
            with httpx.Client(follow_redirects=True, timeout=30.0) as c:
                r = c.get(source)
                r.raise_for_status()
                return r.text
        return Path(source).expanduser().read_text()
    except Exception:  # noqa: BLE001
        return None


def _preview(value: Any, limit: int = 3) -> Any:
    if isinstance(value, list):
        return value[:limit]
    return value


# ---- entrypoint ----


def main() -> None:  # pragma: no cover
    import uvicorn

    uvicorn.run("checkin.api.server:app", host="127.0.0.1", port=8000, reload=False)


if __name__ == "__main__":  # pragma: no cover
    main()
