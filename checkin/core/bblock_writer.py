"""Emit staged building blocks under _sources/_staging/.

Conventions follow the building-block-generator agent:
- description.md  (Markdown, not description.json)
- schema.yaml     (YAML, not schema.json)
- examples.yaml   (example manifest)
- context.jsonld  with @id entries matching property names
- bblock.json     includes dependsOn, ldContext, tests
- transforms.yaml + transforms/transform.py  (OGC bblocks format)

The check-in tool always emits TWO building blocks per registration:

  {id}-source   Raw source data format.
                Schema mirrors the sniffed profile (nested).
                Context maps source field names → vocab URIs.
                No transformer, no base-bblock dependency.

  {id}          Canonical / transformed format.
                Schema uses transformer target paths (nested).
                Context maps output property names → same vocab URIs.
                dependsOn: [{id}-source, <chosen base bblock>]
                Contains transforms.yaml + transforms/transform.py.
"""
from __future__ import annotations

import json
import re
import shutil
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .. import STAGING_DIR
from .transformer_runner import TransformerSpec


@dataclass
class AcknowledgedMapping:
    property_name: str
    uri: str
    label: str = ""
    source: str = ""          # bblock id / OIM/<file.ttl>


@dataclass
class BBlockDraft:
    id: str                   # folder name, snake-or-kebab
    title: str
    abstract: str
    tags: list[str] = field(default_factory=list)
    standards: list[str] = field(default_factory=list)
    depends_on: list[str] = field(default_factory=list)
    # Context for the TARGET (output) bblock — keys are transformed property names
    property_mappings: list[AcknowledgedMapping] = field(default_factory=list)
    # Context for the SOURCE bblock — keys are raw source field names
    source_property_mappings: list[AcknowledgedMapping] = field(default_factory=list)
    # Raw profile properties for source bblock schema
    source_properties: list[dict[str, Any]] = field(default_factory=list)
    extra_properties: list[dict[str, Any]] = field(default_factory=list)
    sample_feature: Any = None          # transformer output example
    canonical_schema: dict[str, Any] | None = None
    source_endpoint: dict[str, Any] | None = None
    source_format: str = ""             # sniffed format: csv, json, netcdf, …
    transformer_kind: str = "library"   # "library" | "local"
    transformer: TransformerSpec | None = None
    transformer_params: dict[str, Any] | None = None
    local_transformer_files: dict[str, str] = field(default_factory=dict)
    custom_vocab_urls: list[str] = field(default_factory=list)
    vocab_source_versions: dict[str, str] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _to_yaml(obj: Any) -> str:
    """Serialize to YAML; fall back to JSON if PyYAML is absent."""
    try:
        import yaml
        return yaml.dump(obj, allow_unicode=True, sort_keys=False, default_flow_style=False)
    except ImportError:
        return json.dumps(obj, indent=2)


def _write(path: Path, content: str | bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, bytes):
        path.write_bytes(content)
    else:
        path.write_text(content)


def _identifier_prefix() -> str:
    try:
        import yaml
        cfg = STAGING_DIR.parent.parent / "bblocks-config.yaml"
        if cfg.exists():
            data = yaml.safe_load(cfg.read_text()) or {}
            return str(data.get("identifier-prefix") or "")
    except Exception:  # noqa: BLE001
        pass
    return ""


def _qualify(bblock_id: str) -> str:
    if not bblock_id or "." in bblock_id:
        return bblock_id
    prefix = _identifier_prefix()
    return f"{prefix}{bblock_id}" if prefix else bblock_id


def _qualify_list(ids: list[str]) -> list[str]:
    return [_qualify(x) for x in ids]


# ---------------------------------------------------------------------------
# Schema generators
# ---------------------------------------------------------------------------

_DTYPE_MAP: dict[str, str] = {
    "float64": "number", "float32": "number", "float": "number", "number": "number",
    "int64": "integer", "int32": "integer", "int": "integer", "integer": "integer",
    "bool": "boolean", "boolean": "boolean",
    "object": "string", "str": "string", "string": "string",
}

_PATH_SPLIT = re.compile(r"[.\[]")


def _path_parts(path: str) -> list[str]:
    return [p for p in _PATH_SPLIT.split(path.rstrip("]")) if p and not p.isdigit()]


