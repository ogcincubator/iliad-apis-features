---
name: dataset-qa
description: Use when assessing a candidate dataset against the SeaDOTs QualityMeasures framework. Accepts a URL or a free-text/markdown data description, scores the seven framework dimensions (1, 2a, 2b, 2c, 3, 4, 5), derives the six QI scores (lineage, representativeness, temporal, spatial, method, uncertainty), computes U_data and readiness, and emits two artefacts — a STAC-compliant Item JSON and a markdown table. Use for SES impact-assessment input registers, indicator-quality-requirement evidence, and digital-twin dataset acceptance.
---

# Dataset QA Skill — SeaDOTs QualityMeasures

## Purpose

Score one candidate dataset against the SeaDOTs **QualityMeasures** framework and return two interoperable artefacts:

- a **STAC Item JSON** with the `seadots:` and `dqv:` quality fields,
- a **markdown table** matching the per-dataset acceptance template.

The framework is defined in `seadots/data_framework/metadata_generator/quality-measures-framework.md` (process) and `…/quality-measures-evaluation.md` (per-dataset form).

## Activation

Use this skill when the user asks to:

- "QA this dataset" / "score this dataset"
- "check this URL against the SeaDOTs quality framework"
- "generate the quality assessment for `<URL>`"
- "fill the indicator-quality-requirement for `<dataset>`"
- "produce the readiness / `U_data` / `QI_total` for `<dataset>`"

Do **not** use this skill for:

- generating generic STAC or DCAT metadata — use `metadata-extraction` instead.
- building OGC building blocks — use `building-block-generator`.
- discovering datasets — use `marine-data-agent`.

This skill performs **assessment**, not discovery or conversion.

## Required input

One of:

- `source_url` — URL to a dataset, OGC service endpoint, DOI landing page, or catalogue record, or
- `description` — free-text or markdown description (publisher, theme, spatial / temporal extent, format, licence, sampling design).

If neither is supplied, ask exactly:

> Provide a dataset URL or a markdown description (publisher, theme, spatial extent, temporal extent, format, licence).

## Optional input

| Parameter | Default | Meaning |
|---|---|---|
| `aoi` | none | Bounding box `[minX, minY, maxX, maxY]` or polygon GeoJSON / URI of the area of interest. If not supplied, the assessment is "publisher-frame": dimension 2a (Representativeness) cannot be scored for geographic fit and is marked `null`. |
| `indicators` | none | Array of Rainbow IRIs the dataset should support (e.g. `https://id3.seadots.eu/indicator/net-primary-production-rate`). Used for the §3.1 thematic-relevance check. |
| `format_hint` | auto-detect | `netcdf | csv | geojson | cog | ogc-service | jsonfg | …` |
| `weights` | unweighted | Object `{ "lineage": w1, … }` summing to 1. Records weights in the output and uses them to compute `QI_total`. |
| `output` | `both` | `both | stac | table` |
| `reviewer` | none | ORCID of the human reviewer; embedded in the STAC Item. |

## Process

### Phase 1 — Source ingestion

1. **Detect input type.** If `source_url` is given, classify by suffix or content-type (NetCDF, CSV, GeoJSON, COG, OGC service capabilities). If `description` is given, parse the markdown as semi-structured metadata. Both may be supplied together.
2. **Fetch metadata only** (no bulk data download): HTTP HEAD + first MB, `GetCapabilities` for OGC services, OpenAPI for OGC API, DOI landing page, STAC Item if pre-existing.
3. **Run the existing `metadata-extraction` skill** to obtain a base record (title, providers, spatial bbox, temporal extent, variables, vocab hints). Treat its output as input for phase 2.

### Phase 2 — Per-dimension scoring

For each framework dimension, evaluate every operational check from §3 of the framework. Score each check in `[0, 1]`; the dimension score is the unweighted mean unless `weights` supplies dimension-level overrides.

Below is the check-to-score logic. Each item is a pure function of metadata observations.

#### Dimension 1 — Relevance

```
thematic_relevance        = 1.0 if dataset variable matches `indicators[*]` via skos:exactMatch
                            0.7 if matches via skos:closeMatch or CF standard-name
                            0.4 if requires proxy
                            0.0 if no link
proxy_distance            = 1.0 if direct
                            0.7 if documented proxy with weight ≥ 0.7
                            0.4 if documented proxy with weight < 0.7
                            0.0 if undocumented proxy
domain_coverage           = ratio of required taxa/sectors actually covered
comprehensiveness         = 1.0 if dataset has a methodology page + data dictionary
                            0.5 if only description
                            0.0 if no documentation
score_1_relevance         = mean(above)
```

