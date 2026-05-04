# A standards-based interoperability framework for coastal Digital Twin engines, data catalogs, and indicator systems: the SeaDOTs approach

**Piotr Zaborowski¹, [co-authors]**  
¹ SINTEF Ocean

---

## Abstract

Coastal Digital Twins (DTs) remain interoperability islands: their simulation engines, input/output datasets, and indicator dependency structures each live in incompatible formats that are not discoverable, queryable, or composable across platforms. We present a three-layer interoperability framework developed in the SeaDOTs project that addresses this gap. A catalog layer (STAC + OGC API Records) makes DT engines and their datasets discoverable and citable. An engine description layer profiles three complementary standards — the Open Simulation Platform Description (OSPD), the Application Package (APKG), and the ODD Protocol — as a single application profile covering co-simulation structure, software packaging, and scientific model specification respectively. An indicator layer (OIM Variables + PropertyRelationship building block) encodes the observable properties at the system boundary and the weighted directed graph of their mutual influence. Together these layers convert a bespoke DT demonstrator into a FAIR, SPARQL-queryable, platform-independent component. The framework is implemented on the Norwegian Utsira, German, and Swedish SeaDOTs demonstrators and published as OGC Building Blocks registered in the OGC Building Block Register.

---

## 1. Introduction

A coastal Digital Twin is, at its core, a simulation pipeline: inputs from observations and forcing data drive a model engine that produces scenario outputs — projections of fisheries yield, renewable energy capacity, species abundance, or economic indicators. These outputs are only meaningful when they come with (a) provenance — which model version, which experiment, which input data produced them; (b) semantic annotation — which real-world variables are being simulated and in what units; and (c) dependency structure — which indicators influence which, and with what directional weight.

In practice none of these three are standardised across DT projects. Engines are distributed as custom software archives or Docker images with no common metadata vocabulary. Inputs and outputs are catalogued inconsistently, often only as file shares. Indicator dependencies are spreadsheets. The result is that comparing scenarios across DT platforms, reproducing model runs, or feeding DT outputs into a policy dashboard requires bespoke integration work for every combination of tools.