def _schema_from_flat_properties(
    properties: list[dict[str, Any]], title: str
) -> dict[str, Any]:
    """Build a nested JSON Schema from a flat list of dotted-path profile properties."""
    root: dict[str, Any] = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": title,
        "type": "object",
        "properties": {},
    }
    for prop in properties:
        path = prop.get("name", "")
        dtype = _DTYPE_MAP.get(str(prop.get("dtype", "")).lower(), "string")
        parts = _path_parts(path)
        if not parts:
            continue
        node = root
        for i, part in enumerate(parts):
            last = (i == len(parts) - 1)
            node.setdefault("properties", {})
            if last:
                node["properties"].setdefault(part, {"type": dtype})
            else:
                if part not in node["properties"]:
                    node["properties"][part] = {"type": "object", "properties": {}}
                elif "properties" not in node["properties"][part]:
                    node["properties"][part]["properties"] = {}
                node = node["properties"][part]
    return root


def _schema_from_target_mappings(
    mappings: list[dict[str, Any]],
    extras: list[dict[str, Any]],
    title: str,
    base_bblock: str | None,
) -> dict[str, Any]:
    """Build a nested JSON Schema from transformer target paths + extras."""

    def _put(node: dict, parts: list[str], dtype: str) -> None:
        if not parts:
            return
        part = parts[0]
        if part.isdigit():
            return
        rest = [p for p in parts[1:] if not p.isdigit()]
        if not rest:
            node.setdefault(part, {"type": dtype})
        else:
            if part not in node:
                node[part] = {"type": "object", "properties": {}}
            elif "properties" not in node[part]:
                node[part]["properties"] = {}
            _put(node[part]["properties"], rest, dtype)

    props: dict[str, Any] = {}
    for m in mappings:
        tgt = m.get("target", "")
        if not tgt:
            continue
        parts = _path_parts(tgt)
        dtype = "object" if "expression" in m else (m.get("type") or "string")
        _put(props, parts, dtype)

    for e in extras:
        name = e.get("name")
        if not name:
            continue
        desc = (
            f"expression: {e['expression'][:100]}" if e.get("expression")
            else f"from source: {e.get('source', '')}"
        )
        props[name] = {"description": desc}

    schema: dict[str, Any] = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": title,
    }
    if base_bblock:
        schema["allOf"] = [{"$ref": f"bblocks://{_qualify(base_bblock)}"}]
    if props:
        schema["type"] = "object"
        schema["properties"] = props
    return schema


# ---------------------------------------------------------------------------
# Context builder
# ---------------------------------------------------------------------------

def _build_context(mappings: list[AcknowledgedMapping]) -> dict[str, Any]:
    ctx: dict[str, Any] = {}
    for m in mappings:
        if not m.uri:
            continue
        entry: dict[str, Any] = {"@id": m.uri}
        if m.label:
            entry["@label"] = m.label
        ctx[m.property_name] = entry
    ctx.setdefault("@vocab", "https://w3id.org/iliad/checkin/")
    return {"@context": ctx}


# ---------------------------------------------------------------------------
# Human-readable files (description.md, examples.yaml)
# ---------------------------------------------------------------------------

def _description_md_source(draft: BBlockDraft) -> str:
    lines = [f"# {draft.title} — source format", "", f"Source data representation for *{draft.title}*.", ""]
    if draft.abstract:
        lines += [draft.abstract, ""]

    if draft.source_endpoint:
        link = draft.source_endpoint.get("link") or draft.source_endpoint.get("local_path", "")
        lines += ["## Source", "", f"- **Format**: `{draft.source_format}`", f"- **URL / Path**: {link}", ""]

    if draft.source_properties:
        lines += ["## Properties", "", "| Property | Type | Sample values |",
                  "|----------|------|---------------|"]
        for p in draft.source_properties:
            name = p.get("name", "")
            dtype = p.get("dtype", "")
            samples = ", ".join(str(v) for v in (p.get("sample_values") or [])[:3])
            lines.append(f"| `{name}` | {dtype} | {samples} |")
        lines.append("")

    if draft.source_property_mappings:
        lines += ["## Vocabulary Mappings", "", "| Property | URI |", "|----------|-----|"]
        for m in draft.source_property_mappings:
            lines.append(f"| `{m.property_name}` | [{m.uri}]({m.uri}) |")
        lines.append("")

    lines += [f"*Generated by ILIAD check-in tool on {_utc_now_iso()[:10]}.*", ""]
    return "\n".join(lines)


