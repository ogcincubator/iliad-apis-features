#!/usr/bin/env python3
"""Minimal Global Fishing Watch API client for guided requests."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, Optional, Tuple
from urllib import parse, request, error


DEFAULT_BASE_URL = "https://gateway.api.globalfishingwatch.org/v3"
FAMILIES = ["vessels", "events", "insights", "4wings", "datasets", "bulk-download"]
OPERATIONS = {
    "vessel-search": ("GET", "/vessels/search"),
    "vessel-details": ("GET", "/vessels/{vessel_id}"),
    "events-get": ("GET", "/events"),
    "insights-by-vessel": ("POST", "/insights/vessels"),
    "4wings-report": ("GET", "/4wings/report"),
    "4wings-last-report": ("GET", "/4wings/last-report"),
    "4wings-generate-png": ("POST", "/4wings/generate-png"),
    "4wings-tile": ("GET", "/4wings/tile/heatmap/{z}/{x}/{y}"),
    "datasets-fixed-infrastructure": ("GET", "/datasets"),
    "bulk-create-report": ("POST", "/bulk/reports"),
    "bulk-report-status": ("GET", "/bulk/reports/{report_id}"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace-root", type=Path, default=Path.cwd())
    parser.add_argument("--list-families", action="store_true")
    parser.add_argument("--list-operations", action="store_true")
    parser.add_argument("--operation", choices=sorted(OPERATIONS))
    parser.add_argument("--param", action="append", default=[], help="key=value")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def load_env(workspace_root: Path) -> Dict[str, str]:
    env: Dict[str, str] = {}
    env_path = workspace_root / ".env"
    if not env_path.exists():
        return env
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip().strip("'\"")
    return env


def get_token(env: Dict[str, str], params: Dict[str, Any]) -> Optional[str]:
    return (
        params.get("token")
        or env.get("GLOBAL_FISHING_WATCH_API_KEY")
        or env.get("GFW_API_TOKEN")
        or env.get("GLOBAL_FISHING_WATCH_API_TOKEN")
        or env.get("GLOBAL_FISHING_WATCH_TOKEN")
    )


def get_base_url(env: Dict[str, str]) -> str:
    return (env.get("GFW_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")


def parse_param_items(items: Iterable[str]) -> Dict[str, Any]:
    parsed: Dict[str, Any] = {}
    for item in items:
        if "=" not in item:
            raise ValueError(f"Invalid --param value: {item}")
        key, value = item.split("=", 1)
        parsed[key] = coerce_value(value)
    return parsed


def coerce_value(value: str) -> Any:
    if "," in value:
        return [coerce_value(part) for part in value.split(",")]
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    return value


def add_query_param(query: Dict[str, Any], key: str, value: Any) -> None:
    if value is None:
        return
    query[key] = value


def add_dataset_params(query: Dict[str, Any], datasets: Any) -> None:
    if datasets is None:
        return
    if not isinstance(datasets, list):
        datasets = [datasets]
    for idx, dataset in enumerate(datasets):
        query[f"datasets[{idx}]"] = dataset


def build_request(operation: str, params: Dict[str, Any], env: Dict[str, str]) -> Tuple[str, str, Dict[str, Any], Optional[Dict[str, Any]]]:
    method, path_template = OPERATIONS[operation]
    path = path_template.format(
        vessel_id=params.get("vessel_id", ""),
        z=params.get("z", ""),
        x=params.get("x", ""),
        y=params.get("y", ""),
        report_id=params.get("report_id", ""),
    )
    query: Dict[str, Any] = {}
    body: Optional[Dict[str, Any]] = None

    if operation == "vessel-search":
        add_query_param(query, "query", params.get("query"))
        add_dataset_params(query, params.get("datasets") or "public-global-vessel-identity:latest")
        add_query_param(query, "limit", params.get("limit"))
        add_query_param(query, "offset", params.get("offset"))
    elif operation == "vessel-details":
        add_dataset_params(query, params.get("datasets") or "public-global-vessel-identity:latest")
    elif operation == "events-get":
        add_dataset_params(query, params.get("dataset"))
        add_query_param(query, "vessel-id", params.get("vessel_id"))
        add_query_param(query, "region-id", params.get("region_id"))
        add_query_param(query, "region-dataset", params.get("region_dataset"))
        add_query_param(query, "start-date", params.get("start_date"))
        add_query_param(query, "end-date", params.get("end_date"))
        add_query_param(query, "limit", params.get("limit"))
    elif operation == "insights-by-vessel":
        includes = params.get("includes")
        confidences = params.get("confidences")
        datasets = params.get("datasets") or "public-global-vessel-identity:latest"
        if not isinstance(datasets, list):
            datasets = [datasets]
        body = {
            "includes": includes if isinstance(includes, list) else ([includes] if includes else ["FISHING"]),
            "confidences": confidences if isinstance(confidences, list) else ([confidences] if confidences else []),
            "startDate": params.get("start_date"),
            "endDate": params.get("end_date"),
            "vessels": [{"datasetId": ds, "vesselId": params.get("vessel_id")} for ds in datasets],
        }
    elif operation == "4wings-report":
        add_dataset_params(query, params.get("datasets"))
        add_query_param(query, "date-range", params.get("date_range"))
        add_query_param(query, "format", params.get("format"))
        add_query_param(query, "spatial-resolution", params.get("spatial_resolution"))
        add_query_param(query, "temporal-resolution", params.get("temporal_resolution"))
        add_query_param(query, "region-id", params.get("region_id"))
        add_query_param(query, "region-dataset", params.get("region_dataset"))
        add_query_param(query, "buffer-value", params.get("buffer_value"))
        add_query_param(query, "buffer-unit", params.get("buffer_unit"))
        filters = params.get("filters")
        if filters is not None and not isinstance(filters, list):
            filters = [filters]
        if filters:
            for idx, filt in enumerate(filters):
                query[f"filters[{idx}]"] = filt
        if params.get("region_json"):
            method = "POST"
            body = {"region": json.loads(params["region_json"])}
    elif operation == "4wings-last-report":
        add_dataset_params(query, params.get("datasets"))
        add_query_param(query, "date-range", params.get("date_range"))
        add_query_param(query, "format", params.get("format"))
    elif operation == "4wings-generate-png":
        add_dataset_params(query, params.get("datasets"))
        add_query_param(query, "date-range", params.get("date_range"))
        add_query_param(query, "interval", params.get("interval"))
        add_query_param(query, "color", params.get("color"))
        filters = params.get("filters")
        if filters is not None and not isinstance(filters, list):
            filters = [filters]
        if filters:
            for idx, filt in enumerate(filters):
                query[f"filters[{idx}]"] = filt
    elif operation == "4wings-tile":
        add_dataset_params(query, params.get("datasets"))
        add_query_param(query, "format", params.get("format"))
        add_query_param(query, "interval", params.get("interval"))
        add_query_param(query, "date-range", params.get("date_range"))
        add_query_param(query, "style", params.get("style"))
        add_query_param(query, "temporal-aggregation", params.get("temporal_aggregation"))
        filters = params.get("filters")
        if filters is not None and not isinstance(filters, list):
            filters = [filters]
        if filters:
            for idx, filt in enumerate(filters):
                query[f"filters[{idx}]"] = filt
    elif operation == "datasets-fixed-infrastructure":
        add_dataset_params(query, params.get("dataset") or "public-fixed-infrastructure-filtered:latest")
        add_query_param(query, "format", params.get("format"))
        if params.get("z") and params.get("x") and params.get("y"):
            path = f"/datasets/{params['z']}/{params['x']}/{params['y']}"
    elif operation == "bulk-create-report":
        body = {
            "dataset": params.get("dataset") or "public-fixed-infrastructure-data:latest",
            "dateRange": params.get("date_range"),
            "format": params.get("format"),
        }
        if params.get("region_json"):
            body["region"] = json.loads(params["region_json"])
        elif params.get("region_id") and params.get("region_dataset"):
            body["region"] = {"id": params["region_id"], "dataset": params["region_dataset"]}
    elif operation == "bulk-report-status":
        pass

    encoded = parse.urlencode(query, doseq=True)
    return method, path + (f"?{encoded}" if encoded else ""), query, body


def perform_request(base_url: str, token: str, method: str, target: str, body: Optional[Dict[str, Any]]) -> Any:
    url = f"{base_url}{target}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        # Cloudflare/GFW gateway rejects the default urllib user agent for some requests.
        "User-Agent": "curl/8.7.1",
    }
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode("utf-8")
    req = request.Request(url, data=data, headers=headers, method=method)
    with request.urlopen(req) as resp:
        content_type = resp.headers.get("Content-Type", "")
        payload = resp.read()
        if "application/json" in content_type:
            return json.loads(payload.decode("utf-8"))
        return {"content_type": content_type, "size": len(payload)}


def operation_catalog() -> Dict[str, Dict[str, str]]:
    return {
        name: {"method": method, "path": path}
        for name, (method, path) in sorted(OPERATIONS.items())
    }


def usage_notes() -> Dict[str, Any]:
    return {
        "terms_and_conditions": "https://globalfishingwatch.org/our-apis/",
        "api_documentation": "https://globalfishingwatch.org/our-apis/documentation",
        "commercial_use_faq": "https://globalfishingwatch.org/faqs/can-i-use-global-fishing-watch-apis-for-commercial-purposes/",
        "license_and_usage_summary": [
            "Global Fishing Watch APIs are available only for non-commercial purposes.",
            "Users must agree to the terms of use and attribute Global Fishing Watch in publications.",
            "Data should be used with the dataset caveats described in the official documentation.",
            "Some activity datasets are delayed and may only be available up to about 96 hours ago."
        ],
    }


def main() -> int:
    args = parse_args()
    if args.list_families:
        print(json.dumps({"families": FAMILIES}, indent=2))
        return 0
    if args.list_operations:
        print(json.dumps({"operations": operation_catalog()}, indent=2))
        return 0
    if not args.operation:
        raise SystemExit("--operation is required unless listing families or operations.")

    params = parse_param_items(args.param)
    env = load_env(args.workspace_root)
    token = get_token(env, params)
    if not token:
        raise SystemExit("No Global Fishing Watch token found in params or workspace .env.")

    base_url = get_base_url(env)
    method, target, query, body = build_request(args.operation, params, env)
    full_url = f"{base_url}{target}"
    try:
        response = perform_request(base_url, token, method, target, body)
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        print(json.dumps({
            "error": f"HTTP {exc.code}",
            "request": {
                "operation": args.operation,
                "method": method,
                "url": full_url,
                "query_params": query,
                "body": body,
            },
            "detail": detail,
        }, indent=2))
        return 1
    except error.URLError as exc:
        print(json.dumps({
            "error": str(exc),
            "request": {
                "operation": args.operation,
                "method": method,
                "url": full_url,
                "query_params": query,
                "body": body,
            },
        }, indent=2))
        return 1

    print(json.dumps({
        "request": {
            "operation": args.operation,
            "method": method,
            "url": full_url,
            "query_params": query,
            "body": body,
        },
        "usage": usage_notes(),
        "response": response,
    }, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
