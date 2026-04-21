# Building Blocks from Marine Data

Use this prompt to discover marine datasets, analyze their content and requirements, and generate complete OGC Building Block packages with validation.

## Quick Start

### Discover and Generate Building Block
```
@marine-content-specialist discover marine content for: jellyfish abundance data
  → identify sources (HELCOM, EMODnet, OBIS)
  → map vocabularies
  → invoke @building-block-generator create building block
```

### Validate Existing Building Block
```
@building-block-generator validate _sources/macroobservation/
```

### Generate from Marine Source
```
@marine-content-specialist profile HELCOM macroobservation
  → retrieve sample data
  → map to NERC/Darwin Core/SOSA vocabularies
  → generate building block requirements
  → create @building-block-generator specification
```

## Two-Agent Workflow

### Agent 1: Marine Content Specialist (@marine-content-specialist)

**Role**: Discover, analyze, and collect marine data requirements

**Tasks**:
- Query HELCOM, EMODnet, ICES, OBIS, ODP for data
- Profile dataset characteristics (spatial, temporal, variables)
- Map properties to marine vocabularies (NERC, CF, Darwin Core)
- Identify semantic gaps and requirements
- Prepare building block specification
- Orchestrate with other agents

**Example**:
```
@marine-content-specialist discover content:
  theme: "jellyfish observations in Swedish EEZ"
  sources: [HELCOM, EMODnet, OBIS]
  output: "building-block-spec.json"
```

**Output**:
```json
{
  "title": "HELCOM Macroobservation",
  "properties": {
    "species": {"vocabulary": "Darwin Core", "uri": "http://rs.tdwg.org/dwc/terms/scientificName"},
    "abundance": {"vocabulary": "NERC", "uri": "http://vocab.nerc.ac.uk/collection/P01/"},
    "depth_m": {"vocabulary": "NERC", "units": "m"},
    "salinity_psu": {"vocabulary": "CF", "standard_name": "sea_water_salinity"}
  },
  "spatial": {"bbox": [19, 58, 22, 60]},
  "temporal": {"start": "2020-01-01", "end": "2024-04-20"},
  "dependencies": [
    "ogc.hosted.iliad.api.features.oim",
    "ogc.hosted.iliad.api.features.oim-bio-tdwg"
  ]
}
```

### Agent 2: Building Block Generator (@building-block-generator)

**Role**: Create, structure, and validate OGC Building Block packages

**Tasks**:
- Create complete folder structure (bblock.json, schema, context, examples)
- Generate JSON Schema from properties
- Create context.jsonld with vocabulary mappings
- Format examples (GeoJSON, JSON-FG, GeoParquet)
- Validate against OGC standards
- Run Docker-based validation
- Generate documentation

**Example**:
```
@building-block-generator create from spec:
  spec_file: "building-block-spec.json"
  output: "_sources/helcom-macroobservation/"
  validate: true
```

**Output Structure**:
```
_sources/helcom-macroobservation/
├── bblock.json
├── schema.yaml
├── context.jsonld
├── description.json
├── examples/
│   ├── sample.geojson
│   ├── sample.jsonfg
│   └── sample.geojson-ld
└── tests/
    └── test.yaml
```

## Complete Workflow: Jellyfish Data → Building Block

### Step 1: Discover Marine Content
```
@marine-content-specialist discover:
  marine theme: "jellyfish observations"
  geographic focus: "HELCOM region, Swedish EEZ"
  data sources: [HELCOM, EMODnet, ICES]
```

**Agent queries:**
- HELCOM: "SELECT observations WHERE species LIKE '%jellyfish%'"
- EMODnet: Get jellyfish species distribution layer
- OBIS: Get Aurelia aurita occurrence records
- ICES: Check for jellyfish surveys

**Result**: Sample data, variable lists, metadata

