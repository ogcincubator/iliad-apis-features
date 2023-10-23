# Modeling patterns

## Complex observations

It is common for an observation to result in a multiple items of information regarding a phenomenon.
For example, the ILIAD Jellyfish Pilot example defines observations where the primary thing of interest is "Jellyfish density", but the data collected also contains information about the taxon (species), location, sting or other species-specific details. See [this example](https://github.com/ogcincubator/iliad-apis-features/blob/master/_sources/iliad-jellyfish/examples/example.ttl)
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

When these are reported as a single multi-component `result` then it is necessary that the `observedProperty` reflect the structure of this result, with the same set of components linked to more specific observable properties. 
However, the definition of http://w3id.org/iliad/jellyfish/property/jellyFishAbundanceProperty is currently only a Concept, and does not provide the user with guidance. The "profile" defined in the repository does provide some of the information - it defines a result schema and a JSON-LD context that links each predicate and values to URLs that can be resolved. Such documentation is "out of reach" for most however as it requires synthesis of three complex standards (JSON schema, JSON-LD and whatever the actual URIs point to in terms of a model).

Alternatively, these items could each be considered to be the result of a distinct 'atomic' observation, members of an `ObservationCollection` sharing the same feature of interest, timing and sensor, but each with a distinct scalar `result` and `observedProperty`. In this case observedProperties are simple to understand but the structure is more complex, although standardised.

The data above can be encoded as shown in https://github.com/ogcincubator/iliad-apis-features/blob/master/patterns/jf-example-01.ttl 
```turtle
<http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata> a sosa:ObservationCollection, geojson:FeatureCollection ;
    rdfs:label "Jelly fish observation #1 location id: 18 sensor: 527 species: Phyllorhiza punctata"@en ;
    geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 3.180691e+01 3.463478e+01 ) ;
            rdfs:comment "pattern for cases when geometry is more strictly associated with the Feature Of Interest" ] ;
    sosa:hasFeatureOfInterest <http://w3id.org/iliad/jellyfish/feature/1-18> ;
    sosa:phenomenonTime "2011-07-01T09:00:00" ;
    sosa:resultTime "2011-07-01T09:00:00" ;
    sosa:madeBySensor <http://w3id.org/iliad/property/sensor/527> ;
    sosa:hasMember <http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata/location> ;
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
    sosa:observedProperty iliad:speciesScientificName ;
    sosa:hasResult [
        rdfs:label "Phyllorhiza punctata" ;
        iliad:wormsConcept <https://marinespecies.org/aphia.php?p=taxdetails&id=135298> ] .

<http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata/location> a sosa:Observation, geojson:Feature ;
    rdfs:label "Jelly fish observation #1 location according to sampling methodology"@en ;
    sosa:observedProperty iliad:location ;
    sosa:hasResult [
        geojson:geometry [ a geojson:Point ;
            geojson:coordinates ( 3.180691e+01 3.463478e+01 ) ] ] .

<http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata/count> a sosa:Observation, geojson:Feature ;
    rdfs:label "Jelly fish observation #1 location id: 18 property: count"@en ;
    sosa:observedProperty jf-property:quantityOfJF ;
    sosa:usedProcedure [
            jf-property:beachedJF "1" ;
            iliad:sampleSizeValue "10-30" ;
    ] ;
    sosa:hasSimpleResult 50 .

<http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata/density> a sosa:Observation, geojson:Feature ;
    rdfs:label "Jelly fish observation #1 location id: 18 property: density"@en ;
    sosa:observedProperty jf-property:densityOfJF ;
    sosa:hasResult jf-density:Some .

<http://w3id.org/iliad/jellyfish/observation/1-18-527-Phyllorhiza_punctata/sting> a sosa:Observation, geojson:Feature ;
    rdfs:label "Jelly fish observation #1 location id: 18 property: sting"@en ;
    sosa:observedProperty jf-property:stingByJF ;
    sosa:hasSimpleResult "Unspecified" .
```

While this may appear more verbose than the first example, note that each of the member `Observations` of the collection is merely an `observedProperty`/`result` pair, which couples the definition of the component to the result component directly.
For one of the `observations` additional detail is included regarding the procedure related to the `count` observation. 
All the other observation properties, including the geometry, are 'inherited' from the collection (a geometry element is required to satisfy GeoJSON requirements, so has a null value here).  

## Spatial aspects

Various OGC standards treat location in special ways - hence location could be a result of an observation or present in any object - this can reflect three possible cases:

1. Location is observed (a "measure")
2. Location is statically defined by the feature of interest (a "dimension")
3. Location is derived from the sensor

The ObservationCollection pattern can be used to distinguished these semantic nuances by either explicitly including or omitting location as an observation result.

## Conclusion

Two distinct patterns are possible:

1. A compound observableProperty with a complex result and a machine readable form of describing the structure of the observableProperty and linkages to the observationProcedure (which might define which elements must be present for a given methodology)
1. ObservationCollections - in which case more complex rules can be defined (e.g. in SHACL) th=o make sure all the elements are present.

These two approaches are isomorphic (data can be transformed between the two) but have pros and cons...

| Pattern | pros | cons | standards |
| ---- | ---- | ---- | ---- |
| compound | compact | need to define structure or follow all links in instances | TBD: RDF-Datacube? |
| collection | no complex observable needs to be defined | verbose | RDF entailments, SHACL |
