---
name: embedding-store
description: Use when reading, writing, or querying vector embeddings for OGC building blocks (or any other corpus) against a configurable set of vector-database backends — Chroma, Qdrant, Pinecone, OpenAI (parquet-cached), and precomputed parquet. Single dispatch layer that hides backend-specific calls behind a normalised interface (`get`, `upsert`, `query`, `delete`, `list-backends`, `health`). Called by `bblock-catalog` (read-only lookups) and `bblock-relevance` (read + write + similarity). Embeds text on the fly using each backend's configured model when only text is supplied.
---

# Embedding Store Dispatcher Skill

## Purpose

Be the only place in the workspace that knows how to talk to a vector database. Other skills (`bblock-catalog`, `bblock-relevance`, and future consumers) declare *which* backend they want by name and *what* operation they need; this skill resolves the backend, opens the connection, performs the call, normalises the response shape, and returns. The result: backend-specific code lives in exactly one place; adding a new backend (or moving from Chroma to Qdrant) is a config change, not a skill rewrite.

## Activation

Use this skill when the user — or another skill — asks to:

- *get* the embedding coordinates of one or more bblock ids
- *query* nearest neighbours for a free-text question or a probe vector
- *upsert* embeddings for a batch of bblocks (after generation or reindexing)
- *delete* embeddings (e.g. when a bblock is removed)
- *list* the configured backends and their health
- *check* a specific backend's reachability

Do not use this skill for:

- bblock inventory (use `bblock-catalog`)
- relevance scoring across many dimensions (use `bblock-relevance` — it calls this skill internally for the embedding dimension)
- generic web/HTTP fetches (use `web-browsing-mcp`)

## Operations

| Operation | Required args | Optional args | Returns |
|---|---|---|---|
| `get` | `ids: string[]` | `backend?`, `include_metadata?` | `[{id, embedding: {backend, model, dim, vector} | null, metadata?}]` |
| `query` | `vector: number[]` *or* `text: string` | `backend?`, `top_k=10`, `filter?`, `include_vectors=false` | `[{id, score, metadata, embedding?}]` |
| `upsert` | `items: [{id, vector? | text?, metadata?}]` | `backend?`, `embed_model?` | `{upserted: n, skipped: n, model, dim}` |
| `delete` | `ids: string[]` | `backend?` | `{deleted: n}` |
| `list-backends` | — | — | `[{name, type, default, health, model, dim}]` |
| `health` | `backend: string` | — | `{ok: bool, message, latency_ms}` |

Every operation accepts an optional `backend` name. When omitted, the skill uses `embeddings.default` from `.claude/embedding-store.yaml`.

## Supported backends

