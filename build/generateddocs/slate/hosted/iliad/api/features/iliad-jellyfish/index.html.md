---
title: Observations - ILIAD Jellyfish Pilot for Citizen Science (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

toc_footers:
  - Version 0.1
  - <a href='#'>Observations - ILIAD Jellyfish Pilot for Citizen Science</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: Observations - ILIAD Jellyfish Pilot for Citizen Science (Schema)
---


# Observations - ILIAD Jellyfish Pilot for Citizen Science `ogc.hosted.iliad.api.features.iliad-jellyfish`

Defines a project profile of the ILIAD Citizen Science profile for Observations in accordance with the Oceans Information Model

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong><a href="https://github.com/ogcincubator/iliad-apis-features/blob/master/build/tests/hosted/iliad/api/features/iliad-jellyfish/" target="_blank">valid</a></strong>
</aside>

# Description

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

# Examples

## Example of Jellyfish abundance observation



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

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/iliad-apis-features/build/tests/hosted/iliad/api/features/iliad-jellyfish/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Ftests%2Fhosted%2Filiad%2Fapi%2Ffeatures%2Filiad-jellyfish%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




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

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/iliad-apis-features/build/tests/hosted/iliad/api/features/iliad-jellyfish/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Ftests%2Fhosted%2Filiad%2Fapi%2Ffeatures%2Filiad-jellyfish%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
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

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/iliad-apis-features/build/tests/hosted/iliad/api/features/iliad-jellyfish/example_1_1.ttl">Open in new window</a>
</blockquote>



## Example of Jellyfish abundance observation collection



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

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/iliad-apis-features/build/tests/hosted/iliad/api/features/iliad-jellyfish/example_2_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Ftests%2Fhosted%2Filiad%2Fapi%2Ffeatures%2Filiad-jellyfish%2Fexample_2_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




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

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/iliad-apis-features/build/tests/hosted/iliad/api/features/iliad-jellyfish/example_2_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Ftests%2Fhosted%2Filiad%2Fapi%2Ffeatures%2Filiad-jellyfish%2Fexample_2_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
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

<http://w3id.org/iliad/jellyfish/observation/1-18-528-Phyllorhiza_punctata> a sosa:Observation,
        geojson:Feature ;
    rdfs:label "Jelly fish observation #1 location id: 18 sensor: 528 species: Phyllorhiza punctata"@en ;
    sosa:hasFeatureOfInterest <http://w3id.org/iliad/jellyfish/feature/1-18> ;
    sosa:hasResult [ jf-property:beachedJF "0" ;
            jf-property:densityOfJF jf-density:Some ;
            jf-property:quantityOfJF 30 ;
            jf-property:stingByJF "Unspecified" ;
            iliad:sampleSizeValue "1-10" ;
            iliad:speciesScientificName "Phyllorhiza punctata" ;
            iliad:wormsConcept <https://marinespecies.org/aphia.php?p=taxdetails&id=135298> ] ;
    sosa:observedProperty jf-property:jellyFishAbundanceProperty ;
    sosa:phenomenonTime "2011-07-01T09:00:00" ;
    sosa:resultTime "2011-07-01T09:00:00" ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 3.564385e+01 3.427363e+01 ) ] .

[] a sosa:ObservationCollection,
        geojson:FeatureCollection ;
    geojson:features <http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata>,
        <http://w3id.org/iliad/jellyfish/observation/1-18-528-Phyllorhiza_punctata> .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/iliad-apis-features/build/tests/hosted/iliad/api/features/iliad-jellyfish/example_2_1.ttl">Open in new window</a>
</blockquote>



## Example of Jellyfish abundance observation ontology

This TTL to be replaced by examples from the ontology development cycle.

Note that the structure of a sosa:Observation is still relevant.




```turtle
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

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/iliad-apis-features/build/tests/hosted/iliad/api/features/iliad-jellyfish/example_3_1.ttl">Open in new window</a>
</blockquote>



# JSON Schema

```yaml--schema
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

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Fannotated%2Fhosted%2Filiad%2Fapi%2Ffeatures%2Filiad-jellyfish%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/schema.yaml" target="_blank">https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/schema.yaml</a>
* JSON version: <a href="https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/schema.json" target="_blank">https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "observedProperty": {
      "@id": "sosa:observedProperty",
      "@type": "@id",
      "@context": {
        "@base": "http://w3id.org/iliad/jellyfish/property/"
      }
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
    "hasFeatureOfInterest": {
      "@context": {
        "@base": "http://w3id.org/iliad/jellyfish/feature/"
      },
      "@id": "sosa:hasFeatureOfInterest",
      "@type": "@id"
    },
    "sampleSizeValue": "iliad:sampleSizeValue",
    "speciesScientificName": "iliad:speciesScientificName",
    "wormsConcept": {
      "@id": "iliad:wormsConcept",
      "@type": "@id"
    },
    "label": {
      "@id": "rdfs:label",
      "@container": "@language"
    },
    "resultTime": "sosa:resultTime",
    "phenomenonTime": "sosa:phenomenonTime",
    "usedProcedure": {
      "@id": "sosa:usedProcedure",
      "@type": "@id"
    },
    "madeBySensor": {
      "@id": "sosa:madeBySensor",
      "@type": "@id"
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
    "hasMember": {
      "@context": {
        "features": "sosa:hasMember"
      },
      "@id": "sosa:hasMember"
    },
    "features": {
      "@context": {
        "features": "sosa:hasMember"
      },
      "@id": "geojson:features",
      "@container": "@set"
    },
    "properties": "@nest",
    "featureType": "@type",
    "Feature": "geojson:Feature",
    "FeatureCollection": "geojson:FeatureCollection",
    "GeometryCollection": "geojson:GeometryCollection",
    "LineString": "geojson:LineString",
    "MultiLineString": "geojson:MultiLineString",
    "MultiPoint": "geojson:MultiPoint",
    "MultiPolygon": "geojson:MultiPolygon",
    "Point": "geojson:Point",
    "Polygon": "geojson:Polygon",
    "bbox": {
      "@container": "@list",
      "@id": "geojson:bbox"
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "type": "@type",
    "id": "@id",
    "links": {
      "@context": {
        "href": "oa:hasTarget",
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
    "geometry": "geojson:geometry",
    "jf-property": "http://w3id.org/iliad/jellyfish/property/",
    "jf-density": "jf-property:densityOfJF/",
    "iliad": "http://w3id.org/iliad/property/",
    "sosa": "http://www.w3.org/ns/sosa/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "ssn": "http://www.w3.org/ns/ssn/",
    "ssn-system": "ssn:systems/",
    "geojson": "https://purl.org/geojson/vocab#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Fannotated%2Fhosted%2Filiad%2Fapi%2Ffeatures%2Filiad-jellyfish%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/context.jsonld" target="_blank">https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/context.jsonld</a>

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
<code><a href="https://github.com/ogcincubator/iliad-apis-features/blob/HEAD/_sources/iliad-jellyfish" target="_blank">_sources/iliad-jellyfish</a></code>

