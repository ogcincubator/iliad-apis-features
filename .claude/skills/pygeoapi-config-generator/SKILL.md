---
name: pygeoapi-config-generator
description: Use when generating a local pygeoapi configuration (pygeoapi-config.yml) from an OGC building block source folder. Inspects the bblock's example files, detects feature format (GeoJSON, GeoPackage, GeoParquet, OGR-readable), and emits a single-collection config ready to mount into a pygeoapi Docker container. Use as the first step of the pygeoapi test harness; not for production pygeoapi deployments.
---

**Status**: pre-release · **Scope**: generic · **Building-block coupling**: none.  
_Just authored; generates pygeoapi config from a bblock package._

# pygeoapi Config Generator Skill

## Purpose

Generate a `pygeoapi-config.yml` that serves the example data of one OGC building block as a local OGC API – Features collection. The config is the input to `pygeoapi-local-runner` and is consumed by `pygeoapi-jsonld-template` to know which collection to template.

## Activation

Use this skill when:

- preparing a local pygeoapi test for a bblock
- rendering bblock examples through `?f=jsonld` to validate context coverage
- assembling artefacts for `pygeoapi-test-harness`

Do not use this skill for:

- production pygeoapi configs
- multi-collection / multi-tenant configs
- non-vector data (NetCDF / CoverageJSON) — those need different providers and are out of scope

## Required input

- `block_path` — absolute or repo-relative path to `_sources/<block-name>/`

## Optional input

| Parameter | Default | Meaning |
|---|---|---|
| `collection_id` | `<block-name>` slugified | OGC API collection identifier |
| `sample` | first `*.geojson` / `*.gpkg` / `*.parquet` under `examples/` | concrete file to serve |
| `host` | `localhost` | server hostname for OpenAPI |
| `port` | `5000` | server port |
| `out` | `build-local/test-harness/<block>/pygeoapi-config.yml` | output path |

## Process

### Phase 1 — discover the bblock

1. Read `<block>/bblock.json` to extract `name`, `abstract`, `itemIdentifier`.
2. Read `<block>/description.md` (bblocks convention) for the long description.
3. Locate example files under `<block>/examples/`. Prefer order: `.geojson` / individual GeoJSON `Feature` `.json` files → `.jsonfg` → `.gpkg` → `.parquet` → CSV with WKT.
4. If examples are individual `.json` GeoJSON Features, combine all schema-valid Feature files into `build-local/test-harness/<block>/data/<collection_id>.geojson` as a `FeatureCollection`; do not modify the source examples.
5. **Fail fast** if no usable example file exists. Surface:
   > No vector example found in `<block>/examples/`. The harness requires at least one `.geojson`, `.gpkg` or `.parquet` example. Add one or supply `sample=` explicitly.

### Phase 2 — detect provider type

```
.geojson  → name: GeoJSON
.json     → if GeoJSON Feature(s), derive FeatureCollection `.geojson`, name: GeoJSON
.gpkg     → name: GeoPackage
.parquet  → name: GeoParquet
.csv      → name: CSV  (with x_field / y_field / geom_field detected from headers)
.fgb      → name: FlatGeobuf
otherwise → name: OGR  with the OGR driver autodetected
```

### Phase 3 — emit YAML

Write the file using this template (Jinja-rendered with the gathered values):

```yaml
server:
  bind:
    host: 0.0.0.0
    port: ${port}
  url: http://${host}:${port}
  mimetype: application/json
  encoding: utf-8
  language: en-US
  cors: true
  pretty_print: true
  limit: 10                    # required so bare /items works without ?limit=
  templates:
    path: /pygeoapi/templates           # mounted by pygeoapi-local-runner
  manager:
    name: TinyDB
    connection: /tmp/pygeoapi-tinydb.json
  map:
    url: https://tile.openstreetmap.org/{z}/{x}/{y}.png
    attribution: Map data (c) OpenStreetMap contributors

logging:
  level: ERROR

metadata:
  identification:
    title: ${block.name} — local test harness
    description: ${block.abstract}
    keywords: [ogc, bblock, ${block-name}, local-test]
    keywords_type: theme
    terms_of_service: local test harness only
    url: ${block.itemIdentifier}
  license:
    name: CC-BY 4.0
    url: https://creativecommons.org/licenses/by/4.0/
  provider:
    name: ILIAD APIs Features (test harness)
    url: https://github.com/ogcincubator/iliad-apis-features
  contact:
    name: local
    email: local@example.org

resources:
  ${collection_id}:
    type: collection
    title: ${block.name}
    description: ${block.abstract}
    keywords: [${block-name}]
    links: []                  # pygeoapi OpenAPI generation expects this key
    extents:
      spatial:
        bbox: [-180, -90, 180, 90]
        crs: http://www.opengis.net/def/crs/OGC/1.3/CRS84
    providers:
      - type: feature
        name: ${provider_name}
        data: /pygeoapi/data/${sample_basename}
        id_field: id           # falls back to fid / OBJECTID / row index
    linked-data:
      context: ${inline_context_array}            # parsed bblock @context as a YAML list
      schema: /pygeoapi/data/schema.json          # bblock schema (for validator skill)
```

### Phase 4 — verify

After writing the file, run a quick YAML-parse + structural check:

- top-level keys: `server`, `logging`, `metadata`, `resources` present
- exactly one collection declared
- `data:` path is reachable in the mount layout
- `server.limit`, `server.map`, `metadata.identification.terms_of_service`, and `resources.<id>.links` are present
- `linked-data.context` is a list/object, not a string path

## Outputs

- `${out}` — the generated `pygeoapi-config.yml`
- A small manifest returned to the caller:

```json
{
  "config":         "build-local/test-harness/<block>/pygeoapi-config.yml",
  "block":          "_sources/<block>",
  "collection_id":  "<block-name>",
  "sample":         "examples/<file> or derived data/<collection_id>.geojson",
  "provider":       "GeoJSON",
  "mount_data":     "build-local/test-harness/<block>/data",
  "mount_context":  "_sources/<block>/context.jsonld",
  "mount_schema":   "_sources/<block>/schema.json"   // or schema.yaml normalised
}
```

## Edge cases

| Situation | Handling |
|---|---|
| `schema.yaml` instead of `schema.json` | Convert to JSON and emit `data/schema.json` under `build-local/test-harness/<block>/` |
| Multiple individual GeoJSON Feature `.json` files | Combine all schema-valid Features into one derived FeatureCollection and surface the count in the manifest |
| Multiple full vector datasets | Pick the first by priority order; surface the list and the chosen one in the manifest |
| `description.md` missing | Use `bblock.json.abstract` as the description |
| `id` field missing in features | Fall back to `id_field: fid` then `id_field: row_number`; surface a warning |
| Block has `schema:` block already in `bblock.json` linking external schemas | Use those URIs as `additional-properties` references; do not embed them |

## Interactions with other skills

- **Output → `pygeoapi-jsonld-template`** uses the manifest to know which collection to template.
- **Output → `pygeoapi-local-runner`** consumes the config + mount paths.
- **`bblock-register-resolution`** is called when the bblock declares external `dependsOn` schemas that need to be fetched before this skill can finish.

## References

- pygeoapi configuration reference — https://docs.pygeoapi.io/en/latest/configuration.html
- pygeoapi providers — https://docs.pygeoapi.io/en/latest/data-publishing/ogcapi-features.html
- OGC API – Features — https://ogcapi.ogc.org/features/
