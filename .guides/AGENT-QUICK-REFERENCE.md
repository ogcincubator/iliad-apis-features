# Agent Quick Reference

Use this for quick lookups and common commands.

## Agent Summary

| Agent | Purpose | Use When | Output |
|-------|---------|----------|--------|
| **@marine-content-specialist** | Discover & analyze marine data | "Find jellyfish data", "Profile HELCOM", "Map vocabularies" | Data profile, vocabulary mappings, building block spec |
| **@building-block-generator** | Create & validate building blocks | "Generate block", "Validate block", "Update schema" | Complete OGC building block package |

## Decision Matrix

### Choose @marine-content-specialist For:
```
Task: Find/Discover data
    └─ @marine-content-specialist discover: "<theme>"

Task: Analyze data characteristics  
    └─ @marine-content-specialist profile: "<source>"

Task: Map to vocabularies and prepare block specification
    └─ @marine-content-specialist analyze: "<data>"
    
Task: Reconcile multiple sources
    └─ @marine-content-specialist reconcile: [sources]
```

### Choose @building-block-generator For:
```
Task: Create building block
    └─ @building-block-generator create from: <spec or data>

Task: Validate block
    └─ @building-block-generator validate: "<path>"

Task: Update block files
    └─ @building-block-generator update: "<path>"

Task: Add examples
    └─ @building-block-generator add-examples: "<path>" example.geojson

Task: Generate documentation
    └─ @building-block-generator generate-docs: "<path>"
```

## Common Commands

### Discover Jellyfish Data
```
@marine-content-specialist discover:
  marine theme: "jellyfish observations"
  geographic_focus: "HELCOM region"
  data_sources: [HELCOM, EMODnet, OBIS]
```

### Create Building Block
```
@building-block-generator create:
  from-spec: "specification.json"
  output: "_sources/macroobservation/"
  validate: true
  convert-to: ["geojson", "jsonfg"]
```

### Validate Building Block
```
@building-block-generator validate:
  block-path: "_sources/macroobservation/"
  verbose: true
  docker-check: true
```

### Reconcile Multi-Source Data
```
@marine-content-specialist reconcile:
  sources: [HELCOM, EMODnet, ICES]
  theme: "fish abundance"
  output: "harmonized-spec.json"
```

### Update & Revalidate
```
@building-block-generator update:
  block-path: "_sources/macroobservation/"
  add-examples: "new-data.geojson"

@building-block-generator validate:
  block-path: "_sources/macroobservation/"
```

## Output Examples

### Building Block Structure
```
_sources/macroobservation/
├── bblock.json              # Metadata & registration
├── schema.yaml              # JSON Schema definition
├── context.jsonld           # Vocabulary mappings
├── description.json         # Dataset description
├── examples/
│   ├── sample.geojson       # GeoJSON format
│   ├── sample.jsonfg        # JSON-FG format (OIM-enriched)
│   └── sample.geojson-ld    # GeoJSON-LD format
├── tests/
│   └── test.yaml            # Validation tests
└── README.md                # Documentation
```

### Validation Report
```json
{
  "status": "valid",
  "checks": {
    "structure": "✓",
    "schema": "✓",
    "context": "✓",
    "examples": "✓",
    "docker": "✓"
  },
  "warnings": [],
  "errors": []
}
```

## Vocabulary Priority (for @marine-content-specialist)

1. **NERC** - Physical parameters (depth, temperature, salinity)
2. **CF Convention** - Standard climate/forecast names
3. **Darwin Core** - Species, taxonomy, occurrence
4. **OBIS / WoRMS** - Marine species databases
5. **ICES** - Fish stocks, surveys, areas
6. **SOSA / SSN** - Observation semantics
7. **OIM** - Marine domain model
8. **schema.org** - General web schema fallback

## Troubleshooting Matrix

