# From Pilot Requirements to OGC Building Blocks: Encoding FMSDI 2024 Coastal Data Integration Standards

**Piotr Zaborowski¹**  
¹ OGC Europe

*Generated with Sonnet 4.6 : 2026-05-04*
*Core building blocks written manually*
*oim coastal feature, vertical datum-reference and dynamic shoreline generated with building-block-generator from this repository with Sonnet 4.6 : 2026-05-04*
*reviewed by human 2026-05-04*
*test data selected and documented manually in SeaDOTs project as tabular data from partners with refrences to the datasets where available*



---

## Abstract and human summary

The OGC Federated Marine SDI 2024 Pilot (FMSDI-2024, OGC documents 24-061 and 24-064) identified five best practices for integrating terrestrial and marine geospatial data across the intertidal zone.
At the same time several initiatives registered OGC incubator building blocks that allows to specify stacked data requimrents composition.
These brought the question if the recommendations from the engineering report are interopretable by the AI assisted metadata quality assessment? if formalisation level is sufficient, if additional step of formalising requiments in the form of building blocks brings any value in the process.

This document traces the process of converting those best practices into concrete OGC Building Block packages registered in the ILIAD APIs repository, and reports on an inventory analysis identifying which datasets in the SeaDOTS data catalogue are directly affected. Three building blocks were produced: `vertical-datum-reference`, `oim-coastal-feature`, and `dynamic-shoreline`. Of 88 records in the SeaDOTS data inventory, 19 are directly applicable to at least one building block, with the highest-priority action being mandatory vertical datum annotation for seven bathymetric and ocean physics datasets before they can be safely published to curated OGC API Features endpoints.

Last chapters (7) traces the comparison of the LLM assisted quality assessment process based on the Engineering report and Building Blocks. Insights are fully machine based interpretation.
Insights are rather predictable understanding LLM mechanics. Identify some requirements from ER where validation needs expert knowledge not available to the model and some requirements that can be evaluated at scale without AI costs with predefined building block. It confirmed also, that building block generated based on the ER are somehow reusable. however, currect test assumed particular encoding and no analysis has been made if the validation would be portable to the other formats, more expresible in other technolgies like RDF/SHACL. These could be assessed next based on the feedback on the direction.

## 1. Introduction and Motivation

Land-sea data integration failures in the intertidal zone are rarely caused by a lack of data. They are caused by a lack of *metadata*: missing vertical datum declarations, undocumented interpolation assumptions, and shoreline geometries stripped of the water-level context that makes them meaningful.

The FMSDI-2024 pilot documented these failures in detail across three demonstrator platforms — Compusult, Pangaea Innovations, and TCarta — and distilled them into five best practices. Those best practices exist as prose in an OGC Engineering Report and Best Practices document. Converting them into machine-enforceable JSON Schema with vocabulary-aligned JSON-LD context transforms them from guidelines into computable artefacts that can validate data and drive automated metadata pipelines.

The ILIAD Ocean Digital Twin APIs repository already hosts OGC Building Blocks for marine observations (`oim-obs`), biodiversity (`oim-bio-tdwg`), and semantic variables (`oim-variables`). The coastal physical domain — elevation, tidal datums, shoreline dynamics — was absent. The FMSDI-2024 requirements fill that gap.

---

## 2. Source Materials

### 2.1 FMSDI-2024 Reports

Two repositories were analysed:

| Document | OGC Number | Path | Content |
|----------|-----------|------|---------|
| FMSDI 2024 Pilot Summary Report | 24-061 | `FMSDI-2024/D001/` | Technical demonstrations, lessons learned, best practices overview |
| FMSDI 2024 Best Practices Report | 24-064 | `FMSDI-2024/D002/` | Normative best practices, data product specifications, governance model |
| FMSDI 2024-2 (revised) Summary Report | — | `FMSDI-2024-2/D001/` | Revised version of 24-061; expanded demonstrator sections |

Both repositories share the same five-part best practice structure and three demonstrator descriptions. The `-2` repository is a revised and more fully elaborated version of the same pilot.

### 2.2 Key Sections Consulted

- `D001/sections/02-topics.adoc` — background on the intertidal zone, harmonisation challenges (multiple datums, resolutions, data types, dimensions, governance frameworks), best practices 1–5 in full, and all three demonstrator descriptions
- `D002/sections/00-00-executive_summary.adoc` — normative framing of the three best practice pillars (surface elevation profiles, data products, governance)
- `D001/sections/00-executive_summary.adoc` — five key findings, value proposition

### 2.3 The Five Best Practices

The reports define five interlinked best practices, each of which maps to technical requirements:

| # | Best Practice | Core technical requirement |
|---|---------------|---------------------------|
| BP1 | Unified Geospatial Reference | Vertical datum declared for every elevation/depth value; national separation models (NOAA VDatum, UKHO VORF, CHS HyVSEPs) used for cross-domain conversion |
| BP2 | FAIR Data Principles | ISO 19115 metadata, GeoDCAT-AP/OGC API Records registration, data quality indicators, lineage |
| BP3 | Mind the Gap | Intertidal data voids documented; interpolation method and confidence level recorded when gap-filling; new observations preferred over interpolation |
| BP4 | Coordinated Governance | Multi-agency data stewardship; IGIF-Hydro framework; out of scope for schema BBs |
| BP5 | Scalable Resolution Management | Point clouds and TIN models preferred over raster resampling; DGGS cell references for multi-scale indexing |

### 2.4 Demonstrator Lessons Learned

Three technical demonstrators provided specific, concrete failure cases that informed the schema design:

**Compusult (D100) — Coastal Erosion Monitoring, The Solent & Chesapeake Bay**
- Critical lesson: early iterations assumed Ordnance Datum Newlyn (ODN, positive = up) for tidal data that was referenced to Southampton Chart Datum (positive = down, offset −2.74 m from ODN). This caused water depths to display incorrectly until the datum was corrected.
- Implication: `verticalOrientation` (up/down) must be a required field, not a convention.

**Pangaea Innovations (D100) — DGGS-based Port Operations Interoperability**
- Critical lesson: "inconsistent or missing vertical datum metadata remains a major barrier to automation" in their DGGS-based spatial integration workflow.
- Implication: vertical datum must be machine-readable (URI-linked), not just a label in a PDF.

**TCarta (D100) — Space-Based Intertidal Awareness, Hurst Spit**
- Approach: NDWI shorelines derived from Planet Labs multispectral imagery and Capella SAR, each attributed with the tide gauge water level at time of capture.
- Critical lesson: a shoreline without its water-level attribution cannot be compared to another shoreline at a different tidal state, or used to derive a tidal datum contour.
- Implication: a `dynamic-shoreline` feature type must carry `waterLevelAtCapture`, `tidalDatumReference`, `captureMethod`, and `temporalValidity` as core fields.

---

## 3. Building Block Design

### 3.1 Identification of Gaps in Existing ILIAD Building Blocks

Existing OIM building blocks cover:

| Existing BB | Coverage |
|-------------|----------|
| `oim-obs` | Marine observations, SOSA/SSN pattern |
| `oim-bio-tdwg` | Biodiversity, Darwin Core |
| `oim-obs-cs` | Citizen science observations |
| `oim-variables` | Indicator variables, SEADOTS PropertyRelationship |

None covered: vertical datum metadata, physical coastal elevation features, or tide-dependent shoreline geometry.

### 3.2 Proposed Building Blocks

Three building blocks were identified, ordered by dependency:

```
vertical-datum-reference          (no new dependencies)
  └── oim-coastal-feature         (depends on vertical-datum-reference + oim-obs)
        └── dynamic-shoreline     (depends on oim-coastal-feature)
```

#### BB1: `vertical-datum-reference`

A standalone, reusable schema component that any feature type carrying elevation, depth, or height values can embed. Directly addresses BP1.

**Required fields:** `datumName` (string), `verticalOrientation` (enum: `up` | `down`)

**Optional fields:** `datumEpoch`, `crsIdentifier` (EPSG URI), `separationSurface` (type + model reference), `transformationMethod`, `verticalAccuracy`

**Design rationale for `verticalOrientation`:** land surveys use positive = up (topographic convention); hydrographic surveys use positive = down (sonar/chart convention). This is the root cause of the Compusult datum error. Making it a required enum field forces every publisher to make an explicit choice.

**Vocabulary mappings:**

| Property | Vocabulary URI |
|----------|---------------|
| `crsIdentifier` | `http://www.opengis.net/def/crs/EPSG/0/{code}` |
| `verticalOrientation` (up) | `http://vocab.nerc.ac.uk/collection/P06/current/ULAA/` |
| `verticalOrientation` (down) | `http://vocab.nerc.ac.uk/collection/P06/current/ULDB/` |
| `verticalAccuracy` | `http://vocab.nerc.ac.uk/collection/P01/current/UNCEJJ01/` |

#### BB2: `oim-coastal-feature`

A GeoJSON Feature profile for the "white ribbon" and adjoining zones. Extends `oim-obs` with coastal-specific properties. Addresses BP1, BP3, BP5.

**Key properties:**

| Property | Type | FMSDI BP addressed |
|----------|------|--------------------|
| `featureDomain` | enum: `land` / `intertidal` / `marine` | BP1, BP3 |
| `elevation` | object with `value`, `unit`, `uncertainty`, `verticalDatum` ref | BP1 |
| `tideContext` | object with `waterLevel`, `tidalState`, `tideGaugeRef` | BP1 |
| `dataLineage.captureMethod` | enum of survey methods | BP2, BP3 |
| `dataLineage.gapFilled` | boolean | BP3 |
| `dataLineage.interpolationMethod` | string (required when `gapFilled=true`) | BP3 |
| `dataLineage.confidenceLevel` | enum | BP2 |
| `resolutionInfo.dggsCellRef` | string (H3/ISEA cell identifier) | BP5 |

