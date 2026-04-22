---
name: netcdf-to-stac
description: Use when converting a NetCDF file to a STAC Item with the datacube, scientific, projection, and (when applicable) eo/raster/processing extensions. Extracts dimensions, variables, CF-convention metadata (standard_name, long_name, units, time bounds), and spatial extent. Returns a standards-compliant STAC Item JSON.
---

# NetCDF to STAC Conversion Skill

## Purpose

Convert NetCDF files to STAC (SpatioTemporal Asset Catalog) Items and Collections, extracting scientific metadata and linking multi-dimensional data as STAC Assets.

## Inputs

- `netcdf_url`: URL or local path to the NetCDF file
- `dataset_id`: optional unique identifier (extracted from file attributes if not provided)
- `base_stac_url`: optional base URL for STAC links (default: http://localhost:8080/stac)
- `collection_id`: optional parent STAC Collection ID

## STAC Structure for NetCDF

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/datacube/v2.2.0/schema.json",
    "https://stac-extensions.github.io/scientific/v1.0.0/schema.json",
    "https://stac-extensions.github.io/projection/v1.1.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json"
  ],
  "id": "<dataset-id>",
  "description": "<scientific description from global attributes>",
  "geometry": {"type": "Polygon", "coordinates": []},
  "bbox": [],
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
      "cube:variables": {}
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
    lat_var = find_variable(['latitude', 'lat', 'y'], ds)
    lon_var = find_variable(['longitude', 'lon', 'x'], ds)
    if lat_var is not None and lon_var is not None:
        lat_min, lat_max = lat_var[:].min(), lat_var[:].max()
        lon_min, lon_max = lon_var[:].min(), lon_var[:].max()
        return {"bbox": [lon_min, lat_min, lon_max, lat_max], "geometry": {"type": "Polygon", "coordinates": []}}
```

### Phase 3: Temporal Extraction
```python
def extract_temporal(ds):
    time_var = find_variable(['time', 'Time'], ds)
    if time_var is not None:
        times = time_var[:]
        start_time = convert_cf_time(times[0], time_var.units)
        end_time = convert_cf_time(times[-1], time_var.units)
        return {"start_datetime": start_time.isoformat() + "Z", "end_datetime": end_time.isoformat() + "Z"}
```

### Phase 4: Variable Mapping to DataCube
```python
def map_variables_to_cube(ds):
    cube_variables = {}
    coordinate_vars = ['time', 'lat', 'lon', 'latitude', 'longitude', 'x', 'y']
    for var_name in ds.variables:
        if var_name in coordinate_vars:
            continue
        var = ds.variables[var_name]
        cube_variables[var_name] = {
            "description": var.getncattr('long_name') if 'long_name' in var.ncattrs() else var_name,
            "type": str(var.dtype),
            "dimensions": list(var.dimensions),
            "unit": var.getncattr('units') if 'units' in var.ncattrs() else None
        }
    return cube_variables
```

## Python Implementation

```python
import json
from datetime import datetime
import netCDF4
from typing import Dict, Any, List, Tuple

class NetCDFtoSTAC:
    
    def __init__(self, netcdf_url: str, base_stac_url: str = "http://localhost:8080/stac"):
        self.netcdf_url = netcdf_url
        self.base_url = base_stac_url
    
    def convert(self) -> Dict[str, Any]:
        with netCDF4.Dataset(self.netcdf_url) as ds:
            return {
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
    
    def _get_extensions(self) -> List[str]:
        return [
            "https://stac-extensions.github.io/scientific/v1.0.0/schema.json",
            "https://stac-extensions.github.io/projection/v1.1.0/schema.json",
            "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
            "https://stac-extensions.github.io/datacube/v2.2.0/schema.json"
        ]
    
    def _extract_id(self, ds) -> str:
        if 'id' in ds.ncattrs():
            return ds.getncattr('id')
        elif 'title' in ds.ncattrs():
            return ds.getncattr('title').lower().replace(' ', '-')
        return f"netcdf-{datetime.now().isoformat()}"
    
    def _extract_description(self, ds) -> str:
        for attr in ['summary', 'description', 'comment']:
            if attr in ds.ncattrs():
                return ds.getncattr(attr)
        return f"NetCDF dataset with {len(ds.variables)} variables"
    
    def _extract_assets(self, ds) -> Dict[str, Dict[str, Any]]:
        cube_vars = {
            var_name: {
                "description": ds.variables[var_name].getncattr('long_name') if 'long_name' in ds.variables[var_name].ncattrs() else var_name,
                "type": str(ds.variables[var_name].dtype),
                "unit": ds.variables[var_name].getncattr('units') if 'units' in ds.variables[var_name].ncattrs() else None
            }
            for var_name in ds.variables
            if var_name not in ['time', 'lat', 'lon', 'latitude', 'longitude', 'x', 'y']
        }
        return {"data": {"href": self.netcdf_url, "type": "application/netcdf", "roles": ["data"], "description": "Full NetCDF dataset", "cube:variables": cube_vars}}
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
  "properties": {
    "start_datetime": "2020-01-01T00:00:00Z",
    "end_datetime": "2023-12-31T23:59:59Z",
    "platform": "satellite",
    "instrument": "AVHRR"
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

- [STAC DataCube Extension](https://github.com/stac-extensions/datacube)
- [NetCDF Climate and Forecast Conventions](http://cfconventions.org/)
- [Unidata NetCDF-4 Python](https://unidata.github.io/netcdf4-python/)