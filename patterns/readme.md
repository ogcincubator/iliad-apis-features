# Modeling patterns

## Complex observations

It is common for an observation to result in a multiple items of information regarding a phenomenon.
For example, Iliad makes observations where the primary thing of interest is Jellyfish density, but the data collected also contains information about the taxon (species), location, sting or other species-specific details. See [this example](https://github.com/ogcincubator/iliad-apis-features/blob/master/_sources/iliad-jellyfish/examples/example.ttl)
```turtle
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

When these are reported as a single multi-component `result` then it is necessary that the `observedProperty` reflect the structure of this result, with the same set of components, in the same order (unless some other indexing method is used). 
However, the definition of http://w3id.org/iliad/jellyfish/property/jellyFishAbundanceProperty does not appear to accomplish this. 

Alternatively, these items could each be considered to be the result of a distinct 'atomic' observation, members of an `ObservationCollection` sharing the same feature of interest, timing and sensor, but each with a distinct scalar `result` and `observedProperty`. 
The data above can be encoded as shown in https://github.com/ogcincubator/iliad-apis-features/blob/master/patterns/jf-example-01.ttl 
```turtle
<http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata> a sosa:ObservationCollection, geojson:FeatureCollection ;
    rdfs:label "Jelly fish observation #1 location id: 18 sensor: 527 species: Phyllorhiza punctata"@en ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 3.180691e+01 3.463478e+01 ) ;
            rdfs:comment "geometry is more strictly associated with the Feature Of Interest" ] ;
    sosa:hasFeatureOfInterest <http://w3id.org/iliad/jellyfish/feature/1-18> ;
    sosa:phenomenonTime "2011-07-01T09:00:00" ;
    sosa:resultTime "2011-07-01T09:00:00" ;
    sosa:madeBySensor <http://w3id.org/iliad/property/sensor/527> ;
    sosa:hasMember <http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata/taxon> ;
    sosa:hasMember <http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata/count> ;
    sosa:hasMember <http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata/density> ;
    sosa:hasMember <http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata/sting> .

<http://w3id.org/iliad/jellyfish/feature/1-18> a geojson:Feature ;
    rdfs:label "Jelly fish observation #1 location id: 18"@en ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 3.180691e+01 3.463478e+01 ) ] .

<http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata/taxon> a sosa:Observation, geojson:Feature ;
    rdfs:label "Jelly fish observation #1 location id: 18 property: taxon"@en ;
    geojson:geometry [ a geojson:Point ; geojson:coordinates ( ) ] ;
    sosa:observedProperty iliad:speciesScientificName ;
    sosa:hasResult [
        rdfs:label "Phyllorhiza punctata" ;
        iliad:wormsConcept <https://marinespecies.org/aphia.php?p=taxdetails&id=135298> ] .

<http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata/count> a sosa:Observation, geojson:Feature ;
    rdfs:label "Jelly fish observation #1 location id: 18 property: count"@en ;
    geojson:geometry [ a geojson:Point ; geojson:coordinates ( ) ] ;
    sosa:observedProperty jf-property:quantityOfJF ;
    sosa:usedProcedure [
            jf-property:beachedJF "1" ;
            iliad:sampleSizeValue "10-30" ;
    ] ;
    sosa:hasSimpleResult 50 .

<http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata/density> a sosa:Observation, geojson:Feature ;
    rdfs:label "Jelly fish observation #1 location id: 18 property: density"@en ;
    geojson:geometry [ a geojson:Point ; geojson:coordinates ( ) ] ;
    sosa:observedProperty jf-property:densityOfJF ;
    sosa:hasResult jf-density:Some .

<http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata/sting> a sosa:Observation, geojson:Feature ;
    rdfs:label "Jelly fish observation #1 location id: 18 property: sting"@en ;
    geojson:geometry [ a geojson:Point ; geojson:coordinates ( ) ] ;
    sosa:observedProperty jf-property:stingByJF ;
    sosa:hasSimpleResult "Unspecified" .
```

While this may appear more verbose than the first example, note that each of the member `Observations` of the collection is essentially an `observedProperty`/`result` pair, which couples the definition of the component to the result component directly.
For one of the `observations` additional detail is included regarding the procedure related to the `count` observation. 
All the other observation properties, including the geometry, are 'inherited' from the collection (a geometry element is required to satisfy GeoJSON requirements, so has a null value here).  
