---
title: OIM Observations (Schema)


toc_footers:
  - Version 0.1
  - <a href='#'>OIM Observations</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: OIM Observations (Schema)
---


# OIM Observations `ogc.hosted.iliad.api.features.oim-sta-obs`

Defines SensorThings API Observations to implement the OIM SOSA cross-domain model in a form compatible with ILIAD and other digital twins using this model.

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="success">
This building block is <strong>valid</strong>
</aside>

# Description

## Ocean Information Model Observations Profile

Currently a stub where requirements for OIM implementation can be defined as required.

Note specific profiles will define specific requirements for interaction with external systems.

The JSON-LD Context declares the default baseURI of Observation with generic STA context and OIM specific context.

TODO: (MVP)
1 - implement the observableProperties Register as a concept scheme under OGC hosted
2 - define a SHACL or other rule that requires observableProperties to be registered in the ILIAD observable properties register.

Note that it may have an externally resolvable URI or be a proxy handled by ILIAD (using the OGC RAINBOW)

The mechanisms for handling external vocabulary constraints to be define here: (TBD)

# Examples

## Oceans Information Model examples

TBD - see specific sub-profile for examples.


# JSON Schema

```yaml--schema
$schema: https://json-schema.org/draft/2020-12/schema
title: A OIM aligned STA Observtion schema
description: Component of OGC STA Observation. no particular added constraints are
  added
$ref: https://ogcincubator.github.io/bblocks-sta/build/annotated/api/sta/Observation/schema.json
x-jsonld-extra-terms:
  implements:
    x-jsonld-id: http://www.w3.org/ns/ssn/implements
    x-jsonld-type: '@id'
  MultiLineString: http://www.opengis.net/ont/sf#MultiLineString
  Attachable: http://purl.org/linked-data/cube#Attachable
  affiliation: https://schema.org/affiliation
  Line: http://www.opengis.net/ont/sf#Line
  member:
    x-jsonld-id: http://xmlns.com/foaf/0.1/member
    x-jsonld-type: '@id'
  versionInfo: http://www.w3.org/2002/07/owl#versionInfo
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
  Organization: https://schema.org/Organization
  GFI_Feature: http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_Feature
  AttributeProperty: http://purl.org/linked-data/cube#AttributeProperty
  hosts:
    x-jsonld-id: http://www.w3.org/ns/sosa/hosts
    x-jsonld-type: '@id'
  asWKT:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#asWKT
    x-jsonld-type: http://www.opengis.net/ont/geosparql#wktLiteral
  asGeoJSON:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#asGeoJSON
    x-jsonld-type: http://www.opengis.net/ont/geosparql#geoJSONLiteral
  RotationalSpeed: http://purl.oclc.org/NET/ssnx/qu/dim#RotationalSpeed
  FeatureOfInterest: http://www.w3.org/ns/sosa/FeatureOfInterest
  ComponentProperty: http://purl.org/linked-data/cube#ComponentProperty
  Class: http://www.w3.org/2000/01/rdf-schema#Class
  Geometry: http://www.opengis.net/ont/geosparql#Geometry
  depiction: http://xmlns.com/foaf/0.1/depiction
  Curve: http://www.opengis.net/ont/sf#Curve
  maker: http://xmlns.com/foaf/0.1/maker
  sfWithin:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#sfWithin
    x-jsonld-type: '@id'
  ThermalConductivity: http://purl.oclc.org/NET/ssnx/qu/dim#ThermalConductivity
  domainIncludes: https://schema.org/domainIncludes
  madeBySensor:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeBySensor
    x-jsonld-type: '@id'
  ActuatableProperty: http://www.w3.org/ns/sosa/ActuatableProperty
  Feature: http://www.opengis.net/ont/geosparql#Feature
  FeatureCollection: http://www.opengis.net/ont/geosparql#FeatureCollection
  SpatialObjectCollection: http://www.opengis.net/ont/geosparql#SpatialObjectCollection
  label: http://www.w3.org/2000/01/rdf-schema#label
  LineString: http://www.opengis.net/ont/sf#LineString
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
  Temperature: http://purl.oclc.org/NET/ssnx/qu/dim#Temperature
  homepage: http://xmlns.com/foaf/0.1/homepage
  hasProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasProperty
    x-jsonld-type: '@id'
  Person: http://xmlns.com/foaf/0.1/Person
  Triangle: http://www.opengis.net/ont/sf#Triangle
  observationGroup:
    x-jsonld-id: http://purl.org/linked-data/cube#observationGroup
    x-jsonld-type: '@id'
  EnergyFlux: http://purl.oclc.org/NET/ssnx/qu/dim#EnergyFlux
  StressOrPressure: http://purl.oclc.org/NET/ssnx/qu/dim#StressOrPressure
  resultTime: https://www.w3.org/TR/vocab-ssn/#resultTime
  Agent: http://xmlns.com/foaf/0.1/Agent
  creator: http://purl.org/dc/terms/creator
  Energy: http://purl.oclc.org/NET/ssnx/qu/dim#Energy
  foaf.name: http://xmlns.com/foaf/0.1/name
  Role: https://schema.org/Role
  hasSerialization:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#hasSerialization
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  SF_SamplingFeature.sampledFeature:
    x-jsonld-id: http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature.sampledFeature
    x-jsonld-type: '@id'
  rangeIncludes: https://schema.org/rangeIncludes
  location:
    x-jsonld-id: http://www.w3.org/2003/01/geo/wgs84_pos#location
    x-jsonld-type: '@id'
  ComponentSpecification: http://purl.org/linked-data/cube#ComponentSpecification
  Scheme: http://www.w3.org/2004/02/skos/core#Scheme
  GeometryCollection: http://www.opengis.net/ont/sf#GeometryCollection
  rights: http://purl.org/dc/terms/rights
  isResultOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isResultOf
    x-jsonld-type: '@id'
  SF_SamplingFeature: http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature
  DimensionProperty: http://purl.org/linked-data/cube#DimensionProperty
  Acceleration: http://purl.oclc.org/NET/ssnx/qu/dim#Acceleration
  identifier: http://purl.org/dc/terms/identifier
  hasSubSystem:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasSubSystem
    x-jsonld-type: '@id'
  QuantityKind: http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind
  Distance: http://purl.oclc.org/NET/ssnx/qu/dim#Distance
  TIN: http://www.opengis.net/ont/sf#TIN
  SurfaceDensity: http://purl.oclc.org/NET/ssnx/qu/dim#SurfaceDensity
  isDefinedBy: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
  wgs84.Point: http://www.w3.org/2003/01/geo/wgs84_pos#Point
  definition: http://www.w3.org/2004/02/skos/core#definition
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
  sfContains:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#sfContains
    x-jsonld-type: '@id'
  title: http://purl.org/dc/terms/title
  Density: http://purl.oclc.org/NET/ssnx/qu/dim#Density
  LinearRing: http://www.opengis.net/ont/sf#LinearRing
  MeasureProperty: http://purl.org/linked-data/cube#MeasureProperty
  PropertyKind: http://purl.oclc.org/NET/ssnx/qu/qu#PropertyKind
  SpatialObject: http://www.opengis.net/ont/geosparql#SpatialObject
  sliceStructure:
    x-jsonld-id: http://purl.org/linked-data/cube#sliceStructure
    x-jsonld-type: '@id'
  hasFeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasFeatureOfInterest
    x-jsonld-type: '@id'
  hasUltimateFeatureOfInterest:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasUltimateFeatureOfInterest
    x-jsonld-type: '@id'
  hasMember:
    x-jsonld-id: http://www.w3.org/ns/sosa/hasMember
    x-jsonld-type: '@id'
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
  dimension:
    x-jsonld-id: http://purl.org/linked-data/cube#dimension
    x-jsonld-type: '@id'
  RadianceExposure: http://purl.oclc.org/NET/ssnx/qu/dim#RadianceExposure
  VelocityOrSpeed: http://purl.oclc.org/NET/ssnx/qu/dim#VelocityOrSpeed
  deployedOnPlatform:
    x-jsonld-id: http://www.w3.org/ns/ssn/deployedOnPlatform
    x-jsonld-type: '@id'
  GFI_DomainFeature: http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_DomainFeature
  observation:
    x-jsonld-id: http://purl.org/linked-data/cube#observation
    x-jsonld-type: '@id'
  Dimensionless: http://purl.oclc.org/NET/ssnx/qu/dim#Dimensionless
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
  DataStructureDefinition: http://purl.org/linked-data/cube#DataStructureDefinition
  MultiPoint: http://www.opengis.net/ont/sf#MultiPoint
  qb.Observation: http://purl.org/linked-data/cube#Observation
  EnergyDensity: http://purl.oclc.org/NET/ssnx/qu/dim#EnergyDensity
  hasSimpleResult: http://www.w3.org/ns/sosa/hasSimpleResult
  componentProperty:
    x-jsonld-id: http://purl.org/linked-data/cube#componentProperty
    x-jsonld-type: '@id'
  isFeatureOfInterestOf:
    x-jsonld-id: http://www.w3.org/ns/sosa/isFeatureOfInterestOf
    x-jsonld-type: '@id'
  sf.Geometry: http://www.opengis.net/ont/sf#Geometry
  schema.Person: https://schema.org/Person
  Observation: http://www.w3.org/ns/sosa/Observation
  ObservationCollection: http://www.w3.org/ns/sosa/ObservationCollection
  Point: http://www.opengis.net/ont/sf#Point
  ssn.Property: http://www.w3.org/ns/ssn/Property
  schema.name: https://schema.org/name
  Measure: http://def.seegrid.csiro.au/isotc211/iso19103/2005/basic#Measure
  Quantity: http://qudt.org/schema/qudt/Quantity
  qudt.QuantityKind: http://qudt.org/schema/qudt/QuantityKind
  QuantityValue: http://qudt.org/schema/qudt/QuantityValue
  Unit: http://qudt.org/schema/qudt/Unit
  unit:
    x-jsonld-id: http://qudt.org/schema/qudt/unit
    x-jsonld-type: '@id'
  quantityValue:
    x-jsonld-id: http://qudt.org/schema/qudt/quantityValue
    x-jsonld-type: '@id'
  hasQuantityKind:
    x-jsonld-id: http://qudt.org/schema/qudt/hasQuantityKind
    x-jsonld-type: '@id'
  numericValue: http://qudt.org/schema/qudt/numericValue
  Sensor: http://www.w3.org/ns/sosa/Sensor
  Actuation: http://www.w3.org/ns/sosa/Actuation
  Sampling: http://www.w3.org/ns/sosa/Sampling
  Procedure: http://www.w3.org/ns/sosa/Procedure
  observes:
    x-jsonld-id: http://www.w3.org/ns/sosa/observes
    x-jsonld-type: '@id'
  phenomenonTime: https://www.w3.org/TR/vocab-ssn/#phenomenonTime
  usedProcedure:
    x-jsonld-id: http://www.w3.org/ns/sosa/usedProcedure
    x-jsonld-type: '@id'
  hasInput:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasInput
    x-jsonld-type: '@id'
  hasOutput:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasOutput
    x-jsonld-type: '@id'
  implementedBy:
    x-jsonld-id: http://www.w3.org/ns/ssn/implementedBy
    x-jsonld-type: '@id'
  lat: http://www.w3.org/2003/01/geo/wgs84_pos#lat
  long: http://www.w3.org/2003/01/geo/wgs84_pos#long
  alt: http://www.w3.org/2003/01/geo/wgs84_pos#alt
  TemporalDuration: http://www.w3.org/2006/time#TemporalDuration
  Thing: http://www.w3.org/2002/07/owl#Thing
  TemporalUnit: http://www.w3.org/2006/time#TemporalUnit
  Instant: http://www.w3.org/2006/time#Instant
  numericDuration:
    x-jsonld-id: http://www.w3.org/2006/time#numericDuration
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  note: http://www.w3.org/2004/02/skos/core#note
  Interval: http://www.w3.org/2006/time#Interval
  hasTime:
    x-jsonld-id: http://www.w3.org/2006/time#hasTime
    x-jsonld-type: '@id'
  hasEnd:
    x-jsonld-id: http://www.w3.org/2006/time#hasEnd
    x-jsonld-type: '@id'
  TemporalEntity: http://www.w3.org/2006/time#TemporalEntity
  hasBeginning:
    x-jsonld-id: http://www.w3.org/2006/time#hasBeginning
    x-jsonld-type: '@id'
  deprecated: http://www.w3.org/2002/07/owl#deprecated
  Duration: http://www.w3.org/2006/time#Duration
  editorialNote: http://www.w3.org/2004/02/skos/core#editorialNote
  inXSDDateTimeStamp:
    x-jsonld-id: http://www.w3.org/2006/time#inXSDDateTimeStamp
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTimeStamp
  inXSDDate:
    x-jsonld-id: http://www.w3.org/2006/time#inXSDDate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#date
  unitType:
    x-jsonld-id: http://www.w3.org/2006/time#unitType
    x-jsonld-type: '@id'
  '@iot.id': '@id'
  '@iot.selfLink': https://schemas.opengis.org/sta/def/core#selfLink
  result: https://www.w3.org/TR/vocab-ssn/#hasSimpleResult
  resultQuality: https://schemas.opengis.org/sta/def/core#resultQuality
  validTime: https://schemas.opengis.org/sta/def/core#validTime
  Datastream@iot.navigationLink: https://schemas.opengis.org/sta/def/core#DataStream
  FeatureOfInterest@iot.navigationLink: https://www.w3.org/TR/vocab-ssn/#hasFeatureOfInterest
x-jsonld-prefixes:
  sta: https://schemas.opengis.org/sta/def/core#
  sosa: https://www.w3.org/TR/vocab-ssn/#
  rel: http://www.iana.org/assignments/relation/

```

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Fannotated%2Fhosted%2Filiad%2Fapi%2Ffeatures%2Foim-sta-obs%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-sta-obs/schema.yaml" target="_blank">https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-sta-obs/schema.yaml</a>
* JSON version: <a href="https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-sta-obs/schema.json" target="_blank">https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-sta-obs/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "@iot.id": "@id",
    "@iot.selfLink": "sta:selfLink",
    "phenomenonTime": "sosa:phenomenonTime",
    "result": "sosa:hasSimpleResult",
    "resultQuality": "sta:resultQuality",
    "resultTime": "sosa:resultTime",
    "validTime": "sta:validTime",
    "Datastream@iot.navigationLink": "sta:DataStream",
    "FeatureOfInterest@iot.navigationLink": "sosa:hasFeatureOfInterest",
    "implements": {
      "@id": "http://www.w3.org/ns/ssn/implements",
      "@type": "@id"
    },
    "MultiLineString": "http://www.opengis.net/ont/sf#MultiLineString",
    "Attachable": "http://purl.org/linked-data/cube#Attachable",
    "affiliation": "https://schema.org/affiliation",
    "Line": "http://www.opengis.net/ont/sf#Line",
    "member": {
      "@id": "http://xmlns.com/foaf/0.1/member",
      "@type": "@id"
    },
    "versionInfo": "http://www.w3.org/2002/07/owl#versionInfo",
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
    "Organization": "https://schema.org/Organization",
    "GFI_Feature": "http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_Feature",
    "AttributeProperty": "http://purl.org/linked-data/cube#AttributeProperty",
    "hosts": {
      "@id": "http://www.w3.org/ns/sosa/hosts",
      "@type": "@id"
    },
    "asWKT": {
      "@id": "http://www.opengis.net/ont/geosparql#asWKT",
      "@type": "http://www.opengis.net/ont/geosparql#wktLiteral"
    },
    "asGeoJSON": {
      "@id": "http://www.opengis.net/ont/geosparql#asGeoJSON",
      "@type": "http://www.opengis.net/ont/geosparql#geoJSONLiteral"
    },
    "RotationalSpeed": "http://purl.oclc.org/NET/ssnx/qu/dim#RotationalSpeed",
    "FeatureOfInterest": "http://www.w3.org/ns/sosa/FeatureOfInterest",
    "ComponentProperty": "http://purl.org/linked-data/cube#ComponentProperty",
    "Class": "http://www.w3.org/2000/01/rdf-schema#Class",
    "Geometry": "http://www.opengis.net/ont/geosparql#Geometry",
    "depiction": "http://xmlns.com/foaf/0.1/depiction",
    "Curve": "http://www.opengis.net/ont/sf#Curve",
    "maker": "http://xmlns.com/foaf/0.1/maker",
    "sfWithin": {
      "@id": "http://www.opengis.net/ont/geosparql#sfWithin",
      "@type": "@id"
    },
    "ThermalConductivity": "http://purl.oclc.org/NET/ssnx/qu/dim#ThermalConductivity",
    "domainIncludes": "https://schema.org/domainIncludes",
    "madeBySensor": {
      "@id": "http://www.w3.org/ns/sosa/madeBySensor",
      "@type": "@id"
    },
    "ActuatableProperty": "http://www.w3.org/ns/sosa/ActuatableProperty",
    "Feature": "http://www.opengis.net/ont/geosparql#Feature",
    "FeatureCollection": "http://www.opengis.net/ont/geosparql#FeatureCollection",
    "SpatialObjectCollection": "http://www.opengis.net/ont/geosparql#SpatialObjectCollection",
    "label": "http://www.w3.org/2000/01/rdf-schema#label",
    "LineString": "http://www.opengis.net/ont/sf#LineString",
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
    "Temperature": "http://purl.oclc.org/NET/ssnx/qu/dim#Temperature",
    "homepage": "http://xmlns.com/foaf/0.1/homepage",
    "hasProperty": {
      "@id": "http://www.w3.org/ns/ssn/hasProperty",
      "@type": "@id"
    },
    "Person": "http://xmlns.com/foaf/0.1/Person",
    "Triangle": "http://www.opengis.net/ont/sf#Triangle",
    "observationGroup": {
      "@id": "http://purl.org/linked-data/cube#observationGroup",
      "@type": "@id"
    },
    "EnergyFlux": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyFlux",
    "StressOrPressure": "http://purl.oclc.org/NET/ssnx/qu/dim#StressOrPressure",
    "Agent": "http://xmlns.com/foaf/0.1/Agent",
    "creator": "http://purl.org/dc/terms/creator",
    "Energy": "http://purl.oclc.org/NET/ssnx/qu/dim#Energy",
    "foaf.name": "http://xmlns.com/foaf/0.1/name",
    "Role": "https://schema.org/Role",
    "hasSerialization": {
      "@id": "http://www.opengis.net/ont/geosparql#hasSerialization",
      "@type": "http://www.w3.org/2000/01/rdf-schema#Literal"
    },
    "SF_SamplingFeature.sampledFeature": {
      "@id": "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature.sampledFeature",
      "@type": "@id"
    },
    "rangeIncludes": "https://schema.org/rangeIncludes",
    "location": {
      "@id": "http://www.w3.org/2003/01/geo/wgs84_pos#location",
      "@type": "@id"
    },
    "ComponentSpecification": "http://purl.org/linked-data/cube#ComponentSpecification",
    "Scheme": "http://www.w3.org/2004/02/skos/core#Scheme",
    "GeometryCollection": "http://www.opengis.net/ont/sf#GeometryCollection",
    "rights": "http://purl.org/dc/terms/rights",
    "isResultOf": {
      "@id": "http://www.w3.org/ns/sosa/isResultOf",
      "@type": "@id"
    },
    "SF_SamplingFeature": "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature",
    "DimensionProperty": "http://purl.org/linked-data/cube#DimensionProperty",
    "Acceleration": "http://purl.oclc.org/NET/ssnx/qu/dim#Acceleration",
    "identifier": "http://purl.org/dc/terms/identifier",
    "hasSubSystem": {
      "@id": "http://www.w3.org/ns/ssn/hasSubSystem",
      "@type": "@id"
    },
    "QuantityKind": "http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind",
    "Distance": "http://purl.oclc.org/NET/ssnx/qu/dim#Distance",
    "TIN": "http://www.opengis.net/ont/sf#TIN",
    "SurfaceDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#SurfaceDensity",
    "isDefinedBy": "http://www.w3.org/2000/01/rdf-schema#isDefinedBy",
    "wgs84.Point": "http://www.w3.org/2003/01/geo/wgs84_pos#Point",
    "definition": "http://www.w3.org/2004/02/skos/core#definition",
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
    "sfContains": {
      "@id": "http://www.opengis.net/ont/geosparql#sfContains",
      "@type": "@id"
    },
    "title": "http://purl.org/dc/terms/title",
    "Density": "http://purl.oclc.org/NET/ssnx/qu/dim#Density",
    "LinearRing": "http://www.opengis.net/ont/sf#LinearRing",
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
    "hasUltimateFeatureOfInterest": {
      "@id": "http://www.w3.org/ns/sosa/hasUltimateFeatureOfInterest",
      "@type": "@id"
    },
    "hasMember": {
      "@id": "http://www.w3.org/ns/sosa/hasMember",
      "@type": "@id"
    },
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
    "GFI_DomainFeature": "http://def.isotc211.org/iso19156/2011/GeneralFeatureInstance#GFI_DomainFeature",
    "observation": {
      "@id": "http://purl.org/linked-data/cube#observation",
      "@type": "@id"
    },
    "Dimensionless": "http://purl.oclc.org/NET/ssnx/qu/dim#Dimensionless",
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
    "DataStructureDefinition": "http://purl.org/linked-data/cube#DataStructureDefinition",
    "MultiPoint": "http://www.opengis.net/ont/sf#MultiPoint",
    "qb.Observation": "http://purl.org/linked-data/cube#Observation",
    "EnergyDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyDensity",
    "hasSimpleResult": "http://www.w3.org/ns/sosa/hasSimpleResult",
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
    "ObservationCollection": "http://www.w3.org/ns/sosa/ObservationCollection",
    "Point": "http://www.opengis.net/ont/sf#Point",
    "ssn.Property": "http://www.w3.org/ns/ssn/Property",
    "schema.name": "https://schema.org/name",
    "Measure": "http://def.seegrid.csiro.au/isotc211/iso19103/2005/basic#Measure",
    "Quantity": "http://qudt.org/schema/qudt/Quantity",
    "qudt.QuantityKind": "http://qudt.org/schema/qudt/QuantityKind",
    "QuantityValue": "http://qudt.org/schema/qudt/QuantityValue",
    "Unit": "http://qudt.org/schema/qudt/Unit",
    "unit": {
      "@id": "http://qudt.org/schema/qudt/unit",
      "@type": "@id"
    },
    "quantityValue": {
      "@id": "http://qudt.org/schema/qudt/quantityValue",
      "@type": "@id"
    },
    "hasQuantityKind": {
      "@id": "http://qudt.org/schema/qudt/hasQuantityKind",
      "@type": "@id"
    },
    "numericValue": "http://qudt.org/schema/qudt/numericValue",
    "Sensor": "http://www.w3.org/ns/sosa/Sensor",
    "Actuation": "http://www.w3.org/ns/sosa/Actuation",
    "Sampling": "http://www.w3.org/ns/sosa/Sampling",
    "Procedure": "http://www.w3.org/ns/sosa/Procedure",
    "observes": {
      "@id": "http://www.w3.org/ns/sosa/observes",
      "@type": "@id"
    },
    "usedProcedure": {
      "@id": "http://www.w3.org/ns/sosa/usedProcedure",
      "@type": "@id"
    },
    "hasInput": {
      "@id": "http://www.w3.org/ns/ssn/hasInput",
      "@type": "@id"
    },
    "hasOutput": {
      "@id": "http://www.w3.org/ns/ssn/hasOutput",
      "@type": "@id"
    },
    "implementedBy": {
      "@id": "http://www.w3.org/ns/ssn/implementedBy",
      "@type": "@id"
    },
    "lat": "http://www.w3.org/2003/01/geo/wgs84_pos#lat",
    "long": "http://www.w3.org/2003/01/geo/wgs84_pos#long",
    "alt": "http://www.w3.org/2003/01/geo/wgs84_pos#alt",
    "TemporalDuration": "http://www.w3.org/2006/time#TemporalDuration",
    "Thing": "http://www.w3.org/2002/07/owl#Thing",
    "TemporalUnit": "http://www.w3.org/2006/time#TemporalUnit",
    "Instant": "http://www.w3.org/2006/time#Instant",
    "numericDuration": {
      "@id": "http://www.w3.org/2006/time#numericDuration",
      "@type": "http://www.w3.org/2001/XMLSchema#decimal"
    },
    "note": "http://www.w3.org/2004/02/skos/core#note",
    "Interval": "http://www.w3.org/2006/time#Interval",
    "hasTime": {
      "@id": "http://www.w3.org/2006/time#hasTime",
      "@type": "@id"
    },
    "hasEnd": {
      "@id": "http://www.w3.org/2006/time#hasEnd",
      "@type": "@id"
    },
    "TemporalEntity": "http://www.w3.org/2006/time#TemporalEntity",
    "hasBeginning": {
      "@id": "http://www.w3.org/2006/time#hasBeginning",
      "@type": "@id"
    },
    "deprecated": "http://www.w3.org/2002/07/owl#deprecated",
    "Duration": "http://www.w3.org/2006/time#Duration",
    "editorialNote": "http://www.w3.org/2004/02/skos/core#editorialNote",
    "inXSDDateTimeStamp": {
      "@id": "http://www.w3.org/2006/time#inXSDDateTimeStamp",
      "@type": "http://www.w3.org/2001/XMLSchema#dateTimeStamp"
    },
    "inXSDDate": {
      "@id": "http://www.w3.org/2006/time#inXSDDate",
      "@type": "http://www.w3.org/2001/XMLSchema#date"
    },
    "unitType": {
      "@id": "http://www.w3.org/2006/time#unitType",
      "@type": "@id"
    },
    "sta": "https://schemas.opengis.org/sta/def/core#",
    "sosa": "https://www.w3.org/TR/vocab-ssn/#",
    "rel": "http://www.iana.org/assignments/relation/",
    "@version": 1.1
  }
}
```

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Fannotated%2Fhosted%2Filiad%2Fapi%2Ffeatures%2Foim-sta-obs%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-sta-obs/context.jsonld" target="_blank">https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/oim-sta-obs/context.jsonld</a>

# References

* [Reference to ILIAD](https://example.com/sources/1)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/ogcincubator/iliad-apis-features" target="_blank">https://github.com/ogcincubator/iliad-apis-features</a>
* Path:
<code><a href="https://github.com/ogcincubator/iliad-apis-features/blob/HEAD/_sources/oim-sta-obs" target="_blank">_sources/oim-sta-obs</a></code>

