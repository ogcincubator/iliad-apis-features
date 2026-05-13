---
name: response-schema-validator
description: Use when validating a JSON HTTP response body against a JSON Schema. Fetches the URL, parses the body, runs jsonschema validation, and returns a structured pass/fail report with the path and message of every error. Generic enough for STAC Items, DCAT Records, OGC API responses, or any other JSON output; used by pygeoapi-test-harness to validate rendered features against a bblock schema.
---

# Response Schema Validator Skill

## Purpose

Fetch a JSON resource from a URL and validate it against a JSON Schema, returning a structured report. Designed for the pygeoapi test harness, but generic enough to validate any JSON output — STAC Items, DCAT Records, bblock examples, etc.

## Activation

Use this skill when:

- a pygeoapi response body needs to validate against a bblock's `schema.json`
- a STAC Item from a remote catalogue needs to validate against its declared schema extensions
- a DCAT record needs to be checked against `dcat:Catalog` shape

Do not use this skill for:

- SHACL validation (use SHACL tooling)
- JSON-LD semantic validation (use `context-completeness-checker`)
- validating non-JSON payloads

## Required input

- `url` — the URL whose body will be fetched
- `schema_path` — path to the JSON Schema file (`.json` or `.yaml`)

## Optional input

| Parameter | Default | Meaning |
|---|---|---|
| `mode` | `feature` | `feature` validates one Feature; `featureCollection` validates the FeatureCollection top-level plus each feature; `auto` chooses based on the `type` field |
| `accept` | `application/json` | HTTP `Accept` header |
| `timeout` | `30` | seconds |
| `feature_path` | `features` | JSON pointer into the body to find the feature array (when mode is `featureCollection`) |
| `max_errors` | `50` | cap on errors reported per feature |

## Process

### Phase 1 — fetch

```bash
curl -sfL -H "Accept: ${accept}" --max-time ${timeout} -o /tmp/response.json "${url}"
```

On non-2xx, return:

```json
{ "pass": false, "fetch_error": "HTTP 5xx from <url>", "body_tail": "..." }
```

### Phase 2 — load schema

- If `.yaml`, parse YAML and convert to dict.
- Otherwise, parse JSON.
- Resolve `$ref` siblings (the `jsonschema` library does this transparently when the schema is structured correctly).
- If schema declares `$schema: https://json-schema.org/draft/2020-12/schema`, use Draft202012Validator. Else autodetect.

### Phase 3 — validate

```python
from jsonschema import Draft202012Validator
import json, yaml, pathlib

schema = json.load(open(schema_path)) if schema_path.endswith('.json') \
         else yaml.safe_load(open(schema_path))
body   = json.load(open('/tmp/response.json'))
v      = Draft202012Validator(schema)

if mode == 'auto':
    mode = 'featureCollection' if body.get('type') == 'FeatureCollection' else 'feature'

errors_per_feature = {}
if mode == 'feature':
    errs = list(v.iter_errors(body))
    if errs: errors_per_feature[body.get('id', '<root>')] = errs

elif mode == 'featureCollection':
    # validate the collection envelope first (FeatureCollection-level schema, if applicable)
    for f in body.get(feature_path, []):
        errs = list(v.iter_errors(f))
        if errs: errors_per_feature[f.get('id', '<unknown>')] = errs
```

### Phase 4 — report

```json
{
  "pass":        false,
  "url":         "<url>",
  "schema":      "<schema_path>",
  "mode":        "featureCollection",
  "checked":     7,
  "failed":      2,
  "details": [
    {
      "feature_id": "no-wfa:rel/...",
      "errors": [
        { "path": "properties.equation", "msg": "required key missing" },
        { "path": "properties.symbols[0].dimensionKind", "msg": "invalid IRI form" }
      ]
    }
  ]
}
```

## Outputs

The report dict above. `pass` is `true` iff `failed == 0`.

When this skill is called by the harness, the report is concatenated with the `context-completeness-checker` report under one umbrella.

## Edge cases

| Situation | Handling |
|---|---|
| YAML schema with `bblocks://` `$ref`s (e.g. `bblocks://ogc.ogc-utils.iri-or-curie`) | Resolve via the bblocks register: try `https://opengeospatial.github.io/bblocks/register.json` first, then any local register file under `./build/register.json`. |
| Response is a Problem Details document (RFC 7807) | Treat as fetch failure with the `title` / `detail` surfaced. |
| Empty FeatureCollection (`numberReturned: 0`) | Pass with a warning: "no features to validate". |
| Schema imposes additionalProperties=false but the rendered feature includes pygeoapi-added fields (`links`, `assets`) | Report as errors **and** suggest relaxing the schema, since this is a common bblock author mistake. |

## Interactions with other skills

- Called by `pygeoapi-test-harness` after `pygeoapi-local-runner` reports the items URL.
- Also useful standalone (no need for pygeoapi) — point at any JSON URL + schema.

## References

- JSON Schema 2020-12 — https://json-schema.org/draft/2020-12
- `jsonschema` Python lib — https://python-jsonschema.readthedocs.io/
- OGC API – Features schema — https://schemas.opengis.net/ogcapi/features/part1/1.0/
