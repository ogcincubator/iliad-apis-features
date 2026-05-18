---
name: pygeoapi-local-runner
description: Use when starting, stopping, or interacting with a local pygeoapi Docker container for OGC building block testing. Wraps `docker run` with the right mount layout (config + templates + bblock examples + context + schema) and exposes lifecycle commands. Use as the runtime layer of pygeoapi-test-harness; not for production deployments.
---

**Status**: pre-release · **Scope**: generic · **Building-block coupling**: none.  
_Just authored; Docker lifecycle for local pygeoapi._

# pygeoapi Local Runner Skill

## Purpose

Run pygeoapi locally in a Docker container with one bblock's data and templates mounted, then expose its base URL to subsequent skills. Provides the lifecycle (`start` / `stop` / `logs` / `restart`) needed by the test harness.

## Activation

Use this skill when:

- a `pygeoapi-config.yml` and templates have been generated and the next step is to actually serve them
- the harness needs to fetch `?f=jsonld` responses for validation
- a developer wants to manually browse the served features (with `--keep-running`)

Do not use this skill for:

- production deployments
- multi-instance load testing
- non-Docker runtimes (native venv etc.)

## Required input

- `config_path` — path to `pygeoapi-config.yml` (output of `pygeoapi-config-generator`)
- `block_path` — `_sources/<block-name>/` (for data, context, schema mounts)
- `templates_dir` — path to the templates tree (output of `pygeoapi-jsonld-template`)

## Optional input

| Parameter | Default | Meaning |
|---|---|---|
| `command` | `start` | `start` / `stop` / `logs` / `restart` / `status` |
| `image` | `geopython/pygeoapi:latest` | container image |
| `port` | `5000` | host port; map to container port `80` for `geopython/pygeoapi:latest` |
| `container_name` | `iliad-pygeoapi-test` | for stop/restart lookup |
| `keep_running` | `false` | leave the container up after the harness exits |
| `wait_seconds` | `30` | max wait for `/openapi` to return 200 |

## Process

### `start`

1. **Stop any prior container** with the same `container_name`:
   ```bash
   docker rm -f iliad-pygeoapi-test 2>/dev/null || true
   ```
2. **Compute mount layout**:
   ```
   ${config_path}                      → /pygeoapi/local.config.yml      (ro)
   ${harness_data_dir}                 → /pygeoapi/data                  (ro)
   # contains derived FeatureCollection, context.jsonld, and schema.json
   ${templates_dir}                    → /pygeoapi/templates             (ro)
   ${harness_dir}/sitecustomize.py      → /etc/python3.10/sitecustomize.py (ro, optional)
   ```
   If `schema.yaml` exists instead of `schema.json`, the prior step (`pygeoapi-config-generator`) normalised it to JSON under `build-local/test-harness/<block>/data/schema.json`.
3. **Start the container**:
   ```bash
   docker run -d \
     --name iliad-pygeoapi-test \
     -p 5000:80 \
     -e PYGEOAPI_CONFIG=/pygeoapi/local.config.yml \
     -e PYGEOAPI_OPENAPI=/tmp/openapi.yml \
     -e BBLOCK_CONTEXT=/pygeoapi/data/context.jsonld \
     -v "${config_path}:/pygeoapi/local.config.yml:ro" \
     -v "${harness_data_dir}:/pygeoapi/data:ro" \
     -v "${templates_dir}:/pygeoapi/templates:ro" \
     -v "${sitecustomize_path}:/etc/python3.10/sitecustomize.py:ro" \
     geopython/pygeoapi:latest
   ```
4. The Docker entrypoint generates OpenAPI automatically from `/pygeoapi/local.config.yml`. Do not run a separate `docker exec pygeoapi openapi generate` unless the image changes and logs show it is needed.
5. **Health check loop** — until `wait_seconds`:
   ```bash
   curl -sf http://localhost:5000/openapi >/dev/null && break
   ```
6. **Return base URL manifest**:
   ```json
   {
     "base":           "http://localhost:5000",
     "openapi":        "http://localhost:5000/openapi",
     "collections":    "http://localhost:5000/collections",
     "collection":     "http://localhost:5000/collections/<collection_id>",
     "items":          "http://localhost:5000/collections/<collection_id>/items",
     "items_json":     "http://localhost:5000/collections/<collection_id>/items?f=json&limit=10",
     "items_jsonld":   "http://localhost:5000/collections/<collection_id>/items?f=jsonld&limit=10",
     "container":      "iliad-pygeoapi-test"
   }
   ```

### `stop`

```bash
docker rm -f iliad-pygeoapi-test
```

### `logs`

```bash
docker logs --tail 200 iliad-pygeoapi-test
```

### `restart` / `status`

`restart` is `stop` + `start`. `status` is `docker inspect` for the container's `State.Running` flag plus a `curl /openapi` probe.

## Outputs

- A running container (when `command=start` and health check passes), or
- A clean state (when `command=stop`), or
- The manifest dict shown above.

## Failure modes

| Situation | Handling |
|---|---|
| Docker not running | abort with message "Docker is required for the pygeoapi runner. Start Docker Desktop or `dockerd`." |
| Port already in use | suggest `port=` override |
| Image pull failure | retry once, then surface the docker error verbatim |
| Health check times out | dump last 50 log lines via `docker logs --tail 50 iliad-pygeoapi-test`; abort harness |
| `/collections/<id>/items` returns 500 without `limit=` | add `server.limit: 10` to generated config and restart |
| `?f=jsonld` fails with `.copy()` on string | inline `linked-data.context` as a list/object, not `/pygeoapi/data/context.jsonld` |
| `/openapi` fails with missing `terms_of_service` or `links` | ensure generated config has `metadata.identification.terms_of_service` and `resources.<id>.links: []` |
| Container exits during start | dump full logs and surface the exit code |

## Cleanup

By default the harness calls this skill with `command=stop` at the end. With `keep_running=true`, the container is left up and the harness prints a hint:

> pygeoapi is running at http://localhost:5000. Stop it with `docker rm -f iliad-pygeoapi-test`.

## References

- pygeoapi Docker image — https://hub.docker.com/r/geopython/pygeoapi
- pygeoapi quickstart — https://docs.pygeoapi.io/en/latest/installation.html#docker
