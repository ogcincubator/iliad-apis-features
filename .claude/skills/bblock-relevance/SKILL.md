---
name: bblock-relevance
description: Use when ranking existing OGC building blocks by their relevance to a candidate input — an example data file, free-text documentation, a service endpoint, and/or a metadata record. Computes six similarity dimensions (data/service type, property names, data-model structure, vocabulary IRIs, themes/keywords, vector-embedding cosine), aggregates them with configurable weights, and returns ranked bblocks grouped by `itemClass` (schema vs. schemaless) × intent (data vs. metadata). Vector-DB access is delegated to the `embedding-store` skill (backends configured in `.claude/embedding-store.yaml`); this skill only declares the backend name and the weight assigned to the embedding dimension. Extracts the relevance-ranking step previously embedded in the `check-in` command and the `data-usability-checkin-agent`.
---

# OGC Building Block Relevance Scorer

## Purpose

When the user has a candidate dataset (example file / docs / endpoint / metadata record) and wants to know *"which existing bblock fits this best, locally or in any imported register"*, this skill answers with a ranked table — grouped by bblock type — and a per-dimension explanation of every score. Replaces the ad-hoc `property-name + context-vocab + format-tag overlap` heuristic mentioned in `check-in` step 4 and in `data-usability-checkin-agent`'s "Rank candidate target blocks" step with one well-defined, weighted, configurable algorithm.

## Activation

Use this skill when the user asks to:

- "find the best matching bblock for this dataset / endpoint / example"
- "rank bblocks by relevance to <X>"
- "is there a bblock that already fits this data model / vocabulary / theme?"
- "compare my schema against bblocks in the repo + imports"
- "score bblocks for the BB1 / BB2 / BB3 picks in a check-in"

Do not use this skill for:

- listing the catalog (use `bblock-catalog`)
- generating new bblocks (use `building-block-generator`)
- validating a bblock (use `validation-agent` / `bblock-container-validation`)

## Inputs

At least one of:

| Input | Type | Meaning |
|---|---|---|
| `example` | file path or URL | A representative data example. Format auto-detected: GeoJSON / JSON-FG / NetCDF / Zarr / CSV / Parquet / STAC Item. |
| `documentation` | string or file path | Free-text or markdown describing the dataset, the data product, or the service. |
| `endpoint` | URL | A service URL — OGC API (Features / Coverages / EDR / Records / STAC), WMS / WFS, ArcGIS REST. Capabilities or `OpenAPI` is fetched to extract metadata. |
| `metadata` | file path or URL | STAC Item, DCAT Record, OGC Records Feature, ISO 19139 XML, or any other catalogue record. |

Optional:

| Parameter | Default | Meaning |
|---|---|---|
| `scope` | `all` | `local` (only `_sources/`), `imported`, or `all` (uses `bblock-catalog`). |
| `top_k` | `20` | Maximum ranked blocks per group. |
| `weights` | from config / defaults | Per-dimension weight override (object). |
| `dimensions` | `["type","properties","model","vocabulary","themes","embeddings"]` | Which dimensions to compute. Excluding a dimension renormalises the remaining weights to sum to 1. |
| `embeddings` | from config | Vector-backend name to use (e.g. `local-chroma`, `openai`). |
| `refresh` | `false` | Bypass any local cache. |

## Configuration

Looked up in priority order:

1. `<workspace>/.claude/bblock-relevance.yaml`
2. `~/.claude/bblock-relevance.yaml`
3. `.claude/skills/bblock-relevance/config.example.yaml` (defaults shipped with the skill)

Format — note that **backend configuration lives in `.claude/embedding-store.yaml`**, not here. This file only carries weights, grouping rules, cache settings, and the name of the embedding backend to use (by reference):

