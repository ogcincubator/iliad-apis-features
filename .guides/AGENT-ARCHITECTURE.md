# Agent Architecture & Integration Guide

## Overview

The iliad-apis-features project uses a specialized agent ecosystem for building blocks and marine data operations. This guide explains the agent roles, interactions, and how to use them effectively.

## Agent Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                   USER REQUEST                                  │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ├──→ "Generate jellyfish building block"
                      │
                      ├──→ "Create OIM-based data structure"
                      │
                      └──→ "Validate building blocks"
                          
                          ↓

┌─────────────────────────────────────────────────────────────────┐
│              PRIMARY AGENTS (Specialized)                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. @marine-content-specialist                                  │
│     ├─ ROLE: Discover & analyze marine data                    │
│     ├─ QUERIES: HELCOM, EMODnet, ICES, OBIS, ODP              │
│     ├─ OUTPUTS: Data profiles, vocabulary mappings              │
│     └─ ORCHESTRATES: @building-block-generator                 │
│                                                                  │
│  2. @building-block-generator                                   │
│     ├─ ROLE: Create & validate OGC building blocks             │
│     ├─ CREATES: bblock.json, schema, context, examples         │
│     ├─ VALIDATES: Docker OGC postprocessor                     │
│     └─ OUTPUTS: Complete building block packages               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

                      ↓

┌─────────────────────────────────────────────────────────────────┐
│                   WORKFLOW ORCHESTRATION                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  @marine-workflow-orchestrator                                  │
│  ├─ Centralizes tool-specific helper calls                      │
│  ├─ Keeps primaries focused on discovery and block creation     │
│  └─ Routes metadata, validation, and format enrichment tasks    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

                      ↓

┌─────────────────────────────────────────────────────────────────┐
│                   SUPPORT SERVICES                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  @marine-data-specialist                                        │
│  ├─ Retrieves sample marine datasets                            │
│  └─ Supports discovery and profile workflows                    │
│                                                                  │
│  @metadata-dispatcher                                           │
│  ├─ Generates STAC, DCAT, and catalog metadata                  │
│  └─ Supports both discovery and block packaging                 │
│                                                                  │
│  @validation-agent                                              │
│  ├─ Validates schema and semantic mappings                      │
│  └─ Supports block generation and quality checks                │
│                                                                  │
│  @geojson-to-jsonfg-converter                                   │
│  ├─ Converts GeoJSON to JSON-FG with OIM enrichment             │
│  └─ Supports example formatting and enrichments                │
│                                                                  │
│  @stac-metadata-generator                                       │
│  ├─ Creates STAC catalog items                                  │
│  └─ Supports metadata-rich block packages                      │
│                                                                  │
│  @dcat-metadata-generator                                       │
│  ├─ Creates DCAT dataset descriptions                           │
│  └─ Supports semantic metadata workflows                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

                      ↓

┌─────────────────────────────────────────────────────────────────┐
│                    OUTPUTS / ARTIFACTS                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Building Block Package:                                        │
│  ├─ bblock.json (OGC metadata)                                 │
│  ├─ schema.yaml (JSON Schema)                                  │
│  ├─ context.jsonld (Vocabulary mappings)                       │
│  ├─ description.json (Dataset description)                     │
│  ├─ examples/ (Sample data in multiple formats)                │
│  └─ tests/ (Validation tests)                                  │
│                                                                  │
│  Data Profile:                                                  │
│  ├─ Variable mappings to vocabularies                          │
│  ├─ Spatial/temporal coverage                                  │
│  ├─ Data quality assessment                                    │
│  └─ Dependency declarations                                    │
│                                                                  │
│  Validation Report:                                             │
│  ├─ Structure validation ✓                                     │
│  ├─ Schema validation ✓                                        │
│  ├─ Context validation ✓                                       │
│  ├─ Example validation ✓                                       │
│  └─ Docker validation ✓                                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Agent Communication Patterns

### Pattern 1: Discovery → Generation
```
User: "Generate building block for jellyfish data"
  ↓
@marine-content-specialist
  1. Discover marine content
  2. Query sources (HELCOM, EMODnet, OBIS)
  3. Analyze data characteristics
  4. Map to vocabularies
  5. Prepare building block specification
  ↓
Calls: @building-block-generator create from spec
  ↓
@building-block-generator
  1. Create folder structure
  2. Generate schema from properties
  3. Build context.jsonld from mappings
  4. Format examples
  5. Run Docker validation
  ↓
Output: Complete validated building block
```

### Pattern 2: Multi-Agent Orchestration
```
User: "Create metadata-rich building block"
  ↓
@marine-content-specialist
  → Calls: @marine-data-specialist (retrieve data)
  → Sends tool requests to: @marine-workflow-orchestrator
  ↓
@building-block-generator
  → Sends support requests to: @marine-workflow-orchestrator
  ↓
@marine-workflow-orchestrator
  → Calls: @metadata-dispatcher, @geojson-to-jsonfg-converter, @stac-metadata-generator, @dcat-metadata-generator, @validation-agent
  ↓
Output: Building block with integrated metadata
```

