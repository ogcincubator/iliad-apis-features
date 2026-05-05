# Agents, Skills, and Commands

Canonical reference for the automation layer of `iliad-apis-features`: the Claude Code subagents under `.claude/agents/`, skills under `.claude/skills/`, and slash commands under `.claude/commands/` that drive marine data discovery, OGC building block generation, metadata generation, validation, and the data-usability check-in workflow.

For conceptual background see [`README.md`](../README.md), [`USAGE.md`](../USAGE.md) (generic OGC building block template), and [`PROFILES.md`](../PROFILES.md). For in-IDE orientation see [`CLAUDE.md`](../CLAUDE.md). Worked examples live under [`docs/`](../docs/).

## Layout

```
.claude/
├── agents/        # 13 subagents — autonomous workers, one .md file each
├── skills/        # 12 skills — focused capabilities loaded on demand
└── commands/      # 6 slash commands — user-facing entry points
```

The frontmatter in each agent / skill / command file is the source of truth for *when* to use it. This document covers *how the pieces fit together*.

## Slash commands

| Command | Invokes | Purpose |
|---|---|---|
| `/check-in <path-or-url>` | `data-usability-checkin-agent` (or interactive `iliad-checkin` CLI) | Profile a source, match against existing blocks, stage a triple of source / target / metadata blocks |
| `/marine-bblock <theme> [sources]` | `marine-content-specialist` → `building-block-generator` | Discover marine data and build a complete OGC block |
| `/generate-metadata <url|path>` | `metadata-dispatcher` | Generate STAC and / or DCAT records |
| `/geojson-to-jsonfg <path> [profile]` | `geojson-to-jsonfg-converter` | Convert GeoJSON to JSON-FG with OIM enrichment |
| `/validate-bblock <path>` | `validation-agent` | Validate a block via the Docker postprocessor |
| `/vocprez-annotation <path-or-ttl>` | inline (Read / Edit) | Add DCAT / SKOS annotations to RDF for VocPrez |

## Agents

Thirteen agents in three roles.

### Primary / orchestrating

Accept user requests directly and delegate.

| Agent | Model | Drives |
|---|---|---|
| `marine-content-specialist` | opus | Marine theme → BB pipeline; calls `marine-data-agent` and `building-block-generator` |
| `metadata-dispatcher` | sonnet | Format detection + STAC / DCAT routing entry point |
| `data-usability-checkin-agent` | sonnet | Source intake → BB1 / BB2 / BB3 triple with usability assessment and a process report |
| `marine-workflow-orchestrator` | sonnet | Pure router for metadata, validation, and enrichment requests; reduces direct agent-to-agent coupling |

### Authoring

| Agent | Model | Produces |
|---|---|---|
| `building-block-generator` | sonnet | Complete OGC building block packages (schema or model `itemClass`). Owns the **Quality Contract: Property Coverage**. |
| `gis-marine-data-specialist` | sonnet | JSON Schema, JSON-LD context, GeoJSON / GeoParquet examples for vector data already in hand |

### Format / output specialists

Invoked by orchestrating agents.

| Agent | Model | Purpose |
|---|---|---|
| `stac-metadata-generator` | sonnet | STAC Items / Collections with extension auto-selection |
| `dcat-metadata-generator` | sonnet | DCAT records (JSON-LD / Turtle / RDF/XML), GeoDCAT-AP profile |
| `csv-to-stac-converter` | haiku | CSV / TSV → STAC Items with table extension |
| `csv-to-dcat-converter` | haiku | CSV / TSV → DCAT records |
| `geojson-to-jsonfg-converter` | haiku | GeoJSON → JSON-FG with OIM profile (`oim`, `oim-obs`, `oim-bio-tdwg`) |

### Discovery and validation

| Agent | Model | Purpose |
|---|---|---|
| `marine-data-agent` | sonnet | Live querying of HELCOM / EMODnet / ICES / OBIS / CMEMS, sample retrieval with provenance |
| `validation-agent` | sonnet | Docker-based postprocessor validation; structure / schema / context / example / test checks |

## Skills

Loaded on demand by agents.

