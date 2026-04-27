"""Materialise a list of JSON records into a GeoParquet file.

Writes a WKT-encoded ``geometry`` column and attaches GeoParquet metadata. For
simplicity we only emit Point geometries; extend with PolyLine / Polygon on demand.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def transform(input_obj: Any, params: dict) -> dict:
    if not isinstance(input_obj, list):
        raise TypeError("json-to-geoparquet expects a list of records")

    try:
        import pyarrow as pa
        import pyarrow.parquet as pq
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError(f"pyarrow not installed: {exc}") from exc

    lon_f = params["lon_field"]
    lat_f = params["lat_field"]
    crs = params.get("crs", "EPSG:4326")
    out_path = Path(params["output_path"]).expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    xs: list[float] = []
    ys: list[float] = []
    for rec in input_obj:
        if not isinstance(rec, dict):
            continue
        lon = _maybe_float(rec.get(lon_f))
        lat = _maybe_float(rec.get(lat_f))
        if lon is None or lat is None:
            continue
        xs.append(lon)
        ys.append(lat)
        r = {k: _scalarise(v) for k, v in rec.items() if k not in {lon_f, lat_f}}
        r["geometry"] = f"POINT ({lon} {lat})"
        rows.append(r)

    if not rows:
        raise ValueError("no valid rows after coordinate validation")

    table = pa.Table.from_pylist(rows)
    bbox = [min(xs), min(ys), max(xs), max(ys)]

    geo_metadata = {
        "version": "1.0.0",
        "primary_column": "geometry",
        "columns": {
            "geometry": {
                "encoding": "WKT",
                "crs": crs,
                "geometry_types": ["Point"],
                "bbox": bbox,
            }
        },
    }
    table = table.replace_schema_metadata(
        {**(table.schema.metadata or {}), b"geo": json.dumps(geo_metadata).encode()}
    )
    pq.write_table(table, out_path)

    return {
        "path": str(out_path),
        "rows": len(rows),
        "bbox": bbox,
        "crs": crs,
        "columns": [c for c in table.column_names],
    }


def _maybe_float(v: Any) -> float | None:
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _scalarise(v: Any) -> Any:
    if isinstance(v, (dict, list)):
        return json.dumps(v, default=str)
    return v