### Pattern 3: Batch Processing
```
User: "Generate building blocks for all EMODnet layers"
  ↓
@marine-content-specialist
  → Query EMODnet API for all layers
  → For each layer: create specification
  → Collect specifications
  ↓
@building-block-generator
  → Batch mode: process all specifications
  → Generate packages in parallel
  → Validate each
  ↓
Output: Multiple building blocks
```

## When to Use Each Agent

### Use @marine-content-specialist When:
- ✓ Discovering marine datasets
- ✓ Understanding data requirements
- ✓ Mapping data to vocabularies
- ✓ Preparing building block specifications
- ✓ Reconciling multi-source data
- ✓ Analyzing data characteristics
- ✓ Creating requirement documents

### Use @building-block-generator When:
- ✓ Creating new building blocks
- ✓ Validating existing blocks
- ✓ Updating block files
- ✓ Adding examples
- ✓ Converting data formats
- ✓ Running Docker validation
- ✓ Publishing blocks

## Task Routing Decision Tree

```
USER REQUEST
│
├─ Contains: "discover", "find", "profile", "analyze"?
│  YES → @marine-content-specialist
│
├─ Contains: "create", "generate", "build", "validate"?
│  YES → @building-block-generator
│
├─ Contains: "metadata", "catalog", "stac", "dcat"?
│  YES → @metadata-dispatcher
│
├─ Contains: "semantic", "vocabulary", "mapping"?
│  YES → @marine-content-specialist
│
└─ Contains: "multi-source", "reconcile", "harmonize"?
   YES → @marine-content-specialist
```

## Vocabulary Priority System

Agents use this priority for mapping marine data properties:

```
Priority 1: NERC (BODC/SKOS)
  → For: Physical parameters (depth, temperature, salinity)
  → Example: http://vocab.nerc.ac.uk/collection/P01/
  
Priority 2: CF Convention
  → For: Standard names (climate/forecast)
  → Example: standard_name="sea_water_salinity"
  
Priority 3: Darwin Core
  → For: Biological observations, taxonomy
  → Example: http://rs.tdwg.org/dwc/terms/scientificName
  
Priority 4: OBIS / WoRMS
  → For: Marine species, occurrences
  → Example: urn:lsid:marinespecies.org:taxname:
  
Priority 5: ICES Vocabulary
  → For: Fish stocks, surveys, areas
  → Example: ICES stock codes, area divisions
  
Priority 6: SOSA / SSN
  → For: Observation/sampling semantics
  → Example: http://www.w3.org/ns/sosa/ObservedProperty
  
Priority 7: OIM (Oceans Information Model)
  → For: Marine domain semantics
  → Example: Custom OIM properties
```

## Building Block Dependency Graph

```
Building Block Dependencies:

macroobservation
  ├─ Depends on: oim (core OIM model)
  ├─ Depends on: oim-bio-tdwg (biology extension)
  └─ May extend: ogc.geo.json-fg.feature

habitat-mapping
  ├─ Depends on: oim (core model)
  ├─ Depends on: simple-features (geometry)
  └─ May extend: ogc.json-fg

fish-abundance
  ├─ Depends on: oim (core model)
  ├─ Depends on: oim-bio-tdwg (biology)
  ├─ May reference: ices-areas
  └─ May reference: ices-stocks
```

## Workflow Examples

### Example 1: Single Building Block Creation
```
@marine-content-specialist discover:
  theme="jellyfish observations"
  geographic_focus="Swedish EEZ"
  sources=[HELCOM, EMODnet, OBIS]

@building-block-generator create:
  from-spec: <output from marine-content-specialist>
  output: "_sources/macroobservation/"
  validate: true
  
Result: _sources/macroobservation/ (complete, validated block)
```

### Example 2: Multi-Source Data Reconciliation
```
@marine-content-specialist reconcile:
  sources: [HELCOM, EMODnet, ICES]
  theme: "fish abundance"
  
  → Creates harmonized vocabulary mappings
  → Identifies common properties
  → Handles unit conversions

@building-block-generator create:
  from-spec: <harmonized specification>
  multi-source: true
  
Result: Single building block supporting all sources
```

### Example 3: Batch Building Block Generation
```
@marine-content-specialist discover-all:
  data-catalog: "https://emodnet.eu/api"
  
  → Generates specification for each layer
  
@building-block-generator batch-create:
  specifications: *.json
  parallel: true
  
Result: Multiple building blocks (one per layer)
```

### Example 4: Update & Revalidate
```
@building-block-generator update:
  block-path: "_sources/macroobservation/"
  add-examples: "new-data.geojson"
  
@building-block-generator validate:
  block-path: "_sources/macroobservation/"
  
Result: Updated, revalidated building block
```

