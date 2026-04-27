---
name: global-fishing-watch-data-service
description: Use when querying Global Fishing Watch APIs for vessels, events, insights, map visualization, datasets, or bulk downloads. Prompts the user to choose an API family and operation, asks only for the parameters needed for that operation, checks the workspace root .env for a Global Fishing Watch token, and maps the selected parameters programmatically to the official GFW v3 API.
---

# Global Fishing Watch Data Service Skill

## Purpose

Query the official Global Fishing Watch APIs programmatically, with operation-aware prompting and parameter mapping.

Use this skill to:

- list the available Global Fishing Watch API families
- ask the user to choose an API family and operation before querying
- ask only for the parameters needed by the selected operation
- check the workspace root `.env` for a GFW API token and optional base URL
- call the API programmatically and return the retrieved data together with a sanitized log of the API calls used to retrieve it

## Activation

Use this skill when the user asks to:

- query Global Fishing Watch data
- search vessels in GFW
- retrieve fishing, encounter, loitering, port visit, or AIS off events
- get vessel insights
- generate 4Wings reports or tiles
- download fixed infrastructure datasets or create bulk download jobs

Do not use this skill for:

- LifeWatch data services
- generic marine web services
- non-GFW vessel databases

## Supported API Families

Start by presenting the available API families and asking the user to choose one:

- `vessels`
- `events`
- `insights`
- `4wings`
- `datasets`
- `bulk-download`

Use the helper script when possible:

```bash
python3 .claude/skills/global-fishing-watch-data-service/scripts/query_gfw_api.py --list-families
python3 .claude/skills/global-fishing-watch-data-service/scripts/query_gfw_api.py --list-operations
```

## Supported Operations

### Vessels

- `vessel-search`
- `vessel-details`

Actual API calls:

- `GET /v3/vessels/search`
- `GET /v3/vessels/{vessel_id}`

### Events

- `events-get`

Actual API call:

- `GET /v3/events`

### Insights

- `insights-by-vessel`

Actual API call:

- `POST /v3/insights/vessels`

### 4Wings

- `4wings-report`
- `4wings-last-report`
- `4wings-generate-png`
- `4wings-tile`

Actual API calls:

- `GET /v3/4wings/report`
- `GET /v3/4wings/last-report`
- `POST /v3/4wings/generate-png`
- `GET /v3/4wings/tile/heatmap/{z}/{x}/{y}`

### Datasets

- `datasets-fixed-infrastructure`

Actual API call:

- `GET /v3/datasets`

### Bulk Download

- `bulk-create-report`
- `bulk-report-status`

Actual API calls:

- `POST /v3/bulk/reports`
- `GET /v3/bulk/reports/{report_id}`

## Required Interaction Pattern

Always follow this sequence:

1. determine the workspace root
2. check for `.env` in that root
3. inspect available GFW auth settings
4. present API family and operation choices if the user did not already choose them
5. ask only for the parameters needed for the selected operation
6. map the answers to query parameters or a JSON body
7. execute the API call programmatically
8. return the result together with the executed method, full URL with query parameters, and payload

## Authentication Rules

First check the workspace root `.env` for any of these keys:

- `GLOBAL_FISHING_WATCH_API_KEY`
- `GFW_API_TOKEN`
- `GLOBAL_FISHING_WATCH_API_TOKEN`
- `GLOBAL_FISHING_WATCH_TOKEN`
- `GFW_BASE_URL`

If the token is not present, ask:

`I couldn't find a Global Fishing Watch API token in the workspace root .env file. Where should I read it from, or would you like to provide it now?`

Use Bearer token authentication:

`Authorization: Bearer <TOKEN>`

Never print, echo, or store the bearer token in returned logs.

When returning request provenance, include only sanitized request details:

- HTTP method
- URL
- query parameters
- request body
- response status or response data summary

Do not include the raw `Authorization` header value.

Default base URL:

`https://gateway.api.globalfishingwatch.org/v3`

If `GFW_BASE_URL` is present, prefer it.

## Operation-Specific Parameter Rules

Ask only for the parameters needed by the selected operation.

### `vessel-search`

Ask for:

- `query`
- `datasets`

Optional:

- `limit`
- `offset`

Default dataset if the user does not specify one:

- `public-global-vessel-identity:latest`

### `vessel-details`

Ask for:

- `vessel_id`

Optional:

- `datasets`

### `events-get`

Ask for:

- `dataset`
- either `vessel_id` or a spatial filter such as `region_id`
- date range when needed

Use the correct event dataset according to the requested event type:

- fishing: `public-global-fishing-events:latest`
- encounters: `public-global-encounters-events:latest`
- loitering: `public-global-loitering-events:latest`
- port visits: `public-global-port-visits-events:latest` or `public-global-port-visits-c2-events:latest`
- AIS off: `public-global-gaps-events:latest`

### `insights-by-vessel`

Ask for:

- `vessel_id`

Optional:

- `datasets`
- `includes`
- `confidences`
- `start_date`
- `end_date`

### `4wings-report`

Ask for:

- `datasets`
- `date_range`
- region input

Region input can be:

- `region_id` plus `region_dataset`
- or a custom region JSON body

Optional:

- `format`
- `spatial_resolution`
- `temporal_resolution`
- `filters`
- `buffer_value`
- `buffer_unit`

### `4wings-last-report`

Ask for the same parameters as `4wings-report`, because the report identity is derived from those request parameters.

### `4wings-generate-png`

Ask for:

- `datasets`
- `date_range`
- `interval`

Optional:

- `filters`
- `color`

### `4wings-tile`

Ask for:

- `z`
- `x`
- `y`
- `datasets`
- `format`
- `interval`
- `date_range`

Optional:

- `style`
- `filters`
- `temporal_aggregation`

### `datasets-fixed-infrastructure`

Ask for:

- `dataset`

Default:

- `public-fixed-infrastructure-filtered:latest`

Optional:

- `z`
- `x`
- `y`
- `format`

### `bulk-create-report`

Ask for:

- `dataset`
- `date_range`
- output `format`
- region input

Default dataset:

- `public-fixed-infrastructure-data:latest`

### `bulk-report-status`

Ask for:

- `report_id`

## Programmatic Mapping

Use the helper script to build requests and execute the API call:

```bash
python3 .claude/skills/global-fishing-watch-data-service/scripts/query_gfw_api.py \
  --workspace-root /path/to/workspace \
  --operation vessel-search \
  --param query=7831410 \
  --param datasets=public-global-vessel-identity:latest
```

The helper returns a `request` block that shows:

- the selected operation
- the resolved HTTP method
- the full request URL
- decoded query parameters
- the JSON body when present

Examples:

```bash
python3 .claude/skills/global-fishing-watch-data-service/scripts/query_gfw_api.py --list-families
python3 .claude/skills/global-fishing-watch-data-service/scripts/query_gfw_api.py --list-operations
python3 .claude/skills/global-fishing-watch-data-service/scripts/query_gfw_api.py --operation events-get --param dataset=public-global-fishing-events:latest --param vessel_id=12345
```

## Output Contract

Always report:

- selected API family
- selected operation
- prompted parameters
- values supplied by the user
- values sourced from `.env`
- retrieved data
- sanitized API call log:
  - executed HTTP method
  - executed URL with query parameters
  - decoded query parameters
  - executed JSON body if any
  - no bearer token in output

Always include links to:

- GFW APIs overview: https://globalfishingwatch.org/our-apis/
- GFW API documentation: https://globalfishingwatch.org/our-apis/documentation
- GFW commercial-use FAQ: https://globalfishingwatch.org/faqs/can-i-use-global-fishing-watch-apis-for-commercial-purposes/

Always highlight usage limitations from the official documentation:

- GFW APIs are available only for non-commercial purposes
- users must agree to the terms of use and attribute Global Fishing Watch in publications
- data should be used with the dataset caveats described in the GFW documentation
- some datasets are delayed or limited in coverage, such as AIS activity products that may only be available up to about 96 hours ago

When the user requests data that may be subject to GFW caveats or terms of use, mention that the official GFW caveats and attribution requirements apply.

## Notes

- This skill is based on the official Global Fishing Watch API documentation for v3.
- The helper script is intentionally conservative and supports the core public operations described in the official docs.
- Global Fishing Watch APIs require a registered account and API access token for use.
- Returned API provenance must keep credentials secret while still documenting the exact calls used to retrieve the data.

## References

- GFW APIs overview: https://globalfishingwatch.org/our-apis/
- GFW API documentation: https://globalfishingwatch.org/our-apis/documentation
- GFW commercial-use FAQ: https://globalfishingwatch.org/faqs/can-i-use-global-fishing-watch-apis-for-commercial-purposes/
