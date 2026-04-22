# Claude Code Compliance Review

Review of agents, skills, prompts, and guides in `iliad-apis-features` against Claude Code conventions (subagents under `.claude/agents/`, skills under `.claude/skills/<name>/SKILL.md`, slash commands under `.claude/commands/`, and YAML frontmatter with `name` and `description` so Claude can auto-discover and invoke them).

The repo today is organized around a GitHub Copilot / VS Code "chat mode" convention (`--- mode: agent ---`, `{{selection}}` templating, references to `GPT-4o`, agent filenames prefixed with a leading dot). None of these are recognised by Claude Code, which means the current agents and skills will not be discovered or auto-triggered when the repo is opened in a Claude Code session. The fix is mechanical but touches every agent and skill file, plus the cross-references that link them.

---

## 1. Directory layout

### What exists today

```
iliad-apis-features/
├── .agents/
│   ├── .helcom-agent.md
│   ├── .metadata-dispatcher.md
│   ├── .marine-content-specialist.md
│   ├── .building-block-generator.md
│   ├── .marine-workflow-orchestrator.md
│   ├── .marine-data-agent.md
│   ├── .gis-marine-data-specialist.md
│   ├── .validation-agent.md
│   ├── .stac-metadata-generator.md
│   ├── .dcat-metadata-generator.md
│   ├── .csv-to-stac-converter.md
│   ├── .csv-to-dcat-converter.md
│   └── .geojson-to-jsonfg-converter.md
├── .skills/
│   ├── ogc-web-services-client/SKILL.md
│   ├── web-browsing-mcp/SKILL.md
│   ├── esri-client/SKILL.md
│   ├── bblock-container-validation/SKILL.md
│   ├── geojson-to-jsonfg-converter/SKILL.md
│   ├── metadata-extraction/SKILL.md
│   ├── csv-to-metadata/SKILL.md
│   └── netcdf-to-stac/SKILL.md
├── .prompts/
│   ├── validate-building-block.md
│   ├── generate-stac-dcat-metadata.md
│   ├── convert-geojson-to-jsonfg.md
│   └── building-blocks-from-marine-data.md
├── .guides/{AGENT-ARCHITECTURE.md, AGENT-QUICK-REFERENCE.md}
├── .docs/{AGENT-ECOSYSTEM-ARCHITECTURE.md, agent-ecosystem-ascii.md, ...}
├── .prompt.md                         # Copilot-style standalone prompt
└── .metadata-generation-ecosystem.md  # top-level ecosystem doc
```

### What Claude Code expects

```
iliad-apis-features/
├── CLAUDE.md                              # repo-level guidance (currently missing)
└── .claude/
    ├── agents/
    │   └── <agent-name>.md                # no leading dot; matches `name:` in frontmatter
    ├── skills/
    │   └── <skill-name>/SKILL.md          # unchanged subfolder; SKILL.md gains frontmatter
    └── commands/                          # slash commands (what `.prompts/` effectively is)
        └── <command-name>.md
```

Recommended moves:

| Current path | Target path |
|---|---|
| `.agents/.metadata-dispatcher.md` | `.claude/agents/metadata-dispatcher.md` |
| `.agents/.*.md` (all 13) | `.claude/agents/*.md` (drop leading dot) |
| `.skills/<name>/SKILL.md` | `.claude/skills/<name>/SKILL.md` |
| `.prompts/*.md` | `.claude/commands/*.md` |
| `.guides/`, `.docs/` | Keep as-is, or move into `.claude/docs/`. These are human-facing documentation, not Claude-executable artifacts. |
| `.prompt.md` (VocPrez) | `.claude/commands/vocprez-annotation.md` (see §4.3 — needs heavy rewrite) |
| `.metadata-generation-ecosystem.md` | `.claude/docs/metadata-generation-ecosystem.md` (or keep at root) |

The leading-dot filenames (`.metadata-dispatcher.md`) make the files hidden in most file browsers and shells and are not required by any tool — Claude Code doesn't use them. Drop the dot.

---

## 2. Agent files (`.agents/*.md`)

### 2.1 Frontmatter — blocking issue for every agent

Every agent currently has:

```yaml
---
mode: agent
---
```

This is **GitHub Copilot / VS Code `chatmode` frontmatter**, not Claude Code. Claude Code's subagent loader looks for `name` and `description` (and optionally `tools` and `model`). Without those fields Claude Code cannot auto-select the agent when the user's request matches — the agent is effectively dead weight.

