# NetCDF to STAC Conversion Skill

## Purpose

Convert NetCDF files to STAC (SpatioTemporal Asset Catalog) Items and Collections, extracting scientific metadata and linking multi-dimensional data as STAC Assets.

## STAC Structure for NetCDF

### STAC Item Structure
```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "datacube",
    "scientific",
    "projection",
    "eo",
    "raster",
    "processing"
  ],
  "id": "<dataset-id>",
  "description": "<scientific description>",
  "geometry": {...},
  "bbox": [...],
  "properties": {
    "start_datetime": "2020-01-01T00:00:00Z",
    "end_datetime": "2023-12-31T23:59:59Z",
    "platform": "extracted from metadata",
    "instruments": "extracted from metadata"
  },
  "assets": {
    "data": {
      "href": "<url-to-netcdf>",
      "type": "application/netcdf",
      "roles": ["data"],
      "description": "Multi-dimensional scientific data",
      "cube:variables": {...}
    }
  },
  "links": [
    {"rel": "collection", "href": "..."},
    {"rel": "parent", "href": "..."}
  ]
}
```

## Conversion Process

### Phase 1: File Analysis
1. Open NetCDF file with netCDF4 library
2. Extract dimensions (time, lat, lon, depth, etc.)
3. List variables with attributes (standard_name, long_name, units)
4. Parse global attributes (Conventions, title, summary, creator)

### Phase 2: Spatial Extraction
```python
def extract_spatial(ds):
    """Extract spatial bounds and CRS."""
    # Find coordinate variables
    lat_var = find_variable(['latitude', 'lat', 'y'], ds)
    lon_var = find_variable(['longitude', 'lon', 'x'], ds)
    
    if lat_var is not None and lon_var is not None:
        # Compute bounds
        lat_min, lat_max = lat_var[:].min(), lat_var[:].max()
        lon_min, lon_max = lon_var[:].min(), lon_var[:].max()
        
        return {
            "bbox": [lon_min, lat_min, lon_max, lat_max],
            "geometry": {"type": "Polygon", "coordinates": [...]}
        }
```

### Phase 3: Temporal Extraction
```python
def extract_temporal(ds):
    """Extract time bounds and intervals."""
    time_var = find_variable(['time', 'Time'], ds)
    
    if time_var is not None:
        times = time_var[:]
        # Convert from CF time units (e.g., "days since 2000-01-01")
        start_time = convert_cf_time(times[0], time_var.units)
        end_time = convert_cf_time(times[-1], time_var.units)
        
        return {
            "start_datetime": start_time.isoformat() + "Z",
            "end_datetime": end_time.isoformat() + "Z",
            "temporal_resolution": detect_frequency(times)
        }
```

### Phase 4: Variable Mapping to STAC Assets/DataCube
```python
def map_variables_to_cube(ds):
    """Create datacube representation of variables."""
    cube_variables = {}
    
    for var_name in ds.variables:
        var = ds.variables[var_name]
        
        # Skip coordinate variables
        if var_name in ['time', 'lat', 'lon', 'latitude', 'longitude', ...]:
            continue
        
        standard_name = var.getncattr('standard_name') if 'standard_name' in var.ncattrs() else None
        long_name = var.getncattr('long_name') if 'long_name' in var.ncattrs() else None
        units = var.getncattr('units') if 'units' in var.ncattrs() else None
        
        cube_variables[var_name] = {
            "description": long_name or standard_name or var_name,
            "type": str(var.dtype),
            "dimensions": list(var.dimensions),
            "unit": units,
            "attrs": dict((k, var.getncattr(k)) for k in var.ncattrs())
        }
    
    return cube_variables
```

## Implementation

