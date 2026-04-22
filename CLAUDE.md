# ILIAD Marine APIs — OGC Building Blocks Repository

This repository is the source for OGC Building Blocks supporting the ILIAD Ocean Digital Twin APIs. Building blocks encode marine data standards, vocabularies, and schemas for interoperable data exchange.

## What This Repo Is

An OGC building block source repository for ILIAD marine APIs. Building blocks define how marine datasets are structured, semantically annotated, and validated. They are used to generate catalog-ready metadata (STAC, DCAT) and to publish data to OGC API Features endpoints.

## Building Block Structure

Each building block lives under `_sources/<block-name>/` and must contain:

```
_sources/<block-name>/
├── bblock.json              # OGC metadata (id, title, abstract, status, dependencies)
├── schema.json or schema.yaml   # JSON Schema for feature validation
├── context.jsonld           # JSON-LD semantic context with vocabulary mappings
├── description.json         # Dataset description (NOT README.md)
├── examples/
│   ├── sample.geojson       # GeoJSON example(s)
│   └── sample.jsonfg        # JSON-FG example with OIM enrichment
├── transforms/              # Optional YARRRML / RML transform definitions
└── tests/
    └── test.yaml            # Validation test cases
```

**Important conventions:**
- Put dataset description in `description.json`, not `README.md`
- Use `schema.json` or `schema.yaml` (not both)
- All example properties must have `@id` entries in `context.jsonld`

## Build Process

Local validation and artifact generation:

```bash
docker run --rm \
  -v $(pwd):/workspace \
  -w /workspace \
  ogcincubator/bblocks-postprocess:latest \
  python -m bblocks.process_config . --split-docs --base-url=http://localhost
```

This produces `build-local/` artifacts (HTML docs, JSON schemas, RDF). The `build/` directory contains the published artifacts.

For a quick build:
```bash
./build.sh
```

## Agent Ecosystem

Primary workflows are handled by agents in `.claude/agents/`:

### Primary Workflows

1. **Marine data → Building Block**
   - Start with `marine-content-specialist` to discover and profile marine data
   - It calls `marine-data-agent` to retrieve samples from HELCOM/EMODnet/ICES/OBIS
   - It calls `building-block-generator` to create the OGC building block package
   - Validation is coordinated via `marine-workflow-orchestrator`

2. **Data source → Metadata (STAC/DCAT)**
   - Start with `metadata-dispatcher` for any URL, file, or inline sample
   - It routes to format-specific agents: `stac-metadata-generator`, `dcat-metadata-generator`, `csv-to-stac-converter`, `csv-to-dcat-converter`

### Slash Commands

| Command | Purpose |
|---|---|
| `/validate-bblock <path>` | Validate a building block via Docker |
| `/generate-metadata <url\|path>` | Generate STAC/DCAT from a data source |
| `/geojson-to-jsonfg <path> [profile]` | Convert GeoJSON to JSON-FG with OIM |
| `/marine-bblock <theme> [sources]` | Discover marine data and generate building block |
| `/vocprez-annotation <ttl-path>` | Add DCAT/SKOS annotations for VocPrez |

## Vocabulary Priority

When mapping data properties to semantic vocabularies, use this priority order:

1. **NERC** — http://vocab.nerc.ac.uk/collection/ (physical/biological parameters)
2. **CF Convention** — climate/forecast standard names
3. **Darwin Core** — http://rs.tdwg.org/dwc/terms/ (species, occurrence)
4. **OBIS / WoRMS** — marine species and taxonomy
5. **ICES** — http://vocab.ices.dk/ (fish stocks, areas, categories)
6. **EMODnet** — thematic classifications
7. **OGC/ISO** — geospatial standards
8. **schema.org** — last resort only

## Key Sources

- `_sources/` — building block source files
- `build/` — published artifacts (generated, do not edit)
- `build-local/` — local validation artifacts (generated, do not edit)
- `bblocks-config.yaml` — repository-level OGC building blocks configuration
- `PROFILES.md` — OIM profile definitions (oim, oim-obs, oim-bio-tdwg)
- `USAGE.md` — user-facing workflow documentation

## References

- [OGC Building Blocks Specification](https://opengeospatial.github.io/bblocks/)
- [OGC Building Block Structure](https://ogcincubator.github.io/bblocks-docs/create/structure)
- [ILIAD OIM Repository](https://github.com/ILIAD-ocean-twin/OIM)
- [GeoDCAT-AP Building Blocks](https://github.com/ogcincubator/geodcat-ogcapi-records)
- [STAC Specification](https://stacspec.org/)
- [DCAT 3.0](https://www.w3.org/TR/vocab-dcat-3/)
