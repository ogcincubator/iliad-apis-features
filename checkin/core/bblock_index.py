"""Index of building blocks from local _sources/ and remote registers.

Local entries are read directly from _sources/*.
Remote entries come from registers declared in bblocks-config.yaml ``imports``.
Remote register responses and per-bblock schemas/contexts are cached under
~/.cache/iliad-checkin/bblock-index/ with a configurable TTL (default 24 h).
"""
from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

import yaml

from .. import SOURCES_DIR

# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------

_CACHE_DIR = Path.home() / ".cache" / "iliad-checkin" / "bblock-index"
_CACHE_TTL = 86_400   # seconds — remote data reused for 24 h

_DEFAULT_REGISTER = "https://opengeospatial.github.io/bblocks"


def _cache_get(key: str) -> Any:
    p = _CACHE_DIR / (hashlib.md5(key.encode()).hexdigest() + ".json")
    if not p.exists():
        return None
    try:
        blob = json.loads(p.read_text())
        if time.time() - blob.get("_ts", 0) < _CACHE_TTL:
            return blob["_v"]
    except Exception:  # noqa: BLE001
        pass
    return None


def _cache_set(key: str, value: Any) -> None:
    try:
        _CACHE_DIR.mkdir(parents=True, exist_ok=True)
        p = _CACHE_DIR / (hashlib.md5(key.encode()).hexdigest() + ".json")
        p.write_text(json.dumps({"_ts": time.time(), "_v": value}))
    except Exception:  # noqa: BLE001
        pass


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class TargetField:
    path: str
    type: str = ""
    example: Any = None
    source: str = ""

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
    properties: list[str] = field(default_factory=list)
    target_fields: list[TargetField] = field(default_factory=list)
    vocab_uris: dict[str, str] = field(default_factory=dict)
    vocabularies: list[dict[str, str]] = field(default_factory=list)

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
            "vocabularies": self.vocabularies,
        }


# ---------------------------------------------------------------------------
# Schema / context walkers (shared by local and remote paths)
# ---------------------------------------------------------------------------

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
        for v in node.values():
            if isinstance(v, (dict, list)):
                _walk_schema_properties(v, out)
    elif isinstance(node, list):
        for item in node:
            _walk_schema_properties(item, out)


def _walk_schema_target_fields(node: Any, prefix: str, out: list[TargetField]) -> None:
    if not isinstance(node, dict):
        return
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
    ap = node.get("additionalProperties")
    if isinstance(ap, dict):
        _walk_schema_target_fields(ap, f"{prefix}.*" if prefix else "*", out)


def _walk_example_fields(node: Any, prefix: str, out: list[TargetField], source: str) -> None:
    if isinstance(node, dict):
        for k, v in node.items():
            path = f"{prefix}.{k}" if prefix else k
            out.append(TargetField(path=path, type=_py_type(v), example=_safe_example(v), source=source))
            _walk_example_fields(v, path, out, source)
    elif isinstance(node, list) and node:
        first = node[0]
        if isinstance(first, (dict, list)):
            _walk_example_fields(first, f"{prefix}[0]", out, source)
        else:
            out.append(TargetField(path=f"{prefix}[]", type=_py_type(first), example=first, source=source))


def _py_type(v: Any) -> str:
    if isinstance(v, bool):   return "boolean"
    if isinstance(v, int):    return "integer"
    if isinstance(v, float):  return "number"
    if isinstance(v, list):   return "array"
    if isinstance(v, dict):   return "object"
    if v is None:             return "null"
    return "string"


def _safe_example(v: Any) -> Any:
    return v if isinstance(v, (str, int, float, bool)) or v is None else None


def _ingest_context(ctx: Any, out: dict[str, str]) -> None:
    if isinstance(ctx, dict):
        for k, v in ctx.items():
            if k.startswith("@"):
                continue
            if isinstance(v, str):
                out[k] = v
            elif isinstance(v, dict) and "@id" in v:
                out[k] = str(v["@id"])
    elif isinstance(ctx, list):
        for item in ctx:
            _ingest_context(item, out)


# ---------------------------------------------------------------------------
# Local entry builder
# ---------------------------------------------------------------------------

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


