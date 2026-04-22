---
name: metadata-extraction
description: Use when extracting STAC/DCAT metadata from a data source — NetCDF, CSV/TSV, GeoJSON, COG, OGC services. Detects format, extracts title/description/spatial/temporal/vocabulary hints, and identifies missing required fields. Returns structured metadata ready to feed into STAC or DCAT generation agents.
---

# STAC and DCAT Metadata Extraction Skill

## Purpose

Extract relevant metadata from data sources (URLs, files, or samples) to populate STAC and DCAT-compliant metadata records. Detects data formats, extracts descriptive/spatial/temporal properties, and prepares data for conversion to standards-compliant JSON.

## Inputs

- `source`: URL or local file path to the data source
- `format`: optional format hint (netcdf | csv | geojson | cog | ogc-service)
- `standard`: target standard (stac | dcat | both)

## Supported Data Formats

- **NetCDF** - Multi-dimensional scientific arrays with CF conventions
- **CSV/TSV** - Tabular data with headers and schemas
- **GeoJSON/Shapefile** - Spatial vector data
- **COG (Cloud Optimized GeoTIFF)** - Geospatial raster data
- **JSON-LD** - Linked data with semantic context
- **OGC Web Services** - WMS, WFS, WMTS metadata endpoints
- **OpenAPI/OGC API Records** - API documentation and conformance

## Metadata Extraction Process

### Phase 1: Format Detection

```python
def detect_format(source_url: str) -> str:
    if source_url.endswith('.nc') or 'netcdf' in source_url:
        return 'netcdf'
    elif source_url.endswith('.csv') or source_url.endswith('.tsv'):
        return 'csv'
    elif source_url.endswith('.geojson'):
        return 'geojson'
    # ... additional format detection
```

### Phase 2: Metadata Retrieval

#### For URLs
- HTTP HEAD/GET to fetch headers (Content-Type, Content-Length, Last-Modified)
- Parse OpenAPI documentation if available
- Extract capabilities from OGC service endpoints
- Read RESTful API metadata endpoints

#### For Local Files
- Read file headers (magic bytes, structure)
- Parse data schema (NetCDF dimensions, CSV headers)
- Extract statistical metadata (min/max, null counts)
- Check for embedded metadata (NetCDF attributes, GeoTIFF tags)

### Phase 3: Property Extraction

**Common Metadata**:
```json
{
  "title": "extracted from file metadata or URL",
  "description": "inferred from content or variable descriptions",
  "format": "netcdf|csv|geojson|...",
  "fileSize": "bytes",
  "accessDate": "ISO 8601",
  "creator": "extracted from metadata or URL organization",
  "license": "detected or unknown",
  "rights": "extracted from metadata"
}
```

**Format-Specific Extraction**:

**NetCDF**: dimensions, variables with standard_name/long_name/units, global attributes (Conventions, title, summary, history), CRS, temporal and spatial extent from lat/lon bounds

**CSV**: column names and detected types, row count and sample data, null/missing value patterns, potential geometry columns (lat/lon, WKT), categorical vs continuous attributes

**GeoJSON**: geometry types, bounding box and extent, feature properties and schema, CRS

**COG/GeoTIFF**: raster dimensions and resolution, bands/channels, CRS and georeferencing, overviews/pyramids, pixel data type

## Implementation

```python
import json
from typing import Dict, Any, List, Tuple
from urllib.parse import urlparse
import requests
import netCDF4

class MetadataExtractor:
    
    def extract_from_url(self, url: str) -> Dict[str, Any]:
        format_type = self._detect_format(url)
        if format_type == 'netcdf':
            return self._extract_netcdf(url)
        elif format_type == 'csv':
            return self._extract_csv(url)
        elif format_type == 'ogc-api':
            return self._extract_ogc_api(url)
    
    def _extract_netcdf(self, url: str) -> Dict[str, Any]:
        with netCDF4.Dataset(url) as ds:
            return {
                "format": "netcdf",
                "dimensions": dict(ds.dimensions),
                "variables": list(ds.variables.keys()),
                "attributes": dict(ds.__dict__),
                "spatial": self._extract_spatial_from_netcdf(ds),
                "temporal": self._extract_temporal_from_netcdf(ds),
                "variables_metadata": {
                    var_name: {
                        "standard_name": ds.variables[var_name].getncattr("standard_name") if "standard_name" in ds.variables[var_name].ncattrs() else None,
                        "long_name": ds.variables[var_name].getncattr("long_name") if "long_name" in ds.variables[var_name].ncattrs() else None,
                        "units": ds.variables[var_name].getncattr("units") if "units" in ds.variables[var_name].ncattrs() else None,
                    }
                    for var_name in ds.variables.keys()
                }
            }
    
    def _extract_csv(self, url: str) -> Dict[str, Any]:
        import pandas as pd
        df = pd.read_csv(url, nrows=100)
        return {
            "format": "csv",
            "columns": df.columns.tolist(),
            "dtypes": df.dtypes.astype(str).to_dict(),
            "shape": df.shape,
            "sample_data": df.head(5).to_dict(orient='records'),
            "missing_values": df.isnull().sum().to_dict(),
            "potential_geometry": self._detect_geometry_columns(df)
        }
    
    def _detect_geometry_columns(self, df) -> List[str]:
        geo_keywords = ['lat', 'lon', 'latitude', 'longitude', 'x', 'y', 'wkt', 'geom', 'geometry']
        return [col for col in df.columns if any(keyword in col.lower() for keyword in geo_keywords)]
    
    def get_missing_fields(self, format_type: str) -> List[str]:
        dcat_required = ["title", "description", "identifier", "issued", "modified", "theme", "accrualPeriodicity"]
        stac_required = ["id", "description", "extent", "links", "license"]
        return list(set(dcat_required + stac_required))
```

## Integration with STAC/DCAT Agents

Output from this skill feeds into specialized agents:

- **stac-metadata-generator**: Uses extracted spatial/temporal/format info to build Item/Catalog
- **dcat-metadata-generator**: Uses extracted properties to populate Dataset/Distribution/Catalog
- **csv-to-stac-converter**, **csv-to-dcat-converter**: CSV-specific conversions

## References

- [NetCDF-4 Python API](https://unidata.github.io/netcdf4-python/)
- [CF Conventions](http://cfconventions.org/)
- [STAC Specification](https://stacspec.org/)
- [DCAT Specification](https://www.w3.org/TR/vocab-dcat-3/)