| Type | Read | Write | Query NN | Embed-on-write | Notes |
|---|---|---|---|---|---|
| `chromadb` | ✓ | ✓ | ✓ | ✓ (via collection's embedding function) | Local on-disk persistent collection. Cheapest to set up. |
| `qdrant` | ✓ | ✓ | ✓ | external (skill embeds first) | Remote, fast nearest-neighbour. Supports payload filters. |
| `pinecone` | ✓ | ✓ | ✓ | external | Hosted; supports metadata filters and namespaces. |
| `openai` | ✓ (parquet cache) | ✓ (writes to parquet cache) | brute-force cosine in memory | live API call | No real DB — embeddings are cached in a parquet next to the workspace. Fine for ≤ a few thousand items. |
| `precomputed` | ✓ | ✗ | brute-force cosine in memory | n/a | Read-only parquet/feather of `{id, vector}` pairs, useful for snapshots / CI / reproducibility. |

The skill also enforces **dimension consistency**: all entries inside one backend's collection must share the same `dim`. A mismatch (e.g. caller supplies an OpenAI 1536-d vector against a Chroma collection initialised at 384-d) raises a clear error rather than silently corrupting the store.

## Configuration

Looked up in priority order:

1. `<workspace>/.claude/embedding-store.yaml`
2. `~/.claude/embedding-store.yaml`
3. `.claude/skills/embedding-store/config.example.yaml` (defaults)

Schema:

```yaml
default: local-chroma            # the backend used when callers omit `backend`

backends:
  local-chroma:
    type: chromadb
    path: ./build-local/.embeddings/chroma
    collection: bblocks
    embed_with: sentence-transformers/all-MiniLM-L6-v2

  qdrant:
    type: qdrant
    url: http://localhost:6333
    api_key_env: QDRANT_API_KEY    # optional
    collection: bblocks
    embed_with: openai:text-embedding-3-small

  pinecone:
    type: pinecone
    api_key_env: PINECONE_API_KEY
    index: bblocks
    namespace: production            # optional
    embed_with: openai:text-embedding-3-small

  openai:
    type: openai
    api_key_env: OPENAI_API_KEY
    model: text-embedding-3-small
    cache: ./build-local/.embeddings/openai.parquet

  precomputed:
    type: precomputed
    path: ./build-local/.embeddings/bblocks.parquet
```

`embed_with` accepts:

- `sentence-transformers/<model>` — local SBERT model
- `openai:<model>` — OpenAI embeddings (requires `OPENAI_API_KEY`)
- any HuggingFace model id supported by `sentence-transformers`

## Process per operation

### `get`

```python
# pseudocode
config = load_config(workspace, user, defaults)
backend = config.backends[args.backend or config.default]

match backend.type:
  case "chromadb":
    col = chromadb.PersistentClient(backend.path).get_collection(backend.collection)
    result = col.get(ids=ids, include=["embeddings","metadatas"])
  case "qdrant":
    result = qdrant.retrieve(backend.collection, ids=ids, with_vectors=True, with_payload=include_metadata)
  case "pinecone":
    result = pinecone.fetch(ids=ids, namespace=backend.namespace)
  case "openai":
    result = parquet.lookup(backend.cache, ids=ids, columns=["embedding","metadata"])
  case "precomputed":
    result = parquet.lookup(backend.path, ids=ids, columns=["embedding"])

return normalise(result, backend)   # → [{id, embedding:{backend,model,dim,vector}|null, metadata}]
```

### `query`

If `text` is supplied: embed it first using the backend's `embed_with` model, then run the nearest-neighbour call. If `vector` is supplied: run the call directly. For `openai` and `precomputed` backends (no native NN index), compute brute-force cosine over all rows and return top-k.

### `upsert`

For each item:

- if `vector` supplied → store directly
- if `text` supplied → embed using `embed_with` and store both the vector and `metadata.text = text`
- skip duplicates whose `id` already exists with a matching `vector` checksum

Report counts in the return.

### `delete`

Backend-native delete by id. For parquet-backed stores, rewrites the file atomically.

### `list-backends` / `health`

Iterate the config; for each backend run a cheap ping (Chroma `count()`, Qdrant `get_collection`, Pinecone `describe_index_stats`, OpenAI list-models, parquet existence). Return `{name, type, default: bool, health: ok|error, message, model, dim}`.

## Normalised output shape

Every operation returns a JSON-serialisable object with a stable shape. Example for `get`:

```json
[
  {
    "id":       "ogc.hosted.seadots.equation-property-relationship",
    "embedding": {
      "backend": "local-chroma",
      "model":   "sentence-transformers/all-MiniLM-L6-v2",
      "dim":     384,
      "vector":  [-0.012, 0.046, -0.118, "…"]
    },
    "metadata": { "name": "Equation property relationship", "itemClass": "schema" }
  },
  {
    "id":       "ogc.hosted.seadots.properties",
    "embedding": null,
    "metadata": { "reason": "not_indexed" }
  }
]
```

For `query`:

```json
[
  { "id": "ogc.hosted.iliad.api.features.macroobservation", "score": 0.84, "metadata": {…} },
  { "id": "ogc.geo.sosa.observation",                       "score": 0.79, "metadata": {…} }
]
```

## Error handling

| Situation | Behaviour |
|---|---|
| Backend not configured | Return `{error: "backend not found", available: [list]}` |
| Backend unreachable | `health` returns `{ok: false, message, latency_ms}`; other operations error fast with a hint to run `health` |
| Dimension mismatch on upsert | Refuse the write, report expected/actual dim |
| Embed-on-write requested but model not available (e.g. missing API key) | Return a clear error naming the missing key |
| `precomputed` backend asked to upsert/delete | Return `{error: "read-only backend"}` |
| Partial hit-rate on `get` | Returns hits + nulls; never aborts the whole batch |
| Two backends share the same id with different vectors | Allowed; callers are expected to scope to one backend per operation |

## Caching

The skill itself is **stateless** for `query`, `upsert`, `delete`. For `get`, an optional in-process LRU caches `{(backend, id) → embedding}` for the duration of a Claude session; bypass with `refresh=true`.

The OpenAI parquet cache and the precomputed parquet are *not* this skill's caches — they are first-class backends.

## Interactions with other skills

- **`bblock-catalog`** — calls `get(ids=...)` in Phase 3b when `include_embeddings=true` is supplied. No write path.
- **`bblock-relevance`** — calls `get(ids=...)` for the `embeddings_similarity` dimension; `upsert(items=...)` from its indexing pipeline; `query(text=...)` for free-text searches.
- **`bblock-register-resolution`** — independent. The store does not care where bblock metadata comes from.

## Embedding model resolution (text → vector)

When a caller supplies `text` instead of `vector`:

```
embed_with                                            → action
sentence-transformers/<model>                         → load locally via `sentence_transformers`
openai:<model> (any backend with api_key_env present) → POST /v1/embeddings, cache to backend's parquet
unset on backend                                      → error: "backend has no embed_with model"
```

The model name + dim are written into the per-row `embedding.model` and `embedding.dim` fields so consumers can detect drift over time.

## Reference

- ChromaDB — https://docs.trychroma.com/
- Qdrant — https://qdrant.tech/documentation/
- Pinecone — https://docs.pinecone.io/
- OpenAI embeddings — https://platform.openai.com/docs/guides/embeddings
- sentence-transformers — https://www.sbert.net/
- parquet (Apache Arrow) — https://arrow.apache.org/docs/python/parquet.html
