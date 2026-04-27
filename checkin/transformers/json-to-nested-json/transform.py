"""Mapping-driven JSON-to-JSON transformer.

Dotted-path syntax (used in both source and target):
    key              object key
    key.sub          nested key
    list[0]          explicit list index (read) / set element 0 (write)
    list[]           append to list (write only; read = first element)
    *                glob over dict keys (read only) — returns dict of subvalues

Each mapping entry may use either:
    {source, target, type, default, required}
        — plain path copy; value = dig(input, source)
    {expression, target, type}
        — template expression; ${path} placeholders are replaced with dig() values.
          After substitution the runner tries JSON-parse, falls back to string.
          Examples:
            "${lon}"                          → numeric value of lon field
            "${first} ${last}"                → string "Jane Doe"
            "[${lon}, ${lat}]"                → JSON array [12.3, 45.6]
            '{"type":"Point","coordinates":[${lon},${lat}]}' → dict

Pipeline per record:
    1. Start from a deep-copy of ``params['target_template']`` (defaults to {}).
    2. For each mapping apply source-copy or expression-eval.
    3. If ``params.passthrough_extras`` is true, source leaves not referenced
       by any mapping are copied into ``output['extras'][<source_path>]``.
"""
from __future__ import annotations

import copy
import json
import re
from typing import Any

_TOKEN_RE = re.compile(r"([^.\[]+)|\[(\d*)\]")


def _tokens(path: str) -> list[tuple[str, Any]]:
    tokens: list[tuple[str, Any]] = []
    for m in _TOKEN_RE.finditer(path):
        key, idx = m.groups()
        if key is not None:
            tokens.append(("key", key))
        elif idx is None or idx == "":
            tokens.append(("list", None))   # append / first
        else:
            tokens.append(("list", int(idx)))
    return tokens


_MISSING = object()
_PLACEHOLDER_RE = re.compile(r"\$\{([^}]+)\}")


def _resolve_expression(expr: str, input_obj: Any) -> Any:
    """Substitute ${path} placeholders and try JSON-parsing the result."""
    def _sub(m: re.Match) -> str:
        val = dig(input_obj, m.group(1))
        if val is _MISSING or val is None:
            return "null"
        if isinstance(val, bool):
            return "true" if val else "false"
        if isinstance(val, (int, float)):
            return repr(val) if isinstance(val, float) else str(val)
        return json.dumps(str(val))  # quoted string

    result = _PLACEHOLDER_RE.sub(_sub, expr)
    # If the entire expression was a single placeholder, the substituted value
    # may already be a typed literal — try JSON-parse to recover numbers/booleans.
    try:
        return json.loads(result)
    except (json.JSONDecodeError, ValueError):
        return result


def dig(obj: Any, path: str) -> Any:
    cur: Any = obj
    for kind, arg in _tokens(path):
        if kind == "key":
            if arg == "*":
                if isinstance(cur, dict):
                    return {k: v for k, v in cur.items()}
                return _MISSING
            if isinstance(cur, dict):
                if arg not in cur:
                    return _MISSING
                cur = cur[arg]
            else:
                return _MISSING
        else:
            if not isinstance(cur, list):
                return _MISSING
            idx = 0 if arg is None else int(arg)
            if idx >= len(cur):
                return _MISSING
            cur = cur[idx]
    return cur


def put(obj: Any, path: str, value: Any) -> None:
    tokens = _tokens(path)
    if not tokens:
        return
    cur = obj
    for i, (kind, arg) in enumerate(tokens):
        last = i == len(tokens) - 1
        next_is_list = not last and tokens[i + 1][0] == "list"
        if kind == "key":
            if not isinstance(cur, dict):
                return
            if last:
                cur[arg] = value
            else:
                if arg not in cur or not _container_matches(cur[arg], next_is_list):
                    cur[arg] = [] if next_is_list else {}
                cur = cur[arg]
        else:
            if not isinstance(cur, list):
                return
            if arg is None:
                # append
                if last:
                    cur.append(value)
                    return
                cur.append([] if next_is_list else {})
                cur = cur[-1]
            else:
                while len(cur) <= arg:
                    cur.append(None)
                if last:
                    cur[arg] = value
                else:
                    if cur[arg] is None or not _container_matches(cur[arg], next_is_list):
                        cur[arg] = [] if next_is_list else {}
                    cur = cur[arg]


def _container_matches(v: Any, want_list: bool) -> bool:
    return isinstance(v, list) if want_list else isinstance(v, dict)


def coerce(value: Any, kind: str) -> Any:
    if value is _MISSING or value is None or not kind:
        return None if value is _MISSING else value
    try:
        if kind == "integer":
            return int(value)
        if kind == "number":
            return float(value)
        if kind == "boolean":
            if isinstance(value, bool):
                return value
            if isinstance(value, str):
                return value.lower() in {"true", "1", "yes"}
            return bool(value)
        if kind == "string":
            return str(value)
        if kind == "array":
            return value if isinstance(value, list) else [value]
        if kind == "object":
            return value if isinstance(value, dict) else {"value": value}
    except (TypeError, ValueError):
        return value
    return value


def _mapping_source_roots(mappings: list[dict]) -> set[str]:
    """Top-level source keys already referenced — so extras excludes them."""
    out = set()
    for m in mappings:
        if "expression" in m:
            # collect all ${path} placeholders
            for ph in _PLACEHOLDER_RE.findall(m["expression"]):
                root = ph.split(".", 1)[0].split("[", 1)[0]
                out.add(root)
        else:
            src = m.get("source", "")
            if src:
                root = src.split(".", 1)[0].split("[", 1)[0]
                out.add(root)
    return out


def _one(input_obj: Any, params: dict) -> Any:
    mappings = params.get("mappings", [])
    out: Any = copy.deepcopy(params.get("target_template", {}))
    if not isinstance(out, dict):
        out = {}
    for m in mappings:
        if "expression" in m:
            value = _resolve_expression(m["expression"], input_obj)
            if value is None and m.get("required"):
                raise ValueError(f"expression produced null for required target: {m['target']}")
        else:
            value = dig(input_obj, m["source"])
            if value is _MISSING or value is None:
                if "default" in m:
                    value = m["default"]
                elif m.get("required"):
                    raise ValueError(f"required source path missing: {m['source']}")
                else:
                    continue
        value = coerce(value, m.get("type", ""))
        put(out, m["target"], value)
    if params.get("passthrough_extras") and isinstance(input_obj, dict):
        referenced = _mapping_source_roots(mappings)
        extras = {k: v for k, v in input_obj.items() if k not in referenced}
        if extras:
            out.setdefault("extras", {}).update(extras)
    return out


def transform(input_obj: Any, params: dict) -> Any:
    if isinstance(input_obj, list):
        return [_one(item, params) for item in input_obj]
    return _one(input_obj, params)
