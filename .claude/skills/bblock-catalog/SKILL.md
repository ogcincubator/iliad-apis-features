---
name: bblock-catalog
description: Use when answering questions about the OGC building-block structure of this repository and the registers it imports — what blocks exist, what each one is for, which are vector vs. gridded vs. ontology vs. metadata, what is locally hosted vs. imported, what depends on what. Walks _sources/ for local blocks, reads bblocks-config.yaml for imports, fetches each imported repo's register.json, classifies blocks by category, and answers ad-hoc natural-language queries with a compact tabular summary plus optional drill-downs. With `include_embeddings=true` also returns embedding coordinates per matched block (looked up in the vector backends configured for the `bblock-relevance` skill), for downstream clustering / projection / similarity tooling.
---

# OGC Building Block Catalog Skill

## Purpose

Be the one place that answers "what's in this repo and what's imported" — for one workspace or for any other bblocks-postprocess-shaped repo. The skill does three things:

1. **Inventories** every locally hosted bblock (under `_sources/`).
2. **Resolves** every register URL listed in `bblocks-config.yaml` `imports:` and pulls its `register.json`.
3. **Classifies** each block (local + imported) into useful categories — vector, gridded, ontology, metadata, model, vocabulary, profile — and answers natural-language questions over the result.

## Activation

Use this skill when the user asks:

- "what blocks are available for vector data / gridded data / metadata / ontologies"
- "what does this repo import?"
- "what depends on `X`?" / "what is `X` used by?"
- "find a block that handles `<theme>`"
- "is there already a bblock for `<intent>`?"
- "show me the seadots / iliad / bblocks-stac inventory"
- "what's the difference between `oim-obs` and `oim-bio-tdwg`?"

Do NOT use this skill to:

- generate new bblocks (use `building-block-generator`)
- validate (use `validation-agent` / `bblock-container-validation`)
- run pygeoapi tests (use `pygeoapi-test-harness`)

## Required input

A free-text question OR one or more structured filters:

| Filter | Meaning |
|---|---|
| `category` | one of `vector`, `gridded`, `ontology`, `metadata`, `model`, `vocabulary`, `profile`, `quality`, `unclassified` |
| `source` | one of `local` (this repo), `<register-url>`, or `all` (default) |
| `tag` | substring match against the block's `tags[]` |
| `itemClass` | `schema` or `model` |
| `id` | exact bblock identifier — returns full record + dependants |
| `depends_on` | bblock identifier — returns the set of blocks depending on it |
| `include_embeddings` | `false` (default) / `true` — when true, call the `embedding-store` skill to attach embedding coordinates per matched block |
| `embeddings_backend` | optional backend name (e.g. `local-chroma`, `qdrant`, `pinecone`, `openai`, `precomputed`) overriding the `default` declared in `.claude/embedding-store.yaml` |

## Process

### Phase 1 — local scan

Walk `_sources/` in the active workspace (default: `pwd`; overridable via `repo=` parameter):

```bash
for bb in _sources/*/bblock.json; do
  jq -c '{
    path: (input_filename | sub("_sources/"; "") | sub("/bblock.json"; "")),
    name, abstract, itemClass, register, version, status, tags, dependsOn,
    license, maturity, scope
  }' "$bb"
done
```

For each local block also probe what other files exist alongside `bblock.json`:

| File present | Implication |
|---|---|
| `schema.json` or `schema.yaml` | schema block, JSON-validatable |
| `context.jsonld` | JSON-LD enriched |
| `ontology.ttl` | ontology block (OWL/SKOS) |
| `rules.shacl` | SHACL constraints |
| `examples/` | has examples |
| `tests/` | has test suite |

### Phase 2 — import resolution

Read `bblocks-config.yaml`:

```bash
yq '.imports[]' bblocks-config.yaml
```

For each non-`default` import URL, call the `bblock-register-resolution` skill (or inline the same logic: try `<url>/build/register.json` first, then `<url>/register.json`). Cache the parsed JSON under `build-local/.cache/registers/<host-slug>.json`. Bypass cache when the user explicitly says `refresh=true`.

`default` resolves to the upstream OGC register at `https://opengeospatial.github.io/bblocks/register.json`.

### Phase 3 — classify

Apply this rule cascade (first match wins for the *primary* category; multiple categories may apply, all are recorded):

```
ontology       ← itemClass == "model"  OR  has ontology.ttl  OR  tags ∋ {"ontology", "ontologies"}
vocabulary     ← tags ∋ {"vocabulary", "skos", "indicator", "rainbow", "variable", "variables"}
                OR id ∋ ["oim-variables", "nerc-cf-standard-names"]
metadata       ← tags ∋ {"metadata", "stac", "dcat", "records", "catalog", "ogc-records"}
                OR id matches /(stac|dcat|records|apkg|coverage_information_model)/
gridded        ← tags ∋ {"netcdf", "zarr", "coverage", "coveragejson", "raster",
                         "cog", "datacube", "grid"}
                OR id matches /(netcdf|zarr|coverage|raster|cog|stac_multidim)/
vector         ← tags ∋ {"geojson", "vector", "feature", "features", "jsonfg",
                         "geoparquet", "ogcapi-features"}
                OR id matches /(geojson|jsonfg|geoparquet|features?)/
model          ← tags ∋ {"odd", "equation", "property-relationship", "model"}
                OR id matches /(odd-protocol|equation-property-relationship|property-relationship)/
quality        ← tags ∋ {"dqv", "quality", "indicator-quality"}
                OR id matches /(indicator-quality|dqv)/
profile        ← name ∋ "profile" AND no other category matched
unclassified   ← everything else
```

