#!/usr/bin/env python3
"""Minimal LifeWatch Data Service client for dataset-aware API calls."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, Optional
from urllib import request, error


DEFAULT_BASE_PATH = "https://opencpu.lifewatch.be/library/lwdataserver/R/"
DATASET_LABELS = {
    "buoy": "Buoy data",
    "station": "Station data",
    "underway": "Underway data",
    "etn": "ETN data",
    "cpod": "CPOD data",
    "mvb": "MVB data",
    "uva-bird": "UVA-bird data",
    "bats": "Bats data",
    "flowcam": "Flowcam data",
    "zooscan": "ZooScan data",
    "ctd": "CTD data",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace-root", type=Path, default=Path.cwd())
    parser.add_argument("--list-datasets", action="store_true")
    parser.add_argument("--dataset", choices=sorted(DATASET_LABELS))
    parser.add_argument("--list-options", choices=["etn", "mvb", "uva-bird"])
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


def get_base_path(env: Dict[str, str]) -> str:
    base_path = env.get("LIFEWATCH_BASE_URL") or env.get("BASE_PATH") or DEFAULT_BASE_PATH
    if not base_path.endswith("/"):
        base_path += "/"
    return base_path


def opencpu_url(base_path: str) -> str:
    return f"{base_path}getLWdata/json"


def auth_from_env(env: Dict[str, str]) -> Dict[str, Optional[str]]:
    return {
        "api_key": env.get("LIFEWATCH_API_KEY")
        or env.get("LIFEWATCH_DATA_API_KEY")
        or env.get("LIFEWATCH_API_TOKEN"),
        "username": env.get("LIFEWATCH_USERNAME"),
        "password": env.get("LIFEWATCH_PASSWORD"),
    }


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


def build_request_body(dataset: str, params: Dict[str, Any], env: Dict[str, str]) -> Dict[str, Any]:
    label = DATASET_LABELS[dataset]
    input_payload: Dict[str, Any] = {"type": label, "getPar": True}
    user_payload: Dict[str, Any] = {}

    if "startdate" in params or "stopdate" in params:
        startdate = params.get("startdate")
        stopdate = params.get("stopdate")
        if not startdate or not stopdate:
            raise ValueError("Both startdate and stopdate are required together.")
        input_payload["daterange"] = [startdate, stopdate]

    if dataset in {"buoy", "station", "ctd"} and "stations" in params:
        input_payload["stationlist"] = params["stations"]
    if dataset == "station" and "categories" in params:
        input_payload["categories"] = params["categories"]
    if dataset in {"underway", "etn", "cpod", "mvb"} and "by" in params:
        input_payload["binSize"] = params["by"]
    if dataset == "etn":
        if "action" in params:
            input_payload["calculate"] = params["action"]
        if "networks" in params:
            input_payload["projects"] = params["networks"]
        if "projects" in params:
            input_payload["tagProjects"] = params["projects"]
    if dataset == "cpod":
        if "processing" in params:
            input_payload["processing"] = params["processing"]
        if "quality" in params:
            input_payload["quality"] = params["quality"]
    if dataset == "mvb":
        if "parameters" in params:
            input_payload["parameters"] = params["parameters"]
        if "calc" in params:
            input_payload["calc"] = params["calc"]
        if "stations" in params:
            input_payload["stationlist"] = params["stations"]
    if dataset == "ctd" and "by" in params:
        input_payload["binSize"] = params["by"]

    if params.get("api_key"):
        user_payload["apiKey"] = params["api_key"]
    elif auth_from_env(env)["api_key"]:
        user_payload["apiKey"] = auth_from_env(env)["api_key"]

    if params.get("username") or env.get("LIFEWATCH_USERNAME"):
        user_payload["username"] = params.get("username") or env.get("LIFEWATCH_USERNAME")
    if params.get("password") or env.get("LIFEWATCH_PASSWORD"):
        user_payload["password"] = params.get("password") or env.get("LIFEWATCH_PASSWORD")

    return {"USER": user_payload or None, "input": input_payload, "client": None}


def list_options_body(list_name: str) -> Dict[str, Any]:
    mapping = {
        "etn": {"USER": None, "input": {"type": "listETNprojects"}, "client": None},
        "mvb": {"USER": None, "input": {"type": "listMVBstations"}, "client": None},
        "uva-bird": {"USER": None, "input": {"type": "listUVAtags"}, "client": None},
    }
    return mapping[list_name]


def post_json(url: str, body: Dict[str, Any]) -> Any:
    payload = json.dumps(body).encode("utf-8")
    req = request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    with request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main() -> int:
    args = parse_args()

    if args.list_datasets:
        print(json.dumps({"datasets": sorted(DATASET_LABELS)}, indent=2))
        return 0

    env = load_env(args.workspace_root)
    base_path = get_base_path(env)
    url = opencpu_url(base_path)

    if args.list_options:
        body = list_options_body(args.list_options)
        try:
            response = post_json(url, body)
        except error.HTTPError as exc:
            print(json.dumps({"error": f"HTTP {exc.code}", "url": url}, indent=2))
            return 1
        print(json.dumps({"url": url, "body": body, "response": response}, indent=2 if args.pretty else None))
        return 0

    if not args.dataset:
        raise SystemExit("--dataset is required unless --list-datasets is used.")

    params = parse_param_items(args.param)
    body = build_request_body(args.dataset, params, env)
    try:
        response = post_json(url, body)
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        print(json.dumps({"error": f"HTTP {exc.code}", "url": url, "body": body, "detail": detail}, indent=2))
        return 1
    except error.URLError as exc:
        print(json.dumps({"error": str(exc), "url": url, "body": body}, indent=2))
        return 1

    print(json.dumps({"url": url, "body": body, "response": response}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
