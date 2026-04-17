# Validate Building Block with Container

Use this prompt to validate OGC building blocks locally using Docker containers.

## Quick Start

```
@validation-agent validate building block at _sources/<building-block-name>
```

## What Gets Validated

1. **Structure** - All required files present and correctly named
2. **Schema** - JSON Schema syntax and JSON-LD context validity
3. **Examples** - Example data conforms to schema
4. **Semantics** - All properties have context entries with authoritative vocabulary URIs
5. **Tests** - Test suites pass
6. **Provenance** - Metadata and source URLs documented

## Example Usage

```
@validation-agent validate building block at _sources/macroobservation using container
```

## Expected Output

- ✅ Structure check results
- ✅ Schema validation summary
- ✅ Example compliance report
- ✅ Context completeness analysis (missing vocabulary mappings)
- ✅ Test execution results
- ✅ Overall validation status (Pass/Warnings/Errors)

## Container Requirements

Requires Docker. If not available, the validation agent will provide setup instructions.

## Related Skills

- `bblock-container-validation` - Container-based validation commands and troubleshooting
