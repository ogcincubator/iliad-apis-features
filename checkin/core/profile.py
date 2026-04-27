"""Profile a data source — properties, dimensions, spatial/temporal extent, sample.

One profile shape regardless of input format. Per-format extractors are small and
private; callers go through ``profile(source, fmt)``.
"""
from __future__ import annotations

import csv
import io
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import httpx


@dataclass
class PropertySpec:
    name: str
    dtype: str = ""
    unit: str = ""
    description: str = ""
    sample_values: list[Any] = field(default_factory=list)


@dataclass
class DimensionSpec:
    name: str
    size: int = 0
    dtype: str = ""
    units: str = ""


@dataclass
class Profile:
    format: str
    source: str
    properties: list[PropertySpec] = field(default_factory=list)
    dimensions: list[DimensionSpec] = field(default_factory=list)
    spatial_extent: list[float] | None = None  # [minx, miny, maxx, maxy]
    temporal_extent: list[str] | None = None   # [start_iso, end_iso]
    sample: Any = None
    errors: list[str] = field(default_factory=list)
    meta: dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        return {
            "format": self.format,
            "source": self.source,
            "properties": [p.__dict__ for p in self.properties],
            "dimensions": [d.__dict__ for d in self.dimensions],
            "spatial_extent": self.spatial_extent,
            "temporal_extent": self.temporal_extent,
            "sample": self.sample,
            "errors": self.errors,
            "meta": self.meta,
        }


# ---------- CSV / TSV ----------


def _profile_tabular(source: str, sep: str) -> Profile:
    p = Profile(format="csv" if sep == "," else "tsv", source=source)
    text = _fetch_text(source)
    if text is None:
        p.errors.append("cannot read source")
        return p
    reader = csv.DictReader(io.StringIO(text), delimiter=sep)
    rows = [row for _, row in zip(range(200), reader)]
    headers = reader.fieldnames or []
    columns: dict[str, list[str]] = {h: [] for h in headers}
    for row in rows:
        for h in headers:
            val = row.get(h)
            if val is not None and val != "":
                columns[h].append(val)
    for h in headers:
        vals = columns[h]
        dtype = _infer_scalar_dtype(vals)
        p.properties.append(PropertySpec(name=h, dtype=dtype, sample_values=vals[:3]))
    p.sample = rows[:3]
    _try_spatial_from_cols(p, rows)
    _try_temporal_from_cols(p, rows)
    return p


def _infer_scalar_dtype(values: list[str]) -> str:
    if not values:
        return "string"
    ints = floats = 0
    for v in values:
        try:
            int(v)
            ints += 1
            continue
        except ValueError:
            pass
        try:
            float(v)
            floats += 1
        except ValueError:
            pass
    if ints == len(values):
        return "integer"
    if ints + floats == len(values):
        return "number"
    return "string"


def _try_spatial_from_cols(p: Profile, rows: list[dict[str, str]]) -> None:
    lat_col = _first_column(p, {"lat", "latitude", "y"})
    lon_col = _first_column(p, {"lon", "long", "longitude", "x"})
    if not lat_col or not lon_col:
        return
    lats, lons = [], []
    for r in rows:
        try:
            lats.append(float(r[lat_col]))
            lons.append(float(r[lon_col]))
        except (KeyError, TypeError, ValueError):
            continue
    if lats and lons:
        p.spatial_extent = [min(lons), min(lats), max(lons), max(lats)]


def _try_temporal_from_cols(p: Profile, rows: list[dict[str, str]]) -> None:
    time_col = _first_column(p, {"time", "datetime", "date", "timestamp", "observedon", "eventdate"})
    if not time_col:
        return
    values = sorted(r[time_col] for r in rows if r.get(time_col))
    if values:
        p.temporal_extent = [values[0], values[-1]]


def _first_column(p: Profile, candidates: set[str]) -> str | None:
    for prop in p.properties:
        if prop.name.lower() in candidates:
            return prop.name
    return None


# ---------- JSON / GeoJSON ----------


def _profile_json(source: str, fmt: str) -> Profile:
    p = Profile(format=fmt, source=source)
    text = _fetch_text(source)
    if text is None:
        p.errors.append("cannot read source")
        return p
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        p.errors.append(f"invalid json: {exc}")
        return p
    if fmt == "geojson":
        feats = data.get("features") if isinstance(data, dict) else None
        if isinstance(feats, list) and feats:
            sample = feats[0]
            _walk_source(sample, "", p.properties)
            p.sample = feats[:3]
            _spatial_from_geojson(p, feats)
        return p
    # plain JSON — dotted paths for nested objects
    record = data[0] if isinstance(data, list) and data else data
    if isinstance(record, (dict, list)):
        _walk_source(record, "", p.properties)
    p.sample = _head(data, n=3)
    return p


