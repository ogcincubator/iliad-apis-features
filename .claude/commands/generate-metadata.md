---
description: Generate STAC and/or DCAT metadata records from a URL, file path, or inline data sample
argument-hint: <url|path|inline-sample>
---

Generate STAC and DCAT metadata from `$ARGUMENTS` using the `metadata-dispatcher` agent.

The dispatcher will:
1. Detect the data format (NetCDF, CSV, GeoJSON, COG, OGC service)
2. Extract metadata automatically (title, description, spatial extent, temporal range, variables)
3. Prompt for any missing required fields (DCAT: title, description, theme, license; STAC: license, extent)
4. Route to the appropriate specialized agent based on format and desired output
5. Output standards-compliant STAC Item JSON and/or DCAT Record JSON-LD

## Supported Formats

| Format | STAC Extensions | DCAT Output |
|--------|-----------------|-------------|
| NetCDF | datacube, scientific, projection | dcat:Dataset with distribution |
| CSV/TSV | table, projection | dcat:Dataset with tabular info |
| GeoJSON | projection | dcat:Dataset with spatial extent |
| COG/GeoTIFF | eo, raster, projection | dcat:Dataset with raster info |
| OGC API | format-dependent | dcat:Catalog |

## Examples

```
/generate-metadata https://data.marine.copernicus.eu/sst_data.nc
/generate-metadata /path/to/observations.csv
/generate-metadata https://api.example.com/wfs?request=GetCapabilities
```

If `$ARGUMENTS` is empty, ask the user for a data source URL, file path, or inline sample.