```yaml
weights:
  type_match:            0.20
  properties_match:      0.20
  model_match:           0.20
  vocabulary_match:      0.15
  themes_keywords_match: 0.10
  embeddings_similarity: 0.15

embeddings:
  backend: local-chroma          # name resolved by the embedding-store skill;
                                 # omit to use embedding-store's own default.

cache:
  dir: ./build-local/.relevance
  ttl_hours: 24

grouping:
  axes: [itemClass, intent]      # schema vs. schemaless × data vs. metadata
  intent_rules:
    data:     [vector, gridded, model, vocabulary]
    metadata: [metadata]
    ontology: [ontology]
```

## Dimensions

Each dimension produces a score in `[0, 1]`. Missing-data behaviour: when a dimension cannot be computed (e.g. no example file → no `properties_match`), its weight is redistributed proportionally across the remaining dimensions.

### 1. `type_match` (0–1)

Classify the **input** with the same rules as `bblock-catalog`'s classifier:

| Input observation | → category |
|---|---|
| GeoJSON / JSON-FG / GeoPackage / GeoParquet / WFS / OGC Features | vector |
| NetCDF / Zarr / GRIB / COG / CoverageJSON / OGC Coverages / EDR | gridded |
| STAC Item / DCAT Record / OGC Records Feature / ISO 19139 | metadata |
| OWL / SKOS / SHACL Turtle / `.ttl` | ontology |
| ODD Protocol / equation record / SES impact assessment | model |

Compare input category to each bblock's primary category (already classified):

- exact match → **1.0**
- compatible (e.g. input metadata, bblock metadata-profile of gridded) → **0.7**
- adjacent (e.g. input vector, bblock metadata about vector) → **0.4**
- unrelated → **0.0**

### 2. `properties_match` (0–1)

Extract property names from the input:

- **example file**: top-level JSON keys + `properties.*` keys; NetCDF variable names; CSV headers; STAC `properties` keys
- **endpoint**: queryable / output fields from `GetCapabilities` / OpenAPI
- **metadata**: top-level keys + nested `properties` keys
- **documentation**: heading words and inline-code identifiers (best-effort)

Extract candidate properties from each bblock:

- `schema.json|yaml`: every `properties.*` key including nested objects
- `context.jsonld`: every term mapped to an `@id`
- absent in `ontology.ttl`-only blocks (score = 0 unless `vocabulary_match` is high)

Score = **Jaccard** `|A ∩ B| / |A ∪ B|`, fuzzy-matched on snake / kebab / camelCase normalisations.

### 3. `model_match` (0–1)

Structural similarity of the input's inferred JSON-Schema against the bblock's schema:

1. Build an input schema (using `metadata-extraction` skill heuristics for non-JSON inputs).
2. Walk both schemas in parallel.
3. For every shared property: type-agreement = 1 if types equal, 0.5 if compatible (number vs. integer, etc.), 0 otherwise.
4. Required-status agreement weighted ×2.
5. Penalise the bblock for required properties it has but the input lacks (signals the input is *narrower*, not a fit).

Final = weighted mean over shared property nodes, clamped to `[0, 1]`.

### 4. `vocabulary_match` (0–1)

Extract vocabulary IRIs:

- from input: parse any embedded `@context` (JSON-LD) or known `vocabularyTerm` / `@id` fields; expand DCAT / STAC well-known properties to their IRIs
- from each bblock: every distinct `@id` value in `context.jsonld`; every `skos:exactMatch` / `closeMatch` URI in `ontology.ttl`