The SeaDOTs project (Semantic and Accessible Digital Twins for the Ocean and Society, http://seadots-project.eu) targets exactly this gap across three national demonstrators in Germany, Norway, and Sweden, each applying a Social-Ecological System (SES) model [1] to a coastal management problem. This paper presents the interoperability framework developed to publish those demonstrators as FAIR, machine-readable components that are composable with the EDITO marine data platform and the ILIAD Ocean Digital Twin ecosystem.

---

## 2. Framework overview

The framework is structured in three layers that answer three orthogonal questions about a DT component (Figure 1):

- **Catalog layer** (STAC + OGC API Records): *Where is it and how do I find it?* Describes engines, input datasets, and output collections as discoverable catalog records with spatial extent, temporal coverage, and provenance links.
- **Engine description layer** (OSPD + APKG + ODD application profile): *What is it and how does it work?* Describes the co-simulation structure, software packaging and execution interface, and scientific model specification in a unified, inheritable profile.
- **Indicator layer** (OIM Variables + PropertyRelationship): *What does it mean at its boundaries?* Encodes the observable properties the DT exposes at its interface to the real world and the directed, weighted graph of influence between them.

Each layer is implemented as an OGC Building Block: a versioned, testable package of JSON Schema, JSON-LD context, SHACL rules, and documentation, composable with other blocks via `$ref` import and validated by the `bblocks-postprocess` CI pipeline. All blocks are published at https://github.com/ogcincubator/bblocks-seadots and https://github.com/ILIAD-ocean-twin/iliad-apis-features.

---

## 3. Catalog layer: STAC and OGC API Records

The catalog layer assigns a persistent, resolvable identifier and a standard metadata record to every catalogable component of a DT demonstrator. Three record types cover the full lifecycle:

**DT engine record** (OGC API Records / GeoDCAT profile). An OGC Feature record with `type: SoftwareApplication` describes the simulation engine: title, version, authors, license, spatial domain (geometry), and links to the APKG package and source code repository. The record acts as the stable, citable reference for the model as a scientific artifact.

**Input dataset collection** (STAC Collection + Item). Input forcing data — observational time series, bathymetry, biogeochemical model outputs, species distribution maps — are catalogued as STAC Items carrying the `datacube` extension for gridded fields and the `table` extension for CSV/tabular inputs. Each item carries a `prov:wasUsedBy` link to the engine record.

**Experiment output record** (STAC Item). A single model run is recorded as a STAC Item with `experiment.id`, `start`/`end` timestamps, and links to output assets. PROV-O properties (`prov:wasGeneratedBy`, `prov:wasAttributedTo`) connect the output item to the engine record and the agent (model version) that produced it. This makes the full provenance chain discoverable through the catalog without additional SPARQL queries.

The STAC/Records catalog is published to the EDITO platform via its OGC API Records endpoint, making SeaDOTs DT components discoverable alongside operational oceanographic datasets.

---

## 4. Engine description layer: OSPD + APKG + ODD as a unified application profile

Three complementary standards describe a DT engine from distinct but non-overlapping perspectives. The SeaDOTs engine profile inherits from all three as an `allOf` composition in the building block schema.

**OSPD (Open Simulation Platform Description)** captures the *co-simulation architecture*: the set of Functional Mock-up Units (FMUs) or model components that make up the engine, their connection topology (input/output variable wiring), and the temporal co-simulation stepping scheme. Based on the FMI and SSP standards from the Modelica Association and OSP (Open Simulation Platform, SINTEF/DNV), OSPD provides the machine-executable specification that allows another platform to reconstruct or federate with the simulation.

**APKG (Application Package Metadata)** [2] captures the *software packaging and execution interface*: the Docker image or JAR, CWL-aligned process definitions for each model component, typed input and output parameters with constraints, temporal validity, spatial geometry of the deployed instance, and credentials/secret declarations. APKG is the deployment contract — it specifies exactly how a platform agent should launch the engine on a cloud or HPC resource.

**ODD Protocol** [3] captures the *scientific model specification*: the seven standardised sections (Purpose, Entities + State Variables, Process Overview, Design Concepts, Initialization, Input Data, Submodels) as machine-readable, vocabulary-annotated JSON. State variable `vocabularyTerm` slots accept NERC P01, CF standard names, or Darwin Core URIs; submodel `equations` fields carry the mathematical specification. The ODD record is the scientific documentation layer — it makes the causal logic of the model reproducible and peer-reviewable as linked data.

The unified engine profile imports all three via `dependsOn` and adds a `catalog` cross-reference that links the APKG process outputs to the ODD input data entries and the STAC output items. A SHACL rule enforces that every ODD `inputData[].source` resolves to a STAC Item in the catalog, closing the loop between scientific specification and data provenance.

---

## 5. Indicator layer: defining system boundaries

The indicator layer answers the question: what does this DT *observe* at its interface with the real world, and how do those observations relate causally?

**OIM Variables** (building block `ogc.hosted.iliadapi.oim-variables`) defines the base ontology: indicator concepts as `sosa:ObservableProperty` instances organised in a SKOS ConceptScheme at `https://id3.seadots.eu/indicator/`. Each indicator is a resolvable URI — a persistent, dereferenceable identifier that any dataset, model, or catalog record can reference. Composite indicators (e.g. a Drought Composite Index derived from rainfall anomaly, soil moisture, and vegetation condition) are modelled as `prov:Activity` instances that `prov:used` their component observable properties, making the composition traceable.

**PropertyRelationship** (building block `ogc.hosted.seadots.property-relationship`) encodes the directed, weighted graph of mutual influence between indicator properties — the cross-impact matrix of the SES model [1]. Each edge links a `fromProperty` and `toProperty` (both `sosa:observedProperty` URIs) with a `qudt:numericValue` weight, model provenance (`prov:wasAttributedTo`), and experiment provenance (`prov:wasGeneratedBy`). The graph is stored in RDF (Turtle), loaded into a hosted SPARQL endpoint, and linked from the STAC experiment record.

Together, OIM Variables and PropertyRelationship define the *boundary of the DT system*: the set of observable properties at the interface between the model interior and the real world it represents, plus the causal dependency structure between those properties. This boundary specification is what makes a DT scenario interpretable — a projection of fisheries production under a wind-park expansion scenario is only meaningful when the model's causal claim (wind-park area suppresses fishing grounds with weight −0.5) is published alongside the output.

---

## 6. Implementation: SeaDOTs demonstrators

All three layers are implemented for the Norwegian Utsira wind-farm demonstrator. The indicator vocabulary covers five SES properties (fisheries-production, number-of-turbines, area-use-by-wind-park, number-of-jobs, bird-tourism) and eight directed relationships. The engine is catalogued as an OGC Records Feature with APKG and ODD records linked from the experiment STAC item. The property relationship graph is queryable via SPARQL at http://defs-hosted.opengis.net/fuseki-hosted/query and browsable via OGC Rainbow / Prez.

Application to the German and Swedish demonstrators (spanning biological, physical, and socio-economic indicator domains) is in progress, requiring only new SKOS concepts and relationship instances — the three-layer profile is reused without modification.

---

## 7. Conclusions

The SeaDOTs three-layer framework — STAC/OGC Records catalog, OSPD+APKG+ODD engine profile, and OIM Variables+PropertyRelationship indicator model — converts bespoke coastal DT demonstrators into FAIR, composable, platform-independent components. By separating the *discovery* concern (catalog), the *execution* concern (engine profile), and the *meaning* concern (indicator model), the framework accommodates heterogeneous DT architectures while maintaining a common semantic interface. The OGC Building Block packaging ensures that each layer is testable, versioned, and importable by any downstream project.

Remaining work: publishing resolvable OGC Rainbow URIs for all SeaDOTs indicator properties; extending the PropertyRelationship schema with a typed influence classification (positive/negative/feedback/threshold); and integrating the OSPD co-simulation wiring with the ODD entity state-variable vocabulary to enable property-level data lineage from simulation variable to STAC output asset.

---

## References

[1] Ostrom, E. (1990). *Governing the Commons*. Cambridge University Press.  
[2] ILIAD project (2024). Application Package Metadata. https://github.com/ILIAD-ocean-twin/APKG  
[3] Grimm et al. (2020). The ODD Protocol: A Second Update. *JASSS* 23(2)7. https://doi.org/10.18564/jasss.4259  
[4] Haller et al. (2019). The Modular SSN Ontology. *Semantic Web* 10(1), 9–32.  
[5] Moreau & Missier (eds.) (2013). PROV-O: The PROV Ontology. W3C Recommendation.  
[6] OGC Incubator (2024). OGC Building Blocks. https://ogcincubator.github.io/bblocks-docs/  
[7] SeaDOTs project (2024). SeaDOTs interoperability building blocks. https://github.com/ogcincubator/bblocks-seadots  
[8] Open Simulation Platform (2023). OSP Interface Specification. https://open-simulation-platform.github.io/  
[9] EDITO-Infra (2024). European Digital Twin of the Ocean. https://edito-infra.eu  
[10] Wilkinson et al. (2016). The FAIR Guiding Principles. *Scientific Data* 3, 160018.
