
# OIM Observations (Schema)

`ogc.hosted.iliad.api.features.oim-obs` *v0.1*

Defines observations and collections to implement the OIM SOSA cross-domain model in a form compatible with ILIAD and other digital twins using this model.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Ocean Information Model Observations Profile

Currently a stub where requirements for OIM implementation can be defined as required.

Note specific profiles will define specific requirements for interaction with external systems.

The JSON-LD Context declares the default baseURI of observableProperty to be the ILIAD Observable Properties Register.

TODO: (MVP)
1 - implement the observableProperties Register as a concept scheme under OGC hosted
2 - define a SHACL or other rule that requires observableProperties to be registered in the ILIAD observable properties register.

Note that it may have an externally resolvable URI or be a proxy handled by ILIAD (using the OGC RAINBOW)

The mechanisms for handling external vocabulary constraints to be define here: (TBD)
## Examples

### Oceans Information Model examples
TBD - see specific sub-profile for examples.
## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Schemas for Observations
$defs:
  OIMObsProps:
    allOf:
    - $ref: https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/properties/observation/schema.json
    - properties:
        label:
          oneOf:
          - type: string
          - type: object
          x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#label
          x-jsonld-container: '@language'
  OIMObsFeature:
    allOf:
    - $ref: https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/features/observation/schema.json
    - properties:
        properties:
          $ref: '#/$defs/OIMObsProps'
  OIMObsCollection:
    allOf:
    - $ref: https://opengeospatial.github.io/ogcapi-sosa/build/annotated/unstable/sosa/features/observationCollection/schema.json
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
  iliad: http://w3id.org/iliad/property/
  observedProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
    x-jsonld-type: '@id'
    x-jsonld-context:
      '@base': http://w3id.org/iliad/jellyfish/property/
x-jsonld-prefixes:
  sosa: http://www.w3.org/ns/sosa/
  rdfs: http://www.w3.org/2000/01/rdf-schema#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-obs/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-obs/schema.yaml)


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
    "hasResult": "sosa:hasResult",
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
    "features": {
      "@id": "sosa:hasMember",
      "@container": "@set",
      "@context": {
        "properties": {
          "@id": "@nest",
          "@context": {
            "features": "sosa:hasMember",
            "properties": "@nest"
          }
        },
        "features": {
          "@container": "@set",
          "@id": "geojson:features"
        },
        "Observation": "sosa:Observation",
        "Sample": "sosa:Sample",
        "observedProperty": "sosa:observedProperty",
        "phenomenonTime": "sosa:phenomenonTime",
        "hasResult": "sosa:hasResult",
        "isResultOf": "sosa:isResultOf",
        "hasSimpleResult": "sosa:hasSimpleResult",
        "resultTime": "sosa:resultTime",
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
        "featureType": "@type"
      }
    },
    "properties": {
      "@id": "@nest",
      "@context": {
        "features": "sosa:hasMember",
        "properties": "@nest"
      }
    },
    "featureType": "@type",
    "label": {
      "@id": "rdfs:label",
      "@container": "@language"
    },
    "type": "@type",
    "id": "@id",
    "geometry": {
      "@id": "geojson:geometry",
      "@context": {}
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
      "@id": "rdfs:seeAlso",
      "@context": {
        "href": "oa:hasTarget",
        "rel": {
          "@id": "http://www.iana.org/assignments/relation",
          "@type": "@id",
          "@context": {
            "@base": "http://www.iana.org/assignments/relation/"
          }
        },
        "type": "dct:type",
        "hreflang": "dct:language",
        "title": "rdfs:label",
        "length": "dct:extent"
      }
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "iliad": "http://w3id.org/iliad/property/",
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "ssn:systems/",
    "geojson": "https://purl.org/geojson/vocab#",
    "oa": "http://www.w3.org/ns/oa#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-obs/context.jsonld)

## Sources

* [Reference to ILIAD](https://example.com/sources/1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/iliad-apis-features](https://github.com/ogcincubator/iliad-apis-features)
* Path: `_sources/oim-obs`

