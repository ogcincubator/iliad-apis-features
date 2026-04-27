"""Convert a custom JSON record (or list of records) to a GeoJSON Feature.

``params``:
    lon_field, lat_field  (dot-notation paths)
    id_field              optional; default "id"
    property_fields       optional; default = every non-geometry top-level key
"""
from __future__ import annotations

from typing import Any


def _dig(obj: Any, path: str) -> Any:
    cur = obj
    for part in path.split("."):
        if isinstance(cur, dict):
            cur = cur.get(part)
        else:
            return None
    return cur


def _to_feature(record: dict, params: dict) -> dict:
    lon = _dig(record, params["lon_field"])
    lat = _dig(record, params["lat_field"])
    if lon is None or lat is None:
        raise ValueError(f"missing coords at lon_field={params['lon_field']} / lat_field={params['lat_field']}")
    try:
        lon = float(lon)
        lat = float(lat)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"non-numeric coordinates: lon={lon!r} lat={lat!r}") from exc

    id_field = params.get("id_field", "id")
    feat_id = _dig(record, id_field) if id_field else None

    prop_fields = params.get("property_fields") or [
        k for k in record.keys() if k not in {params["lon_field"], params["lat_field"], id_field}
    ]
    properties = {k: _dig(record, k) for k in prop_fields}

    feature: dict = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [lon, lat]},
        "properties": properties,
    }
    if feat_id is not None:
        feature["id"] = feat_id
    return feature


def transform(input_obj: Any, params: dict) -> Any:
    if isinstance(input_obj, list):
        return {"type": "FeatureCollection", "features": [_to_feature(r, params) for r in input_obj]}
    if isinstance(input_obj, dict):
        return _to_feature(input_obj, params)
    raise TypeError(f"unsupported input type: {type(input_obj).__name__}")
