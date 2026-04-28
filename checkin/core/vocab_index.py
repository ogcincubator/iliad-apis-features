"""Build a vocabulary index from the local repo.

Sources (ordered by default priority):
  0 local   — every _sources/<bb>/context.jsonld in this repo
  1 oim     — OIM/*.ttl ontology files bundled with the repo
  2 imported — repos declared in bblocks-config.yaml (recorded; terms loaded
               only when the built register cache is present locally)
  3 custom  — user-supplied TTL URLs loaded at runtime during a session

Each VocabSource carries provenance metadata (version, timestamp) so the
generated context.jsonld can record which vocabulary version was used.
"""
from __future__ import annotations

import json
import os
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml

from .. import OIM_DIR, SOURCES_DIR

try:
    from rdflib import Graph, URIRef
    from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, SKOS

    RDFLIB_AVAILABLE = True
except ImportError:  # pragma: no cover
    RDFLIB_AVAILABLE = False

# ---- Provenance levels (lower = higher default priority) ----------------

PROV_LOCAL = 0      # context.jsonld from this repo's _sources/
PROV_OIM = 1        # OIM/*.ttl ontologies bundled with the repo
PROV_IMPORTED = 2   # repos listed in bblocks-config.yaml imports
PROV_CUSTOM = 3     # user-supplied TTL URL


@dataclass
class VocabSource:
    id: str               # stable key used in priority lists
    label: str            # human-readable name shown in UI
    uri: str              # canonical URL or local path string
    provenance: str       # "local" | "oim" | "imported" | "custom"
    provenance_level: int # 0–3; lower = higher default priority
    version: str = ""     # from bblock.json "version" or TTL owl:versionInfo
    timestamp: str = ""   # ISO-8601; from bblock.json dateOfLastChange or file mtime
    term_count: int = 0
    enabled: bool = True

    def as_dict(self) -> dict:
        return self.__dict__


@dataclass
class VocabTerm:
    term: str           # local name / label / property name as seen in source
    uri: str            # expanded URI
    source: str         # human-readable source description (legacy, kept for compat)
    source_id: str = "" # matches VocabSource.id
    label: str = ""     # human label if available
    kind: str = ""      # "property" | "class" | "concept" | "context"
    aliases: list[str] = field(default_factory=list)


@dataclass
class VocabIndex:
    terms: list[VocabTerm] = field(default_factory=list)
    by_term: dict[str, list[VocabTerm]] = field(default_factory=lambda: defaultdict(list))
    by_uri: dict[str, VocabTerm] = field(default_factory=dict)
    sources: list[VocabSource] = field(default_factory=list)
    _source_map: dict[str, VocabSource] = field(default_factory=dict)

    def add(self, t: VocabTerm) -> None:
        self.terms.append(t)
        self.by_term[t.term.lower()].append(t)
        for alias in t.aliases:
            self.by_term[alias.lower()].append(t)
        self.by_uri.setdefault(t.uri, t)

    def add_source(self, s: VocabSource) -> None:
        self.sources.append(s)
        self._source_map[s.id] = s

    def get_source(self, sid: str) -> VocabSource | None:
        return self._source_map.get(sid)

    def all_terms(self) -> list[str]:
        return sorted(self.by_term.keys())

    def terms_for_sources(self, enabled_ids: set[str]) -> "VocabIndex":
        """Return a filtered view that only includes terms from enabled sources."""
        if not enabled_ids:
            return self
        filtered = VocabIndex(sources=self.sources, _source_map=self._source_map)
        for t in self.terms:
            if not t.source_id or t.source_id in enabled_ids:
                filtered.add(t)
        return filtered


# ---- Helpers ---------------------------------------------------------------

def _load_json(p: Path) -> Any:
    try:
        return json.loads(p.read_text())
    except Exception:  # noqa: BLE001
        return None


def _load_yaml(p: Path) -> Any:
    try:
        return yaml.safe_load(p.read_text())
    except Exception:  # noqa: BLE001
        return None