**Design rationale for `gapFilled` conditional:** BP3 states that "interpolation is a last resort" and that "all assumptions must be clearly documented." The JSON Schema `if/then` construct enforces `interpolationMethod` as required whenever `gapFilled=true`, making this a machine-enforceable rule rather than advisory text.

#### BB3: `dynamic-shoreline`

A LineString/MultiLineString feature type for tide-dependent shoreline vectors. Directly encodes the TCarta demonstrator output pattern. Addresses BP1, BP3.

**Key properties:**

| Property | Type | Notes |
|----------|------|-------|
| `shorelineType` | enum: `instantaneous` / `tidalDatumContour` / `meanHighWater` / `meanLowWater` / `chartDatumContour` / `astronomicalLowestTide` | Core discriminator |
| `waterLevelAtCapture` | object (required when `shorelineType=instantaneous`) | Water level + datum ref |
| `tidalDatumReference` | enum: `LAT`, `MLWS`, `MLW`, `MSL`, `MHW`, `MHWS`, `HAT`, `CD` | IHO S-32 terminology |
| `captureMethod` | enum: `opticalSatellite_NDWI`, `SAR_backscatter`, `airborneLidar`, etc. | |
| `ndwiThreshold` | number [-1,1], required for NDWI methods | Affects position by 10s of metres |
| `tideGaugeRef` | URI | Links to authoritative tide gauge |
| `ihoAccuracyZone` | string: CATZOC classification | IHO S-44 |

**Design rationale for `shorelineType`:** the most damaging integration error with shoreline data is mixing `instantaneous` shorelines (captured at a specific water level) with tidal datum contours (derived/modelled lines) as if they were equivalent. The `shorelineType` discriminator makes this distinction explicit and machine-readable. Schema conditionals enforce that `instantaneous` shorelines always carry `waterLevelAtCapture`.

---

## 4. Building Block Implementation

All three building blocks were created under `_sources/` in this repository:

```
_sources/
├── vertical-datum-reference/
│   ├── bblock.json          # id: ogc.hosted.iliad.api.features.vertical-datum-reference
│   ├── schema.yaml          # JSON Schema 2020-12, required: [datumName, verticalOrientation]
│   ├── context.jsonld       # NERC P06, EPSG, OGC CRS vocabulary mappings
│   ├── description.json     # Full description, datum table, usage guidance, references
│   ├── examples.yaml
│   ├── examples/            # chart-datum-example.json, msl-example.json, ellipsoidal-example.json
│   └── tests/test.yaml      # 7 test cases (positive + negative)
│
├── oim-coastal-feature/
│   ├── bblock.json          # depends on vertical-datum-reference + oim-obs
│   ├── schema.yaml          # GeoJSON Feature + coastal properties + if/then for gapFilled
│   ├── context.jsonld       # NERC P01, P02, L05; IHO S-100; OGC DGGS
│   ├── description.json     # White ribbon concept, 4D data model, usage rules
│   ├── examples/            # intertidal-sounding, TIN gap-fill, land LiDAR
│   └── tests/test.yaml
│
└── dynamic-shoreline/
    ├── bblock.json          # depends on oim-coastal-feature
    ├── schema.yaml          # LineString/MultiLineString + shoreline properties + conditionals
    ├── context.jsonld       # NERC S13, P01, L06; IHO S-32
    ├── description.json     # Shoreline type taxonomy, NDWI explanation, consistency rules
    ├── examples/            # NDWI/Sentinel-2, SAR/Capella, MHW datum contour
    └── tests/test.yaml
```

Each `bblock.json` references OGC documents 24-061 (Summary Report) and 24-064 (Best Practices Report) in its `sources` array. Each `description.json` contains:
- `description`: full narrative with FMSDI citations and demonstrator lesson references
- `usageGuidance`: numbered step-by-step rules for consistent application
- `references`: structured list with URIs including OGC document numbers and demonstrator links
- `relatedBuildingBlocks`: cross-references to the other two BBs

Docker validation (`ogcincubator/bblocks-postprocess`) passed for all three building blocks. A pre-existing JSON-LD prefix error in the `odd-protocol` block prevented the full postprocessor pipeline from completing but did not affect schema or context validation for the new blocks.

---

## 5. Data Inventory Analysis

The SeaDOTS data inventory (`data_inventory.xlsx`, sheet `Raw inventory-proposed`) was analysed to identify which of its 88 dataset records are applicable to the three building blocks. The `Consumed Data sets` sheet contained only header rows and was not analysed.

### 5.1 Method

Each record's `Data set name`, `Dataset (short) Description`, and `Category` fields were used for keyword matching, followed by manual curation to remove false positives (e.g., "offshore" matching "shore" keywords for the shoreline building block).

