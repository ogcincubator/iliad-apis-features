
# Observations - ILIAD Jellyfish Pilot for Citizen Science (Schema)

`ogc.hosted.iliad.api.features.iliad-jellyfish-features` *v0.1*

Defines a project specific interoperability profile of the ILIAD Citizen Science profile for Observations in accordance with the Oceans Information Model

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### Example of Jellyfish abundance observation
#### json
```json
{
  "@id": "63dc376df84bda32b6bbf78ed3e279e2",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "label": {
      "en": "Jelly fish observation location id: 18 sensor: 527 species: Phyllorhiza punctata"
    },
    "phenomenonTime": "2011-07-01T09:00:00",
    "resultTime": "2011-07-01T09:00:00",
    "observedProperty": "jellyFishAbundanceProperty",
    "basisOfRecord": "HumanObservation",
    "occurrenceStatus": "present",
    "distanceWalkedInMeters": "1000-2000m",
    "hasFeatureOfInterest": {
      "type": "Feature",
      "featureType": [
        "FeatureOfInterest",
        "Point",
        "Location"
      ],
      "properties": {
        "lat": 31.806910,
        "long": 31.806910,
        "coordinateUncertaintyInMeters": 10000,
        "locality": 19,
        "distanceFromShore": "0-200"
      }
    },
    "madeBySensor": {
      "type": [
        "Sensor",
        "HumanSensor"
      ],
      "label": "Human sensor: 3602",
      "agentConfidence": "1"
    },
    "hasResult": {
      "type": [
        "Result",
        "JellyFishAbundance"
      ],
      "aphiaID": "https://marinespecies.org/aphia.php?p=taxdetails&id=232032",
      "individualCount": 20,
      "organismQuantity": "Some",
      "organismQuantityType": "individuals",
      "sampleSizeUnit": "cm",
      "sampleSizeValue": "11-30",
      "scientificName": "Rhopilema nomadica",
      "scientificNameID": "https://marinespecies.org/aphia.php?p=taxdetails&id=232032",
      "stingByJellyFish": "0",
      "strandedJellyfish": "1"
    }
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish-features/context.jsonld",
  "@id": "63dc376df84bda32b6bbf78ed3e279e2",
  "type": "Feature",
  "geometry": null,
  "properties": {
    "label": {
      "en": "Jelly fish observation location id: 18 sensor: 527 species: Phyllorhiza punctata"
    },
    "phenomenonTime": "2011-07-01T09:00:00",
    "resultTime": "2011-07-01T09:00:00",
    "observedProperty": "jellyFishAbundanceProperty",
    "basisOfRecord": "HumanObservation",
    "occurrenceStatus": "present",
    "distanceWalkedInMeters": "1000-2000m",
    "hasFeatureOfInterest": {
      "type": "Feature",
      "featureType": [
        "FeatureOfInterest",
        "Point",
        "Location"
      ],
      "properties": {
        "lat": 31.80691,
        "long": 31.80691,
        "coordinateUncertaintyInMeters": 10000,
        "locality": 19,
        "distanceFromShore": "0-200"
      }
    },
    "madeBySensor": {
      "type": [
        "Sensor",
        "HumanSensor"
      ],
      "label": "Human sensor: 3602",
      "agentConfidence": "1"
    },
    "hasResult": {
      "type": [
        "Result",
        "JellyFishAbundance"
      ],
      "aphiaID": "https://marinespecies.org/aphia.php?p=taxdetails&id=232032",
      "individualCount": 20,
      "organismQuantity": "Some",
      "organismQuantityType": "individuals",
      "sampleSizeUnit": "cm",
      "sampleSizeValue": "11-30",
      "scientificName": "Rhopilema nomadica",
      "scientificNameID": "https://marinespecies.org/aphia.php?p=taxdetails&id=232032",
      "stingByJellyFish": "0",
      "strandedJellyfish": "1"
    }
  }
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/iliad/oim/default-context/> .
@prefix dwc: <http://rs.tdwg.org/dwc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <https://w3id.org/iliad/oim/ext/jellyfish/> .
@prefix ns2: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/iliad/jellyfish/observation/63dc376df84bda32b6bbf78ed3e279e2> a geojson:Feature ;
    rdfs:label "Jelly fish observation location id: 18 sensor: 527 species: Phyllorhiza punctata"@en ;
    dwc:basisOfRecord "HumanObservation" ;
    dwc:occurrenceStatus "present" ;
    sosa:hasFeatureOfInterest [ a sosa:FeatureOfInterest,
                geojson:Feature,
                geojson:Point,
                :Location ;
            dwc:coordinateUncertaintyInMeters 10000 ;
            dwc:locality 19 ;
            ns2:lat 3.180691e+01 ;
            ns2:long 3.180691e+01 ;
            ns1:distanceFromShore "0-200" ] ;
    sosa:madeBySensor [ a sosa:Sensor,
                ns1:HumanSensor ;
            rdfs:label "Human sensor: 3602" ;
            ns1:agentConfidence "1" ] ;
    sosa:observedProperty <https://w3id.org/iliad/jellyfish/property/jellyFishAbundanceProperty> ;
    sosa:phenomenonTime <2011-07-01T09:00:00> ;
    sosa:resultTime "2011-07-01T09:00:00" ;
    :hasResult [ a sosa:Result,
                ns1:JellyFishAbundance ;
            dwc:individualCount 20 ;
            dwc:organismQuantity "Some" ;
            dwc:organismQuantityType "individuals" ;
            dwc:sampleSizeUnit "cm" ;
            dwc:sampleSizeValue "11-30" ;
            dwc:scientificName "Rhopilema nomadica" ;
            dwc:scientificNameID "https://marinespecies.org/aphia.php?p=taxdetails&id=232032" ;
            :aphiaID "https://marinespecies.org/aphia.php?p=taxdetails&id=232032" ;
            ns1:stingByJellyFish "0" ;
            ns1:strandedJellyfish "1" ] ;
    ns1:distanceWalkedInMeters "1000-2000m" .


```


