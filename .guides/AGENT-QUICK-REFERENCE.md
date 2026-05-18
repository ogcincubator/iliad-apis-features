# Agent Quick Reference

Use this for quick lookup. The full index is `.claude/agents/README.md`; the ecosystem reference is `.docs/AGENT-ECOSYSTEM.md`.

## Agent Folders

| Folder | Use for |
|---|---|
| `.claude/agents/integrator/` | workflow orchestration, marine discovery, cross-block alignment |
| `.claude/agents/converters/` | STAC, DCAT, CSV, and JSON-FG conversion |
| `.claude/agents/generators/` | building block package generation |
| `.claude/agents/validators/` | static validation and pygeoapi runtime tests |

## Common Routing

| User intent | Agent path |
|---|---|
| Discover/profile marine data | `.claude/agents/integrator/marine-content-specialist.md` |
| Retrieve marine samples | `.claude/agents/integrator/marine-data-agent.md` |
| Create/update a building block | `.claude/agents/generators/building-block-generator.md` |
| Generate STAC/DCAT metadata | `.claude/agents/converters/metadata-dispatcher.md` |
| Convert CSV to STAC | `.claude/agents/converters/csv-to-stac-converter.md` |
| Convert CSV to DCAT | `.claude/agents/converters/csv-to-dcat-converter.md` |
| Convert GeoJSON to JSON-FG | `.claude/agents/converters/geojson-to-jsonfg-converter.md` |
| Validate a building block | `.claude/agents/validators/validation-agent.md` |
| Serve/test a block with pygeoapi | `.claude/agents/validators/pygeoapi-test-harness.md` |
| Run a data usability check-in | `.claude/agents/integrator/data-usability-checkin-agent.md` |

## Common Commands

```text
/marine-bblock jellyfish observations HELCOM EMODnet OBIS
/generate-metadata /path/to/source.csv
/geojson-to-jsonfg examples/sample.geojson oim-obs
/validate-bblock _sources/<block-name>
/test-bblock-rendering _sources/<block-name> --keep-running
/check-in /path/or/url
```

## Building Block Output Shape

```text
_sources/<block-name>/
├── bblock.json
├── schema.yaml or schema.json
├── context.jsonld
├── description.md or description.json
├── examples/
└── tests/
```

## Vocabulary Priority

NERC -> CF Convention -> Darwin Core -> OBIS/WoRMS -> ICES -> EMODnet -> SOSA/SSN -> OIM -> OGC/ISO -> schema.org fallback.