def _file_timestamp(p: Path) -> str:
    try:
        mtime = p.stat().st_mtime
        return datetime.fromtimestamp(mtime, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:  # noqa: BLE001
        return ""


def _expand(ctx_map: dict[str, str], value: str) -> str:
    if ":" in value:
        prefix, rest = value.split(":", 1)
        if prefix in ctx_map and not rest.startswith("//"):
            return ctx_map[prefix] + rest
    return value


def _local_name(uri: str) -> str:
    for sep in ("#", "/"):
        if sep in uri:
            return uri.rsplit(sep, 1)[-1]
    return uri


# ---- Per-source collectors -------------------------------------------------

def _collect_context(path: Path, index: VocabIndex, source_id: str) -> int:
    """Ingest a context.jsonld file; return count of terms added."""
    data = _load_json(path)
    if not isinstance(data, dict):
        return 0
    ctx = data.get("@context")
    prefix_map: dict[str, str] = {}
    added = 0

    def _ingest(node: Any) -> None:
        nonlocal added
        if isinstance(node, dict):
            for k, v in node.items():
                if k.startswith("@"):
                    continue
                if isinstance(v, str):
                    prefix_map[k] = v
            for k, v in node.items():
                if k.startswith("@") or not isinstance(v, (str, dict)):
                    continue
                if isinstance(v, str):
                    uri = _expand(prefix_map, v)
                    index.add(VocabTerm(term=k, uri=uri,
                                       source=f"{path.parent.name}/context.jsonld",
                                       source_id=source_id, kind="context"))
                    added += 1
                elif isinstance(v, dict):
                    vid = v.get("@id")
                    if isinstance(vid, str):
                        uri = _expand(prefix_map, vid)
                        index.add(VocabTerm(term=k, uri=uri,
                                            source=f"{path.parent.name}/context.jsonld",
                                            source_id=source_id, kind="context"))
                        added += 1
        elif isinstance(node, list):
            for item in node:
                _ingest(item)

    _ingest(ctx)
    return added


def _collect_ttl(path: Path, index: VocabIndex, source_id: str) -> int:
    """Parse a Turtle ontology file; return count of terms added."""
    if not RDFLIB_AVAILABLE:
        return 0
    g = Graph()
    try:
        g.parse(path, format="turtle")
    except Exception:  # noqa: BLE001
        return 0
    kinds = {
        OWL.Class: "class",
        OWL.ObjectProperty: "property",
        OWL.DatatypeProperty: "property",
        OWL.AnnotationProperty: "property",
        RDF.Property: "property",
        RDFS.Class: "class",
        SKOS.Concept: "concept",
    }
    added = 0
    for subj, _p, rdf_type in g.triples((None, RDF.type, None)):
        kind = kinds.get(rdf_type)
        if not kind or not isinstance(subj, URIRef):
            continue
        uri = str(subj)
        term = _local_name(uri)
        labels: list[str] = []
        for _s, _p2, lab in g.triples((subj, RDFS.label, None)):
            labels.append(str(lab))
        for _s, _p2, lab in g.triples((subj, SKOS.prefLabel, None)):
            labels.append(str(lab))
        label = labels[0] if labels else ""
        index.add(VocabTerm(term=term, uri=uri,
                             source=f"OIM/{path.name}",
                             source_id=source_id,
                             label=label, kind=kind, aliases=labels))
        added += 1
    return added


def _ttl_version(path: Path) -> str:
    """Extract owl:versionInfo or dcterms:modified from a TTL file."""
    if not RDFLIB_AVAILABLE:
        return ""
    g = Graph()
    try:
        g.parse(path, format="turtle")
    except Exception:  # noqa: BLE001
        return ""
    for _s, _p, o in g.triples((None, OWL.versionInfo, None)):
        return str(o)
    for _s, _p, o in g.triples((None, DCTERMS.modified, None)):
        return str(o)
    return ""


# ---- Custom TTL loader (session-time) -------------------------------------

def add_custom_source(url: str, index: VocabIndex) -> VocabSource:
    """Fetch a TTL from *url*, parse it, add terms to *index*, return VocabSource.

    The caller is responsible for persisting the VocabSource in the session so
    the URL can be written into the generated bblock's metadata.
    """
    import httpx

    source_id = f"custom:{url}"
    # Fetch
    with httpx.Client(follow_redirects=True, timeout=30.0) as c:
        r = c.get(url, headers={"Accept": "text/turtle, application/rdf+xml;q=0.9, */*;q=0.5"})
        r.raise_for_status()
        ttl_text = r.text

    if not RDFLIB_AVAILABLE:
        raise RuntimeError("rdflib is required to parse custom TTL vocabularies")

    g = Graph()
    fmt = "turtle"
    ct = r.headers.get("content-type", "")
    if "xml" in ct:
        fmt = "xml"
    g.parse(data=ttl_text, format=fmt)

    # Attempt to get a label / version from the ontology declaration
    label = url
    version = ""
    timestamp = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for _s, _p, o in g.triples((None, RDFS.label, None)):
        label = str(o); break
    for _s, _p, o in g.triples((None, OWL.versionInfo, None)):
        version = str(o); break
    for _s, _p, o in g.triples((None, DCTERMS.modified, None)):
        timestamp = str(o); break

    kinds = {
        OWL.Class: "class",
        OWL.ObjectProperty: "property",
        OWL.DatatypeProperty: "property",
        OWL.AnnotationProperty: "property",
        RDF.Property: "property",
        RDFS.Class: "class",
        SKOS.Concept: "concept",
    }
    added = 0
    for subj, _p, rdf_type in g.triples((None, RDF.type, None)):
        kind = kinds.get(rdf_type)
        if not kind or not isinstance(subj, URIRef):
            continue
        uri = str(subj)
        term = _local_name(uri)
        labels: list[str] = []
        for _s2, _p2, lab in g.triples((subj, RDFS.label, None)):
            labels.append(str(lab))
        for _s2, _p2, lab in g.triples((subj, SKOS.prefLabel, None)):
            labels.append(str(lab))
        lbl = labels[0] if labels else ""
        index.add(VocabTerm(term=term, uri=uri, source=url,
                             source_id=source_id,
                             label=lbl, kind=kind, aliases=labels))
        added += 1

    src = VocabSource(
        id=source_id,
        label=label,
        uri=url,
        provenance="custom",
        provenance_level=PROV_CUSTOM,
        version=version,
        timestamp=timestamp,
        term_count=added,
        enabled=True,
    )
    index.add_source(src)
    return src


# ---- Main builder ----------------------------------------------------------

def _read_imports(repo_root: Path) -> list[dict]:
    """Parse bblocks-config.yaml and return a list of import entries."""
    cfg_path = repo_root / "bblocks-config.yaml"
    if not cfg_path.exists():
        return []
    cfg = _load_yaml(cfg_path) or {}
    imports = cfg.get("imports") or []
    return [{"url": u, "label": str(u)} for u in imports if isinstance(u, str) and u != "default"]


def build_index(
    sources_dir: Path | None = None,
    oim_dir: Path | None = None,
    repo_root: Path | None = None,
) -> VocabIndex:
    idx = VocabIndex()
    sdir = sources_dir or SOURCES_DIR
    odir = oim_dir or OIM_DIR
    root = repo_root or (SOURCES_DIR.parent if SOURCES_DIR else Path("."))

    # ---- Local building block context.jsonld files (provenance_level=0) ----
    if sdir.exists():
        for ctx in sorted(sdir.glob("*/context.jsonld")):
            bb_dir = ctx.parent
            bb_meta = _load_json(bb_dir / "bblock.json") or {}
            version = str(bb_meta.get("version") or "")
            ts = str(bb_meta.get("dateOfLastChange") or _file_timestamp(ctx))
            sid = f"local:{bb_dir.name}"
            before = len(idx.terms)
            _collect_context(ctx, idx, sid)
            count = len(idx.terms) - before
            idx.add_source(VocabSource(
                id=sid,
                label=str(bb_meta.get("name") or bb_dir.name),
                uri=str(ctx),
                provenance="local",
                provenance_level=PROV_LOCAL,
                version=version,
                timestamp=ts,
                term_count=count,
                enabled=True,
            ))

    # ---- OIM TTL ontologies (provenance_level=1) ---------------------------
    if odir.exists():
        for ttl in sorted(odir.glob("*.ttl")):
            sid = f"oim:{ttl.stem}"
            version = _ttl_version(ttl)
            ts = _file_timestamp(ttl)
            before = len(idx.terms)
            _collect_ttl(ttl, idx, sid)
            count = len(idx.terms) - before
            idx.add_source(VocabSource(
                id=sid,
                label=f"OIM — {ttl.stem}",
                uri=str(ttl),
                provenance="oim",
                provenance_level=PROV_OIM,
                version=version,
                timestamp=ts,
                term_count=count,
                enabled=True,
            ))

    # ---- Imported repos from bblocks-config.yaml (provenance_level=2) ------
    # Terms are not fetched at build time (would require network); just record sources.
    for imp in _read_imports(root):
        sid = f"imported:{imp['url']}"
        if sid not in idx._source_map:
            idx.add_source(VocabSource(
                id=sid,
                label=imp["label"],
                uri=imp["url"],
                provenance="imported",
                provenance_level=PROV_IMPORTED,
                term_count=0,
                enabled=False,  # disabled by default until explicitly loaded
            ))

    return idx


def summary(idx: VocabIndex) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for t in idx.terms:
        counts[t.kind] += 1
    counts["total"] = len(idx.terms)
    counts["distinct_terms"] = len(idx.by_term)
    counts["distinct_uris"] = len(idx.by_uri)
    return dict(counts)


def iter_uris(idx: VocabIndex) -> Iterable[str]:
    return iter(idx.by_uri.keys())
