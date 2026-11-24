## APKG Metadata Application Profile

This building block captures the Application Package Metadata Application Profile (APKG-MAP) published in the `ILIAD-ocean-twin/APKG` repository.

It models:

- application packages as software applications and source code assets
- registries, organisations, postal addresses, and people
- CWL-aligned processes and parameters
- temporal coverage and spatial geometry
- distribution links and secret input declarations

This block does not define its own ontology. It reuses the upstream APKG vocabulary (`terms/apkg-ms.ttl`, namespace `http://w3id.org/apkg/terms#`) together with standard schema.org, Dublin Core, DCAT and OWL-Time properties, and adds SHACL constraints on top of it.
