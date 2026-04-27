"""Execute a transformer and validate the output against its canonical schema.

A transformer is a directory with:
    transformer.json
    canonical.schema.json      (or canonical-ref pointing to a bblock)
    transform.py               (exposes `def transform(input, params) -> output`)
    tests/ (optional)

The runner is intentionally minimal: it imports transform.py by path, calls
``transform(input_obj, params)``, captures exceptions, and validates the result
with jsonschema if a canonical schema is available.
"""
from __future__ import annotations

import importlib.util
import json
import sys
import traceback
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import jsonschema

from .. import SOURCES_DIR, TRANSFORMERS_DIR


@dataclass
class TransformerSpec:
    id: str
    path: Path
    manifest: dict[str, Any]

    @property
    def input_format(self) -> str:
        return self.manifest.get("input", "")

    @property
    def output_format(self) -> str:
        return self.manifest.get("output", "")

    @property
    def canonical_ref(self) -> str:
        return self.manifest.get("canonical-ref", "")

    @property
    def depends_on(self) -> list[str]:
        d = self.manifest.get("dependsOn") or []
        return [str(x) for x in d]

    @property
    def params_schema(self) -> dict[str, Any]:
        return self.manifest.get("params-schema") or {}

    def as_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "path": str(self.path),
            "input": self.input_format,
            "output": self.output_format,
            "canonical-ref": self.canonical_ref,
            "dependsOn": self.depends_on,
        }


@dataclass
class RunResult:
    ok: bool
    output: Any = None
    errors: list[str] = field(default_factory=list)
    validation_errors: list[str] = field(default_factory=list)


def load_library(lib_dir: Path | None = None) -> list[TransformerSpec]:
    root = lib_dir or TRANSFORMERS_DIR
    specs: list[TransformerSpec] = []
    if not root.exists():
        return specs
    for child in sorted(root.iterdir()):
        if not child.is_dir() or child.name.startswith((".", "_")):
            continue
        manifest_path = child / "transformer.json"
        if not manifest_path.exists():
            continue
        try:
            manifest = json.loads(manifest_path.read_text())
        except Exception:  # noqa: BLE001
            continue
        specs.append(TransformerSpec(id=manifest.get("id") or child.name, path=child, manifest=manifest))
    return specs


def find_matching(
    input_format: str,
    target_output: str | None,
    lib: list[TransformerSpec] | None = None,
) -> list[TransformerSpec]:
    specs = lib or load_library()
    hits: list[TransformerSpec] = []
    for s in specs:
        if s.input_format and s.input_format != input_format:
            continue
        if target_output and s.output_format and s.output_format != target_output:
            continue
        hits.append(s)
    return hits


def _import_transform(spec: TransformerSpec) -> Any:
    tfile = spec.path / "transform.py"
    if not tfile.exists():
        raise FileNotFoundError(f"transform.py missing in {spec.path}")
    mod_name = f"_iliad_tf_{spec.id.replace('-', '_')}"
    module_spec = importlib.util.spec_from_file_location(mod_name, tfile)
    if module_spec is None or module_spec.loader is None:
        raise ImportError(f"cannot import {tfile}")
    module = importlib.util.module_from_spec(module_spec)
    sys.modules[mod_name] = module
    module_spec.loader.exec_module(module)
    if not hasattr(module, "transform"):
        raise AttributeError(f"{tfile} has no transform(input, params) function")
    return module.transform


def _resolve_bblock_schema(bblock_id: str) -> dict[str, Any] | None:
    import yaml  # local import to keep top-level deps minimal

    bb_dir = SOURCES_DIR / bblock_id
    if not bb_dir.exists():
        return None
    for name in ("schema.json", "schema.yaml"):
        p = bb_dir / name
        if p.exists():
            try:
                raw = p.read_text()
                return json.loads(raw) if name.endswith(".json") else yaml.safe_load(raw)
            except Exception:  # noqa: BLE001
                return None
    return None


def _resolve_canonical_schema(spec: TransformerSpec, override_bblock: str | None = None) -> dict[str, Any] | None:
    if override_bblock:
        schema = _resolve_bblock_schema(override_bblock)
        if schema is not None:
            return schema
    ref = spec.canonical_ref
    # Prefer sibling file
    local = spec.path / "canonical.schema.json"
    if local.exists():
        return json.loads(local.read_text())
    if not ref:
        return None
    # bblock reference: bblock://<id> or just an id like "macroobservation"
    if ref.startswith("bblock://"):
        ref = ref[len("bblock://"):]
    schema = _resolve_bblock_schema(ref)
    return schema


def run(spec: TransformerSpec, input_obj: Any, params: dict[str, Any] | None = None) -> RunResult:
    params = params or {}
    try:
        fn = _import_transform(spec)
    except Exception as exc:  # noqa: BLE001
        return RunResult(ok=False, errors=[f"load failed: {exc}", traceback.format_exc()])
    try:
        out = fn(input_obj, params)
    except Exception as exc:  # noqa: BLE001
        return RunResult(ok=False, errors=[f"transform raised: {exc}", traceback.format_exc()])

    schema = _resolve_canonical_schema(spec, override_bblock=(params or {}).get("target_bblock"))
    if schema is None:
        return RunResult(ok=True, output=out, errors=["no canonical schema available to validate against"])
    # JSON-Schemas with unresolvable $ref (e.g. bblocks://...) blow up Draft2020Validator — use a permissive resolver.
    if schema.get("$ref", "").startswith(("bblocks://", "bblock://")):
        schema = {**schema, "$ref": None}  # type: ignore[assignment]
        schema.pop("$ref")
    validator = jsonschema.Draft202012Validator(schema)
    # If the canonical schema describes a single object but the transformer produced a list,
    # validate each item individually. (Transformers accept list-or-single and mirror that shape.)
    items = out if isinstance(out, list) and schema.get("type") == "object" else [out]
    errors: list[str] = []
    for i, item in enumerate(items):
        prefix = f"[{i}]" if isinstance(out, list) else ""
        for e in validator.iter_errors(item):
            errors.append(f"{prefix}{'/'.join(str(p) for p in e.absolute_path)}: {e.message}")
    return RunResult(ok=not errors, output=out, validation_errors=errors)
