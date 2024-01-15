
# Observations - ILIAD Jellyfish Pilot for Citizen Science (Schema)

`ogc.hosted.iliad.api.features.iliad-jellyfish` *v0.1*

Defines a project profile of the ILIAD Citizen Science profile for Observations in accordance with the Oceans Information Model

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Ocean Information Model Observations Profile for Citizen Science - Jellyfish Pilot

This specification defines the specific requirements of the ILIAD Jellyfish Pilot as an implementation of the Oceans Information Model.

Constraints that are not unique to the pilot should be described in one of the "parent" profiles in the chain:

- [OIM Observations for Citizen Science](../oim-obs-cs/)
- [OIM Observations](../oim-obs/)
- [OGC-API SOSA](https://opengeospatial.github.io/ogcapi-sosa/)

## Key features of this profile:

- a schema for the hasResult element of observations
- a JSON-LD context for this result schema
- JSON-LD context elements defining namespaces for values specific to the pilot context:

e.g. 
```"observedProperty": {
      "@id": "sosa:observedProperty",
      "@type": "@id",
      "@context": {
        "@base": "http://w3id.org/iliad/jellyfish/property/"
      }
    },
```

## Future work
This profile defines Features for use in OGCAPI Features, and will be part of a suite of options bding alternative APIs to the same information model.

The SHACL rules (and any other validators developed) will be tested against the semantic annotations of each alternative to demonstrate (and help develop) these to be consistent, thus achieving **schema-agnostic semantic interoperability**.
  
  - see the [README](https://github.com/ogcincubator/iliad-apis-features/blob/master/README.md) for more information.

## Examples

### Example of Jellyfish abundance observation
#### json
```json
{
  "@id": "1-18-527-Phyllorhiza_punctata",
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
  "@id": "1-18-527-Phyllorhiza_punctata",
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
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix iliad: <http://w3id.org/iliad/property/> .
@prefix jf-density: <http://w3id.org/iliad/jellyfish/property/densityOfJF/> .
@prefix jf-property: <http://w3id.org/iliad/jellyfish/property/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata> a sosa:Observation,
        geojson:Feature ;
    rdfs:label "Jelly fish observation #1 location id: 18 sensor: 527 species: Phyllorhiza punctata"@en ;
    sosa:hasFeatureOfInterest <http://w3id.org/iliad/jellyfish/feature/1-18> ;
    sosa:hasResult [ jf-property:beachedJF "1" ;
            jf-property:densityOfJF jf-density:Some ;
            jf-property:quantityOfJF 50 ;
            jf-property:stingByJF "Unspecified" ;
            iliad:sampleSizeValue "10-30" ;
            iliad:speciesScientificName "Phyllorhiza punctata" ;
            iliad:wormsConcept <https://marinespecies.org/aphia.php?p=taxdetails&id=135298> ] ;
    sosa:observedProperty jf-property:jellyFishAbundanceProperty ;
    sosa:phenomenonTime <2011-07-01t09:00:00> ;
    sosa:resultTime "2011-07-01T09:00:00" ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 3.180691e+01 3.463478e+01 ) ] .


```


### Example of Jellyfish abundance observation collection
#### json
```json
{
  "type": "FeatureCollection",
  "featureType": "sosa:ObservationCollection",

  "features": [
    {
      "@id": "1-18-527-Phyllorhiza_punctata",
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
    },
    {
      "@id": "1-18-528-Phyllorhiza_punctata",
      "type": "Feature",
      "featureType": "sosa:Observation",
      "geometry": {
        "type": "Point",
        "coordinates": [
          35.643846, 34.273634
        ]
      },
      "properties": {
        "label": {
          "en": "Jelly fish observation #1 location id: 18 sensor: 528 species: Phyllorhiza punctata"
        },
        "phenomenonTime": "2011-07-01T09:00:00",
        "resultTime": "2011-07-01T09:00:00",
        "observedProperty": "jellyFishAbundanceProperty",
        "hasFeatureOfInterest": "1-18",
        "hasResult": {
          "densityOfJF": "Some",
          "quantityOfJF": 30,
          "sampleSizeValue": "1-10",
          "speciesScientificName": "Phyllorhiza punctata",
          "wormsConcept": "https://marinespecies.org/aphia.php?p=taxdetails&id=135298",
          "stingByJF": "Unspecified",
          "beachedJF": "0"
        }
      }
    }
  ]
}
```

#### jsonld
```jsonld
{
  "type": "FeatureCollection",
  "featureType": "sosa:ObservationCollection",
  "features": [
    {
      "@id": "1-18-527-Phyllorhiza_punctata",
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
      }
    },
    {
      "@id": "1-18-528-Phyllorhiza_punctata",
      "type": "Feature",
      "featureType": "sosa:Observation",
      "geometry": {
        "type": "Point",
        "coordinates": [
          35.643846,
          34.273634
        ]
      },
      "properties": {
        "label": {
          "en": "Jelly fish observation #1 location id: 18 sensor: 528 species: Phyllorhiza punctata"
        },
        "phenomenonTime": "2011-07-01T09:00:00",
        "resultTime": "2011-07-01T09:00:00",
        "observedProperty": "jellyFishAbundanceProperty",
        "hasFeatureOfInterest": "1-18",
        "hasResult": {
          "densityOfJF": "Some",
          "quantityOfJF": 30,
          "sampleSizeValue": "1-10",
          "speciesScientificName": "Phyllorhiza punctata",
          "wormsConcept": "https://marinespecies.org/aphia.php?p=taxdetails&id=135298",
          "stingByJF": "Unspecified",
          "beachedJF": "0"
        }
      }
    }
  ],
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/context.jsonld"
}
```

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix iliad: <http://w3id.org/iliad/property/> .
@prefix jf-property: <http://w3id.org/iliad/jellyfish/property/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata> a sosa:Observation,
        geojson:Feature ;
    rdfs:label "Jelly fish observation #1 location id: 18 sensor: 527 species: Phyllorhiza punctata"@en ;
    sosa:hasFeatureOfInterest <http://w3id.org/iliad/jellyfish/observation/1-18> ;
    sosa:hasResult [ iliad:sampleSizeValue "10-30" ;
            iliad:speciesScientificName "Phyllorhiza punctata" ;
            iliad:wormsConcept <https://marinespecies.org/aphia.php?p=taxdetails&id=135298> ] ;
    sosa:observedProperty jf-property:jellyFishAbundanceProperty ;
    sosa:phenomenonTime <2011-07-01t09:00:00> ;
    sosa:resultTime "2011-07-01T09:00:00" ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 3.180691e+01 3.463478e+01 ) ] .

<http://w3id.org/iliad/jellyfish/observation/1-18-528-Phyllorhiza_punctata> a sosa:Observation,
        geojson:Feature ;
    rdfs:label "Jelly fish observation #1 location id: 18 sensor: 528 species: Phyllorhiza punctata"@en ;
    sosa:hasFeatureOfInterest <http://w3id.org/iliad/jellyfish/observation/1-18> ;
    sosa:hasResult [ iliad:sampleSizeValue "1-10" ;
            iliad:speciesScientificName "Phyllorhiza punctata" ;
            iliad:wormsConcept <https://marinespecies.org/aphia.php?p=taxdetails&id=135298> ] ;
    sosa:observedProperty jf-property:jellyFishAbundanceProperty ;
    sosa:phenomenonTime <2011-07-01t09:00:00> ;
    sosa:resultTime "2011-07-01T09:00:00" ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 3.564385e+01 3.427363e+01 ) ] .