```python
import json
from datetime import datetime
import netCDF4
from cf_units import Unit

class NetCDFtoSTAC:
    """Convert NetCDF files to STAC Items."""
    
    def __init__(self, netcdf_url: str, base_stac_url: str = "http://localhost:8080/stac"):
        self.netcdf_url = netcdf_url
        self.base_url = base_stac_url
    
    def convert(self) -> Dict[str, Any]:
        """Generate STAC Item from NetCDF."""
        with netCDF4.Dataset(self.netcdf_url) as ds:
            item = {
                "type": "Feature",
                "stac_version": "1.0.0",
                "stac_extensions": self._get_extensions(),
                "id": self._extract_id(ds),
                "description": self._extract_description(ds),
                "geometry": self._extract_geometry(ds),
                "bbox": self._extract_bbox(ds),
                "properties": self._extract_properties(ds),
                "assets": self._extract_assets(ds),
                "links": self._generate_links(ds)
            }
        
        return item
    
    def _get_extensions(self) -> List[str]:
        """Return applicable STAC extensions."""
        return [
            "https://stac-extensions.github.io/scientific/v1.0.0/schema.json",
            "https://stac-extensions.github.io/projection/v1.1.0/schema.json",
            "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
            "https://stac-extensions.github.io/datacube/v2.2.0/schema.json"
        ]
    
    def _extract_id(self, ds) -> str:
        """Extract or generate STAC Item ID."""
        if 'id' in ds.ncattrs():
            return ds.getncattr('id')
        elif 'title' in ds.ncattrs():
            return ds.getncattr('title').lower().replace(' ', '-')
        else:
            return f"netcdf-{datetime.now().isoformat()}"
    
    def _extract_description(self, ds) -> str:
        """Extract scientific description."""
        if 'summary' in ds.ncattrs():
            return ds.getncattr('summary')
        elif 'description' in ds.ncattrs():
            return ds.getncattr('description')
        else:
            return f"NetCDF dataset with {len(ds.variables)} variables"
    
    def _extract_geometry(self, ds) -> Dict[str, Any]:
        """Create geometry from spatial bounds."""
        bbox = self._extract_bbox(ds)
        if bbox:
            lon_min, lat_min, lon_max, lat_max = bbox
            return {
                "type": "Polygon",
                "coordinates": [[
                    [lon_min, lat_min], [lon_max, lat_min],
                    [lon_max, lat_max], [lon_min, lat_max],
                    [lon_min, lat_min]
                ]]
            }
        return None
    
    def _extract_bbox(self, ds) -> Tuple[float, float, float, float]:
        """Extract bounding box from lat/lon coordinates."""
        lat_var = self._find_var(['latitude', 'lat', 'y'], ds)
        lon_var = self._find_var(['longitude', 'lon', 'x'], ds)
        
        if lat_var and lon_var:
            return [
                float(lon_var[:].min()),
                float(lat_var[:].min()),
                float(lon_var[:].max()),
                float(lat_var[:].max())
            ]
        return None
    
    def _extract_properties(self, ds) -> Dict[str, Any]:
        """Extract temporal and other properties."""
        time_var = self._find_var(['time', 'Time'], ds)
        props = {}
        
        if time_var:
            times = time_var[:]
            props["start_datetime"] = self._cf_time_to_iso(times[0], time_var.units)
            props["end_datetime"] = self._cf_time_to_iso(times[-1], time_var.units)
        
        # Add platform/instrument metadata
        for attr in ['platform', 'instrument', 'source', 'history', 'references']:
            if attr in ds.ncattrs():
                props[attr] = ds.getncattr(attr)
        
        return props
    
    def _extract_assets(self, ds) -> Dict[str, Dict[str, Any]]:
        """Create STAC Asset entries."""
        cube_vars = {}
        for var_name in ds.variables:
            if var_name not in ['time', 'lat', 'lon', 'latitude', 'longitude', 'x', 'y']:
                var = ds.variables[var_name]
                cube_vars[var_name] = {
                    "description": var.getncattr('long_name') if 'long_name' in var.ncattrs() else var_name,
                    "type": str(var.dtype),
                    "unit": var.getncattr('units') if 'units' in var.ncattrs() else None
                }
        
        return {
            "data": {
                "href": self.netcdf_url,
                "type": "application/netcdf",
                "roles": ["data"],
                "description": "Full NetCDF dataset",
                "cube:variables": cube_vars
            }
        }
    
    def _generate_links(self, ds) -> List[Dict[str, str]]:
        """Generate STAC links."""
        links = [
            {"rel": "self", "href": f"{self.base_url}/items/{self._extract_id(ds)}.json"}
        ]
        
        if 'source_url' in ds.ncattrs():
            links.append({
                "rel": "derived_from",
                "href": ds.getncattr('source_url')
            })
        
        return links
    
    def _find_var(self, names: List[str], ds) -> Any:
        """Find first matching variable by name."""
        for name in names:
            if name in ds.variables:
                return ds.variables[name]
        return None
    
    def _cf_time_to_iso(self, cf_time: float, units_str: str) -> str:
        """Convert CF time to ISO 8601."""
        # Parse CF time units (e.g., "days since 2000-01-01")
        import cftime
        times = cftime.num2date(cf_time, units_str)
        return times.isoformat() + "Z"
```

## Output Example

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json",
    "https://stac-extensions.github.io/datacube/v2.2.0/schema.json"
  ],
  "id": "CMEMS-SST-GLO-2020-2023",
  "description": "Sea Surface Temperature global daily analysis",
  "bbox": [-180, -90, 180, 90],
  "geometry": {"type": "Polygon", "coordinates": [...]},
  "properties": {
    "start_datetime": "2020-01-01T00:00:00Z",
    "end_datetime": "2023-12-31T23:59:59Z",
    "platform": "satellite",
    "instrument": "AVHRR",
    "references": "https://data.marine.copernicus.eu/..."
  },
  "assets": {
    "data": {
      "href": "https://example.com/sst.nc",
      "type": "application/netcdf",
      "cube:variables": {
        "sea_surface_temperature": {
          "description": "Sea Surface Temperature",
          "type": "float32",
          "unit": "Kelvin"
        }
      }
    }
  }
}
```

## References

- [STAC Specification](https://stacspec.org/)
- [STAC DataCube Extension](https://github.com/stac-extensions/datacube)
- [NetCDF Climate and Forecast Conventions](http://cfconventions.org/)
- [Unidata NetCDF-4 Python](https://unidata.github.io/netcdf4-python/)
