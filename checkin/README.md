# ILIAD Check-in Tool

Interactive wizard (CLI + web) that registers a new data source into the ILIAD OGC Building Blocks repository.

## Flow

1. **Register** a data source (file path or URL — NetCDF / CSV / GeoParquet / GeoJSON / OGC WFS/WMS/EDR / OPeNDAP).
2. **Profile** the source: detect format, extract properties, dimensions, spatial/temporal extent.
3. **Match** the profile against existing building blocks in `_sources/`.
4. **Propose** related bblocks based on OGC standards (STAC alongside Coverage, EDR alongside Features, …).
5. **Map vocabularies** — properties auto-matched against the local vocab index built from every `context.jsonld` and `OIM/*.ttl`; user acknowledges each mapping.
6. **Transformer** — reuse a library transformer or generate a bblock-local one; execute it on sample data and validate the output against the canonical schema.
7. **Stage** a new bblock at `_sources/_staging/<name>/`.
8. **Validate** via `ogcincubator/bblocks-postprocess`.
9. **Promote** to `_sources/<name>/`.

## Usage

```bash
pip install -e .
iliad-checkin            # CLI wizard
iliad-checkin-server     # http://localhost:8000 web UI
```

Or via slash command: `/check-in <path-or-url>`.

## Layout

- `core/` — orchestration (sniff, profile, index, match, transform, write)
- `transformers/` — shared transformer library (generic, reusable across bblocks)
- `api/` — FastAPI backend
- `web/` — vanilla HTML + htmx wizard
- `cli.py` — terminal flow

Per-bblock transformers live inside the bblock: `_sources/<bb>/transforms/`. A transformer becomes a library transformer once it is used by ≥ 2 bblocks.