Replace with:

```yaml
---
name: metadata-dispatcher
description: Use this agent when the user asks to generate STAC or DCAT metadata records from a data source (URL, file path, or inline sample). The agent detects the format, extracts metadata, collects missing required fields interactively, and routes to @stac-metadata-generator, @dcat-metadata-generator, or a format-specific converter.
tools: Read, Write, Edit, Bash, Grep, Glob, WebFetch
model: sonnet
---
```

Per-agent recommended frontmatter is listed in §2.3. A few notes on the fields:

- **`name`**: kebab-case, must match the filename (`metadata-dispatcher.md` → `name: metadata-dispatcher`). Cross-references in guides currently use `@metadata-dispatcher`, which aligns with this.
- **`description`**: needs to read like a trigger contract — start with "Use this agent when…" and include concrete phrases users are likely to type. The first sentence of most current agent files is close; it just needs to be moved into frontmatter and tightened.
- **`tools`**: Claude Code expects a comma-separated list of actual tool names. The current agents refer to capabilities in prose ("Web browsing", "OGC Web Services client") but never declare a tool allowlist. Leaving this off inherits every tool, which is usually the wrong default for support agents like `validation-agent`.
- **`model`**: optional. `sonnet` is a reasonable default; reserve `opus` for the orchestrators (`metadata-dispatcher`, `marine-content-specialist`, `marine-workflow-orchestrator`) and `haiku` for narrow converters (`csv-to-stac-converter`, `csv-to-dcat-converter`, `geojson-to-jsonfg-converter`).

### 2.2 `.helcom-agent.md` — a special case

This file is **not a subagent**. It's a Copilot prompt template:

```yaml
---
agent: vocprez-annotation
description: 'Add DCAT and SKOS annotations to RDF data for VocPrez/Prez UI visibility.'
model: GPT-4o
tools: [read, edit]
---
...
### Context:
{{selection}}
```

Three problems:

1. `agent:` is not a Claude Code field (`name:` is).
2. `model: GPT-4o` is an OpenAI model name; Claude Code will either ignore or reject it.
3. `{{selection}}` is VS Code Copilot templating — Claude Code does not substitute it.

This belongs under `.claude/commands/vocprez-annotation.md` as a slash command, rewritten to accept the RDF via a normal argument (`$ARGUMENTS` or an explicit `<rdf_to_annotate>` placeholder the user pastes in). The filename should also change — `.helcom-agent.md` is misleading since the content is about VocPrez/SKOS annotation, not HELCOM data.

### 2.3 Per-agent summary and recommended frontmatter

| File (current) | Role | Recommended `name` | Recommended `model` | Notes |
|---|---|---|---|---|
| `.metadata-dispatcher.md` | Orchestrator for STAC/DCAT generation | `metadata-dispatcher` | `sonnet` | Strong prose; move trigger description into `description`. Declare `tools: Read, Write, Edit, Bash, WebFetch, Grep, Glob`. |
| `.marine-content-specialist.md` | Discovery + orchestration for marine data | `marine-content-specialist` | `opus` | Heaviest agent; needs broader tool access. |
| `.marine-workflow-orchestrator.md` | Coordinates support agents | `marine-workflow-orchestrator` | `sonnet` | Pure routing — minimal tool footprint (`Read, Grep, Glob`). |
| `.building-block-generator.md` | Creates OGC bblocks | `building-block-generator` | `sonnet` | Needs `Bash` for Docker validation. |
| `.validation-agent.md` | Validates bblocks | `validation-agent` | `sonnet` | Needs `Bash, Read, Grep, Glob`. |
| `.marine-data-agent.md` | Data retrieval | `marine-data-agent` | `sonnet` | **Near-duplicate of `.gis-marine-data-specialist.md`** (see §2.4). |
| `.gis-marine-data-specialist.md` | GIS + semantic modeling | `gis-marine-data-specialist` | `sonnet` | Overlaps heavily with `marine-data-agent` and `marine-content-specialist`. |
| `.stac-metadata-generator.md` | Generic STAC generation | `stac-metadata-generator` | `sonnet` | Good. |
| `.dcat-metadata-generator.md` | Generic DCAT generation | `dcat-metadata-generator` | `sonnet` | Good. |
| `.csv-to-stac-converter.md` | CSV → STAC | `csv-to-stac-converter` | `haiku` | Narrow; `haiku` is fine. |
| `.csv-to-dcat-converter.md` | CSV → DCAT | `csv-to-dcat-converter` | `haiku` | Narrow; `haiku` is fine. |
| `.geojson-to-jsonfg-converter.md` | GeoJSON → JSON-FG | `geojson-to-jsonfg-converter` | `haiku` | Narrow; `haiku` is fine. |
| `.helcom-agent.md` | **Actually a VocPrez prompt** | (move to commands) | n/a | See §2.2. |

