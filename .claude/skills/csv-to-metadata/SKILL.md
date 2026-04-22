---
name: csv-to-metadata
description: Use when converting CSV or TSV tabular data into STAC Items and/or DCAT Records. Detects lat/lon or WKT geometry, temporal columns, and column schema for the STAC table extension. Returns structured STAC Item and/or DCAT Record JSON ready for output.
---

# CSV to Metadata Conversion Skill

## Purpose

Convert CSV or TSV tabular data to STAC metadata, DCAT metadata, or both.

This skill is for structured metadata generation from tabular files. It should:

- inspect the file structure and sample values
- detect spatial and temporal coverage when possible
- derive or request core metadata fields
- propose theme and title values when they are missing
- return output in STAC, DCAT, or both formats

## Activation

Use this skill when the user asks to:

- convert a CSV or TSV into metadata
- generate STAC from tabular data
- generate DCAT from tabular data
- inspect a CSV or TSV to derive dataset metadata

Do not use this skill for:

- GeoJSON, NetCDF, RDF, XML, or database-native inputs
- general CSV analysis that is not about metadata generation
- full OGC Building Block generation

## Required Input

- `filepath`: mandatory path to a CSV or TSV file

If `filepath` is missing, ask exactly:

`Please provide the path to the CSV or TSV file you want to convert.`

Do not continue until a file path is provided.

## Optional Inputs

- `identifier`: explicit identifier to use as `dataset_id`
- `baseurl`: base URL used to derive a stable `dataset_id` when `identifier` is not provided
- `title`: human-readable title
- `description`: dataset description
- `theme`: SKOS theme URI or keyword
- `license`: license identifier such as `CC-BY-4.0` or `CC0`
- `output`: `stac`, `dcat`, or `both`

## Defaults And Fallbacks

- `identifier`: if missing, derive `dataset_id` from `baseurl` plus filename stem when `baseurl` is available; otherwise use the filename stem
- `baseurl`: optional helper for identifier and access URL construction
- `description`: if missing, generate a concise description from the filename, columns, and detected spatial or temporal extent
- `title`: if missing, propose one at the end of the analysis
- `theme`: if missing, propose candidate themes from known theme registers and ask the user to confirm or replace them
- `license`: if missing, omit it and say license information was not provided
- `output`: if missing, default to `both`

## Decision Rules

### Identifier Rules

Determine `dataset_id` using this priority:

1. user-provided `identifier`
2. derived from `baseurl` plus sanitized filename stem
3. sanitized filename stem

Examples:

- `identifier=helcom-stations` -> `dataset_id: "helcom-stations"`
- `baseurl=https://example.org/datasets` and file `stations.csv` -> `dataset_id: "https://example.org/datasets/stations"` or a sanitized derivative if only an ID is needed
- file `stations.csv` only -> `dataset_id: "stations"`

### Theme Rules

If `theme` is not provided, do not silently invent a final theme value.

Instead:

1. analyze the description, filename, column names, sample values, geometry, and time coverage
2. match the dataset against known theme registers available to the workflow
3. propose one or more likely themes with labels and URIs where possible
4. ask the user to confirm or replace the proposed theme or themes

Use wording like:

`Based on the data and description, and using the available theme registers, the proposed themes are: ... Is that OK, or would you like to propose another?`

Prefer theme concepts from known SKOS-based theme registers relevant to catalog metadata, such as:

- GeoDCAT-AP or DCAT-compatible theme vocabularies used in the metadata workflow
- GEMET or INSPIRE-style environmental themes when the dataset is geospatial or environmental
- local project or domain theme registers when the repository workflow or the user provides them

If multiple registers are available, prefer the most domain-appropriate and standards-aligned one.

If no authoritative register can be identified locally, say so and propose keyword-based placeholder themes for confirmation.

Present themes as a short candidate list, for example:

- `Oceanography` — `<theme-uri>`
- `Marine environment` — `<theme-uri>`
- `Biodiversity` — `<theme-uri>`

Explain briefly why they were chosen, based on the data and description.

Do not finalize `dcat:theme` until the user confirms, unless the user explicitly asks for automatic inference without confirmation.

### Title Rules

If `title` is not provided, propose it at the end of the analysis, after description, column semantics, spatial extent, temporal extent, and grouping have been detected.

Build the proposed title from:

1. user-provided or generated `description`
2. filename stem as fallback subject
3. meaningful column names or detected subject terms
4. spatial extent
5. temporal extent
6. dominant sociological grouping or category

Do not finalize the title until the earlier extraction steps have completed.

For geospatial datasets, include the detected bounding box when helpful.

Preferred pattern:

`<subject> for bbox <minx>, <miny>, <maxx>, <maxy>`

For temporal datasets, include the detected time range.

Preferred pattern:

`<subject> for <start> to <end>`

For sociological or grouped datasets, include the dominant grouping column when present.

Typical grouping columns include:

- `group`
- `category`
- `sex`
- `gender`
- `age_group`
- `household_type`
- `income_band`
- `education_level`
- `region`
- `community`
- `occupation`

Preferred pattern:

`<subject> by <grouping>`

When multiple extents are available, combine them concisely.

Preferred pattern:

`<subject> by <grouping> for <time-period> in bbox <minx>, <miny>, <maxx>, <maxy>`

## Workflow

### Phase 1: Structure Analysis

