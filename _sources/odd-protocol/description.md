# ODD Protocol Description Record

## Purpose

This building block defines an OGC API Records profile for publications and descriptions that use the **ODD Protocol** (Overview, Design concepts, Details) for documenting agent-based and individual-based simulation models (Grimm et al. 2020, https://doi.org/10.18564/jasss.4259).

The record combines:

- **GeoDCAT-Records** (`ogc.geo.geodcat.geodcat-records`) as the outer bibliographic scaffold — providing title, authors, DOI, themes, keywords, and links via OGC API Records / DCAT
- **PROV profile** (`ogc.geo.geodcat.geodcat-records-prov`) for model lineage and derivation chains
- **Open Science** (`ogc.osc.ontology.openscience`) for code and workflow links
- An **`odd` extension object** encoding all seven ODD elements as structured, machine-readable properties

## Design Philosophy

The `odd` extension is intentionally **open-ended at the vocabulary level**. State variable `vocabularyTerm` fields and `inputData[].vocabularyTerm` fields are annotation slots where domain profiles inject authoritative URIs:

| Domain | Preferred vocabulary |
|---|---|
| Marine physics / chemistry | NERC P01/P02/P06, CF standard names |
| Marine biology | Darwin Core, WoRMS/OBIS AphiaID |
| Fish stocks | ICES vocabulary |
| Social simulation | FOAF, schema.org, CESSDA |
| General units | QUDT |

This means the base block validates any string in those fields. A domain sub-profile (e.g. `odd-protocol-marine`) would constrain `vocabularyTerm` to a specific vocabulary URI pattern.

## ODD Seven Elements

| Element | Section | Schema key |
|---|---|---|
| Purpose and Patterns | Overview | `odd.purpose`, `odd.patterns` |
| Entities, State Variables and Scales | Overview | `odd.entities` |
| Process Overview and Scheduling | Overview | `odd.processOverview` |
| Design Concepts | Design Concepts | `odd.designConcepts` |
| Initialization | Details | `odd.initialization` |
| Input Data | Details | `odd.inputData` |
| Submodels | Details | `odd.submodels` |

The 11 design concepts (`basicPrinciples`, `emergence`, `adaptation`, `objectives`, `learning`, `prediction`, `sensing`, `interaction`, `stochasticity`, `collectives`, `observation`) are all free-text fields within `odd.designConcepts`.

## Namespace

The `odd:` namespace is provisionally `https://w3id.org/iliad/odd#`. Terms without an established external ontology mapping are defined there. A formal ODD ontology may be registered once the vocabulary stabilises.

## Relationship to TRACE

The TRACE framework (Transparent and Comprehensive model Evaluation) documents broader model development and testing. TRACE documents may be linked via `links[rel="related"]`; a separate `odd-trace` profile would extend this block if structured TRACE encoding is needed.
