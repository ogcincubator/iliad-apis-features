"""Index of existing building blocks under _sources/*.

Each entry exposes the fields needed for matching and rendering:
- id (folder name, stable)
- title / abstract / tags / standards
- property names extracted from schema.json|schema.yaml
- vocab URIs and terms from context.jsonld
- dependsOn list
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

import yaml

from .. import SOURCES_DIR


@dataclass
class TargetField:
    """A property slot in a target bblock, addressable via a dotted path."""

    path: str            # e.g. "properties.datetime", "geometry.coordinates[0]", "cube:variables.*.unit"
    type: str = ""       # json type hint ("string", "number", "integer", "boolean", "object", "array", "null")
    example: Any = None
    source: str = ""     # "schema" | "example:<file>"

    def as_dict(self) -> dict[str, Any]:
        return self.__dict__


@dataclass
class BBlockEntry:
    id: str
    path: Path
    title: str
    abstract: str
    tags: list[str] = field(default_factory=list)
    standards: list[str] = field(default_factory=list)
    depends_on: list[str] = field(default_factory=list)
    properties: list[str] = field(default_factory=list)       # flat list of leaf names (legacy)
    target_fields: list[TargetField] = field(default_factory=list)  # dotted-path target slots
    vocab_uris: dict[str, str] = field(default_factory=dict)  # term -> uri from context

    def as_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "path": str(self.path),
            "title": self.title,
            "abstract": self.abstract,
            "tags": self.tags,
            "standards": self.standards,
            "depends_on": self.depends_on,
            "properties": self.properties,
            "target_fields": [f.as_dict() for f in self.target_fields],
            "vocab_uris": self.vocab_uris,
        }


def _load_json(p: Path) -> dict[str, Any] | None:
    try:
        return json.loads(p.read_text())
    except Exception:  # noqa: BLE001
        return None


def _load_yaml(p: Path) -> dict[str, Any] | None:
    try:
        return yaml.safe_load(p.read_text())
    except Exception:  # noqa: BLE001
        return None


def _walk_schema_properties(node: Any, out: set[str]) -> None:
    if isinstance(node, dict):
        props = node.get("properties")
        if isinstance(props, dict):
            out.update(props.keys())
        for key in ("items", "allOf", "anyOf", "oneOf", "$defs", "definitions", "additionalProperties"):
            if key in node:
                _walk_schema_properties(node[key], out)
        # Also walk nested objects to catch deep schemas
        for v in node.values():
            if isinstance(v, (dict, list)):
                _walk_schema_properties(v, out)
    elif isinstance(node, list):
        for item in node:
            _walk_schema_properties(item, out)


def _extract_properties(bb_dir: Path) -> list[str]:
    out: set[str] = set()
    for name in ("schema.json", "schema.yaml"):
        p = bb_dir / name
        if not p.exists():
            continue
        data = _load_json(p) if name.endswith(".json") else _load_yaml(p)
        if data:
            _walk_schema_properties(data, out)
    return sorted(out)


def _walk_schema_target_fields(node: Any, prefix: str, out: list[TargetField]) -> None:
    """Walk a JSON schema and emit dotted paths for each property slot (best-effort)."""
    if not isinstance(node, dict):
        return
    t = node.get("type")
    props = node.get("properties") if isinstance(node.get("properties"), dict) else None
    if props:
        for k, sub in props.items():
            path = f"{prefix}.{k}" if prefix else k
            sub_type = sub.get("type", "") if isinstance(sub, dict) else ""
            if isinstance(sub_type, list):
                sub_type = next((x for x in sub_type if x != "null"), sub_type[0])
            out.append(TargetField(path=path, type=str(sub_type or ""), source="schema"))
            _walk_schema_target_fields(sub, path, out)
    items = node.get("items")
    if isinstance(items, dict):
        _walk_schema_target_fields(items, f"{prefix}[]" if prefix else "[]", out)
    for key in ("allOf", "anyOf", "oneOf"):
        for sub in node.get(key) or []:
            _walk_schema_target_fields(sub, prefix, out)
    # additionalProperties with a schema — rare
    ap = node.get("additionalProperties")
    if isinstance(ap, dict):
        _walk_schema_target_fields(ap, f"{prefix}.*" if prefix else "*", out)


def _walk_example_fields(node: Any, prefix: str, out: list[TargetField], source: str) -> None:
    """Walk a concrete example JSON and emit dotted paths for each leaf + intermediate."""
    if isinstance(node, dict):
        for k, v in node.items():
            path = f"{prefix}.{k}" if prefix else k
            out.append(TargetField(path=path, type=_py_type(v), example=_safe_example(v), source=source))
            _walk_example_fields(v, path, out, source)
    elif isinstance(node, list) and node:
        # Represent list shape with a single [0] child; skip scalar-only lists
        first = node[0]
        if isinstance(first, (dict, list)):
            _walk_example_fields(first, f"{prefix}[0]", out, source)
        else:
            out.append(TargetField(path=f"{prefix}[]", type=_py_type(first), example=first, source=source))


def _py_type(v: Any) -> str:
    if isinstance(v, bool):
        return "boolean"
    if isinstance(v, int):
        return "integer"
    if isinstance(v, float):
        return "number"
    if isinstance(v, list):
        return "array"
    if isinstance(v, dict):
        return "object"
    if v is None:
        return "null"
    return "string"


def _safe_example(v: Any) -> Any:
    if isinstance(v, (str, int, float, bool)) or v is None:
        return v
    return None


def _extract_target_fields(bb_dir: Path) -> list[TargetField]:
    fields: list[TargetField] = []
    # Schema-derived
    for name in ("schema.json", "schema.yaml"):
        p = bb_dir / name
        if p.exists():
            data = _load_json(p) if name.endswith(".json") else _load_yaml(p)
            if isinstance(data, dict):
                _walk_schema_target_fields(data, "", fields)
            break
    # Example-derived (covers $ref-only schemas like stac_multidim_data)
    ex_dir = bb_dir / "examples"
    if ex_dir.is_dir():
        for ex in sorted(ex_dir.glob("*.json")):
            data = _load_json(ex)
            if isinstance(data, (dict, list)):
                _walk_example_fields(data, "", fields, source=f"example:{ex.name}")
    # Dedupe by path, prefer schema origin
    best: dict[str, TargetField] = {}
    for f in fields:
        cur = best.get(f.path)
        if cur is None or (f.source == "schema" and cur.source != "schema"):
            best[f.path] = f
    return sorted(best.values(), key=lambda f: f.path)


def _extract_context_terms(bb_dir: Path) -> dict[str, str]:
    ctx_file = bb_dir / "context.jsonld"
    if not ctx_file.exists():
        return {}
    data = _load_json(ctx_file)
    if not isinstance(data, dict):
        return {}
    ctx = data.get("@context")
    out: dict[str, str] = {}

    def _ingest(obj: Any) -> None:
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k.startswith("@"):
                    continue
                if isinstance(v, str):
                    out[k] = v
                elif isinstance(v, dict) and "@id" in v:
                    out[k] = str(v["@id"])
        elif isinstance(obj, list):
            for item in obj:
                _ingest(item)

    _ingest(ctx)
    return out


def _entry_from_dir(bb_dir: Path) -> BBlockEntry | None:
    meta_file = bb_dir / "bblock.json"
    if not meta_file.exists():
        return None
    meta = _load_json(meta_file) or {}
    depends = meta.get("dependsOn") or []
    if isinstance(depends, str):
        depends = [depends]
    return BBlockEntry(
        id=bb_dir.name,
        path=bb_dir,
        title=str(meta.get("name") or bb_dir.name),
        abstract=str(meta.get("abstract") or ""),
        tags=list(meta.get("tags") or []),
        standards=list(meta.get("standards") or []),
        depends_on=[str(x) for x in depends],
        properties=_extract_properties(bb_dir),
        target_fields=_extract_target_fields(bb_dir),
        vocab_uris=_extract_context_terms(bb_dir),
    )


def load_index(sources_dir: Path | None = None) -> list[BBlockEntry]:
    root = sources_dir or SOURCES_DIR
    entries: list[BBlockEntry] = []
    for child in sorted(root.iterdir()):
        if not child.is_dir() or child.name.startswith((".", "_")):
            continue
        entry = _entry_from_dir(child)
        if entry:
            entries.append(entry)
    return entries


def iter_properties(entries: Iterable[BBlockEntry]) -> set[str]:
    acc: set[str] = set()
    for e in entries:
        acc.update(e.properties)
    return acc
