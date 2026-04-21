# Generate STAC and DCAT Metadata Records

Use this prompt to automatically generate STAC (SpatioTemporal Asset Catalog) and DCAT (Data Catalog Vocabulary) compliant metadata from data sources—either URLs or local file samples. The system will auto-detect format, extract metadata, prompt for missing fields, and generate standards-compliant JSON records.

## Quick Start

### Generate from URL
```
@metadata-dispatcher generate STAC and DCAT metadata from https://example.com/data.nc
```

### Generate from Local File
```
@metadata-dispatcher generate metadata from /path/to/data.csv output as STAC,DCAT
```

### Generate from Data Sample (Inline)
```
@metadata-dispatcher generate DCAT from this NetCDF data:
<paste sample headers or structure>
```

## Supported Data Formats

| Format | Detection | STAC Extensions | DCAT Output |
|--------|-----------|-----------------|-------------|
| **NetCDF** | .nc, netcdf | datacube, scientific, projection | dcat:Dataset with distribution |
| **CSV/TSV** | .csv, .tsv | table, projection | dcat:Dataset with tabular info |
| **GeoJSON** | .geojson | projection, eo | dcat:Dataset with spatial extent |
| **COG/GeoTIFF** | .tif, .tiff, .cog | eo, raster, projection | dcat:Dataset with raster info |
| **OGC API** | /collections, /items | Multiple (format-dependent) | dcat:Catalog |
| **GeoPackage** | .gpkg | projection, table | dcat:Dataset |
| **Zarr** | .zarr | datacube, scientific | dcat:Dataset with cloud-optimized |

## Input Specification

### Option 1: URL Input
```
@metadata-dispatcher generate STAC from https://data.marine.copernicus.eu/sst_data.nc
@metadata-dispatcher generate DCAT from https://data.example.com/biodiversity.csv
@metadata-dispatcher generate both from https://api.example.com/wfs?request=GetCapabilities
```

### Option 2: File Path Input
```
@metadata-dispatcher generate metadata from /Users/data/observations.geojson
@metadata-dispatcher generate STAC catalog from /Users/data/netcdf_folder/
```

### Option 3: Inline Sample
```
@metadata-dispatcher generate metadata from this CSV:
species,latitude,longitude,abundance,date
Aurelia_aurita,59.0,20.5,high,2024-04-15
Rhizostoma_pulmo,58.9,20.6,medium,2024-04-16
```

### Option 4: Multiple Sources (Batch)
```
@metadata-dispatcher generate metadata from:
- https://data1.example.com/file1.nc
- https://data2.example.com/file2.csv
- /local/path/file3.geojson
```

## Metadata Extraction (Automatic)

The system will automatically extract:

### From NetCDF Files
- **Title/Description**: From global attributes (title, summary, abstract)
- **Spatial Extent**: From latitude/longitude coordinate variables
- **Temporal Range**: From time dimension (CF-compliant)
- **Variables**: All variables with standard_name, long_name, units attributes
- **CRS**: From spatial_ref or projection metadata
- **Creator/Contact**: From author, contact, institution attributes
- **License**: From license or rights attributes

### From CSV Files
- **Column Schema**: Column names and detected data types
- **Geometry**: Detects latitude/longitude or WKT geometry columns
- **Temporal**: Identifies date/datetime columns
- **Keywords**: Extracted from column names
- **Extent**: Calculated from geographic/date columns
- **Sample Data**: First rows included for validation

### From GeoJSON/Shapefile
- **Geometry Types**: Point, LineString, Polygon, etc.
- **Properties Schema**: All feature properties
- **Coordinate Reference System**: From CRS object
- **Bounding Box**: Calculated from features
- **Feature Count**: Included in metadata

### From OGC Service Endpoints
- **Service Title/Abstract**: From GetCapabilities response
- **Available Layers**: From WMS/WFS layer list
- **Spatial Reference Systems**: From service metadata
- **Temporal Coverage**: From time dimension
- **Access URLs**: From service endpoints

## Interactive Metadata Collection

If metadata cannot be auto-detected, the system will prompt for required fields in this order:

### For DCAT (Required)
```
? Dataset title: [auto-detected or required]
? Description (2-3 sentences): [required if missing]
? Theme/Category: [select: oceans|climate|biodiversity|environment|etc.]
? License: [CC-BY-4.0|CC0|proprietary|other]
? Update Frequency: [annual|monthly|daily|never|etc.]
? Contact Email: [optional]
```

### For STAC (Required)
```
? Spatial extent confirmed? [bbox or geometry auto-detected]
? Temporal range confirmed? [start/end dates auto-detected]
? Dataset platform (satellite|model|in-situ|other): [optional]
? Processing level: [raw|processed|analysis|other]
```

