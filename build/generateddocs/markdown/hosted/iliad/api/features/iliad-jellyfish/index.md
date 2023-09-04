
# Observations - ILIAD Jellyfish Pilot for Citizen Science (Schema)

`ogc.hosted.iliad.api.features.iliad-jellyfish` *v0.1*

Defines a project profile of the ILIAD Citizen Science profile for Observations in accordance with the Oceans Information Model

[*Status*](http://www.opengis.net/def/status): Invalid

## Description

## Ocean Information Model Observations Profile for Citizen Science - Jellyfish Pilot

This specification defines the specific requirements of the ILIAD Jellyfish Pilot as an implementation of the Oceans Information Model.

Constraints that are not unique to the pilot should be described in one of the "parent" profiles in the chain.

Currently this is a stub 
## Examples

### Example of Jellyfish abundance observation
#### json
```json
{
  "@id": "1-18-527-Phyllorhiza punctata",
  "type": "Feature",
  "featureType": "sosa:Observation",
  "geometry": {
    "type": "Point",
    "coordinates": [
      31.806910,
      34.634776
    ]
  },
  "properties": {
    "label": {
      "en": "Jelly fish observation #1 location id: 18 sensor: 527 species: Phyllorhiza punctata"
    },
    "phenomenonTime": "2011-07-01T09:00:00",
    "resultTime": "2011-07-01T09:00:00",
    "observedProperty": "jellyFishAbundanceProperty",
    "hasFeatureOfInterest": "1-18",
    "hasResult": {
      "densityOfJF": "Some",
      "quantityOfJF": 50,
      "sampleSizeValue": "10-30",
      "speciesScientificName": "Phyllorhiza punctata",
      "wormsConcept": "https://marinespecies.org/aphia.php?p=taxdetails&id=135298",
      "stingByJF": "Unspecified",
      "beachedJF": "1"
    }
  }
}
```

#### jsonld
```jsonld
{
  "@id": "1-18-527-Phyllorhiza punctata",
  "type": "Feature",
  "featureType": "sosa:Observation",
  "geometry": {
    "type": "Point",
    "coordinates": [
      31.80691,
      34.634776
    ]
  },
  "properties": {
    "label": {
      "en": "Jelly fish observation #1 location id: 18 sensor: 527 species: Phyllorhiza punctata"
    },
    "phenomenonTime": "2011-07-01T09:00:00",
    "resultTime": "2011-07-01T09:00:00",
    "observedProperty": "jellyFishAbundanceProperty",
    "hasFeatureOfInterest": "1-18",
    "hasResult": {
      "densityOfJF": "Some",
      "quantityOfJF": 50,
      "sampleSizeValue": "10-30",
      "speciesScientificName": "Phyllorhiza punctata",
      "wormsConcept": "https://marinespecies.org/aphia.php?p=taxdetails&id=135298",
      "stingByJF": "Unspecified",
      "beachedJF": "1"
    }
  },
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/context.jsonld"
}
```

#### ttl
```ttl


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Schemas for Ocean Information Model Observations
$defs:
  OIMObsProps:
    allOf:
    - $ref: ../oim-obs-cs/schema.yaml#/$defs/OIMObsProps
    - properties:
        hasResult:
          type: object
          properties:
            quantityOfJF:
              type: integer
            densityOfJF:
              type: string
              enum:
              - None
              - Some
              - Swarm
              - Few
              x-jsonld-id: http://w3id.org/iliad/jellyfish/property/densityOfJF
              x-jsonld-base: http://w3id.org/iliad/jellyfish/property/densityOfJF/
            sampleSizeValue:
              type: string
            speciesScientificName:
              type: string
            wormsConcept:
              type: string
              pattern: ^https://marinespecies\.org/.*
            stingByJF:
              type: string
            beachedJF:
              type: string
          x-jsonld-id: sosa:hasResult
          x-jsonld-vocab: http://w3id.org/iliad/jellyfish/property/
  OIMObsFeature:
    allOf:
    - $ref: ../oim-obs-cs/schema.yaml#/$defs/OIMObsProps
    - properties:
        properties:
          $ref: '#/$defs/OIMObsProps'
  OIMObsCollection:
    allOf:
    - $ref: ../oim-obs-cs/schema.yaml#/$defs/OIMObsProps
    - properties:
        features:
          type: array
          items:
            allOf:
            - $ref: '#/$defs/OIMObsFeature'
anyOf:
- $ref: '#/$defs/OIMObsProps'
- $ref: '#/$defs/OIMObsFeature'
- $ref: '#/$defs/OIMObsCollection'
x-jsonld-extra-terms:
  observedProperty:
    x-jsonld-id: sosa:observedProperty
    x-jsonld-context:
      '@base': http://w3id.org/iliad/jellyfish/property/
  hasFeatureOfInterest:
    x-jsonld-id: sosa:hasFeatureOfInterest
    x-jsonld-context:
      '@base': http://w3id.org/iliad/jellyfish/feature/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "resultTime": "sosa:resultTime",
    "phenomenonTime": "sosa:phenomenonTime",
    "hasFeatureOfInterest": {
      "@id": "sosa:hasFeatureOfInterest",
      "@type": "@id"
    },
    "observedProperty": "sosa:observedProperty",
    "usedProcedure": {
      "@id": "sosa:usedProcedure",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "sosa:madeBySensor",
      "@type": "@id"
    },
    "hasResult": {
      "@id": "sosa:hasResult",
      "@vocab": "http://w3id.org/iliad/jellyfish/property/",
      "@context": {
        "densityOfJF": {
          "@id": "http://w3id.org/iliad/jellyfish/property/densityOfJF",
          "@context": {
            "@base": {
              "@id": "http://w3id.org/iliad/jellyfish/property/densityOfJF/"
            }
          }
        }
      }
    },
    "hasSimpleResult": "sosa:hasSimpleResult",
    "Observation": "sosa:Observation",
    "Sample": "sosa:Sample",
    "observes": {
      "@id": "sosa:observes",
      "@type": "@id"
    },
    "isObservedBy": {
      "@id": "sosa:isObservedBy",
      "@type": "@id"
    },
    "madeObservation": {
      "@id": "sosa:madeObservation",
      "@type": "@id"
    },
    "actsOnProperty": {
      "@id": "sosa:actsOnProperty",
      "@type": "@id"
    },
    "isActedOnBy": {
      "@id": "sosa:isActedOnBy",
      "@type": "@id"
    },
    "madeActuation": {
      "@id": "sosa:madeActuation",
      "@type": "@id"
    },
    "madeByActuator": {
      "@id": "sosa:madeByActuator",
      "@type": "@id"
    },
    "hasSample": {
      "@id": "sosa:hasSample",
      "@type": "@id"
    },
    "isSampleOf": {
      "@id": "sosa:isSampleOf",
      "@type": "@id"
    },
    "madeSampling": {
      "@id": "sosa:madeSampling",
      "@type": "@id"
    },
    "madeBySampler": {
      "@id": "sosa:madeBySampler",
      "@type": "@id"
    },
    "isFeatureOfInterestOf": {
      "@id": "sosa:isFeatureOfInterestOf",
      "@type": "@id"
    },
    "isResultOf": "sosa:isResultOf",
    "hosts": {
      "@id": "sosa:hosts",
      "@type": "@id"
    },
    "isHostedBy": "sosa:isHostedBy",
    "isProxyFor": "ssn:isProxyFor",
    "wasOriginatedBy": "ssn:wasOriginatedBy",
    "detects": "ssn:detects",
    "hasProperty": "ssn:hasProperty",
    "isPropertyOf": "ssn:isPropertyOf",
    "forProperty": "ssn:forProperty",
    "implements": "ssn:implements",
    "implementedBy": "ssn:implementedBy",
    "hasInput": "ssn:hasInput",
    "hasOutput": "ssn:hasOutput",
    "hasSubSystem": "ssn:hasSubSystem",
    "deployedSystem": "ssn:deployedSystem",
    "hasDeployment": "ssn:hasDeployment",
    "deployedOnPlatform": "ssn:deployedOnPlatform",
    "inDeployment": "ssn:inDeployment",
    "inCondition": "ssn:systems/inCondition",
    "hasSystemCapability": "ssn:systems/hasSystemCapability",
    "hasSystemProperty": "ssn:systems/hasSystemProperty",
    "hasOperatingRange": "ssn:systems/hasOperatingRange",
    "hasOperatingProperty": "ssn:systems/hasOperatingProperty",
    "hasSurvivalRange": "ssn:systems/hasSurvivalRange",
    "hasSurvivalProperty": "ssn:systems/hasSurvivalProperty",
    "qualityOfObservation": "ssn:systems/qualityOfObservation",
    "hasMember": "sosa:hasMember",
    "features": "sosa:hasMember",
    "properties": "@nest",
    "featureType": "@type",
    "label": {
      "@id": "http://www.w3.org/2000/01/rdf-schema#label",
      "@container": "@language"
    },
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "ssn:systems/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/context.jsonld)

## Sources

* [Reference to ILIAD](https://example.com/sources/1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/iliad-apis-features](https://github.com/ogcincubator/iliad-apis-features)
* Path: `_sources/iliad-jellyfish`