### Example of Jellyfish abundance observation collection
#### json
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "@id": "63dc376df84bda32b6bbf78ed3e279e2",
      "type": "Feature",
      "featureType": "Observation",
          "geometry": {
            "type": "Point",
            "coordinates": [
              31.806910,
              34.634776
            ]
          },
      "properties": {
        "label": {
          "en": "Jelly fish observation location id: 18 sensor: 3604 species: Phyllorhiza punctata"
        },
        "phenomenonTime": "2011-07-01T09:00:00",
        "resultTime": "2011-07-01T09:00:00",
        "observedProperty": "jellyFishAbundanceProperty",
        "basisOfRecord": "HumanObservation",
        "occurrenceStatus": "present",
        "distanceWalkedInMeters": "1000-2000m",
        "hasFeatureOfInterest": {
          "type": "Feature",
          "featureType": [
            "FeatureOfInterest",
            "Point",
            "Location"
          ],
          "properties": {
            "lat": 31.806910,
            "long": 34.65,
            "coordinateUncertaintyInMeters": 10000,
            "locality": 18,
            "distanceFromShore": "0-200"
          }
        },
        "madeBySensor": {
          "type": [
            "Sensor",
            "HumanSensor"
          ],
          "label": "Human sensor: 3604",
          "agentConfidence": "1"
        },
        "hasResult": {
          "type": [
            "Result",
            "JellyFishAbundance"
          ],
          "aphiaID": "https://marinespecies.org/aphia.php?p=taxdetails&id=232032",
          "individualCount": 20,
          "organismQuantity": "Some",
          "organismQuantityType": "individuals",
          "sampleSizeUnit": "cm",
          "sampleSizeValue": "11-30",
          "scientificName": "Rhopilema nomadica",
          "scientificNameID": "https://marinespecies.org/aphia.php?p=taxdetails&id=232032",
          "stingByJellyFish": "0",
          "strandedJellyfish": "1"
        }
      }
    },
    {
      "@id": "63dc376df84bda32b6bbf78ed3e27333",
            "type": "Feature",
      "featureType": "Observation",
          "geometry": {
            "type": "Point",
            "coordinates": [
              31.806910,
              34.634776
            ]
          },
      "properties": {
        "label": {
          "en": "Jelly fish observation location id: 19 sensor: 3602 species: Phyllorhiza punctata"
        },
        "phenomenonTime": "2013-07-01T09:00:00",
        "resultTime": "2013-07-01T09:00:00",
        "observedProperty": "jellyFishAbundanceProperty",
        "basisOfRecord": "HumanObservation",
        "occurrenceStatus": "present",
        "distanceWalkedInMeters": "500-2000m",
        "hasFeatureOfInterest": {
          "type": "Feature",
          "featureType": [
            "FeatureOfInterest",
            "Point",
            "Location"
          ],
          "properties": {
            "lat": 33.806910,
            "long": 36.634776,
            "coordinateUncertaintyInMeters": 10000,
            "locality": 19,
            "distanceFromShore": "0-200"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              33.806910,
              36.634776
            ]
          }
        },
        "madeBySensor": {
          "type": [
            "Sensor",
            "HumanSensor"
          ],
          "label": "Human sensor: 3602",
          "agentConfidence": "1"
        },
        "hasResult": {
          "type": [
            "Result",
            "JellyFishAbundance"
          ],
          "aphiaID": "https://marinespecies.org/aphia.php?p=taxdetails&id=232032",
          "individualCount": 50,
          "organismQuantity": "Some",
          "organismQuantityType": "individuals",
          "sampleSizeUnit": "cm",
          "sampleSizeValue": "5-30",
          "scientificName": "Rhopilema nomadica",
          "scientificNameID": "https://marinespecies.org/aphia.php?p=taxdetails&id=232032",
          "stingByJellyFish": "0",
          "strandedJellyfish": "1"
        }
      }
    }
  ]
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish-features/context.jsonld",
  "type": "FeatureCollection",
  "features": [
    {
      "@id": "63dc376df84bda32b6bbf78ed3e279e2",
      "type": "Feature",
      "featureType": "Observation",
      "geometry": {
        "type": "Point",
        "coordinates": [
          31.80691,
          34.634776
        ]
      },
      "properties": {
        "label": {
          "en": "Jelly fish observation location id: 18 sensor: 3604 species: Phyllorhiza punctata"
        },
        "phenomenonTime": "2011-07-01T09:00:00",
        "resultTime": "2011-07-01T09:00:00",
        "observedProperty": "jellyFishAbundanceProperty",
        "basisOfRecord": "HumanObservation",
        "occurrenceStatus": "present",
        "distanceWalkedInMeters": "1000-2000m",
        "hasFeatureOfInterest": {
          "type": "Feature",
          "featureType": [
            "FeatureOfInterest",
            "Point",
            "Location"
          ],
          "properties": {
            "lat": 31.80691,
            "long": 34.65,
            "coordinateUncertaintyInMeters": 10000,
            "locality": 18,
            "distanceFromShore": "0-200"
          }
        },
        "madeBySensor": {
          "type": [
            "Sensor",
            "HumanSensor"
          ],
          "label": "Human sensor: 3604",
          "agentConfidence": "1"
        },
        "hasResult": {
          "type": [
            "Result",
            "JellyFishAbundance"
          ],
          "aphiaID": "https://marinespecies.org/aphia.php?p=taxdetails&id=232032",
          "individualCount": 20,
          "organismQuantity": "Some",
          "organismQuantityType": "individuals",
          "sampleSizeUnit": "cm",
          "sampleSizeValue": "11-30",
          "scientificName": "Rhopilema nomadica",
          "scientificNameID": "https://marinespecies.org/aphia.php?p=taxdetails&id=232032",
          "stingByJellyFish": "0",
          "strandedJellyfish": "1"
        }
      }
    },
    {
      "@id": "63dc376df84bda32b6bbf78ed3e27333",
      "type": "Feature",
      "featureType": "Observation",
      "geometry": {
        "type": "Point",
        "coordinates": [
          31.80691,
          34.634776
        ]
      },
      "properties": {
        "label": {
          "en": "Jelly fish observation location id: 19 sensor: 3602 species: Phyllorhiza punctata"
        },
        "phenomenonTime": "2013-07-01T09:00:00",
        "resultTime": "2013-07-01T09:00:00",
        "observedProperty": "jellyFishAbundanceProperty",
        "basisOfRecord": "HumanObservation",
        "occurrenceStatus": "present",
        "distanceWalkedInMeters": "500-2000m",
        "hasFeatureOfInterest": {
          "type": "Feature",
          "featureType": [
            "FeatureOfInterest",
            "Point",
            "Location"
          ],
          "properties": {
            "lat": 33.80691,
            "long": 36.634776,
            "coordinateUncertaintyInMeters": 10000,
            "locality": 19,
            "distanceFromShore": "0-200"
          },
          "geometry": {
            "type": "Point",
            "coordinates": [
              33.80691,
              36.634776
            ]
          }
        },
        "madeBySensor": {
          "type": [
            "Sensor",
            "HumanSensor"
          ],
          "label": "Human sensor: 3602",
          "agentConfidence": "1"
        },
        "hasResult": {
          "type": [
            "Result",
            "JellyFishAbundance"
          ],
          "aphiaID": "https://marinespecies.org/aphia.php?p=taxdetails&id=232032",
          "individualCount": 50,
          "organismQuantity": "Some",
          "organismQuantityType": "individuals",
          "sampleSizeUnit": "cm",
          "sampleSizeValue": "5-30",
          "scientificName": "Rhopilema nomadica",
          "scientificNameID": "https://marinespecies.org/aphia.php?p=taxdetails&id=232032",
          "stingByJellyFish": "0",
          "strandedJellyfish": "1"
        }
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/iliad/oim/default-context/> .
@prefix dwc: <http://rs.tdwg.org/dwc/terms/> .
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix ns1: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix ns2: <https://w3id.org/iliad/oim/ext/jellyfish/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://w3id.org/iliad/jellyfish/observation/63dc376df84bda32b6bbf78ed3e27333> a sosa:Observation,
        geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 3.180691e+01 3.463478e+01 ) ] ;
    :properties [ rdfs:label "Jelly fish observation location id: 19 sensor: 3602 species: Phyllorhiza punctata"@en ;
            dwc:basisOfRecord "HumanObservation" ;
            dwc:occurrenceStatus "present" ;
            sosa:hasFeatureOfInterest [ a sosa:FeatureOfInterest,
                        geojson:Feature,
                        geojson:Point,
                        :Location ;
                    geojson:geometry [ a geojson:Point ;
                            geojson:coordinates ( 3.380691e+01 3.663478e+01 ) ] ;
                    :properties [ dwc:coordinateUncertaintyInMeters 10000 ;
                            dwc:locality 19 ;
                            ns1:lat 3.380691e+01 ;
                            ns1:long 3.663478e+01 ;
                            ns2:distanceFromShore "0-200" ] ] ;
            sosa:madeBySensor [ a sosa:Sensor,
                        ns2:HumanSensor ;
                    rdfs:label "Human sensor: 3602" ;
                    ns2:agentConfidence "1" ] ;
            sosa:observedProperty <https://w3id.org/iliad/jellyfish/property/jellyFishAbundanceProperty> ;
            sosa:phenomenonTime <2013-07-01T09:00:00> ;
            sosa:resultTime "2013-07-01T09:00:00" ;
            :hasResult [ a sosa:Result,
                        ns2:JellyFishAbundance ;
                    dwc:individualCount 50 ;
                    dwc:organismQuantity "Some" ;
                    dwc:organismQuantityType "individuals" ;
                    dwc:sampleSizeUnit "cm" ;
                    dwc:sampleSizeValue "5-30" ;
                    dwc:scientificName "Rhopilema nomadica" ;
                    dwc:scientificNameID "https://marinespecies.org/aphia.php?p=taxdetails&id=232032" ;
                    :aphiaID "https://marinespecies.org/aphia.php?p=taxdetails&id=232032" ;
                    ns2:stingByJellyFish "0" ;
                    ns2:strandedJellyfish "1" ] ;
            ns2:distanceWalkedInMeters "500-2000m" ] .

<https://w3id.org/iliad/jellyfish/observation/63dc376df84bda32b6bbf78ed3e279e2> a sosa:Observation,
        geojson:Feature ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 3.180691e+01 3.463478e+01 ) ] ;
    :properties [ rdfs:label "Jelly fish observation location id: 18 sensor: 3604 species: Phyllorhiza punctata"@en ;
            dwc:basisOfRecord "HumanObservation" ;
            dwc:occurrenceStatus "present" ;
            sosa:hasFeatureOfInterest [ a sosa:FeatureOfInterest,
                        geojson:Feature,
                        geojson:Point,
                        :Location ;
                    :properties [ dwc:coordinateUncertaintyInMeters 10000 ;
                            dwc:locality 18 ;
                            ns1:lat 3.180691e+01 ;
                            ns1:long 3.465e+01 ;
                            ns2:distanceFromShore "0-200" ] ] ;
            sosa:madeBySensor [ a sosa:Sensor,
                        ns2:HumanSensor ;
                    rdfs:label "Human sensor: 3604" ;
                    ns2:agentConfidence "1" ] ;
            sosa:observedProperty <https://w3id.org/iliad/jellyfish/property/jellyFishAbundanceProperty> ;
            sosa:phenomenonTime <2011-07-01T09:00:00> ;
            sosa:resultTime "2011-07-01T09:00:00" ;
            :hasResult [ a sosa:Result,
                        ns2:JellyFishAbundance ;
                    dwc:individualCount 20 ;
                    dwc:organismQuantity "Some" ;
                    dwc:organismQuantityType "individuals" ;
                    dwc:sampleSizeUnit "cm" ;
                    dwc:sampleSizeValue "11-30" ;
                    dwc:scientificName "Rhopilema nomadica" ;
                    dwc:scientificNameID "https://marinespecies.org/aphia.php?p=taxdetails&id=232032" ;
                    :aphiaID "https://marinespecies.org/aphia.php?p=taxdetails&id=232032" ;
                    ns2:stingByJellyFish "0" ;
                    ns2:strandedJellyfish "1" ] ;
            ns2:distanceWalkedInMeters "1000-2000m" ] .