def _description_md_target(draft: BBlockDraft) -> str:
    source_id = f"{draft.id}-source"
    base = draft.depends_on[0] if draft.depends_on else "—"
    tf_id = draft.transformer.id if draft.transformer else "custom"
    lines = [f"# {draft.title}", "", draft.abstract or "", ""]
    lines += [
        "## Overview", "",
        f"- **Source building block**: `{source_id}`",
        f"- **Base building block**: `{base}`",
        f"- **Transformer**: `{tf_id}`",
        f"- **Source format**: `{draft.source_format}`",
        "",
    ]

    mappings = (draft.transformer_params or {}).get("mappings") or []
    if mappings:
        lines += ["## Field Mappings", "", "| Source / Expression | Target | Type |",
                  "|---------------------|--------|------|"]
        for m in mappings:
            src = m.get("expression", f"`{m.get('source', '')}`")
            tgt = f"`{m.get('target', '')}`"
            typ = m.get("type", "")
            lines.append(f"| {src} | {tgt} | {typ} |")
        lines.append("")

    if draft.property_mappings:
        lines += ["## Vocabulary Mappings (output)", "", "| Property | URI |", "|----------|-----|"]
        for m in draft.property_mappings:
            lines.append(f"| `{m.property_name}` | [{m.uri}]({m.uri}) |")
        lines.append("")

    lines += [f"*Generated by ILIAD check-in tool on {_utc_now_iso()[:10]}.*", ""]
    return "\n".join(lines)


def _examples_yaml(filename: str, media_type: str, title: str = "Sample") -> str:
    return f"- title: {title}\n  content: examples/{filename}\n  mediaType: {media_type}\n"


# ---------------------------------------------------------------------------
# OGC transforms.yaml + transform.py generation
# ---------------------------------------------------------------------------

_FORMAT_MEDIA_TYPE: dict[str, str] = {
    "csv": "text/csv", "tsv": "text/tab-separated-values",
    "json": "application/json", "geojson": "application/geo+json",
    "netcdf": "application/x-netcdf", "geoparquet": "application/x-parquet",
    "ogc-wfs": "application/json", "ogc-wms": "application/json",
    "ogc-edr": "application/json", "opendap": "application/json",
}

_TARGET_MEDIA_TYPE: dict[str, str] = {
    "json-to-nested-json": "application/geo+json",
    "json-to-json-feature": "application/geo+json",
    "csv-to-stac-item": "application/json",
    "json-to-geoparquet": "application/x-parquet",
    "netcdf-structure-to-json": "application/json",
}

_ENGINE_PY = (
    Path(__file__).parent.parent / "transformers" / "json-to-nested-json" / "transform.py"
).read_text()


def _qualify_tf_params(params: dict[str, Any] | None) -> dict[str, Any]:
    out = dict(params or {})
    if "target_bblock" in out and out["target_bblock"]:
        out["target_bblock"] = _qualify(str(out["target_bblock"]))
    return out


def _transforms_yaml(draft: BBlockDraft) -> str:
    tf_id = draft.transformer.id if draft.transformer else "mapping-transform"
    slug = re.sub(r"[^a-z0-9]+", "-", tf_id.lower()).strip("-")
    in_mt = _FORMAT_MEDIA_TYPE.get(draft.source_format, "application/json")
    out_mt = _TARGET_MEDIA_TYPE.get(tf_id, "application/json")
    src_id = _qualify(f"{draft.id}-source")
    base_ids = _qualify_list(draft.depends_on)
    profiles = "\n".join(f"        - bblocks://{b}" for b in [src_id] + base_ids)
    desc_src = draft.source_format or "source"
    desc_tgt = draft.depends_on[0] if draft.depends_on else draft.id
    return (
        "transforms:\n"
        f"  - id: {slug}\n"
        f"    description: |\n"
        f"      Map {desc_src} fields to {desc_tgt} structure.\n"
        f"      Generated by ILIAD check-in tool.\n"
        f"    type: python\n"
        f"    inputs:\n"
        f"      mediaTypes:\n"
        f"        - {in_mt}\n"
        f"    outputs:\n"
        f"      mediaTypes:\n"
        f"        - {out_mt}\n"
        f"      profiles:\n"
        f"{profiles}\n"
        f"    ref: transforms/transform.py\n"
    )