## File Structure for Agent Configuration

```
iliad-apis-features/
├── .agents/
│   ├── .building-block-generator.md      ← Agent definition
│   ├── .marine-content-specialist.md     ← Agent definition
│   └── .README.md                         ← Agent documentation
│
├── .prompts/
│   ├── building-blocks-from-marine-data.md  ← Workflow prompt
│   └── .README.md                           ← Prompt catalog
│
├── _sources/                              ← Building blocks created
│   ├── helcom-macroobservation/
│   │   ├── bblock.json
│   │   ├── schema.yaml
│   │   ├── context.jsonld
│   │   ├── description.json
│   │   ├── examples/
│   │   └── tests/
│   └── ...
│
└── build/                                 ← Docker build artifacts
    ├── register.json
    ├── bblocks.jsonld
    └── generateddocs/
```

## Docker Validation Flow

```
@building-block-generator validate
  │
  ├─ Structure check
  │   └─ All files present, naming correct
  │
  ├─ Schema validation
  │   └─ JSON Schema syntax valid, $refs resolvable
  │
  ├─ Context validation
  │   └─ JSON-LD structure, @ids resolve to URIs
  │
  ├─ Example validation
  │   └─ Examples conform to schema
  │
  ├─ Docker run: ghcr.io/opengeospatial/bblocks-postprocess
  │   ├─ Generate build artifacts
  │   ├─ Run tests
  │   ├─ Check for errors
  │   └─ Generate documentation
  │
  └─ Output: validation_report.json
      ├─ status: "valid" | "invalid"
      ├─ checks: {...}
      ├─ errors: [...]
      └─ warnings: [...]
```

## Error Handling & Recovery

### Common Issues

**Issue 1: "Vocabulary mapping not found"**
```
Solution:
  1. Check NERC/CF/Darwin Core sources
  2. If property is custom: document with @id as local URI
  3. Add comment explaining mapping decision
  4. Suggest vocabulary to data provider
```

**Issue 2: "Building block validation fails"**
```
Solution:
  1. Run: @building-block-generator validate --verbose
  2. Check schema syntax (YAML indentation)
  3. Verify examples conform to schema
  4. Ensure all @ids are valid URIs
  5. Run locally: docker run ghcr.io/opengeospatial/bblocks-postprocess
```

**Issue 3: "Examples don't pass validation"**
```
Solution:
  1. Verify examples match schema properties
  2. Check required fields present
  3. Validate data types (string, number, etc.)
  4. Regenerate examples with: @building-block-generator add-examples
```

## Performance & Scaling

### Single Building Block
- Discovery: ~5-10 minutes (query sources)
- Generation: ~2-3 minutes (create files, validation)
- Total: ~10-15 minutes

### Multiple Building Blocks (Batch)
- Discovery: ~10-20 minutes (all sources)
- Generation: ~5-10 minutes per block (parallelizable)
- Total: ~15-30 minutes for 3-5 blocks

### Optimization Tips
1. Cache vocabulary mappings between blocks
2. Reuse contexts across similar blocks
3. Pre-generate Docker image locally
4. Use batch mode for multiple blocks

## Integration Checklist

Before using these agents:

- [ ] Read agent definitions in `.agents/` folder
- [ ] Review workflow prompts in `.prompts/` folder
- [ ] Understand building block structure in `_sources/`
- [ ] Set up Docker for validation
- [ ] Identify primary data sources (HELCOM, EMODnet, etc.)
- [ ] Plan vocabulary mappings (NERC, CF, Darwin Core, etc.)
- [ ] Test with single building block first
- [ ] Review validation reports
- [ ] Publish to OGC incubator when ready

## Related Documentation

- [Building Block Generator Agent](../.agents/.building-block-generator.md)
- [Marine Content Specialist Agent](../.agents/.marine-content-specialist.md)
- [Building Blocks from Marine Data Prompt](../.prompts/building-blocks-from-marine-data.md)
- [OGC Building Blocks Official](https://opengeospatial.github.io/bblocks/)
- [HELCOM Data Portal](https://www.helcom.fi/data/)
- [EMODnet Portal](https://www.emodnet.eu/)
- [ICES Data Services](https://www.ices.dk/)

## Quick Command Reference

```bash
# Discover marine data
@marine-content-specialist discover: "jellyfish observations"

# Generate building block from discovery
@building-block-generator create from spec

# Validate existing building block
@building-block-generator validate _sources/macroobservation/

# Update building block
@building-block-generator update _sources/macroobservation/

# Reconcile multi-source data
@marine-content-specialist reconcile: [HELCOM, EMODnet, ICES]

# Batch generate blocks
@building-block-generator batch-create: specifications/*.json

# Add examples
@building-block-generator add-examples _sources/macroobservation/ example.geojson
```

---

**Last Updated**: 2024-04-20  
**Version**: 1.0  
**Status**: Active  
