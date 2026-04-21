# Agent Ecosystem - ASCII Diagram

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              USER REQUEST                                       │
└─────────────────────┬───────────────────────────────────────────────────────────┘
                      │
                      ├──→ "Discover marine data"
                      │
                      ├──→ "Generate building blocks"
                      │
                      └──→ "Use workflow prompt"
                              │
                              ↓

┌─────────────────────────────────────────────────────────────────────────────────┐
│                           PRIMARY AGENTS                                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │                @marine-content-specialist                             │   │
│  │  ├─ Discovers marine data from HELCOM, EMODnet, ICES, OBIS, ODP     │   │
│  │  ├─ Maps properties to vocabularies (NERC, CF, Darwin Core)          │   │
│  │  ├─ Orchestrates support services                                    │   │
│  │  └─ Produces: Data profiles, vocabulary mappings, block specs        │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │                @building-block-generator                              │   │
│  │  ├─ Creates OGC building block packages                              │   │
│  │  ├─ Generates bblock.json, schema.yaml, context.jsonld              │   │
│  │  ├─ Validates with Docker OGC postprocessor                          │   │
│  │  └─ Produces: Complete validated building block packages             │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

                              ↓

┌─────────────────────────────────────────────────────────────────────────────────┐
│                        WORKFLOW ORCHESTRATION                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  @marine-workflow-orchestrator                                                    │
│  ├─ Routes metadata, validation, and format tasks                                │
│  └─ Reduces direct primary agent tool coupling                                   │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

                              ↓

┌─────────────────────────────────────────────────────────────────────────────────┐
│                           SUPPORT SERVICES                                      │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  @marine-data-specialist      @metadata-dispatcher      @validation-agent       │
│  ├─ Retrieves sample data     ├─ Generates STAC/DCAT    ├─ Semantic validation  │
│  └─ Called by orchestrator     └─ Called by orchestrator    └─ Called by orchestrator  │
│                                                                                 │
│  @geojson-to-jsonfg-converter @stac-metadata-generator @dcat-metadata-generator │
│  ├─ Converts GeoJSON→JSON-FG  ├─ Creates STAC items     ├─ Creates DCAT desc   │
│  └─ Called by orchestrator     └─ Called by orchestrator    └─ Called by orchestrator  │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

                              ↓

┌─────────────────────────────────────────────────────────────────────────────────┐
│                               SKILLS                                           │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ogc-web-services-client    web-browsing-mcp      metadata-extraction           │
│  ├─ Queries OGC services    ├─ Browses web sources ├─ Extracts metadata        │
│  └─ Used by marine-spec     └─ Used by marine-spec └─ Used by both agents      │
│                                                                                 │
│  netcdf-to-stac            csv-to-metadata         bblock-container-validation  │
│  ├─ Converts NetCDF→STAC   ├─ Converts CSV→metadata├─ Validates containers     │
│  └─ Used by bblock-gen     └─ Used by bblock-gen  └─ Used by bblock-gen       │
│                                                                                 │
│  esri-client               geojson-to-jsonfg-converter                          │
│  ├─ ESRI service client    ├─ GeoJSON→JSON-FG conversion                       │
│  └─ Available for use      └─ Available for use                                │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

                              ↓

┌─────────────────────────────────────────────────────────────────────────────────┐
│                              PROMPTS                                           │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  building-blocks-from-marine-data.md                                           │
│  ├─ Guides end-to-end workflow from marine data to building blocks            │
│  ├─ References both primary agents                                            │
│  └─ Provides command examples and troubleshooting                              │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

                              ↓

┌─────────────────────────────────────────────────────────────────────────────────┐
│                          EXTERNAL SYSTEMS                                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  HELCOM Database          EMODnet Portal          ICES Data Services           │
│  ├─ Biodiversity data     ├─ Thematic data        ├─ Fish stocks data          │
│  └─ Queried by marine-spec└─ Queried by marine-spec└─ Queried by marine-spec   │
│                                                                                 │
│  OBIS Database           ODP Features API        Docker OGC Postprocessor      │
│  ├─ Species occurrences  ├─ Feature collections  ├─ Block validation           │
│  └─ Queried by marine-spec└─ Queried by marine-spec└─ Used by bblock-gen       │
│                                                                                 │
│  OGC Building Blocks Registry                                                   │
│  ├─ Publishes validated building blocks                                        │
│  └─ Target for bblock-gen output                                               │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## Key Relationships Summary

### Orchestration Flow
```
User → Prompt → Marine Specialist → Support Services → Building Block Generator → Skills → External Systems
```

### Primary Calls
- **Marine Specialist** calls: Marine Data, Metadata Dispatcher, Validation Agent, GeoJSON Converter, STAC/DCAT Generators
- **Building Block Generator** calls: Validation Agent, Metadata Dispatcher, GeoJSON Converter

### Skill Usage
- **Marine Specialist** uses: OGC Web Services, Web Browsing, Metadata Extraction
- **Building Block Generator** uses: Metadata Extraction, NetCDF→STAC, CSV→Metadata, Container Validation

### Data Sources
- **Marine Specialist** queries: HELCOM, EMODnet, ICES, OBIS, ODP
- **Building Block Generator** validates with: Docker OGC Postprocessor
- **Output** published to: OGC Building Blocks Registry

## Quick Reference

| Component Type | Count | Location | Purpose |
|----------------|-------|----------|---------|
| Primary Agents | 2 | `.agents/` | Core specialized functionality |
| Support Services | 6 | External | Helper agents for specific tasks |
| Skills | 8 | `.skills/` | Reusable capability modules |
| Prompts | 1 | `.prompts/` | Workflow guidance |
| External Systems | 7 | External | Data sources and services |

---

**ASCII Diagram Version**: 1.0  
**Generated**: 2024-04-20  
**Source**: Agent ecosystem analysis