- read the CSV or TSV
- inspect up to a reasonable sample size
- identify rows, columns, dtypes, null rates, numeric ranges, and representative values

### Phase 2: Spatial Detection

- detect latitude and longitude columns
- detect WKT or geometry-like columns
- derive geometry and bbox when possible

### Phase 3: Temporal Detection

- detect date or time-like columns
- parse them conservatively
- derive start and end temporal extent

### Phase 4: Subject Detection

- infer the dataset subject from description, filename, column names, and representative values
- detect likely domains such as marine, environmental, socioeconomic, biodiversity, monitoring, or survey data
- detect dominant grouping columns for sociological or grouped datasets

### Phase 5: Metadata Synthesis

- derive `dataset_id`
- generate or refine `description`
- propose `theme` if missing
- propose `title` if missing
- assemble STAC, DCAT, or both depending on `output`

### Phase 6: User Confirmation

If the user did not supply `theme`, ask for confirmation before finalizing it.

If the user did not supply `title`, propose one in the final synthesis step. The title can be accepted directly unless the user asks to revise it.

## Output Contract

Always make it clear:

- which inputs were provided by the user
- which values were inferred
- which values were defaulted
- which values still need confirmation

When `theme` was inferred, explicitly label it as proposed, not final.

When `license` is missing, state that it was not provided.

When output format is not specified, return both STAC and DCAT.

## STAC Output Shape

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/table/v1.0.0/schema.json",
    "https://stac-extensions.github.io/projection/v1.1.0/schema.json"
  ],
  "id": "csv-dataset-id",
  "description": "Tabular data from CSV",
  "geometry": {"type": "Polygon", "coordinates": []},
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
        {"name": "column_name", "type": "string|number|date", "description": "column description"}
      ]
    }
  }
}
```

## DCAT Output Shape

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
  "dct:temporal": {
    "@type": "dct:PeriodOfTime",
    "dcat:startDate": "2020-01-01",
    "dcat:endDate": "2023-12-31"
  }
}
```

## Reference Implementation Hints

```python
import json
import pandas as pd
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Tuple

class CSVtoMetadata:

    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path, nrows=1000)

    def to_stac_item(self, dataset_id: str = None) -> Dict[str, Any]:
        geometry, bbox = self._extract_spatial()
        start_dt, end_dt = self._extract_temporal()
        return {
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
                    "table:row_count": len(self.df)
                }
            },
            "links": []
        }

    def to_dcat_record(self, title: str = None, description: str = None) -> Dict[str, Any]:
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
        lat_col = next((col for col in self.df.columns if any(x in col.lower() for x in ['lat', 'latitude', 'y'])), None)
        lon_col = next((col for col in self.df.columns if any(x in col.lower() for x in ['lon', 'lng', 'longitude', 'x'])), None)
        if lat_col and lon_col:
            lat_vals = pd.to_numeric(self.df[lat_col], errors='coerce').dropna()
            lon_vals = pd.to_numeric(self.df[lon_col], errors='coerce').dropna()
            if len(lat_vals) > 0 and len(lon_vals) > 0:
                bbox = [float(lon_vals.min()), float(lat_vals.min()), float(lon_vals.max()), float(lat_vals.max())]
                geometry = {"type": "Polygon", "coordinates": [[[bbox[0], bbox[1]], [bbox[2], bbox[1]], [bbox[2], bbox[3]], [bbox[0], bbox[3]], [bbox[0], bbox[1]]]]}
                return geometry, bbox
        return None, None

    def _describe_columns(self) -> List[Dict[str, Any]]:
        columns = []
        for col in self.df.columns:
            col_type = str(self.df[col].dtype)
            stac_type = 'integer' if 'int' in col_type else 'number' if 'float' in col_type else 'string'
            columns.append({"name": col, "type": stac_type, "description": col})
        return columns

    def _extract_keywords(self) -> List[str]:
        return [col.lower().replace('_', ' ').strip() for col in self.df.columns if len(col) > 2][:10]

def derive_dataset_id(filepath: str, identifier: str = None, baseurl: str = None) -> str:
    stem = Path(filepath).stem.strip().lower().replace(' ', '-')
    if identifier:
        return identifier
    if baseurl:
        return f"{baseurl.rstrip('/')}/{stem}"
    return stem

def propose_title(
    filepath: str,
    description: str = None,
    subject: str = None,
    bbox: list = None,
    start_dt: str = None,
    end_dt: str = None,
    grouping: str = None,
) -> str:
    base = subject or description or Path(filepath).stem.replace('_', ' ').replace('-', ' ')
    parts = [base.strip()]
    if grouping:
        parts.append(f"by {grouping}")
    if start_dt and end_dt:
        parts.append(f"for {start_dt} to {end_dt}")
    elif start_dt:
        parts.append(f"from {start_dt}")
    elif end_dt:
        parts.append(f"until {end_dt}")
    if bbox and len(bbox) == 4:
        parts.append(f"in bbox {bbox[0]}, {bbox[1]}, {bbox[2]}, {bbox[3]}")
    return " ".join(parts)
```

## References

- [STAC Table Extension](https://github.com/stac-extensions/table)
- [DCAT 3.0](https://www.w3.org/TR/vocab-dcat-3/)
- [Pandas I/O Tools](https://pandas.pydata.org/docs/user_guide/io.html)
