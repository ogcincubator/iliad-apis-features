---
name: global-fishing-watch-data-service
description: Use when querying Global Fishing Watch APIs for vessels, events, insights, map visualization, datasets, or bulk downloads. Prompts the user to choose an API family and operation, asks only for the parameters needed for that operation, checks the workspace root .env for a Global Fishing Watch token, and maps the selected parameters programmatically to the official GFW v3 API.
---

# Global Fishing Watch Data Service Skill

Use this skill when querying the official Global Fishing Watch APIs.

Core behavior:

- prompt the user to choose an API family and operation
- prompt only for the parameters required by that operation
- check the workspace root `.env` for `GLOBAL_FISHING_WATCH_API_KEY`, `GFW_API_TOKEN`, `GLOBAL_FISHING_WATCH_API_TOKEN`, `GLOBAL_FISHING_WATCH_TOKEN`, or `GFW_BASE_URL`
- if the token is missing, ask the user where to get it from or ask them to provide it
- map the selected parameters programmatically to the official GFW v3 API
- execute the request and return the executed method, full URL with parameters, decoded query params, and request body for provenance

Supported API families:

- `vessels`
- `events`
- `insights`
- `4wings`
- `datasets`
- `bulk-download`

Helper script:

```bash
python3 .claude/skills/global-fishing-watch-data-service/scripts/query_gfw_api.py --list-families
python3 .claude/skills/global-fishing-watch-data-service/scripts/query_gfw_api.py --list-operations
```

Actual API calls currently covered:

- `GET /v3/vessels/search`
- `GET /v3/vessels/{vessel_id}`
- `GET /v3/events`
- `POST /v3/insights/vessels`
- `GET /v3/4wings/report`
- `GET /v3/4wings/last-report`
- `POST /v3/4wings/generate-png`
- `GET /v3/4wings/tile/heatmap/{z}/{x}/{y}`
- `GET /v3/datasets`
- `POST /v3/bulk/reports`
- `GET /v3/bulk/reports/{report_id}`

Example query:

```bash
python3 .claude/skills/global-fishing-watch-data-service/scripts/query_gfw_api.py \
  --workspace-root /path/to/workspace \
  --operation vessel-search \
  --param query=7831410 \
  --param datasets=public-global-vessel-identity:latest
```

If token is missing, ask:

`I couldn't find a Global Fishing Watch API token in the workspace root .env file. Where should I read it from, or would you like to provide it now?`