[] a sosa:ObservationCollection,
        geojson:FeatureCollection ;
    sosa:hasMember <http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata>,
        <http://w3id.org/iliad/jellyfish/observation/1-18-528-Phyllorhiza_punctata> .


```


### Example of Jellyfish abundance observation ontology
This TTL to be replaced by examples from the ontology development cycle.

Note that the structure of a sosa:Observation is still relevant.

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix iliad: <http://w3id.org/iliad/property/> .
@prefix jf-density: <http://w3id.org/iliad/jellyfish/property/densityOfJF/> .
@prefix jf-property: <http://w3id.org/iliad/jellyfish/property/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata> a sosa:Observation,
        geojson:Feature ;
    rdfs:label "Jelly fish observation #1 location id: 18 sensor: 527 species: Phyllorhiza punctata"@en ;
    sosa:hasFeatureOfInterest <http://w3id.org/iliad/jellyfish/feature/1-18> ;
    sosa:hasResult [ jf-property:beachedJF "1" ;
            jf-property:densityOfJF jf-density:Some ;
            jf-property:quantityOfJF 50 ;
            jf-property:stingByJF "Unspecified" ;
            iliad:sampleSizeValue "10-30" ;
            iliad:speciesScientificName "Phyllorhiza punctata" ;
            iliad:wormsConcept <https://marinespecies.org/aphia.php?p=taxdetails&id=135298> ] ;
    sosa:observedProperty jf-property:jellyFishAbundanceProperty ;
    sosa:phenomenonTime "2011-07-01T09:00:00" ;
    sosa:resultTime "2011-07-01T09:00:00" ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 3.180691e+01 3.463478e+01 ) ] .


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
              x-jsonld-id: http://w3id.org/iliad/jellyfish/property/quantityOfJF
            densityOfJF:
              type: string
              enum:
              - None
              - Some
              - Swarm
              - Few
              x-jsonld-id: http://w3id.org/iliad/jellyfish/property/densityOfJF
              x-jsonld-type: '@id'
              x-jsonld-base: http://w3id.org/iliad/jellyfish/property/densityOfJF/
            stingByJF:
              type: string
              x-jsonld-id: http://w3id.org/iliad/jellyfish/property/stingByJF
            beachedJF:
              type: string
              x-jsonld-id: http://w3id.org/iliad/jellyfish/property/beachedJF
          x-jsonld-id: sosa:hasResult
        hasFeatureOfInterest:
          $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
          x-jsonld-id: sosa:hasFeatureOfInterest
          x-jsonld-base: http://w3id.org/iliad/jellyfish/feature/
  OIMObsFeature:
    allOf:
    - $ref: ../oim-obs-cs/schema.yaml#/$defs/OIMObsFeature
    - properties:
        properties:
          $ref: '#/$defs/OIMObsProps'
  OIMObsCollection:
    allOf:
    - $ref: ../oim-obs-cs/schema.yaml#/$defs/OIMObsCollection
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
    x-jsonld-type: '@id'
    x-jsonld-context:
      '@base': http://w3id.org/iliad/jellyfish/property/
x-jsonld-prefixes:
  jf-property: http://w3id.org/iliad/jellyfish/property/
  jf-density: http://w3id.org/iliad/jellyfish/property/densityOfJF/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "resultTime": "sosa:resultTime",
    "phenomenonTime": {
      "@id": "sosa:phenomenonTime",
      "@type": "@id"
    },
    "hasFeatureOfInterest": {
      "@context": {
        "@base": "http://w3id.org/iliad/jellyfish/feature/"
      },
      "@id": "sosa:hasFeatureOfInterest",
      "@type": "@id"
    },
    "observedProperty": {
      "@context": {
        "@base": "http://w3id.org/iliad/jellyfish/property/"
      },
      "@id": "sosa:observedProperty",
      "@type": "@id"
    },
    "usedProcedure": {
      "@id": "sosa:usedProcedure",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "sosa:madeBySensor",
      "@type": "@id"
    },
    "hasResult": {
      "@context": {
        "quantityOfJF": "jf-property:quantityOfJF",
        "densityOfJF": {
          "@context": {
            "@base": "http://w3id.org/iliad/jellyfish/property/densityOfJF/"
          },
          "@id": "jf-property:densityOfJF",
          "@type": "@id"
        },
        "stingByJF": "jf-property:stingByJF",
        "beachedJF": "jf-property:beachedJF"
      },
      "@id": "sosa:hasResult"
    },
    "hasSimpleResult": "sosa:hasSimpleResult",
    "id": "@id",
    "ActuatableProperty": {
      "@id": "sosa:ActuatableProperty",
      "@type": "@id"
    },
    "Actuation": {
      "@id": "sosa:Actuation",
      "@type": "@id"
    },
    "Actuator": {
      "@id": "sosa:Actuator",
      "@type": "@id"
    },
    "Deployment": {
      "@id": "sosa:Deployment",
      "@type": "@id"
    },
    "FeatureOfInterest": {
      "@id": "sosa:FeatureOfInterest",
      "@type": "@id"
    },
    "Input": {
      "@id": "sosa:Input",
      "@type": "@id"
    },
    "ObservableProperty": {
      "@id": "sosa:ObservableProperty",
      "@type": "@id"
    },
    "Observation": {
      "@id": "sosa:Observation",
      "@type": "@id"
    },
    "Output": {
      "@id": "sosa:Output",
      "@type": "@id"
    },
    "Platform": {
      "@id": "sosa:Platform",
      "@type": "@id"
    },
    "Property": {
      "@id": "sosa:Property",
      "@type": "@id"
    },
    "Procedure ": {
      "@id": "sosa:Procedure",
      "@type": "@id"
    },
    "Result": {
      "@id": "sosa:Result",
      "@type": "@id"
    },
    "Sample": {
      "@id": "sosa:Sample",
      "@type": "@id"
    },
    "Sampler": {
      "@id": "sosa:Sampler",
      "@type": "@id"
    },
    "Sampling": {
      "@id": "sosa:Sampling",
      "@type": "@id"
    },
    "Sensor": {
      "@id": "sosa:Sensor",
      "@type": "@id"
    },
    "Stimulus": {
      "@id": "sosa:Stimulus",
      "@type": "@id"
    },
    "System": {
      "@id": "sosa:System",
      "@type": "@id"
    },
    "actsOnProperty": {
      "@id": "sosa:actsOnProperty",
      "@type": "@id"
    },
    "deployedOnPlatform": {
      "@id": "sosa:deployedOnPlatform",
      "@type": "@id"
    },
    "deployedSystem": {
      "@id": "sosa:deployedSystem",
      "@type": "@id"
    },
    "detects": {
      "@id": "sosa:detects",
      "@type": "@id"
    },
    "features": {
      "@id": "sosa:hasMember",
      "@type": "@id",
      "@context": {
        "features": {
          "@container": "@set",
          "@id": "geojson:features"
        },
        "hasFeatureOfInterest": {
          "@id": "sosa:hasFeatureOfInterest",
          "@type": "@id"
        },
        "hasResult": "sosa:hasResult"
      },
      "@container": "@set"
    },
    "forProperty": {
      "@id": "sosa:forProperty",
      "@type": "@id"
    },
    "hasDeployment": {
      "@id": "sosa:hasDeployment",
      "@type": "@id"
    },
    "hasInput": {
      "@id": "sosa:hasInput",
      "@type": "@id"
    },
    "hasMember": {
      "@id": "sosa:hasMember",
      "@type": "@id",
      "@context": {
        "hasFeatureOfInterest": {
          "@id": "sosa:hasFeatureOfInterest",
          "@type": "@id"
        },
        "hasResult": "sosa:hasResult"
      }
    },
    "hasOutput": {
      "@id": "sosa:hasOutput",
      "@type": "@id"
    },
    "hasProperty": {
      "@id": "sosa:hasProperty",
      "@type": "@id"
    },
    "hasSample": {
      "@id": "sosa:hasSample",
      "@type": "@id"
    },
    "hasSubSystem": {
      "@id": "sosa:hasSubSystem",
      "@type": "@id",
      "@container": "@set"
    },
    "hasUltimateFeatureOfInterest": {
      "@id": "sosa:hasUltimateFeatureOfInterest",
      "@type": "@id"
    },
    "hosts": {
      "@id": "sosa:hosts",
      "@type": "@id",
      "@container": "@set"
    },
    "implementedBy": {
      "@id": "sosa:implementedBy",
      "@type": "@id"
    },
    "implements": {
      "@id": "sosa:implements",
      "@type": "@id"
    },
    "inDeployment": {
      "@id": "sosa:inDeployment",
      "@type": "@id"
    },
    "isActedOnBy": {
      "@id": "sosa:isActedOnBy",
      "@type": "@id"
    },
    "isFeatureOfInterestOf": {
      "@id": "sosa:isFeatureOfInterestOf",
      "@type": "@id"
    },
    "isHostedBy": {
      "@id": "sosa:isHostedBy",
      "@type": "@id"
    },
    "isObservedBy": {
      "@id": "sosa:isObservedBy",
      "@type": "@id"
    },
    "isPropertyOf": {
      "@id": "sosa:isPropertyOf",
      "@type": "@id"
    },
    "isProxyFor": {
      "@id": "sosa:isProxyFor",
      "@type": "@id"
    },
    "isResultOf": {
      "@id": "sosa:isResultOf",
      "@type": "@id"
    },
    "isSampleOf": {
      "@id": "sosa:isSampleOf",
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
    "madeBySampler": {
      "@id": "sosa:madeBySampler",
      "@type": "@id"
    },
    "madeObservation": {
      "@id": "sosa:madeObservation",
      "@type": "@id"
    },
    "madeSampling": {
      "@id": "sosa:madeSampling",
      "@type": "@id"
    },
    "observes": {
      "@id": "sosa:observes",
      "@type": "@id"
    },
    "wasOriginatedBy": {
      "@id": "sosa:wasOriginatedBy",
      "@type": "@id"
    },
    "inCondition": {
      "@id": "ssn-system:inCondition",
      "@type": "@id"
    },
    "Condition": {
      "@id": "ssn-system:Condition",
      "@type": "@id"
    },
    "hasSystemCapability": {
      "@id": "ssn-system:hasSystemCapability",
      "@type": "@id"
    },
    "SystemCapability": {
      "@id": "ssn-system:SystemCapability",
      "@type": "@id"
    },
    "hasSystemProperty": {
      "@id": "ssn-system:hasSystemProperty",
      "@type": "@id"
    },
    "SystemProperty": {
      "@id": "ssn-system:SystemProperty",
      "@type": "@id"
    },
    "MeasurementRange": {
      "@id": "ssn-system:MeasurementRange",
      "@type": "@id"
    },
    "ActuationRange": {
      "@id": "ssn-system:ActuationRange",
      "@type": "@id"
    },
    "Accuracy": {
      "@id": "ssn-system:Accuracy",
      "@type": "@id"
    },
    "DetectionLimit": {
      "@id": "ssn-system:DetectionLimit",
      "@type": "@id"
    },
    "Drift": {
      "@id": "ssn-system:Drift",
      "@type": "@id"
    },
    "Frequency": {
      "@id": "ssn-system:Frequency",
      "@type": "@id"
    },
    "Latency": {
      "@id": "ssn-system:Latency",
      "@type": "@id"
    },
    "Precision": {
      "@id": "ssn-system:Precision",
      "@type": "@id"
    },
    "Resolution": {
      "@id": "ssn-system:Resolution",
      "@type": "@id"
    },
    "ResponseTime": {
      "@id": "ssn-system:ResponseTime",
      "@type": "@id"
    },
    "Selectivity": {
      "@id": "ssn-system:Selectivity",
      "@type": "@id"
    },
    "Sensitivity": {
      "@id": "ssn-system:Sensitivity",
      "@type": "@id"
    },
    "hasOperatingRange": {
      "@id": "ssn-system:hasOperatingRange",
      "@type": "@id"
    },
    "OperatingRange": {
      "@id": "ssn-system:OperatingRange",
      "@type": "@id"
    },
    "hasOperatingProperty": {
      "@id": "ssn-system:hasOperatingProperty",
      "@type": "@id"
    },
    "OperatingProperty": {
      "@id": "ssn-system:OperatingProperty",
      "@type": "@id"
    },
    "MaintenanceSchedule": {
      "@id": "ssn-system:MaintenanceSchedule",
      "@type": "@id"
    },
    "OperatingPowerRange": {
      "@id": "ssn-system:OperatingPowerRange",
      "@type": "@id"
    },
    "hasSurvivalRange": {
      "@id": "ssn-system:hasSurvivalRange",
      "@type": "@id"
    },
    "SurvivalRange": {
      "@id": "ssn-system:SurvivalRange",
      "@type": "@id"
    },
    "hasSurvivalProperty": {
      "@id": "ssn-system:hasSurvivalProperty",
      "@type": "@id"
    },
    "SurvivalProperty": {
      "@id": "ssn-system:SurvivalProperty",
      "@type": "@id"
    },
    "SystemLifetime": {
      "@id": "ssn-system:SystemLifetime",
      "@type": "@id"
    },
    "BatteryLifetime": {
      "@id": "ssn-system:BatteryLifetime",
      "@type": "@id"
    },
    "qualityOfObservation": {
      "@id": "ssn-system:qualityOfObservation",
      "@type": "@id"
    },
    "properties": "@nest",
    "featureType": "@type",
    "label": {
      "@id": "rdfs:label",
      "@container": "@language"
    },
    "sampleSizeValue": "iliad:sampleSizeValue",
    "speciesScientificName": "iliad:speciesScientificName",
    "wormsConcept": {
      "@id": "iliad:wormsConcept",
      "@type": "@id"
    },
    "type": "@type",
    "geometry": {
      "@context": {},
      "@id": "geojson:geometry"
    },
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "links": {
      "@context": {
        "href": {
          "@type": "@id",
          "@id": "oa:hasTarget"
        },
        "rel": {
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          },
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id"
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      },
      "@id": "rdfs:seeAlso"
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn-system": "ssn:systems/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "iliad": "http://w3id.org/iliad/property/",
    "jf-property": "http://w3id.org/iliad/jellyfish/property/",
    "jf-density": "jf-property:densityOfJF/",
    "geojson": "https://purl.org/geojson/vocab#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
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