def _transform_py(draft: BBlockDraft) -> str:
    params = _qualify_tf_params(draft.transformer_params)
    mappings = params.get("mappings", [])
    template = params.get("target_template", {})
    passthrough = params.get("passthrough_extras", False)
    tf_id = draft.transformer.id if draft.transformer else "json-to-nested-json"
    base = draft.depends_on[0] if draft.depends_on else draft.id

    header = f'''\
"""OGC bblocks Python transform — generated by ILIAD check-in tool.

Source format : {draft.source_format or 'unknown'}
Source bblock : {_qualify(draft.id + "-source")}
Target bblock : {base}
Transformer   : {tf_id}
Generated     : {_utc_now_iso()}

OGC bblocks transform interface
  input_data  — provided by the postprocessor (list of records or single dict)
  output_data — read back by the postprocessor
"""
'''
    config = f"""\
# ---- Mapping configuration --------------------------------------------------
MAPPINGS = {json.dumps(mappings, indent=2)}
TARGET_TEMPLATE = {json.dumps(template, indent=2)}
PASSTHROUGH_EXTRAS = {repr(passthrough)}

"""
    engine = _ENGINE_PY
    if engine.startswith('"""') or engine.startswith("'''"):
        q = '"""' if engine.startswith('"""') else "'''"
        end = engine.index(q, 3) + 3
        engine = engine[end:].lstrip("\n")

    entry = """\

# ---- OGC bblocks transform entry point -------------------------------------
_params = {
    "mappings": MAPPINGS,
    "target_template": TARGET_TEMPLATE,
    "passthrough_extras": PASSTHROUGH_EXTRAS,
}
output_data = transform(input_data, _params)
"""
    return header + config + engine + entry


def _transforms_assets(draft: BBlockDraft) -> dict[str, str]:
    """Return bblock-root-relative path → content for all transform assets."""
    if not draft.transformer and not draft.local_transformer_files:
        return {}
    assets: dict[str, str] = {}
    if draft.local_transformer_files:
        for name, body in draft.local_transformer_files.items():
            assets[f"transforms/{name}"] = body
        assets["transforms.yaml"] = _transforms_yaml(draft)
        return assets
    assets["transforms.yaml"] = _transforms_yaml(draft)
    assets["transforms/transform.py"] = _transform_py(draft)
    assets["transforms/mapping.json"] = json.dumps(_qualify_tf_params(draft.transformer_params), indent=2)
    return assets


# ---------------------------------------------------------------------------
# Custom vocabulary stub
# ---------------------------------------------------------------------------

def _write_custom_vocab_stub(url: str, staging_root: Path) -> None:
    slug = re.sub(r"[^a-z0-9]+", "-", url.lower().split("://", 1)[-1]).strip("-")[:48]
    target = staging_root / f"vocab-{slug}"
    target.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    meta = {
        "name": f"Custom vocabulary: {url}",
        "abstract": f"Schema-less building block referencing an external vocabulary at {url}",
        "status": "under-development",
        "itemClass": "ontology",
        "register": "ogc-incubator",
        "dateTimeAddition": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "dateOfLastChange": now.strftime("%Y-%m-%d"),
        "ontology": url,
        "tags": ["vocabulary", "ontology", "checkin"],
        "scope": "dev",
        "sources": [{"title": "Vocabulary source", "link": url}],
    }
    (target / "bblock.json").write_text(json.dumps(meta, indent=2))


# ---------------------------------------------------------------------------
# bblock.json builder (shared fields)
# ---------------------------------------------------------------------------

def _bblock_json(
    draft_id: str,
    title: str,
    abstract: str,
    tags: list[str],
    depends_on: list[str],
    source_endpoint: dict[str, Any] | None,
    standards: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "name": title,
        "version": "0.1.0",
        "dateTimeAddition": _utc_now_iso(),
        "status": "under-development",
        "itemClass": "schema",
        "register": "ogc-incubator",
        "dateOfLastChange": _utc_now_iso()[:10],
        "abstract": abstract,
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "tags": tags,
        "ldContext": "context.jsonld",
        "tests": "tests/test.yaml",
        "dependsOn": _qualify_list(depends_on),
        "standards": standards or [],
        "shaclRules": [],
        "sources": [source_endpoint] if source_endpoint else [],
        "scope": "dev",
    }


# ---------------------------------------------------------------------------
# Synthetic source example from profile properties
# ---------------------------------------------------------------------------

