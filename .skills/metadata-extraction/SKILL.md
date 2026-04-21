# STAC and DCAT Metadata Extraction Skill

## Purpose

Extract relevant metadata from data sources (URLs, files, or samples) to populate STAC and DCAT-compliant metadata records. Detects data formats, extracts descriptive/spatial/temporal properties, and prepares data for conversion to standards-compliant JSON.

## Supported Data Formats

- **NetCDF** - Multi-dimensional scientific arrays with CF conventions
- **CSV/TSV** - Tabular data with headers and schemas
- **GeoJSON/Shapefile** - Spatial vector data
- **COG (Cloud Optimized GeoTiff)** - Geospatial raster data
- **JSON-LD** - Linked data with semantic context
- **OGC Web Services** - WMS, WFS, WMTS metadata endpoints
- **OpenAPI/OGC API Records** - API documentation and conformance

## Metadata Extraction Process

### Phase 1: Format Detection
```python
def detect_format(source_url: str) -> str:
    """Identify file format from URL path or file content."""
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

**NetCDF**:
- Dimensions (time, latitude, longitude, etc.)
- Variables with standard_name, long_name, units
- Global attributes (Conventions, title, summary, history)
- Coordinate reference system (CRS)
- Temporal extent from time dimension
- Spatial extent from lat/lon bounds

**CSV**:
- Column names and detected types
- Row count and sample data
- Null/missing value patterns
- Potential geometry columns (lat/lon, WKT)
- Categorical vs. continuous attributes

**GeoJSON**:
- Geometry types present
- Bounding box and extent
- Feature properties and schema
- Coordinate Reference System

**COG/GeoTIFF**:
- Raster dimensions and resolution
- Bands/channels
- CRS and georeferencing
- Overviews/pyramids
- Pixel data type

## Implementation

```python
import json
from typing import Dict, Any, List, Tuple
from urllib.parse import urlparse
import requests
import netCDF4

