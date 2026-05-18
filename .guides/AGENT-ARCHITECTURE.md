# Agent Architecture & Integration Guide

## Overview

The repository uses grouped Claude agents under `.claude/agents/` plus skills under `.claude/skills/` and slash commands under `.claude/commands/`.

```text
User request
  -> slash command or direct agent
      -> integrator agents for routing/discovery
      -> converter/generator/validator agents for concrete outputs
      -> skills for focused local capabilities
```

## Groups

| Group | Path | Role |
|---|---|---|
| Integrator | `.claude/agents/integrator/` | Own workflow routing, marine discovery, usability checks, and cross-block coordination. |
| Converters | `.claude/agents/converters/` | Own STAC/DCAT/CSV/JSON-FG metadata and format conversion. |
| Generators | `.claude/agents/generators/` | Own OGC building block package authoring. |
| Validators | `.claude/agents/validators/` | Own static bblock validation and pygeoapi runtime tests. |

## Primary Flows

### Discovery to Building Block

```text
marine-content-specialist
  -> marine-data-agent
  -> building-block-generator
  -> validation-agent
```

### Metadata Generation

```text
metadata-dispatcher
  -> stac-metadata-generator
  -> dcat-metadata-generator
  -> csv-to-stac-converter / csv-to-dcat-converter
```

### Runtime Rendering Validation

```text
pygeoapi-test-harness
  -> pygeoapi-config-generator
  -> pygeoapi-local-runner
  -> response-schema-validator
  -> context-completeness-checker
```

## Current Agent Index

See `.claude/agents/README.md` for the canonical path table.

## Design Rules

- Keep agent names stable even when files move between groups.
- Cross-reference agents by both `name` and path when editing docs.
- Let integrator agents route; let converter/generator/validator agents own concrete artifacts.
- Prefer skills for reusable capabilities shared by multiple agents.
