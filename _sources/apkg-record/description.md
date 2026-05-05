# ILIAD APKG Registry Record

Profile of an OGC API Records record describing one Application Package (APKG) entry in the ILIAD registry hosted at `https://iliad-registry.inesctec.pt/collections/apkg`.

Every register item is returned as a GeoJSON Feature whose `properties` payload follows the APKG Metadata Profile (APKG-MAP) — a flattened metadata view over a CWL `Process` (either a `CommandLineTool` or a `Workflow`) plus its registry-side metadata (identifier family, latest flag, publication record, organisations, spatial / temporal coverage, embedded CWL document).

## Extension model

This is a **Records-extension** building block. It conforms to the OGC API Records record schema as a GeoJSON Feature with `type`, `id`, `geometry`, and `properties`, and adds APKG-specific properties under `properties`. The base record envelope (geometry, type, id) is unchanged; only the `properties` payload is profiled.

The `dependsOn` list declares both:

- [`ogc.hosted.iliad.api.features.apkg`](../apkg/) — the APKG model block, which defines `apkg:ApplicationPackage`, `apkg:Process`, `apkg:Parameter`, `apkg:hasInput`, `apkg:hasOutput`, `apkg:hasGeometry`, `apkg:hasTemporalCoverage`, `apkg:family`, `apkg:latest`, and the upstream `apkg-ms.ttl` term URIs;
- [`ogc.geo.geodcat.dcat-records`](https://ogcincubator.github.io/geodcat-ogcapi-records/bblock/ogc.geo.geodcat.dcat-records/) — the DCAT / Records binding that the registry's catalogue exposes.

## Property mapping

The JSON-LD `context.jsonld` maps every property in the register item payload to an authoritative term, prioritising the local APKG ontology where it has a matching term and falling back to schema.org, Dublin Core, CWL, and DCAT. The full list is enumerated in `context.jsonld`; the most relevant mappings are:

| Register property | Mapping |
|---|---|
| `identifier` | `dct:identifier` (URN, used as primary identifier) |
| `id` | `schema:identifier` (short id within the URN) |
| `family` | `apkg:family` |
| `latest` | `apkg:latest` |
| `class` | `cwl:class` (`CommandLineTool` / `Workflow`) |
| `cwl` | `apkg:cwl` (full CWL document as a string) |
| `name`, `description`, `keywords`, `programming_language`, `software_version` | `schema:name`, `schema:description`, `schema:keywords`, `schema:programmingLanguage`, `schema:softwareVersion` |
| `author`, `contributor`, `maintainer`, `producer` | `schema:author`, `schema:contributor`, `schema:maintainer`, `schema:producer` |
| `source_organization`, `sdPublisher` | `schema:sourceOrganization`, `schema:sdPublisher` |
| `inputs`, `outputs` | `apkg:hasInput`, `apkg:hasOutput` |
| `spatial_coverage`, `temporal_coverage` | `schema:spatialCoverage`, `schema:temporalCoverage` |
| `license`, `code_repository`, `citation` | `schema:license`, `schema:codeRepository`, `schema:citation` |
| `date_created`, `sdDatePublished` | `schema:dateCreated`, `schema:sdDatePublished` |
| `url`, `registration_url` | `schema:url`, `apkg:originalURL` |
| `Secrets` | `cwltool:Secrets` |

Address sub-properties (`*.address.address_country`) are mapped through `schema:address` → `schema:addressCountry`. Spatial bounding-box data follows `schema:GeoShape` with `schema:box`.

## Examples

Three real items drawn from the live registry are bundled under `examples/`:

- `commandlinetool-wo-data-filter.json` — a minimal `CommandLineTool` (CSV filter from MELOA).
- `workflow-oilspill-pipeline.json` — a multi-step `Workflow` (Sentinel-1 oil-spill detection with MEDSLIK forecasting), demonstrating `temporal_coverage`, `license`, and a multi-organisation `source_organization`.
- `commandlinetool-virtual-choreographies.json` — a `CommandLineTool` with non-null `maintainer` and `contributor`, demonstrating the full provenance chain.

Together these three examples exercise every property in the register's collection schema (`https://iliad-registry.inesctec.pt/collections/apkg/schema`).

## Source-property coverage

All 28 properties exposed by the registry's collection schema are mapped in `context.jsonld` and validated by `schema.yaml`. The following properties are sparsely populated in the live data and are therefore optional in the schema but covered semantically in the context:

- `temporal_coverage` (14 / 178 items) — string interval (ISO 8601 / DCAT-style)
- `license` (16 / 178 items) — SPDX or URI
- `maintainer` (15 / 178 items) — array of person/organisation objects
- `Secrets` (29 / 178 items) — CWL `cwltool:Secrets` block, names of secret inputs

No source property is silently dropped.

## References

- [ILIAD APKG repository](https://github.com/ILIAD-ocean-twin/APKG)
- [APKG metadata profile context](https://github.com/ILIAD-ocean-twin/APKG/blob/main/apkg-profile-context.jsonld)
- [Common Workflow Language v1.2 specification](https://www.commonwl.org/v1.2/)
- [OGC API Records — Part 1: Core](https://docs.ogc.org/DRAFTS/20-004.html)
- [GeoDCAT-AP for OGC API Records](https://ogcincubator.github.io/geodcat-ogcapi-records/)