#### Dimension 2a — Representativeness

```
geographic_repr           = bounded(% AOI overlap, lower=0.4 if any overlap, upper=1.0 if AOI ⊂ dataset)
                            0.0 if no AOI was provided → null
local_vs_general          = 1.0 if site-specific
                            0.6 if regional (e.g. North Sea) used with proxy
                            0.3 if global without local clipping
sampled_population        = 1.0 if sample frame declared (Darwin Core samplingEffort, ESS sample frame)
                            0.5 if partial
                            0.0 if missing (for social/economic data)
stratification            = 1.0 if stratified ≥ minimum strata for the indicator
                            0.5 if simple random
                            0.0 if opportunistic
heterogeneity_fusion      = 1.0 if fusion recipe with stable join keys exists
                            0.5 if join keys exist but no recipe
                            0.0 otherwise
temporal_representativeness = 1.0 if sample period ⊇ climatology window
                              0.5 if sample period overlaps climatology partially
                              0.0 if anomalous-year-only
effort_bias               = 1.0 if effort recorded + bias declared
                            0.5 if one of two
                            0.0 if neither
score_2a_representativeness = mean(above, skipping null)
```

#### Dimension 2b — Reliability

```
lineage                   = 1.0 if processing level + tooling + version recorded
                            0.6 if level only
                            0.0 if none
qa_process                = 1.0 if QA programme named (Copernicus QA / EMODnet QC / OceanSITES / IODE / publisher SoP)
                            0.5 if QC flags but no programme
                            0.0 if none
authority                 = 1.0 if publisher ∈ trusted-registry (Copernicus, ECMWF, ICES, NOAA, IMR/HI, MAREANO, NVE, EMODnet, OBIS, GBIF, SSB, ESA, EEA, OGC, …)
                            0.5 if recognised academic / NGO
                            0.0 unknown
positional_accuracy       = compare RMSE / CE90 to required minimumSpatialResolution
                            1.0 if RMSE ≤ resolution / 4
                            0.5 if RMSE ≤ resolution
                            0.0 if RMSE > resolution
temporal_accuracy         = 1.0 if time zone, clock-sync handling explicit
                            0.5 if timestamps present without zone
                            0.0 missing
sampling_design           = 1.0 transect/random/stratified declared
                            0.5 opportunistic
                            0.0 unknown
uncertainty               = 1.0 per-pixel/sample uncertainty layer
                            0.5 scalar uncertainty
                            0.0 none
score_2b_reliability      = mean(above)
```

#### Dimension 2c — Temporal validity

```
temporal_extent           = 1.0 if dataset extent ⊇ scenario period
                            0.5 if overlaps scenario partially
                            0.0 disjoint
temporal_resolution       = 1.0 if cadence ≤ required cadence
                            0.5 if cadence ≤ 2× required
                            0.0 otherwise
currency                  = 1.0 if dct:modified within 1× cadence
                            0.5 if within 3× cadence
                            0.0 otherwise
update_frequency          = 1.0 if SLA published / NRT
                            0.5 monthly / quarterly
                            0.0 one-off / no SLA
historical_baseline       = 1.0 if BACI baseline available
                            0.5 if reference period only
                            0.0 missing
seasonal_coverage         = % of required seasons covered
score_2c_temporal_validity = mean(above)
```

#### Dimension 3 — Ingestibility (hard gate)

```
format_compliance         = 1.0 if format aligns with an ILIAD building-block format
                            0.5 if convertible
                            0.0 otherwise → blocked
access_protocol           = 1.0 OGC API / open S3 / DOI
                            0.5 authenticated standard
                            0.0 proprietary / FTP-only → conditional
licence                   = 1.0 CC-BY / CC0 / public-domain / Copernicus-open
                            0.5 conditional reuse
                            0.0 forbidden → blocked
gdpr                      = 1.0 anonymised + DPIA / n/a
                            0.5 aggregated only
                            0.0 unmitigated personal data → blocked
ethical_clearance         = 1.0 IRB/REK number / n/a
                            0.5 process described
                            0.0 none for surveys → blocked
size                      = 1.0 within budget + chunked
                            0.5 within budget
                            0.0 above budget → conditional
preprocessing_burden      = 1.0 ingestible raw
                            0.5 ≤ 3 transforms
                            0.0 > 3 transforms → conditional
score_3_ingestibility     = mean(above) ;   if any of {format, licence, gdpr} == 0 → readiness = blocked
```