A block can carry multiple labels. The primary one is the first match; secondaries are also collected.

### Phase 3b — embedding-coordinate lookup (only when `include_embeddings=true`)

Call the `embedding-store` skill once with the surviving block ids:

```
embedding-store get  ids=[id1, id2, …]  backend=${embeddings_backend or default}
```

The `embedding-store` dispatcher resolves the configured backend (Chroma / Qdrant / Pinecone / OpenAI parquet cache / precomputed parquet) and returns a normalised list of `{id, embedding | null, metadata}`. Attach each result to the matching block record; misses keep `embedding: null` and feed into the "missing ids" summary at the foot of the run.

This skill never writes to the store; it only reads. Indexing is the responsibility of `bblock-relevance` (which calls `embedding-store upsert`). That keeps `bblock-catalog` cheap and side-effect-free for navigation queries.

### Phase 4 — answer

For the active query:

1. **Free-text question** — parse to filters (category, source, tag, …) using the keywords in the question. If ambiguous, ask the user one short clarifying question.
2. **Structured filters** — apply directly.
3. **Single-block lookup** (`id=`) — return: full bblock.json, file inventory, dependants (blocks whose `dependsOn` includes this id), reverse-imports (registers that contain this id).
4. **Dependency query** (`depends_on=`) — return both directions:
   - *forward*: the block's `dependsOn` list (fully resolved to register entries).
   - *reverse*: every block in the local + imported registers that lists this id under `dependsOn`.

### Output formats

**Tabular summary** (default — no embedding column shown unless `include_embeddings=true`):

```
Source                                     Category     ID                                  Name                           Status
─────────────────────────────────────────  ───────────  ──────────────────────────────────  ─────────────────────────────  ────────
local                                      vector       ogc.hosted.iliad.api.features
                                                          .geoparquet                       GeoParquet                     development
local                                      gridded      ogc.hosted.iliad.api.features
                                                          .stac_multidim_data               STAC multidim data             development
imported (bblocks-seadots)                 model        ogc.hosted.seadots.odd-protocol     ODD Protocol Description       under-development
imported (bblocks-seadots)                 model        ogc.hosted.seadots
                                                          .equation-property-relationship   Equation property relationship under-development
imported (bblocks-seadots)                 ontology     ogc.hosted.seadots.ontology         Property relationship ontology under-development
...
```

**Embedding-augmented row shape** (when `include_embeddings=true`):

For consumers that need machine-readable output (e.g. a 2-D projection plot or a downstream similarity job), the skill also emits a JSON Lines stream alongside the table, one block per line:

```json
{
  "id":            "ogc.hosted.seadots.equation-property-relationship",
  "source":        "imported (bblocks-seadots)",
  "category":      "model",
  "secondary":     ["vocabulary"],
  "itemClass":     "schema",
  "name":          "Equation property relationship",
  "embedding": {
    "backend":  "local-chroma",
    "model":    "sentence-transformers/all-MiniLM-L6-v2",
    "dim":      384,
    "vector":   [-0.0123, 0.0456, …]
  }
}
```

Blocks without an embedding hit get `"embedding": null`. The default text rendering truncates the vector to the first three components plus a count, e.g. `[-0.012, 0.046, -0.118, … (384d)]`; the full vector is in the JSONL stream.

A short header line declares the backend, model and total hit-rate:

```
embeddings   backend=local-chroma   model=sentence-transformers/all-MiniLM-L6-v2   dim=384   hits=18/24   missing=6
missing ids:
  ogc.hosted.iliad.api.features.zarr_attrs_sdn
  ogc.hosted.iliad.api.features.iliad-jellyfish-ontology
  …
```

**Counts per category** (always printed at the end):

```
local:    18 blocks    vector 4, gridded 6, metadata 5, ontology 1, model 1, vocabulary 1
imported: 24 blocks    [bblocks-seadots: 5, geodcat-ogcapi-records: 4, ogcapi-sosa: 6, ...]
```

**Per-block detail** (when `id=` is supplied):

```
ogc.hosted.seadots.equation-property-relationship
  name        Equation property relationship
  abstract    Schema profile for declaring …
  itemClass   schema
  status      under-development     version 0.1
  source      seadots
  category    model  (secondary: vocabulary)
  dependsOn   ogc.hosted.seadots.ontology
  depended on by
              ogc.hosted.iliad.api.features.ses-impact-assessment
  has         schema.yaml, context.jsonld, examples/ (2), description.md
  ldContext   context.jsonld
```

## Output sources

