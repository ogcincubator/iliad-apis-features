# CSV to Metadata Conversion Skill

## Purpose

Convert CSV/tabular data to STAC Items and DCAT Records with automatic schema detection, optional geometry extraction, and semantic property mapping.

## CSV Analysis & Metadata Extraction

### Phase 1: Structure Analysis
```python
def analyze_csv(filepath: str) -> Dict[str, Any]:
    """Analyze CSV structure and content."""
    df = pd.read_csv(filepath, nrows=500)
    
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "dtypes": df.dtypes.to_dict(),
        "sample": df.head(10).to_dict(orient='records'),
        "missing_pct": df.isnull().sum() / len(df) * 100,
        "numeric_ranges": df.describe().to_dict(),
        "categorical": {col: df[col].nunique() for col in df.columns if df[col].dtype == 'object'}
    }
```

### Phase 2: Geometry Detection
```python
def detect_geometry(df) -> Dict[str, str]:
    """Detect latitude, longitude, or WKT geometry columns."""
    geo_patterns = {
        'latitude': ['lat', 'latitude', 'y', 'northing'],
        'longitude': ['lon', 'lng', 'longitude', 'x', 'easting'],
        'wkt': ['geometry', 'wkt', 'geom', 'shape']
    }
    
    detected = {}
    for geo_type, patterns in geo_patterns.items():
        for col in df.columns:
            if any(p in col.lower() for p in patterns):
                detected[geo_type] = col
                break
    
    return detected
```

### Phase 3: Temporal Detection
```python
def detect_temporal(df) -> Dict[str, str]:
    """Detect date/time columns."""
    temporal = {}
    
    for col in df.columns:
        if any(x in col.lower() for x in ['date', 'time', 'year', 'month', 'day']):
            try:
                pd.to_datetime(df[col], errors='coerce')
                temporal[col] = 'datetime'
            except:
                pass
    
    return temporal
```

## STAC Item Generation from CSV

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": ["table", "projection"],
  "id": "csv-dataset-id",
  "description": "Tabular data from CSV",
  "geometry": {
    "type": "Polygon",
    "coordinates": [["minx", "miny", "maxx", "maxy"]]
  },
  "bbox": [minx, miny, maxx, maxy],
  "properties": {
    "start_datetime": "extracted from temporal column",
    "end_datetime": "extracted from temporal column"
  },
  "assets": {
    "data": {
      "href": "path/to/data.csv",
      "type": "text/csv",
      "roles": ["data"],
      "table:columns": [
        {
          "name": "column_name",
          "type": "string|number|date",
          "description": "column description"
        }
      ]
    }
  }
}
```

## DCAT Record Generation from CSV

```json
{
  "@context": "https://www.w3.org/ns/dcat",
  "@type": "dcat:Dataset",
  "dct:title": "Dataset Title",
  "dct:description": "Dataset description",
  "dcat:distribution": {
    "@type": "dcat:Distribution",
    "dcat:accessURL": "https://example.com/data.csv",
    "dcat:mediaType": "text/csv",
    "dcat:format": "CSV",
    "dcat:byteSize": 1024000
  },
  "dcat:keyword": ["extracted", "from", "column", "names"],
  "dct:spatial": {
    "@type": "dcatap:SpatialResolutionInMeters",
    "rdfs:value": resolution_meters
  },
  "dct:temporal": {
    "@type": "dct:PeriodOfTime",
    "dcat:startDate": "2020-01-01",
    "dcat:endDate": "2023-12-31"
  }
}
```

## Implementation

```python
import json
import pandas as pd
from datetime import datetime
from pathlib import Path