def _synthetic_example(source_properties: list[dict[str, Any]]) -> dict[str, Any] | None:
    example: dict[str, Any] = {}
    for p in source_properties:
        vals = p.get("sample_values") or []
        if not vals:
            continue
        parts = _path_parts(p.get("name", ""))
        if not parts:
            continue
        node = example
        for i, part in enumerate(parts):
            if i == len(parts) - 1:
                if isinstance(node, dict):
                    node[part] = vals[0]
            else:
                if not isinstance(node, dict):
                    break
                existing = node.get(part)
                if not isinstance(existing, dict):
                    node[part] = {}
                node = node[part]
    return example or None


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def write_staged_pair(
    draft: BBlockDraft,
    staging_root: Path | None = None,
    overwrite: bool = False,
) -> tuple[Path, Path]:
    """Write two complementary staged bblocks.

    Returns ``(source_path, target_path)``.
    """
    root = staging_root or STAGING_DIR
    source_id = f"{draft.id}-source"

    # ---- 1. Source bblock ---------------------------------------------------
    src_dir = root / source_id
    if src_dir.exists():
        if not overwrite:
            raise FileExistsError(f"{src_dir} already exists")
        shutil.rmtree(src_dir)
    src_dir.mkdir(parents=True)

    src_schema = _schema_from_flat_properties(
        draft.source_properties,
        f"{draft.title} — source format",
    )
    src_abstract = (
        f"Source data format for {draft.title}. "
        f"Represents the raw {draft.source_format} payload before transformation."
    )
    _write(src_dir / "bblock.json", json.dumps(
        _bblock_json(
            source_id,
            f"{draft.title} — source",
            src_abstract,
            tags=[draft.source_format, "source", "checkin"] + draft.tags,
            depends_on=[],
            source_endpoint=draft.source_endpoint,
        ), indent=2,
    ))
    _write(src_dir / "context.jsonld",
           json.dumps(_build_context(draft.source_property_mappings), indent=2))
    _write(src_dir / "schema.yaml", _to_yaml(src_schema))
    _write(src_dir / "description.md", _description_md_source(draft))
    _write(src_dir / "tests" / "test.yaml", "# Test suite scaffolded by check-in tool\n")

    src_example = _synthetic_example(draft.source_properties)
    if src_example:
        src_mt = _FORMAT_MEDIA_TYPE.get(draft.source_format, "application/json")
        _write(src_dir / "examples" / "sample.json", json.dumps(src_example, indent=2))
        _write(src_dir / "examples.yaml", _examples_yaml("sample.json", src_mt))

    # ---- 2. Target bblock ---------------------------------------------------
    tgt_dir = root / draft.id
    if tgt_dir.exists():
        if not overwrite:
            raise FileExistsError(f"{tgt_dir} already exists")
        shutil.rmtree(tgt_dir)
    tgt_dir.mkdir(parents=True)

    tf_mappings = (draft.transformer_params or {}).get("mappings") or []
    tgt_schema = _schema_from_target_mappings(
        tf_mappings,
        draft.extra_properties,
        draft.title,
        draft.depends_on[0] if draft.depends_on else None,
    )
    # dependsOn: source bblock first, then the chosen base bblock
    tgt_depends = [source_id] + list(draft.depends_on)

    _write(tgt_dir / "bblock.json", json.dumps(
        _bblock_json(
            draft.id,
            draft.title,
            draft.abstract,
            tags=draft.tags,
            depends_on=tgt_depends,
            source_endpoint=draft.source_endpoint,
            standards=draft.standards,
        ), indent=2,
    ))
    _write(tgt_dir / "context.jsonld",
           json.dumps(_build_context(draft.property_mappings), indent=2))
    _write(tgt_dir / "schema.yaml", _to_yaml(tgt_schema))
    _write(tgt_dir / "description.md", _description_md_target(draft))
    _write(tgt_dir / "tests" / "test.yaml", "# Test suite scaffolded by check-in tool\n")

    if draft.sample_feature is not None:
        out_mt = _TARGET_MEDIA_TYPE.get(
            draft.transformer.id if draft.transformer else "",
            "application/geo+json",
        )
        ext = "geojson" if "geo+json" in out_mt else "json"
        sample_name = f"sample.{ext}"
        _write(tgt_dir / "examples" / sample_name,
               json.dumps(draft.sample_feature, indent=2))
        _write(tgt_dir / "examples.yaml", _examples_yaml(sample_name, out_mt))

    for rel_path, body in _transforms_assets(draft).items():
        _write(tgt_dir / rel_path, body)

    # Custom vocab stubs (written once at the staging root level)
    for url in (draft.custom_vocab_urls or []):
        _write_custom_vocab_stub(url, root)

    return src_dir, tgt_dir


def promote(draft_id: str, staging_root: Path | None = None) -> list[Path]:
    """Move both the source and target staged bblocks into _sources/.

    Returns the two destination paths.  Raises FileNotFoundError /
    FileExistsError if either side is missing or already promoted.
    """
    sroot = staging_root or STAGING_DIR
    dest_root = sroot.parent
    promoted: list[Path] = []
    for bid in (f"{draft_id}-source", draft_id):
        src = sroot / bid
        if not src.exists():
            raise FileNotFoundError(f"no staged bblock at {src}")
        dest = dest_root / bid
        if dest.exists():
            raise FileExistsError(f"destination already exists: {dest}")
        shutil.move(str(src), str(dest))
        promoted.append(dest)
    return promoted