Score = `|input ∩ bblock| / max(|input|, 1)` (asymmetric — measures coverage of the input's vocab).

### 5. `themes_keywords_match` (0–1)

Build a bag-of-words document for each side:

- **input doc** = documentation + extracted themes from metadata + endpoint description + filename tokens
- **bblock doc** = `name` + `abstract` + `tags[]` + `description.md` first paragraph

Compute **TF–IDF cosine** across the corpus = all `_sources/` + imported bblocks. Score = the cosine ∈ `[0, 1]`.

### 6. `embeddings_similarity` (0–1)

Delegated to the `embedding-store` skill. This skill never opens a backend connection directly — it issues two calls:

1. `embedding-store upsert items=[{id: "__candidate-input__", text: <input documentation>}] backend=<configured>` — to embed the input documentation using the backend's `embed_with` model and cache the result.
2. `embedding-store query text=<input documentation> top_k=<N>` — returns the top-N bblock ids with cosine scores against the input. Alternatively, `embedding-store get ids=<all-bblock-ids>` returns vectors which this skill cosines in-memory against the input embedding.

The backend used is `embeddings` (parameter override) or the `embedding-store` default. Configuration of the backends themselves — Chroma / Qdrant / Pinecone / OpenAI parquet / precomputed parquet — lives in `.claude/embedding-store.yaml`; this skill knows backends only by name.

If no backend is configured or reachable (the `embedding-store health` probe fails), set `embeddings_similarity = null` and redistribute its weight to the other dimensions.

## Aggregation

```
overall = Σ ( weight[d] × score[d] )  for d in computed dimensions
          ─────────────────────────────
                  Σ weight[d]            (renormalisation when some d skipped)
```

## Output

### 1. Ranked table per group

Four groups (cross-product of two axes):

| Axis | Values |
|---|---|
| `itemClass` | `schema` (has `schema.json` / `schema.yaml`) vs. `schemaless` (`ontology.ttl` only — itemClass `model`) |
| `intent` | `data` (vector / gridded / model / vocabulary) vs. `metadata` (records / dcat / stac) |

Within each group, sort by `overall` descending. Print only `top_k` per group.

Sample output sketch:

```
schema / data
─────────────────────────────────────────────────────────────────────────────────────────
ID                                                       Source      Overall   type props model vocab themes embed
ogc.hosted.iliad.api.features.macroobservation           local       0.78      1.00  0.55  0.62  0.71  0.69  0.84
ogc.geo.sosa.observation                                 imported    0.71      1.00  0.48  0.55  0.69  0.55  0.79
ogc.hosted.iliad.api.features.iliad-jellyfish-features   local       0.66      1.00  0.45  0.51  0.62  0.61  0.72

schema / metadata
─────────────────────────────────────────────────────────────────────────────────────────
ID                                                       Source      Overall   type props model vocab themes embed
ogc.hosted.iliad.api.features.ses-impact-assessment      local       0.62      0.70  0.38  0.41  0.55  0.71  0.82
ogc.geo.geodcat.geodcat-records                          imported    0.58      0.70  0.32  0.36  0.58  0.61  0.78

schemaless / data
─────────────────────────────────────────────────────────────────────────────────────────
ID                                                       Source      Overall   type props model vocab themes embed
ogc.hosted.seadots.ontology                              imported    0.41      0.40  —     —     0.62  0.51  0.53
ogc.hosted.iliad.api.features.oim-variables              local       0.40      0.40  —     —     0.71  0.49  0.51

schemaless / metadata
─────────────────────────────────────────────────────────────────────────────────────────
(no candidates above the floor)
```

`—` means "not computable on this block". Empty groups are still printed for completeness.

### 2. Per-dimension explanation (drill-down on request)

```
bblock                  macroobservation
overall                 0.78
weights effective       type 0.20 / props 0.20 / model 0.20 / vocab 0.15 / themes 0.10 / embed 0.15

dimension scores
  type_match            1.00   input is vector → bblock category vector
  properties_match      0.55   shared keys: id, geometry, observedProperty, datetime; missing in bblock: sampleSizeUnit, organismQuantityType
  model_match           0.62   ✓ id ✓ geometry ✓ observedProperty (string→string); ✗ datetime (date vs. date-time)
  vocabulary_match      0.71   input vocabs: dwc:scientificName, sosa:observedProperty …
  themes_keywords_match 0.69   tags ∩ doc terms: observation, marine, biodiversity
  embeddings_similarity 0.84   nearest-neighbour in local-chroma collection
```

### 3. Aggregate caveats

The skill always surfaces:

- which dimensions were **computed**, which were **skipped** (and why)
- which **vector backend** answered the embeddings call
- which **bblock register snapshots** were used (from `bblock-catalog`'s cache)
- the **effective weights** after renormalisation

## Process

1. **Load config** (workspace > user > skill defaults).
2. **Inventory bblocks** by calling `bblock-catalog` (with cache).
3. **Ingest input(s)**: for `example`, call `metadata-extraction` to lift to a normalised feature; for `endpoint`, fetch capabilities; for `metadata`, parse; for `documentation`, tokenise.
4. **Per-bblock feature extraction**: read `bblock.json`, `schema.json|yaml`, `context.jsonld`, `description.md`, `ontology.ttl` lazily; cache to `./build-local/.relevance/<bblock-id>.json`.
5. **Compute dimensions** — skip any whose inputs are missing.
6. **Embeddings**: if enabled, batch-call the configured backend; cache.
7. **Aggregate, renormalise, group, sort, truncate**.
8. **Format & print** the four-group table and the requested drill-downs.

## Edge cases

| Situation | Handling |
|---|---|
| Multiple inputs of different shapes | Compute features independently from each input; OR their property/vocab sets; merge themes; take max per dimension across inputs. |
| Bblock has neither `schema.*` nor `context.jsonld` (pure-ontology) | Compute only `vocabulary_match` and `themes_keywords_match` + `embeddings_similarity`; record `model_match = null`. |
| Embeddings backend unreachable | Fail soft — set `embeddings_similarity = null`, redistribute weight, surface the backend error. |
| Input is itself a bblock | Skip its own id from results; otherwise score normally (useful when looking for siblings). |
| `bblock-catalog` cache stale | Refresh on the first call; honour `refresh=true` to force. |

## Interactions with other skills

- **`bblock-catalog`** — source of the bblock list and the classification.
- **`embedding-store`** — dispatcher for every vector-DB call this skill makes (`upsert` to index, `query`/`get` to score). All backend-specific code (Chroma / Qdrant / Pinecone / OpenAI / precomputed) lives in that skill, not here.
- **`metadata-extraction`** — used to normalise non-JSON example inputs into a schema-shaped object.
- **`bblock-register-resolution`** — fetches imported registers when a bblock-catalog cache miss requires it.
- **`web-browsing-mcp`** — used when `endpoint` is supplied and capabilities must be fetched live.
- **`bblock-container-validation`** / **`validation-agent`** — referenced from the output ("the top candidate validates against your example — try `/validate-bblock` …").
- **`pygeoapi-test-harness`** — referenced when the user accepts a top candidate ("serve your example through this bblock — try `/test-bblock-rendering` …").

## Provenance the skill prints with every run

```
relevance-run-id    2026-05-14T11:08:12Z-3f7a
inputs              example=examples/utsira.geojson  doc=docs/utsira.md
scope               all
catalog snapshot    build-local/.cache/registers/{iliad,seadots,sosa,stac,…}.json (ttl 24h)
backend             local-chroma  (124 bblocks embedded; 7 missing — listed below)
weights effective   type 0.20 / props 0.20 / model 0.20 / vocab 0.15 / themes 0.10 / embed 0.15
dimensions skipped  (none)
```

## References

- `bblock-catalog` skill — `.claude/skills/bblock-catalog/SKILL.md`
- `check-in` command (delegates ranking here) — `.claude/commands/check-in.md`
- `data-usability-checkin-agent` (delegates BB-selection ranking here) — `.claude/agents/data-usability-checkin-agent.md`
- ChromaDB — https://docs.trychroma.com/
- Qdrant — https://qdrant.tech/documentation/
- Pinecone — https://docs.pinecone.io/
- OpenAI embeddings — https://platform.openai.com/docs/guides/embeddings
- sentence-transformers — https://www.sbert.net/
