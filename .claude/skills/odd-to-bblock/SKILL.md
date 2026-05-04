---
name: odd-to-bblock
description: >
  Use when converting a textual ODD Protocol description (pasted text, URL, file
  path, folder of documents, or conversation-attached files) into a JSON record
  conforming to the ogc.hosted.iliad.api.features.odd-protocol building block.
  Accepts multiple source documents simultaneously — main paper plus supplements,
  code README, and attached files — assigns each a role, then extracts the seven
  ODD elements across all sources. Asks for confirmation at each section before
  producing the final record.
---

# ODD-to-Building-Block Conversion Skill

## Purpose

Convert a textual ODD Protocol description into a machine-readable JSON record
conforming to the `ogc.hosted.iliad.api.features.odd-protocol` building block.
The output is an OGC API Records Feature with a `properties.odd` extension object
covering all seven ODD elements.

Accepts a **document bundle** — any combination of a main paper, numbered ODD
supplements, a code README, and files attached directly to the conversation.
ODD sections that are spread across multiple documents are merged coherently.

## Activation

Use this skill when the user:

- Pastes ODD text from a paper or supplement
- Provides a URL to a paper, PDF, or web page containing an ODD
- Provides a file path to a single document
- Provides a folder path containing multiple ODD-related documents
- Attaches one or more files directly to the conversation
- Asks to "convert", "encode", "extract", or "generate a record from" an ODD

Do not use this skill for:

- General ABM code generation
- STAC or DCAT generation from non-ODD data sources (use `csv-to-metadata` or `generate-metadata` instead)
- Building block creation (use `check-in` instead)

## Required Input

At least one of:

- `text`: pasted ODD text (or multiple blocks separated by `---`)
- `url`: URL to the paper or ODD description (may be repeated: `url=X url=Y`)
- `filepath`: local path to a single document
- `folder`: local path to a directory; all readable files in it are ingested
- **conversation attachments**: files or text blocks the user drops directly into the chat

If none are provided, ask exactly:

> Please provide the ODD description — paste text, give a URL, a file path, or a folder path. You can also attach files directly to this message.

Do not continue until at least one source is provided.

## Optional Inputs

- `doi`: DOI of the paper (helps pre-fill `externalIds`)
- `domain`: domain hint (marine | ecology | social | other) — used to suggest vocabulary terms
- `output_path`: path to write the resulting JSON record
- `confirm`: `yes` to skip per-section confirmation and produce the full record immediately
- `primary`: filename or URL hint identifying the main paper when multiple documents are provided

---

## Document Role Classification

Each ingested document is assigned one of these roles before extraction begins.
Role assignment drives which fields and ODD sections are read from which source.

| Role | Description | Assigned when… |
|---|---|---|
| `primary` | Main publication — bibliographic metadata and top-level ODD | Contains title/authors/abstract or DOI; or is named by `primary` argument |
| `supplement-odd` | Standalone ODD description (full or partial) | Filename or heading contains "ODD", "supplement", "S1"–"S7" and ODD section headings are detected |
| `supplement-trace` | TRACE document | Filename or content contains "TRACE" |
| `supplement-experiment` | Experiment / scenario descriptions | Filename or content contains "experiment", "scenario", "S7" |
| `code-readme` | Model implementation notes | Filename is `README*`, `DESCRIPTION*`, or content is a code repository description |
| `parameter-table` | Parameter list or calibration tables | Content is predominantly tabular with numeric values and unit strings |
| `input-data` | Input dataset description | Content describes input files (CSV, NetCDF, shapefile) used by the model |
| `other` | Supplementary material with unrecognised structure | Default when no other role matches |

A single document may carry more than one role (e.g. a paper that contains both the main ODD and a parameter table).

---

## Extraction Workflow

### Phase 1 — Source Ingestion and Inventory

#### 1a. Collect all sources

Gather documents from all provided inputs in parallel:

**From `folder`:**
- List all files: `*.txt`, `*.md`, `*.html`, `*.pdf`, `*.docx`, `*.rtf`, `*.csv`, `*.json`
- Read each file that is readable as text
- Record filename, byte size, and first 200 characters as a preview

**From `url` (one or more):**
- Fetch each URL and extract plain text
- Record the URL as the document identifier

**From `filepath`:**
- Read the single file

**From `text`:**
- If multiple blocks are separated by `---`, treat each block as a separate document
- Otherwise treat as a single document

**From conversation attachments:**
- Treat each attached file or text block as a separate document
- Use the attachment filename (if available) as the document identifier; otherwise label sequentially as `attachment-1`, `attachment-2`, …

#### 1b. Build document inventory

After ingestion, show the user a table:

> **Document inventory (N documents):**
>
> | # | Source | Size | Detected role | Preview |
> |---|---|---|---|---|
> | 1 | main_paper.pdf | 42 kB | primary | "The ODD Protocol for…" |
> | 2 | supplement_S1.pdf | 18 kB | supplement-odd | "ODD Guidance and check…" |
> | 3 | parameters.csv | 4 kB | parameter-table | "Parameter, Value, Unit…" |
> | 4 | attachment-1 | — | supplement-odd | "1. Purpose…" |
>
> Are the role assignments correct? Type `role <#> <new-role>` to reassign, or press Enter to continue.

Wait for confirmation before proceeding to Phase 2.

### Phase 2 — Bibliographic Extraction

Read bibliographic fields **only from the `primary` document** (or from the
document with the most complete title/author/date information if no primary was
identified). Other documents contribute ODD content, not bibliographic metadata.

Locate the following fields in the source text:

| Field | Target path | Fallback |
|---|---|---|
| Title | `properties.title` | Ask user |
| Authors | `properties.contacts[].name` | Ask user |
| Publication date | `properties.created` | Ask user |
| Journal / venue | `links[rel=canonical].title` | Omit |
| DOI | `properties.externalIds[scheme=doi]` | Use `doi` arg or ask |
| URL | `links[rel=canonical].href` | Use source URL |
| Abstract | `properties.description` | First paragraph after title |
| License | `properties.license` | Omit, note as missing |
| Keywords | `properties.keywords` | Infer from themes |

Report what was found and ask for corrections before proceeding:

> **Bibliographic fields extracted:**
> - Title: …
> - Authors: … (N authors)
> - DOI: …
> - Date: …
> - License: [not found — please provide if known]
>
> Are these correct? Anything to add or change?

Wait for confirmation before continuing to Phase 3.

### Phase 3 — Cross-Document ODD Section Detection