class CSVtoMetadata:
    """Convert CSV to STAC and DCAT metadata."""
    
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path, nrows=1000)
    
    def to_stac_item(self, dataset_id: str = None) -> Dict[str, Any]:
        """Generate STAC Item from CSV."""
        geometry, bbox = self._extract_spatial()
        start_dt, end_dt = self._extract_temporal()
        
        item = {
            "type": "Feature",
            "stac_version": "1.0.0",
            "stac_extensions": [
                "https://stac-extensions.github.io/table/v1.0.0/schema.json",
                "https://stac-extensions.github.io/projection/v1.1.0/schema.json"
            ],
            "id": dataset_id or Path(self.csv_path).stem,
            "description": f"Tabular dataset: {self.csv_path}",
            "geometry": geometry,
            "bbox": bbox,
            "properties": {
                "start_datetime": start_dt,
                "end_datetime": end_dt,
                "table:columns": self._describe_columns()
            },
            "assets": {
                "data": {
                    "href": str(self.csv_path),
                    "type": "text/csv",
                    "roles": ["data"],
                    "title": f"Data from {Path(self.csv_path).name}",
                    "table:row_count": len(self.df)
                }
            },
            "links": []
        }
        
        return item
    
    def to_dcat_record(self, title: str = None, description: str = None) -> Dict[str, Any]:
        """Generate DCAT record from CSV."""
        spatial_extent = self._extract_spatial()
        start_dt, end_dt = self._extract_temporal()
        keywords = self._extract_keywords()
        
        record = {
            "@context": "https://www.w3.org/ns/dcat",
            "@type": "dcat:Dataset",
            "dct:title": title or Path(self.csv_path).stem,
            "dct:description": description or f"Tabular data from {Path(self.csv_path).name}",
            "dcat:distribution": {
                "@type": "dcat:Distribution",
                "dcat:accessURL": str(self.csv_path),
                "dcat:mediaType": "text/csv",
                "dcat:format": "CSV",
                "dcat:byteSize": Path(self.csv_path).stat().st_size
            },
            "dcat:keyword": keywords,
            "dct:issued": datetime.now().isoformat(),
            "dct:modified": datetime.fromtimestamp(Path(self.csv_path).stat().st_mtime).isoformat()
        }
        
        if start_dt or end_dt:
            record["dct:temporal"] = {
                "@type": "dct:PeriodOfTime",
                "dcat:startDate": start_dt,
                "dcat:endDate": end_dt
            }
        
        return record
    
    def _extract_spatial(self) -> Tuple[Dict, List[float]]:
        """Extract geometry and bbox from data."""
        lat_col = None
        lon_col = None
        
        for col in self.df.columns:
            if any(x in col.lower() for x in ['lat', 'latitude', 'y']):
                lat_col = col
            if any(x in col.lower() for x in ['lon', 'lng', 'longitude', 'x']):
                lon_col = col
        
        if lat_col and lon_col:
            lat_vals = pd.to_numeric(self.df[lat_col], errors='coerce').dropna()
            lon_vals = pd.to_numeric(self.df[lon_col], errors='coerce').dropna()
            
            if len(lat_vals) > 0 and len(lon_vals) > 0:
                bbox = [
                    float(lon_vals.min()),
                    float(lat_vals.min()),
                    float(lon_vals.max()),
                    float(lat_vals.max())
                ]
                
                geometry = {
                    "type": "Polygon",
                    "coordinates": [[
                        [bbox[0], bbox[1]], [bbox[2], bbox[1]],
                        [bbox[2], bbox[3]], [bbox[0], bbox[3]],
                        [bbox[0], bbox[1]]
                    ]]
                }
                
                return geometry, bbox
        
        return None, None
    
    def _extract_temporal(self) -> Tuple[str, str]:
        """Extract start and end datetime from data."""
        start_dt = None
        end_dt = None
        
        for col in self.df.columns:
            try:
                dates = pd.to_datetime(self.df[col], errors='coerce')
                valid_dates = dates.dropna()
                
                if len(valid_dates) > 0:
                    if start_dt is None:
                        start_dt = valid_dates.min().isoformat()
                    if end_dt is None:
                        end_dt = valid_dates.max().isoformat()
                    break
            except:
                pass
        
        return start_dt, end_dt
    
    def _describe_columns(self) -> List[Dict[str, Any]]:
        """Describe CSV columns for STAC table extension."""
        columns = []
        for col in self.df.columns:
            col_type = str(self.df[col].dtype)
            if 'int' in col_type:
                stac_type = 'integer'
            elif 'float' in col_type:
                stac_type = 'number'
            elif 'object' in col_type:
                stac_type = 'string'
            else:
                stac_type = 'string'
            
            columns.append({
                "name": col,
                "type": stac_type,
                "description": col
            })
        
        return columns
    
    def _extract_keywords(self) -> List[str]:
        """Extract keywords from column names."""
        keywords = []
        for col in self.df.columns:
            # Clean column name for use as keyword
            keyword = col.lower().replace('_', ' ').strip()
            if len(keyword) > 2:
                keywords.append(keyword)
        
        return keywords[:10]  # Limit to 10 keywords
```

## References

- [STAC Table Extension](https://github.com/stac-extensions/table)
- [DCAT 3.0](https://www.w3.org/TR/vocab-dcat-3/)
- [Pandas I/O Tools](https://pandas.pydata.org/docs/user_guide/io.html)