## Output Formats

### Default: Both STAC and DCAT
```
@metadata-dispatcher generate metadata from data.csv
# Outputs: 
# - item.json (STAC Item)
# - record.json-ld (DCAT JSON-LD)
```

### STAC Only
```
@metadata-dispatcher generate STAC from data.csv output to item.json
```

### DCAT Only
```
@metadata-dispatcher generate DCAT from data.csv output to record.jsonld
```

### Alternative Formats
```
@metadata-dispatcher generate metadata from data.csv output as turtle
# Outputs: record.ttl (Turtle RDF)

@metadata-dispatcher generate metadata from data.csv output as rdf-xml
# Outputs: record.rdf (RDF/XML for European data portals)

@metadata-dispatcher generate metadata from data.csv output as dcat-xml
# Outputs: record.xml (DCAT-AP XML profile)
```

### Batch Output
```
@metadata-dispatcher generate metadata from folder/ output as json-ld-catalog
# Outputs: catalog.json (DCAT Catalog with all datasets)
```

## Conversion Workflows

### Workflow 1: NetCDF → STAC DataCube Item
```
@metadata-dispatcher generate STAC from https://example.com/model_output.nc
→ Auto-detects NetCDF with multiple variables
→ Applies datacube + scientific + projection extensions
→ Extracts spatial/temporal bounds, variable descriptions
→ Prompts for title, license (if missing)
→ Outputs: STAC Item with cube:variables mapping
```

**Output example:**
```json
{
  "stac_version": "1.0.0",
  "stac_extensions": ["datacube", "scientific", "projection"],
  "id": "model-output-2024",
  "description": "Climate model output",
  "assets": {
    "data": {
      "href": "https://example.com/model_output.nc",
      "cube:variables": {
        "temperature": {...},
        "precipitation": {...}
      }
    }
  }
}
```

### Workflow 2: CSV → DCAT Dataset
```
@metadata-dispatcher generate DCAT from https://example.com/species.csv
→ Auto-detects CSV tabular data
→ Extracts geometry columns (latitude, longitude)
→ Creates spatial extent from geographic data
→ Prompts for title, description, theme
→ Outputs: DCAT Record with distribution
```

**Output example:**
```json
{
  "@type": "dcat:Dataset",
  "dct:title": "Species Observations",
  "dcat:theme": ["http://purl.org/iso/25012/2008/biologicalData"],
  "dcat:distribution": {
    "dcat:accessURL": "https://example.com/species.csv",
    "dcat:mediaType": "text/csv"
  },
  "dct:spatial": {...}
}
```

### Workflow 3: GeoJSON → STAC Feature Collection
```
@metadata-dispatcher generate STAC from observations.geojson
→ Auto-detects Point/Polygon features
→ Applies projection extension
→ Extracts geometry bounds
→ Prompts for temporal coverage, license
→ Outputs: STAC Item with geometry + properties
```

### Workflow 4: OGC API → DCAT Catalog
```
@metadata-dispatcher generate DCAT from https://api.example.com/ogcapi/records
→ Auto-detects OGC API Records endpoint
→ Extracts collection metadata
→ Creates DCAT Catalog with Dataset entries for each collection
→ Outputs: DCAT Catalog JSON-LD with multiple datasets
```

## Advanced Options

### With Custom Context
```
@metadata-dispatcher generate STAC from data.csv using context=/path/to/context.jsonld
# Uses custom JSON-LD context for property mapping
```

### With Validation
```
@metadata-dispatcher generate STAC from data.csv validate against https://stacspec.org/
# Validates output against official STAC schema before output
```

### With Conformance Declaration
```
@metadata-dispatcher generate DCAT from data.csv conformsTo OGC,ISO,INSPIRE
# Adds conformance links to declared standards
```

### With Provenance Tracking
```
@metadata-dispatcher generate metadata from data.csv track-provenance
# Includes prov:wasDerivedFrom link to source
# Documents metadata generation timestamp and process
```

## Common Use Cases

### Use Case 1: Build Data Catalog for Marine Data Repository
```
@metadata-dispatcher generate DCAT from:
- https://cmems-data-portal.eu/sst.nc
- https://ices-data.dk/fish_survey.csv
- https://emodnet.eu/layers/habitats.geojson

Output: Catalog.jsonld (GeoDCAT-compliant)
# Ready for import into OGC API Records endpoint
```

### Use Case 2: Create STAC Items from Research Dataset Collection
```
@metadata-dispatcher generate STAC catalog from /research/datasets/
Output: catalog.json + items/
# Creates hierarchical STAC catalog with Items for each file
# Ready for deployment with STAC API server
```

