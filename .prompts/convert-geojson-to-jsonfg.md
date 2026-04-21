# Convert GeoJSON to JSON-FG with OIM Context

Use this prompt to convert GeoJSON features to JSON-FG format with OIM (Oceans Information Model) semantic enrichment and linked-data context.

## Quick Start

### Basic Conversion
```
@geojson-to-jsonfg-converter convert /path/to/features.geojson to JSON-FG
```

### With OIM Profile Selection
```
@geojson-to-jsonfg-converter convert /path/to/observations.geojson to JSON-FG with oim-obs (SOSA observations)
```

```
@geojson-to-jsonfg-converter convert /path/to/biodiversity.geojson to JSON-FG with oim-bio-tdwg
```

### From Inline GeoJSON
```
@geojson-to-jsonfg-converter convert this GeoJSON feature to JSON-FG:
{
  "type": "Feature",
  "geometry": {...},
  "properties": {...}
}
```

## Supported Inputs

- **GeoJSON FeatureCollection** - Batch converts all features while preserving structure
- **Single GeoJSON Feature** - Converts individual feature with full semantic enrichment
- **CSV with Geometry** - Converts CSV rows to GeoJSON then JSON-FG
- **API Response** - Ingests GeoJSON from OGC web services (WFS, ODP, etc.)

## Conversion Modes

### OIM Base Context
```
convert ... to JSON-FG with oim
```
Use for general marine spatial data without specific observation semantics.

**Adds:**
- Links to `ogc.hosted.iliad.api.features.oim`
- Generic place references
- Data provenance metadata

### OIM Observations (SOSA)
```
convert ... to JSON-FG with oim-obs
```
Use for sensor, observation, or sampling data.

**Adds:**
- Links to `ogc.hosted.iliad.api.features.oim-obs`
- SOSA-compliant semantic properties
- ObservedProperty and FeatureOfInterest references
- Procedure and Result mappings

### OIM Biological/TDWG
```
convert ... to JSON-FG with oim-bio-tdwg
```
Use for species, biodiversity, or occurrence data.

**Adds:**
- Links to `ogc.hosted.iliad.api.features.oim-bio-tdwg`
- Darwin Core vocabulary mappings (taxonID, scientificName, etc.)
- TDWG vocabularies for taxonomic ranks
- Occurrence semantics

### Auto-Detect Profile
```
convert ... to JSON-FG with auto
```
Agent analyzes feature properties and selects appropriate OIM profile.

## Output Format

All conversions produce JSON-FG with:

```json
{
  "type": "Feature",
  "featureType": "<most apropritate featue type>",
  "crs"
  "@context": [
    "https://geojson.org/geojson-ld/geojson-context.jsonld",
    "<path-to-context.jsonld>"
  ],
  "geometry": { "type": "Point", "coordinates": [...] },
  "properties": { ... },
  "links": [
    {
      "rel": "conformsTo",
      "href": "https://opengeospatial.github.io/bblocks/ogc.geo.json-fg.feature"
    },
    {
      "rel": "conformsTo",
      "href": "https://opengeospatial.github.io/bblocks/ogc.hosted.iliad.api.features.oim"
    }
  ],
  "place": {
    "type": "Point",
    "coordinates": [...],
    "vocab": { ... }
  }
}
```

## Examples

### Example 1: Convert Marine Observation GeoJSON
```
@geojson-to-jsonfg-converter convert _sources/macroobservation/examples/sample.geojson to JSON-FG with oim-obs output to macroobservation-jsonfg.json
```

**Input (GeoJSON Feature):**
```json
{
  "type": "Feature",
  "geometry": {"type": "Point", "coordinates": [20.5, 59.0]},
  "properties": {
    "species": "Aurelia aurita",
    "abundance": "high",
    "observationTime": "2024-04-15T10:30:00Z",
    "depth_m": 5.2,
    "salinity_psu": 6.8
  }
}
```

**Output (JSON-FG with SOSA context):**
```json
{
  "type": "Feature",
  "@context": [
    "https://geojson.org/geojson-ld/geojson-context.jsonld",
    "context.jsonld"
  ],
  "geometry": {"type": "Point", "coordinates": [20.5, 59.0]},
  "properties": {
    "species": "Aurelia aurita",
    "abundance": "high",
    "observationTime": "2024-04-15T10:30:00Z",
    "depth_m": 5.2,
    "salinity_psu": 6.8
  },
  "links": [
    {"rel": "conformsTo", "href": "https://opengeospatial.github.io/bblocks/ogc.geo.json-fg.feature"},
    {"rel": "conformsTo", "href": "https://opengeospatial.github.io/bblocks/ogc.hosted.iliad.api.features.oim"},
    {"rel": "conformsTo", "href": "https://opengeospatial.github.io/bblocks/ogc.hosted.iliad.api.features.oim-obs"},
    {"rel": "conformsTo", "href": "https://opengeospatial.github.io/bblocks/ogc.hosted.iliad.api.features.oim-bio-tdwg"}
  ],
  "place": {
    "type": "Point",
    "coordinates": [20.5, 59.0],
    "vocab": {"location": "http://www.opengis.net/ont/sf#Point"}
  }
}
```

### Example 2: Batch Convert FeatureCollection
```
@geojson-to-jsonfg-converter convert biodiversity/swedish_case/species_observations.geojson to JSON-FG with oim-bio-tdwg batch output to swedish_species_jsonfg.json
```

### Example 3: Convert with Custom Context
```
@geojson-to-jsonfg-converter convert data.geojson to JSON-FG using context at _sources/macroobservation/context.jsonld
```

## Output Options

- `output to <filename>` - Save converted JSON-FG to file
- `display` - Show conversion results in terminal (default for single features)
- `summary` - Show statistics only (feature count, property coverage, etc.)
- `validation report` - Include compliance check results

## Validation Included

The agent validates each conversion against:
1. **JSON-FG Schema** - Structural compliance
2. **OIM Conformance** - Links and context mapping validity
3. **Property Coverage** - All GeoJSON properties mapped to context entries
4. **Geometry Validity** - Proper coordinate format and CRS

## Common Patterns

### Pattern 1: Raw GeoJSON to OIM-compliant JSON-FG
```
Convert geojson to json-fg with oim context
```

### Pattern 2: Observation Data with Temporal Coverage
```
Convert observations.geojson to JSON-FG preserving temporal properties with oim-obs
```

### Pattern 3: Batch Processing with Filtering
```
Convert features.geojson to JSON-FG filtering by property presence and oim-bio-tdwg
```

### Pattern 4: CSV Ingestion
```
Convert species_list.csv with geometry columns to JSON-FG with oim-bio-tdwg
```

## Related Workflows

- **Building Block Creation**: Use converted JSON-FG output as `examples.geojson` in bblock source
- **Data Validation**: Validate JSON-FG against target OIM building block schema
- **Semantic Annotation**: Use links and place objects for enhanced discoverability
- **Linked Data Export**: Convert to RDF/Turtle using JSON-LD context

## Troubleshooting

**Q: "Properties don't have context mappings"**  
A: Provide a context.jsonld file mapping properties to OIM vocabularies, or use `auto` profile for agent to infer mappings.

**Q: "Geometry type not supported"**  
A: JSON-FG supports Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, GeometryCollection. Ensure input GeoJSON uses these types.

**Q: "Links reference non-existent building blocks"**  
A: Use valid OGC building block IRIs:
- ogc.hosted.iliad.api.features.oim
- ogc.hosted.iliad.api.features.oim-bio-tdwg
- ogc.hosted.iliad.api.features.oim-obs
- ogc.geo.json-fg.feature