| Skill | Used by | Purpose |
|---|---|---|
| `metadata-extraction` | `metadata-dispatcher`, `building-block-generator` | Detect format, pull title / description / spatial / temporal / vocabulary hints |
| `csv-to-metadata` | `csv-to-stac-converter`, `csv-to-dcat-converter`, `metadata-dispatcher` | CSV column schema, geometry detection |
| `netcdf-to-stac` | `stac-metadata-generator`, `metadata-dispatcher` | NetCDF dimensions / variables / CF conventions → STAC datacube + scientific |
| `jsonfg-conversion` | `geojson-to-jsonfg-converter` | OIM-aware GeoJSON → JSON-FG conversion template |
| `bblock-container-validation` | `validation-agent`, `building-block-generator` | Docker `ogcincubator/bblocks-postprocess` runner |
| `bblock-register-resolution` | `building-block-generator`, `data-usability-checkin-agent` | Resolve published BB site URLs to register endpoints |
| `web-browsing-mcp` | `marine-data-agent`, `marine-content-specialist` | HTTP fetches for catalogues, vocabularies, services |
| `ogc-web-services-client` | `marine-data-agent` | OGC WMS / WFS / WMTS / CSW / API clients |
| `esri-client` | `marine-data-agent` | ArcGIS REST FeatureServer / MapServer / ImageServer |
| `lifewatch-data-service` | `marine-data-agent` | LifeWatch Data Service API |
| `global-fishing-watch-data-service` | `marine-data-agent` | Global Fishing Watch v3 API |
| `odd-to-bblock` | interactive | ODD Protocol text → ODD building block JSON |

## Architecture

```
                                ┌──────────────┐
                                │     User     │
                                └──────┬───────┘
                                       │  /command or @agent
        ┌──────────────────────────────┼──────────────────────────────┐
        ↓                              ↓                              ↓
┌──────────────────────┐  ┌────────────────────────┐  ┌──────────────────────────┐
│ marine-content-      │  │ metadata-dispatcher    │  │ data-usability-          │
│ specialist           │  │  (URL / file →         │  │ checkin-agent            │
│  (theme → BB)        │  │   STAC / DCAT)         │  │  (source → BB1/BB2/BB3)  │
└──────────┬───────────┘  └───────────┬────────────┘  └──────────┬───────────────┘
           │                          │                          │
           │   ┌──────────────────────┼──────────────────────────┘
           ↓   ↓                      ↓
┌──────────────────────────┐  ┌────────────────────────┐
│ building-block-generator │  │ marine-workflow-       │
│  (BB authoring;          │  │ orchestrator (router)  │
│   property-coverage      │  └─────┬──────────────────┘
│   contract owner)        │        │
└──────────┬───────────────┘        ├─→ stac-metadata-generator
           │                        ├─→ dcat-metadata-generator
           ├─→ marine-data-agent    ├─→ csv-to-{stac,dcat}-converter
           │   (sample retrieval)   ├─→ geojson-to-jsonfg-converter
           │                        └─→ validation-agent
           ├─→ validation-agent
           │   (Docker postproc)
           │
           └─→ gis-marine-data-specialist
               (semantic vector modeling)
```

Skills are loaded by individual agents per the Skills table above.

## Workflows

### W1 — Marine theme → OGC Building Block (`/marine-bblock`)

```
user → marine-content-specialist
         │
         ├─→ marine-data-agent           (sample data + provenance)
         ├─→ web-browsing-mcp /          (vocabulary lookups)
         │   ogc-web-services-client
         ├─→ metadata-extraction         (profile)
         │
         └─→ building-block-generator
                ├─→ creates _sources/<name>/ tree
                ├─→ enforces Quality Contract: Property Coverage
                ├─→ runs bblock-container-validation
                └─→ returns block + validation report
```

### W2 — Source intake → BB1 / BB2 / BB3 triple (`/check-in`)

```
user → data-usability-checkin-agent
         │
         ├─→ metadata-dispatcher              (profile + format detection)
         ├─→ score against usability matrix
         ├─→ rank candidate BB2 from
         │   _sources/ + imported registers
         │   (uses bblock-register-resolution)
         │
         ├─→ building-block-generator × 3
         │      BB1 source-data block (real source examples)
         │      BB2 target-model block (or import)
         │      BB3 metadata / catalog block (links BB1 + BB2)
         │
         ├─→ building-block-generator (BB1 → BB2 transform)
         │
         ├─→ validation-agent                 (or marine-workflow-orchestrator
         │                                     for batched validation)
         │
         └─→ writes process report to
             docs/<slug>-data-usability-checkin.md
```

The triple must satisfy the **Cross-Block Property-Coverage Contract** — every source property reaches `context.jsonld`, BB2 either maps it or documents it as a gap, and the transform either uses it or excludes it explicitly.

### W3 — Data source → STAC / DCAT (`/generate-metadata`)

```
user → metadata-dispatcher
         │
         ├─→ metadata-extraction              (auto fields)
         ├─→ ask user for missing required fields
         │
         └─→ route by format / intent
                CSV     → csv-to-stac-converter / csv-to-dcat-converter
                NetCDF  → stac-metadata-generator (uses netcdf-to-stac)
                GeoJSON / COG / OGC services
                        → stac-metadata-generator / dcat-metadata-generator
```