| Where the answer comes from | Cache file |
|---|---|
| `_sources/<block>/bblock.json` (local) | (no cache — read live) |
| `<imported-url>/build/register.json` | `build-local/.cache/registers/<host-slug>.json` |
| `bblocks-config.yaml`'s `imports[]` | (no cache — read live) |
| Each block's auxiliary files (`schema.*`, `context.jsonld`, `ontology.ttl`) | (no cache — file-existence check) |

Cache is invalidated either by `refresh=true` or when the source register's `etag`/`last-modified` changes.

## Workflow examples

### "what ontologies are imported?"

```text
Step 1 — local: 1 ontology block found  (ogc.hosted.iliad.api.features.oim-variables)
Step 2 — imports: 7 registers fetched
Step 3 — classify: 9 ontology blocks across all sources
Step 4 — table:

Source                                  ID                                        Name
local                                   ogc.hosted.iliad.api.features.oim-variables    OIM Variables
imported (bblocks-seadots)              ogc.hosted.seadots.ontology                     Property relationship ontology
imported (bblocks-seadots)              ogc.hosted.seadots.properties                   Seadots Properties
imported (cross-domain-model)           ogc.cross-domain.cross-domain-model             …
imported (openscience)                  ogc.osc.ontology.openscience                    Open Science ontology
...
```

### "what blocks handle vector data, both locally and imported?"

```text
Category: vector

local                                   ogc.hosted.iliad.api.features.geoparquet
local                                   ogc.hosted.iliad.api.features.iliad-jellyfish-features
local                                   ogc.hosted.iliad.api.features.dynamic-shoreline
local                                   ogc.hosted.iliad.api.features.macroobservation
imported (ogcapi-sosa)                  ogc.geo.sosa.observation
imported (geodcat-ogcapi-records)       ogc.geo.geodcat.geodcat-records
...
```

### "what's the gridded data story?"

```text
Category: gridded

local                                   stac_multidim_data
local                                   zarr_array_metadata
local                                   zarr_attrs_metadata
local                                   zarr_attrs_sdn
local                                   coverageJSON
local                                   coverageJSONFisheries
local                                   coverage_information_model
imported (bblocks-stac)                 ogc.stac.collection
...
```

### "what does ses-impact-assessment depend on?"

```text
Forward dependencies of ogc.hosted.iliad.api.features.ses-impact-assessment:
  ogc.hosted.seadots.odd-protocol             (seadots, after the recent move)
  ogc.hosted.iliad.api.features.oim-variables (local)
  ogc.hosted.iliad.api.features.indicator-quality-requirement (local)
  ogc.hosted.iliad.api.features.property-relationship         (local)

No reverse dependants found in local + imported registers.
```

### "is there already a bblock for floating-wind ecological impact?"

Returns substring matches on name, abstract, and tags across local + imported, ranked by score, with the top three shown verbatim.

## Edge cases

| Situation | Handling |
|---|---|
| `bblocks-config.yaml` missing | Inventory local only; surface the issue. |
| Import URL unreachable | Skip with a warning; continue with cached copy if present. |
| Cached register older than 24 h | Re-fetch unless the user passed `refresh=false`. |
| Two registers expose the same id | Surface both with their source registers; preference goes to local source. |
| Block has empty `tags[]` and an ambiguous name | Mark `unclassified`; surface for the user to triage. |
| User asks about a block that doesn't exist | Suggest closest matches by name / abstract distance. |
| `include_embeddings=true` but no vector backend configured | Skip Phase 3b with a warning; surface `embeddings: null` on every row and a one-line hint pointing at `.claude/bblock-relevance.yaml`. |
| `include_embeddings=true` but backend reachable, partial hits | Surface coordinates for hits, `null` for misses, and a `missing ids` list at the foot of the run. |
| Backend embeds at a different model than expected | Annotate every row's `embedding.model` field; consumers can detect mismatch. |

## How this skill cooperates with others

- **`bblock-register-resolution`** — used internally to normalise external URLs to register endpoints.
- **`web-browsing-mcp`** — used to fetch registers when the resolver can't determine them statically.
- **`embedding-store`** — sole dispatcher this skill calls for the `include_embeddings=true` lookup. Hides Chroma / Qdrant / Pinecone / OpenAI / precomputed backends behind one interface.
- **`bblock-relevance`** — the *writer* of the same embedding store (`upsert` after generation/reindexing). `bblock-catalog` only reads. The two skills share the backend pool declared in `.claude/embedding-store.yaml`.
- **`validation-agent`** / **`bblock-container-validation`** — referenced from this skill's output ("Want to validate the missing block? Run `/validate-bblock` on…").
- **`pygeoapi-test-harness`** — referenced when the user asks "can I serve this block locally?"
- **`marine-bblock`** / **`building-block-generator`** — referenced when the catalog answer is "nothing yet — would you like to generate one?".

## Reference

- bblocks-postprocess register schema — https://ogcincubator.github.io/bblocks-docs/
- bblocks register format — `<repo>/build/register.json`
- OGC building blocks documentation — https://blocks.ogc.org/
- Local bblocks-config.yaml: `bblocks-config.yaml`
- Local register: `build/register.json` (when built)
