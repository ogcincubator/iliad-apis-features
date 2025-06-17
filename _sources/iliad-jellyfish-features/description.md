## Iliad Jellyfish Pilot OGC API Features profile

This specification defines the specific requirements of the ILIAD Jellyfish Pilot as an implementation of the Oceans Information Model.

Constraints that are not unique to the pilot should be described in one of the "parent" profiles in the chain:

- [OIM Observations for Citizen Science](../oim-obs-cs/)
- [OIM Observations](../oim-obs/)
- [OGC-API SOSA](https://opengeospatial.github.io/ogcapi-sosa/)

Note the source for the mapping to the semantic model is the context:
https://raw.githubusercontent.com/ILIAD-ocean-twin/OIM/refs/heads/main/extensions/jsonld/jellyfish-context.jsonld

however this context contains many other elements not specific to this application, so a clean subset is defined in [context.jsonld] .

Using the building blocks these common elements are inherited from the dependencies on the OIM model, allowing transparency around common usage and maintenance in a single location.

## Key features of this profile:

- a schema for the hasResult element of observations
- a JSON-LD context for this result schema
- JSON-LD context elements defining namespaces for values specific to the pilot context:
- inheritance from common OIM components and broader biodiversity domain standards.

e.g. 
```"observedProperty": {
      "@id": "sosa:observedProperty",
      "@type": "@id",
      "@context": {
        "@base": "https://w3id.org/iliad/jellyfish/property/"
      }
    },
```

## Future work
This profile defines Features for use in OGCAPI Features, and will be part of a suite of options binding alternative APIs to the same information model.

The SHACL rules (and any other validators developed) will be tested against the semantic annotations of each alternative to demonstrate (and help develop) these to be consistent, thus achieving **schema-agnostic semantic interoperability**.
  
  - see the [README](/README.md) for more information.