### Step 2: Analyze Content
```
Agent profile analysis:
  Properties found: [species, abundance, depth, salinity, date, coordinates]
  Spatial: Point observations in bounding box [19, 58, 22, 60]
  Temporal: 2020-01-01 to 2024-04-20
  Quality: 95% completeness, authoritative sources
```

### Step 3: Map Vocabularies
```
For each property:
  species → Darwin Core scientificName
  abundance → NERC P01 abundance code
  depth_m → NERC parameter P01
  salinity_psu → CF standard_name: sea_water_salinity
  observationTime → ISO 8601 datetime
  coordinates → WGS84 + OGC Simple Features
```

### Step 4: Generate Building Block Specification
```json
{
  "title": "HELCOM Macroobservation",
  "abstract": "Marine observations of abundance and occurrence within Swedish EEZ",
  "examples": "sample.geojson",
  "properties": {
    "species": {
      "type": "string",
      "description": "Species scientific name",
      "@id": "http://rs.tdwg.org/dwc/terms/scientificName"
    },
    "abundance": {
      "type": "string",
      "enum": ["low", "medium", "high"],
      "description": "Relative abundance estimate",
      "@id": "http://vocab.nerc.ac.uk/collection/P01/"
    },
    "depth_m": {
      "type": "number",
      "description": "Water depth in meters",
      "@id": "http://vocab.nerc.ac.uk/collection/P01/P01/NDEPZZ01/",
      "units": "meters"
    }
  }
}
```

### Step 5: Generate Building Block Package
```
@building-block-generator create:
  from-spec: "spec.json"
  output: "_sources/macroobservation/"
  add-examples: "sample.geojson"
  dependencies: ["oim", "oim-bio-tdwg"]
  convert-to: ["geojson", "jsonfg"]
```

**Generator creates:**
- bblock.json with metadata and dependencies
- schema.yaml from property definitions
- context.jsonld with vocabulary URIs
- examples/sample.geojson with real data
- examples/sample.jsonfg with OIM enrichment
- tests/test.yaml for validation

### Step 6: Validate Building Block
```
@building-block-generator validate:
  block-path: "_sources/macroobservation/"
```

**Validation steps:**
1. Structure check: All required files present ✓
2. Schema validation: JSON Schema valid ✓
3. Context validation: All properties have URIs ✓
4. Example validation: Examples conform to schema ✓
5. Docker validation: OGC postprocessor check ✓
6. Semantic validation: Vocabulary URIs resolve ✓

**Output**: Validation report with status and any warnings

## Specialized Workflows

### Workflow A: Multi-Source Data Reconciliation
```
@marine-content-specialist reconcile:
  sources: [HELCOM, EMODnet, ICES]
  theme: "habitat mapping"
  
  → Identify common properties across sources
  → Map to unified vocabulary
  → Generate harmonized context.jsonld
  
@building-block-generator create:
  multi-source-context: "harmonized.jsonld"
  
  → Creates flexible schema supporting all sources
```

### Workflow B: Batch Building Block Generation
```
@marine-content-specialist discover themes: [
  "jellyfish observations",
  "fish abundance surveys",
  "benthic habitat mapping"
]

For each theme:
  → Profile marine data
  → Prepare specification
  → @building-block-generator create building block
  
Output: 3 complete, validated building blocks
```

### Workflow C: Data Catalog to Building Blocks
```
@marine-content-specialist analyze:
  data-catalog: "https://emodnet.eu/api/collections"
  extract-layers: true
  
For each layer:
  → Extract schema and sample
  → Map to vocabularies
  → Create building block spec
  
@building-block-generator batch-create:
  all-specs: "*.json"
  
Output: Building block for each catalog layer
```

## Commands Reference

### Discovery Phase
```
@marine-content-specialist discover <THEME>
@marine-content-specialist profile <SOURCE>
@marine-content-specialist analyze <DATA>
@marine-content-specialist map-vocabularies <PROPERTIES>
@marine-content-specialist reconcile <SOURCES>
```