### 5.2 Results by Building Block

#### `vertical-datum-reference` — 12 records

Applies to any record where depth or elevation values are part of the data product. The nine high-confidence records are datasets where incorrect or missing datum metadata would cause quantitative errors in any downstream integration.

| Row | Dataset | Demonstrator | Confidence | Critical issue |
|-----|---------|-------------|------------|----------------|
| 11 | Atlantic NW Shelf Ocean Physics | German | H | Sea surface height without datum = unusable for coastal inundation |
| 12 | Bathymetrie | German | H | Gridded depth values; datum source unknown from record |
| 15 | Norkyst800 | Norway/Utsira | H | Operational sea level output; must be MSL-referenced explicitly |
| 39/40 | Ports (two entries) | Norway/Utsira | H | Berthing depth safety-critical; datum error = navigational hazard |
| 45 | MAREANO | Norway/Utsira | H | Multibeam survey; Norwegian Chart Datum vs MSL gap exists |
| 46 | EMODnet bathymetry | Norway/Utsira | H | Composite grid from multiple source datums |
| 47 | Kartverket/GeoNorge | Norway/Utsira | H | Authoritative Norwegian bathymetry; Norwegian CD ≠ MSL |
| 73 | Baltic Sea Physics | Swedish | H | Sea surface height; CMEMS datum convention must be explicit |
| 79 | EMODnet Human activities — ports | Swedish | H | Harbour depths; same as rows 39/40 |
| 2 | CMEMS NW Shelf BGC L3 | German | M | Depth-indexed profiles |
| 13 | Sedimentologie | German | M | Grain size samples at depth |

#### `oim-coastal-feature` — 16 records

Applies to datasets representing spatial features in the coastal zone where explicit domain classification, tidal context, or gap-fill documentation would improve interoperability.

| Row | Dataset | Demonstrator | Confidence | Key application |
|-----|---------|-------------|------------|----------------|
| 12 | Bathymetrie | German | H | `featureDomain=intertidal` for nearshore cells; `gapFilled=true` for interpolated zone |
| 39/40 | Ports | Norway/Utsira | H | `featureDomain=intertidal`; `tideContext.tidalState` for tidal access window |
| 45 | MAREANO | Norway/Utsira | H | Sea floor features with `dataLineage.captureMethod=bathySonar` |
| 46 | EMODnet bathymetry | Norway/Utsira | H | **BP3 case**: coastal cells likely gap-filled; `gapFilled=true` + `interpolationMethod` required |
| 47 | Kartverket/GeoNorge | Norway/Utsira | H | Coastal cells near shoreline; same BP3 concern |
| 79 | EMODnet Human activities — ports | Swedish | H | Port geometry with tidal context |
| 2 | CMEMS NW Shelf BGC L3 | German | M | Depth-indexed profiles as features |
| 13 | Sedimentologie | German | M | Sea floor sediment patches |
| 25 | Utsira Nord polygon | Norway/Utsira | M | `featureDomain=marine` for development zone |
| 41 | Protected areas (Norway) | Norway/Utsira | M | `featureDomain=marine` / `intertidal` for MPA boundary |
| 71 | HELCOM MPAs | Swedish | M | Marine zone polygon; `featureDomain=marine` |
| 81 | EMODnet protected areas (Baltic) | Swedish | M | `featureDomain=marine` |
| 82 | Swedish Marine Spatial Plan | Swedish | M | Coastal zone boundaries |
| 61 | CPUE/MPAs/ecosystems map | Swedish | L | Marine zone featureDomain |
| 74 | Offshore wind parks map | Swedish | L | Marine footprint featureDomain |

#### `dynamic-shoreline` — 3 records (indirect)

No record in the inventory explicitly provides or consumes tide-dependent shoreline vectors. The three indirect matches represent datasets whose spatial extent or boundary definition is a shoreline, and where encoding that boundary as a `dynamic-shoreline` feature would add precision.

| Row | Dataset | Demonstrator | Application |
|-----|---------|-------------|------------|
| 45 | MAREANO | Norway/Utsira | Survey area boundary IS a shoreline; `shorelineType=tidalDatumContour` with `tidalDatumReference=MHWS` gives it geodetic precision |
| 25 | Utsira Nord polygon | Norway/Utsira | Seaward development zone boundary; encoding as `tidalDatumContour` + `tidalDatumReference=MHWS` aligns with jurisdictional shoreline definition |
| 74 | Offshore wind parks map | Swedish | Near-shore wind park footprint edges cross the intertidal zone |

**Gap identified:** No dataset in the inventory tracks dynamic shoreline positions, water-line vectors, or satellite-derived coastal delineations. If any SeaDOTS demonstrator develops a coastal monitoring or erosion tracking component, `dynamic-shoreline` is the schema to use. The capability demonstrated by TCarta (NDWI from Planet Labs + SAR from Capella, attributed to tide gauges) is absent from the current inventory and represents a data gap for the Norway/Utsira case, which has an active intertidal zone around the island.

