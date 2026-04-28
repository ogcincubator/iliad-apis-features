"""Match property names against the local vocabulary index.

Pipeline per property:
1. Exact case-insensitive hit on VocabIndex.by_term.
2. Prefix / token-set fuzzy match (rapidfuzz) on all known terms.
3. Return top-k candidates as VocabCandidate records.

Also exposes helpers for building external-lookup hints (NERC / CF / DwC) that
the UI can surface when the user clicks "search external" — actual external
lookups are delegated to the existing `web-browsing-mcp` skill and aren't
performed here.
"""
from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Iterable

from rapidfuzz import fuzz, process

from .vocab_index import VocabIndex, VocabTerm


@dataclass
class VocabCandidate:
    term: str
    uri: str
    label: str
    source: str
    kind: str
    score: int

    def as_dict(self) -> dict:
        return self.__dict__


def match_one(
    property_name: str,
    idx: VocabIndex,
    k: int = 5,
    source_priority: list[str] | None = None,
    disabled_sources: set[str] | None = None,
) -> list[VocabCandidate]:
    """Return up to *k* vocab candidates for *property_name*.

    *source_priority* is an ordered list of VocabSource ids; candidates from
    earlier sources are ranked first within the same fuzzy score band.
    *disabled_sources* is a set of VocabSource ids to exclude entirely.
    """
    needles = _candidate_needles(property_name)
    disabled = disabled_sources or set()

    def _priority(t: VocabTerm) -> int:
        if source_priority and t.source_id in source_priority:
            return source_priority.index(t.source_id)
        return 9999

    seen: set[str] = set()
    out: list[VocabCandidate] = []
    for needle in needles:
        exact = idx.by_term.get(needle) or []
        for t in sorted(exact, key=_priority):
            if t.source_id in disabled:
                continue
            if t.uri in seen:
                continue
            seen.add(t.uri)
            out.append(_to_candidate(t, score=100))
    if len(out) >= k:
        return out[:k]

    choices = idx.all_terms()
    fuzzy_choices: dict[str, int] = {}
    for needle in needles:
        fuzzy = process.extract(needle, choices, scorer=fuzz.token_set_ratio, limit=max(k * 3, 10))
        for term_str, score, _ in fuzzy:
            if score < 60:
                continue
            fuzzy_choices[term_str] = max(fuzzy_choices.get(term_str, 0), int(score))
    for term_str, score in sorted(fuzzy_choices.items(), key=lambda item: (-item[1], item[0])):
        candidates_for_term = sorted(idx.by_term.get(term_str, []), key=_priority)
        for t in candidates_for_term:
            if t.source_id in disabled:
                continue
            if t.uri in seen:
                continue
            seen.add(t.uri)
            out.append(_to_candidate(t, score=int(score)))
            if len(out) >= k:
                return out[:k]
    return out[:k]


def _candidate_needles(property_name: str) -> list[str]:
    alias_map = {
        "href": "url",
        "rel": "type",
        "class": "type",
    }
    raw = property_name.strip().lower()
    needles: list[str] = []

    def add(value: str) -> None:
        if value and value not in needles:
            needles.append(value)

    add(raw)
    leaf = re.split(r"[.\[]", raw)[-1].replace("]", "")
    add(leaf)
    if "_" in leaf:
        add(leaf.split("_")[-1])
    alias = alias_map.get(leaf)
    if alias:
        add(alias)
    return needles


def _to_candidate(t: VocabTerm, score: int) -> VocabCandidate:
    return VocabCandidate(
        term=t.term,
        uri=t.uri,
        label=t.label or t.term,
        source=t.source,
        kind=t.kind,
        score=score,
    )


def match_properties(
    property_names: Iterable[str],
    idx: VocabIndex,
    k: int = 5,
    source_priority: list[str] | None = None,
    disabled_sources: set[str] | None = None,
) -> dict[str, list[VocabCandidate]]:
    return {
        name: match_one(name, idx, k=k,
                        source_priority=source_priority,
                        disabled_sources=disabled_sources)
        for name in property_names
    }


# ---- External lookup hints (consumed by web UI / CLI) ----

EXTERNAL_VOCAB_HINTS = [
    {
        "id": "nerc-p01",
        "label": "NERC BODC Parameter Usage Vocabulary (P01)",
        "url_template": "https://vocab.nerc.ac.uk/search_nvs/P01/?query={q}",
    },
    {
        "id": "nerc-p06",
        "label": "NERC Units of Measure (P06)",
        "url_template": "https://vocab.nerc.ac.uk/search_nvs/P06/?query={q}",
    },
    {
        "id": "cf",
        "label": "CF Standard Names",
        "url_template": "https://cfconventions.org/Data/cf-standard-names/current/build/cf-standard-name-table.html",
    },
    {
        "id": "dwc",
        "label": "Darwin Core terms",
        "url_template": "https://dwc.tdwg.org/terms/",
    },
    {
        "id": "worms",
        "label": "WoRMS taxonomy",
        "url_template": "https://www.marinespecies.org/aphia.php?p=search&searchsp={q}",
    },
]


def external_hints(query: str) -> list[dict]:
    return [
        {**h, "url": h["url_template"].replace("{q}", query)}
        for h in EXTERNAL_VOCAB_HINTS
    ]