### Generation Phase
```
@building-block-generator create from <SPEC|DATA>
@building-block-generator generate-schema <PROPERTIES>
@building-block-generator create-context <MAPPINGS>
@building-block-generator add-examples <DATA>
```

### Validation Phase
```
@building-block-generator validate <BLOCK-PATH>
@building-block-generator validate-schema <BLOCK-PATH>
@building-block-generator validate-context <BLOCK-PATH>
@building-block-generator validate-examples <BLOCK-PATH>
```

### Update Phase
```
@building-block-generator update <BLOCK-PATH>
@building-block-generator update-schema <BLOCK-PATH> --file <SCHEMA>
@building-block-generator update-context <BLOCK-PATH> --file <CONTEXT>
@building-block-generator regenerate-examples <BLOCK-PATH> --source <DATA>
```

## Output Formats

### Marine Content Profile (JSON)
```json
{
  "theme": "jellyfish observations",
  "data_sources": ["HELCOM", "EMODnet", "OBIS"],
  "properties": {...},
  "spatial_extent": {...},
  "temporal_extent": {...},
  "vocabularies": {...}
}
```

### Building Block Package (Directory Structure)
```
_sources/block-name/
├── bblock.json
├── schema.yaml
├── context.jsonld
├── description.json
├── examples/
└── tests/
```

### Validation Report (JSON)
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

## Integration with Ecosystem

```
@marine-content-specialist
  ├→ Calls: @marine-data-specialist (retrieve data)
  ├→ Calls: @marine-workflow-orchestrator (metadata/enrichment coordination)
  ├→ Calls: @building-block-generator (create)
  ├→ Uses: ogc-web-services-client skill
  └→ Uses: metadata-extraction skill

@building-block-generator
  ├→ Calls: @marine-workflow-orchestrator (validation/metadata coordination)
  ├→ Uses: Docker OGC postprocessor
  └→ Uses: metadata-extraction skill
```

## Examples

### Example 1: HELCOM Jellyfish Observations
```
@marine-content-specialist discover:
  jellyfish abundance in Swedish EEZ

Results:
  - HELCOM macroobservation database: 15,000+ records
  - Species: Aurelia aurita, Rhizostoma pulmo, Cyanea capillata
  - Properties: species, abundance, depth, salinity, date, location
  - Vocabularies: Darwin Core, NERC P01, CF Convention
  
@building-block-generator create:
  Output: _sources/helcom-macroobservation/
  Status: ✓ Valid, ✓ Examples conform, ✓ All properties mapped
```

### Example 2: EMODnet Habitat Mapping
```
@marine-content-specialist profile:
  EMODnet Habitat layer

Results:
  - Polygonal habitats: seagrass beds, coral gardens
  - Properties: habitat_type, confidence, area_m2
  - Standards: EUSeaMap, EUNIS habitat classification
  
@building-block-generator create:
  Output: _sources/emodnet-habitat/
  Dependencies: OGC Simple Features, EUNIS vocabulary
```

## Troubleshooting

**Q: "Cannot find marine data for theme"**  
A: Theme may not be available in HELCOM/EMODnet. Try:
- Search OBIS for species-level data
- Query ODP API directly
- Provide custom sample data

**Q: "Vocabulary mapping incomplete"**  
A: Some properties may not have authoritative vocabulary.
- Document custom term in context.jsonld
- Suggest vocabulary to data provider
- Create extension vocabulary if needed

**Q: "Building block validation fails"**  
A: Review validation report:
- Check schema syntax (YAML/JSON)
- Verify all examples conform to schema
- Ensure context.jsonld @id URIs resolve

## Related Documentation

- [Building Block Generator](../agents/.building-block-generator.md)
- [Marine Content Specialist](../agents/.marine-content-specialist.md)
- [OGC Building Blocks](https://opengeospatial.github.io/bblocks/)
- [HELCOM Data](https://www.helcom.fi/data/)
- [EMODnet Portal](https://www.emodnet.eu/)
- [NERC Vocabularies](http://vocab.nerc.ac.uk/)