[] a geojson:FeatureCollection ;
    sosa:hasMember <https://w3id.org/iliad/jellyfish/observation/63dc376df84bda32b6bbf78ed3e27333>,
        <https://w3id.org/iliad/jellyfish/observation/63dc376df84bda32b6bbf78ed3e279e2> .


```


### Example of Jellyfish abundance observation ontology
This TTL to be replaced by examples from the ontology development cycle.

Note that the structure of a sosa:Observation is still relevant.

#### ttl
```ttl
@prefix geojson: <https://purl.org/geojson/vocab#> .
@prefix iliad: <https://w3id.org/iliad/property/> .
@prefix jf-property: <https://w3id.org/iliad/jellyfish/property/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix wgs84_pos: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix dct: <http://purl.org/dc/terms/Location> .
@prefix dwc: <http://rs.tdwg.org/dwc/terms/> .
@prefix dwc_mb: <http://mmisw.org/ont/ioos/marine_biogeography/> .
@prefix iliad_jf: <https://w3id.org/iliad/oim/ext/jellyfish/> . 

<https://w3id.org/iliad/jellyfish/observation/63dc376df84bda32b6bbf78ed3e279e2> a sosa:Observation ;
    rdfs:label "Jelly fish observation #1 location id: 18 sensor: 527 species: Phyllorhiza punctata"@en ;
    dct:identifier "63dc376df84bda32b6bbf78ed3e279e2" ;
    sosa:observedProperty jf-property:jellyFishAbundanceProperty ;
    sosa:phenomenonTime "2011-07-01T09:00:00" ;
    sosa:resultTime "2011-07-01T09:00:00" ;
    dwc:basisOfRecord "HumanObservation" ;
    dwc:occurrenceStatus "present" ;
    iliad_jf:distanceWalkedInMeters "1000-2000m" ;
    sosa:hasFeatureOfInterest [ 
        a wgs84_pos:Point, sosa:FeatureOfInterest, dct:Location, geojson:Feature ;
        wgs84_pos:lat 31.8008805 ;
        wgs84_pos:long 34.62660548 ;        
        dwc:coordinateUncertaintyInMeters 10000 ;
        dwc:locality 19 ;
        iliad_jf:distanceFromShore "0-200" ;
        geojson:geometry [ 
            a geojson:Point ;
            geojson:coordinates ( 3.18008805e+01 3.462660548e+01 ) 
        ]     
    ];
    sosa:madeBySensor [
        a sosa:Sensor, iliad_jf:HumanSensor ;
        rdfs:label "Human sensor: 3602"@en ;
        iliad_jf:agentConfidence: "1"
    ];
    sosa:hasResult [ 
        a sosa:Result, iliad_jf:JellyFishAbundance ;
        dwc_mb:aphiaID "https://marinespecies.org/aphia.php?p=taxdetails&id=232032" ;            
        dwc:individualCount 20 ;
        dwc:organismQuantity "Some" ;
        dwc:organismQuantityType "individuals" ;
        dwc:sampleSizeUnit "cm" ;
        dwc:sampleSizeValue "11-30" ;
        dwc:scientificName "Rhopilema nomadica" ;
        dwc:scientificNameID "https://marinespecies.org/aphia.php?p=taxdetails&id=232032" ;
        iliad_jf:stingByJellyFish "0" ;
        iliad_jf:strandedJellyfish "1"     
    ] .
    
    


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Schemas for Ocean Information Model Observations
$defs:
  OIMObsProps:
    allOf:
    - $ref: https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-obs-cs/schema.yaml#/$defs/OIMObsProps
    - $ref: https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-bio-tdwg/schema.yaml
    - properties:
        hasResult:
          type: object
          properties:
            densityOfJellyFish:
              type: string
              enum:
              - None
              - Some
              - Swarm
              - Few
              x-jsonld-id: https://w3id.org/iliad/oim/default-context/densityOfJellyFish
            stingByJellyFish:
              type: string
              x-jsonld-id: https://w3id.org/iliad/oim/ext/jellyfish/stingByJellyFish
            strandedJellyFish:
              type: string
              x-jsonld-id: https://w3id.org/iliad/oim/default-context/strandedJellyFish
          x-jsonld-id: https://w3id.org/iliad/oim/default-context/hasResult
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
  HumanSensor: https://w3id.org/iliad/oim/ext/jellyfish/HumanSensor
  distanceWalkedInMeters: https://w3id.org/iliad/oim/ext/jellyfish/distanceWalkedInMeters
  distanceFromShore: https://w3id.org/iliad/oim/ext/jellyfish/distanceFromShore
  agentConfidence: https://w3id.org/iliad/oim/ext/jellyfish/agentConfidence