| Problem | Solution | Agent |
|---------|----------|-------|
| "Can't find data for theme" | Try different sources, search OBIS, provide sample data | @marine-content-specialist |
| "Vocabulary not mapped" | Document custom term, suggest vocab to provider | @marine-content-specialist |
| "Schema validation fails" | Check YAML syntax, verify examples conform | @building-block-generator |
| "Docker validation errors" | Run locally, check all files present | @building-block-generator |
| "Examples don't validate" | Regenerate with add-examples, verify schema | @building-block-generator |

## Data Sources

### Primary Marine Data Sources
- **HELCOM**: Biodiversity, assessments, macroobservations
- **EMODnet**: Bathymetry, habitats, human activities, biology
- **ICES**: Fish stocks, surveys, acoustic data
- **OBIS**: Marine species occurrence records
- **ODP**: OGC Features API endpoints
- **CMEMS**: Copernicus Marine Environmental Data

### Vocabulary Services
- **NERC**: http://vocab.nerc.ac.uk/ (P01 parameters)
- **CF Convention**: https://cfconventions.org/ (standard names)
- **Darwin Core**: http://rs.tdwg.org/dwc/terms/ (taxonomy)
- **ICES**: https://vocab.ices.dk/ (fish stocks, areas)
- **SOSA**: https://www.w3.org/TR/vocab-ssn/ (observations)
- **OIM**: Oceans Information Model (custom URIs)

## File Locations

```
iliad-apis-features/
├── .agents/
│   ├── .building-block-generator.md       ← Full agent definition
│   └── .marine-content-specialist.md      ← Full agent definition
│
├── .guides/
│   ├── AGENT-ARCHITECTURE.md              ← Full architecture guide
│   └── AGENT-QUICK-REFERENCE.md           ← This file
│
├── .prompts/
│   └── building-blocks-from-marine-data.md ← Workflow prompt
│
└── _sources/                               ← Created building blocks
    ├── helcom-macroobservation/
    ├── emodnet-habitat/
    └── ...
```

## Example Workflows

### Workflow 1: Jellyfish Data → Building Block (10 min)
```
1. @marine-content-specialist discover: jellyfish
2. Review data profile output
3. @building-block-generator create from spec
4. Review validation report
5. Result: _sources/macroobservation/ ready to use
```

### Workflow 2: Multi-Source Reconciliation (20 min)
```
1. @marine-content-specialist reconcile: [HELCOM, EMODnet, ICES]
2. Review harmonized mappings
3. @building-block-generator create multi-source
4. Validate all sources
5. Result: Unified building block supporting all sources
```

### Workflow 3: Batch Generation (30 min)
```
1. @marine-content-specialist discover-all from catalog
2. Generate specifications for each layer
3. @building-block-generator batch-create all
4. Validate in parallel
5. Result: Multiple validated building blocks
```

## Performance Notes

- **Single block creation**: 10-15 minutes (discovery + generation + validation)
- **Batch of 5 blocks**: 20-30 minutes (parallelizable)
- **Validation**: ~2-3 minutes per block (Docker)
- **Re-validation**: ~1-2 minutes (incremental)

## Next Steps

1. **First Time**:
   - Read `.agents/.building-block-generator.md`
   - Read `.agents/.marine-content-specialist.md`
   - Review `.guides/AGENT-ARCHITECTURE.md`

2. **Quick Start**:
   - Use workflow prompt: `.prompts/building-blocks-from-marine-data.md`
   - Follow command examples above

3. **Advanced Use**:
   - Explore multi-source reconciliation
   - Create batch building blocks
   - Set up continuous validation

## Support

- **Agent documentation**: `.agents/` folder
- **Workflow guide**: `.prompts/` folder  
- **Architecture**: `.guides/AGENT-ARCHITECTURE.md`
- **OGC Reference**: https://opengeospatial.github.io/bblocks/

---

**Last Updated**: 2024-04-20  
**Version**: 1.0  
**Quick Link**: `.agents/` & `.prompts/` folders
