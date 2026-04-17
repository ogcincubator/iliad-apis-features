# HELCOM Macroobservation Building Block

This building block defines a standard representation for HELCOM macrospecies observation data sampled within the Swedish economic zone north of Gotland.

## Overview
- **Purpose:** Provide an interoperable structure for HELCOM macroobservation point data.
- **Spatial scope:** Swedish EEZ approximately 100 km north of Gotland.
- **Formats:** GeoJSON, GeoParquet metadata, RDF/Turtle.
- **Provenance:** Records include source URLs and query parameters from HELCOM data services.

## Contents
- `bblock.json` — building block metadata.
- `description.md` — human-readable specification of the building block.
- `schema.json` — JSON Schema for GeoJSON.
- `schema.yaml` — YAML equivalent.
- `metadata.json` — GeoParquet metadata.
- `context.jsonld` — JSON-LD context for linked data.
- `examples.yaml` — example manifest.
- `examples/sample.geojson` — example feature collection.
- `tests/test.yaml` — validation tests.
- `sample_macrospecies_observations.ttl` — RDF sample data.

## Standards
- SOSA/SSN for observation modeling
- SKOS for species vocabulary
- WGS84 for geolocation
- DCAT/DCTERMS for dataset metadata
- OGC API / GeoJSON for vector data

## Spatial extent
- Swedish EEZ north of Gotland
- Approximate bounding box: `lon 17.8–18.8`, `lat 58.4–59.0`
- Use EEZ polygon clipping where available for precise filtering

## Provenance
Sources should include executed HELCOM service URLs and API query parameters, stored in `provenance_urls` for each feature and in dataset metadata.