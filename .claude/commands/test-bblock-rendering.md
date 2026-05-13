---
description: Spin up a local pygeoapi serving one OGC building block, render its features as JSON-LD using the block's context.jsonld, and validate the response against the block's schema + context completeness
argument-hint: <path-to-_sources/block-name> [--collection-id <id>] [--keep-running]
---

Run the pygeoapi test harness against the OGC building block at `$ARGUMENTS` using the `pygeoapi-test-harness` agent.

The harness:

1. Generates a local `pygeoapi-config.yml` from the bblock's example data (skill: `pygeoapi-config-generator`).
2. Generates Jinja2 templates that render features as JSON-LD using the block's `context.jsonld` (skill: `pygeoapi-jsonld-template`).
3. Starts pygeoapi in Docker (`geopython/pygeoapi:latest`) on port 5000 (skill: `pygeoapi-local-runner`).
4. Fetches the rendered `?f=jsonld` response from `/collections/<id>/items` and `/collections/<id>/items/<feature_id>`.
5. Validates each response against the block's `schema.json` (skill: `response-schema-validator`).
6. Walks every property key in every feature against the embedded `@context` to assert no key is unmapped (skill: `context-completeness-checker`).
7. Stops the container — unless `--keep-running` is supplied, in which case it leaves the service up at `http://localhost:5000` for manual exploration.

Report results as:

- **Configuration** — paths to the generated config, templates and mount layout.
- **Service** — base URL, container name, status (running / stopped).
- **Schema validation** — pass/fail per feature with the failing JSON Pointer + message.
- **Context completeness** — unmapped properties (errors), ambiguous mappings (errors), `context_unused` terms (info).
- **Overall** — Pass / Warnings / Errors.

If `$ARGUMENTS` is empty, ask the user to specify a building block path (e.g. `_sources/equation-property-relationship`).

If the bblock has no vector example file or no `context.jsonld`, abort with a clear message — the harness cannot proceed without them.

If Docker is not running, abort with the message "Docker is required for the pygeoapi runner. Start Docker Desktop or `dockerd`."

To clean up afterwards (when `--keep-running` was used), run:

```bash
docker rm -f iliad-pygeoapi-test
```