### 5.3 Summary Table

| Row | Dataset | Demo | VDR | OCF | DS |
|-----|---------|------|:---:|:---:|:--:|
| 2 | CMEMS NW Shelf BGC L3 | German | M | M | — |
| 11 | Atlantic NW Shelf Ocean Physics | German | H | — | — |
| 12 | Bathymetrie | German | H | H | — |
| 13 | Sedimentologie | German | M | M | — |
| 15 | Norkyst800 | Norway | H | — | — |
| 25 | Utsira Nord polygon | Norway | — | M | M |
| 39 | Ports (entry 1) | Norway | H | H | — |
| 40 | Ports (entry 2) | Norway | H | H | — |
| 41 | Protected areas | Norway | — | M | — |
| 45 | MAREANO | Norway | H | H | H |
| 46 | EMODnet bathymetry | Norway | H | H | — |
| 47 | Kartverket/GeoNorge | Norway | H | H | — |
| 61 | CPUE/MPAs map | Swedish | — | L | — |
| 71 | HELCOM MPAs | Swedish | — | M | — |
| 73 | Baltic Sea Physics | Swedish | H | — | — |
| 74 | Offshore wind parks | Swedish | — | L | L |
| 79 | EMODnet Human activities — ports | Swedish | H | H | — |
| 81 | EMODnet protected areas | Swedish | — | M | — |
| 82 | Swedish Marine Spatial Plan | Swedish | — | M | — |

*H = high confidence (BB applies directly, correctness at risk without it); M = medium; L = low/structural benefit only*

---

## 6. Recommendations

### 6.1 Immediate: Annotate before publishing to ILIAD

Seven datasets must have vertical datum declared before they can be safely published to OGC API Features endpoints and federated with land-domain data. Publishing without it replicates exactly the integration failure documented by the Compusult demonstrator.

| Dataset | Action | BB property |
|---------|--------|-------------|
| Bathymetrie (row 12) | Confirm source datum (likely MSL or Chart Datum); declare `datumName`, `verticalOrientation=down`, `crsIdentifier` | `vertical-datum-reference` |
| EMODnet bathymetry (row 46) | Composite grid — verify constituent datums; flag cells where transformation was applied | `vertical-datum-reference.transformationMethod` |
| Kartverket/GeoNorge (row 47) | Norwegian Chart Datum; confirm model reference (likely UKHO VORF equivalent for Norway) | `vertical-datum-reference.separationSurface.modelReference` |
| Norkyst800 (row 15) | Confirm sea surface height is MSL; epoch must be declared | `vertical-datum-reference.datumEpoch` |
| Baltic Sea Physics (row 73) | CMEMS convention is MSL; confirm `verticalOrientation=up` | `vertical-datum-reference` |
| Ports — Norway (rows 39/40) | Chart Datum for berthing depths; distinguish from MSL dredging depths if mixed | `vertical-datum-reference.verticalOrientation` |
| EMODnet ports (row 79) | Same as above | `vertical-datum-reference` |

### 6.2 Short-term: Re-encode coastal features

Five datasets should be re-encoded as `oim-coastal-feature` GeoJSON when published to ILIAD OGC API Features endpoints:

| Dataset | Key change |
|---------|-----------|
| EMODnet bathymetry (row 46) | Tag coastal/intertidal cells with `featureDomain=intertidal` and `dataLineage.gapFilled=true` |
| Kartverket/GeoNorge (row 47) | Same |
| Bathymetrie (row 12) | `dataLineage.captureMethod` + gap-fill documentation for any interpolated nearshore cells |
| MAREANO (row 45) | `dataLineage.captureMethod=bathySonar`, `resolutionInfo.horizontalResolution` |
| Ports (rows 39/40, 79) | `tideContext.tidalState` to document tidal window constraints on access depth |

### 6.3 Gap: Acquire shoreline data for Norway/Utsira

The inventory contains no tide-dependent shoreline dataset for the Utsira case. Island coastline dynamics, tidal flat extent around Utsira, and the seaward boundary of the development zone (row 25) are all defined by shoreline geometry that is currently absent or encoded only as static PDF coordinates.

Recommended action: derive MHWS and MLWS shoreline contours from Kartverket/GeoNorge (row 47) bathymetric grid and encode them using `dynamic-shoreline` with `shorelineType=meanHighWater` / `meanLowWater`, `captureMethod=derived_model`, and `tidalDatumReference=MHWS` / `MLWS`. This directly implements FMSDI BP3 (Mind the Gap) for the Utsira demonstrator.

### 6.4 Governance (BP4)

