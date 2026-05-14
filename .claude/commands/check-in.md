---
description: Register a new data source and stage an ILIAD OGC building block for it
argument-hint: <path-or-url> [--name=<bb-id>] [--title="..."]
---

Run the check-in wizard for `$ARGUMENTS`. The tool sniffs the data, profiles it, matches against existing building blocks in `_sources/`, proposes related blocks, auto-maps properties to locally-known vocabularies (`_sources/**/context.jsonld` + `OIM/*.ttl`), lets the user acknowledge mappings, picks a transformer from `checkin/transformers/`, executes it, validates the output against the transformer's canonical schema, and writes a staged bblock to `_sources/_staging/<bb-id>/`.

## How to run

Terminal (interactive):

```
cd iliad-apis-features
pip install -e ./checkin
iliad-checkin "$ARGUMENTS"
```

Web UI (wizard):

```
iliad-checkin-server   # http://127.0.0.1:8000/
```

## Behaviour

1. Sniffs the source (NetCDF / CSV / GeoParquet / GeoJSON / OGC WFS/WMS/EDR / OPeNDAP).
2. Profiles properties, dimensions, spatial/temporal extent.
3. Invokes the `bblock-catalog` skill with the inferred category filter (`vector` / `gridded` / `metadata`) and a free-text query built from the profile, covering local `_sources/` **and** every register imported in `bblocks-config.yaml`. Catalog matches are surfaced alongside the local-only ranking in step 4.
4. Ranks candidate bblocks in `_sources/*` by property-name + context-vocab + format-tag overlap (top 5).
5. Proposes related bblocks (OGC standard pairings — STAC + Coverage, EDR + Features, JSON-FG + GeoJSON).
6. Builds a vocab index and surfaces per-property candidates for user acknowledgement. External candidates (NERC / CF / Darwin Core / WoRMS) are linked out; external lookups proper are delegated to the `web-browsing-mcp` skill.
7. Picks or generates a transformer, executes it on a sample, and validates the output against the transformer's `canonical.schema.json`.
8. Stages the new bblock at `_sources/_staging/<bb-id>/` and prints the path **only when the catalog returned no suitable match in step 3**. When a strong match exists, prefer reuse or profile extension over staging a duplicate. Run `/validate-bblock _sources/_staging/<bb-id>` before promoting.

## After staging

- `/validate-bblock _sources/_staging/<bb-id>` to run the Docker OGC postprocessor.
- Promote: in the web UI, or `iliad-checkin promote --id <bb-id>`.