### Use Case 3: Generate Metadata for Data Submission
```
@metadata-dispatcher generate both from /data/sample.nc
Output: 
- item.json (for STAC servers)
- record.jsonld (for DCAT portals)
# Metadata ready for multi-catalog submission
```

### Use Case 4: Validate and Convert Existing Data
```
@metadata-dispatcher generate STAC from data.nc validate inspect
# Shows detected metadata
# Prompts for any missing required fields
# Allows manual corrections before output
```

## Metadata Properties Guide

### STAC Item Properties
- `stac_version` - Always 1.0.0
- `stac_extensions` - Array of extension URIs (auto-selected)
- `id` - Unique dataset identifier
- `description` - Human-readable description
- `bbox` - [minx, miny, maxx, maxy]
- `geometry` - GeoJSON geometry
- `properties` - start_datetime, end_datetime, platform, instruments, etc.
- `assets` - Links to data files with roles: data, thumbnail, metadata
- `links` - Relationships: collection, license, derived_from, etc.

### DCAT Record Properties
- `dct:title` - Dataset name
- `dct:description` - Detailed description
- `dcat:keyword` - Search keywords
- `dcat:theme` - SKOS concept URIs
- `dcat:distribution` - Data formats and access URLs
- `dct:spatial` - Geographic extent (GeoDCAT)
- `dct:temporal` - Date range (start/end)
- `dct:issued` - Publication date
- `dct:modified` - Last update date
- `dcat:accrualPeriodicity` - Update frequency
- `dct:license` - Data license
- `dct:creator` - Creator organization
- `dcat:contactPoint` - Contact email/organization

## Output Examples

### Example: STAC Item (JSON)
```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/datacube/v2.2.0/schema.json",
    "https://stac-extensions.github.io/projection/v1.1.0/schema.json"
  ],
  "id": "helcom-macroobs-2024",
  "description": "HELCOM macroobservation data within Swedish EEZ",
  "bbox": [19, 58, 22, 60],
  "properties": {
    "start_datetime": "2020-01-01T00:00:00Z",
    "end_datetime": "2024-04-20T23:59:59Z",
    "platform": "in-situ"
  },
  "assets": {
    "data": {
      "href": "https://helcom.fi/data.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  },
  "links": [
    {
      "rel": "license",
      "href": "https://creativecommons.org/licenses/by/4.0/"
    }
  ]
}
```

### Example: DCAT Record (JSON-LD)
```json
{
  "@context": "https://www.w3.org/ns/dcat",
  "@type": "dcat:Dataset",
  "dct:title": "HELCOM Macroobservation",
  "dct:description": "Observation data from Swedish EEZ",
  "dcat:keyword": ["jellyfish", "abundance", "HELCOM"],
  "dcat:theme": ["http://purl.org/iso/25012/2008/marineData"],
  "dcat:distribution": {
    "@type": "dcat:Distribution",
    "dcat:accessURL": "https://helcom.fi/data.geojson",
    "dcat:mediaType": "application/geo+json"
  },
  "dct:issued": "2024-01-15",
  "dct:modified": "2024-04-20",
  "dct:license": "http://creativecommons.org/licenses/by/4.0/"
}
```

## Troubleshooting

**Q: "Cannot detect format from URL"**  
A: Ensure URL is publicly accessible or provide file path. Supported formats: .nc, .csv, .geojson, .tif, .gpkg

**Q: "Missing required metadata"**  
A: Agent will prompt interactively. Provide title, description, and theme at minimum.

**Q: "Cannot extract spatial extent"**  
A: Manually specify bbox=[minx, miny, maxx, maxy] or provide context file with geometry mapping.

**Q: "Output file not found"**  
A: Specify output path with `output to /path/file.json` or check working directory.

**Q: "Validation failed"**  
A: Use `validate` option to see specific schema violations. Check conformance to STAC/DCAT specs.

## Related Workflows

- **Building Block Creation**: Use generated STAC as examples in OGC building blocks
- **Data Catalog Ingestion**: Import DCAT records into OGC API Records
- **Linked Data Integration**: Export as Turtle for RDF triple stores
- **OGC API Conformance**: Use STAC/DCAT for OGC API Records endpoints

## References

- [STAC Specification](https://stacspec.org/)
- [STAC Extensions](https://stac-extensions.github.io/)
- [DCAT 3.0](https://www.w3.org/TR/vocab-dcat-3/)
- [GeoDCAT-AP](https://semiceu.github.io/GeoDCAT-AP/)
- [OGC API Records](https://ogcapi.ogc.org/records/)
- [geodcat-ogcapi-records](https://github.com/ogcincubator/geodcat-ogcapi-records)