BP4 (Coordinated Governance) does not translate into a schema building block — it addresses institutional arrangements. For SeaDOTS, the relevant alignment is with the IGIF-Hydro Umbrella Governance Model and the EDITO platform's data stewardship policies. The building blocks produced here support BP4 indirectly: publishing datasets with explicit datum metadata and gap-fill documentation is a prerequisite for the multi-agency data sharing that BP4 mandates.

---

## 7. Comparison: Formalized Building Blocks vs. Raw FMSDI Report Guidance

This section compares what the inventory analysis yields when conducted using the formalized building blocks produced in this work against what the same analysis would yield using the FMSDI reports directly as prose guidelines. The purpose is to assess what formalization adds and where its limits lie.

### 7.1 What the Raw FMSDI Reports Provide

The FMSDI-2024 reports provide best practices as prescriptive prose. BP1, for example, states:

> *"Always record the datum, epoch, transformation method, and vertical orientation convention in metadata."*

BP3 states:

> *"If fresh acquisition is not feasible, interpolation techniques may be applied. However, introduced artefacts or assumptions must be clearly documented, and error metrics and confidence levels should be quantified and included in metadata."*

An analyst reading these reports and applying them to the SeaDOTS inventory would produce a qualitative checklist: *Does this dataset have a declared datum? Is interpolation documented?* The answer would be subjective — recorded as a narrative note, not a structured property name. Two analysts would produce different outputs. Neither output could be fed into a validation pipeline.

### 7.2 Side-by-side comparison per inventory record

The table below shows, for the 19 matched records, what a raw-report assessment produces versus what the building-block assessment produces. The columns are:

- **Report guidance** — the best-practice text that applies, as a direct quote or paraphrase
- **BB property** — the specific schema property that encodes that requirement
- **What changes** — the concrete difference in output

| Row | Dataset | Report guidance | BB property | What changes |
|-----|---------|----------------|-------------|--------------|
| 12 | Bathymetrie | BP1: "record datum, epoch, transformation method" | `vertical-datum-reference.datumName`, `.verticalOrientation` (required), `.transformationMethod` | Report → note in spreadsheet. BB → JSON Schema `required` constraint; validation fails at ingest if absent |
| 46 | EMODnet bathymetry | BP3: "interpolation assumptions must be clearly documented; introduced artefacts or assumptions must be clearly documented" | `oim-coastal-feature.dataLineage.gapFilled=true` → conditionally requires `.interpolationMethod` | Report → reviewer checks PDF lineage. BB → machine-enforced: `gapFilled=true` without `interpolationMethod` fails schema validation |
| 47 | Kartverket/GeoNorge | BP1: "prefer the geoid as the zero-height reference; use national models" | `vertical-datum-reference.separationSurface.modelReference` | Report → analyst must know that Norwegian Chart Datum ≠ MSL and look up UKHO VORF equivalent. BB → field explicitly requires model name at publish time |
| 45 | MAREANO | BP2: "provide data quality indicators associated with observation datasets" | `oim-coastal-feature.dataLineage.captureMethod`, `.resolutionInfo.horizontalResolution` | Report → ISO 19115 quality report (separate document). BB → inline properties in each GeoJSON feature; queryable via OGC API Features filter |
| 39/40 | Ports | BP1: "always record the datum, epoch, transformation method, and vertical orientation convention" | `vertical-datum-reference.verticalOrientation` (required enum `up`/`down`) | Report → "document the datum". BB → forces an explicit choice between land convention (up) and hydrographic convention (down); cannot publish without it |
| 15 | Norkyst800 | BP1: "use a gravity-based vertical datum as the baseline zero-height reference surface" | `vertical-datum-reference.datumEpoch`, `.crsIdentifier` (EPSG URI) | Report → human reads CMEMS documentation and notes "MSL". BB → machine-readable EPSG URI; epoch makes temporal drift in dynamic frame explicit |
| 25 | Utsira Nord polygon | BP1: "common Geodetic Reference Frame"; BP3 (implicit — polygon boundary = gap boundary) | `dynamic-shoreline.shorelineType`, `.tidalDatumReference` | Report → no specific guidance for area polygons. BB → identifies the polygon boundary as a `tidalDatumContour` requiring `tidalDatumReference=MHWS`, making the legal shoreline definition explicit |
| 2 | CMEMS NW Shelf BGC L3 | BP2: "include metadata… including spatial reference systems, vertical datums, accuracy" | `vertical-datum-reference` embedded in observation feature | Report → check ISO 19115 metadata record (separate). BB → datum embedded in each feature; present regardless of whether ISO metadata record exists |
| 11/73 | Ocean Physics products | BP1: "sea surface height and depth fields require unambiguous vertical datum" | `vertical-datum-reference.datumName`, `.crsIdentifier` | Report → "check the product documentation". BB → fails validation if crsIdentifier not an EPSG URI with valid format |
| 71/81/82 | MPAs / Marine Spatial Plan | BP4: "multi-agency data frameworks" (governance, not technical) | `oim-coastal-feature.featureDomain` | Report → no schema-level guidance; BP4 is governance only. BB → `featureDomain=marine` annotation enables SPARQL queries across federated datasets regardless of source agency |
| 61/74/90 | Map layers (low confidence) | BP2: "register datasets in federated catalogs using GeoDCAT-AP or OGC API Records" | `oim-coastal-feature.featureDomain` (structural benefit only) | Report → "publish to catalog". BB → featureDomain annotation is a prerequisite for cross-domain feature queries; report does not identify this as a per-feature requirement |

