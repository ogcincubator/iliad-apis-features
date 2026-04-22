---
description: Add DCAT and SKOS annotations to RDF/Turtle for VocPrez/Prez UI visibility
argument-hint: <turtle-content-or-path>
---

Add DCAT and SKOS annotations to the RDF/Turtle in `$ARGUMENTS` so it is fully browsable in the VocPrez UI.

`$ARGUMENTS` may be a file path to a `.ttl` file, or inline Turtle content.

## Requirements

1. **Prez catalog**: ensure the `prez` prefix is imported and used for the catalog entry.
2. **Catalog Entry**: create a `dcat:Catalog` instance if one doesn't exist and link the `skos:ConceptScheme` via `dcat:dataset` or `dcterms:hasPart`.
3. **Top Concepts**: identify all primary `skos:Concept` instances and link them to the `skos:ConceptScheme` using `skos:hasTopConcept`.
4. **Hierarchy Integrity**: ensure every concept has `skos:inScheme` and a `skos:prefLabel`.
5. **Prez Compatibility**: ensure the classes `skos:ConceptScheme` and `skos:Concept` are explicitly assigned to relevant entities.

## Output Format

Return the full updated Turtle (`.ttl`) content including the new annotations. Use inline comments to mark additions clearly.

## Examples

```
/vocprez-annotation /path/to/vocabulary.ttl
/vocprez-annotation _sources/my-block/ontology.ttl
```

If `$ARGUMENTS` is empty, ask the user to provide a Turtle file path or paste Turtle content directly.