Scan **every document** with role `primary`, `supplement-odd`, or `other` for
ODD section headings. Accept heading variations (e.g. "1. Purpose" / "Purpose
and patterns" / "OVERVIEW — Purpose").

Standard headings to match (case-insensitive, partial match):

```
Overview
  1. Purpose (and Patterns)
  2. Entities, State Variables (and Scales)
  3. Process Overview (and Scheduling)
Design Concepts
  4. Design Concepts
Details
  5. Initialization
  6. Input Data
  7. Submodels
```

#### Source assignment rules

- If a section heading is found in **one document only**, that document is the sole
  source for that section.
- If the same section heading is found in **multiple documents** (e.g. a brief
  version in the paper and a detailed version in supplement S1), **use the longer
  / more detailed version** and note the secondary source as a `links[rel=related]`
  entry pointing to the shorter version.
- If a `parameter-table` document is present, it feeds `odd.submodels[].parameterization`
  and `odd.inputData[]` entries regardless of where submodel headings appear.
- If a `code-readme` document is present, extract any model version, platform,
  and repository URL for `links[rel="osc:software"]`; also mine it for submodel
  implementation details that supplement the ODD text.
- If a `supplement-experiment` document is present, its content feeds
  `odd.inputData[]` and `odd.submodels[]` scenario entries, and generates a
  `links[rel="osc:experiment"]` entry.

#### Cross-document section map

After scanning, show the user which document each section came from:

> **ODD sections — source assignment:**
>
> | Section | Found | Source document | Notes |
> |---|---|---|---|
> | Purpose and Patterns | ✓ | main_paper.pdf (§1) | — |
> | Entities, State Variables | ✓ | supplement_S1.pdf (§2) | longer version used; paper §2 linked |
> | Process Overview | ✓ | main_paper.pdf (§3) | — |
> | Design Concepts | ✓ | main_paper.pdf (§4) | — |
> | Initialization | ✓ | attachment-1 | — |
> | Input Data | ✗ | — | not found in any document |
> | Submodels | ✓ | supplement_S1.pdf (§7) + parameters.csv | parameter table merged |
>
> Missing sections will be set to empty/null.
> Proceed with extraction?

Wait for confirmation.

### Phase 4 — Section-by-Section Extraction

Process sections in ODD order. For each section, extract the structured content
and show it to the user in abbreviated form before moving on.

#### 4a. Purpose and Patterns → `odd.purpose`, `odd.patterns`

- Extract the purpose statement as a single string for `odd.purpose`
- Detect any explicitly named patterns (POM patterns, stylised facts):
  - Look for phrases like "the model reproduces", "pattern:", "key pattern"
  - Each pattern becomes an entry in `odd.patterns` with `name` and `description`
  - If a DOI or URL for the pattern source is found, add it as `reference`

Show extracted values and ask:

> **Purpose and Patterns:**
> ```json
> { "purpose": "…", "patterns": [ … ] }
> ```
> Correct, or anything to add?

#### 4b. Entities, State Variables and Scales → `odd.entities`

For each entity type:
1. Extract name and role (agent, patch, grid-cell, network-node, environment, resource, other)
2. Extract all listed state variables with name, type, unit, range if given
3. For each state variable, propose a `vocabularyTerm` URI:
   - If `domain=marine`: search for NERC P01/P02 or CF standard name matches
   - If `domain=ecology`: search for Darwin Core term matches
   - If `domain=social`: note no standard vocabulary; leave vocabularyTerm empty
   - Otherwise: note candidate vocabulary and ask user to confirm
4. Extract spatial and temporal scales

Show extracted values and propose vocabularyTerm candidates:

> **Entities extracted:**
> | Entity | Type | State Variables |
> |---|---|---|
> | Fish school | agent | x, y, speed, energyLevel |
>
> **Proposed vocabulary terms (please confirm or replace):**
> - `speed` → `http://vocab.nerc.ac.uk/collection/P01/current/LCSAZZ01/` (NERC: velocity)
> - `energyLevel` → no standard term found — leave empty or provide URI

Wait for confirmation per entity group.

#### 4c. Process Overview and Scheduling → `odd.processOverview`

- Extract `scheduling` description (synchronous/asynchronous, random order, etc.)
- List each named process with its executedBy entity type and brief description

Show and confirm.

#### 4d. Design Concepts → `odd.designConcepts`

Scan for the 11 concept subsections. Accept both numbered list format ("4.1 Emergence")
and free-text paragraph format. Extract the text corresponding to each concept.

If a concept subsection is absent, set its value to `null` and note it.

Show a summary table and ask:

> **Design Concepts extracted:**
> | Concept | Found | Length |
> |---|---|---|
> | basicPrinciples | ✓ | 2 sentences |
> | emergence | ✓ | 1 sentence |
> | learning | ✗ | not found |
> | … | … | … |
>
> Continue?

#### 4e. Initialization → `odd.initialization`

- Extract the description of the initial state
- Note any mentioned random seeds
- Detect links to initialization data files

Show and confirm.

#### 4f. Input Data → `odd.inputData`

For each named input dataset:
1. Extract name and description
2. Detect access URL or DOI if mentioned → `source`
3. Detect format (CSV, NetCDF, shapefile, …) → `format`
4. Detect temporal coverage if stated
5. Propose `vocabularyTerm` using same vocabulary priority as Phase 4b

Show and confirm.

#### 4g. Submodels → `odd.submodels`

For each named submodel:
1. Extract name and description
2. Extract equations (LaTeX or plain text)
3. Extract parameter table or list → `parameterization`
4. Detect any linked code repositories or supplements → `links`

Show and confirm.

### Phase 5 — Themes and Keywords

From the extracted content, propose `properties.themes` entries:

1. Identify the simulation domain (ecology, marine, social, epidemiology, …)
2. Map to a vocabulary concept where possible:
   - Marine: NERC/EMODnet theme registers
   - Ecology: ENVO, Darwin Core
   - Social: CESSDA Thesaurus
   - ABM (all domains): propose `agent-based-model` as a keyword concept
3. Present candidates and ask user to confirm the scheme URI

> **Proposed themes:**
> - "Agent-Based Model" — https://vocabularies.jasss.org/themes (JASSS)
> - "Marine Ecology" — [proposed, no authoritative URI found — confirm or provide]
>
> OK to use these, or provide a preferred vocabulary scheme?

Wait for confirmation before finalising.

### Phase 6 — Provenance and Supplement Links

Build the `links` array from all documents in the bundle:

#### From the `primary` document
- `rel: "canonical"` → journal article URL if available
- `rel: "cite-as"` → DOI URL

#### From each `supplement-odd` document
- `rel: "related"` with `title` set to the supplement label (e.g. "ODD Guidance — Supplement S1")
- If the supplement is a local file with no public URL, omit `href` and add
  `title` only; the record remains valid but the link is informational

#### From each `supplement-trace` document
- `rel: "related"` with `title: "TRACE document"`

#### From each `supplement-experiment` document
- `rel: "osc:experiment"` with `title` from the document title or filename

#### From each `code-readme` document
- Extract repository URL (GitHub, CoMSES, OpenABM, Zenodo) if present
- Add `rel: "osc:software"` with `href` = repo URL and `type: "text/html"` or
  `"application/zip"` as appropriate
- If no URL is found, note software as described but not linked

#### From predecessor mentions in any document
- If the text mentions "based on", "extends", "adapted from", or cites a prior
  model with a DOI → add `prov:wasDerivedFrom` entry at the `properties` level

#### From `input-data` documents
- Add `rel: "dcat:distribution"` entries for each described input dataset

After building the links list, show it to the user:

> **Links to be added (N entries):**
> | rel | href / title | Source document |
> |---|---|---|
> | canonical | https://www.jasss.org/… | primary |
> | related | Supplement S1 — ODD Guidance | supplement_S1.pdf |
> | osc:software | https://github.com/… | README.md |
>
> Add, remove, or edit any entry?

### Phase 7 — Record Assembly

Assemble the complete JSON record using this template:

```json
{
  "id": "<doi:DOI or url-slug>",
  "type": "Feature",
  "geometry": null,
  "time": { "date": "<YYYY-MM-DD>" },
  "properties": {
    "type": "ScholarlyArticle",
    "title": "…",
    "description": "…",
    "created": "…",
    "updated": "…",
    "language": "en",
    "externalIds": [ { "scheme": "doi", "value": "…" } ],
    "contacts": [ { "name": "…", "roles": ["author"], "organization": "…" } ],
    "themes": [ { "concepts": [ … ], "scheme": "…" } ],
    "keywords": [ … ],
    "license": "…",
    "formats": [ { "mediaType": "text/html" } ],
    "odd": {
      "purpose": "…",
      "patterns": [ … ],
      "entities": [ … ],
      "processOverview": { "scheduling": "…", "processes": [ … ] },
      "designConcepts": {
        "basicPrinciples": "…",
        "emergence": "…",
        "adaptation": "…",
        "objectives": "…",
        "learning": "…",
        "prediction": "…",
        "sensing": "…",
        "interaction": "…",
        "stochasticity": "…",
        "collectives": "…",
        "observation": "…"
      },
      "initialization": { "description": "…", "seed": "…", "links": [] },
      "inputData": [ … ],
      "submodels": [ … ]
    }
  },
  "links": [ … ]
}
```

Show the complete record to the user and ask:

> **Record assembled.** Review the complete JSON above.
> - Type `ok` to accept and write to `<output_path>` (if provided)
> - Type `edit <section>` to revise a specific section
> - Type `copy` to receive the JSON without writing to disk

### Phase 8 — Output

If `output_path` is provided and the user accepts:
- Write the JSON record to `output_path`
- Confirm: `Written to <path>`

If no `output_path`, return the JSON inline.

---

## Vocabulary Priority (for vocabularyTerm slots)

| Priority | Vocabulary | Base URI | Use for |
|---|---|---|---|
| 1 | NERC P01/P02/P06 | http://vocab.nerc.ac.uk/collection/ | Physical/chemical/biological parameters |
| 2 | CF Standard Names | http://cfconventions.org/Data/cf-standard-names/ | Atmospheric/ocean variables |
| 3 | Darwin Core | http://rs.tdwg.org/dwc/terms/ | Species, occurrences, taxonomy |
| 4 | OBIS / WoRMS | http://www.marinespecies.org/ | Marine taxa |
| 5 | ICES | http://vocab.ices.dk/ | Fish stocks, sampling areas |
| 6 | EMODnet | EMODnet thematic URIs | Marine thematic classification |
| 7 | OGC / ISO | OGC definitions server | Geospatial standards |
| 8 | schema.org | https://schema.org/ | Last resort only |

---

## Incomplete ODD Handling

If an ODD section is missing or incomplete:
- Set the corresponding value to `null` (scalar fields) or `[]` (array fields)
- Add a note in `description` of the parent object where applicable
- Include a `links` entry with `rel: "related"` pointing to supplements if referenced

Do not fabricate content for missing sections.

---

## Output Contract

Always make clear which values were:

- **extracted** from the source text
- **proposed** (vocabulary terms, themes) and awaiting confirmation
- **missing** (null / empty) due to absent ODD sections
- **user-provided** via arguments

Mark proposed vocabulary terms explicitly as `[proposed — please confirm]` in
the confirmation prompts.

---

## Example Invocations

**Single URL:**
```
/odd-to-bblock url=https://www.jasss.org/23/2/7.html doi=10.18564/jasss.4259 domain=social output_path=_sources/odd-protocol/examples/jasss_odd_2020.json
```

**Folder of documents (paper + supplements):**
```
/odd-to-bblock folder=~/papers/fishschool-odd domain=marine output_path=_sources/odd-protocol/examples/fishschool.json
```

**Multiple URLs (main paper + supplement):**
```
/odd-to-bblock url=https://doi.org/10.1234/paper url=https://example.org/supplement_S1.pdf domain=ecology
```

**Pasted text:**
```
/odd-to-bblock text="<paste ODD text here>" domain=marine
```

**Conversation attachments:**

Attach one or more files directly to the message, then write:
```
/odd-to-bblock domain=social primary=main_paper.pdf
```
The skill will ingest every attached file and ask you to confirm role assignments.

**Mixed: folder + URL for the main paper:**
```
/odd-to-bblock folder=~/odd-supplements url=https://www.jasss.org/23/2/7.html primary=https://www.jasss.org/23/2/7.html domain=social
```

---

## References

- ODD Protocol (second update): https://doi.org/10.18564/jasss.4259
- Building block schema: `_sources/odd-protocol/schema.yaml`
- Building block example: `_sources/odd-protocol/examples/jasss_odd_protocol_2020.json`
- GeoDCAT-Records: https://ogcincubator.github.io/geodcat-ogcapi-records/
- NERC vocabulary server: https://vocab.nerc.ac.uk/
- CF standard names: http://cfconventions.org/
- Darwin Core: https://dwc.tdwg.org/
