
# OIM STA Observations (Schema)

`ogc.hosted.iliad.api.features.oim-sta-obs` *v0.1*

Defines SensorThings API Observations to implement the OIM SOSA cross-domain model in a form compatible with ILIAD and other digital twins using this model.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Ocean Information Model Observations Profile

Currently a stub where requirements for OIM implementation can be defined as required.

Note specific profiles will define specific requirements for interaction with external systems.

The JSON-LD Context declares the default baseURI of Observation with generic STA context and OIM specific context.

TODO: (MVP)
1 - implement the observableProperties Register as a concept scheme under OGC hosted
2 - define a SHACL or other rule that requires observableProperties to be registered in the ILIAD observable properties register.

Note that it may have an externally resolvable URI or be a proxy handled by ILIAD (using the OGC RAINBOW)

The mechanisms for handling external vocabulary constraints to be define here: (TBD)

## Examples

### Coverage JSON Coverage representing snapshot series of Grid with LD
#### json
```json
{
  "@iot.id": "1",
  "@iot.selfLink": "http://example.org/v1.1/Observations(1)",
  "FeatureOfInterest@iot.navigationLink": "Observations(1)/FeatureOfInterest",
  "Datastream@iot.navigationLink": "Observations(1)/Datastream",
  "phenomenonTime": "2014-12-31T11:59:59.00+08:00",
  "resultTime": "2014-12-31T11:59:59.00+08:00",
  "result": 70.4
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-sta-obs/context.jsonld",
  "@iot.id": "1",
  "@iot.selfLink": "http://example.org/v1.1/Observations(1)",
  "FeatureOfInterest@iot.navigationLink": "Observations(1)/FeatureOfInterest",
  "Datastream@iot.navigationLink": "Observations(1)/Datastream",
  "phenomenonTime": "2014-12-31T11:59:59.00+08:00",
  "resultTime": "2014-12-31T11:59:59.00+08:00",
  "result": 70.4
}
```