def _walk_source(node: Any, prefix: str, out: list[PropertySpec]) -> None:
    """Emit PropertySpec(name=dotted.path) for every leaf + intermediate in a JSON record."""
    if isinstance(node, dict):
        for k, v in node.items():
            path = f"{prefix}.{k}" if prefix else k
            out.append(PropertySpec(name=path, dtype=_py_dtype(v), sample_values=[_leaf_example(v)]))
            if isinstance(v, (dict, list)):
                _walk_source(v, path, out)
    elif isinstance(node, list) and node:
        first = node[0]
        child = f"{prefix}[0]"
        if isinstance(first, (dict, list)):
            _walk_source(first, child, out)
        else:
            out.append(PropertySpec(name=f"{prefix}[]", dtype=_py_dtype(first), sample_values=[first]))


def _leaf_example(v: Any) -> Any:
    if isinstance(v, (str, int, float, bool)) or v is None:
        return v
    if isinstance(v, list) and v and isinstance(v[0], (str, int, float, bool)):
        return v[:3]
    return None


def _py_dtype(v: Any) -> str:
    if isinstance(v, bool):
        return "boolean"
    if isinstance(v, int):
        return "integer"
    if isinstance(v, float):
        return "number"
    if isinstance(v, list):
        return "array"
    if isinstance(v, dict):
        return "object"
    if v is None:
        return "null"
    return "string"


def _head(v: Any, n: int = 3) -> Any:
    if isinstance(v, list):
        return v[:n]
    return v


def _spatial_from_geojson(p: Profile, feats: list[dict[str, Any]]) -> None:
    xs, ys = [], []
    for f in feats:
        geom = f.get("geometry") or {}
        coords = geom.get("coordinates")
        _walk_coords(coords, xs, ys)
    if xs and ys:
        p.spatial_extent = [min(xs), min(ys), max(xs), max(ys)]


def _walk_coords(c: Any, xs: list[float], ys: list[float]) -> None:
    if isinstance(c, list):
        if c and isinstance(c[0], (int, float)) and len(c) >= 2:
            xs.append(float(c[0]))
            ys.append(float(c[1]))
        else:
            for sub in c:
                _walk_coords(sub, xs, ys)


# ---------- NetCDF ----------


def _profile_netcdf(source: str) -> Profile:
    p = Profile(format="netcdf", source=source)
    try:
        import xarray as xr
    except ImportError as exc:  # pragma: no cover
        p.errors.append(f"xarray unavailable: {exc}")
        return p
    local = _maybe_download(source)
    try:
        ds = xr.open_dataset(local)
    except Exception as exc:  # noqa: BLE001
        p.errors.append(f"open_dataset failed: {exc}")
        return p
    for name, coord in ds.coords.items():
        p.dimensions.append(
            DimensionSpec(
                name=str(name),
                size=int(coord.size),
                dtype=str(coord.dtype),
                units=str(coord.attrs.get("units", "")),
            )
        )
    for name, var in ds.data_vars.items():
        attrs = var.attrs or {}
        p.properties.append(
            PropertySpec(
                name=str(name),
                dtype=str(var.dtype),
                unit=str(attrs.get("units", "")),
                description=str(attrs.get("long_name") or attrs.get("standard_name") or ""),
            )
        )
    _netcdf_extents(ds, p)
    p.meta["global_attrs"] = {k: str(v) for k, v in ds.attrs.items()}
    ds.close()
    return p


def _netcdf_extents(ds: Any, p: Profile) -> None:
    lat_name = _coord_match(ds, {"lat", "latitude", "y"})
    lon_name = _coord_match(ds, {"lon", "longitude", "x"})
    if lat_name and lon_name:
        try:
            lat = ds[lat_name]
            lon = ds[lon_name]
            p.spatial_extent = [float(lon.min()), float(lat.min()), float(lon.max()), float(lat.max())]
        except Exception:  # noqa: BLE001
            pass
    time_name = _coord_match(ds, {"time", "t"})
    if time_name:
        try:
            t = ds[time_name]
            p.temporal_extent = [str(t.min().values), str(t.max().values)]
        except Exception:  # noqa: BLE001
            pass


def _coord_match(ds: Any, names: set[str]) -> str | None:
    for c in ds.coords:
        if str(c).lower() in names:
            return str(c)
    return None


# ---------- GeoParquet ----------


def _profile_parquet(source: str) -> Profile:
    p = Profile(format="geoparquet", source=source)
    try:
        import pyarrow.parquet as pq
    except ImportError as exc:  # pragma: no cover
        p.errors.append(f"pyarrow unavailable: {exc}")
        return p
    local = _maybe_download(source)
    try:
        tbl = pq.read_table(local)
    except Exception as exc:  # noqa: BLE001
        p.errors.append(f"read failed: {exc}")
        return p
    for field_ in tbl.schema:
        p.properties.append(PropertySpec(name=field_.name, dtype=str(field_.type)))
    p.sample = tbl.slice(0, 3).to_pylist()
    md = tbl.schema.metadata or {}
    geo = md.get(b"geo")
    if geo:
        try:
            geo_meta = json.loads(geo)
            p.meta["geoparquet"] = geo_meta
            col = geo_meta.get("primary_column")
            if col and col in geo_meta.get("columns", {}):
                bbox = geo_meta["columns"][col].get("bbox")
                if bbox and len(bbox) == 4:
                    p.spatial_extent = [float(x) for x in bbox]
        except Exception:  # noqa: BLE001
            pass
    return p


