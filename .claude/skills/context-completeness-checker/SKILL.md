---
name: context-completeness-checker
description: Use when checking whether every property key in a JSON-LD instance has a corresponding @id mapping in its @context. Walks the instance recursively, lists unmapped properties, ambiguous mappings (multiple @ids), and context terms that are declared but never used. Catches the silent "property without semantic mapping" failure that JSON Schema validation alone misses.
---

# Context Completeness Checker Skill

## Purpose

Given a JSON-LD instance and a `@context` (either inline or by path), assert that every property key in the instance has a semantic mapping (`@id`) defined in the context. Reports:

- **unmapped**: keys present in the instance but with no context entry
- **ambiguous**: keys mapped to multiple `@id`s (typically a context bug)
- **context_unused**: context terms that no instance key uses (cleanup candidate)

## Activation

Use this skill when:

- validating a rendered pygeoapi JSON-LD output against a bblock context
- auditing a published example file against its `context.jsonld`
- ensuring every property in a STAC/DCAT JSON-LD has an authoritative vocabulary mapping

Do not use this skill for:

- JSON Schema validation (use `response-schema-validator`)
- SHACL validation
- syntactic JSON-LD validity (use `pyld` for context expansion)

## Required input

- `instance` — JSON-LD object (dict or list of dicts) OR a URL to fetch
- `context` — either:
  - inline `@context` object (preferred; what pygeoapi embedded)
  - URL to a `context.jsonld`
  - file path

## Optional input

| Parameter | Default | Meaning |
|---|---|---|
| `ignore_keywords` | `["@context", "@id", "@type", "@graph", "@list", "@set", "@value", "@language", "@reverse", "@nest", "type", "id"]` | JSON-LD keywords and trivial aliases that don't need an explicit `@id` |
| `descend` | `true` | recurse into nested objects and arrays |
| `feature_path` | `properties` | when checking pygeoapi features, descend into `properties` and each feature in `features[]` |

## Process

### Phase 1 — load both

If `instance` is a URL, fetch it:

```bash
curl -sfL -H "Accept: application/ld+json" "${instance}"
```

If `context` is a URL, fetch and parse. If it's a file path, read. If inline, use directly.

### Phase 2 — collect declared terms

Walk the parsed `@context` (single object or array of objects). Build:

```python
declared = {
  "submergedInfrastructureArea": "indo:submerged-infrastructure-area",
  "symbol": "prop-rel:hasSymbol",
  # ...
}
```

Handle nested `@context` blocks inside term definitions (JSON-LD 1.1) by tracking the path: a key inside `symbols[i]` is checked against the inner `@context` first, then the outer.

### Phase 3 — walk the instance

For every object encountered (recursively):

1. for each key not in `ignore_keywords`:
   - is it declared in the current `@context` scope? → ok
   - declared multiple times in nested scopes with **different** `@id`s? → `ambiguous`
   - not declared anywhere? → `unmapped`
2. recurse into nested values when `descend=true`.

Track `used_terms` so that, after the walk, `context_unused = declared.keys() - used_terms`.

### Phase 4 — report

```json
{
  "pass":           false,
  "checked_keys":   142,
  "unmapped": [
    { "key": "windEnergyOutputMW", "first_seen_at": "features[3].properties.windEnergyOutputMW" },
    { "key": "turbineCountAdjusted", "first_seen_at": "features[3].properties.turbineCountAdjusted" }
  ],
  "ambiguous": [],
  "context_unused": [
    "fishingExclusionFraction",
    "areaUseByWindPark"
  ],
  "suggestions": [
    { "key": "windEnergyOutputMW", "suggested_id": "qudt:value", "rationale": "matches QUDT pattern" }
  ]
}
```

`pass = (unmapped == []) and (ambiguous == [])`.

`context_unused` is **informational** — does not fail the run; surface as a cleanup hint.

### Phase 5 (optional) — vocabulary lookup for `unmapped`

For each `unmapped` key, optionally try to suggest a mapping by:

- exact-string lookup in NERC P01 / CF Standard Names / Darwin Core terms (via the existing `web-browsing-mcp` skill if online)
- token similarity against terms declared in the context

This is best-effort and surfaces under `suggestions[]`. The harness can disable it with `suggest=false`.

## Outputs

The report dict above.

## Edge cases

| Situation | Handling |
|---|---|
| Context declares a term with the same `@id` twice (consistent) | Allow; not ambiguous |
| Instance has no `@context` (plain JSON) and `context=` not supplied | Fail with "no context available — supply context= or embed @context inline" |
| Context is itself an array of contexts (JSON-LD 1.1) | Walk each in order; later entries override earlier on key collisions |
| Instance is an OGC API FeatureCollection (`type=FeatureCollection`) | Auto-recurse into `features[].properties` |
| Property key uses a JSON-LD prefix (e.g. `"dwc:scientificName"`) | Pass if the prefix is declared and the suffix isn't required to be a context term |

## Interactions with other skills

- Called by `pygeoapi-test-harness` after `response-schema-validator`. Combined report is returned to the user.
- Can run standalone against any `example.json + context.jsonld` pair in a bblock — useful as a pre-commit check.

## References

- JSON-LD 1.1 (context evaluation) — https://www.w3.org/TR/json-ld11/#context-definitions
- `pyld` — https://github.com/digitalbazaar/pyld
- NERC Vocabulary Server — https://vocab.nerc.ac.uk/
