---
description: Discover marine data and generate a complete OGC building block from it
argument-hint: <theme> [sources...]
---

Discover marine datasets for `$ARGUMENTS` and generate a complete, validated OGC Building Block package using the `marine-content-specialist` and `building-block-generator` agents.

Parse `$ARGUMENTS` as: `<marine-data-theme> [optional-sources]`

where sources are authoritative marine databases (HELCOM, EMODnet, ICES, OBIS, CMEMS, ODP).

## Two-Agent Workflow

### Phase 0: Catalog pre-check (`bblock-catalog`) — mandatory

Before any discovery or generation, run the `bblock-catalog` skill with a free-text query for `<theme>` and category filters drawn from the expected data shape (`vector` for occurrence/observation data, `gridded` for environmental fields, `metadata` for catalogue outputs, `vocabulary` for indicator concepts). The catalog inspects `_sources/` and every register in `bblocks-config.yaml` imports (geodcat-ogcapi-records, ogcapi-sosa, cross-domain-model, bblocks-sta, bblocks-stac, bblocks-openscience, bblocks-seadots). If a matching block already exists, **stop**: show the match to the user and ask whether to reuse / extend / supersede before continuing to Phase 1. Only proceed when the catalog returns no suitable match.

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
