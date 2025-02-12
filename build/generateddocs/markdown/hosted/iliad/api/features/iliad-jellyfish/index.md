
# Observations - ILIAD Jellyfish Pilot for Citizen Science (Schema)

`ogc.hosted.iliad.api.features.iliad-jellyfish` *v0.1*

Defines a project specific interoperability profile of the ILIAD Citizen Science profile for Observations in accordance with the Oceans Information Model

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
        "@base": "https://w3id.org/iliad/jellyfish/property/"
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
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/context.jsonld",
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
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/iliad/oim/default-context/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix iliad: <https://w3id.org/iliad/property/> .
@prefix ns1: <https://saref.etsi.org/core/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata> a sosa:Observation,
        geojson:Feature ;
    rdfs:label "Jelly fish observation #1 location id: 18 sensor: 527 species: Phyllorhiza punctata"@en ;
    sosa:hasResult [ :beachedJF "1" ;
            :densityOfJF "Some" ;
            :quantityOfJF 50 ;
            :stingByJF "Unspecified" ;
            iliad:sampleSizeValue "10-30" ;
            iliad:speciesScientificName "Phyllorhiza punctata" ;
            iliad:wormsConcept <https://marinespecies.org/aphia.php?p=taxdetails&id=135298> ] ;
    sosa:observedProperty <https://w3id.org/iliad/jellyfish/property/jellyFishAbundanceProperty> ;
    sosa:phenomenonTime <2011-07-01T09:00:00> ;
    sosa:resultTime "2011-07-01T09:00:00" ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 3.180691e+01 3.463478e+01 ) ] ;
    ns1:hasFeatureOfInterest <https://w3id.org/iliad/jellyfish/observation/1-18> .


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
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/context.jsonld",
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
  ]
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/iliad/oim/default-context/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix iliad: <https://w3id.org/iliad/property/> .
@prefix ns1: <https://saref.etsi.org/core/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata> a sosa:Observation,
        geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 3.180691e+01 3.463478e+01 ) ] ;
    :properties [ rdfs:label "Jelly fish observation #1 location id: 18 sensor: 527 species: Phyllorhiza punctata"@en ;
            sosa:hasResult [ :beachedJF "1" ;
                    :densityOfJF "Some" ;
                    :quantityOfJF 50 ;
                    :stingByJF "Unspecified" ;
                    iliad:sampleSizeValue "10-30" ;
                    iliad:speciesScientificName "Phyllorhiza punctata" ;
                    iliad:wormsConcept <https://marinespecies.org/aphia.php?p=taxdetails&id=135298> ] ;
            sosa:observedProperty <https://w3id.org/iliad/jellyfish/property/jellyFishAbundanceProperty> ;
            sosa:phenomenonTime <2011-07-01T09:00:00> ;
            sosa:resultTime "2011-07-01T09:00:00" ;
            ns1:hasFeatureOfInterest <https://w3id.org/iliad/jellyfish/observation/1-18> ] .

<https://w3id.org/iliad/jellyfish/observation/1-18-528-Phyllorhiza_punctata> a sosa:Observation,
        geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 3.564385e+01 3.427363e+01 ) ] ;
    :properties [ rdfs:label "Jelly fish observation #1 location id: 18 sensor: 528 species: Phyllorhiza punctata"@en ;
            sosa:hasResult [ :beachedJF "0" ;
                    :densityOfJF "Some" ;
                    :quantityOfJF 30 ;
                    :stingByJF "Unspecified" ;
                    iliad:sampleSizeValue "1-10" ;
                    iliad:speciesScientificName "Phyllorhiza punctata" ;
                    iliad:wormsConcept <https://marinespecies.org/aphia.php?p=taxdetails&id=135298> ] ;
            sosa:observedProperty <https://w3id.org/iliad/jellyfish/property/jellyFishAbundanceProperty> ;
            sosa:phenomenonTime <2011-07-01T09:00:00> ;
            sosa:resultTime "2011-07-01T09:00:00" ;
            ns1:hasFeatureOfInterest <https://w3id.org/iliad/jellyfish/observation/1-18> ] .

[] a sosa:ObservationCollection,
        geojson:FeatureCollection ;
    sosa:hasMember <https://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata>,
        <https://w3id.org/iliad/jellyfish/observation/1-18-528-Phyllorhiza_punctata> .


```


### Example of Jellyfish abundance observation ontology
This TTL to be replaced by examples from the ontology development cycle.

Note that the structure of a sosa:Observation is still relevant.

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix iliad: <https://w3id.org/iliad/property/> .
@prefix jf-density: <https://w3id.org/iliad/jellyfish/property/densityOfJF/> .
@prefix jf-property: <https://w3id.org/iliad/jellyfish/property/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata> a sosa:Observation,
        geojson:Feature ;
    rdfs:label "Jelly fish observation #1 location id: 18 sensor: 527 species: Phyllorhiza punctata"@en ;
    sosa:hasFeatureOfInterest <https://w3id.org/iliad/jellyfish/feature/1-18> ;
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
    - $ref: https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-obs-cs/schema.yaml#/$defs/OIMObsProps
    - properties:
        hasResult:
          type: object
          properties:
            quantityOfJF:
              type: integer
              x-jsonld-id: https://w3id.org/iliad/oim/default-context/quantityOfJF
            densityOfJF:
              type: string
              enum:
              - None
              - Some
              - Swarm
              - Few
              x-jsonld-id: https://w3id.org/iliad/oim/default-context/densityOfJF
            stingByJF:
              type: string
              x-jsonld-id: https://w3id.org/iliad/oim/default-context/stingByJF
            beachedJF:
              type: string
              x-jsonld-id: https://w3id.org/iliad/oim/default-context/beachedJF
          x-jsonld-id: http://www.w3.org/ns/sosa/hasResult
        hasFeatureOfInterest:
          $ref: https://opengeospatial.github.io/bblocks/annotated-schemas/ogc-utils/iri-or-curie/schema.yaml
          x-jsonld-id: https://saref.etsi.org/core/hasFeatureOfInterest
          x-jsonld-type: '@id'
  OIMObsFeature:
    allOf:
    - $ref: https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-obs-cs/schema.yaml#/$defs/OIMObsFeature
    - properties:
        properties:
          $ref: '#/$defs/OIMObsProps'
          x-jsonld-id: https://w3id.org/iliad/oim/default-context/properties
  OIMObsCollection:
    allOf:
    - $ref: https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-obs-cs/schema.yaml#/$defs/OIMObsCollection
    - properties:
        features:
          type: array
          items:
            allOf:
            - $ref: '#/$defs/OIMObsFeature'
          x-jsonld-id: https://w3id.org/iliad/oim/default-context/features
anyOf:
- $ref: '#/$defs/OIMObsProps'
- $ref: '#/$defs/OIMObsFeature'
- $ref: '#/$defs/OIMObsCollection'
x-jsonld-extra-terms:
  strandedJellyfish: https://w3id.org/iliad/oim/ext/jellyfish/strandedJellyfish
  JellyFishAbundance: https://w3id.org/iliad/oim/ext/jellyfish/JellyFishAbundance
  affiliation: https://schema.org/affiliation
  distanceFromShore: https://w3id.org/iliad/oim/ext/jellyfish/distanceFromShore
  agentConfidence: https://w3id.org/iliad/oim/ext/jellyfish/agentConfidence
  versionInfo: http://www.w3.org/2002/07/owl#versionInfo
  maker: http://xmlns.com/foaf/0.1/maker
  stingByJellyFish: https://w3id.org/iliad/oim/ext/jellyfish/stingByJellyFish
  label: http://www.w3.org/2000/01/rdf-schema#label
  Result: http://www.w3.org/ns/sosa/Result
  homepage: http://xmlns.com/foaf/0.1/homepage
  creator: http://purl.org/dc/terms/creator
  name: https://schema.org/name
  rights: http://purl.org/dc/terms/rights
  HumanSensor: https://w3id.org/iliad/oim/ext/jellyfish/HumanSensor
  isDefinedBy: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
  title: http://purl.org/dc/terms/title
  seeAlso: http://www.w3.org/2000/01/rdf-schema#seeAlso
  comment: http://www.w3.org/2000/01/rdf-schema#comment
  contributor: http://purl.org/dc/terms/contributor
  description: http://purl.org/dc/terms/description
  distanceWalkedInMeters: https://w3id.org/iliad/oim/ext/jellyfish/distanceWalkedInMeters
  Sensor: http://www.w3.org/ns/sosa/Sensor
  type: '@type'
  PhotonFluxDensity: http://purl.oclc.org/NET/ssnx/qu/dim#PhotonFluxDensity
  implements: http://www.w3.org/ns/ssn/implements
  sampleSizeUnit: http://rs.tdwg.org/dwc/terms/sampleSizeUnit
  recordNumber: http://rs.tdwg.org/dwc/terms/recordNumber
  verbatimLongitude: http://rs.tdwg.org/dwc/terms/verbatimLongitude
  invalidatedAtTime: http://www.w3.org/ns/prov#invalidatedAtTime
  behavior: http://rs.tdwg.org/dwc/terms/behavior
  organismQuantity: http://rs.tdwg.org/dwc/terms/organismQuantity
  spatial: http://purl.org/dc/terms/spatial
  scientificNameID: http://rs.tdwg.org/dwc/terms/scientificNameID
  lowestBiostratigraphicZone: http://rs.tdwg.org/dwc/terms/lowestBiostratigraphicZone
  MultiLineString: http://www.opengis.net/ont/sf#MultiLineString
  Attachable: http://purl.org/linked-data/cube#Attachable
  earliestEonOrLowestEonothem: http://rs.tdwg.org/dwc/terms/earliestEonOrLowestEonothem
  originalNameUsageID: http://rs.tdwg.org/dwc/terms/originalNameUsageID
  GeologicalContext: http://rs.tdwg.org/dwc/terms/GeologicalContext
  countryCode: http://rs.tdwg.org/dwc/terms/countryCode
  UnitOfMeasure: https://saref.etsi.org/core/UnitOfMeasure
  verbatimCoordinates: http://rs.tdwg.org/dwc/terms/verbatimCoordinates
  recordType: http://mmisw.org/ont/ioos/marine_biogeography/recordType
  maximumDistanceAboveSurfaceInMeters: http://rs.tdwg.org/dwc/terms/maximumDistanceAboveSurfaceInMeters
  verbatimLocality: http://rs.tdwg.org/dwc/terms/verbatimLocality
  QuantityValue: http://qudt.org/schema/qudt/QuantityValue
  identificationReferences: http://rs.tdwg.org/dwc/terms/identificationReferences
  Unit: http://qudt.org/schema/qudt/Unit
  isControlledByDevice:
    x-jsonld-id: https://saref.etsi.org/core/isControlledByDevice
    x-jsonld-type: '@id'
  verbatimCoordinateSystem: http://rs.tdwg.org/dwc/terms/verbatimCoordinateSystem
  sampleLengthInMeters: http://mmisw.org/ont/ioos/marine_biogeography/sampleLengthInMeters
  measurementType: http://rs.tdwg.org/dwc/terms/measurementType
  sampleWidthInMeters: http://mmisw.org/ont/ioos/marine_biogeography/sampleWidthInMeters
  measurementAccuracy: http://rs.tdwg.org/dwc/terms/measurementAccuracy
  Line: http://www.opengis.net/ont/sf#Line
  member: http://rs.tdwg.org/dwc/terms/member
  genus: http://rs.tdwg.org/dwc/terms/genus
  coordinatePrecision: http://rs.tdwg.org/dwc/terms/coordinatePrecision
  weightInKg: http://mmisw.org/ont/ioos/marine_biogeography/weightInKg
  generatedAtTime: http://www.w3.org/ns/prov#generatedAtTime
  georeferencedDate: http://rs.tdwg.org/dwc/terms/georeferencedDate
  example: http://www.w3.org/2004/02/skos/core#example
  taxonomicStatus: http://rs.tdwg.org/dwc/terms/taxonomicStatus
  validFrom:
    x-jsonld-id: http://portele.de/ont/inspire/baseInspire#validFrom
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  SurfaceMediumMedium: http://purl.oclc.org/NET/ssnx/cf/cf-feature#SurfaceMediumMedium
  Slice: http://purl.org/linked-data/cube#Slice
  Humidity: https://saref.etsi.org/core/Humidity
  previousIdentifications: http://rs.tdwg.org/dwc/terms/previousIdentifications
  Concentration: http://purl.oclc.org/NET/ssnx/qu/dim#Concentration
  dataSet: http://purl.org/linked-data/cube#dataSet
  Period: http://def.seegrid.csiro.au/isotc211/iso19108/2002/temporal#Period
  startDayOfYear: http://rs.tdwg.org/dwc/terms/startDayOfYear
  componentAttachment: http://purl.org/linked-data/cube#componentAttachment
  Platform: http://www.w3.org/ns/sosa/Platform
  otherCatalogNumbers: http://rs.tdwg.org/dwc/terms/otherCatalogNumbers
  MachineObservation: http://rs.tdwg.org/dwc/terms/MachineObservation
  Relationship: https://uri.etsi.org/ngsi-ld/Relationship
  license: http://purl.org/dc/terms/license
  concept: http://purl.org/linked-data/cube#concept
  coordinateUncertaintyInMeters: http://rs.tdwg.org/dwc/terms/coordinateUncertaintyInMeters
  Deployment: http://www.w3.org/ns/ssn/Deployment
  MultiSurface: http://www.opengis.net/ont/sf#MultiSurface
  eventID: http://rs.tdwg.org/dwc/terms/eventID
  Organism: http://rs.tdwg.org/dwc/terms/Organism
  TemporalDuration: http://www.w3.org/2006/time#TemporalDuration
  identificationID: http://rs.tdwg.org/dwc/terms/identificationID
  recordedByID: http://rs.tdwg.org/dwc/terms/recordedByID
  dateCreated:
    x-jsonld-id: https://smartdatamodels.org/dateCreated
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  Identification: http://rs.tdwg.org/dwc/terms/Identification
  Procedure: http://www.w3.org/ns/sosa/Procedure
  WeatherObserved: https://smartdatamodels.org/dataModel.Weather/WeatherObserved
  quantificationUnit: http://mmisw.org/ont/ioos/marine_biogeography/quantificationUnit
  country: http://rs.tdwg.org/dwc/terms/country
  genericName: http://rs.tdwg.org/dwc/terms/genericName
  DiffusionCoefficient: http://purl.oclc.org/NET/ssnx/qu/dim#DiffusionCoefficient
  bibliographicCitation: http://purl.org/dc/terms/bibliographicCitation
  Organization: https://schema.org/Organization
  decimalLongitude: http://rs.tdwg.org/dwc/terms/decimalLongitude
  scientificName: http://rs.tdwg.org/dwc/terms/scientificName
  Volume: http://purl.oclc.org/NET/ssnx/qu/dim#Volume
  Thing: http://www.w3.org/2002/07/owl#Thing
  organismQuantityType: http://rs.tdwg.org/dwc/terms/organismQuantityType
  catalogNumber: http://rs.tdwg.org/dwc/terms/catalogNumber
  continent: http://rs.tdwg.org/dwc/terms/continent
  minimumDistanceAboveSurfaceInMeters: http://rs.tdwg.org/dwc/terms/minimumDistanceAboveSurfaceInMeters
  GFI_Feature: http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_Feature
  dateModified:
    x-jsonld-id: https://smartdatamodels.org/dateModified
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  decimalLatitude: http://rs.tdwg.org/dwc/terms/decimalLatitude
  references: http://purl.org/dc/terms/references
  AttributeProperty: http://purl.org/linked-data/cube#AttributeProperty
  agroVocConcept:
    x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/agroVocConcept
    x-jsonld-type: '@id'
  quantityValue: http://qudt.org/schema/qudt/quantityValue
  TemporalUnit: http://www.w3.org/2006/time#TemporalUnit
  higherGeographyID: http://rs.tdwg.org/dwc/terms/higherGeographyID
  addressRegion: https://schema.org/addressRegion
  hosts: http://www.w3.org/ns/sosa/hosts
  asWKT:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#asWKT
    x-jsonld-type: http://www.opengis.net/ont/geosparql#wktLiteral
  measurementDeterminedBy: http://rs.tdwg.org/dwc/terms/measurementDeterminedBy
  sampleShape: http://mmisw.org/ont/ioos/marine_biogeography/sampleShape
  hasOutput: http://www.w3.org/ns/ssn/hasOutput
  geodeticDatum: http://rs.tdwg.org/dwc/terms/geodeticDatum
  Angle: http://purl.oclc.org/NET/ssnx/qu/dim#Angle
  TemperatureDrift: http://purl.oclc.org/NET/ssnx/qu/dim#TemperatureDrift
  verbatimSiteDescriptions: http://rs.tdwg.org/hc/terms/verbatimSiteDescriptions
  RotationalSpeed: http://purl.oclc.org/NET/ssnx/qu/dim#RotationalSpeed
  FeatureOfInterest: http://www.w3.org/ns/sosa/FeatureOfInterest
  dataProvider: https://smartdatamodels.org/dataProvider
  ComponentProperty: http://purl.org/linked-data/cube#ComponentProperty
  maximumDepthInMeters: http://rs.tdwg.org/dwc/terms/maximumDepthInMeters
  measuresProperty:
    x-jsonld-id: https://saref.etsi.org/core/measuresProperty
    x-jsonld-type: '@id'
  Class: http://www.w3.org/2000/01/rdf-schema#Class
  ObservationCollection: http://www.w3.org/ns/sosa/ObservationCollection
  Geometry: http://www.opengis.net/ont/geosparql#Geometry
  locationAccordingTo: http://rs.tdwg.org/dwc/terms/locationAccordingTo
  depiction: http://xmlns.com/foaf/0.1/depiction
  nameAccordingTo: http://rs.tdwg.org/dwc/terms/nameAccordingTo
  Curve: http://www.opengis.net/ont/sf#Curve
  group: http://rs.tdwg.org/dwc/terms/group
  hasValue: https://saref.etsi.org/core/hasValue
  class: http://rs.tdwg.org/dwc/terms/class
  footprintWKT: http://rs.tdwg.org/dwc/terms/footprintWKT
  Instant: http://www.w3.org/2006/time#Instant
  FossilSpecimen: http://rs.tdwg.org/dwc/terms/FossilSpecimen
  snowHeight: https://smartdatamodels.org/dataModel.Weather/snowHeight
  Medium: http://purl.oclc.org/NET/ssnx/cf/cf-feature#Medium
  sfWithin: http://www.opengis.net/ont/geosparql#sfWithin
  ThermalConductivity: http://purl.oclc.org/NET/ssnx/qu/dim#ThermalConductivity
  typeStatus: http://rs.tdwg.org/dwc/terms/typeStatus
  acceptedNameUsage: http://rs.tdwg.org/dwc/terms/acceptedNameUsage
  hasUltimateFeatureOfInterest: http://www.w3.org/ns/sosa/hasUltimateFeatureOfInterest
  domainIncludes: https://schema.org/domainIncludes
  earliestEpochOrLowestSeries: http://rs.tdwg.org/dwc/terms/earliestEpochOrLowestSeries
  madeBySensor:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
    x-jsonld-type: '@id'
  long: http://www.w3.org/2003/01/geo/wgs84_pos#long
  ActuatableProperty: http://www.w3.org/ns/sosa/ActuatableProperty
  streamGauge: https://smartdatamodels.org/dataModel.Weather/streamGauge
  Feature: http://www.opengis.net/ont/geosparql#Feature
  parentNameUsageID: http://rs.tdwg.org/dwc/terms/parentNameUsageID
  dynamicProperties: http://rs.tdwg.org/dwc/terms/dynamicProperties
  LineString: http://www.opengis.net/ont/sf#LineString
  numericValue: http://qudt.org/schema/qudt/numericValue
  Wind: http://purl.oclc.org/NET/ssnx/cf/cf-feature#Wind
  caste: http://rs.tdwg.org/dwc/terms/caste
  footprintSpatialFit: http://rs.tdwg.org/dwc/terms/footprintSpatialFit
  namePublishedInYear: http://rs.tdwg.org/dwc/terms/namePublishedInYear
  highestBiostratigraphicZone: http://rs.tdwg.org/dwc/terms/highestBiostratigraphicZone
  fieldNotes: http://rs.tdwg.org/dwc/terms/fieldNotes
  measurementID: http://rs.tdwg.org/dwc/terms/measurementID
  parentNameUsage: http://rs.tdwg.org/dwc/terms/parentNameUsage
  acceptedNameUsageID: http://rs.tdwg.org/dwc/terms/acceptedNameUsageID
  maximumElevationInMeters: http://rs.tdwg.org/dwc/terms/maximumElevationInMeters
  visibilityInMeters: http://mmisw.org/ont/ioos/marine_biogeography/visibilityInMeters
  Concept: http://www.w3.org/2004/02/skos/core#Concept
  component: http://purl.org/linked-data/cube#component
  measure:
    x-jsonld-id: http://purl.org/linked-data/cube#measure
    x-jsonld-type: '@id'
  identificationVerificationStatus: http://rs.tdwg.org/dwc/terms/identificationVerificationStatus
  SliceKey: http://purl.org/linked-data/cube#SliceKey
  Measurement: https://saref.etsi.org/core/Measurement
  Location: http://purl.org/dc/terms/Location
  footprintSRS: http://rs.tdwg.org/dwc/terms/footprintSRS
  individualCount: http://rs.tdwg.org/dwc/terms/individualCount
  collectionCode: http://rs.tdwg.org/dwc/terms/collectionCode
  isHostedBy: http://www.w3.org/ns/sosa/isHostedBy
  lithostratigraphicTerms: http://rs.tdwg.org/dwc/terms/lithostratigraphicTerms
  subfamily: http://rs.tdwg.org/dwc/terms/subfamily
  eventType: http://rs.tdwg.org/dwc/terms/eventType
  Compressibility: http://purl.oclc.org/NET/ssnx/qu/dim#Compressibility
  associatedMedia: http://rs.tdwg.org/dwc/terms/associatedMedia
  Taxon: http://rs.tdwg.org/dwc/terms/Taxon
  vernacularName: http://rs.tdwg.org/dwc/terms/vernacularName
  windDirection: https://smartdatamodels.org/dataModel.Weather/windDirection
  inDeployment: http://www.w3.org/ns/ssn/inDeployment
  ComponentSet: http://purl.org/linked-data/cube#ComponentSet
  MassPerTimePerArea: http://purl.oclc.org/NET/ssnx/qu/dim#MassPerTimePerArea
  numericDuration: http://www.w3.org/2006/time#numericDuration
  ElectricConductivity: http://purl.oclc.org/NET/ssnx/qu/dim#ElectricConductivity
  preparations: http://rs.tdwg.org/dwc/terms/preparations
  Temperature: http://purl.oclc.org/NET/ssnx/qu/dim#Temperature
  Event: http://rs.tdwg.org/dwc/terms/Event
  observationLocation: http://mmisw.org/ont/ioos/marine_biogeography/observationLocation
  institutionID: http://rs.tdwg.org/dwc/terms/institutionID
  WeatherForecast: https://smartdatamodels.org/dataModel.Weather/WeatherForecast
  hasProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasProperty
    x-jsonld-type: '@id'
  verbatimDepth: http://rs.tdwg.org/dwc/terms/verbatimDepth
  Measure: http://def.seegrid.csiro.au/isotc211/iso19103/2005/basic#Measure
  Person: https://schema.org/Person
  Triangle: http://www.opengis.net/ont/sf#Triangle
  county: http://rs.tdwg.org/dwc/terms/county
  note: http://www.w3.org/2004/02/skos/core#note
  rightsHolder: http://purl.org/dc/terms/rightsHolder
  measurementMadeBy:
    x-jsonld-id: https://saref.etsi.org/core/measurementMadeBy
    x-jsonld-type: '@id'
  earliestEraOrLowestErathem: http://rs.tdwg.org/dwc/terms/earliestEraOrLowestErathem
  observationGroup: http://purl.org/linked-data/cube#observationGroup
  Interval: http://www.w3.org/2006/time#Interval
  occurrenceStatus: http://rs.tdwg.org/dwc/terms/occurrenceStatus
  LocationRelationship: https://uri.etsi.org/ngsi-ld/LocationRelationship
  EnergyFlux: http://purl.oclc.org/NET/ssnx/qu/dim#EnergyFlux
  StressOrPressure: http://purl.oclc.org/NET/ssnx/qu/dim#StressOrPressure
  observedMinLengthInCm: http://mmisw.org/ont/ioos/marine_biogeography/observedMinLengthInCm
  verbatimTaxonRank: http://rs.tdwg.org/dwc/terms/verbatimTaxonRank
  resultTime:
    x-jsonld-id: http://www.w3.org/ns/sosa/resultTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  disposition: http://rs.tdwg.org/dwc/terms/disposition
  visibility: https://smartdatamodels.org/dataModel.Weather/visibility
  namePublishedInID: http://rs.tdwg.org/dwc/terms/namePublishedInID
  Agent: http://xmlns.com/foaf/0.1/Agent
  dateIdentified: http://rs.tdwg.org/dwc/terms/dateIdentified
  ImageObject: https://schema.org/ImageObject
  organismRemarks: http://rs.tdwg.org/dwc/terms/organismRemarks
  latestPeriodOrHighestSystem: http://rs.tdwg.org/dwc/terms/latestPeriodOrHighestSystem
  Precipitation: http://purl.oclc.org/NET/ssnx/cf/cf-feature#Precipitation
  taxonRemarks: http://rs.tdwg.org/dwc/terms/taxonRemarks
  phenomenonTime: http://www.w3.org/ns/sosa/phenomenonTime
  georeferencedBy: http://rs.tdwg.org/dwc/terms/georeferencedBy
  Energy: http://purl.oclc.org/NET/ssnx/qu/dim#Energy
  Role: https://schema.org/Role
  hasSerialization: http://www.opengis.net/ont/geosparql#hasSerialization
  verbatimElevation: http://rs.tdwg.org/dwc/terms/verbatimElevation
  higherClassification: http://rs.tdwg.org/dwc/terms/higherClassification
  waterBody: http://rs.tdwg.org/dwc/terms/waterBody
  Layer: http://purl.oclc.org/NET/ssnx/cf/cf-feature#Layer
  hasTime: http://www.w3.org/2006/time#hasTime
  GeoProperty: https://uri.etsi.org/ngsi-ld/GeoProperty
  namePublishedIn: http://rs.tdwg.org/dwc/terms/namePublishedIn
  organismID: http://rs.tdwg.org/dwc/terms/organismID
  SF_SamplingFeature.sampledFeature: http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature.sampledFeature
  hasMember: http://www.w3.org/ns/sosa/hasMember
  stateProvince: http://rs.tdwg.org/dwc/terms/stateProvince
  rangeIncludes: https://schema.org/rangeIncludes
  hasInput: http://www.w3.org/ns/ssn/hasInput
  Mass: http://purl.oclc.org/NET/ssnx/qu/dim#Mass
  endDayOfYear: http://rs.tdwg.org/dwc/terms/endDayOfYear
  geologicalContextID: http://rs.tdwg.org/dwc/terms/geologicalContextID
  implementedBy: http://www.w3.org/ns/ssn/implementedBy
  pathway: http://rs.tdwg.org/dwc/terms/pathway
  verbatimSiteNames: http://rs.tdwg.org/hc/terms/verbatimSiteNames
  location: http://www.w3.org/2003/01/geo/wgs84_pos#location
  parentEventID: http://rs.tdwg.org/dwc/terms/parentEventID
  datasetName: http://rs.tdwg.org/dwc/terms/datasetName
  ComponentSpecification: http://purl.org/linked-data/cube#ComponentSpecification
  temperature: https://smartdatamodels.org/dataModel.Weather/temperature
  measurementMethod: http://rs.tdwg.org/dwc/terms/measurementMethod
  Scheme: http://www.w3.org/2004/02/skos/core#Scheme
  verbatimLatitude: http://rs.tdwg.org/dwc/terms/verbatimLatitude
  hasEnd:
    x-jsonld-id: http://www.w3.org/2006/time#hasEnd
    x-jsonld-type: '@id'
  GeometryCollection: http://www.opengis.net/ont/sf#GeometryCollection
  parentMeasurementID: http://rs.tdwg.org/dwc/terms/parentMeasurementID
  sightingCue: http://mmisw.org/ont/ioos/marine_biogeography/sightingCue
  waterTemperatureInCelsius: http://mmisw.org/ont/ioos/marine_biogeography/waterTemperatureInCelsius
  tribe: http://rs.tdwg.org/dwc/terms/tribe
  status: https://schema.org/status
  TemporalEntity: http://www.w3.org/2006/time#TemporalEntity
  hasBeginning:
    x-jsonld-id: http://www.w3.org/2006/time#hasBeginning
    x-jsonld-type: '@id'
  isResultOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isResultOf
    x-jsonld-type: '@id'
  SF_SamplingFeature: http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature
  DimensionProperty: http://purl.org/linked-data/cube#DimensionProperty
  alt: http://www.w3.org/2003/01/geo/wgs84_pos#alt
  superfamily: http://rs.tdwg.org/dwc/terms/superfamily
  sampleSizeValue: http://rs.tdwg.org/dwc/terms/sampleSizeValue
  Acceleration: http://purl.oclc.org/NET/ssnx/qu/dim#Acceleration
  identifier: http://purl.org/dc/terms/identifier
  LivingSpecimen: http://rs.tdwg.org/dwc/terms/LivingSpecimen
  visibilityType: http://mmisw.org/ont/ioos/marine_biogeography/visibilityType
  locationRemarks: http://rs.tdwg.org/dwc/terms/locationRemarks
  hasSubSystem: http://www.w3.org/ns/ssn/hasSubSystem
  Quantity: http://qudt.org/schema/qudt/Quantity
  MassFlowRate: http://purl.oclc.org/NET/ssnx/qu/dim#MassFlowRate
  QuantityKind: http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind
  Distance: http://purl.oclc.org/NET/ssnx/qu/dim#Distance
  higherGeography: http://rs.tdwg.org/dwc/terms/higherGeography
  informationWithheld: http://rs.tdwg.org/dwc/terms/informationWithheld
  dateObserved:
    x-jsonld-id: https://smartdatamodels.org/dateObserved
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  relatesToMeasurement:
    x-jsonld-id: https://saref.etsi.org/core/relatesToMeasurement
    x-jsonld-type: '@id'
  atmosphericPressure: https://smartdatamodels.org/dataModel.Weather/atmosphericPressure
  organismName: http://rs.tdwg.org/dwc/terms/organismName
  deprecated: http://www.w3.org/2002/07/owl#deprecated
  institutionCode: http://rs.tdwg.org/dwc/terms/institutionCode
  Radiance: http://purl.oclc.org/NET/ssnx/qu/dim#Radiance
  isMeasuredByDevice:
    x-jsonld-id: https://saref.etsi.org/core/isMeasuredByDevice
    x-jsonld-type: '@id'
  occurrenceID: http://rs.tdwg.org/dwc/terms/occurrenceID
  subject: http://purl.org/dc/terms/subject
  quantificationMethod: http://mmisw.org/ont/ioos/marine_biogeography/quantificationMethod
  measurementUnit: http://rs.tdwg.org/dwc/terms/measurementUnit
  lengthType: http://mmisw.org/ont/ioos/marine_biogeography/lengthType
  HumanObservation: http://rs.tdwg.org/dwc/terms/HumanObservation
  Duration: http://purl.oclc.org/NET/ssnx/qu/dim#Duration
  associatedSequences: http://rs.tdwg.org/dwc/terms/associatedSequences
  TIN: http://www.opengis.net/ont/sf#TIN
  phylum: http://rs.tdwg.org/dwc/terms/phylum
  fieldNumber: http://rs.tdwg.org/dwc/terms/fieldNumber
  relationshipRemarks: http://rs.tdwg.org/dwc/terms/relationshipRemarks
  infragenericEpithet: http://rs.tdwg.org/dwc/terms/infragenericEpithet
  SurfaceDensity: http://purl.oclc.org/NET/ssnx/qu/dim#SurfaceDensity
  sampleVolumeInCubicMeters: http://mmisw.org/ont/ioos/marine_biogeography/sampleVolumeInCubicMeters
  resourceRelationshipID: http://rs.tdwg.org/dwc/terms/resourceRelationshipID
  relationshipOfResource: http://rs.tdwg.org/dwc/terms/relationshipOfResource
  habitat: http://rs.tdwg.org/dwc/terms/habitat
  userName:
    x-jsonld-id: https://w3id.org/demeter/agri/agriCommon#userName
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  materialSampleID: http://rs.tdwg.org/dwc/terms/materialSampleID
  Point: http://www.w3.org/2003/01/geo/wgs84_pos#Point
  georeferenceVerificationStatus: http://rs.tdwg.org/dwc/terms/georeferenceVerificationStatus
  definition: http://www.w3.org/2004/02/skos/core#definition
  bed: http://rs.tdwg.org/dwc/terms/bed
  locality: http://rs.tdwg.org/dwc/terms/locality
  editorialNote: http://www.w3.org/2004/02/skos/core#editorialNote
  MaterialCitation: http://rs.tdwg.org/dwc/terms/MaterialCitation
  observes: http://www.w3.org/ns/sosa/observes
  samplingPerformedBy: http://rs.tdwg.org/hc/terms/samplingPerformedBy
  makesMeasurement:
    x-jsonld-id: https://saref.etsi.org/core/makesMeasurement
    x-jsonld-type: '@id'
  hasDeployment: http://www.w3.org/ns/ssn/hasDeployment
  associatedTaxa: http://rs.tdwg.org/dwc/terms/associatedTaxa
  measurementDeterminedDate: http://rs.tdwg.org/dwc/terms/measurementDeterminedDate
  eventDurationUnit: http://rs.tdwg.org/hc/terms/eventDurationUnit
  order: http://rs.tdwg.org/dwc/terms/order
  hasGeometry: http://www.opengis.net/ont/geosparql#hasGeometry
  vitality: http://rs.tdwg.org/dwc/terms/vitality
  minimumDepthInMeters: http://rs.tdwg.org/dwc/terms/minimumDepthInMeters
  usedProcedure: http://www.w3.org/ns/sosa/usedProcedure
  samplingEffort: http://rs.tdwg.org/dwc/terms/samplingEffort
  Property: https://saref.etsi.org/core/Property
  pressureTendency: https://smartdatamodels.org/dataModel.Weather/pressureTendency
  streetAddress: https://schema.org/streetAddress
  sfContains: http://www.opengis.net/ont/geosparql#sfContains
  Density: http://purl.oclc.org/NET/ssnx/qu/dim#Density
  LinearRing: http://www.opengis.net/ont/sf#LinearRing
  eventDate: http://rs.tdwg.org/dwc/terms/eventDate
  validTo:
    x-jsonld-id: http://portele.de/ont/inspire/baseInspire#validTo
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  Occurrence: http://rs.tdwg.org/dwc/terms/Occurrence
  year: http://rs.tdwg.org/dwc/terms/year
  family: http://rs.tdwg.org/dwc/terms/family
  inXSDDateTimeStamp: http://www.w3.org/2006/time#inXSDDateTimeStamp
  source: https://smartdatamodels.org/source
  eppoConcept:
    x-jsonld-id: https://w3id.org/demeter/agri/agriCommon#eppoConcept
    x-jsonld-type: '@id'
  georeferenceSources: http://rs.tdwg.org/dwc/terms/georeferenceSources
  MeasureProperty: http://purl.org/linked-data/cube#MeasureProperty
  resourceType: http://purl.org/dc/terms/type
  weatherType: https://smartdatamodels.org/dataModel.Weather/weatherType
  MaterialSample: http://rs.tdwg.org/dwc/terms/MaterialSample
  isMeasuredIn:
    x-jsonld-id: https://saref.etsi.org/core/isMeasuredIn
    x-jsonld-type: '@id'
  PropertyKind: http://purl.oclc.org/NET/ssnx/qu/qu#PropertyKind
  publisher: http://purl.org/dc/terms/publisher
  island: http://rs.tdwg.org/dwc/terms/island
  SpatialObject: http://www.opengis.net/ont/geosparql#SpatialObject
  sliceStructure: http://purl.org/linked-data/cube#sliceStructure
  dewPoint: https://smartdatamodels.org/dataModel.Weather/dewPoint
  NumberPerLength: http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerLength
  lat: http://www.w3.org/2003/01/geo/wgs84_pos#lat
  sightingDistanceInMeters: http://mmisw.org/ont/ioos/marine_biogeography/sightingDistanceInMeters
  taxonRank: http://rs.tdwg.org/dwc/terms/taxonRank
  VolumeFlowRate: http://purl.oclc.org/NET/ssnx/qu/dim#VolumeFlowRate
  SpecificEntropy: http://purl.oclc.org/NET/ssnx/qu/dim#SpecificEntropy
  locationID: http://rs.tdwg.org/dwc/terms/locationID
  TemporalProperty: https://uri.etsi.org/ngsi-ld/TemporalProperty
  CodedProperty: http://purl.org/linked-data/cube#CodedProperty
  identificationRemarks: http://rs.tdwg.org/dwc/terms/identificationRemarks
  modified: http://purl.org/dc/terms/modified
  eventDuration: http://rs.tdwg.org/hc/terms/eventDuration
  observedProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
    x-jsonld-type: '@id'
  associatedOrganisms: http://rs.tdwg.org/dwc/terms/associatedOrganisms
  sampleAreaInSquareMeters: http://mmisw.org/ont/ioos/marine_biogeography/sampleAreaInSquareMeters
  password:
    x-jsonld-id: https://w3id.org/demeter/agri/agriCommon#password
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  slice:
    x-jsonld-id: http://purl.org/linked-data/cube#slice
    x-jsonld-type: '@id'
  subgenus: http://rs.tdwg.org/dwc/terms/subgenus
  madeObservation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
    x-jsonld-type: '@id'
  observedMaxLengthInCm: http://mmisw.org/ont/ioos/marine_biogeography/observedMaxLengthInCm
  accessRights: http://purl.org/dc/terms/accessRights
  aphiaID: http://mmisw.org/ont/ioos/marine_biogeography/aphiaID
  relationshipOfResourceID: http://rs.tdwg.org/dwc/terms/relationshipOfResourceID
  siteCount: http://rs.tdwg.org/hc/terms/siteCount
  solarRadiation: https://smartdatamodels.org/dataModel.Weather/solarRadiation
  unit:
    x-jsonld-id: http://qudt.org/schema/qudt/unit
    x-jsonld-type: '@id'
  SurfaceMedium: http://purl.oclc.org/NET/ssnx/cf/cf-feature#SurfaceMedium
  date: http://purl.org/dc/terms/date
  isPropertyOf:
    x-jsonld-id: https://saref.etsi.org/core/isPropertyOf
    x-jsonld-type: '@id'
  sampleHeightInMeters: http://mmisw.org/ont/ioos/marine_biogeography/sampleHeightInMeters
  earliestAgeOrLowestStage: http://rs.tdwg.org/dwc/terms/earliestAgeOrLowestStage
  relativeHumidity: https://smartdatamodels.org/dataModel.Weather/relativeHumidity
  Entity: https://uri.etsi.org/ngsi-ld/Entity
  kingdom: http://rs.tdwg.org/dwc/terms/kingdom
  totalInSample: http://mmisw.org/ont/ioos/marine_biogeography/totalInSample
  latestEonOrHighestEonothem: http://rs.tdwg.org/dwc/terms/latestEonOrHighestEonothem
  taxonConceptID: http://rs.tdwg.org/dwc/terms/taxonConceptID
  islandGroup: http://rs.tdwg.org/dwc/terms/islandGroup
  ObservationGroup: http://purl.org/linked-data/cube#ObservationGroup
  establishmentMeans: http://rs.tdwg.org/dwc/terms/establishmentMeans
  relationshipEstablishedDate: http://rs.tdwg.org/dwc/terms/relationshipEstablishedDate
  identifiedBy: http://rs.tdwg.org/dwc/terms/identifiedBy
  sex: http://rs.tdwg.org/dwc/terms/sex
  Sample: http://www.w3.org/ns/sosa/Sample
  verbatimLabel: http://rs.tdwg.org/dwc/terms/verbatimLabel
  relatesToProperty:
    x-jsonld-id: https://saref.etsi.org/core/relatesToProperty
    x-jsonld-type: '@id'
  verbatimEventDate: http://rs.tdwg.org/dwc/terms/verbatimEventDate
  month: http://rs.tdwg.org/dwc/terms/month
  taxonID: http://rs.tdwg.org/dwc/terms/taxonID
  DataSet: http://purl.org/linked-data/cube#DataSet
  addressLocality: https://schema.org/addressLocality
  municipality: http://rs.tdwg.org/dwc/terms/municipality
  reportedWeather: http://rs.tdwg.org/hc/terms/reportedWeather
  airTemperatureForecast: https://smartdatamodels.org/dataModel.Weather/airTemperatureForecast
  nomenclaturalStatus: http://rs.tdwg.org/dwc/terms/nomenclaturalStatus
  observedIndividualLengthInCm: http://mmisw.org/ont/ioos/marine_biogeography/observedIndividualLengthInCm
  samplingProtocol: http://rs.tdwg.org/dwc/terms/samplingProtocol
  earliestPeriodOrLowestSystem: http://rs.tdwg.org/dwc/terms/earliestPeriodOrLowestSystem
  lifeStage: http://rs.tdwg.org/dwc/terms/lifeStage
  PolyhedralSurface: http://www.opengis.net/ont/sf#PolyhedralSurface
  basisOfRecord: http://rs.tdwg.org/dwc/terms/basisOfRecord
  day: http://rs.tdwg.org/dwc/terms/day
  controlsProperty:
    x-jsonld-id: https://saref.etsi.org/core/controlsProperty
    x-jsonld-type: '@id'
  verticalDatum: http://rs.tdwg.org/dwc/terms/verticalDatum
  Polygon: http://www.opengis.net/ont/sf#Polygon
  MultiPolygon: http://www.opengis.net/ont/sf#MultiPolygon
  language: http://purl.org/dc/terms/language
  latestEpochOrHighestSeries: http://rs.tdwg.org/dwc/terms/latestEpochOrHighestSeries
  originalNameUsage: http://rs.tdwg.org/dwc/terms/originalNameUsage
  ObservableProperty: http://www.w3.org/ns/sosa/ObservableProperty
  cultivarEpithet: http://rs.tdwg.org/dwc/terms/cultivarEpithet
  identifiedByID: http://rs.tdwg.org/dwc/terms/identifiedByID
  reproductiveCondition: http://rs.tdwg.org/dwc/terms/reproductiveCondition
  latestEraOrHighestErathem: http://rs.tdwg.org/dwc/terms/latestEraOrHighestErathem
  deployedSystem: http://www.w3.org/ns/ssn/deployedSystem
  System: http://www.w3.org/ns/ssn/System
  datasetID: http://rs.tdwg.org/dwc/terms/datasetID
  unitKind:
    x-jsonld-id: http://purl.oclc.org/NET/ssnx/qu/qu#unitKind
    x-jsonld-type: '@id'
  scientificNameAuthorship: http://rs.tdwg.org/dwc/terms/scientificNameAuthorship
  dimension:
    x-jsonld-id: http://purl.org/linked-data/cube#dimension
    x-jsonld-type: '@id'
  RadianceExposure: http://purl.oclc.org/NET/ssnx/qu/dim#RadianceExposure
  VelocityOrSpeed: http://purl.oclc.org/NET/ssnx/qu/dim#VelocityOrSpeed
  Device: https://saref.etsi.org/core/Device
  collectionID: http://rs.tdwg.org/dwc/terms/collectionID
  pointRadiusSpatialFit: http://rs.tdwg.org/dwc/terms/pointRadiusSpatialFit
  deployedOnPlatform: http://www.w3.org/ns/ssn/deployedOnPlatform
  nameAccordingToID: http://rs.tdwg.org/dwc/terms/nameAccordingToID
  subtribe: http://rs.tdwg.org/dwc/terms/subtribe
  georeferenceProtocol: http://rs.tdwg.org/dwc/terms/georeferenceProtocol
  eventRemarks: http://rs.tdwg.org/dwc/terms/eventRemarks
  minimumElevationInMeters: http://rs.tdwg.org/dwc/terms/minimumElevationInMeters
  verbatimSRS: http://rs.tdwg.org/dwc/terms/verbatimSRS
  degreeOfEstablishment: http://rs.tdwg.org/dwc/terms/degreeOfEstablishment
  inXSDDate: http://www.w3.org/2006/time#inXSDDate
  GFI_DomainFeature: http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_DomainFeature
  MeasurementOrFact: http://rs.tdwg.org/dwc/terms/MeasurementOrFact
  Actuation: http://www.w3.org/ns/sosa/Actuation
  observation: http://purl.org/linked-data/cube#observation
  hasTimestamp: https://saref.etsi.org/core/hasTimestamp
  identificationQualifier: http://rs.tdwg.org/dwc/terms/identificationQualifier
  Dimensionless: http://purl.oclc.org/NET/ssnx/qu/dim#Dimensionless
  Area: http://purl.oclc.org/NET/ssnx/qu/dim#Area
  Sampling: http://www.w3.org/ns/sosa/Sampling
  infraspecificEpithet: http://rs.tdwg.org/dwc/terms/infraspecificEpithet
  precipitation: https://smartdatamodels.org/dataModel.Weather/precipitation
  latestAgeOrHighestStage: http://rs.tdwg.org/dwc/terms/latestAgeOrHighestStage
  alternateName: https://smartdatamodels.org/alternateName
  Power: http://purl.oclc.org/NET/ssnx/qu/dim#Power
  OM_Observation: http://def.isotc211.org/iso19156/2011/Observation#OM_Observation
  prefLabel: http://www.w3.org/2004/02/skos/core#prefLabel
  Surface: http://purl.oclc.org/NET/ssnx/cf/cf-feature#Surface
  addressCountry: https://schema.org/addressCountry
  dataGeneralizations: http://rs.tdwg.org/dwc/terms/dataGeneralizations
  SurfaceLayer: http://purl.oclc.org/NET/ssnx/cf/cf-feature#SurfaceLayer
  ResourceRelationship: http://rs.tdwg.org/dwc/terms/ResourceRelationship
  eventTime: http://rs.tdwg.org/dwc/terms/eventTime
  sliceKey: http://purl.org/linked-data/cube#sliceKey
  verbatimIdentification: http://rs.tdwg.org/dwc/terms/verbatimIdentification
  PeriodOfTime: http://purl.org/dc/terms/PeriodOfTime
  inScheme: http://www.w3.org/2004/02/skos/core#inScheme
  PreservedSpecimen: http://rs.tdwg.org/dwc/terms/PreservedSpecimen
  associatedReferences: http://rs.tdwg.org/dwc/terms/associatedReferences
  recordedBy: http://rs.tdwg.org/dwc/terms/recordedBy
  specificEpithet: http://rs.tdwg.org/dwc/terms/specificEpithet
  formation: http://rs.tdwg.org/dwc/terms/formation
  nomenclaturalCode: http://rs.tdwg.org/dwc/terms/nomenclaturalCode
  ResponsibleParty: http://def.seegrid.csiro.au/isotc211/iso19115/2003/citation#ResponsibleParty
  observedMeanLengthInCm: http://mmisw.org/ont/ioos/marine_biogeography/observedMeanLengthInCm
  MultiCurve: http://www.opengis.net/ont/sf#MultiCurve
  hasQuantityKind: http://qudt.org/schema/qudt/hasQuantityKind
  ownerInstitutionCode: http://rs.tdwg.org/dwc/terms/ownerInstitutionCode
  temporal: http://purl.org/dc/terms/temporal
  relatedResourceID: http://rs.tdwg.org/dwc/terms/relatedResourceID
  windSpeed: https://smartdatamodels.org/dataModel.Weather/windSpeed
  measurementValue: http://rs.tdwg.org/dwc/terms/measurementValue
  occurrenceRemarks: http://rs.tdwg.org/dwc/terms/occurrenceRemarks
  DataStructureDefinition: http://purl.org/linked-data/cube#DataStructureDefinition
  MultiPoint: http://www.opengis.net/ont/sf#MultiPoint
  Observation: http://www.w3.org/ns/sosa/Observation
  EnergyDensity: http://purl.oclc.org/NET/ssnx/qu/dim#EnergyDensity
  measurementRemarks: http://rs.tdwg.org/dwc/terms/measurementRemarks
  illuminance: https://smartdatamodels.org/dataModel.Weather/illuminance
  georeferenceRemarks: http://rs.tdwg.org/dwc/terms/georeferenceRemarks
  organismScope: http://rs.tdwg.org/dwc/terms/organismScope
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  resourceID: http://rs.tdwg.org/dwc/terms/resourceID
  associatedOccurrences: http://rs.tdwg.org/dwc/terms/associatedOccurrences
  unitType: http://www.w3.org/2006/time#unitType
  componentProperty: http://purl.org/linked-data/cube#componentProperty
  relationshipAccordingTo: http://rs.tdwg.org/dwc/terms/relationshipAccordingTo
  isFeatureOfInterestOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    x-jsonld-type: '@id'
x-jsonld-vocab: https://w3id.org/iliad/oim/default-context/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/iliad/oim/default-context/",
    "resultTime": "sosa:resultTime",
    "phenomenonTime": {
      "@id": "sosa:phenomenonTime",
      "@type": "@id"
    },
    "hasFeatureOfInterest": {
      "@id": "https://saref.etsi.org/core/hasFeatureOfInterest",
      "@type": "@id"
    },
    "observedProperty": {
      "@context": {
        "@base": "https://w3id.org/iliad/jellyfish/property/"
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
    "id": "@id",
    "properties": "@nest",
    "featureType": "@type",
    "ActuatableProperty": {
      "@id": "sosa:ActuatableProperty",
      "@type": "@id"
    },
    "Actuation": {
      "@id": "sosa:Actuation",
      "@type": "@id"
    },
    "ActuationCollection": {
      "@id": "sosa:ActuationCollection",
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
    "Execution": {
      "@id": "sosa:Execution",
      "@type": "@id"
    },
    "FeatureOfInterest": {
      "@id": "sosa:FeatureOfInterest",
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
    "ObservationCollection": {
      "@id": "sosa:ObservationCollection",
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
    "Sample": {
      "@id": "sosa:Sample",
      "@type": "@id"
    },
    "SampleCollection": {
      "@id": "sosa:SampleCollection",
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
      "@container": "@set",
      "@context": {
        "properties": "https://w3id.org/iliad/oim/default-context/properties"
      }
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
        }
      }
    },
    "hasOriginalSample": {
      "@id": "sosa:hasOriginalSample",
      "@type": "@id"
    },
    "hasOutput": {
      "@id": "sosa:hasOutput",
      "@type": "@id"
    },
    "hasProperty": {
      "@id": "sosa:hasProperty",
      "@type": "@id"
    },
    "hasResult": {
      "@id": "sosa:hasResult",
      "@type": "@id",
      "@context": {
        "quantityOfJF": "https://w3id.org/iliad/oim/default-context/quantityOfJF",
        "densityOfJF": "https://w3id.org/iliad/oim/default-context/densityOfJF",
        "stingByJF": "https://w3id.org/iliad/oim/default-context/stingByJF",
        "beachedJF": "https://w3id.org/iliad/oim/default-context/beachedJF"
      }
    },
    "hasResultQuality": {
      "@id": "sosa:hasResultQuality",
      "@type": "@id"
    },
    "hasSample": {
      "@id": "sosa:hasSample",
      "@type": "@id"
    },
    "hasSampledFeature": {
      "@id": "sosa:hasSampledFeature",
      "@type": "@id"
    },
    "hasSimpleResult": {
      "@id": "sosa:hasSimpleResult",
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
    "isResultOfMadeBySampler": {
      "@id": "sosa:isResultOfMadeBySampler",
      "@type": "@id"
    },
    "isResultOfUsedProcedure": {
      "@id": "sosa:isResultOfUsedProcedure",
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
    "Accuracy": {
      "@id": "ssn-system:Accuracy",
      "@type": "@id"
    },
    "ActuationRange": {
      "@id": "ssn-system:ActuationRange",
      "@type": "@id"
    },
    "BatteryLifetime": {
      "@id": "ssn-system:BatteryLifetime",
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
    "MaintenanceSchedule": {
      "@id": "ssn-system:MaintenanceSchedule",
      "@type": "@id"
    },
    "MeasurementRange": {
      "@id": "ssn-system:MeasurementRange",
      "@type": "@id"
    },
    "OperatingPowerRange": {
      "@id": "ssn-system:OperatingPowerRange",
      "@type": "@id"
    },
    "OperatingProperty": {
      "@id": "ssn-system:OperatingProperty",
      "@type": "@id"
    },
    "OperatingRange": {
      "@id": "ssn-system:OperatingRange",
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
    "SurvivalProperty": {
      "@id": "ssn-system:SurvivalProperty",
      "@type": "@id"
    },
    "SystemLifetime": {
      "@id": "ssn-system:SystemLifetime",
      "@type": "@id"
    },
    "SurvivalRange": {
      "@id": "ssn-system:SurvivalRange",
      "@type": "@id"
    },
    "SystemCapability": {
      "@id": "ssn-system:SystemCapability",
      "@type": "@id"
    },
    "SystemProperty": {
      "@id": "ssn-system:SystemProperty",
      "@type": "@id"
    },
    "hasOperatingProperty": {
      "@id": "ssn-system:hasOperatingProperty",
      "@type": "@id"
    },
    "hasOperatingRange": {
      "@id": "ssn-system:hasOperatingRange",
      "@type": "@id"
    },
    "hasSurvivalProperty": {
      "@id": "ssn-system:hasSurvivalProperty",
      "@type": "@id"
    },
    "hasSystemCapability": {
      "@id": "ssn-system:hasSystemCapability",
      "@type": "@id"
    },
    "hasSystemProperty": {
      "@id": "ssn-system:hasSystemProperty",
      "@type": "@id"
    },
    "hasSurvivalRange": {
      "@id": "ssn-system:hasSurvivalRange",
      "@type": "@id"
    },
    "inCondition": {
      "@id": "ssn-system:inCondition",
      "@type": "@id"
    },
    "qualityOfObservation": {
      "@id": "ssn-system:qualityOfObservation",
      "@type": "@id"
    },
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
    "geometry": "geojson:geometry",
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
    "time": {
      "@context": {
        "date": {
          "@id": "owlTime:hasTime",
          "@type": "xsd:date"
        },
        "timestamp": {
          "@id": "owlTime:hasTime",
          "@type": "xsd:dateTime"
        },
        "interval": {
          "@id": "owlTime:hasTime",
          "@container": "@list"
        }
      },
      "@id": "dct:time"
    },
    "coordRefSys": "http://www.opengis.net/def/glossary/term/CoordinateReferenceSystemCRS",
    "place": "dct:spatial",
    "Polyhedron": "geojson:Polyhedron",
    "MultiPolyhedron": "geojson:MultiPolyhedron",
    "Prism": {
      "@id": "geojson:Prism",
      "@context": {
        "base": "geojson:prismBase",
        "lower": "geojson:prismLower",
        "upper": "geojson:prismUpper"
      }
    },
    "MultiPrism": {
      "@id": "geojson:MultiPrism",
      "@context": {
        "prisms": "geojson:prisms"
      }
    },
    "coordinates": {
      "@container": "@list",
      "@id": "geojson:coordinates"
    },
    "geometries": {
      "@id": "geojson:geometry",
      "@container": "@list"
    },
    "strandedJellyfish": "https://w3id.org/iliad/oim/ext/jellyfish/strandedJellyfish",
    "JellyFishAbundance": "https://w3id.org/iliad/oim/ext/jellyfish/JellyFishAbundance",
    "affiliation": "https://schema.org/affiliation",
    "distanceFromShore": "https://w3id.org/iliad/oim/ext/jellyfish/distanceFromShore",
    "agentConfidence": "https://w3id.org/iliad/oim/ext/jellyfish/agentConfidence",
    "versionInfo": "http://www.w3.org/2002/07/owl#versionInfo",
    "maker": "http://xmlns.com/foaf/0.1/maker",
    "stingByJellyFish": "https://w3id.org/iliad/oim/ext/jellyfish/stingByJellyFish",
    "Result": "sosa:Result",
    "homepage": "http://xmlns.com/foaf/0.1/homepage",
    "creator": "dct:creator",
    "name": "https://schema.org/name",
    "rights": "dct:rights",
    "HumanSensor": "https://w3id.org/iliad/oim/ext/jellyfish/HumanSensor",
    "isDefinedBy": "rdfs:isDefinedBy",
    "title": "dct:title",
    "seeAlso": "rdfs:seeAlso",
    "comment": "rdfs:comment",
    "contributor": "dct:contributor",
    "description": "dct:description",
    "distanceWalkedInMeters": "https://w3id.org/iliad/oim/ext/jellyfish/distanceWalkedInMeters",
    "PhotonFluxDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#PhotonFluxDensity",
    "sampleSizeUnit": "http://rs.tdwg.org/dwc/terms/sampleSizeUnit",
    "recordNumber": "http://rs.tdwg.org/dwc/terms/recordNumber",
    "verbatimLongitude": "http://rs.tdwg.org/dwc/terms/verbatimLongitude",
    "invalidatedAtTime": "http://www.w3.org/ns/prov#invalidatedAtTime",
    "behavior": "http://rs.tdwg.org/dwc/terms/behavior",
    "organismQuantity": "http://rs.tdwg.org/dwc/terms/organismQuantity",
    "spatial": "dct:spatial",
    "scientificNameID": "http://rs.tdwg.org/dwc/terms/scientificNameID",
    "lowestBiostratigraphicZone": "http://rs.tdwg.org/dwc/terms/lowestBiostratigraphicZone",
    "Attachable": "http://purl.org/linked-data/cube#Attachable",
    "earliestEonOrLowestEonothem": "http://rs.tdwg.org/dwc/terms/earliestEonOrLowestEonothem",
    "originalNameUsageID": "http://rs.tdwg.org/dwc/terms/originalNameUsageID",
    "GeologicalContext": "http://rs.tdwg.org/dwc/terms/GeologicalContext",
    "countryCode": "http://rs.tdwg.org/dwc/terms/countryCode",
    "UnitOfMeasure": "https://saref.etsi.org/core/UnitOfMeasure",
    "verbatimCoordinates": "http://rs.tdwg.org/dwc/terms/verbatimCoordinates",
    "recordType": "http://mmisw.org/ont/ioos/marine_biogeography/recordType",
    "maximumDistanceAboveSurfaceInMeters": "http://rs.tdwg.org/dwc/terms/maximumDistanceAboveSurfaceInMeters",
    "verbatimLocality": "http://rs.tdwg.org/dwc/terms/verbatimLocality",
    "QuantityValue": "http://qudt.org/schema/qudt/QuantityValue",
    "identificationReferences": "http://rs.tdwg.org/dwc/terms/identificationReferences",
    "Unit": "http://qudt.org/schema/qudt/Unit",
    "isControlledByDevice": {
      "@id": "https://saref.etsi.org/core/isControlledByDevice",
      "@type": "@id"
    },
    "verbatimCoordinateSystem": "http://rs.tdwg.org/dwc/terms/verbatimCoordinateSystem",
    "sampleLengthInMeters": "http://mmisw.org/ont/ioos/marine_biogeography/sampleLengthInMeters",
    "measurementType": "http://rs.tdwg.org/dwc/terms/measurementType",
    "sampleWidthInMeters": "http://mmisw.org/ont/ioos/marine_biogeography/sampleWidthInMeters",
    "measurementAccuracy": "http://rs.tdwg.org/dwc/terms/measurementAccuracy",
    "Line": "http://www.opengis.net/ont/sf#Line",
    "member": "http://rs.tdwg.org/dwc/terms/member",
    "genus": "http://rs.tdwg.org/dwc/terms/genus",
    "coordinatePrecision": "http://rs.tdwg.org/dwc/terms/coordinatePrecision",
    "weightInKg": "http://mmisw.org/ont/ioos/marine_biogeography/weightInKg",
    "generatedAtTime": "http://www.w3.org/ns/prov#generatedAtTime",
    "georeferencedDate": "http://rs.tdwg.org/dwc/terms/georeferencedDate",
    "example": "http://www.w3.org/2004/02/skos/core#example",
    "taxonomicStatus": "http://rs.tdwg.org/dwc/terms/taxonomicStatus",
    "validFrom": {
      "@id": "http://portele.de/ont/inspire/baseInspire#validFrom",
      "@type": "xsd:dateTime"
    },
    "SurfaceMediumMedium": "http://purl.oclc.org/NET/ssnx/cf/cf-feature#SurfaceMediumMedium",
    "Slice": "http://purl.org/linked-data/cube#Slice",
    "Humidity": "https://saref.etsi.org/core/Humidity",
    "previousIdentifications": "http://rs.tdwg.org/dwc/terms/previousIdentifications",
    "Concentration": "http://purl.oclc.org/NET/ssnx/qu/dim#Concentration",
    "dataSet": "http://purl.org/linked-data/cube#dataSet",
    "Period": "http://def.seegrid.csiro.au/isotc211/iso19108/2002/temporal#Period",
    "startDayOfYear": "http://rs.tdwg.org/dwc/terms/startDayOfYear",
    "componentAttachment": "http://purl.org/linked-data/cube#componentAttachment",
    "otherCatalogNumbers": "http://rs.tdwg.org/dwc/terms/otherCatalogNumbers",
    "MachineObservation": "http://rs.tdwg.org/dwc/terms/MachineObservation",
    "Relationship": "https://uri.etsi.org/ngsi-ld/Relationship",
    "license": "dct:license",
    "concept": "http://purl.org/linked-data/cube#concept",
    "coordinateUncertaintyInMeters": "http://rs.tdwg.org/dwc/terms/coordinateUncertaintyInMeters",
    "MultiSurface": "http://www.opengis.net/ont/sf#MultiSurface",
    "eventID": "http://rs.tdwg.org/dwc/terms/eventID",
    "Organism": "http://rs.tdwg.org/dwc/terms/Organism",
    "TemporalDuration": "owlTime:TemporalDuration",
    "identificationID": "http://rs.tdwg.org/dwc/terms/identificationID",
    "recordedByID": "http://rs.tdwg.org/dwc/terms/recordedByID",
    "dateCreated": {
      "@id": "https://smartdatamodels.org/dateCreated",
      "@type": "xsd:dateTime"
    },
    "Identification": "http://rs.tdwg.org/dwc/terms/Identification",
    "Procedure": "sosa:Procedure",
    "WeatherObserved": "https://smartdatamodels.org/dataModel.Weather/WeatherObserved",
    "quantificationUnit": "http://mmisw.org/ont/ioos/marine_biogeography/quantificationUnit",
    "country": "http://rs.tdwg.org/dwc/terms/country",
    "genericName": "http://rs.tdwg.org/dwc/terms/genericName",
    "DiffusionCoefficient": "http://purl.oclc.org/NET/ssnx/qu/dim#DiffusionCoefficient",
    "bibliographicCitation": "dct:bibliographicCitation",
    "Organization": "https://schema.org/Organization",
    "decimalLongitude": "http://rs.tdwg.org/dwc/terms/decimalLongitude",
    "scientificName": "http://rs.tdwg.org/dwc/terms/scientificName",
    "Volume": "http://purl.oclc.org/NET/ssnx/qu/dim#Volume",
    "Thing": "http://www.w3.org/2002/07/owl#Thing",
    "organismQuantityType": "http://rs.tdwg.org/dwc/terms/organismQuantityType",
    "catalogNumber": "http://rs.tdwg.org/dwc/terms/catalogNumber",
    "continent": "http://rs.tdwg.org/dwc/terms/continent",
    "minimumDistanceAboveSurfaceInMeters": "http://rs.tdwg.org/dwc/terms/minimumDistanceAboveSurfaceInMeters",
    "GFI_Feature": "http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_Feature",
    "dateModified": {
      "@id": "https://smartdatamodels.org/dateModified",
      "@type": "xsd:dateTime"
    },
    "decimalLatitude": "http://rs.tdwg.org/dwc/terms/decimalLatitude",
    "references": "dct:references",
    "AttributeProperty": "http://purl.org/linked-data/cube#AttributeProperty",
    "agroVocConcept": {
      "@id": "https://smartdatamodels.org/dataModel.Agrifood/agroVocConcept",
      "@type": "@id"
    },
    "quantityValue": "http://qudt.org/schema/qudt/quantityValue",
    "TemporalUnit": "owlTime:TemporalUnit",
    "higherGeographyID": "http://rs.tdwg.org/dwc/terms/higherGeographyID",
    "addressRegion": "https://schema.org/addressRegion",
    "asWKT": {
      "@id": "http://www.opengis.net/ont/geosparql#asWKT",
      "@type": "http://www.opengis.net/ont/geosparql#wktLiteral"
    },
    "measurementDeterminedBy": "http://rs.tdwg.org/dwc/terms/measurementDeterminedBy",
    "sampleShape": "http://mmisw.org/ont/ioos/marine_biogeography/sampleShape",
    "geodeticDatum": "http://rs.tdwg.org/dwc/terms/geodeticDatum",
    "Angle": "http://purl.oclc.org/NET/ssnx/qu/dim#Angle",
    "TemperatureDrift": "http://purl.oclc.org/NET/ssnx/qu/dim#TemperatureDrift",
    "verbatimSiteDescriptions": "http://rs.tdwg.org/hc/terms/verbatimSiteDescriptions",
    "RotationalSpeed": "http://purl.oclc.org/NET/ssnx/qu/dim#RotationalSpeed",
    "dataProvider": "https://smartdatamodels.org/dataProvider",
    "ComponentProperty": "http://purl.org/linked-data/cube#ComponentProperty",
    "maximumDepthInMeters": "http://rs.tdwg.org/dwc/terms/maximumDepthInMeters",
    "measuresProperty": {
      "@id": "https://saref.etsi.org/core/measuresProperty",
      "@type": "@id"
    },
    "Class": "rdfs:Class",
    "Geometry": "http://www.opengis.net/ont/geosparql#Geometry",
    "locationAccordingTo": "http://rs.tdwg.org/dwc/terms/locationAccordingTo",
    "depiction": "http://xmlns.com/foaf/0.1/depiction",
    "nameAccordingTo": "http://rs.tdwg.org/dwc/terms/nameAccordingTo",
    "Curve": "http://www.opengis.net/ont/sf#Curve",
    "group": "http://rs.tdwg.org/dwc/terms/group",
    "hasValue": "https://saref.etsi.org/core/hasValue",
    "class": "http://rs.tdwg.org/dwc/terms/class",
    "footprintWKT": "http://rs.tdwg.org/dwc/terms/footprintWKT",
    "Instant": "owlTime:Instant",
    "FossilSpecimen": "http://rs.tdwg.org/dwc/terms/FossilSpecimen",
    "snowHeight": "https://smartdatamodels.org/dataModel.Weather/snowHeight",
    "Medium": "http://purl.oclc.org/NET/ssnx/cf/cf-feature#Medium",
    "sfWithin": "http://www.opengis.net/ont/geosparql#sfWithin",
    "ThermalConductivity": "http://purl.oclc.org/NET/ssnx/qu/dim#ThermalConductivity",
    "typeStatus": "http://rs.tdwg.org/dwc/terms/typeStatus",
    "acceptedNameUsage": "http://rs.tdwg.org/dwc/terms/acceptedNameUsage",
    "domainIncludes": "https://schema.org/domainIncludes",
    "earliestEpochOrLowestSeries": "http://rs.tdwg.org/dwc/terms/earliestEpochOrLowestSeries",
    "long": "http://www.w3.org/2003/01/geo/wgs84_pos#long",
    "streamGauge": "https://smartdatamodels.org/dataModel.Weather/streamGauge",
    "parentNameUsageID": "http://rs.tdwg.org/dwc/terms/parentNameUsageID",
    "dynamicProperties": "http://rs.tdwg.org/dwc/terms/dynamicProperties",
    "numericValue": "http://qudt.org/schema/qudt/numericValue",
    "Wind": "http://purl.oclc.org/NET/ssnx/cf/cf-feature#Wind",
    "caste": "http://rs.tdwg.org/dwc/terms/caste",
    "footprintSpatialFit": "http://rs.tdwg.org/dwc/terms/footprintSpatialFit",
    "namePublishedInYear": "http://rs.tdwg.org/dwc/terms/namePublishedInYear",
    "highestBiostratigraphicZone": "http://rs.tdwg.org/dwc/terms/highestBiostratigraphicZone",
    "fieldNotes": "http://rs.tdwg.org/dwc/terms/fieldNotes",
    "measurementID": "http://rs.tdwg.org/dwc/terms/measurementID",
    "parentNameUsage": "http://rs.tdwg.org/dwc/terms/parentNameUsage",
    "acceptedNameUsageID": "http://rs.tdwg.org/dwc/terms/acceptedNameUsageID",
    "maximumElevationInMeters": "http://rs.tdwg.org/dwc/terms/maximumElevationInMeters",
    "visibilityInMeters": "http://mmisw.org/ont/ioos/marine_biogeography/visibilityInMeters",
    "Concept": "http://www.w3.org/2004/02/skos/core#Concept",
    "component": "http://purl.org/linked-data/cube#component",
    "measure": {
      "@id": "http://purl.org/linked-data/cube#measure",
      "@type": "@id"
    },
    "identificationVerificationStatus": "http://rs.tdwg.org/dwc/terms/identificationVerificationStatus",
    "SliceKey": "http://purl.org/linked-data/cube#SliceKey",
    "Measurement": "https://saref.etsi.org/core/Measurement",
    "Location": "dct:Location",
    "footprintSRS": "http://rs.tdwg.org/dwc/terms/footprintSRS",
    "individualCount": "http://rs.tdwg.org/dwc/terms/individualCount",
    "collectionCode": "http://rs.tdwg.org/dwc/terms/collectionCode",
    "lithostratigraphicTerms": "http://rs.tdwg.org/dwc/terms/lithostratigraphicTerms",
    "subfamily": "http://rs.tdwg.org/dwc/terms/subfamily",
    "eventType": "http://rs.tdwg.org/dwc/terms/eventType",
    "Compressibility": "http://purl.oclc.org/NET/ssnx/qu/dim#Compressibility",
    "associatedMedia": "http://rs.tdwg.org/dwc/terms/associatedMedia",
    "Taxon": "http://rs.tdwg.org/dwc/terms/Taxon",
    "vernacularName": "http://rs.tdwg.org/dwc/terms/vernacularName",
    "windDirection": "https://smartdatamodels.org/dataModel.Weather/windDirection",
    "ComponentSet": "http://purl.org/linked-data/cube#ComponentSet",
    "MassPerTimePerArea": "http://purl.oclc.org/NET/ssnx/qu/dim#MassPerTimePerArea",
    "numericDuration": "owlTime:numericDuration",
    "ElectricConductivity": "http://purl.oclc.org/NET/ssnx/qu/dim#ElectricConductivity",
    "preparations": "http://rs.tdwg.org/dwc/terms/preparations",
    "Temperature": "http://purl.oclc.org/NET/ssnx/qu/dim#Temperature",
    "Event": "http://rs.tdwg.org/dwc/terms/Event",
    "observationLocation": "http://mmisw.org/ont/ioos/marine_biogeography/observationLocation",
    "institutionID": "http://rs.tdwg.org/dwc/terms/institutionID",
    "WeatherForecast": "https://smartdatamodels.org/dataModel.Weather/WeatherForecast",
    "verbatimDepth": "http://rs.tdwg.org/dwc/terms/verbatimDepth",
    "Measure": "http://def.seegrid.csiro.au/isotc211/iso19103/2005/basic#Measure",
    "Person": "https://schema.org/Person",
    "Triangle": "http://www.opengis.net/ont/sf#Triangle",
    "county": "http://rs.tdwg.org/dwc/terms/county",
    "note": "http://www.w3.org/2004/02/skos/core#note",
    "rightsHolder": "dct:rightsHolder",
    "measurementMadeBy": {
      "@id": "https://saref.etsi.org/core/measurementMadeBy",
      "@type": "@id"
    },
    "earliestEraOrLowestErathem": "http://rs.tdwg.org/dwc/terms/earliestEraOrLowestErathem",
    "observationGroup": "http://purl.org/linked-data/cube#observationGroup",
    "Interval": "owlTime:Interval",
    "occurrenceStatus": "http://rs.tdwg.org/dwc/terms/occurrenceStatus",
    "LocationRelationship": "https://uri.etsi.org/ngsi-ld/LocationRelationship",
    "EnergyFlux": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyFlux",
    "StressOrPressure": "http://purl.oclc.org/NET/ssnx/qu/dim#StressOrPressure",
    "observedMinLengthInCm": "http://mmisw.org/ont/ioos/marine_biogeography/observedMinLengthInCm",
    "verbatimTaxonRank": "http://rs.tdwg.org/dwc/terms/verbatimTaxonRank",
    "disposition": "http://rs.tdwg.org/dwc/terms/disposition",
    "visibility": "https://smartdatamodels.org/dataModel.Weather/visibility",
    "namePublishedInID": "http://rs.tdwg.org/dwc/terms/namePublishedInID",
    "Agent": "http://xmlns.com/foaf/0.1/Agent",
    "dateIdentified": "http://rs.tdwg.org/dwc/terms/dateIdentified",
    "ImageObject": "https://schema.org/ImageObject",
    "organismRemarks": "http://rs.tdwg.org/dwc/terms/organismRemarks",
    "latestPeriodOrHighestSystem": "http://rs.tdwg.org/dwc/terms/latestPeriodOrHighestSystem",
    "Precipitation": "http://purl.oclc.org/NET/ssnx/cf/cf-feature#Precipitation",
    "taxonRemarks": "http://rs.tdwg.org/dwc/terms/taxonRemarks",
    "georeferencedBy": "http://rs.tdwg.org/dwc/terms/georeferencedBy",
    "Energy": "http://purl.oclc.org/NET/ssnx/qu/dim#Energy",
    "Role": "https://schema.org/Role",
    "hasSerialization": "http://www.opengis.net/ont/geosparql#hasSerialization",
    "verbatimElevation": "http://rs.tdwg.org/dwc/terms/verbatimElevation",
    "higherClassification": "http://rs.tdwg.org/dwc/terms/higherClassification",
    "waterBody": "http://rs.tdwg.org/dwc/terms/waterBody",
    "Layer": "http://purl.oclc.org/NET/ssnx/cf/cf-feature#Layer",
    "hasTime": "owlTime:hasTime",
    "GeoProperty": "https://uri.etsi.org/ngsi-ld/GeoProperty",
    "namePublishedIn": "http://rs.tdwg.org/dwc/terms/namePublishedIn",
    "organismID": "http://rs.tdwg.org/dwc/terms/organismID",
    "SF_SamplingFeature.sampledFeature": "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature.sampledFeature",
    "stateProvince": "http://rs.tdwg.org/dwc/terms/stateProvince",
    "rangeIncludes": "https://schema.org/rangeIncludes",
    "Mass": "http://purl.oclc.org/NET/ssnx/qu/dim#Mass",
    "endDayOfYear": "http://rs.tdwg.org/dwc/terms/endDayOfYear",
    "geologicalContextID": "http://rs.tdwg.org/dwc/terms/geologicalContextID",
    "pathway": "http://rs.tdwg.org/dwc/terms/pathway",
    "verbatimSiteNames": "http://rs.tdwg.org/hc/terms/verbatimSiteNames",
    "location": "http://www.w3.org/2003/01/geo/wgs84_pos#location",
    "parentEventID": "http://rs.tdwg.org/dwc/terms/parentEventID",
    "datasetName": "http://rs.tdwg.org/dwc/terms/datasetName",
    "ComponentSpecification": "http://purl.org/linked-data/cube#ComponentSpecification",
    "temperature": "https://smartdatamodels.org/dataModel.Weather/temperature",
    "measurementMethod": "http://rs.tdwg.org/dwc/terms/measurementMethod",
    "Scheme": "http://www.w3.org/2004/02/skos/core#Scheme",
    "verbatimLatitude": "http://rs.tdwg.org/dwc/terms/verbatimLatitude",
    "hasEnd": {
      "@id": "owlTime:hasEnd",
      "@type": "@id"
    },
    "parentMeasurementID": "http://rs.tdwg.org/dwc/terms/parentMeasurementID",
    "sightingCue": "http://mmisw.org/ont/ioos/marine_biogeography/sightingCue",
    "waterTemperatureInCelsius": "http://mmisw.org/ont/ioos/marine_biogeography/waterTemperatureInCelsius",
    "tribe": "http://rs.tdwg.org/dwc/terms/tribe",
    "status": "https://schema.org/status",
    "TemporalEntity": "owlTime:TemporalEntity",
    "hasBeginning": {
      "@id": "owlTime:hasBeginning",
      "@type": "@id"
    },
    "SF_SamplingFeature": "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature",
    "DimensionProperty": "http://purl.org/linked-data/cube#DimensionProperty",
    "alt": "http://www.w3.org/2003/01/geo/wgs84_pos#alt",
    "superfamily": "http://rs.tdwg.org/dwc/terms/superfamily",
    "Acceleration": "http://purl.oclc.org/NET/ssnx/qu/dim#Acceleration",
    "identifier": "dct:identifier",
    "LivingSpecimen": "http://rs.tdwg.org/dwc/terms/LivingSpecimen",
    "visibilityType": "http://mmisw.org/ont/ioos/marine_biogeography/visibilityType",
    "locationRemarks": "http://rs.tdwg.org/dwc/terms/locationRemarks",
    "Quantity": "http://qudt.org/schema/qudt/Quantity",
    "MassFlowRate": "http://purl.oclc.org/NET/ssnx/qu/dim#MassFlowRate",
    "QuantityKind": "http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind",
    "Distance": "http://purl.oclc.org/NET/ssnx/qu/dim#Distance",
    "higherGeography": "http://rs.tdwg.org/dwc/terms/higherGeography",
    "informationWithheld": "http://rs.tdwg.org/dwc/terms/informationWithheld",
    "dateObserved": {
      "@id": "https://smartdatamodels.org/dateObserved",
      "@type": "xsd:dateTime"
    },
    "relatesToMeasurement": {
      "@id": "https://saref.etsi.org/core/relatesToMeasurement",
      "@type": "@id"
    },
    "atmosphericPressure": "https://smartdatamodels.org/dataModel.Weather/atmosphericPressure",
    "organismName": "http://rs.tdwg.org/dwc/terms/organismName",
    "deprecated": "http://www.w3.org/2002/07/owl#deprecated",
    "institutionCode": "http://rs.tdwg.org/dwc/terms/institutionCode",
    "Radiance": "http://purl.oclc.org/NET/ssnx/qu/dim#Radiance",
    "isMeasuredByDevice": {
      "@id": "https://saref.etsi.org/core/isMeasuredByDevice",
      "@type": "@id"
    },
    "occurrenceID": "http://rs.tdwg.org/dwc/terms/occurrenceID",
    "subject": "dct:subject",
    "quantificationMethod": "http://mmisw.org/ont/ioos/marine_biogeography/quantificationMethod",
    "measurementUnit": "http://rs.tdwg.org/dwc/terms/measurementUnit",
    "lengthType": "http://mmisw.org/ont/ioos/marine_biogeography/lengthType",
    "HumanObservation": "http://rs.tdwg.org/dwc/terms/HumanObservation",
    "Duration": "http://purl.oclc.org/NET/ssnx/qu/dim#Duration",
    "associatedSequences": "http://rs.tdwg.org/dwc/terms/associatedSequences",
    "TIN": "http://www.opengis.net/ont/sf#TIN",
    "phylum": "http://rs.tdwg.org/dwc/terms/phylum",
    "fieldNumber": "http://rs.tdwg.org/dwc/terms/fieldNumber",
    "relationshipRemarks": "http://rs.tdwg.org/dwc/terms/relationshipRemarks",
    "infragenericEpithet": "http://rs.tdwg.org/dwc/terms/infragenericEpithet",
    "SurfaceDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#SurfaceDensity",
    "sampleVolumeInCubicMeters": "http://mmisw.org/ont/ioos/marine_biogeography/sampleVolumeInCubicMeters",
    "resourceRelationshipID": "http://rs.tdwg.org/dwc/terms/resourceRelationshipID",
    "relationshipOfResource": "http://rs.tdwg.org/dwc/terms/relationshipOfResource",
    "habitat": "http://rs.tdwg.org/dwc/terms/habitat",
    "userName": {
      "@id": "https://w3id.org/demeter/agri/agriCommon#userName",
      "@type": "xsd:string"
    },
    "materialSampleID": "http://rs.tdwg.org/dwc/terms/materialSampleID",
    "georeferenceVerificationStatus": "http://rs.tdwg.org/dwc/terms/georeferenceVerificationStatus",
    "definition": "http://www.w3.org/2004/02/skos/core#definition",
    "bed": "http://rs.tdwg.org/dwc/terms/bed",
    "locality": "http://rs.tdwg.org/dwc/terms/locality",
    "editorialNote": "http://www.w3.org/2004/02/skos/core#editorialNote",
    "MaterialCitation": "http://rs.tdwg.org/dwc/terms/MaterialCitation",
    "samplingPerformedBy": "http://rs.tdwg.org/hc/terms/samplingPerformedBy",
    "makesMeasurement": {
      "@id": "https://saref.etsi.org/core/makesMeasurement",
      "@type": "@id"
    },
    "associatedTaxa": "http://rs.tdwg.org/dwc/terms/associatedTaxa",
    "measurementDeterminedDate": "http://rs.tdwg.org/dwc/terms/measurementDeterminedDate",
    "eventDurationUnit": "http://rs.tdwg.org/hc/terms/eventDurationUnit",
    "order": "http://rs.tdwg.org/dwc/terms/order",
    "hasGeometry": "http://www.opengis.net/ont/geosparql#hasGeometry",
    "vitality": "http://rs.tdwg.org/dwc/terms/vitality",
    "minimumDepthInMeters": "http://rs.tdwg.org/dwc/terms/minimumDepthInMeters",
    "samplingEffort": "http://rs.tdwg.org/dwc/terms/samplingEffort",
    "pressureTendency": "https://smartdatamodels.org/dataModel.Weather/pressureTendency",
    "streetAddress": "https://schema.org/streetAddress",
    "sfContains": "http://www.opengis.net/ont/geosparql#sfContains",
    "Density": "http://purl.oclc.org/NET/ssnx/qu/dim#Density",
    "LinearRing": "http://www.opengis.net/ont/sf#LinearRing",
    "eventDate": "http://rs.tdwg.org/dwc/terms/eventDate",
    "validTo": {
      "@id": "http://portele.de/ont/inspire/baseInspire#validTo",
      "@type": "xsd:dateTime"
    },
    "Occurrence": "http://rs.tdwg.org/dwc/terms/Occurrence",
    "year": "http://rs.tdwg.org/dwc/terms/year",
    "family": "http://rs.tdwg.org/dwc/terms/family",
    "inXSDDateTimeStamp": "owlTime:inXSDDateTimeStamp",
    "source": "https://smartdatamodels.org/source",
    "eppoConcept": {
      "@id": "https://w3id.org/demeter/agri/agriCommon#eppoConcept",
      "@type": "@id"
    },
    "georeferenceSources": "http://rs.tdwg.org/dwc/terms/georeferenceSources",
    "MeasureProperty": "http://purl.org/linked-data/cube#MeasureProperty",
    "resourceType": "dct:type",
    "weatherType": "https://smartdatamodels.org/dataModel.Weather/weatherType",
    "MaterialSample": "http://rs.tdwg.org/dwc/terms/MaterialSample",
    "isMeasuredIn": {
      "@id": "https://saref.etsi.org/core/isMeasuredIn",
      "@type": "@id"
    },
    "PropertyKind": "http://purl.oclc.org/NET/ssnx/qu/qu#PropertyKind",
    "publisher": "dct:publisher",
    "island": "http://rs.tdwg.org/dwc/terms/island",
    "SpatialObject": "http://www.opengis.net/ont/geosparql#SpatialObject",
    "sliceStructure": "http://purl.org/linked-data/cube#sliceStructure",
    "dewPoint": "https://smartdatamodels.org/dataModel.Weather/dewPoint",
    "NumberPerLength": "http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerLength",
    "lat": "http://www.w3.org/2003/01/geo/wgs84_pos#lat",
    "sightingDistanceInMeters": "http://mmisw.org/ont/ioos/marine_biogeography/sightingDistanceInMeters",
    "taxonRank": "http://rs.tdwg.org/dwc/terms/taxonRank",
    "VolumeFlowRate": "http://purl.oclc.org/NET/ssnx/qu/dim#VolumeFlowRate",
    "SpecificEntropy": "http://purl.oclc.org/NET/ssnx/qu/dim#SpecificEntropy",
    "locationID": "http://rs.tdwg.org/dwc/terms/locationID",
    "TemporalProperty": "https://uri.etsi.org/ngsi-ld/TemporalProperty",
    "CodedProperty": "http://purl.org/linked-data/cube#CodedProperty",
    "identificationRemarks": "http://rs.tdwg.org/dwc/terms/identificationRemarks",
    "modified": "dct:modified",
    "eventDuration": "http://rs.tdwg.org/hc/terms/eventDuration",
    "associatedOrganisms": "http://rs.tdwg.org/dwc/terms/associatedOrganisms",
    "sampleAreaInSquareMeters": "http://mmisw.org/ont/ioos/marine_biogeography/sampleAreaInSquareMeters",
    "password": {
      "@id": "https://w3id.org/demeter/agri/agriCommon#password",
      "@type": "xsd:string"
    },
    "slice": {
      "@id": "http://purl.org/linked-data/cube#slice",
      "@type": "@id"
    },
    "subgenus": "http://rs.tdwg.org/dwc/terms/subgenus",
    "observedMaxLengthInCm": "http://mmisw.org/ont/ioos/marine_biogeography/observedMaxLengthInCm",
    "accessRights": "dct:accessRights",
    "aphiaID": "http://mmisw.org/ont/ioos/marine_biogeography/aphiaID",
    "relationshipOfResourceID": "http://rs.tdwg.org/dwc/terms/relationshipOfResourceID",
    "siteCount": "http://rs.tdwg.org/hc/terms/siteCount",
    "solarRadiation": "https://smartdatamodels.org/dataModel.Weather/solarRadiation",
    "unit": {
      "@id": "http://qudt.org/schema/qudt/unit",
      "@type": "@id"
    },
    "SurfaceMedium": "http://purl.oclc.org/NET/ssnx/cf/cf-feature#SurfaceMedium",
    "date": "dct:date",
    "sampleHeightInMeters": "http://mmisw.org/ont/ioos/marine_biogeography/sampleHeightInMeters",
    "earliestAgeOrLowestStage": "http://rs.tdwg.org/dwc/terms/earliestAgeOrLowestStage",
    "relativeHumidity": "https://smartdatamodels.org/dataModel.Weather/relativeHumidity",
    "Entity": "https://uri.etsi.org/ngsi-ld/Entity",
    "kingdom": "http://rs.tdwg.org/dwc/terms/kingdom",
    "totalInSample": "http://mmisw.org/ont/ioos/marine_biogeography/totalInSample",
    "latestEonOrHighestEonothem": "http://rs.tdwg.org/dwc/terms/latestEonOrHighestEonothem",
    "taxonConceptID": "http://rs.tdwg.org/dwc/terms/taxonConceptID",
    "islandGroup": "http://rs.tdwg.org/dwc/terms/islandGroup",
    "ObservationGroup": "http://purl.org/linked-data/cube#ObservationGroup",
    "establishmentMeans": "http://rs.tdwg.org/dwc/terms/establishmentMeans",
    "relationshipEstablishedDate": "http://rs.tdwg.org/dwc/terms/relationshipEstablishedDate",
    "identifiedBy": "http://rs.tdwg.org/dwc/terms/identifiedBy",
    "sex": "http://rs.tdwg.org/dwc/terms/sex",
    "verbatimLabel": "http://rs.tdwg.org/dwc/terms/verbatimLabel",
    "relatesToProperty": {
      "@id": "https://saref.etsi.org/core/relatesToProperty",
      "@type": "@id"
    },
    "verbatimEventDate": "http://rs.tdwg.org/dwc/terms/verbatimEventDate",
    "month": "http://rs.tdwg.org/dwc/terms/month",
    "taxonID": "http://rs.tdwg.org/dwc/terms/taxonID",
    "DataSet": "http://purl.org/linked-data/cube#DataSet",
    "addressLocality": "https://schema.org/addressLocality",
    "municipality": "http://rs.tdwg.org/dwc/terms/municipality",
    "reportedWeather": "http://rs.tdwg.org/hc/terms/reportedWeather",
    "airTemperatureForecast": "https://smartdatamodels.org/dataModel.Weather/airTemperatureForecast",
    "nomenclaturalStatus": "http://rs.tdwg.org/dwc/terms/nomenclaturalStatus",
    "observedIndividualLengthInCm": "http://mmisw.org/ont/ioos/marine_biogeography/observedIndividualLengthInCm",
    "samplingProtocol": "http://rs.tdwg.org/dwc/terms/samplingProtocol",
    "earliestPeriodOrLowestSystem": "http://rs.tdwg.org/dwc/terms/earliestPeriodOrLowestSystem",
    "lifeStage": "http://rs.tdwg.org/dwc/terms/lifeStage",
    "PolyhedralSurface": "http://www.opengis.net/ont/sf#PolyhedralSurface",
    "basisOfRecord": "http://rs.tdwg.org/dwc/terms/basisOfRecord",
    "day": "http://rs.tdwg.org/dwc/terms/day",
    "controlsProperty": {
      "@id": "https://saref.etsi.org/core/controlsProperty",
      "@type": "@id"
    },
    "verticalDatum": "http://rs.tdwg.org/dwc/terms/verticalDatum",
    "language": "dct:language",
    "latestEpochOrHighestSeries": "http://rs.tdwg.org/dwc/terms/latestEpochOrHighestSeries",
    "originalNameUsage": "http://rs.tdwg.org/dwc/terms/originalNameUsage",
    "cultivarEpithet": "http://rs.tdwg.org/dwc/terms/cultivarEpithet",
    "identifiedByID": "http://rs.tdwg.org/dwc/terms/identifiedByID",
    "reproductiveCondition": "http://rs.tdwg.org/dwc/terms/reproductiveCondition",
    "latestEraOrHighestErathem": "http://rs.tdwg.org/dwc/terms/latestEraOrHighestErathem",
    "datasetID": "http://rs.tdwg.org/dwc/terms/datasetID",
    "unitKind": {
      "@id": "http://purl.oclc.org/NET/ssnx/qu/qu#unitKind",
      "@type": "@id"
    },
    "scientificNameAuthorship": "http://rs.tdwg.org/dwc/terms/scientificNameAuthorship",
    "dimension": {
      "@id": "http://purl.org/linked-data/cube#dimension",
      "@type": "@id"
    },
    "RadianceExposure": "http://purl.oclc.org/NET/ssnx/qu/dim#RadianceExposure",
    "VelocityOrSpeed": "http://purl.oclc.org/NET/ssnx/qu/dim#VelocityOrSpeed",
    "Device": "https://saref.etsi.org/core/Device",
    "collectionID": "http://rs.tdwg.org/dwc/terms/collectionID",
    "pointRadiusSpatialFit": "http://rs.tdwg.org/dwc/terms/pointRadiusSpatialFit",
    "nameAccordingToID": "http://rs.tdwg.org/dwc/terms/nameAccordingToID",
    "subtribe": "http://rs.tdwg.org/dwc/terms/subtribe",
    "georeferenceProtocol": "http://rs.tdwg.org/dwc/terms/georeferenceProtocol",
    "eventRemarks": "http://rs.tdwg.org/dwc/terms/eventRemarks",
    "minimumElevationInMeters": "http://rs.tdwg.org/dwc/terms/minimumElevationInMeters",
    "verbatimSRS": "http://rs.tdwg.org/dwc/terms/verbatimSRS",
    "degreeOfEstablishment": "http://rs.tdwg.org/dwc/terms/degreeOfEstablishment",
    "inXSDDate": "owlTime:inXSDDate",
    "GFI_DomainFeature": "http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_DomainFeature",
    "MeasurementOrFact": "http://rs.tdwg.org/dwc/terms/MeasurementOrFact",
    "observation": "http://purl.org/linked-data/cube#observation",
    "hasTimestamp": "https://saref.etsi.org/core/hasTimestamp",
    "identificationQualifier": "http://rs.tdwg.org/dwc/terms/identificationQualifier",
    "Dimensionless": "http://purl.oclc.org/NET/ssnx/qu/dim#Dimensionless",
    "Area": "http://purl.oclc.org/NET/ssnx/qu/dim#Area",
    "infraspecificEpithet": "http://rs.tdwg.org/dwc/terms/infraspecificEpithet",
    "precipitation": "https://smartdatamodels.org/dataModel.Weather/precipitation",
    "latestAgeOrHighestStage": "http://rs.tdwg.org/dwc/terms/latestAgeOrHighestStage",
    "alternateName": "https://smartdatamodels.org/alternateName",
    "Power": "http://purl.oclc.org/NET/ssnx/qu/dim#Power",
    "OM_Observation": "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation",
    "prefLabel": "http://www.w3.org/2004/02/skos/core#prefLabel",
    "Surface": "http://purl.oclc.org/NET/ssnx/cf/cf-feature#Surface",
    "addressCountry": "https://schema.org/addressCountry",
    "dataGeneralizations": "http://rs.tdwg.org/dwc/terms/dataGeneralizations",
    "SurfaceLayer": "http://purl.oclc.org/NET/ssnx/cf/cf-feature#SurfaceLayer",
    "ResourceRelationship": "http://rs.tdwg.org/dwc/terms/ResourceRelationship",
    "eventTime": "http://rs.tdwg.org/dwc/terms/eventTime",
    "sliceKey": "http://purl.org/linked-data/cube#sliceKey",
    "verbatimIdentification": "http://rs.tdwg.org/dwc/terms/verbatimIdentification",
    "PeriodOfTime": "dct:PeriodOfTime",
    "inScheme": "http://www.w3.org/2004/02/skos/core#inScheme",
    "PreservedSpecimen": "http://rs.tdwg.org/dwc/terms/PreservedSpecimen",
    "associatedReferences": "http://rs.tdwg.org/dwc/terms/associatedReferences",
    "recordedBy": "http://rs.tdwg.org/dwc/terms/recordedBy",
    "specificEpithet": "http://rs.tdwg.org/dwc/terms/specificEpithet",
    "formation": "http://rs.tdwg.org/dwc/terms/formation",
    "nomenclaturalCode": "http://rs.tdwg.org/dwc/terms/nomenclaturalCode",
    "ResponsibleParty": "http://def.seegrid.csiro.au/isotc211/iso19115/2003/citation#ResponsibleParty",
    "observedMeanLengthInCm": "http://mmisw.org/ont/ioos/marine_biogeography/observedMeanLengthInCm",
    "MultiCurve": "http://www.opengis.net/ont/sf#MultiCurve",
    "hasQuantityKind": "http://qudt.org/schema/qudt/hasQuantityKind",
    "ownerInstitutionCode": "http://rs.tdwg.org/dwc/terms/ownerInstitutionCode",
    "temporal": "dct:temporal",
    "relatedResourceID": "http://rs.tdwg.org/dwc/terms/relatedResourceID",
    "windSpeed": "https://smartdatamodels.org/dataModel.Weather/windSpeed",
    "measurementValue": "http://rs.tdwg.org/dwc/terms/measurementValue",
    "occurrenceRemarks": "http://rs.tdwg.org/dwc/terms/occurrenceRemarks",
    "DataStructureDefinition": "http://purl.org/linked-data/cube#DataStructureDefinition",
    "EnergyDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyDensity",
    "measurementRemarks": "http://rs.tdwg.org/dwc/terms/measurementRemarks",
    "illuminance": "https://smartdatamodels.org/dataModel.Weather/illuminance",
    "georeferenceRemarks": "http://rs.tdwg.org/dwc/terms/georeferenceRemarks",
    "organismScope": "http://rs.tdwg.org/dwc/terms/organismScope",
    "resourceID": "http://rs.tdwg.org/dwc/terms/resourceID",
    "associatedOccurrences": "http://rs.tdwg.org/dwc/terms/associatedOccurrences",
    "unitType": "owlTime:unitType",
    "componentProperty": "http://purl.org/linked-data/cube#componentProperty",
    "relationshipAccordingTo": "http://rs.tdwg.org/dwc/terms/relationshipAccordingTo",
    "asGeoJSON": {
      "@id": "http://www.opengis.net/ont/geosparql#asGeoJSON",
      "@type": "http://www.opengis.net/ont/geosparql#geoJSONLiteral"
    },
    "NumberPerArea": "http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerArea",
    "VolumeDensityRate": "http://purl.oclc.org/NET/ssnx/qu/dim#VolumeDensityRate",
    "foaf.name": "http://xmlns.com/foaf/0.1/name",
    "qu.QuantityKind": "http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind",
    "SpatialObjectCollection": "http://www.opengis.net/ont/geosparql#SpatialObjectCollection",
    "wgs84.Point": "http://www.w3.org/2003/01/geo/wgs84_pos#Point",
    "ssn.Property": "ssn:Property",
    "Molality": "http://purl.oclc.org/NET/ssnx/qu/dim#Molality",
    "dct.description": "dct:description",
    "qb.Observation": "http://purl.org/linked-data/cube#Observation",
    "sf.Geometry": "http://www.opengis.net/ont/sf#Geometry",
    "schema.Person": "https://schema.org/Person",
    "schema.name": "https://schema.org/name",
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn-system": "ssn:systems/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "iliad": "https://w3id.org/iliad/property/",
    "geojson": "https://purl.org/geojson/vocab#",
    "oa": "http://www.w3.org/ns/oa#",
    "dct": "http://purl.org/dc/terms/",
    "owlTime": "http://www.w3.org/2006/time#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
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