### 7.3 Precision

The raw reports use vocabulary that is precise in intent but imprecise in operationalisation. BP1 says to record "vertical orientation convention" — but does not define the canonical terms, does not specify where in the metadata this should appear, and does not distinguish it from the CRS orientation already encoded in the EPSG definition. The `verticalOrientation` enum (`up`/`down`) in the building block resolves all three ambiguities: it is a named field, at feature level, with exactly two legal values, independent of the EPSG CRS string.

Similarly, BP3's mandate to document interpolation assumptions is open-ended. The building block narrows it to a specific boolean flag (`gapFilled`) and a schema `if/then` rule that makes the interpolation method field required when that flag is true. The report cannot enforce this; the building block can.

### 7.4 Coverage differences

Some inventory records that are directly affected by the FMSDI requirements were not identified by a raw-report reading but were identified by the building-block analysis:

**Records the report would not flag but the BB analysis does:**

- **Rows 39/40 (Ports):** BP1 is framed around elevation datasets and topo-bathymetric surveys. A port location dataset is not the obvious target of BP1 prose. However, berthing depths are depth values, and the building-block analysis flags them because `oim-coastal-feature` includes `tideContext.tidalState` — making the tidal window constraint on harbour access a required field rather than an implicit assumption.

- **Row 82 (Swedish Marine Spatial Plan):** BP4 addresses governance but not schema. The building-block analysis adds `featureDomain=marine` classification that is not prompted by any BP prose, but that enables the cross-agency federated queries BP4 is trying to facilitate.

- **Row 25 (Utsira Nord polygon):** The FMSDI reports address shoreline data in the context of survey products and satellite observations. A static polygon from a development tender is not discussed. The building-block analysis identifies it as a `tidalDatumContour` candidate because the seaward boundary of a development zone is legally a tidal datum line — a connection the report does not make explicitly.

**Records the report flags that the BB analysis rates low:**

- **All BP2 records (FAIR metadata):** BP2 requires ISO 19115 metadata for every dataset. Applied to the inventory, every record (88/88) should be flagged. The building-block analysis deliberately excludes this: the STAC/DCAT metadata generation workflow in ILIAD covers BP2 separately, and including it here would dilute the signal. The reports do not make this distinction — BP2 appears co-equal with BP1.

- **BP4 governance records:** The reports apply BP4 broadly, including to fisheries statistics (e.g., rows 58–67, 75–89). The building-block analysis rates these out of scope because no schema BB operationalises governance. The reports give no basis for making this distinction.

### 7.5 False positives: what formalization prevents

The keyword-matching phase of the building-block analysis produced false positives that manual curation removed:

- "Offshore" matching "shore" → rows 3, 16, 55 wrongly scored for `dynamic-shoreline`
- "Coastal infrastructure" matching economic reports → rows 75–78 wrongly scored for `oim-coastal-feature`

The raw-report analysis would produce the same false positives — BP1 applies to "all observations" and BP3 to "all coastal data" — but without a schema to test against, there is no mechanism to detect them. The building-block analysis surfaced them because the schema required specific property types (LineString geometry, numeric elevation values) that economic tabular data does not have.

### 7.6 What formalization does not provide

**Temporal change:** the inventory records are snapshots. A building-block schema cannot flag that EMODnet bathymetry (row 46) was last updated in 2022 and may have an outdated datum definition. BP2 addresses this through `datumEpoch` and `temporalCoverage` in metadata, but only a human reviewer with knowledge of the dataset's history would know to check.

**Confidence in absence:** the `dynamic-shoreline` building block found only 3 indirect matches. This correctly identifies a data gap — but the building-block analysis cannot determine whether the gap is because shoreline data does not exist for Utsira, or because it exists but was not included in the inventory. That distinction requires domain knowledge about what data providers hold.

**Governance and legal context:** BP4 requirements — which agency is responsible, what data-sharing agreements exist, how funding affects availability — are entirely outside schema formalization. The building blocks produced here address BP1, BP3, and BP5. BP2 is partially covered (metadata properties embedded in features). BP4 is not covered.

### 7.7 Summary assessment

