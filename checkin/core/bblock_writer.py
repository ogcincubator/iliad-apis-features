"""Emit a staged building block under _sources/_staging/<name>/.

Conventions (see CLAUDE.md):
- description.json (not README.md)
- schema.json OR schema.yaml (we write .json)
- context.jsonld with @id entries matching property names
- bblock.json includes `dependsOn`, `standards`, `tests`, `ldContext`
- examples/ and tests/ directories
- transforms/ (optional) — bblock-local transformer(s)
"""
from __future__ import annotations

import json
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
    id: str                             # folder name, snake-or-kebab
    title: str
    abstract: str
    tags: list[str] = field(default_factory=list)
    standards: list[str] = field(default_factory=list)
    depends_on: list[str] = field(default_factory=list)
    property_mappings: list[AcknowledgedMapping] = field(default_factory=list)
    extra_properties: list[dict[str, Any]] = field(default_factory=list)  # {name, source, uri}
    sample_feature: Any = None          # example GeoJSON feature or dict
    canonical_schema: dict[str, Any] | None = None
    source_endpoint: dict[str, Any] | None = None
    transformer_kind: str = "library"   # "library" | "local"
    transformer: TransformerSpec | None = None
    transformer_params: dict[str, Any] | None = None
    local_transformer_files: dict[str, str] = field(default_factory=dict)  # name -> text


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _build_context(draft: BBlockDraft) -> dict[str, Any]:
    context: dict[str, Any] = {}
    for m in draft.property_mappings:
        context[m.property_name] = {"@id": m.uri}
        if m.label:
            context[m.property_name]["@label"] = m.label
    # Minimal conventional bindings
    context.setdefault("@vocab", "https://w3id.org/iliad/checkin/")
    return {"@context": context}


def _compose_schema(draft: BBlockDraft) -> dict[str, Any] | None:
    """Compose a schema.json that extends the target bblock with the user's extras.

    If the user provided an inline canonical_schema we respect it verbatim. Otherwise:
      - If depends_on includes a single bblock AND extras are present, generate an
        `allOf` that references the target bblock's schema plus a local extension
        adding the extras as properties.
      - If extras alone, emit a minimal standalone schema.
      - If neither, return None.
    """
    if draft.canonical_schema is not None:
        return draft.canonical_schema
    extras = draft.extra_properties or []
    if not extras and not draft.depends_on:
        return None
    extras_schema = {
        "type": "object",
        "properties": {
            e["name"]: {"type": "string", "description": f"from source path {e['source']}"}
            for e in extras
            if e.get("name")
        },
    }
    if not extras:
        return None
    if draft.depends_on:
        parent = draft.depends_on[0]
        return {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": draft.title,
            "description": f"Extension of {parent} with extras contributed by check-in.",
            "allOf": [
                {"$ref": f"bblocks://{parent}"},
                extras_schema,
            ],
        }
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": draft.title,
        **extras_schema,
    }


def _build_bblock_json(draft: BBlockDraft) -> dict[str, Any]:
    return {
        "name": draft.title,
        "version": "0.1.0",
        "dateTimeAddition": _utc_now_iso(),
        "status": "under-development",
        "itemClass": "schema",
        "register": "ogc-incubator",
        "dateOfLastChange": _utc_now_iso()[:10],
        "abstract": draft.abstract,
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "tags": draft.tags,
        "authors": [
            {
                "name": "ILIAD check-in tool",
                "organization": "ILIAD",
                "email": "info@example.com",
            }
        ],
        "standards": draft.standards,
        "ldContext": "context.jsonld",
        "tests": "tests/test.yaml",
        "dependsOn": draft.depends_on,
        "shaclRules": [],
        "sources": [draft.source_endpoint] if draft.source_endpoint else [],
        "scope": "dev",
    }


def _build_description(draft: BBlockDraft) -> dict[str, Any]:
    return {
        "title": draft.title,
        "abstract": draft.abstract,
        "source": draft.source_endpoint or {},
        "transformer": {
            "kind": draft.transformer_kind,
            "id": draft.transformer.id if draft.transformer else None,
            "params": draft.transformer_params or {},
        },
        "property_mappings": [m.__dict__ for m in draft.property_mappings],
    }


def _transforms_dir_assets(draft: BBlockDraft) -> dict[str, str]:
    """Files to write under transforms/."""
    if draft.transformer_kind == "library" and draft.transformer:
        # Reference — not a copy of code. Canonical schema is inherited via canonical-ref.
        ref = {
            "transformer_id": draft.transformer.id,
            "input": draft.transformer.input_format,
            "output": draft.transformer.output_format,
            "canonical-ref": draft.transformer.canonical_ref or f"bblock://{draft.id}",
            "params": draft.transformer_params or {},
        }
        return {"transform.ref.json": json.dumps(ref, indent=2)}
    # local transformer — user supplied files verbatim
    return dict(draft.local_transformer_files)


def _write(path: Path, content: str | bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, bytes):
        path.write_bytes(content)
    else:
        path.write_text(content)


def write_staged(draft: BBlockDraft, staging_root: Path | None = None, overwrite: bool = False) -> Path:
    root = staging_root or STAGING_DIR
    target = root / draft.id
    if target.exists():
        if not overwrite:
            raise FileExistsError(f"{target} exists; pass overwrite=True to replace")
        shutil.rmtree(target)
    target.mkdir(parents=True)

    _write(target / "bblock.json", json.dumps(_build_bblock_json(draft), indent=2))
    _write(target / "context.jsonld", json.dumps(_build_context(draft), indent=2))
    _write(target / "description.json", json.dumps(_build_description(draft), indent=2))

    schema = _compose_schema(draft)
    if schema is not None:
        _write(target / "schema.json", json.dumps(schema, indent=2))

    # Example
    if draft.sample_feature is not None:
        _write(target / "examples" / "sample.geojson", json.dumps(draft.sample_feature, indent=2))

    # Tests — minimal shell matching other bblocks
    test_yaml = "# Test suite scaffolded by check-in tool\n"
    _write(target / "tests" / "test.yaml", test_yaml)

    for name, body in _transforms_dir_assets(draft).items():
        _write(target / "transforms" / name, body)

    return target


def promote(draft_id: str, staging_root: Path | None = None) -> Path:
    """Move a staged bblock into _sources/<id>/ (one level up from staging)."""
    sroot = staging_root or STAGING_DIR
    src = sroot / draft_id
    if not src.exists():
        raise FileNotFoundError(f"no staged bblock at {src}")
    dest = sroot.parent / draft_id
    if dest.exists():
        raise FileExistsError(f"destination already exists: {dest}")
    shutil.move(str(src), str(dest))
    return dest
