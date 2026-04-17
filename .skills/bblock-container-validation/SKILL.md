# OGC Building Block Container Validation Skill

## Purpose

Validate OGC building blocks locally using Docker containers to ensure schema compliance, semantic consistency, and test coverage before publishing.

## Setup

### Prerequisites

- Docker installed and running
- OGC building block source files in `_sources/<block-name>/`
- Local copy of `bblocks-config.yaml`

### Docker Image

Uses the official OGC Building Blocks postprocessor image:
```bash
docker pull ogcincubator/bblocks-postprocess:latest
```

## Validation Commands

### 1. Local Build and Validation

```bash
# From the repository root
docker run --rm \
  -v $(pwd):/workspace \
  -w /workspace \
  ogcincubator/bblocks-postprocess:latest \
  python -m bblocks.process_config . --split-docs --base-url=http://localhost
```

This command:
- Mounts the workspace
- Runs the building block post-processor
- Generates `build-local/` artifacts
- Performs schema validation, context validation, and example validation

### 2. Validate Specific Building Block

```bash
docker run --rm \
  -v $(pwd):/workspace \
  -w /workspace \
  ogcincubator/bblocks-postprocess:latest \
  python -m bblocks.process_config . \
    --split-docs \
    --base-url=http://localhost \
    --id 'ogc.hosted.iliad.api.features.<block-name>'
```

### 3. Run Schema Validation Only

```bash
docker run --rm \
  -v $(pwd):/workspace \
  -w /workspace \
  ogcincubator/bblocks-postprocess:latest \
  python -c "
from bblocks import validate_schemas
validate_schemas('_sources/<block-name>')
"
```

### 4. Validate Examples Against Schema

```bash
docker run --rm \
  -v $(pwd):/workspace \
  -w /workspace \
  ogcincubator/bblocks-postprocess:latest \
  python -c "
from bblocks import validate_examples
validate_examples('_sources/<block-name>')
"
```

## Validation Checks

The container runs automatic checks for:

- **Structure**: Required files present (bblock.json, description.md, schema.json, context.jsonld, examples.yaml)
- **JSON Schema**: schema.json/yaml valid JSON schema, no syntax errors
- **JSON-LD Context**: context.jsonld valid JSON-LD, proper @id mappings
- **Examples**: Example files valid GeoJSON, conform to schema
- **Test Suites**: tests/*.yaml executed successfully
- **Semantic Consistency**: context entries reference authoritative vocabularies
- **Provenance**: provenance_urls and metadata documented

## Output

Validation generates:

- `build-local/` artifacts (HTML docs, JSON schemas, RDF)
- Validation report with errors, warnings, and suggestions
- Schema compliance summary
- Coverage report for context mappings

## Troubleshooting

### Docker Not Available

Install Docker:
- macOS: https://docs.docker.com/desktop/install/mac-install/
- Linux: https://docs.docker.com/engine/install/
- Windows: https://docs.docker.com/desktop/install/windows-install/

### Validation Failures

Check:
1. Schema syntax: `python -m json.tool _sources/<block>/schema.json`
2. Context validity: `python -m json.tool _sources/<block>/context.jsonld`
3. Example format: `python -m json.tool _sources/<block>/examples/*.geojson`

### Memory Issues

Increase Docker memory limits:
```bash
docker run --rm --memory 2g -v $(pwd):/workspace ...
```

## Integration with Agents

Use this skill when:
- The validation agent needs to check building block compliance
- Building blocks are updated with new examples or properties
- Context.jsonld requires validation against examples
- Before committing building block changes to version control
- Preparing building blocks for publication