class MetadataExtractor:
    """Extract metadata from various data sources."""
    
    def __init__(self):
        self.extracted = {}
        self.missing_fields = []
    
    def extract_from_url(self, url: str) -> Dict[str, Any]:
        """Extract metadata from URL endpoint."""
        format_type = self._detect_format(url)
        
        if format_type == 'netcdf':
            return self._extract_netcdf(url)
        elif format_type == 'csv':
            return self._extract_csv(url)
        elif format_type == 'ogc-api':
            return self._extract_ogc_api(url)
        # ... additional format handlers
    
    def _extract_netcdf(self, url: str) -> Dict[str, Any]:
        """Extract metadata from NetCDF file or remote endpoint."""
        try:
            with netCDF4.Dataset(url) as ds:
                metadata = {
                    "format": "netcdf",
                    "dimensions": dict(ds.dimensions),
                    "variables": list(ds.variables.keys()),
                    "attributes": dict(ds.__dict__),
                    "spatial": self._extract_spatial_from_netcdf(ds),
                    "temporal": self._extract_temporal_from_netcdf(ds),
                    "variables_metadata": {}
                }
                
                for var_name in ds.variables.keys():
                    var = ds.variables[var_name]
                    metadata["variables_metadata"][var_name] = {
                        "standard_name": var.getncattr("standard_name") if "standard_name" in var.ncattrs() else None,
                        "long_name": var.getncattr("long_name") if "long_name" in var.ncattrs() else None,
                        "units": var.getncattr("units") if "units" in var.ncattrs() else None,
                        "dtype": str(var.dtype)
                    }
                
                return metadata
        except Exception as e:
            return {"error": str(e), "format": "netcdf"}
    
    def _extract_csv(self, url: str) -> Dict[str, Any]:
        """Extract metadata from CSV file."""
        import pandas as pd
        try:
            df = pd.read_csv(url, nrows=100)
            metadata = {
                "format": "csv",
                "columns": df.columns.tolist(),
                "dtypes": df.dtypes.astype(str).to_dict(),
                "shape": df.shape,
                "sample_data": df.head(5).to_dict(orient='records'),
                "missing_values": df.isnull().sum().to_dict(),
                "potential_geometry": self._detect_geometry_columns(df)
            }
            return metadata
        except Exception as e:
            return {"error": str(e), "format": "csv"}
    
    def _extract_spatial_from_netcdf(self, ds) -> Dict[str, Any]:
        """Extract spatial extent from NetCDF."""
        spatial = {"bounds": None, "crs": "EPSG:4326"}
        
        # Look for lat/lon variables
        for var_name in ['latitude', 'lat', 'y', 'Latitude', 'Lat']:
            if var_name in ds.variables:
                lat_var = ds.variables[var_name]
                if hasattr(lat_var, 'valid_min') and hasattr(lat_var, 'valid_max'):
                    spatial["lat_bounds"] = [lat_var.valid_min, lat_var.valid_max]
        
        for var_name in ['longitude', 'lon', 'x', 'Longitude', 'Lon']:
            if var_name in ds.variables:
                lon_var = ds.variables[var_name]
                if hasattr(lon_var, 'valid_min') and hasattr(lon_var, 'valid_max'):
                    spatial["lon_bounds"] = [lon_var.valid_min, lon_var.valid_max]
        
        return spatial
    
    def _extract_temporal_from_netcdf(self, ds) -> Dict[str, Any]:
        """Extract temporal extent from NetCDF time dimension."""
        temporal = {"start": None, "end": None, "resolution": None}
        
        for var_name in ['time', 'Time', 'datetime']:
            if var_name in ds.variables:
                time_var = ds.variables[var_name]
                times = time_var[:]
                if len(times) > 0:
                    temporal["start"] = str(times[0])
                    temporal["end"] = str(times[-1])
                    temporal["count"] = len(times)
        
        return temporal
    
    def _detect_geometry_columns(self, df) -> List[str]:
        """Detect potential geometry columns in DataFrame."""
        geometry_cols = []
        geo_keywords = ['lat', 'lon', 'latitude', 'longitude', 'x', 'y', 'wkt', 'geom', 'geometry']
        
        for col in df.columns:
            if any(keyword in col.lower() for keyword in geo_keywords):
                geometry_cols.append(col)
        
        return geometry_cols
    
    def _detect_format(self, url: str) -> str:
        """Detect data format from URL."""
        if any(ext in url.lower() for ext in ['.nc', 'netcdf']):
            return 'netcdf'
        elif any(ext in url.lower() for ext in ['.csv', '.tsv']):
            return 'csv'
        elif '.geojson' in url.lower():
            return 'geojson'
        elif any(ext in url.lower() for ext in ['.tif', '.tiff', '.cog']):
            return 'cog'
        elif 'wfs' in url.lower() or 'wms' in url.lower():
            return 'ogc-service'
        else:
            return 'unknown'
    
    def get_missing_fields(self, format_type: str) -> List[str]:
        """List required metadata fields for format/standard."""
        dcat_required = ["title", "description", "identifier", "issued", "modified", "theme", "accrualPeriodicity"]
        stac_required = ["id", "description", "extent", "links", "license"]
        
        return list(set(dcat_required + stac_required))
```

## Usage in Workflow

### Step 1: Automatic Extraction
```bash
extract_metadata(source="https://example.com/data.nc")
# Returns: {"format": "netcdf", "dimensions": {...}, "spatial": {...}, ...}
```

### Step 2: Identify Gaps
```python
missing = extractor.get_missing_fields("netcdf")
# Returns: ["title", "description", "theme", "license", ...]
```

### Step 3: Feed to User Dialog
Present extracted metadata and prompt for missing required fields.

## Integration with STAC/DCAT Agents

Output from this skill feeds into specialized agents:

- **STAC Generator**: Uses extracted spatial/temporal/format info to build Item/Catalog
- **DCAT Generator**: Uses extracted properties to populate Dataset/Distribution/Catalog
- **Format Converters**: NetCDF→STAC→JSON, CSV→JSON→RDF, etc.

## References

- [NetCDF-4 Python API](https://unidata.github.io/netcdf4-python/)
- [Pandas I/O Tools](https://pandas.pydata.org/docs/user_guide/io.html)
- [CF Conventions](http://cfconventions.org/)
- [STAC Specification](https://stacspec.org/)
- [DCAT Specification](https://www.w3.org/TR/vocab-dcat-3/)
