---
name: pygeoapi-jsonld-template
description: Use when generating Jinja2 templates that render a pygeoapi feature collection as JSON-LD using a specific OGC building block's context.jsonld. Produces minimal template overrides for the items endpoint only (single feature + feature collection); leaves all other pygeoapi pages untouched. Use after pygeoapi-config-generator; not for non-bblock pygeoapi customisation.
---

# pygeoapi JSON-LD Template Skill

## Purpose

Generate Jinja2 templates that override the default pygeoapi JSON-LD output for one collection so that:

- the `@context` is the bblock's own `context.jsonld` (not pygeoapi's generic GeoSPARQL/Schema.org one),
- every feature property is rendered as-is (the context drives the semantics), and
- the templates ride on top of pygeoapi's defaults — only the items endpoint is overridden.

## Activation

Use this skill when:

- a bblock has its own `context.jsonld` that diverges from pygeoapi's defaults
- the harness needs to test that the rendered output validates against the bblock schema + context

Do not use this skill for:

- non-`f=jsonld` representations (HTML / GeoJSON stay default)
- templates that touch the landing page, conformance, or collections list endpoints
- production pygeoapi UIs

## Required input

- `block_path` — `_sources/<block-name>/`
- `collection_id` — collection identifier (from `pygeoapi-config-generator`'s manifest)

## Optional input

| Parameter | Default | Meaning |
|---|---|---|
| `out` | `build-local/test-harness/<block>/templates/` | template tree root |
| `format_aliases` | `["jsonld"]` | which `f=` value(s) to override |

## Process

### Phase 1 — locate context

Read `<block>/context.jsonld`. Validate it parses as JSON. If the file is missing, **fail fast**:

> Block `<block>` has no `context.jsonld`. The harness requires the context to render JSON-LD output. Aborting.

### Phase 2 — emit template tree

Write the **minimal** override tree (paths match pygeoapi's template loader; everything else falls back to defaults):

```
build-local/test-harness/<block>/templates/
└── collections/
    └── items/
        ├── index.jsonld.j2       # FeatureCollection
        └── item.jsonld.j2        # single Feature
```

### Phase 3 — template content

`item.jsonld.j2`:

```jinja
{
  "@context": {{ bblock_context | tojson }},
  "id": "{{ data.id }}",
  "type": "Feature",
  {%- if data.geometry %}
  "geometry": {{ data.geometry | tojson }},
  {%- endif %}
  "properties": {
    {%- for key, value in data.properties.items() %}
    "{{ key }}": {{ value | tojson }}{% if not loop.last %},{% endif %}
    {%- endfor %}
  },
  "links": [
    {%- for link in data.links %}
    { "rel": "{{ link.rel }}", "href": "{{ link.href }}", "type": "{{ link.type }}" }
    {%- if not loop.last %},{% endif %}
    {%- endfor %}
  ]
}
```

`index.jsonld.j2`:

```jinja
{
  "@context": {{ bblock_context | tojson }},
  "type": "FeatureCollection",
  "numberMatched": {{ data.numberMatched }},
  "numberReturned": {{ data.numberReturned }},
  "features": [
    {%- for feature in data.features %}
    {
      "id": "{{ feature.id }}",
      "type": "Feature",
      {%- if feature.geometry %}
      "geometry": {{ feature.geometry | tojson }},
      {%- endif %}
      "properties": {
        {%- for key, value in feature.properties.items() %}
        "{{ key }}": {{ value | tojson }}{% if not loop.last %},{% endif %}
        {%- endfor %}
      }
    }{% if not loop.last %},{% endif %}
    {%- endfor %}
  ],
  "links": [
    {%- for link in data.links %}
    { "rel": "{{ link.rel }}", "href": "{{ link.href }}", "type": "{{ link.type }}" }
    {%- if not loop.last %},{% endif %}
    {%- endfor %}
  ]
}
```

### Phase 4 — injection helper

pygeoapi templates receive `data` from the renderer but not arbitrary file content. Emit a small Python startup hook `pygeoapi_jsonld_context.py` alongside the templates that exposes `bblock_context` via Jinja's `globals`:

```python
# Loaded by pygeoapi-local-runner via PYGEOAPI_STARTUP_SCRIPT
import json, os
from pygeoapi.flask_app import APP

_ctx_path = os.environ.get("BBLOCK_CONTEXT", "/pygeoapi/data/context.jsonld")
with open(_ctx_path) as f:
    APP.jinja_env.globals["bblock_context"] = json.load(f)
```

`pygeoapi-local-runner` mounts this script and sets `BBLOCK_CONTEXT` to the bblock's `context.jsonld` path.

## Outputs

- template tree at `${out}`
- `pygeoapi_jsonld_context.py` startup hook
- manifest:

```json
{
  "templates": "build-local/test-harness/<block>/templates",
  "startup_hook": "build-local/test-harness/<block>/pygeoapi_jsonld_context.py",
  "collection_id": "<block-name>",
  "format_aliases": ["jsonld"]
}
```

## Notes

- Templates use `tojson` for safe JSON escaping — no manual string interpolation of feature values.
- The `@context` is embedded **inline** as the parsed JSON object, not as a URL — this lets the harness validate the rendered output offline without pygeoapi needing internet access.
- pygeoapi's default templates for HTML / GeoJSON / OpenAPI remain untouched. Only `index.jsonld.j2` and `item.jsonld.j2` are added.

## References

- pygeoapi templates — https://docs.pygeoapi.io/en/latest/configuration.html#templates
- pygeoapi JSON-LD plugin — https://docs.pygeoapi.io/en/latest/plugins.html#json-ld
- JSON-LD 1.1 — https://www.w3.org/TR/json-ld11/