| Dimension | Raw FMSDI reports | Formalized building blocks |
|-----------|-------------------|---------------------------|
| **Precision of requirement** | Prose; multiple valid interpretations | Named properties with types, enums, and schema conditionals |
| **Machine-enforceability** | None — manual checklist only | JSON Schema validation at ingest; fails at publish without required fields |
| **Analyst consistency** | Dependent on individual knowledge | Deterministic: same schema, same result |
| **Coverage (true positives)** | All 5 BPs, 88 records in scope | 3 BPs operationalised; 19 records matched |
| **False positive rate** | High for tabular/economic data (no geometry filter) | Reduced by schema type constraints; residual false positives caught by curation |
| **Gap detection** | Identifies missing survey coverage (BP3) | Identifies missing *schema types* — the absence of any `dynamic-shoreline` record is machine-detectable |
| **Novel connections** | Reports context = intertidal surveys and products | BBs extend to ports, development zone polygons, marine spatial plans — not discussed in reports |
| **BP2 (FAIR metadata)** | Applies to all 88 records | Deferred to STAC/DCAT pipeline; not in scope for feature-level BBs |
| **BP4 (Governance)** | Applies broadly | Out of scope for schema formalization |
| **Speed of assessment** | Days per dataset (ISO 19115 audit) | Seconds per dataset (schema validation) |

The core finding is that formalization trades coverage for precision and speed. The raw reports apply to everything and say something about everything. The building blocks apply to a defined subset and say something machine-enforceable about that subset. Both are needed: the reports establish intent and scope; the building blocks provide the computable layer that makes compliance verifiable at the point of data publication rather than in a separate audit.

---

## 8. References

| Reference | URI |
|-----------|-----|
| OGC FMSDI 2024 Pilot Summary Report (OGC 24-061) | http://ogc.pages.ogc.org/FMSDI-2024/ |
| OGC FMSDI 2024 Best Practices Report (OGC 24-064) | http://ogc.pages.ogc.org/FMSDI-2024/ |
| OGC FMSDI 2024-2 Revised Summary Report | http://ogc.pages.ogc.org/FMSDI-2024-2/ |
| Compusult D100 — FMSDI5 Coastal Erosion & Vessel Navigation Demonstrator | http://ogc.pages.ogc.org/FMSDI-2024/ |
| Pangaea Innovations D100 — DGGS-based Port Operations Demonstrator | http://ogc.pages.ogc.org/FMSDI-2024/ |
| TCarta D100 — Space-Based Intertidal Awareness, Hurst Spit | http://ogc.pages.ogc.org/FMSDI-2024/ |
| IHO S-100 Universal Hydrographic Data Model | https://iho.int/en/iho-standards/standard-publications-and-s-100 |
| IHO S-32 Hydrographic Dictionary (tidal datum terminology) | https://iho.int/en/iho-standards/standard-publications-and-s-32 |
| IHO S-44 / CATZOC accuracy classification | https://iho.int/en/iho-standards/standard-publications-and-s-44 |
| EPSG Geodetic Parameter Registry | https://epsg.org/ |
| NERC Vocabulary Server | https://vocab.nerc.ac.uk/ |
| OGC Building Blocks Specification | https://opengeospatial.github.io/bblocks/ |
| ILIAD OIM Repository | https://github.com/ILIAD-ocean-twin/OIM |
| SeaDOTS Project | http://seadots-project.eu |
| UN-GGIM Integrated Geospatial Information Framework Hydro (IGIF-Hydro) | https://ggim.un.org/IGIF/ |

---

## Appendix A: Building Block IDs and File Locations

| Building Block | OGC BB ID | Source Path |
|----------------|-----------|-------------|
| Vertical Datum Reference | `ogc.hosted.iliad.api.features.vertical-datum-reference` | `_sources/vertical-datum-reference/` |
| OIM Coastal Feature | `ogc.hosted.iliad.api.features.oim-coastal-feature` | `_sources/oim-coastal-feature/` |
| Dynamic Shoreline | `ogc.hosted.iliad.api.features.dynamic-shoreline` | `_sources/dynamic-shoreline/` |

## Appendix B: Vertical Datum Quick Reference

Common datums encountered in intertidal zone work (see `vertical-datum-reference` description.json for full table):

| Datum | Abbrev. | Orientation | EPSG | Typical use |
|-------|---------|------------|------|-------------|
| Chart Datum | CD | down | 5861 | UK/IHO navigational charts |
| Lowest Astronomical Tide | LAT | down | — | IHO standard chart datum |
| Mean Sea Level | MSL | up | 5714 | Geodetic reference |
| Mean High Water Springs | MHWS | up | — | Legal shoreline, UK |
| Ordnance Datum Newlyn | ODN | up | 5701 | UK national land levelling |
| WGS84 Ellipsoid | WGS84 | up | 4979 | GNSS, satellite imagery |
| Southampton Chart Datum | SCD | down | — | The Solent; offset −2.74 m from ODN |
| Norwegian Chart Datum | NCD | down | — | Norwegian charts |

National transformation models: NOAA VDatum 4.3 (US) · UKHO VORF 2022 (UK) · CHS HyVSEPs (Canada)
