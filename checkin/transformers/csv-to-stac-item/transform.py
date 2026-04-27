"""Convert a CSV row (dict) — or list of rows — into STAC Item(s).

``params``:
    lon_field, lat_field, time_field  — required
    id_field         optional; falls back to hash of the row
    collection       optional; becomes `collection`
"""
from __future__ import annotations

import hashlib
import json
from typing import Any


def _coerce_float(v: Any) -> float | None:
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _row_to_item(row: dict, params: dict) -> dict:
    lon = _coerce_float(row.get(params["lon_field"]))
    lat = _coerce_float(row.get(params["lat_field"]))
    if lon is None or lat is None:
        raise ValueError(f"row missing lon/lat: {row!r}")

    time_field = params["time_field"]
    dt = row.get(time_field)

    id_field = params.get("id_field")
    if id_field and row.get(id_field):
        item_id = str(row[id_field])
    else:
        item_id = hashlib.sha1(json.dumps(row, sort_keys=True, default=str).encode()).hexdigest()[:16]

    props = {k: v for k, v in row.items() if k not in {params["lon_field"], params["lat_field"]}}
    props["datetime"] = dt if dt else None

    item = {
        "type": "Feature",
        "stac_version": "1.0.0",
        "stac_extensions": [],
        "id": item_id,
        "bbox": [lon, lat, lon, lat],
        "geometry": {"type": "Point", "coordinates": [lon, lat]},
        "properties": props,
        "links": [],
        "assets": {},
    }
    if params.get("collection"):
        item["collection"] = params["collection"]
    return item


def transform(input_obj: Any, params: dict) -> Any:
    if isinstance(input_obj, list):
        return [_row_to_item(r, params) for r in input_obj]
    if isinstance(input_obj, dict):
        return _row_to_item(input_obj, params)
    raise TypeError(f"unsupported input type: {type(input_obj).__name__}")
