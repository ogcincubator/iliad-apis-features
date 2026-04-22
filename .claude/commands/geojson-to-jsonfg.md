---
description: Convert GeoJSON to JSON-FG with OIM semantic enrichment
argument-hint: <geojson-path> [oim|oim-obs|oim-bio-tdwg|auto]
---

Convert the GeoJSON file or inline GeoJSON in `$ARGUMENTS` to JSON-FG format with OIM (Oceans Information Model) semantic enrichment using the `geojson-to-jsonfg-converter` agent.

Parse `$ARGUMENTS` as: `<file-path-or-inline-geojson> [profile]`

where profile is one of:
- `oim` — general marine spatial data
- `oim-obs` — sensor/observation data with SOSA semantics
- `oim-bio-tdwg` — species/biodiversity data with Darwin Core mappings
- `auto` (default) — agent detects profile from feature properties

The agent will:
1. Validate the input GeoJSON structure
2. Detect or apply the specified OIM profile
3. Add `@context`, `links` (conformsTo OGC building blocks), and `place` references
4. Preserve all original properties unchanged
5. Validate JSON-FG schema compliance
6. Output the converted JSON-FG

## Examples

```
/geojson-to-jsonfg _sources/macroobservation/examples/sample.geojson oim-obs
/geojson-to-jsonfg /path/to/biodiversity.geojson oim-bio-tdwg
/geojson-to-jsonfg observations.geojson auto
```

If `$ARGUMENTS` is empty, ask the user for a GeoJSON file path or inline GeoJSON content.