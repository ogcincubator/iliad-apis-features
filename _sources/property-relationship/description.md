# SeaDOTs Property Relationship

This draft building block represents a directed, weighted relationship between two indicator or observed-property URIs.

It is intended to replace ad hoc `ses:Edge` structures in new SeaDOTs material with a reusable `prop-rel:PropertyRelationship` shape. Each relationship can include:

- source and target properties (`fromProperty`, `toProperty`)
- a signed weight in `[-1, 1]`
- evidence and explanation
- model and experiment provenance

In impact-assessment cases, this block forms the relationship layer between OIM variables.
