"""Format detection for a data source (path or URL).

Returns one of:
    netcdf | csv | tsv | geoparquet | parquet | geojson | json |
    ogc-wfs | ogc-wms | ogc-edr | ogc-api-features | ogc-api-records |
    opendap | unknown
"""
from __future__ import annotations

import json
import mimetypes
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

import httpx

KNOWN_FORMATS = {
    "netcdf",
    "csv",
    "tsv",
    "geoparquet",
    "parquet",
    "geojson",
    "json",
    "ogc-wfs",
    "ogc-wms",
    "ogc-edr",
    "ogc-api-features",
    "ogc-api-records",
    "opendap",
    "unknown",
}


@dataclass
class SniffResult:
    source: str
    is_url: bool
    format: str
    content_type: str | None = None
    hints: dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        return {
            "source": self.source,
            "is_url": self.is_url,
            "format": self.format,
            "content_type": self.content_type,
            "hints": self.hints,
        }


def _ext(path: str) -> str:
    return Path(path).suffix.lower().lstrip(".")


def _sniff_by_extension(path: str) -> str | None:
    ext = _ext(path)
    mapping = {
        "nc": "netcdf",
        "nc4": "netcdf",
        "cdf": "netcdf",
        "csv": "csv",
        "tsv": "tsv",
        "parquet": "parquet",
        "geoparquet": "geoparquet",
        "geojson": "geojson",
        "json": "json",
    }
    return mapping.get(ext)


def _sniff_local(path: Path) -> SniffResult:
    fmt = _sniff_by_extension(str(path))
    hints: dict[str, Any] = {}
    if fmt == "parquet":
        # Try to detect geoparquet via footer metadata.
        try:
            import pyarrow.parquet as pq

            md = pq.read_metadata(path)
            kv = md.metadata or {}
            if any(k == b"geo" or (isinstance(k, bytes) and k.startswith(b"geo")) for k in kv.keys()):
                fmt = "geoparquet"
                hints["geoparquet_metadata_key"] = True
        except Exception as exc:  # noqa: BLE001
            hints["parquet_error"] = str(exc)
    if fmt == "json":
        try:
            with path.open() as fh:
                head = fh.read(4096)
            blob = json.loads(head) if head.strip().startswith("{") else None
            if isinstance(blob, dict) and blob.get("type") in {"FeatureCollection", "Feature"}:
                fmt = "geojson"
        except Exception:  # noqa: BLE001, S110
            pass
    if fmt is None:
        ct, _ = mimetypes.guess_type(str(path))
        fmt = "unknown"
        if ct:
            hints["guessed_mime"] = ct
    return SniffResult(source=str(path), is_url=False, format=fmt, hints=hints)


def _sniff_ogc_url(url: str) -> str | None:
    parsed = urlparse(url)
    path = parsed.path.lower()
    qs = {k.lower(): [v.lower() for v in vals] for k, vals in parse_qs(parsed.query).items()}
    service = (qs.get("service") or [""])[0]
    request = (qs.get("request") or [""])[0]
    if service == "wfs" or "wfs" in path:
        return "ogc-wfs"
    if service == "wms" or "wms" in path or request == "getmap":
        return "ogc-wms"
    if "/edr/" in path or "edr" in path.split("/"):
        return "ogc-edr"
    if path.endswith("/collections") or "/collections/" in path:
        return "ogc-api-features"
    if path.endswith("/records") or "/records/" in path:
        return "ogc-api-records"
    if ".dods" in path or ".dap" in path or path.endswith(".nc.html") or "/dodsC/" in path or "/thredds/" in path:
        return "opendap"
    return None


def _sniff_remote(url: str) -> SniffResult:
    hints: dict[str, Any] = {}
    ogc = _sniff_ogc_url(url)
    if ogc:
        return SniffResult(source=url, is_url=True, format=ogc, hints=hints)

    ext_fmt = _sniff_by_extension(urlparse(url).path)
    if ext_fmt:
        return SniffResult(source=url, is_url=True, format=ext_fmt, hints=hints)

    ct: str | None = None
    try:
        with httpx.Client(follow_redirects=True, timeout=10.0) as client:
            resp = client.head(url)
            ct = resp.headers.get("content-type")
            if resp.status_code >= 400 or not ct:
                resp = client.get(url, headers={"Range": "bytes=0-2047"})
                ct = resp.headers.get("content-type")
    except Exception as exc:  # noqa: BLE001
        hints["http_error"] = str(exc)

    if ct:
        hints["content_type"] = ct
        ctl = ct.lower().split(";", 1)[0].strip()
        mime_map = {
            "application/geo+json": "geojson",
            "application/vnd.geo+json": "geojson",
            "application/json": "json",
            "text/csv": "csv",
            "text/tab-separated-values": "tsv",
            "application/x-netcdf": "netcdf",
            "application/netcdf": "netcdf",
            "application/vnd.apache.parquet": "parquet",
            "application/x-parquet": "parquet",
        }
        fmt = mime_map.get(ctl, "unknown")
        return SniffResult(source=url, is_url=True, format=fmt, content_type=ct, hints=hints)

    return SniffResult(source=url, is_url=True, format="unknown", hints=hints)


def sniff(source: str) -> SniffResult:
    """Classify a filesystem path or URL into one of KNOWN_FORMATS."""
    if source.startswith(("http://", "https://")):
        return _sniff_remote(source)
    p = Path(source).expanduser()
    if not p.exists():
        return SniffResult(source=source, is_url=False, format="unknown", hints={"error": "file not found"})
    return _sniff_local(p)
