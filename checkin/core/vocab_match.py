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


def match_one(property_name: str, idx: VocabIndex, k: int = 5) -> list[VocabCandidate]:
    needle = property_name.lower()
    exact = idx.by_term.get(needle) or []
    seen: set[str] = set()
    out: list[VocabCandidate] = []
    for t in exact:
        if t.uri in seen:
            continue
        seen.add(t.uri)
        out.append(_to_candidate(t, score=100))
    if len(out) >= k:
        return out[:k]

    choices = idx.all_terms()
    fuzzy = process.extract(needle, choices, scorer=fuzz.token_set_ratio, limit=max(k * 3, 10))
    for term_str, score, _ in fuzzy:
        if score < 60:
            break
        for t in idx.by_term.get(term_str, []):
            if t.uri in seen:
                continue
            seen.add(t.uri)
            out.append(_to_candidate(t, score=int(score)))
            if len(out) >= k:
                return out[:k]
    return out[:k]


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
) -> dict[str, list[VocabCandidate]]:
    return {name: match_one(name, idx, k=k) for name in property_names}


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