### 2.4 Duplicate/overlapping agents

`.marine-data-agent.md` and `.helcom-agent.md`'s *original intent* both describe "marine data discovery and retrieval specialist" with near-identical language. `.gis-marine-data-specialist.md` and `.marine-content-specialist.md` also have significant overlap around vocabulary mapping. In Claude Code, overlapping `description:` fields cause non-deterministic auto-selection — Claude has to guess which one to delegate to, which usually produces worse results than a single, well-scoped agent.

Recommendation: consolidate down to one discovery agent (`marine-data-agent`) and one modeling/semantic agent (`marine-content-specialist` — keep this as the orchestrator, delete `gis-marine-data-specialist` or merge its vocabulary-mapping workflow into `marine-content-specialist`). Update the architecture diagram in `.guides/AGENT-ARCHITECTURE.md` accordingly.

### 2.5 `@agent-name` invocation syntax in prose

The agent bodies and prompts use `@metadata-dispatcher generate X` as if that were a Claude Code command. Claude Code does not parse `@agent-name ...` in user input as a delegation directive — agents are invoked via the Task tool by the parent Claude, driven by the `description:` field matching the user's request. The `@`-prefixed references in prose are fine as documentation convention (they still read clearly) but the examples that show the user typing `@metadata-dispatcher ...` should be rewritten as natural-language requests Claude will match against the `description`, e.g. "generate a STAC item from this NetCDF file."

### 2.6 Content-level fixes common to most agents

- **Remove the preamble sentence that repeats the description.** Currently every agent opens with a prose "Use this agent when..." paragraph *and* a `description:` frontmatter field will be added on top. Move the useful content to `description:` and delete the duplicate from the body.
- **Replace the "Do not use this agent for..." paragraph.** Claude Code agents don't have a concept of negative triggers — the `description:` is the only contract. You can keep a one-line boundary statement, but put it in the description (e.g. "Not for non-marine data sources.").
- **Code blocks are still useful.** All the JSON schema, STAC item, DCAT record, and Python examples in the agent bodies are exactly what Claude will condition on at runtime. Keep them.

---

## 3. Skill files (`.skills/*/SKILL.md`)

### 3.1 Frontmatter — missing on every skill

None of the eight SKILL.md files have YAML frontmatter. They all start with `# <Title>`. Claude Code's skill loader will ignore them because it can't tell what they're for or when to trigger them.

Every skill needs:

```yaml
---
name: skill-name
description: Trigger contract — "Use this skill whenever the user wants to...". Include concrete keywords and file extensions. Include what it does in one sentence.
---

# Skill Title
...
```

Per-skill recommendations:

| Skill | Suggested `description` (opening) |
|---|---|
| `ogc-web-services-client` | `Use whenever the task involves querying OGC web services (WMS, WFS, WMTS, CSW, OGC API). Handles GetCapabilities, GetMap, GetFeature, bbox/CRS parameters, and returns executed URLs for provenance.` |
| `web-browsing-mcp` | `Use for HTTP fetches and API browsing during data discovery — marine data catalogues, vocabulary services (NERC, CF, Darwin Core, OBIS, ICES), and OGC service endpoints. Returns executed URLs for provenance.` |
| `esri-client` | `Use when the task involves ArcGIS REST services (FeatureServer, MapServer, ImageServer). Builds queries with where/outFields/bbox, handles tokens, and returns executed URLs for provenance.` |
| `bblock-container-validation` | `Use when validating an OGC building block locally via Docker (ogcincubator/bblocks-postprocess). Runs schema, context, example, and test-suite checks and produces a build-local/ artifact tree.` |
| `geojson-to-jsonfg-converter` | `Use when converting GeoJSON features or FeatureCollections to JSON-FG with OIM semantic enrichment (links, place, conformsTo). Supports oim, oim-bio-tdwg, oim-obs profiles.` |
| `metadata-extraction` | `Use when extracting STAC/DCAT metadata from a data source — NetCDF, CSV/TSV, GeoJSON, COG, OGC services. Detects format, extracts title/description/spatial/temporal/vocabulary hints.` |
| `csv-to-metadata` | `Use when converting CSV or TSV tabular data into STAC Items and/or DCAT Records. Detects lat/lon or WKT geometry, temporal columns, and column schema for the STAC table extension.` |
| `netcdf-to-stac` | `Use when converting a NetCDF file to a STAC Item with the datacube, scientific, projection, and (when applicable) eo/raster/processing extensions. Extracts dimensions, variables, CF-convention metadata.` |