#### Dimension 4 — Reusability in DT

```
findable                  = 1.0 DOI + catalogue + w3id
                            0.5 DOI only
                            0.0 nothing persistent
accessible                = 1.0 standardised protocol with documented auth
                            0.5 ad-hoc URL
                            0.0 hand-shared
interoperable             = 1.0 standard vocab (NERC/CF/DwC/QUDT) + standard model
                            0.5 standard model only
                            0.0 bespoke
reusable                  = 1.0 licence + provenance + community standard
                            0.5 licence only
                            0.0 missing
scenario_compat           = 1.0 parameterisable
                            0.5 partially parameterisable
                            0.0 read-only
iso_19127                 = 1.0 / 0.0
ogc_bb_conformance        = 1.0 / 0.0
score_4_reusability       = mean(above)
```

#### Dimension 5 — Logical Consistency (hard gate)

```
logical_consistency       = 1.0 SHACL / JSON-Schema pass
                            0.5 minor warnings
                            0.0 errors → blocked
completeness              = % required attributes present
model_existence           = 1.0 published schema (XSD / JSON-Schema / RDF / SHACL)
                            0.5 informal schema
                            0.0 none
semantics                 = 1.0 every property mapped to NERC/CF/DwC/QUDT
                            0.5 some mapped
                            0.0 none
technical_interoperability = 1.0 conforms to CF/OGC API/STAC/DCAT-AP profile
                             0.5 partial
                             0.0 bespoke
qa_beyond_science         = 1.0 QA badge
                            0.5 internal SoP
                            0.0 none
score_5_logical_consistency = mean(above) ; if logical_consistency == 0 → readiness = blocked
```

### Phase 3 — Aggregation

```
QI_lineage            = score_2b_reliability projection on lineage + qa_process + authority
QI_representativeness = score_2a_representativeness
QI_temporal           = mean(score_2c_temporal_validity, temporal_accuracy from §2b)
QI_spatial            = mean(positional_accuracy from §2b, geographic_repr from §2a)
QI_method             = mean(sampling_design from §2b, completeness/semantics from §5, FAIR-interoperable from §4)
QI_uncertainty        = uncertainty from §2b

QI_total = weighted_mean(QI_*) if weights else unweighted mean
U_data   = 1 − QI_total
```

Readiness:

```
if ingestibility_hard_gate == blocked OR logical_consistency_hard_gate == blocked → blocked
elif QI_total ≥ 0.80 AND every QI_* ≥ 0.60 → pass
elif 0.50 ≤ QI_total < 0.80 OR any QI_* in [0.30, 0.60) → conditional
elif input_planned_but_not_available → planned
elif QI_total < 0.50 OR required_geometry_or_method_absent → blocked
```

### Phase 4 — Emission

Produce two artefacts.

#### 4a. STAC Item

Follow the schema in §2.3 of `quality-measures-evaluation.md`. Required STAC extensions: `scientific`, `version`, `processing`. Custom namespace `seadots:` carries the framework fields; `dqv:hasQualityMeasurement` is emitted **once per supported indicator** with `dqv:value = QI_total` plus one explanation in `rdfs:comment`.

#### 4b. Markdown table

Follow §1 of `quality-measures-evaluation.md`. Include every field; mark unknown fields as `unknown` (not blank) and explain in the adjacent `Notes` column.

Optionally produce a third artefact, the **per-check breakdown**, as a Markdown table with one row per check from §3.1–§3.7 of the framework.

## Output formats

| Option | Returns |
|---|---|
| `output = stac` | STAC Item JSON only. |
| `output = table` | Markdown table only. |
| `output = both` (default) | STAC Item JSON + markdown table + per-check breakdown, written to `assessments/<id>.json`, `assessments/<id>.md`, `assessments/<id>-checks.md`. The STAC Item's `assets` reference the markdown files. |

## File-system conventions

```
<project-root>/assessments/
  <dataset-slug>--<aoi-slug>--<review-date>.json       # STAC Item
  <dataset-slug>--<aoi-slug>--<review-date>.md         # tabular report
  <dataset-slug>--<aoi-slug>--<review-date>-checks.md  # per-check breakdown
```

Slug rules: lowercase, `[a-z0-9-]+`, no slashes; AOI slug is the project polygon's short name.

## STAC field reference