def _extract_target_fields(bb_dir: Path) -> list[TargetField]:
    fields: list[TargetField] = []
    for name in ("schema.json", "schema.yaml"):
        p = bb_dir / name
        if p.exists():
            data = _load_json(p) if name.endswith(".json") else _load_yaml(p)
            if isinstance(data, dict):
                _walk_schema_target_fields(data, "", fields)
            break
    ex_dir = bb_dir / "examples"
    if ex_dir.is_dir():
        for ex in sorted(ex_dir.glob("*.json")):
            data = _load_json(ex)
            if isinstance(data, (dict, list)):
                _walk_example_fields(data, "", fields, source=f"example:{ex.name}")
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
    out: dict[str, str] = {}
    _ingest_context(data.get("@context"), out)
    return out


def _extract_vocabularies(meta: dict[str, Any]) -> list[dict[str, str]]:
    raw = meta.get("vocabularies") or []
    if not isinstance(raw, list):
        return []
    out: list[dict[str, str]] = []
    for item in raw:
        if isinstance(item, str) and item.strip():
            out.append({"url": item.strip()})
            continue
        if not isinstance(item, dict):
            continue
        url = item.get("url") or item.get("link") or item.get("href")
        if not isinstance(url, str) or not url.strip():
            continue
        rec = {"url": url.strip()}
        for key in ("title", "format", "profile", "role"):
            val = item.get(key)
            if isinstance(val, str) and val.strip():
                rec[key] = val.strip()
        out.append(rec)
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
        vocabularies=_extract_vocabularies(meta),
    )


# ---------------------------------------------------------------------------
# Remote register fetching
# ---------------------------------------------------------------------------

def _fetch_json_remote(url: str, timeout: float = 20.0) -> Any:
    try:
        import httpx
        with httpx.Client(follow_redirects=True, timeout=timeout) as c:
            r = c.get(url)
            r.raise_for_status()
            return r.json()
    except Exception:  # noqa: BLE001
        return None


def _schema_fields_from_url(url: str) -> tuple[list[str], list[TargetField]]:
    """Fetch a remote schema URL and return (properties, target_fields).  Cached."""
    cached = _cache_get(f"schema:{url}")
    if cached is not None:
        props = cached.get("p") or []
        tfs = [TargetField(**f) for f in (cached.get("tf") or [])]
        return props, tfs
    data = _fetch_json_remote(url)
    if not isinstance(data, dict):
        _cache_set(f"schema:{url}", {"p": [], "tf": []})
        return [], []
    prop_set: set[str] = set()
    tf_list: list[TargetField] = []
    _walk_schema_properties(data, prop_set)
    _walk_schema_target_fields(data, "", tf_list)
    result = {"p": sorted(prop_set), "tf": [f.as_dict() for f in tf_list]}
    _cache_set(f"schema:{url}", result)
    return result["p"], tf_list


def _context_terms_from_url(url: str) -> dict[str, str]:
    """Fetch a remote context URL and return term→uri map.  Cached."""
    cached = _cache_get(f"ctx:{url}")
    if cached is not None:
        return cached
    data = _fetch_json_remote(url)
    out: dict[str, str] = {}
    if isinstance(data, dict):
        _ingest_context(data.get("@context"), out)
    _cache_set(f"ctx:{url}", out)
    return out


