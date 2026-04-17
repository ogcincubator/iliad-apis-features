# HELCOM Macroobservation Building Block

This building block defines a reusable specification for HELCOM macroobservation point data sampled within the Swedish Economic Exclusion Zone (EEZ) north of Gotland.

## Purpose

Provide a standards-based GeoJSON representation for macrospecies observation records, enriched with provenance metadata, marine observation context, and linked-data vocabulary references.

## Scope

- Geographic focus: Swedish EEZ north of Gotland.
- Data type: macroobservation point records for marine species.
- Formats: GeoJSON, GeoParquet metadata, JSON-LD context, RDF/Turtle sample data.
- Use cases: coastal/marine observation ingestion, interoperable dataset publication, OGC building block reuse.

## Core design

- Each record is a GeoJSON `Feature` with a `Point` geometry.
- Observation properties include species identity, abundance, time, depth, salinity, sampling method, and provenance.
- `provenance_urls` captures executed HELCOM or marine service query URLs used during data retrieval.
- `species_uri` supports vocabulary-based species identification using SKOS or other linked-data concepts.

## Standards referenced

- GeoJSON for feature collection structure.
- SOSA/SSN for observation semantics.
- SKOS for species and concept vocabulary.
- WGS84 CRS84 for geolocation.
- DCAT/DCTERMS for dataset metadata and provenance.

## Outputs

- `schema.json` / `schema.yaml`: schema definitions for GeoJSON observations.
- `context.jsonld`: JSON-LD context to map schema properties to semantic URIs.
- `examples/sample.geojson`: example dataset instance.
- `tests/test.yaml`: validation rules for schema and provenance content.
- `sample_macrospecies_observations.ttl`: RDF sample content.

## Provenance

Provenance should include source service URLs, query parameters, and data provider metadata. For HELCOM-derived data, this includes the backend service endpoint, request parameters, and the originating dataset or catalog reference.
