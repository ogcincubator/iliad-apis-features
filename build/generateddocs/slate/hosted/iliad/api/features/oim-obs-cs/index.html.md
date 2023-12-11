---
title: OIM Observations - Citizen Science (Schema)


toc_footers:
  - Version 0.1
  - <a href='#'>OIM Observations - Citizen Science</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: OIM Observations - Citizen Science (Schema)
---


# OIM Observations - Citizen Science `ogc.hosted.iliad.api.features.oim-obs-cs`

Defines observations and collections to implement the OIM SOSA cross-domain model in a form compatible with ILIAD and other digital twins using this model.

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong>valid</strong>
</aside>

# Description

## Ocean Information Model Observations Profile for Citizen Science

Currently a stub where requirements for OIM implementation can be defined as required.

Note this will typically be combined with requirements for particular application domains needed to interoperate with external systems.
# Examples

## Oceans Information Model examples

TBD - see specific sub-profile for examples.


# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
description: Schemas for Ocean Information Model Observations
comment: This is a stub for now - with simple proxies for each object where schemas
  can be specialised.
$defs:
  OIMObsProps:
    allOf:
    - $ref: ../oim-obs/schema.yaml#/$defs/OIMObsProps
    - properties:
        sampleSizeValue:
          type: string
          x-jsonld-id: http://w3id.org/iliad/property/sampleSizeValue
        speciesScientificName:
          type: string
          x-jsonld-id: http://w3id.org/iliad/property/speciesScientificName
        wormsConcept:
          type: string
          pattern: ^https://marinespecies\.org/.*
          x-jsonld-id: http://w3id.org/iliad/property/wormsConcept
          x-jsonld-type: '@id'
  OIMObsFeature:
    allOf:
    - $ref: ../oim-obs/schema.yaml#/$defs/OIMObsFeature
    - properties:
        properties:
          $ref: '#/$defs/OIMObsProps'
  OIMObsCollection:
    allOf:
    - $ref: ../oim-obs/schema.yaml#/$defs/OIMObsCollection
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
x-jsonld-prefixes:
  iliad: http://w3id.org/iliad/property/

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Fannotated%2Fhosted%2Filiad%2Fapi%2Ffeatures%2Foim-obs-cs%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-obs-cs/schema.yaml" target="_blank">https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-obs-cs/schema.yaml</a>
* JSON version: <a href="https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-obs-cs/schema.json" target="_blank">https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-obs-cs/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "resultTime": "sosa:resultTime",
    "phenomenonTime": "sosa:phenomenonTime",
    "hasFeatureOfInterest": {
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
    "hasResult": "sosa:hasResult",
    "hasSimpleResult": "sosa:hasSimpleResult",
    "Observation": "sosa:Observation",
    "Sample": "sosa:Sample",
    "System": "sosa:System",
    "Platform": "sosa:Platform",
    "id": "@id",
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
      "@type": "@id",
      "@container": "@set"
    },
    "isHostedBy": "sosa:isHostedBy",
    "isProxyFor": "sosa:isProxyFor",
    "wasOriginatedBy": "sosa:wasOriginatedBy",
    "detects": "sosa:detects",
    "hasProperty": "sosa:hasProperty",
    "isPropertyOf": "sosa:isPropertyOf",
    "forProperty": "sosa:forProperty",
    "implements": "sosa:implements",
    "implementedBy": "sosa:implementedBy",
    "hasInput": "sosa:hasInput",
    "hasOutput": "sosa:hasOutput",
    "hasSubSystem": {
      "@id": "sosa:hasSubSystem",
      "@type": "@id",
      "@container": "@set"
    },
    "deployedSystem": "sosa:deployedSystem",
    "hasDeployment": "sosa:hasDeployment",
    "deployedOnPlatform": "sosa:deployedOnPlatform",
    "inDeployment": "sosa:inDeployment",
    "inCondition": "ssn-system:inCondition",
    "hasSystemCapability": "ssn-system:hasSystemCapability",
    "hasSystemProperty": "ssn-system:hasSystemProperty",
    "hasOperatingRange": "ssn-system:hasOperatingRange",
    "hasOperatingProperty": "ssn-system:hasOperatingProperty",
    "hasSurvivalRange": "ssn-system:hasSurvivalRange",
    "hasSurvivalProperty": "ssn-system:hasSurvivalProperty",
    "qualityOfObservation": "ssn-system:qualityOfObservation",
    "hasMember": {
      "@context": {},
      "@id": "sosa:hasMember"
    },
    "features": {
      "@context": {
        "features": {
          "@container": "@set",
          "@id": "geojson:features"
        }
      },
      "@container": "@set",
      "@id": "sosa:hasMember"
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
    "geojson": "https://purl.org/geojson/vocab#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Fannotated%2Fhosted%2Filiad%2Fapi%2Ffeatures%2Foim-obs-cs%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-obs-cs/context.jsonld" target="_blank">https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-obs-cs/context.jsonld</a>

# Validation

## SHACL Shapes

The following sets of SHACL shapes are used for validating this building block:

* OIM Observations <small><code>ogc.hosted.iliad.api.features.oim-obs</code></small>
  * [https://ogcincubator.github.io/iliad-apis-features/_sources/oim-obs/rules.shacl](https://ogcincubator.github.io/iliad-apis-features/_sources/oim-obs/rules.shacl)
* SOSA Observation <small><code>ogc.unstable.sosa.properties.observation</code></small>
  * [https://opengeospatial.github.io/ogcapi-sosa/_sources/properties/observation/rules.shacl](https://opengeospatial.github.io/ogcapi-sosa/_sources/properties/observation/rules.shacl)

# References

* [Reference to ILIAD](https://example.com/sources/1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/ogcincubator/iliad-apis-features" target="_blank">https://github.com/ogcincubator/iliad-apis-features</a>
* Path:
<code><a href="https://github.com/ogcincubator/iliad-apis-features/blob/HEAD/_sources/oim-obs-cs" target="_blank">_sources/oim-obs-cs</a></code>