def _entry_from_remote(item: dict[str, Any]) -> BBlockEntry | None:
    bid = str(item.get("itemIdentifier") or "").strip()
    if not bid:
        return None

    title = str(item.get("name") or bid)
    abstract = str(item.get("abstract") or "")
    tags = list(item.get("tags") or [])
    depends_on = [str(x) for x in (item.get("dependsOn") or [])]
    standards: list[str] = []
    for key in ("conformsTo", "conformanceClasses", "standards"):
        v = item.get(key)
        if isinstance(v, list):
            standards = [str(x) for x in v]
            break

    # Schema → target_fields + properties
    # register.json may have schema as dict {media-type: url}, list, or string
    raw_schema = item.get("schema") or []
    if isinstance(raw_schema, dict):
        # prefer application/json; fall back to any value
        schema_urls = [raw_schema.get("application/json") or next(iter(raw_schema.values()), "")]
        schema_urls = [u for u in schema_urls if u]
    elif isinstance(raw_schema, str):
        schema_urls = [raw_schema] if raw_schema else []
    else:
        schema_urls = list(raw_schema)
    # Prefer the non-annotated / source schema when available
    source_schema = item.get("sourceSchema") or ""
    if source_schema:
        schema_urls = [source_schema] + [u for u in schema_urls if u != source_schema]

    properties: list[str] = []
    target_fields: list[TargetField] = []
    for surl in schema_urls[:1]:
        if surl and surl.startswith("http"):
            properties, target_fields = _schema_fields_from_url(surl)

    # Context → vocab_uris  (may be string, list, or dict {media-type: url})
    ctx_url = item.get("ldContext") or item.get("sourceLdContext") or ""
    if isinstance(ctx_url, dict):
        ctx_url = next(iter(ctx_url.values()), "")
    elif isinstance(ctx_url, list):
        ctx_url = ctx_url[0] if ctx_url else ""
    vocab_uris: dict[str, str] = {}
    if ctx_url and ctx_url.startswith("http"):
        vocab_uris = _context_terms_from_url(ctx_url)

    return BBlockEntry(
        id=bid,
        path=Path(bid.replace(".", "/")),
        title=title,
        abstract=abstract,
        tags=tags,
        standards=standards,
        depends_on=depends_on,
        properties=properties,
        target_fields=target_fields,
        vocab_uris=vocab_uris,
        vocabularies=_extract_vocabularies(item),
    )


# ---------------------------------------------------------------------------
# Config parser
# ---------------------------------------------------------------------------

def _import_urls() -> list[str]:
    """Return absolute register base URLs from bblocks-config.yaml imports."""
    cfg_path = SOURCES_DIR.parent / "bblocks-config.yaml"
    if not cfg_path.exists():
        return []
    try:
        cfg = yaml.safe_load(cfg_path.read_text()) or {}
    except Exception:  # noqa: BLE001
        return []

    schema_mapping = cfg.get("schema-mapping") or {}
    # Resolve 'default' alias: strip trailing 'annotated-schemas/' segment
    raw_default = schema_mapping.get("default", _DEFAULT_REGISTER)
    if "annotated-schemas" in raw_default:
        base_default = raw_default.rstrip("/").rsplit("/annotated-schemas", 1)[0]
    else:
        base_default = raw_default.rstrip("/")

    urls: list[str] = []
    for imp in (cfg.get("imports") or []):
        if imp == "default":
            urls.append(base_default)
        elif isinstance(imp, str) and imp.startswith("http"):
            urls.append(imp.rstrip("/"))
    return urls


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def load_index(sources_dir: Path | None = None) -> list[BBlockEntry]:
    """Load building blocks from local _sources/ and all remote imports.

    Remote register lists are fetched once and cached for ``_CACHE_TTL`` seconds.
    Individual schemas and contexts are also cached separately so incremental
    updates only re-fetch new or changed entries.
    """
    root = sources_dir or SOURCES_DIR
    entries: list[BBlockEntry] = []
    seen: set[str] = set()

    # 1. Local entries (always authoritative — override remote duplicates)
    for child in sorted(root.iterdir()):
        if not child.is_dir() or child.name.startswith((".", "_")):
            continue
        entry = _entry_from_dir(child)
        if entry:
            entries.append(entry)
            seen.add(entry.id)

    # 2. Remote registers from bblocks-config.yaml imports
    for base_url in _import_urls():
        # Modern OGC registers publish at build/register.json; fall back to bblocks.json
        bb_list = None
        for candidate_url in (f"{base_url}/build/register.json", f"{base_url}/bblocks.json"):
            bb_list = _cache_get(f"bblist:{candidate_url}")
            if bb_list is not None:
                break
            raw = _fetch_json_remote(candidate_url)
            if raw is None:
                continue
            if isinstance(raw, list):
                bb_list = raw
            elif isinstance(raw, dict):
                bb_list = raw.get("bblocks") or raw.get("items") or []
            else:
                continue
            _cache_set(f"bblist:{candidate_url}", bb_list)
            break  # found a working endpoint
        if bb_list is None:
            bb_list = []

        for item in (bb_list or []):
            bid = str(item.get("itemIdentifier") or "").strip()
            if not bid or bid in seen:
                continue
            entry = _entry_from_remote(item)
            if entry:
                entries.append(entry)
                seen.add(bid)

    return entries


def iter_properties(entries: Iterable[BBlockEntry]) -> set[str]:
    acc: set[str] = set()
    for e in entries:
        acc.update(e.properties)
    return acc