#### ttl
```ttl
@prefix sosa1: <https://www.w3.org/TR/vocab-ssn/#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://w3id.org/ogcincubator/coverageJSON/1> sosa1:hasFeatureOfInterest "Observations(1)/FeatureOfInterest" ;
    sosa1:hasSimpleResult 7.04e+01 ;
    sosa1:isMemberOf "Observations(1)/Datastream" ;
    sosa1:phenomenonTime "2014-12-31T11:59:59.00+08:00" ;
    sosa1:resultTime "2014-12-31T11:59:59.00+08:00" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: A OIM aligned STA Observtion schema
description: Component of OGC STA Observation. no particular added constraints are
  added
$ref: https://ogcincubator.github.io/bblocks-sta/build/annotated/api/sta/Observation/schema.json
x-jsonld-extra-terms:
  PhotonFluxDensity: http://purl.oclc.org/NET/ssnx/qu/dim#PhotonFluxDensity
  implements:
    x-jsonld-id: http://www.w3.org/ns/ssn/implements
    x-jsonld-type: '@id'
  invalidatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#invalidatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  MultiLineString: http://www.opengis.net/ont/sf#MultiLineString
  Attachable: http://purl.org/linked-data/cube#Attachable
  QuantityValue: http://qudt.org/schema/qudt/QuantityValue
  affiliation: https://schema.org/affiliation
  Unit: http://qudt.org/schema/qudt/Unit
  Line: http://www.opengis.net/ont/sf#Line
  member:
    x-jsonld-id: http://xmlns.com/foaf/0.1/member
    x-jsonld-type: '@id'
  versionInfo: http://www.w3.org/2002/07/owl#versionInfo
  generatedAtTime:
    x-jsonld-id: http://www.w3.org/ns/prov#generatedAtTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  example: http://www.w3.org/2004/02/skos/core#example
  Slice: http://purl.org/linked-data/cube#Slice
  Concentration: http://purl.oclc.org/NET/ssnx/qu/dim#Concentration
  dataSet:
    x-jsonld-id: http://purl.org/linked-data/cube#dataSet
    x-jsonld-type: '@id'
  componentAttachment:
    x-jsonld-id: http://purl.org/linked-data/cube#componentAttachment
    x-jsonld-type: '@id'
  Platform: http://www.w3.org/ns/sosa/Platform
  concept:
    x-jsonld-id: http://purl.org/linked-data/cube#concept
    x-jsonld-type: '@id'
  Deployment: http://www.w3.org/ns/ssn/Deployment
  MultiSurface: http://www.opengis.net/ont/sf#MultiSurface
  TemporalDuration: http://www.w3.org/2006/time#TemporalDuration
  Procedure: http://www.w3.org/ns/sosa/Procedure
  DiffusionCoefficient: http://purl.oclc.org/NET/ssnx/qu/dim#DiffusionCoefficient
  asGeoJSON:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#asGeoJSON
    x-jsonld-type: http://www.opengis.net/ont/geosparql#geoJSONLiteral
  Organization: https://schema.org/Organization
  Volume: http://purl.oclc.org/NET/ssnx/qu/dim#Volume
  Thing: http://www.w3.org/2002/07/owl#Thing
  GFI_Feature: http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_Feature
  AttributeProperty: http://purl.org/linked-data/cube#AttributeProperty
  quantityValue:
    x-jsonld-id: http://qudt.org/schema/qudt/quantityValue
    x-jsonld-type: '@id'
  TemporalUnit: http://www.w3.org/2006/time#TemporalUnit
  hosts:
    x-jsonld-id: http://www.w3.org/ns/sosa/hosts
    x-jsonld-type: '@id'
  asWKT:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#asWKT
    x-jsonld-type: http://www.opengis.net/ont/geosparql#wktLiteral
  hasOutput:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasOutput
    x-jsonld-type: '@id'
  Angle: http://purl.oclc.org/NET/ssnx/qu/dim#Angle
  TemperatureDrift: http://purl.oclc.org/NET/ssnx/qu/dim#TemperatureDrift
  RotationalSpeed: http://purl.oclc.org/NET/ssnx/qu/dim#RotationalSpeed
  FeatureOfInterest: http://www.w3.org/ns/sosa/FeatureOfInterest
  ComponentProperty: http://purl.org/linked-data/cube#ComponentProperty
  Class: http://www.w3.org/2000/01/rdf-schema#Class
  ObservationCollection: http://www.w3.org/ns/sosa/ObservationCollection
  Geometry: http://www.opengis.net/ont/geosparql#Geometry
  NumberPerArea: http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerArea
  depiction: http://xmlns.com/foaf/0.1/depiction
  Curve: http://www.opengis.net/ont/sf#Curve
  Instant: http://www.w3.org/2006/time#Instant
  maker: http://xmlns.com/foaf/0.1/maker
  sfWithin:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#sfWithin
    x-jsonld-type: '@id'
  ThermalConductivity: http://purl.oclc.org/NET/ssnx/qu/dim#ThermalConductivity
  hasUltimateFeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasUltimateFeatureOfInterest
    x-jsonld-type: '@id'
  domainIncludes: https://schema.org/domainIncludes
  madeBySensor:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
    x-jsonld-type: '@id'
  long: http://www.w3.org/2003/01/geo/wgs84_pos#long
  ActuatableProperty: http://www.w3.org/ns/sosa/ActuatableProperty
  Feature: http://www.opengis.net/ont/geosparql#Feature
  label: http://www.w3.org/2000/01/rdf-schema#label
  LineString: http://www.opengis.net/ont/sf#LineString
  numericValue: http://qudt.org/schema/qudt/numericValue
  Concept: http://www.w3.org/2004/02/skos/core#Concept
  component:
    x-jsonld-id: http://purl.org/linked-data/cube#component
    x-jsonld-type: '@id'
  measure:
    x-jsonld-id: http://purl.org/linked-data/cube#measure
    x-jsonld-type: '@id'
  SliceKey: http://purl.org/linked-data/cube#SliceKey
  Result: http://www.w3.org/ns/sosa/Result
  isHostedBy:
    x-jsonld-id: http://www.w3.org/ns/sosa/isHostedBy
    x-jsonld-type: '@id'
  Compressibility: http://purl.oclc.org/NET/ssnx/qu/dim#Compressibility
  inDeployment:
    x-jsonld-id: http://www.w3.org/ns/ssn/inDeployment
    x-jsonld-type: '@id'
  ComponentSet: http://purl.org/linked-data/cube#ComponentSet
  MassPerTimePerArea: http://purl.oclc.org/NET/ssnx/qu/dim#MassPerTimePerArea
  numericDuration:
    x-jsonld-id: http://www.w3.org/2006/time#numericDuration
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  ElectricConductivity: http://purl.oclc.org/NET/ssnx/qu/dim#ElectricConductivity
  Temperature: http://purl.oclc.org/NET/ssnx/qu/dim#Temperature
  homepage: http://xmlns.com/foaf/0.1/homepage
  hasProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasProperty
    x-jsonld-type: '@id'
  Measure: http://def.seegrid.csiro.au/isotc211/iso19103/2005/basic#Measure
  Person: http://xmlns.com/foaf/0.1/Person
  Triangle: http://www.opengis.net/ont/sf#Triangle
  note: http://www.w3.org/2004/02/skos/core#note
  observationGroup:
    x-jsonld-id: http://purl.org/linked-data/cube#observationGroup
    x-jsonld-type: '@id'
  Interval: http://www.w3.org/2006/time#Interval
  EnergyFlux: http://purl.oclc.org/NET/ssnx/qu/dim#EnergyFlux
  StressOrPressure: http://purl.oclc.org/NET/ssnx/qu/dim#StressOrPressure
  resultTime: https://www.w3.org/TR/vocab-ssn/#resultTime
  VolumeDensityRate: http://purl.oclc.org/NET/ssnx/qu/dim#VolumeDensityRate
  Agent: http://xmlns.com/foaf/0.1/Agent
  creator: http://purl.org/dc/terms/creator
  phenomenonTime: https://www.w3.org/TR/vocab-ssn/#phenomenonTime
  Energy: http://purl.oclc.org/NET/ssnx/qu/dim#Energy
  foaf.name: http://xmlns.com/foaf/0.1/name
  Role: https://schema.org/Role
  hasSerialization:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#hasSerialization
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  hasTime:
    x-jsonld-id: http://www.w3.org/2006/time#hasTime
    x-jsonld-type: '@id'
  SF_SamplingFeature.sampledFeature:
    x-jsonld-id: http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature.sampledFeature
    x-jsonld-type: '@id'
  hasMember:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
    x-jsonld-type: '@id'
  rangeIncludes: https://schema.org/rangeIncludes
  hasInput:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasInput
    x-jsonld-type: '@id'
  Mass: http://purl.oclc.org/NET/ssnx/qu/dim#Mass
  implementedBy:
    x-jsonld-id: http://www.w3.org/ns/ssn/implementedBy
    x-jsonld-type: '@id'
  location:
    x-jsonld-id: http://www.w3.org/2003/01/geo/wgs84_pos#location
    x-jsonld-type: '@id'
  ComponentSpecification: http://purl.org/linked-data/cube#ComponentSpecification
  Scheme: http://www.w3.org/2004/02/skos/core#Scheme
  hasEnd:
    x-jsonld-id: http://www.w3.org/2006/time#hasEnd
    x-jsonld-type: '@id'
  GeometryCollection: http://www.opengis.net/ont/sf#GeometryCollection
  rights: http://purl.org/dc/terms/rights
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
  Acceleration: http://purl.oclc.org/NET/ssnx/qu/dim#Acceleration
  identifier: http://purl.org/dc/terms/identifier
  hasSubSystem:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasSubSystem
    x-jsonld-type: '@id'
  Quantity: http://qudt.org/schema/qudt/Quantity
  MassFlowRate: http://purl.oclc.org/NET/ssnx/qu/dim#MassFlowRate
  qu.QuantityKind: http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind
  SpatialObjectCollection: http://www.opengis.net/ont/geosparql#SpatialObjectCollection
  Distance: http://purl.oclc.org/NET/ssnx/qu/dim#Distance
  deprecated: http://www.w3.org/2002/07/owl#deprecated
  Radiance: http://purl.oclc.org/NET/ssnx/qu/dim#Radiance
  Duration: http://www.w3.org/2006/time#Duration
  TIN: http://www.opengis.net/ont/sf#TIN
  SurfaceDensity: http://purl.oclc.org/NET/ssnx/qu/dim#SurfaceDensity
  isDefinedBy: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
  wgs84.Point: http://www.w3.org/2003/01/geo/wgs84_pos#Point
  definition: http://www.w3.org/2004/02/skos/core#definition
  editorialNote: http://www.w3.org/2004/02/skos/core#editorialNote
  observes:
    x-jsonld-id: http://www.w3.org/ns/sosa/observes
    x-jsonld-type: '@id'
  hasDeployment:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasDeployment
    x-jsonld-type: '@id'
  hasResult:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasResult
    x-jsonld-type: '@id'
  order:
    x-jsonld-id: http://purl.org/linked-data/cube#order
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#int
  hasGeometry:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#hasGeometry
    x-jsonld-type: '@id'
  usedProcedure:
    x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
    x-jsonld-type: '@id'
  ssn.Property: http://www.w3.org/ns/ssn/Property
  sfContains:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#sfContains
    x-jsonld-type: '@id'
  title: http://purl.org/dc/terms/title
  Density: http://purl.oclc.org/NET/ssnx/qu/dim#Density
  LinearRing: http://www.opengis.net/ont/sf#LinearRing
  Molality: http://purl.oclc.org/NET/ssnx/qu/dim#Molality
  inXSDDateTimeStamp:
    x-jsonld-id: http://www.w3.org/2006/time#inXSDDateTimeStamp
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTimeStamp
  MeasureProperty: http://purl.org/linked-data/cube#MeasureProperty
  PropertyKind: http://purl.oclc.org/NET/ssnx/qu/qu#PropertyKind
  SpatialObject: http://www.opengis.net/ont/geosparql#SpatialObject
  sliceStructure:
    x-jsonld-id: http://purl.org/linked-data/cube#sliceStructure
    x-jsonld-type: '@id'
  hasFeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    x-jsonld-type: '@id'
  NumberPerLength: http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerLength
  lat: http://www.w3.org/2003/01/geo/wgs84_pos#lat
  VolumeFlowRate: http://purl.oclc.org/NET/ssnx/qu/dim#VolumeFlowRate
  SpecificEntropy: http://purl.oclc.org/NET/ssnx/qu/dim#SpecificEntropy
  CodedProperty: http://purl.org/linked-data/cube#CodedProperty
  observedProperty:
    x-jsonld-id: http://www.w3.org/ns/sosa/observedProperty
    x-jsonld-type: '@id'
  slice:
    x-jsonld-id: http://purl.org/linked-data/cube#slice
    x-jsonld-type: '@id'
  madeObservation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
    x-jsonld-type: '@id'
  FeatureCollection: http://www.opengis.net/ont/geosparql#FeatureCollection
  unit:
    x-jsonld-id: http://qudt.org/schema/qudt/unit
    x-jsonld-type: '@id'
  date: http://purl.org/dc/terms/date
  isPropertyOf:
    x-jsonld-id: http://www.w3.org/ns/ssn/isPropertyOf
    x-jsonld-type: '@id'
  seeAlso: http://www.w3.org/2000/01/rdf-schema#seeAlso
  ObservationGroup: http://purl.org/linked-data/cube#ObservationGroup
  Sample: http://www.w3.org/ns/sosa/Sample
  DataSet: http://purl.org/linked-data/cube#DataSet
  comment: http://www.w3.org/2000/01/rdf-schema#comment
  PolyhedralSurface: http://www.opengis.net/ont/sf#PolyhedralSurface
  Polygon: http://www.opengis.net/ont/sf#Polygon
  MultiPolygon: http://www.opengis.net/ont/sf#MultiPolygon
  ObservableProperty: http://www.w3.org/ns/sosa/ObservableProperty
  contributor: http://purl.org/dc/terms/contributor
  deployedSystem:
    x-jsonld-id: http://www.w3.org/ns/ssn/deployedSystem
    x-jsonld-type: '@id'
  System: http://www.w3.org/ns/ssn/System
  unitKind:
    x-jsonld-id: http://purl.oclc.org/NET/ssnx/qu/qu#unitKind
    x-jsonld-type: '@id'
  dimension:
    x-jsonld-id: http://purl.org/linked-data/cube#dimension
    x-jsonld-type: '@id'
  RadianceExposure: http://purl.oclc.org/NET/ssnx/qu/dim#RadianceExposure
  VelocityOrSpeed: http://purl.oclc.org/NET/ssnx/qu/dim#VelocityOrSpeed
  deployedOnPlatform:
    x-jsonld-id: http://www.w3.org/ns/ssn/deployedOnPlatform
    x-jsonld-type: '@id'
  inXSDDate:
    x-jsonld-id: http://www.w3.org/2006/time#inXSDDate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
  GFI_DomainFeature: http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_DomainFeature
  Actuation: http://www.w3.org/ns/sosa/Actuation
  observation:
    x-jsonld-id: http://purl.org/linked-data/cube#observation
    x-jsonld-type: '@id'
  Dimensionless: http://purl.oclc.org/NET/ssnx/qu/dim#Dimensionless
  Area: http://purl.oclc.org/NET/ssnx/qu/dim#Area
  Sampling: http://www.w3.org/ns/sosa/Sampling
  Power: http://purl.oclc.org/NET/ssnx/qu/dim#Power
  OM_Observation: http://def.isotc211.org/iso19156/2011/Observation#OM_Observation
  prefLabel: http://www.w3.org/2004/02/skos/core#prefLabel
  Surface: http://www.opengis.net/ont/sf#Surface
  sliceKey:
    x-jsonld-id: http://purl.org/linked-data/cube#sliceKey
    x-jsonld-type: '@id'
  inScheme: http://www.w3.org/2004/02/skos/core#inScheme
  dct.description: http://purl.org/dc/terms/description
  MultiCurve: http://www.opengis.net/ont/sf#MultiCurve
  hasQuantityKind:
    x-jsonld-id: http://qudt.org/schema/qudt/hasQuantityKind
    x-jsonld-type: '@id'
  DataStructureDefinition: http://purl.org/linked-data/cube#DataStructureDefinition
  MultiPoint: http://www.opengis.net/ont/sf#MultiPoint
  qb.Observation: http://purl.org/linked-data/cube#Observation
  EnergyDensity: http://purl.oclc.org/NET/ssnx/qu/dim#EnergyDensity
  Sensor: http://www.w3.org/ns/sosa/Sensor
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  unitType:
    x-jsonld-id: http://www.w3.org/2006/time#unitType
    x-jsonld-type: '@id'
  componentProperty:
    x-jsonld-id: http://purl.org/linked-data/cube#componentProperty
    x-jsonld-type: '@id'
  isFeatureOfInterestOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    x-jsonld-type: '@id'
  sf.Geometry: http://www.opengis.net/ont/sf#Geometry
  schema.Person: https://schema.org/Person
  Observation: http://www.w3.org/ns/sosa/Observation
  Point: http://www.opengis.net/ont/sf#Point
  schema.name: https://schema.org/name
  QuantityKind: http://qudt.org/schema/qudt/QuantityKind
  '@iot.id': '@id'
  '@iot.selfLink': http://www.opengis.net/def/rel/iana/1.0/self
  result: https://www.w3.org/TR/vocab-ssn/#hasSimpleResult
  resultQuality: https://www.w3.org/TR/vocab-ssn/#resultQuality
  validTime: https://schemas.opengis.org/sta/def/core#validTime
  Datastream@iot.navigationLink: https://www.w3.org/TR/vocab-ssn/#isMemberOf
  FeatureOfInterest@iot.navigationLink: https://www.w3.org/TR/vocab-ssn/#hasFeatureOfInterest
x-jsonld-prefixes:
  orel: http://www.opengis.net/def/rel/
  sosa: https://www.w3.org/TR/vocab-ssn/#
  sta: https://schemas.opengis.org/sta/def/core#
  rel: http://www.iana.org/assignments/relation/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-sta-obs/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-sta-obs/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@iot.id": "@id",
    "@iot.selfLink": "orel:iana/1.0/self",
    "phenomenonTime": "sosa:phenomenonTime",
    "result": "sosa:hasSimpleResult",
    "resultQuality": "sosa:resultQuality",
    "resultTime": "sosa:resultTime",
    "validTime": "sta:validTime",
    "Datastream@iot.navigationLink": "sosa:isMemberOf",
    "FeatureOfInterest@iot.navigationLink": "sosa:hasFeatureOfInterest",
    "PhotonFluxDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#PhotonFluxDensity",
    "implements": {
      "@id": "http://www.w3.org/ns/ssn/implements",
      "@type": "@id"
    },
    "invalidatedAtTime": {
      "@id": "http://www.w3.org/ns/prov#invalidatedAtTime",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "MultiLineString": "http://www.opengis.net/ont/sf#MultiLineString",
    "Attachable": "http://purl.org/linked-data/cube#Attachable",
    "QuantityValue": "http://qudt.org/schema/qudt/QuantityValue",
    "affiliation": "https://schema.org/affiliation",
    "Unit": "http://qudt.org/schema/qudt/Unit",
    "Line": "http://www.opengis.net/ont/sf#Line",
    "member": {
      "@id": "http://xmlns.com/foaf/0.1/member",
      "@type": "@id"
    },
    "versionInfo": "http://www.w3.org/2002/07/owl#versionInfo",
    "generatedAtTime": {
      "@id": "http://www.w3.org/ns/prov#generatedAtTime",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
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
    "Platform": "http://www.w3.org/ns/sosa/Platform",
    "concept": {
      "@id": "http://purl.org/linked-data/cube#concept",
      "@type": "@id"
    },
    "Deployment": "http://www.w3.org/ns/ssn/Deployment",
    "MultiSurface": "http://www.opengis.net/ont/sf#MultiSurface",
    "TemporalDuration": "http://www.w3.org/2006/time#TemporalDuration",
    "Procedure": "http://www.w3.org/ns/sosa/Procedure",
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
    "TemporalUnit": "http://www.w3.org/2006/time#TemporalUnit",
    "hosts": {
      "@id": "http://www.w3.org/ns/sosa/hosts",
      "@type": "@id"
    },
    "asWKT": {
      "@id": "http://www.opengis.net/ont/geosparql#asWKT",
      "@type": "http://www.opengis.net/ont/geosparql#wktLiteral"
    },
    "hasOutput": {
      "@id": "http://www.w3.org/ns/ssn/hasOutput",
      "@type": "@id"
    },
    "Angle": "http://purl.oclc.org/NET/ssnx/qu/dim#Angle",
    "TemperatureDrift": "http://purl.oclc.org/NET/ssnx/qu/dim#TemperatureDrift",
    "RotationalSpeed": "http://purl.oclc.org/NET/ssnx/qu/dim#RotationalSpeed",
    "FeatureOfInterest": "http://www.w3.org/ns/sosa/FeatureOfInterest",
    "ComponentProperty": "http://purl.org/linked-data/cube#ComponentProperty",
    "Class": "http://www.w3.org/2000/01/rdf-schema#Class",
    "ObservationCollection": "http://www.w3.org/ns/sosa/ObservationCollection",
    "Geometry": "http://www.opengis.net/ont/geosparql#Geometry",
    "NumberPerArea": "http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerArea",
    "depiction": "http://xmlns.com/foaf/0.1/depiction",
    "Curve": "http://www.opengis.net/ont/sf#Curve",
    "Instant": "http://www.w3.org/2006/time#Instant",
    "maker": "http://xmlns.com/foaf/0.1/maker",
    "sfWithin": {
      "@id": "http://www.opengis.net/ont/geosparql#sfWithin",
      "@type": "@id"
    },
    "ThermalConductivity": "http://purl.oclc.org/NET/ssnx/qu/dim#ThermalConductivity",
    "hasUltimateFeatureOfInterest": {
      "@id": "http://www.w3.org/ns/sosa/hasUltimateFeatureOfInterest",
      "@type": "@id"
    },
    "domainIncludes": "https://schema.org/domainIncludes",
    "madeBySensor": {
      "@id": "http://www.w3.org/ns/sosa/madeBySensor",
      "@type": "@id"
    },
    "long": "http://www.w3.org/2003/01/geo/wgs84_pos#long",
    "ActuatableProperty": "http://www.w3.org/ns/sosa/ActuatableProperty",
    "Feature": "http://www.opengis.net/ont/geosparql#Feature",
    "label": "http://www.w3.org/2000/01/rdf-schema#label",
    "LineString": "http://www.opengis.net/ont/sf#LineString",
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
    "SliceKey": "http://purl.org/linked-data/cube#SliceKey",
    "Result": "http://www.w3.org/ns/sosa/Result",
    "isHostedBy": {
      "@id": "http://www.w3.org/ns/sosa/isHostedBy",
      "@type": "@id"
    },
    "Compressibility": "http://purl.oclc.org/NET/ssnx/qu/dim#Compressibility",
    "inDeployment": {
      "@id": "http://www.w3.org/ns/ssn/inDeployment",
      "@type": "@id"
    },
    "ComponentSet": "http://purl.org/linked-data/cube#ComponentSet",
    "MassPerTimePerArea": "http://purl.oclc.org/NET/ssnx/qu/dim#MassPerTimePerArea",
    "numericDuration": {
      "@id": "http://www.w3.org/2006/time#numericDuration",
      "@type": "http://www.w3.org/2001/XMLSchema#decimal"
    },
    "ElectricConductivity": "http://purl.oclc.org/NET/ssnx/qu/dim#ElectricConductivity",
    "Temperature": "http://purl.oclc.org/NET/ssnx/qu/dim#Temperature",
    "homepage": "http://xmlns.com/foaf/0.1/homepage",
    "hasProperty": {
      "@id": "http://www.w3.org/ns/ssn/hasProperty",
      "@type": "@id"
    },
    "Measure": "http://def.seegrid.csiro.au/isotc211/iso19103/2005/basic#Measure",
    "Person": "http://xmlns.com/foaf/0.1/Person",
    "Triangle": "http://www.opengis.net/ont/sf#Triangle",
    "note": "http://www.w3.org/2004/02/skos/core#note",
    "observationGroup": {
      "@id": "http://purl.org/linked-data/cube#observationGroup",
      "@type": "@id"
    },
    "Interval": "http://www.w3.org/2006/time#Interval",
    "EnergyFlux": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyFlux",
    "StressOrPressure": "http://purl.oclc.org/NET/ssnx/qu/dim#StressOrPressure",
    "VolumeDensityRate": "http://purl.oclc.org/NET/ssnx/qu/dim#VolumeDensityRate",
    "Agent": "http://xmlns.com/foaf/0.1/Agent",
    "creator": "http://purl.org/dc/terms/creator",
    "Energy": "http://purl.oclc.org/NET/ssnx/qu/dim#Energy",
    "foaf.name": "http://xmlns.com/foaf/0.1/name",
    "Role": "https://schema.org/Role",
    "hasSerialization": {
      "@id": "http://www.opengis.net/ont/geosparql#hasSerialization",
      "@type": "http://www.w3.org/2000/01/rdf-schema#Literal"
    },
    "hasTime": {
      "@id": "http://www.w3.org/2006/time#hasTime",
      "@type": "@id"
    },
    "SF_SamplingFeature.sampledFeature": {
      "@id": "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature.sampledFeature",
      "@type": "@id"
    },
    "hasMember": {
      "@id": "http://www.w3.org/ns/sosa/hasMember",
      "@type": "@id"
    },
    "rangeIncludes": "https://schema.org/rangeIncludes",
    "hasInput": {
      "@id": "http://www.w3.org/ns/ssn/hasInput",
      "@type": "@id"
    },
    "Mass": "http://purl.oclc.org/NET/ssnx/qu/dim#Mass",
    "implementedBy": {
      "@id": "http://www.w3.org/ns/ssn/implementedBy",
      "@type": "@id"
    },
    "location": {
      "@id": "http://www.w3.org/2003/01/geo/wgs84_pos#location",
      "@type": "@id"
    },
    "ComponentSpecification": "http://purl.org/linked-data/cube#ComponentSpecification",
    "Scheme": "http://www.w3.org/2004/02/skos/core#Scheme",
    "hasEnd": {
      "@id": "http://www.w3.org/2006/time#hasEnd",
      "@type": "@id"
    },
    "GeometryCollection": "http://www.opengis.net/ont/sf#GeometryCollection",
    "rights": "http://purl.org/dc/terms/rights",
    "TemporalEntity": "http://www.w3.org/2006/time#TemporalEntity",
    "hasBeginning": {
      "@id": "http://www.w3.org/2006/time#hasBeginning",
      "@type": "@id"
    },
    "isResultOf": {
      "@id": "http://www.w3.org/ns/sosa/isResultOf",
      "@type": "@id"
    },
    "SF_SamplingFeature": "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature",
    "DimensionProperty": "http://purl.org/linked-data/cube#DimensionProperty",
    "alt": "http://www.w3.org/2003/01/geo/wgs84_pos#alt",
    "Acceleration": "http://purl.oclc.org/NET/ssnx/qu/dim#Acceleration",
    "identifier": "http://purl.org/dc/terms/identifier",
    "hasSubSystem": {
      "@id": "http://www.w3.org/ns/ssn/hasSubSystem",
      "@type": "@id"
    },
    "Quantity": "http://qudt.org/schema/qudt/Quantity",
    "MassFlowRate": "http://purl.oclc.org/NET/ssnx/qu/dim#MassFlowRate",
    "qu.QuantityKind": "http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind",
    "SpatialObjectCollection": "http://www.opengis.net/ont/geosparql#SpatialObjectCollection",
    "Distance": "http://purl.oclc.org/NET/ssnx/qu/dim#Distance",
    "deprecated": "http://www.w3.org/2002/07/owl#deprecated",
    "Radiance": "http://purl.oclc.org/NET/ssnx/qu/dim#Radiance",
    "Duration": "http://www.w3.org/2006/time#Duration",
    "TIN": "http://www.opengis.net/ont/sf#TIN",
    "SurfaceDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#SurfaceDensity",
    "isDefinedBy": "http://www.w3.org/2000/01/rdf-schema#isDefinedBy",
    "wgs84.Point": "http://www.w3.org/2003/01/geo/wgs84_pos#Point",
    "definition": "http://www.w3.org/2004/02/skos/core#definition",
    "editorialNote": "http://www.w3.org/2004/02/skos/core#editorialNote",
    "observes": {
      "@id": "http://www.w3.org/ns/sosa/observes",
      "@type": "@id"
    },
    "hasDeployment": {
      "@id": "http://www.w3.org/ns/ssn/hasDeployment",
      "@type": "@id"
    },
    "hasResult": {
      "@id": "http://www.w3.org/ns/sosa/hasResult",
      "@type": "@id"
    },
    "order": {
      "@id": "http://purl.org/linked-data/cube#order",
      "@type": "http://www.w3.org/2001/XMLSchema#int"
    },
    "hasGeometry": {
      "@id": "http://www.opengis.net/ont/geosparql#hasGeometry",
      "@type": "@id"
    },
    "usedProcedure": {
      "@id": "http://www.w3.org/ns/sosa/usedProcedure",
      "@type": "@id"
    },
    "ssn.Property": "http://www.w3.org/ns/ssn/Property",
    "sfContains": {
      "@id": "http://www.opengis.net/ont/geosparql#sfContains",
      "@type": "@id"
    },
    "title": "http://purl.org/dc/terms/title",
    "Density": "http://purl.oclc.org/NET/ssnx/qu/dim#Density",
    "LinearRing": "http://www.opengis.net/ont/sf#LinearRing",
    "Molality": "http://purl.oclc.org/NET/ssnx/qu/dim#Molality",
    "inXSDDateTimeStamp": {
      "@id": "http://www.w3.org/2006/time#inXSDDateTimeStamp",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTimeStamp"
    },
    "MeasureProperty": "http://purl.org/linked-data/cube#MeasureProperty",
    "PropertyKind": "http://purl.oclc.org/NET/ssnx/qu/qu#PropertyKind",
    "SpatialObject": "http://www.opengis.net/ont/geosparql#SpatialObject",
    "sliceStructure": {
      "@id": "http://purl.org/linked-data/cube#sliceStructure",
      "@type": "@id"
    },
    "hasFeatureOfInterest": {
      "@id": "http://www.w3.org/ns/sosa/hasFeatureOfInterest",
      "@type": "@id"
    },
    "NumberPerLength": "http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerLength",
    "lat": "http://www.w3.org/2003/01/geo/wgs84_pos#lat",
    "VolumeFlowRate": "http://purl.oclc.org/NET/ssnx/qu/dim#VolumeFlowRate",
    "SpecificEntropy": "http://purl.oclc.org/NET/ssnx/qu/dim#SpecificEntropy",
    "CodedProperty": "http://purl.org/linked-data/cube#CodedProperty",
    "observedProperty": {
      "@id": "http://www.w3.org/ns/sosa/observedProperty",
      "@type": "@id"
    },
    "slice": {
      "@id": "http://purl.org/linked-data/cube#slice",
      "@type": "@id"
    },
    "madeObservation": {
      "@id": "http://www.w3.org/ns/sosa/madeObservation",
      "@type": "@id"
    },
    "FeatureCollection": "http://www.opengis.net/ont/geosparql#FeatureCollection",
    "unit": {
      "@id": "http://qudt.org/schema/qudt/unit",
      "@type": "@id"
    },
    "date": "http://purl.org/dc/terms/date",
    "isPropertyOf": {
      "@id": "http://www.w3.org/ns/ssn/isPropertyOf",
      "@type": "@id"
    },
    "seeAlso": "http://www.w3.org/2000/01/rdf-schema#seeAlso",
    "ObservationGroup": "http://purl.org/linked-data/cube#ObservationGroup",
    "Sample": "http://www.w3.org/ns/sosa/Sample",
    "DataSet": "http://purl.org/linked-data/cube#DataSet",
    "comment": "http://www.w3.org/2000/01/rdf-schema#comment",
    "PolyhedralSurface": "http://www.opengis.net/ont/sf#PolyhedralSurface",
    "Polygon": "http://www.opengis.net/ont/sf#Polygon",
    "MultiPolygon": "http://www.opengis.net/ont/sf#MultiPolygon",
    "ObservableProperty": "http://www.w3.org/ns/sosa/ObservableProperty",
    "contributor": "http://purl.org/dc/terms/contributor",
    "deployedSystem": {
      "@id": "http://www.w3.org/ns/ssn/deployedSystem",
      "@type": "@id"
    },
    "System": "http://www.w3.org/ns/ssn/System",
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
    "deployedOnPlatform": {
      "@id": "http://www.w3.org/ns/ssn/deployedOnPlatform",
      "@type": "@id"
    },
    "inXSDDate": {
      "@id": "http://www.w3.org/2006/time#inXSDDate",
      "@type": "http://www.w3.org/2001/XMLSchema#date"
    },
    "GFI_DomainFeature": "http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_DomainFeature",
    "Actuation": "http://www.w3.org/ns/sosa/Actuation",
    "observation": {
      "@id": "http://purl.org/linked-data/cube#observation",
      "@type": "@id"
    },
    "Dimensionless": "http://purl.oclc.org/NET/ssnx/qu/dim#Dimensionless",
    "Area": "http://purl.oclc.org/NET/ssnx/qu/dim#Area",
    "Sampling": "http://www.w3.org/ns/sosa/Sampling",
    "Power": "http://purl.oclc.org/NET/ssnx/qu/dim#Power",
    "OM_Observation": "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation",
    "prefLabel": "http://www.w3.org/2004/02/skos/core#prefLabel",
    "Surface": "http://www.opengis.net/ont/sf#Surface",
    "sliceKey": {
      "@id": "http://purl.org/linked-data/cube#sliceKey",
      "@type": "@id"
    },
    "inScheme": "http://www.w3.org/2004/02/skos/core#inScheme",
    "dct.description": "http://purl.org/dc/terms/description",
    "MultiCurve": "http://www.opengis.net/ont/sf#MultiCurve",
    "hasQuantityKind": {
      "@id": "http://qudt.org/schema/qudt/hasQuantityKind",
      "@type": "@id"
    },
    "DataStructureDefinition": "http://purl.org/linked-data/cube#DataStructureDefinition",
    "MultiPoint": "http://www.opengis.net/ont/sf#MultiPoint",
    "qb.Observation": "http://purl.org/linked-data/cube#Observation",
    "EnergyDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyDensity",
    "Sensor": "http://www.w3.org/ns/sosa/Sensor",
    "hasSimpleResult": "http://www.w3.org/ns/sosa/hasSimpleResult",
    "unitType": {
      "@id": "http://www.w3.org/2006/time#unitType",
      "@type": "@id"
    },
    "componentProperty": {
      "@id": "http://purl.org/linked-data/cube#componentProperty",
      "@type": "@id"
    },
    "isFeatureOfInterestOf": {
      "@id": "http://www.w3.org/ns/sosa/isFeatureOfInterestOf",
      "@type": "@id"
    },
    "sf.Geometry": "http://www.opengis.net/ont/sf#Geometry",
    "schema.Person": "https://schema.org/Person",
    "Observation": "http://www.w3.org/ns/sosa/Observation",
    "Point": "http://www.opengis.net/ont/sf#Point",
    "schema.name": "https://schema.org/name",
    "QuantityKind": "http://qudt.org/schema/qudt/QuantityKind",
    "orel": "http://www.opengis.net/def/rel/",
    "sosa": "https://www.w3.org/TR/vocab-ssn/#",
    "sta": "https://schemas.opengis.org/sta/def/core#",
    "rel": "http://www.iana.org/assignments/relation/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-sta-obs/context.jsonld)

## Sources

* [Reference to ILIAD](https://example.com/sources/1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/iliad-apis-features](https://github.com/ogcincubator/iliad-apis-features)
* Path: `_sources/oim-sta-obs`

