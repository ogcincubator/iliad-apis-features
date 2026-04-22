---
description: Discover marine data and generate a complete OGC building block from it
argument-hint: <theme> [sources...]
---

Discover marine datasets for `$ARGUMENTS` and generate a complete, validated OGC Building Block package using the `marine-content-specialist` and `building-block-generator` agents.

Parse `$ARGUMENTS` as: `<marine-data-theme> [optional-sources]`

where sources are authoritative marine databases (HELCOM, EMODnet, ICES, OBIS, CMEMS, ODP).

## Two-Agent Workflow

### Phase 1: Discovery (marine-content-specialist)
1. Query the specified sources for the given theme
2. Profile dataset characteristics (spatial, temporal, variables)
3. Map properties to marine vocabularies (NERC, CF, Darwin Core, OBIS, ICES)
4. Identify semantic gaps and missing vocabulary URIs
5. Prepare building block specification

### Phase 2: Generation (building-block-generator)
1. Create complete folder structure at `_sources/<block-name>/`
2. Generate `bblock.json`, `schema.yaml`, `context.jsonld`, `description.json`
3. Convert examples to GeoJSON and JSON-FG with OIM enrichment
4. Declare OIM dependencies in bblock.json
5. Run Docker-based OGC postprocessor validation
6. Report validation status and any vocabulary gaps

## Examples

```
/marine-bblock jellyfish observations HELCOM EMODnet OBIS
/marine-bblock fish abundance surveys ICES CMEMS
/marine-bblock benthic habitat mapping EMODnet
/marine-bblock sea surface temperature CMEMS
```

## Output

```
_sources/<block-name>/
├── bblock.json
├── schema.yaml
├── context.jsonld
├── description.json
├── examples/
│   ├── sample.geojson
│   └── sample.jsonfg
└── tests/
    └── test.yaml
```

If `$ARGUMENTS` is empty, ask the user for a marine data theme and optional sources.
