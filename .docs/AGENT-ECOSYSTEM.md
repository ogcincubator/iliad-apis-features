# Agents, Skills, and Commands

Canonical reference for the automation layer of `iliad-apis-features`: Claude agents under `.claude/agents/`, skills under `.claude/skills/`, and slash commands under `.claude/commands/`.

For in-IDE orientation see [`CLAUDE.md`](../CLAUDE.md). The agent-only index is [`../.claude/agents/README.md`](../.claude/agents/README.md).

## Layout

```text
.claude/
├── agents/
│   ├── integrator/     # workflow coordination, marine discovery, cross-block alignment
│   ├── converters/     # STAC/DCAT/CSV/JSON-FG conversion
│   ├── generators/     # building block authoring
│   └── validators/     # static and runtime validation
├── skills/             # focused capabilities loaded on demand
└── commands/           # user-facing slash-command entry points
```

## Slash Commands

| Command | Primary agent | Purpose |
|---|---|---|
| `/check-in <path-or-url>` | `.claude/agents/integrator/data-usability-checkin-agent.md` | Profile a source, match blocks, and stage BB1/BB2/BB3. |
| `/marine-bblock <theme> [sources]` | `.claude/agents/integrator/marine-content-specialist.md` + `.claude/agents/generators/building-block-generator.md` | Discover marine data and build an OGC block. |
| `/generate-metadata <url|path>` | `.claude/agents/converters/metadata-dispatcher.md` | Generate STAC and/or DCAT records. |
| `/geojson-to-jsonfg <path> [profile]` | `.claude/agents/converters/geojson-to-jsonfg-converter.md` | Convert GeoJSON to JSON-FG with OIM enrichment. |
| `/validate-bblock <path>` | `.claude/agents/validators/validation-agent.md` | Validate a block via Docker postprocessor. |
| `/test-bblock-rendering <path>` | `.claude/agents/validators/pygeoapi-test-harness.md` | Serve a block through pygeoapi and validate runtime responses. |
| `/vocprez-annotation <path-or-ttl>` | inline command | Add DCAT/SKOS annotations for VocPrez. |

## Agents

### Integrator

| Agent | Path | Purpose |
|---|---|---|
| `marine-workflow-orchestrator` | `.claude/agents/integrator/marine-workflow-orchestrator.md` | Routes metadata, validation, and enrichment requests across workflows. |
| `marine-content-specialist` | `.claude/agents/integrator/marine-content-specialist.md` | Discovers marine content and prepares bblock specifications. |
| `marine-data-agent` | `.claude/agents/integrator/marine-data-agent.md` | Retrieves samples from marine data services with provenance. |
| `gis-marine-data-specialist` | `.claude/agents/integrator/gis-marine-data-specialist.md` | Models geospatial vector data with semantic annotations. |
| `data-usability-checkin-agent` | `.claude/agents/integrator/data-usability-checkin-agent.md` | Runs source usability assessment and BB1/BB2/BB3 alignment. |

### Converters

| Agent | Path | Purpose |
|---|---|---|
| `metadata-dispatcher` | `.claude/agents/converters/metadata-dispatcher.md` | Detects input format and routes STAC/DCAT work. |
| `stac-metadata-generator` | `.claude/agents/converters/stac-metadata-generator.md` | Generates STAC Items and Collections. |
| `dcat-metadata-generator` | `.claude/agents/converters/dcat-metadata-generator.md` | Generates DCAT and GeoDCAT records. |
| `csv-to-stac-converter` | `.claude/agents/converters/csv-to-stac-converter.md` | Converts CSV/tabular sources to STAC metadata. |
| `csv-to-dcat-converter` | `.claude/agents/converters/csv-to-dcat-converter.md` | Converts CSV/tabular sources to DCAT metadata. |
| `geojson-to-jsonfg-converter` | `.claude/agents/converters/geojson-to-jsonfg-converter.md` | Converts GeoJSON examples to JSON-FG. |

### Generators

| Agent | Path | Purpose |
|---|---|---|
| `building-block-generator` | `.claude/agents/generators/building-block-generator.md` | Creates OGC building block source packages. |

### Validators

| Agent | Path | Purpose |
|---|---|---|
| `validation-agent` | `.claude/agents/validators/validation-agent.md` | Runs static/container building block validation. |
| `pygeoapi-test-harness` | `.claude/agents/validators/pygeoapi-test-harness.md` | Serves blocks through pygeoapi and validates runtime responses. |

## Current Skills

| Skill | Purpose |
|---|---|
| `bblock-catalog` | Catalog and classify local/imported building blocks. |
| `bblock-container-validation` | Run Docker-based building block validation. |
| `bblock-register-resolution` | Resolve imported building block registers. |
| `bblock-relevance` | Rank candidate blocks by relevance to data/examples/docs. |
| `context-completeness-checker` | Check JSON-LD context coverage for response/example properties. |
| `csv-to-metadata` | Profile CSV columns, schema, and geometry hints. |
| `dataset-qa` | Assess dataset usability and quality constraints. |
| `embedding-store` | Provide vector index operations for relevance ranking. |
| `jsonfg-conversion` | Convert GeoJSON examples to JSON-FG. |
| `metadata-extraction` | Extract metadata from files, URLs, and service descriptions. |
| `netcdf-to-stac` | Build STAC datacube/scientific metadata from NetCDF. |
| `ogc-web-services-client` | Query OGC service capabilities and data. |
| `pygeoapi-config-generator` | Generate local pygeoapi harness config. |
| `pygeoapi-jsonld-template` | Generate JSON-LD/context support for pygeoapi harnesses. |
| `pygeoapi-local-runner` | Start/stop local pygeoapi Docker harness. |
| `response-schema-validator` | Validate HTTP JSON responses against JSON Schema. |
| `web-browsing-mcp` | Fetch web resources for discovery and vocabulary/service checks. |
| `specific/esri-client` | Query ArcGIS REST services. |
| `specific/odd-to-bblock` | Convert ODD protocol material to building block examples. |

## Core Workflows

### Marine Theme to Building Block

```text
/marine-bblock
  -> integrator/marine-content-specialist
      -> integrator/marine-data-agent
      -> generators/building-block-generator
      -> validators/validation-agent
```

### Source to STAC/DCAT

```text
/generate-metadata
  -> converters/metadata-dispatcher
      -> converters/stac-metadata-generator
      -> converters/dcat-metadata-generator
      -> converters/csv-to-stac-converter
      -> converters/csv-to-dcat-converter
```

### Building Block Runtime Check

```text
/test-bblock-rendering
  -> validators/pygeoapi-test-harness
      -> pygeoapi-config-generator
      -> pygeoapi-local-runner
      -> response-schema-validator
      -> context-completeness-checker
```

## Vocabulary Priority

NERC -> CF Convention -> Darwin Core -> OBIS/WoRMS -> ICES -> EMODnet -> SOSA/SSN -> OIM -> OGC/ISO -> schema.org fallback.
