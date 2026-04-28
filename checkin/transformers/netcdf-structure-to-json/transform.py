"""Reorganize NetCDF structure into templated JSON.

Accepted inputs:
- a pre-built structure dict containing metadata / dimensions / variables
- a filesystem path to a NetCDF file
- an in-memory xarray Dataset

Template features:
- "${path}" or strings containing "${path}" placeholders
- {"$value": "path"} for direct extraction
- {"$for": "path", "template": {...}} for collection mapping
"""
from __future__ import annotations

import json
import re
from os import PathLike
from pathlib import Path
from typing import Any

_EXPR_RE = re.compile(r"\$\{([^}]+)\}")


def transform(input_obj: Any, params: dict) -> Any:
    template = params.get("template")
    if template is None:
        raise ValueError("missing required param: template")
    structure = _to_structure(input_obj)
    context = {"root": structure, **structure}
    return _expand(template, context)


def _to_structure(input_obj: Any) -> dict[str, Any]:
    if isinstance(input_obj, dict) and {"metadata", "dimensions", "variables"} <= set(input_obj.keys()):
        return input_obj
    if isinstance(input_obj, (str, PathLike)):
        try:
            import xarray as xr
        except ImportError as exc:  # pragma: no cover
            raise RuntimeError(f"xarray not installed: {exc}") from exc
        ds = xr.open_dataset(Path(input_obj).expanduser())
        try:
            return _dataset_to_structure(ds)
        finally:
            ds.close()
    if hasattr(input_obj, "dims") and hasattr(input_obj, "data_vars") and hasattr(input_obj, "coords"):
        return _dataset_to_structure(input_obj)
    raise TypeError(f"unsupported input type: {type(input_obj).__name__}")


def _dataset_to_structure(ds: Any) -> dict[str, Any]:
    metadata = {str(k): _json_safe(v) for k, v in (ds.attrs or {}).items()}
    dimensions: list[dict[str, Any]] = []
    dimensions_by_name: dict[str, dict[str, Any]] = {}
    for name, size in ds.sizes.items():
        coord = ds.coords.get(name)
        entry = {
            "name": str(name),
            "size": int(size),
            "dtype": str(getattr(coord, "dtype", "")),
            "units": str((getattr(coord, "attrs", {}) or {}).get("units", "")),
            "attrs": {str(k): _json_safe(v) for k, v in ((getattr(coord, "attrs", {}) or {}).items())},
        }
        dimensions.append(entry)
        dimensions_by_name[entry["name"]] = entry

    coordinates = [_variable_entry(name, coord, kind="coordinate") for name, coord in ds.coords.items()]
    coordinates_by_name = {entry["name"]: entry for entry in coordinates}
    variables = [_variable_entry(name, var, kind="data") for name, var in ds.data_vars.items()]
    variables_by_name = {entry["name"]: entry for entry in variables}

    structure = {
        "metadata": metadata,
        "dimensions": dimensions,
        "dimensions_by_name": dimensions_by_name,
        "coordinates": coordinates,
        "coordinates_by_name": coordinates_by_name,
        "variables": variables,
        "variables_by_name": variables_by_name,
    }
    return structure


def _variable_entry(name: str, var: Any, kind: str) -> dict[str, Any]:
    attrs = getattr(var, "attrs", {}) or {}
    return {
        "name": str(name),
        "kind": kind,
        "dtype": str(getattr(var, "dtype", "")),
        "dimensions": [str(dim) for dim in getattr(var, "dims", ())],
        "shape": [int(s) for s in getattr(var, "shape", ())],
        "attrs": {str(k): _json_safe(v) for k, v in attrs.items()},
        "units": str(attrs.get("units", "")),
        "long_name": str(attrs.get("long_name") or attrs.get("standard_name") or ""),
    }


def _expand(node: Any, context: dict[str, Any]) -> Any:
    if isinstance(node, dict):
        if "$value" in node:
            return _resolve(context, str(node["$value"]))
        if "$for" in node:
            return _expand_loop(node, context)
        return {k: _expand(v, context) for k, v in node.items()}
    if isinstance(node, list):
        return [_expand(item, context) for item in node]
    if isinstance(node, str):
        return _interpolate(node, context)
    return node


def _expand_loop(node: dict[str, Any], context: dict[str, Any]) -> list[Any]:
    if "template" not in node:
        raise ValueError("$for directive requires a template")
    items = _resolve(context, str(node["$for"]))
    if items is None:
        return []
    if isinstance(items, dict):
        iterable = list(items.items())
    elif isinstance(items, list):
        iterable = list(enumerate(items))
    else:
        raise ValueError(f"$for expects list or dict, got {type(items).__name__}")

    out: list[Any] = []
    for index, raw in enumerate(iterable):
        if isinstance(items, dict):
            key, item = raw
        else:
            key, item = raw
        child = dict(context)
        child["item"] = item
        child["key"] = key
        child["index"] = index
        out.append(_expand(node["template"], child))
    return out


def _interpolate(template: str, context: dict[str, Any]) -> Any:
    match = _EXPR_RE.fullmatch(template)
    if match:
        return _resolve(context, match.group(1))

    def repl(found: re.Match[str]) -> str:
        value = _resolve(context, found.group(1))
        if value is None:
            return ""
        if isinstance(value, (dict, list)):
            return json.dumps(value, ensure_ascii=False)
        return str(value)

    return _EXPR_RE.sub(repl, template)


def _resolve(context: dict[str, Any], path: str) -> Any:
    if path in {"", "."}:
        return context.get("item", context.get("root"))

    cur: Any = context
    for part in path.split("."):
        if isinstance(cur, dict):
            if part not in cur:
                return None
            cur = cur[part]
            continue
        if isinstance(cur, list):
            try:
                cur = cur[int(part)]
            except (TypeError, ValueError, IndexError):
                return None
            continue
        return None
    return cur


def _json_safe(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, dict):
        return {str(k): _json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(v) for v in value]
    try:
        return value.item()
    except Exception:  # noqa: BLE001
        return str(value)
