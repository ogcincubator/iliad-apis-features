"""Build a vocabulary index from the local repo.

Sources:
- Every `_sources/<bb>/context.jsonld`: term -> URI bindings, plus prefix/namespace
  expansions.
- `OIM/*.ttl`: rdf:Property, owl:ObjectProperty, owl:DatatypeProperty, owl:Class,
  skos:Concept. Labels via rdfs:label / skos:prefLabel.
"""
from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

from .. import OIM_DIR, SOURCES_DIR

try:
    from rdflib import Graph, Namespace, URIRef
    from rdflib.namespace import OWL, RDF, RDFS, SKOS

    RDFLIB_AVAILABLE = True
except ImportError:  # pragma: no cover
    RDFLIB_AVAILABLE = False


@dataclass
class VocabTerm:
    term: str          # local name / label / property name as seen in source
    uri: str           # expanded URI
    source: str        # e.g. "macroobservation", "oim/cross-domain.ttl"
    label: str = ""    # human label if available
    kind: str = ""     # "property" | "class" | "concept" | "context"
    aliases: list[str] = field(default_factory=list)


@dataclass
class VocabIndex:
    terms: list[VocabTerm] = field(default_factory=list)
    by_term: dict[str, list[VocabTerm]] = field(default_factory=lambda: defaultdict(list))
    by_uri: dict[str, VocabTerm] = field(default_factory=dict)

    def add(self, t: VocabTerm) -> None:
        self.terms.append(t)
        self.by_term[t.term.lower()].append(t)
        for alias in t.aliases:
            self.by_term[alias.lower()].append(t)
        self.by_uri.setdefault(t.uri, t)

    def all_terms(self) -> list[str]:
        return sorted(self.by_term.keys())


def _load_json(p: Path) -> Any:
    try:
        return json.loads(p.read_text())
    except Exception:  # noqa: BLE001
        return None


def _expand(ctx_map: dict[str, str], value: str) -> str:
    if ":" in value:
        prefix, rest = value.split(":", 1)
        if prefix in ctx_map and not rest.startswith("//"):
            return ctx_map[prefix] + rest
    return value


def _collect_context(path: Path, index: VocabIndex) -> None:
    data = _load_json(path)
    if not isinstance(data, dict):
        return
    ctx = data.get("@context")
    prefix_map: dict[str, str] = {}

    def _ingest(node: Any) -> None:
        if isinstance(node, dict):
            # First pass — gather prefix-style entries (string values acting as namespaces)
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
                    index.add(VocabTerm(term=k, uri=uri, source=f"{path.parent.name}/context.jsonld", kind="context"))
                elif isinstance(v, dict):
                    vid = v.get("@id")
                    if isinstance(vid, str):
                        uri = _expand(prefix_map, vid)
                        index.add(VocabTerm(term=k, uri=uri, source=f"{path.parent.name}/context.jsonld", kind="context"))
        elif isinstance(node, list):
            for item in node:
                _ingest(item)

    _ingest(ctx)


def _local_name(uri: str) -> str:
    for sep in ("#", "/"):
        if sep in uri:
            return uri.rsplit(sep, 1)[-1]
    return uri


def _collect_ttl(path: Path, index: VocabIndex) -> None:
    if not RDFLIB_AVAILABLE:
        return
    g = Graph()
    try:
        g.parse(path, format="turtle")
    except Exception:  # noqa: BLE001
        return
    kinds = {
        OWL.Class: "class",
        OWL.ObjectProperty: "property",
        OWL.DatatypeProperty: "property",
        OWL.AnnotationProperty: "property",
        RDF.Property: "property",
        RDFS.Class: "class",
        SKOS.Concept: "concept",
    }
    source = f"OIM/{path.name}"
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
        index.add(VocabTerm(term=term, uri=uri, source=source, label=label, kind=kind, aliases=labels))


def build_index(
    sources_dir: Path | None = None,
    oim_dir: Path | None = None,
) -> VocabIndex:
    idx = VocabIndex()
    sdir = sources_dir or SOURCES_DIR
    odir = oim_dir or OIM_DIR
    if sdir.exists():
        for ctx in sorted(sdir.glob("*/context.jsonld")):
            _collect_context(ctx, idx)
    if odir.exists():
        for ttl in sorted(odir.glob("*.ttl")):
            _collect_ttl(ttl, idx)
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