| STAC field | Source |
|---|---|
| `id` | `<dataset-slug>--<aoi-slug>--<review-date>` |
| `geometry`, `bbox` | AOI polygon (not the dataset's footprint) |
| `properties.datetime` | review date (ISO 8601) |
| `properties.start_datetime`, `properties.end_datetime` | dataset temporal extent |
| `properties.title`, `description` | reviewer-supplied or auto-generated |
| `properties.license` | dataset SPDX licence |
| `properties.providers` | dataset publisher + reviewer org |
| `properties.sci:doi` | dataset DOI |
| `properties.version` | framework version |
| `properties.processing:software` | `{ "seadots-quality-measures": "1.0", "dataset-qa-skill": "0.1" }` |
| `properties.seadots:supports_indicators` | from input `indicators` |
| `properties.seadots:aoi_polygon` | URI of AOI |
| `properties.seadots:dimensions` | seven dimensions, each `{ score, notes, mitigation_input, mitigation_output }` |
| `properties.seadots:qi` | six QI scores |
| `properties.seadots:qi_total`, `seadots:u_data`, `seadots:readiness` | aggregates |
| `properties.seadots:reviewer`, `seadots:review_date` | provenance |
| `properties.dqv:hasQualityMeasurement[]` | one entry per supported indicator |
| `assets.data` | URL of source dataset |
| `assets.tabular_report`, `assets.check_breakdown` | markdown sidecars |
| `assets.framework_reference` | link to `quality-measures-framework.md` |
| `links` | `self`, `describedby` (framework), `via` (evaluation), `derived_from` (dataset DOI) |

## Validation

After emission:

- Validate the STAC Item against the core STAC v1.0.0 schema and against each declared extension.
- Confirm every `seadots:dimensions.*.score` is in `[0, 1]` or `null`.
- Confirm `seadots:u_data = 1 − seadots:qi_total` to within `1e-6`.
- Confirm `seadots:readiness` matches the rule in Phase 3.
- Confirm each `assets.*.href` resolves (HEAD request) when paths are absolute.

If any validation fails, surface the violation to the user and do not write the file; offer to re-score the failing dimension or to relax the gate manually.

## Interactions with other skills

- `metadata-extraction` — called in phase 1 to extract base metadata.
- `ogc-web-services-client` — for OGC service endpoints (WMS, WFS, OGC API).
- `esri-client` — for ArcGIS FeatureServer / MapServer / ImageServer.
- `web-browsing-mcp` — for HTML landing pages, DOI redirection, vocabulary look-up.
- `bblock-container-validation` — optional, to check that the dataset's declared building-block conformance is real.

## Edge cases

| Situation | Handling |
|---|---|
| AOI not supplied | Skip 2a geographic component; mark `score_2a_representativeness.notes = "AOI not supplied; geographic component skipped"`. |
| No indicator URIs supplied | Score 1 (Relevance) thematic_relevance against the data variables' CF/NERC names only; flag `notes = "no Rainbow indicators supplied; thematic relevance scored against vocabulary alignment only"`. |
| Dataset behind paywall | Hard-gate `score_3_ingestibility.access_protocol = 0` if no documented free / authenticated access; else proceed. |
| Multiple datasets at one URL (catalogue) | Refuse and ask the user to pick one dataset id. |
| Existing STAC Item at the URL | Treat as one of the *inputs* — copy its provider/temporal/spatial fields, then perform the assessment on top. |
| Personal / clinical / interview data | Hard-gate dimension 3 (GDPR) to `0` unless DPIA URL is supplied. |

## Worked example call

```text
/dataset-qa
  source_url: https://doi.org/10.48670/moi-00280
  aoi: [4.40, 59.20, 5.10, 59.55]
  indicators: ["https://id3.seadots.eu/indicator/net-primary-production-rate"]
  reviewer: https://orcid.org/0000-0000-0000-0000
```

Produces:

- `assessments/copernicus-marine-npp-l4--utsira-nord--2026-05-11.json` (STAC Item)
- `assessments/copernicus-marine-npp-l4--utsira-nord--2026-05-11.md`   (tabular report)
- `assessments/copernicus-marine-npp-l4--utsira-nord--2026-05-11-checks.md` (per-check breakdown)

The full content of these three files matches §3 of `quality-measures-evaluation.md`.

## References

- Generic process — `seadots/data_framework/metadata_generator/quality-measures-framework.md`
- Per-dataset form — `seadots/data_framework/metadata_generator/quality-measures-evaluation.md`
- STAC spec — https://stacspec.org/
- STAC extensions — https://stac-extensions.github.io/
- W3C DQV — https://www.w3.org/TR/vocab-dqv/
- Interoperability framework — `seadots/data_framework/models/demo_ses/norwegian_ses/windpark-biomass-impact/interoperability-framework-manual.md`