### W4 — GeoJSON → JSON-FG (`/geojson-to-jsonfg`)

```
user → geojson-to-jsonfg-converter
         │
         ├─→ jsonfg-conversion skill (Python template)
         ├─→ select OIM profile (oim | oim-obs | oim-bio-tdwg | auto)
         ├─→ add @context, links (conformsTo), place reference
         └─→ output JSON-FG
```

### W5 — Validate building block (`/validate-bblock`)

```
user → validation-agent
         │
         └─→ bblock-container-validation (Docker)
               structure check
               schema validity
               context completeness        (rule 1 of property-coverage contract)
               example compliance
               test execution
```

### W6 — VocPrez annotation (`/vocprez-annotation`)

Inline transformation of an RDF / Turtle file: ensure a `dcat:Catalog` exists, link the `skos:ConceptScheme`, declare `skos:hasTopConcept`, ensure every concept has `skos:inScheme` and `skos:prefLabel`, and emit Prez-compatible output.

## Quality contracts

Two contracts govern outputs. Both are enforced before validation; failures loop back to `building-block-generator`.

1. **Quality Contract: Property Coverage** — defined in `building-block-generator`. Every example property maps to `context.jsonld`; source-data blocks use real source samples with recorded provenance URLs; target-model blocks document coverage gaps in `description.md` under "Source-property coverage gaps"; transforms use every source property or list exclusions in `transforms.yaml`.
2. **Cross-Block Property-Coverage Contract** — defined in `data-usability-checkin-agent`. Restates the four rules over the BB1 / BB2 / BB3 triple and additionally requires BB3 to surface BB2's gap section.

## Vocabulary priority

When mapping properties to semantic vocabularies, agents apply this order:

NERC → CF Convention → Darwin Core → OBIS / WoRMS → ICES → EMODnet → SOSA / SSN → OIM → OGC / ISO → schema.org (fallback).

## Portability across coding agents

Most of the content in `.claude/` is platform-agnostic Markdown; the *frontmatter* and *invocation semantics* are not portable.

| Concern | Claude Code | GitHub Copilot | OpenAI Codex |
|---|---|---|---|
| Repo-level guidance | `CLAUDE.md` (also reads `AGENTS.md`) | `.github/copilot-instructions.md` | `AGENTS.md` |
| Subagent files | `.claude/agents/*.md` | `.github/chatmodes/*.chatmode.md` | none — nested `AGENTS.md` |
| Skills | `.claude/skills/<name>/SKILL.md` | none | none |
| Slash commands | `.claude/commands/*.md` (`$ARGUMENTS`) | `.github/prompts/*.prompt.md` (`{{selection}}`) | none |
| Tool allowlist | `tools: Read, Write, Bash` | `tools: ['read', 'edit', 'terminal']` | sandbox policy |

What ports cleanly: agent body Markdown, examples, JSON snippets. What does not: frontmatter, templating, tool allowlists, the skill loader (Claude-only). For multi-agent-platform repos consider [Ruler](https://github.com/intellectronica/ruler) or a small generator script over a single source of truth.

The legacy `.prompt.md` and `.prompts/*.md` files are Copilot-style standalone prompts kept for portability with non-Claude tooling; they duplicate the slash-command bodies under `.claude/commands/`.

## Worked examples

Case-study reports under [`docs/`](../docs/):

- [`fmsdi-coastal-bblocks-process.md`](../docs/fmsdi-coastal-bblocks-process.md) — FMSDI 2024 best practices encoded as building blocks
- [`nina-seapop-data-usability-checkin.md`](../docs/nina-seapop-data-usability-checkin.md) — Norwegian seabird tracking dataset, BB1 / BB2 / BB3 walkthrough
- [`seadots-dt-interoperability-framework.md`](../docs/seadots-dt-interoperability-framework.md) — three-layer DT interoperability framework

## References

- [OGC Building Blocks Specification](https://opengeospatial.github.io/bblocks/)
- [Building Block Structure](https://ogcincubator.github.io/bblocks-docs/create/structure)
- [STAC Specification](https://stacspec.org/) and [STAC extensions](https://stac-extensions.github.io/)
- [DCAT 3.0](https://www.w3.org/TR/vocab-dcat-3/) and [GeoDCAT-AP](https://semiceu.github.io/GeoDCAT-AP/)
- [OGC API Records](https://ogcapi.ogc.org/records/)
- [JSON-FG](https://docs.ogc.org/per/23-068.html)
- [OIM (Oceans Information Model)](https://github.com/ILIAD-ocean-twin/OIM)