x-jsonld-vocab: https://w3id.org/iliad/oim/default-context/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish-features/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish-features/schema.yaml)


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
      "@id": "sosa:hasFeatureOfInterest",
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
        "hasResult": {
          "@id": "sosa:hasResult",
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
      "@id": "https://w3id.org/iliad/oim/default-context/hasResult",
      "@type": "@id",
      "@context": {
        "densityOfJellyFish": "https://w3id.org/iliad/oim/default-context/densityOfJellyFish",
        "stingByJellyFish": "https://w3id.org/iliad/oim/ext/jellyfish/stingByJellyFish",
        "strandedJellyFish": "https://w3id.org/iliad/oim/default-context/strandedJellyFish"
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
    "sampleSizeValue": "dwc:sampleSizeValue",
    "wormsConcept": {
      "@id": "iliad:wormsConcept",
      "@type": "@id"
    },
    "verbatimSiteDescriptions": "hc:verbatimSiteDescriptions",
    "verbatimSiteNames": "hc:verbatimSiteNames",
    "samplingPerformedBy": "hc:samplingPerformedBy",
    "eventDurationUnit": "hc:eventDurationUnit",
    "eventDuration": "hc:eventDuration",
    "siteCount": "hc:siteCount",
    "reportedWeather": "hc:reportedWeather",
    "sampleSizeUnit": "dwc:sampleSizeUnit",
    "recordNumber": "dwc:recordNumber",
    "verbatimLongitude": "dwc:verbatimLongitude",
    "behavior": "dwc:behavior",
    "organismQuantity": "dwc:organismQuantity",
    "scientificNameID": "dwc:scientificNameID",
    "lowestBiostratigraphicZone": "dwc:lowestBiostratigraphicZone",
    "earliestEonOrLowestEonothem": "dwc:earliestEonOrLowestEonothem",
    "originalNameUsageID": "dwc:originalNameUsageID",
    "GeologicalContext": "dwc:GeologicalContext",
    "countryCode": "dwc:countryCode",
    "verbatimCoordinates": "dwc:verbatimCoordinates",
    "maximumDistanceAboveSurfaceInMeters": "dwc:maximumDistanceAboveSurfaceInMeters",
    "verbatimLocality": "dwc:verbatimLocality",
    "identificationReferences": "dwc:identificationReferences",
    "verbatimCoordinateSystem": "dwc:verbatimCoordinateSystem",
    "measurementType": "dwc:measurementType",
    "measurementAccuracy": "dwc:measurementAccuracy",
    "member": "dwc:member",
    "genus": "dwc:genus",
    "coordinatePrecision": "dwc:coordinatePrecision",
    "georeferencedDate": "dwc:georeferencedDate",
    "taxonomicStatus": "dwc:taxonomicStatus",
    "previousIdentifications": "dwc:previousIdentifications",
    "startDayOfYear": "dwc:startDayOfYear",
    "otherCatalogNumbers": "dwc:otherCatalogNumbers",
    "MachineObservation": "dwc:MachineObservation",
    "coordinateUncertaintyInMeters": "dwc:coordinateUncertaintyInMeters",
    "eventID": "dwc:eventID",
    "Organism": "dwc:Organism",
    "identificationID": "dwc:identificationID",
    "recordedByID": "dwc:recordedByID",
    "Identification": "dwc:Identification",
    "country": "dwc:country",
    "genericName": "dwc:genericName",
    "decimalLongitude": "dwc:decimalLongitude",
    "scientificName": "dwc:scientificName",
    "organismQuantityType": "dwc:organismQuantityType",
    "catalogNumber": "dwc:catalogNumber",
    "continent": "dwc:continent",
    "minimumDistanceAboveSurfaceInMeters": "dwc:minimumDistanceAboveSurfaceInMeters",
    "decimalLatitude": "dwc:decimalLatitude",
    "higherGeographyID": "dwc:higherGeographyID",
    "measurementDeterminedBy": "dwc:measurementDeterminedBy",
    "geodeticDatum": "dwc:geodeticDatum",
    "maximumDepthInMeters": "dwc:maximumDepthInMeters",
    "locationAccordingTo": "dwc:locationAccordingTo",
    "nameAccordingTo": "dwc:nameAccordingTo",
    "group": "dwc:group",
    "class": "dwc:class",
    "footprintWKT": "dwc:footprintWKT",
    "FossilSpecimen": "dwc:FossilSpecimen",
    "typeStatus": "dwc:typeStatus",
    "acceptedNameUsage": "dwc:acceptedNameUsage",
    "earliestEpochOrLowestSeries": "dwc:earliestEpochOrLowestSeries",
    "parentNameUsageID": "dwc:parentNameUsageID",
    "dynamicProperties": "dwc:dynamicProperties",
    "caste": "dwc:caste",
    "footprintSpatialFit": "dwc:footprintSpatialFit",
    "namePublishedInYear": "dwc:namePublishedInYear",
    "highestBiostratigraphicZone": "dwc:highestBiostratigraphicZone",
    "fieldNotes": "dwc:fieldNotes",
    "measurementID": "dwc:measurementID",
    "parentNameUsage": "dwc:parentNameUsage",
    "acceptedNameUsageID": "dwc:acceptedNameUsageID",
    "maximumElevationInMeters": "dwc:maximumElevationInMeters",
    "identificationVerificationStatus": "dwc:identificationVerificationStatus",
    "footprintSRS": "dwc:footprintSRS",
    "individualCount": "dwc:individualCount",
    "collectionCode": "dwc:collectionCode",
    "lithostratigraphicTerms": "dwc:lithostratigraphicTerms",
    "subfamily": "dwc:subfamily",
    "eventType": "dwc:eventType",
    "associatedMedia": "dwc:associatedMedia",
    "Taxon": "dwc:Taxon",
    "vernacularName": "dwc:vernacularName",
    "preparations": "dwc:preparations",
    "Event": "dwc:Event",
    "institutionID": "dwc:institutionID",
    "verbatimDepth": "dwc:verbatimDepth",
    "county": "dwc:county",
    "earliestEraOrLowestErathem": "dwc:earliestEraOrLowestErathem",
    "occurrenceStatus": "dwc:occurrenceStatus",
    "verbatimTaxonRank": "dwc:verbatimTaxonRank",
    "disposition": "dwc:disposition",
    "namePublishedInID": "dwc:namePublishedInID",
    "dateIdentified": "dwc:dateIdentified",
    "organismRemarks": "dwc:organismRemarks",
    "latestPeriodOrHighestSystem": "dwc:latestPeriodOrHighestSystem",
    "taxonRemarks": "dwc:taxonRemarks",
    "georeferencedBy": "dwc:georeferencedBy",
    "verbatimElevation": "dwc:verbatimElevation",
    "higherClassification": "dwc:higherClassification",
    "waterBody": "dwc:waterBody",
    "namePublishedIn": "dwc:namePublishedIn",
    "organismID": "dwc:organismID",
    "stateProvince": "dwc:stateProvince",
    "endDayOfYear": "dwc:endDayOfYear",
    "geologicalContextID": "dwc:geologicalContextID",
    "pathway": "dwc:pathway",
    "parentEventID": "dwc:parentEventID",
    "datasetName": "dwc:datasetName",
    "measurementMethod": "dwc:measurementMethod",
    "verbatimLatitude": "dwc:verbatimLatitude",
    "parentMeasurementID": "dwc:parentMeasurementID",
    "tribe": "dwc:tribe",
    "superfamily": "dwc:superfamily",
    "LivingSpecimen": "dwc:LivingSpecimen",
    "locationRemarks": "dwc:locationRemarks",
    "higherGeography": "dwc:higherGeography",
    "informationWithheld": "dwc:informationWithheld",
    "organismName": "dwc:organismName",
    "institutionCode": "dwc:institutionCode",
    "occurrenceID": "dwc:occurrenceID",
    "measurementUnit": "dwc:measurementUnit",
    "HumanObservation": "dwc:HumanObservation",
    "associatedSequences": "dwc:associatedSequences",
    "phylum": "dwc:phylum",
    "fieldNumber": "dwc:fieldNumber",
    "relationshipRemarks": "dwc:relationshipRemarks",
    "infragenericEpithet": "dwc:infragenericEpithet",
    "resourceRelationshipID": "dwc:resourceRelationshipID",
    "relationshipOfResource": "dwc:relationshipOfResource",
    "habitat": "dwc:habitat",
    "materialSampleID": "dwc:materialSampleID",
    "georeferenceVerificationStatus": "dwc:georeferenceVerificationStatus",
    "bed": "dwc:bed",
    "locality": "dwc:locality",
    "MaterialCitation": "dwc:MaterialCitation",
    "associatedTaxa": "dwc:associatedTaxa",
    "measurementDeterminedDate": "dwc:measurementDeterminedDate",
    "order": "dwc:order",
    "vitality": "dwc:vitality",
    "minimumDepthInMeters": "dwc:minimumDepthInMeters",
    "samplingEffort": "dwc:samplingEffort",
    "eventDate": "dwc:eventDate",
    "Occurrence": "dwc:Occurrence",
    "year": "dwc:year",
    "family": "dwc:family",
    "georeferenceSources": "dwc:georeferenceSources",
    "MaterialSample": "dwc:MaterialSample",
    "island": "dwc:island",
    "taxonRank": "dwc:taxonRank",
    "locationID": "dwc:locationID",
    "identificationRemarks": "dwc:identificationRemarks",
    "associatedOrganisms": "dwc:associatedOrganisms",
    "subgenus": "dwc:subgenus",
    "relationshipOfResourceID": "dwc:relationshipOfResourceID",
    "earliestAgeOrLowestStage": "dwc:earliestAgeOrLowestStage",
    "kingdom": "dwc:kingdom",
    "latestEonOrHighestEonothem": "dwc:latestEonOrHighestEonothem",
    "taxonConceptID": "dwc:taxonConceptID",
    "islandGroup": "dwc:islandGroup",
    "establishmentMeans": "dwc:establishmentMeans",
    "relationshipEstablishedDate": "dwc:relationshipEstablishedDate",
    "identifiedBy": "dwc:identifiedBy",
    "sex": "dwc:sex",
    "verbatimLabel": "dwc:verbatimLabel",
    "verbatimEventDate": "dwc:verbatimEventDate",
    "month": "dwc:month",
    "taxonID": "dwc:taxonID",
    "municipality": "dwc:municipality",
    "nomenclaturalStatus": "dwc:nomenclaturalStatus",
    "samplingProtocol": "dwc:samplingProtocol",
    "earliestPeriodOrLowestSystem": "dwc:earliestPeriodOrLowestSystem",
    "lifeStage": "dwc:lifeStage",
    "basisOfRecord": "dwc:basisOfRecord",
    "day": "dwc:day",
    "verticalDatum": "dwc:verticalDatum",
    "latestEpochOrHighestSeries": "dwc:latestEpochOrHighestSeries",
    "originalNameUsage": "dwc:originalNameUsage",
    "cultivarEpithet": "dwc:cultivarEpithet",
    "identifiedByID": "dwc:identifiedByID",
    "reproductiveCondition": "dwc:reproductiveCondition",
    "latestEraOrHighestErathem": "dwc:latestEraOrHighestErathem",
    "datasetID": "dwc:datasetID",
    "scientificNameAuthorship": "dwc:scientificNameAuthorship",
    "collectionID": "dwc:collectionID",
    "pointRadiusSpatialFit": "dwc:pointRadiusSpatialFit",
    "nameAccordingToID": "dwc:nameAccordingToID",
    "subtribe": "dwc:subtribe",
    "georeferenceProtocol": "dwc:georeferenceProtocol",
    "eventRemarks": "dwc:eventRemarks",
    "minimumElevationInMeters": "dwc:minimumElevationInMeters",
    "verbatimSRS": "dwc:verbatimSRS",
    "degreeOfEstablishment": "dwc:degreeOfEstablishment",
    "MeasurementOrFact": "dwc:MeasurementOrFact",
    "identificationQualifier": "dwc:identificationQualifier",
    "infraspecificEpithet": "dwc:infraspecificEpithet",
    "latestAgeOrHighestStage": "dwc:latestAgeOrHighestStage",
    "dataGeneralizations": "dwc:dataGeneralizations",
    "ResourceRelationship": "dwc:ResourceRelationship",
    "eventTime": "dwc:eventTime",
    "verbatimIdentification": "dwc:verbatimIdentification",
    "PreservedSpecimen": "dwc:PreservedSpecimen",
    "associatedReferences": "dwc:associatedReferences",
    "recordedBy": "dwc:recordedBy",
    "specificEpithet": "dwc:specificEpithet",
    "formation": "dwc:formation",
    "nomenclaturalCode": "dwc:nomenclaturalCode",
    "ownerInstitutionCode": "dwc:ownerInstitutionCode",
    "relatedResourceID": "dwc:relatedResourceID",
    "measurementValue": "dwc:measurementValue",
    "occurrenceRemarks": "dwc:occurrenceRemarks",
    "measurementRemarks": "dwc:measurementRemarks",
    "georeferenceRemarks": "dwc:georeferenceRemarks",
    "organismScope": "dwc:organismScope",
    "resourceID": "dwc:resourceID",
    "associatedOccurrences": "dwc:associatedOccurrences",
    "relationshipAccordingTo": "dwc:relationshipAccordingTo",
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
    "HumanSensor": "https://w3id.org/iliad/oim/ext/jellyfish/HumanSensor",
    "distanceWalkedInMeters": "https://w3id.org/iliad/oim/ext/jellyfish/distanceWalkedInMeters",
    "distanceFromShore": "https://w3id.org/iliad/oim/ext/jellyfish/distanceFromShore",
    "agentConfidence": "https://w3id.org/iliad/oim/ext/jellyfish/agentConfidence",
    "PhotonFluxDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#PhotonFluxDensity",
    "invalidatedAtTime": {
      "@id": "http://www.w3.org/ns/prov#invalidatedAtTime",
      "@type": "xsd:dateTime"
    },
    "Attachable": "http://purl.org/linked-data/cube#Attachable",
    "QuantityValue": "http://qudt.org/schema/qudt/QuantityValue",
    "affiliation": "https://schema.org/affiliation",
    "Unit": "http://qudt.org/schema/qudt/Unit",
    "Line": "http://www.opengis.net/ont/sf#Line",
    "versionInfo": "http://www.w3.org/2002/07/owl#versionInfo",
    "generatedAtTime": {
      "@id": "http://www.w3.org/ns/prov#generatedAtTime",
      "@type": "xsd:dateTime"
    },
    "example": "http://www.w3.org/2004/02/skos/core#example",
    "Slice": "http://purl.org/linked-data/cube#Slice",
    "Concentration": "http://purl.oclc.org/NET/ssnx/qu/dim#Concentration",
    "dataSet": {
      "@id": "http://purl.org/linked-data/cube#dataSet",
      "@type": "@id"
    },
    "componentAttachment": {
      "@id": "http://purl.org/linked-data/cube#componentAttachment",
      "@type": "@id"
    },
    "concept": {
      "@id": "http://purl.org/linked-data/cube#concept",
      "@type": "@id"
    },
    "MultiSurface": "http://www.opengis.net/ont/sf#MultiSurface",
    "TemporalDuration": "owlTime:TemporalDuration",
    "Procedure": "sosa:Procedure",
    "DiffusionCoefficient": "http://purl.oclc.org/NET/ssnx/qu/dim#DiffusionCoefficient",
    "asGeoJSON": {
      "@id": "http://www.opengis.net/ont/geosparql#asGeoJSON",
      "@type": "http://www.opengis.net/ont/geosparql#geoJSONLiteral"
    },
    "Organization": "https://schema.org/Organization",
    "Volume": "http://purl.oclc.org/NET/ssnx/qu/dim#Volume",
    "Thing": "http://www.w3.org/2002/07/owl#Thing",
    "GFI_Feature": "http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_Feature",
    "AttributeProperty": "http://purl.org/linked-data/cube#AttributeProperty",
    "quantityValue": {
      "@id": "http://qudt.org/schema/qudt/quantityValue",
      "@type": "@id"
    },
    "TemporalUnit": "owlTime:TemporalUnit",
    "asWKT": {
      "@id": "http://www.opengis.net/ont/geosparql#asWKT",
      "@type": "http://www.opengis.net/ont/geosparql#wktLiteral"
    },
    "Angle": "http://purl.oclc.org/NET/ssnx/qu/dim#Angle",
    "TemperatureDrift": "http://purl.oclc.org/NET/ssnx/qu/dim#TemperatureDrift",
    "RotationalSpeed": "http://purl.oclc.org/NET/ssnx/qu/dim#RotationalSpeed",
    "ComponentProperty": "http://purl.org/linked-data/cube#ComponentProperty",
    "Class": "rdfs:Class",
    "Geometry": "http://www.opengis.net/ont/geosparql#Geometry",
    "NumberPerArea": "http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerArea",
    "depiction": "http://xmlns.com/foaf/0.1/depiction",
    "Curve": "http://www.opengis.net/ont/sf#Curve",
    "Instant": "owlTime:Instant",
    "maker": "http://xmlns.com/foaf/0.1/maker",
    "sfWithin": {
      "@id": "http://www.opengis.net/ont/geosparql#sfWithin",
      "@type": "@id"
    },
    "hasBoundingBox": {
      "@id": "http://www.opengis.net/ont/geosparql#hasBoundingBox",
      "@type": "@id"
    },
    "ThermalConductivity": "http://purl.oclc.org/NET/ssnx/qu/dim#ThermalConductivity",
    "domainIncludes": "https://schema.org/domainIncludes",
    "long": "http://www.w3.org/2003/01/geo/wgs84_pos#long",
    "numericValue": "http://qudt.org/schema/qudt/numericValue",
    "Concept": "http://www.w3.org/2004/02/skos/core#Concept",
    "component": {
      "@id": "http://purl.org/linked-data/cube#component",
      "@type": "@id"
    },
    "measure": {
      "@id": "http://purl.org/linked-data/cube#measure",
      "@type": "@id"
    },
    "attribute": {
      "@id": "http://purl.org/linked-data/cube#attribute",
      "@type": "@id"
    },
    "structure": {
      "@id": "http://purl.org/linked-data/cube#structure",
      "@type": "@id"
    },
    "SliceKey": "http://purl.org/linked-data/cube#SliceKey",
    "Result": "sosa:Result",
    "Compressibility": "http://purl.oclc.org/NET/ssnx/qu/dim#Compressibility",
    "ComponentSet": "http://purl.org/linked-data/cube#ComponentSet",
    "MassPerTimePerArea": "http://purl.oclc.org/NET/ssnx/qu/dim#MassPerTimePerArea",
    "numericDuration": {
      "@id": "owlTime:numericDuration",
      "@type": "xsd:decimal"
    },
    "ElectricConductivity": "http://purl.oclc.org/NET/ssnx/qu/dim#ElectricConductivity",
    "Temperature": "http://purl.oclc.org/NET/ssnx/qu/dim#Temperature",
    "homepage": "http://xmlns.com/foaf/0.1/homepage",
    "Measure": "http://def.seegrid.csiro.au/isotc211/iso19103/2005/basic#Measure",
    "Person": "http://xmlns.com/foaf/0.1/Person",
    "Triangle": "http://www.opengis.net/ont/sf#Triangle",
    "note": "http://www.w3.org/2004/02/skos/core#note",
    "observationGroup": {
      "@id": "http://purl.org/linked-data/cube#observationGroup",
      "@type": "@id"
    },
    "Interval": "owlTime:Interval",
    "EnergyFlux": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyFlux",
    "StressOrPressure": "http://purl.oclc.org/NET/ssnx/qu/dim#StressOrPressure",
    "VolumeDensityRate": "http://purl.oclc.org/NET/ssnx/qu/dim#VolumeDensityRate",
    "Agent": "http://xmlns.com/foaf/0.1/Agent",
    "creator": "dct:creator",
    "Energy": "http://purl.oclc.org/NET/ssnx/qu/dim#Energy",
    "foaf.name": "http://xmlns.com/foaf/0.1/name",
    "Role": "https://schema.org/Role",
    "hasSerialization": {
      "@id": "http://www.opengis.net/ont/geosparql#hasSerialization",
      "@type": "rdfs:Literal"
    },
    "hasTime": {
      "@id": "owlTime:hasTime",
      "@type": "@id"
    },
    "SF_SamplingFeature.sampledFeature": {
      "@id": "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature.sampledFeature",
      "@type": "@id"
    },
    "rangeIncludes": "https://schema.org/rangeIncludes",
    "Mass": "http://purl.oclc.org/NET/ssnx/qu/dim#Mass",
    "location": {
      "@id": "http://www.w3.org/2003/01/geo/wgs84_pos#location",
      "@type": "@id"
    },
    "ComponentSpecification": "http://purl.org/linked-data/cube#ComponentSpecification",
    "Scheme": "http://www.w3.org/2004/02/skos/core#Scheme",
    "hasEnd": {
      "@id": "owlTime:hasEnd",
      "@type": "@id"
    },
    "rights": "dct:rights",
    "TemporalEntity": "owlTime:TemporalEntity",
    "hasBeginning": {
      "@id": "owlTime:hasBeginning",
      "@type": "@id"
    },
    "SF_SamplingFeature": "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature",
    "DimensionProperty": "http://purl.org/linked-data/cube#DimensionProperty",
    "alt": "http://www.w3.org/2003/01/geo/wgs84_pos#alt",
    "Acceleration": "http://purl.oclc.org/NET/ssnx/qu/dim#Acceleration",
    "identifier": "dct:identifier",
    "Quantity": "http://qudt.org/schema/qudt/Quantity",
    "MassFlowRate": "http://purl.oclc.org/NET/ssnx/qu/dim#MassFlowRate",
    "qu.QuantityKind": "http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind",
    "SpatialObjectCollection": "http://www.opengis.net/ont/geosparql#SpatialObjectCollection",
    "Distance": "http://purl.oclc.org/NET/ssnx/qu/dim#Distance",
    "deprecated": "http://www.w3.org/2002/07/owl#deprecated",
    "Radiance": "http://purl.oclc.org/NET/ssnx/qu/dim#Radiance",
    "Duration": "owlTime:Duration",
    "TIN": "http://www.opengis.net/ont/sf#TIN",
    "SurfaceDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#SurfaceDensity",
    "isDefinedBy": "rdfs:isDefinedBy",
    "wgs84.Point": "http://www.w3.org/2003/01/geo/wgs84_pos#Point",
    "definition": "http://www.w3.org/2004/02/skos/core#definition",
    "editorialNote": "http://www.w3.org/2004/02/skos/core#editorialNote",
    "hasGeometry": {
      "@id": "http://www.opengis.net/ont/geosparql#hasGeometry",
      "@type": "@id"
    },
    "ssn.Property": "ssn:Property",
    "sfContains": {
      "@id": "http://www.opengis.net/ont/geosparql#sfContains",
      "@type": "@id"
    },
    "title": "dct:title",
    "Density": "http://purl.oclc.org/NET/ssnx/qu/dim#Density",
    "LinearRing": "http://www.opengis.net/ont/sf#LinearRing",
    "Molality": "http://purl.oclc.org/NET/ssnx/qu/dim#Molality",
    "inXSDDateTimeStamp": {
      "@id": "owlTime:inXSDDateTimeStamp",
      "@type": "xsd:dateTimeStamp"
    },
    "MeasureProperty": "http://purl.org/linked-data/cube#MeasureProperty",
    "PropertyKind": "http://purl.oclc.org/NET/ssnx/qu/qu#PropertyKind",
    "SpatialObject": "http://www.opengis.net/ont/geosparql#SpatialObject",
    "sliceStructure": {
      "@id": "http://purl.org/linked-data/cube#sliceStructure",
      "@type": "@id"
    },
    "NumberPerLength": "http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerLength",
    "lat": "http://www.w3.org/2003/01/geo/wgs84_pos#lat",
    "VolumeFlowRate": "http://purl.oclc.org/NET/ssnx/qu/dim#VolumeFlowRate",
    "SpecificEntropy": "http://purl.oclc.org/NET/ssnx/qu/dim#SpecificEntropy",
    "CodedProperty": "http://purl.org/linked-data/cube#CodedProperty",
    "slice": {
      "@id": "http://purl.org/linked-data/cube#slice",
      "@type": "@id"
    },
    "unit": {
      "@id": "http://qudt.org/schema/qudt/unit",
      "@type": "@id"
    },
    "date": "dct:date",
    "seeAlso": "rdfs:seeAlso",
    "ObservationGroup": "http://purl.org/linked-data/cube#ObservationGroup",
    "DataSet": "http://purl.org/linked-data/cube#DataSet",
    "comment": "rdfs:comment",
    "PolyhedralSurface": "http://www.opengis.net/ont/sf#PolyhedralSurface",
    "contributor": "dct:contributor",
    "unitKind": {
      "@id": "http://purl.oclc.org/NET/ssnx/qu/qu#unitKind",
      "@type": "@id"
    },
    "dimension": {
      "@id": "http://purl.org/linked-data/cube#dimension",
      "@type": "@id"
    },
    "RadianceExposure": "http://purl.oclc.org/NET/ssnx/qu/dim#RadianceExposure",
    "VelocityOrSpeed": "http://purl.oclc.org/NET/ssnx/qu/dim#VelocityOrSpeed",
    "inXSDDate": {
      "@id": "owlTime:inXSDDate",
      "@type": "xsd:date"
    },
    "GFI_DomainFeature": "http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_DomainFeature",
    "observation": {
      "@id": "http://purl.org/linked-data/cube#observation",
      "@type": "@id"
    },
    "Dimensionless": "http://purl.oclc.org/NET/ssnx/qu/dim#Dimensionless",
    "Area": "http://purl.oclc.org/NET/ssnx/qu/dim#Area",
    "Power": "http://purl.oclc.org/NET/ssnx/qu/dim#Power",
    "OM_Observation": "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation",
    "prefLabel": "http://www.w3.org/2004/02/skos/core#prefLabel",
    "Surface": "http://www.opengis.net/ont/sf#Surface",
    "sliceKey": {
      "@id": "http://purl.org/linked-data/cube#sliceKey",
      "@type": "@id"
    },
    "inScheme": "http://www.w3.org/2004/02/skos/core#inScheme",
    "dct.description": "dct:description",
    "MultiCurve": "http://www.opengis.net/ont/sf#MultiCurve",
    "hasQuantityKind": {
      "@id": "http://qudt.org/schema/qudt/hasQuantityKind",
      "@type": "@id"
    },
    "DataStructureDefinition": "http://purl.org/linked-data/cube#DataStructureDefinition",
    "qb.Observation": "http://purl.org/linked-data/cube#Observation",
    "EnergyDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyDensity",
    "unitType": {
      "@id": "owlTime:unitType",
      "@type": "@id"
    },
    "componentProperty": {
      "@id": "http://purl.org/linked-data/cube#componentProperty",
      "@type": "@id"
    },
    "sf.Geometry": "http://www.opengis.net/ont/sf#Geometry",
    "schema.Person": "https://schema.org/Person",
    "schema.name": "https://schema.org/name",
    "QuantityKind": "http://qudt.org/schema/qudt/QuantityKind",
    "speciesScientificName": "iliad:speciesScientificName",
    "aphiaId": {
      "@id": "iliad:wormsConcept",
      "@type": "@id"
    },
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn-system": "ssn:systems/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "iliad": "https://w3id.org/iliad/property/",
    "hc": "http://rs.tdwg.org/hc/terms/",
    "dwc": "http://rs.tdwg.org/dwc/terms/",
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
[context.jsonld](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/iliad-jellyfish-features/context.jsonld)

## Sources

* [OIM master repository](https://github.com/ILIAD-ocean-twin/OIM)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/iliad-apis-features](https://github.com/ogcincubator/iliad-apis-features)
* Path: `_sources/iliad-jellyfish-features`