# ---------- OGC services ----------


def _profile_wfs(source: str) -> Profile:
    p = Profile(format="ogc-wfs", source=source)
    try:
        from owslib.wfs import WebFeatureService
    except ImportError as exc:  # pragma: no cover
        p.errors.append(f"OWSLib unavailable: {exc}")
        return p
    try:
        wfs = WebFeatureService(source, version="2.0.0")
    except Exception as exc:  # noqa: BLE001
        p.errors.append(f"WFS caps failed: {exc}")
        return p
    p.meta["types"] = list(wfs.contents.keys())
    if wfs.contents:
        ft_name = next(iter(wfs.contents))
        ft = wfs.contents[ft_name]
        p.meta["feature_type"] = ft_name
        bbox = ft.boundingBoxWGS84
        if bbox:
            p.spatial_extent = [float(x) for x in bbox]
    return p


def _profile_edr(source: str) -> Profile:
    p = Profile(format="ogc-edr", source=source)
    try:
        resp = httpx.get(source, timeout=15.0, follow_redirects=True)
        p.meta["status"] = resp.status_code
        if resp.headers.get("content-type", "").startswith("application/json"):
            body = resp.json()
            p.meta["capabilities"] = body
            exts = body.get("extent") or {}
            sp = (exts.get("spatial") or {}).get("bbox")
            if sp and isinstance(sp, list) and sp and isinstance(sp[0], list):
                p.spatial_extent = [float(x) for x in sp[0]]
            tr = (exts.get("temporal") or {}).get("interval")
            if tr and isinstance(tr, list) and tr and isinstance(tr[0], list):
                p.temporal_extent = [str(tr[0][0]), str(tr[0][1])]
            params = body.get("parameter_names") or body.get("parameters") or {}
            for name, spec in (params or {}).items():
                p.properties.append(
                    PropertySpec(
                        name=name,
                        unit=str((spec or {}).get("unit", {}).get("symbol", "")) if isinstance(spec, dict) else "",
                        description=str((spec or {}).get("description", "")) if isinstance(spec, dict) else "",
                    )
                )
    except Exception as exc:  # noqa: BLE001
        p.errors.append(f"EDR fetch failed: {exc}")
    return p


def _profile_opendap(source: str) -> Profile:
    # Attempt to open as NetCDF via xarray (works with DAP when netCDF4 supports it)
    p = _profile_netcdf(source)
    if p.errors:
        p.meta["note"] = "OPeNDAP opened via xarray; consider `#fillmismatch` if types differ."
    p.format = "opendap"
    return p


# ---------- helpers ----------


def _fetch_text(source: str) -> str | None:
    try:
        if source.startswith(("http://", "https://")):
            with httpx.Client(follow_redirects=True, timeout=30.0) as c:
                r = c.get(source)
                r.raise_for_status()
                return r.text
        return Path(source).expanduser().read_text()
    except Exception:  # noqa: BLE001
        return None


def _maybe_download(source: str) -> str:
    if not source.startswith(("http://", "https://")):
        return str(Path(source).expanduser())
    import tempfile

    with httpx.Client(follow_redirects=True, timeout=120.0) as c:
        with c.stream("GET", source) as r:
            r.raise_for_status()
            suffix = Path(source.split("?", 1)[0]).suffix or ".bin"
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
            for chunk in r.iter_bytes():
                tmp.write(chunk)
            tmp.flush()
            tmp.close()
            return tmp.name


# ---------- dispatcher ----------


def profile(source: str, fmt: str) -> Profile:
    if fmt == "csv":
        return _profile_tabular(source, ",")
    if fmt == "tsv":
        return _profile_tabular(source, "\t")
    if fmt == "geojson":
        return _profile_json(source, "geojson")
    if fmt == "json":
        return _profile_json(source, "json")
    if fmt == "netcdf":
        return _profile_netcdf(source)
    if fmt in {"parquet", "geoparquet"}:
        return _profile_parquet(source)
    if fmt == "ogc-wfs":
        return _profile_wfs(source)
    if fmt in {"ogc-edr", "ogc-api-features", "ogc-api-records"}:
        return _profile_edr(source)
    if fmt == "opendap":
        return _profile_opendap(source)
    p = Profile(format=fmt or "unknown", source=source)
    p.errors.append(f"no profiler for format '{fmt}'")
    return p
