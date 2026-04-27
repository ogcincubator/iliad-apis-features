"""Rank existing building blocks against a Profile.

The score is a weighted sum of four signals:
- leaf-name overlap between profile source-field leaves and the bblock's schema /
  target-field leaves (flat *and* nested paths both get a leaf extracted)
- full-path overlap between profile dotted paths and bblock target-field paths
- context-vocab overlap between profile source-field leaves and context.jsonld terms
- tag/standards overlap with the profile's format

Every bblock is returned (no cutoff); the UI is responsible for truncating /
scrolling. Deterministic and explainable.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable

from rapidfuzz import fuzz

from .bblock_index import BBlockEntry
from .profile import Profile


@dataclass
class BBlockMatch:
    entry: BBlockEntry
    score: float
    matched_properties: list[str]
    reason: str


FORMAT_TAG_HINTS = {
    "netcdf": {"netcdf", "coverage", "covjson", "coveragejson", "zarr"},
    "csv": {"table", "csv", "observation", "sosa"},
    "tsv": {"table", "tsv", "csv"},
    "geoparquet": {"geoparquet", "parquet", "table"},
    "parquet": {"parquet", "table"},
    "geojson": {"geojson", "feature", "features"},
    "json": {"json"},
    "ogc-wfs": {"wfs", "feature", "geojson"},
    "ogc-wms": {"wms", "coverage"},
    "ogc-edr": {"edr", "coverage", "observation"},
    "ogc-api-features": {"geojson", "feature", "sosa"},
    "ogc-api-records": {"stac", "records", "dcat"},
    "opendap": {"netcdf", "coverage", "covjson"},
}


def _leaf(path: str) -> str:
    """Last path segment, stripped of [N] list indices."""
    tail = path.rsplit(".", 1)[-1]
    return re.sub(r"\[\d*\]$", "", tail).lower()


def _leaf_overlap(profile_leaves: set[str], bb_leaves: set[str]) -> tuple[float, list[str]]:
    if not profile_leaves or not bb_leaves:
        return 0.0, []
    matched: list[str] = []
    total = 0.0
    for pl in profile_leaves:
        if pl in bb_leaves:
            matched.append(pl)
            total += 1.0
            continue
        best = 0
        best_name = ""
        for bl in bb_leaves:
            s = fuzz.token_set_ratio(pl, bl)
            if s > best:
                best = s
                best_name = bl
        if best >= 85:
            matched.append(f"{pl}≈{best_name}")
            total += best / 100.0
    return total / max(len(profile_leaves), 1), matched


def _path_overlap(profile_paths: set[str], bb_paths: set[str]) -> float:
    if not profile_paths or not bb_paths:
        return 0.0
    hit = len(profile_paths & bb_paths)
    return hit / max(len(profile_paths), 1)


def _tag_overlap(fmt: str, bb: BBlockEntry) -> float:
    hints = FORMAT_TAG_HINTS.get(fmt, set())
    if not hints:
        return 0.0
    bag = {t.lower() for t in bb.tags} | {s.lower() for s in bb.standards} | {bb.id.lower()}
    hit = sum(1 for h in hints if any(h in item for item in bag))
    return hit / max(len(hints), 1)


def _vocab_overlap(profile_props: set[str], bb_context_terms: Iterable[str]) -> float:
    ctx = {t.lower() for t in bb_context_terms}
    if not ctx or not profile_props:
        return 0.0
    pl = {p.lower() for p in profile_props}
    return len(pl & ctx) / max(len(pl), 1)


def rank(profile: Profile, entries: list[BBlockEntry], k: int | None = None) -> list[BBlockMatch]:
    """Return every entry scored against the profile, sorted by score descending.

    ``k`` is an optional cap for when the caller only wants the top-N; by default
    everything is returned so the UI can show the full list.
    """
    profile_paths = {p.name for p in profile.properties}
    profile_leaves = {_leaf(p.name) for p in profile.properties if _leaf(p.name)}

    results: list[BBlockMatch] = []
    for bb in entries:
        bb_target_paths = {tf.path for tf in bb.target_fields}
        bb_leaves = {_leaf(path) for path in bb_target_paths} | {p.lower() for p in bb.properties}
        bb_leaves.discard("")

        leaf_score, matched = _leaf_overlap(profile_leaves, bb_leaves)
        path_score = _path_overlap(profile_paths, bb_target_paths)
        tag_score = _tag_overlap(profile.format, bb)
        ctx_score = _vocab_overlap(profile_leaves, {t.lower() for t in bb.vocab_uris.keys()})
        total = 0.45 * leaf_score + 0.20 * path_score + 0.20 * ctx_score + 0.15 * tag_score
        reason = (
            f"leaves {leaf_score:.0%} · paths {path_score:.0%} · "
            f"ctx {ctx_score:.0%} · fmt {tag_score:.0%}"
        )
        results.append(BBlockMatch(entry=bb, score=total, matched_properties=matched, reason=reason))

    results.sort(key=lambda m: m.score, reverse=True)
    return results if k is None else results[:k]


# ---- Related-bblock proposer (non-ranked, standards-based) ----

RELATED_MAP = {
    "coverageJSON": ["coverage_information_model", "stac_multidim_data", "EDR_collection"],
    "coverage_information_model": ["coverageJSON", "stac_multidim_data"],
    "EDR_collection": ["coverageJSON", "coverage_information_model"],
    "macroobservation": ["oim-obs", "oim-bio-tdwg"],
    "oim-obs": ["oim", "oim-obs-cs", "oim-sta-obs"],
    "oim-bio-tdwg": ["oim", "oim-obs"],
    "iliad-jellyfish-features": ["iliad-jellyfish-ontology", "oim-obs-cs"],
    "geoparquet": ["stac_multidim_data"],
    "marine-protected-area-emodnet": ["oim", "oim-bio-tdwg"],
    "zarr_array_metadata": ["zarr_attrs_metadata", "zarr_attrs_sdn", "stac_multidim_data"],
    "zarr_attrs_metadata": ["zarr_array_metadata", "zarr_attrs_sdn"],
}


def related(bb_id: str, entries: list[BBlockEntry]) -> list[BBlockEntry]:
    by_id = {e.id: e for e in entries}
    return [by_id[r] for r in RELATED_MAP.get(bb_id, []) if r in by_id]