### 3.2 Structural notes on skills

The skills themselves are substantively good — `bblock-container-validation` and `csv-to-metadata` in particular have working Python snippets and Docker commands that Claude can follow directly. A couple of small structural fixes make them more Claude-compliant:

- **`geojson-to-jsonfg-converter`** and **`csv-to-metadata`** include full Python class bodies. That's fine as inline reference, but Claude skills can also ship helper scripts (e.g. `.claude/skills/csv-to-metadata/converter.py`) and have SKILL.md point to them with `bash python {skill_path}/converter.py ...`. This keeps the SKILL.md short and makes the code executable rather than copy-paste.
- **`web-browsing-mcp`, `ogc-web-services-client`, `esri-client`** describe MCP server capabilities without naming the MCP servers. If there's a specific MCP server (e.g. a Fetch MCP, an OGC MCP) that backs these, call it out by name so Claude knows which server tool to reach for. Otherwise the skill is effectively "use whatever browsing/HTTP tool you have," which is implicit anyway.
- **No skill declares required inputs via frontmatter** — optional, but a block like `## Inputs` listing expected arguments (file path, URL, profile name) helps Claude pick up arguments from the user's message.

### 3.3 Naming collision: skill vs. agent

`geojson-to-jsonfg-converter` exists as both an agent (`.agents/.geojson-to-jsonfg-converter.md`) and a skill (`.skills/geojson-to-jsonfg-converter/SKILL.md`). Same kebab-case name is fine from Claude Code's perspective because agents and skills live in separate registries, but it's confusing for humans. Consider renaming the skill (`jsonfg-conversion` or `geojson-jsonfg-toolkit`) to signal the layering: the agent orchestrates, the skill is the reusable toolkit the agent uses.

---

## 4. Prompts (`.prompts/*.md`) → slash commands

### 4.1 Move to `.claude/commands/`

Claude Code's slash-command convention lives in `.claude/commands/*.md`. File frontmatter is optional; when present, it can include `description:` (shown in the `/` picker) and `argument-hint:` (shown next to the command).

| File | Target | Suggested frontmatter |
|---|---|---|
| `validate-building-block.md` | `.claude/commands/validate-bblock.md` | `description: Validate an OGC building block via Docker container`  `argument-hint: <path-to-_sources/block-name>` |
| `generate-stac-dcat-metadata.md` | `.claude/commands/generate-metadata.md` | `description: Generate STAC and/or DCAT records from a URL, file, or sample`  `argument-hint: <url\|path\|inline-sample>` |
| `convert-geojson-to-jsonfg.md` | `.claude/commands/geojson-to-jsonfg.md` | `description: Convert GeoJSON to JSON-FG with OIM semantic enrichment`  `argument-hint: <geojson-path> [oim\|oim-obs\|oim-bio-tdwg\|auto]` |
| `building-blocks-from-marine-data.md` | `.claude/commands/marine-bblock.md` | `description: Discover marine data and generate a complete OGC building block`  `argument-hint: <theme> [sources...]` |

### 4.2 Use `$ARGUMENTS` not free-form prose

Current prompts open with `@metadata-dispatcher generate X from Y` examples as if the user types that literally. Slash commands in Claude Code are more useful if they template over `$ARGUMENTS` (the text the user types after the command name). Rewrite the "Quick Start" sections to show the command invocation rather than the `@agent ...` delegation, e.g.:

```
Usage: /generate-metadata <url-or-path>

Example: /generate-metadata https://data.marine.copernicus.eu/sst.nc
```

### 4.3 `.prompt.md` (root-level VocPrez prompt)

As noted in §2.2 this is mis-labeled. It's a single-shot prompt for adding DCAT/SKOS annotations to RDF, with `{{selection}}` templating. Rewrite as a slash command:

```yaml
---
description: Add DCAT and SKOS annotations to RDF/Turtle for VocPrez/Prez UI visibility
argument-hint: <turtle-content-or-path>
---

Add DCAT and SKOS annotations to the RDF in $ARGUMENTS so it is fully browsable in the VocPrez UI.

### Requirements
1. vocprez catalog: ensure the `prez` prefix is imported and used for the catalog entry
2. Catalog Entry: create `dcat:Catalog` if missing and link the `skos:ConceptScheme` via `dcat:dataset` or `dcterms:hasPart`
...
```

---

## 5. Missing `CLAUDE.md`

There is no `CLAUDE.md` at the repo root. Claude Code reads this file on session start to pick up repo-level context. For this repo, a useful `CLAUDE.md` would cover:

- What this repo is (an OGC building blocks source repository for ILIAD marine APIs).
- How building blocks are structured (`_sources/<block-name>/` with `bblock.json`, `schema.yaml`, `context.jsonld`, `examples/`, `tests/`).
- The build process (`docker run ... ogcincubator/bblocks-postprocess ...` produces `build/` and `build-local/`).
- Pointers to the agent ecosystem (`.claude/agents/marine-content-specialist.md`, etc.) and the two primary workflows (metadata generation, marine bblock creation).
- Vocabulary priority order (NERC → CF → Darwin Core → OBIS → ICES → EMODnet → OGC/ISO → schema.org).
- Conventions: "don't create README.md in a building block; put dataset description in `description.json`".

Roughly 80–120 lines, not a novel.

---

## 6. Cross-references to update

After renaming files, these cross-reference points must be updated or the ecosystem docs will drift:

- `.guides/AGENT-ARCHITECTURE.md` and `.guides/AGENT-QUICK-REFERENCE.md` — reference `@agent-name` throughout. Links like `(../agents/.building-block-generator.md)` in `.prompts/building-blocks-from-marine-data.md` (line 404) need to point at `.claude/agents/building-block-generator.md`.
- `.docs/AGENT-ECOSYSTEM-ARCHITECTURE.md` and `.docs/agent-ecosystem-ascii.md` — update the ASCII diagrams.
- `.metadata-generation-ecosystem.md` — references `@metadata-dispatcher`, `@stac-metadata-generator`, `@dcat-metadata-generator`, etc.
- Agent bodies themselves reference other agents (`@marine-workflow-orchestrator`, `@building-block-generator`, etc.) — the names stay the same after renaming, so prose cross-refs should keep working as long as every agent's `name:` field matches the referenced token.
- `README.md` and `USAGE.md` at the root — worth a scan to confirm they don't link into `.agents/` or `.prompts/` by path.

---

## 7. Priority-ordered punch list

1. **Add YAML frontmatter (`name`, `description`) to every agent and skill file.** This is the single change that flips the repo from invisible-to-Claude to discoverable. Without it, nothing else matters. (13 agents + 8 skills = 21 edits.)
2. **Move files out of dot-prefixed paths:** `.agents/` → `.claude/agents/`, `.skills/` → `.claude/skills/`, `.prompts/` → `.claude/commands/`. Drop the leading dot on agent filenames.
3. **Fix `.helcom-agent.md`:** it's a VocPrez prompt, not an agent. Move to `.claude/commands/vocprez-annotation.md`. Remove `model: GPT-4o`. Replace `{{selection}}` with `$ARGUMENTS`.
4. **Consolidate duplicate agents:** merge `marine-data-agent` and `gis-marine-data-specialist` (or clearly differentiate them in `description:`). The current wording gives Claude no basis to pick one over the other.
5. **Add `CLAUDE.md`** at the repo root with repo intent, bblock structure, build process, and agent/skill pointers.
6. **Declare `tools:` allowlists** on each agent — orchestrators get wide access; converters and validators get narrow access.
7. **Rewrite `@agent ...` invocation examples** in agents, prompts, and guides to use natural-language requests (for agents) or `$ARGUMENTS` (for commands).
8. **Update cross-references** in `.guides/`, `.docs/`, and `.metadata-generation-ecosystem.md` to the new paths.
9. **Rename the colliding `geojson-to-jsonfg-converter`** skill to disambiguate from the agent of the same name.
10. **Optional: extract Python helpers** from `csv-to-metadata/SKILL.md` and `geojson-to-jsonfg-converter/SKILL.md` into executable scripts under their skill folders so Claude can run them via Bash rather than copy-pasting.

Items 1–3 are enough to make the repo functionally Claude-compliant; 4–10 are quality improvements that raise auto-triggering accuracy and reduce user-visible rough edges.
