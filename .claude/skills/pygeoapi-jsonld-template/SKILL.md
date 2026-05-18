---
name: pygeoapi-jsonld-template
description: Use when generating Jinja2 templates that render a pygeoapi feature collection as JSON-LD using a specific OGC building block's context.jsonld. Produces minimal template overrides for the items endpoint only (single feature + feature collection); leaves all other pygeoapi pages untouched. Use after pygeoapi-config-generator; not for non-bblock pygeoapi customisation.
---

**Status**: pre-release · **Scope**: generic · **Building-block coupling**: none.  
_Just authored; Jinja2 templates per bblock context._

# pygeoapi JSON-LD Template Skill

## Purpose

Generate harness JSON-LD support files for one collection. Prefer pygeoapi's built-in `linked-data.context` support when available; generate Jinja2 templates only as a fallback/diagnostic artefact, because `geopython/pygeoapi:latest` handles `f=jsonld` before the items templates in the tested path.

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

Write the **minimal** override tree as a fallback/diagnostic artefact (paths match pygeoapi's template loader; everything else falls back to defaults):

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

### Phase 4 — optional local patch helper

The tested `geopython/pygeoapi:latest` Docker image does **not** execute `PYGEOAPI_STARTUP_SCRIPT`. Do not emit instructions that depend on that environment variable.

When the harness needs to patch local response behaviour, emit `build-local/test-harness/<block>/sitecustomize.py` and have `pygeoapi-local-runner` mount it to `/etc/python3.10/sitecustomize.py`. Preserve the image's default apport hook at the top of this file.

For APKG/Records-style collections, use this helper to add a harness-only `itemSchema` member to `/collections/<collection_id>?f=json` and append a `rel=describedby` link. The schema should be loaded from `/pygeoapi/data/schema.json`. Record values remain under `/collections/<collection_id>/items`; the collection endpoint should expose schema/description, not duplicate all item values.

```python
import json

try:
    import apport_python_hook
except ImportError:
    pass
else:
    apport_python_hook.install()

from pygeoapi.api import API

SCHEMA_PATH = "/pygeoapi/data/schema.json"
COLLECTION_ID = "<collection_id>"

with open(SCHEMA_PATH) as schema_file:
    ITEM_SCHEMA = json.load(schema_file)

_describe_collections = API.describe_collections

def describe_collections_with_item_schema(self, request, dataset=None):
    headers, status, content = _describe_collections(self, request, dataset)
    try:
        body = json.loads(content)
    except (TypeError, json.JSONDecodeError):
        return headers, status, content

    if dataset == COLLECTION_ID:
        body["itemSchema"] = ITEM_SCHEMA
        body.setdefault("links", []).append({
            "type": "application/schema+json",
            "rel": "describedby",
            "title": "Full item schema",
            "href": f"{self.config['server']['url']}/collections/{dataset}?f=json#itemSchema",
        })
        return headers, status, json.dumps(body, indent=4)

    return headers, status, content

API.describe_collections = describe_collections_with_item_schema
```

## Outputs

- template tree at `${out}`
- optional `sitecustomize.py` local patch helper
- manifest:

```json
{
  "templates": "build-local/test-harness/<block>/templates",
  "sitecustomize": "build-local/test-harness/<block>/sitecustomize.py",
  "collection_id": "<block-name>",
  "format_aliases": ["jsonld"]
}
```

## Notes

- Templates use `tojson` for safe JSON escaping — no manual string interpolation of feature values.
- The `@context` is embedded **inline** in `pygeoapi-config.yml` as the parsed JSON object/list, not as a URL or file path — this lets the harness validate the rendered output offline and avoids pygeoapi `.copy()` failures on string paths.
- pygeoapi's default templates for HTML / GeoJSON / OpenAPI remain untouched. `index.jsonld.j2` and `item.jsonld.j2` are fallback artefacts, not the primary JSON-LD path for the tested Docker image.

## References

- pygeoapi templates — https://docs.pygeoapi.io/en/latest/configuration.html#templates
- pygeoapi JSON-LD plugin — https://docs.pygeoapi.io/en/latest/plugins.html#json-ld
- JSON-LD 1.1 — https://www.w3.org/TR/json-ld11/
