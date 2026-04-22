---
description: Validate an OGC building block via Docker container (schema, context, examples, tests)
argument-hint: <path-to-_sources/block-name>
---

Validate the OGC building block at `$ARGUMENTS` using the `validation-agent`.

Run a full validation including:
1. Structure check — all required files present and correctly named
2. Schema validation — JSON Schema syntax and JSON-LD context validity
3. Example compliance — example data conforms to schema
4. Semantic coverage — all properties have context entries with authoritative vocabulary URIs
5. Test execution — test suites pass
6. Provenance — metadata and source URLs documented

Use the `bblock-container-validation` skill to run the Docker-based ogcincubator/bblocks-postprocess container.

Report results as:
- Structure check results
- Schema validation summary
- Example compliance report
- Context completeness analysis (missing vocabulary mappings)
- Test execution results
- Overall validation status (Pass / Warnings / Errors)

If `$ARGUMENTS` is empty, ask the user to specify a building block path (e.g., `_sources/macroobservation`).
