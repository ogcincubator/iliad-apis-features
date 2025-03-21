
# GeoZarr Attributes description metadata aligned to the SeaDataNet time series profile (Schema)

`ogc.hosted.iliad.api.features.zarr_attrs_sdn` *v0.1*

based on the https://zarr.readthedocs.io/en/v2.1.2/spec/v2.html, tooling support constraints and Iliad requiremnts

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Ocean Information Model Records profile

SeadataNet format example where requirements for OIM implementation can be defined as required.

Note specific profiles will define specific requirements for interaction with external systems.

The JSON-LD Context declares the default baseURI of Observation with generic STA context and OIM specific context.

TODO: (MVP)
1 - complete OIM mapping in the context files
2 - resolve gaps with the OIM and SDN

Note that it may have an externally resolvable URI or be a proxy handled by ILIAD (using the OGC RAINBOW)

## Examples

### Zarr v2 attributes metadata for CRS
#### json
```json
{
    "_ARRAY_DIMENSIONS": [],
    "epsg_code": "EPSG:4326",
    "grid_mapping_name": "latitude_longitude",
    "inverse_flattening": 298.257223563,
    "semi_major_axis": 6378137.0
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_sdn/context.jsonld",
  "_ARRAY_DIMENSIONS": [],
  "epsg_code": "EPSG:4326",
  "grid_mapping_name": "latitude_longitude",
  "inverse_flattening": 298.257223563,
  "semi_major_axis": 6378137,
  "sdn_parameter_urn": null,
  "sdn_uom_urn": null
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/iliad/oim/default-context/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] :epsg_code "EPSG:4326" ;
    :grid_mapping_name "latitude_longitude" ;
    :inverse_flattening 2.982572e+02 ;
    :semi_major_axis 6378137 .


```


### Zarr v2 attributes metadata for LATITUDE
#### json
```json
{
    "_ARRAY_DIMENSIONS": [
        "INSTANCE"
    ],
    "ancillary_variables": "POSITION_SEADATANET_QC",
    "axis": "Y",
    "grid_mapping": "crs",
    "long_name": "Latitude",
    "sdn_parameter_name": "Latitude north",
    "sdn_parameter_urn": "SDN:P01::ALATZZ01",
    "sdn_uom_name": "Degrees north",
    "sdn_uom_urn": "SDN:P06::DEGN",
    "standard_name": "latitude",
    "units": "degrees_north"
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_sdn/context.jsonld",
  "_ARRAY_DIMENSIONS": [
    "INSTANCE"
  ],
  "ancillary_variables": "POSITION_SEADATANET_QC",
  "axis": "Y",
  "grid_mapping": "crs",
  "long_name": "Latitude",
  "sdn_parameter_name": "Latitude north",
  "sdn_parameter_urn": {
    "@id": "http://vocab.nerc.ac.uk/collection/P01/ALATZZ01"
  },
  "sdn_uom_name": "Degrees north",
  "sdn_uom_urn": {
    "@id": "http://vocab.nerc.ac.uk/collection/P06/DEGN"
  },
  "standard_name": "latitude",
  "units": "degrees_north"
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/iliad/oim/default-context/> .
@prefix ns1: <http://www.opengis.net/cis/1.1/> .

[] ns1:axis <http://schemas.opengis.net/Y> ;
    :_ARRAY_DIMENSIONS "INSTANCE" ;
    :ancillary_variables "POSITION_SEADATANET_QC" ;
    :grid_mapping "crs" ;
    :long_name "Latitude" ;
    :sdn_parameter_name "Latitude north" ;
    :sdn_parameter_urn <http://vocab.nerc.ac.uk/collection/P01/ALATZZ01> ;
    :sdn_uom_name "Degrees north" ;
    :sdn_uom_urn <http://vocab.nerc.ac.uk/collection/P06/DEGN> ;
    :standard_name "latitude" ;
    :units "degrees_north" .


```


### Zarr v2 attributes metadata for TIME
#### json
```json
{
    "_ARRAY_DIMENSIONS": [
        "INSTANCE",
        "MAXT"
    ],
    "ancillary_variables": "TIME_SEADATANET_QC",
    "axis": "T",
    "calendar": "julian",
    "long_name": "Chronological Julian Date",
    "sdn_parameter_name": "Julian Date (chronological)",
    "sdn_parameter_urn": "SDN:P01::CJDY1101",
    "sdn_uom_name": "Days",
    "sdn_uom_urn": "SDN:P06::UTAA",
    "standard_name": "time",
    "units": "seconds since 2024-10-01 01:00:00.000000"
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_sdn/context.jsonld",
  "_ARRAY_DIMENSIONS": [
    "INSTANCE",
    "MAXT"
  ],
  "ancillary_variables": "TIME_SEADATANET_QC",
  "axis": "T",
  "calendar": "julian",
  "long_name": "Chronological Julian Date",
  "sdn_parameter_name": "Julian Date (chronological)",
  "sdn_parameter_urn": {
    "@id": "http://vocab.nerc.ac.uk/collection/P01/CJDY1101"
  },
  "sdn_uom_name": "Days",
  "sdn_uom_urn": {
    "@id": "http://vocab.nerc.ac.uk/collection/P06/UTAA"
  },
  "standard_name": "time",
  "units": "seconds since 2024-10-01 01:00:00.000000"
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/iliad/oim/default-context/> .
@prefix covjson: <https://covjson.org/def/core#> .
@prefix ns1: <http://www.opengis.net/cis/1.1/> .

[] ns1:axis <http://schemas.opengis.net/T> ;
    covjson:calendar :julian ;
    :_ARRAY_DIMENSIONS "INSTANCE",
        "MAXT" ;
    :ancillary_variables "TIME_SEADATANET_QC" ;
    :long_name "Chronological Julian Date" ;
    :sdn_parameter_name "Julian Date (chronological)" ;
    :sdn_parameter_urn <http://vocab.nerc.ac.uk/collection/P01/CJDY1101> ;
    :sdn_uom_name "Days" ;
    :sdn_uom_urn <http://vocab.nerc.ac.uk/collection/P06/UTAA> ;
    :standard_name "time" ;
    :units "seconds since 2024-10-01 01:00:00.000000" .


```


### Zarr v2 attributes metadata for crs
#### json
```json
{
    "_ARRAY_DIMENSIONS": [
        "INSTANCE",
        "MAXT"
    ],
    "ancillary_variables": "TEMPTADC_SEADATANET_QC",
    "coordinates": "TIME DEPTH LATITUDE LONGITUDE",
    "long_name": "SST",
    "sdn_parameter_name": "Temperature of the water body by in-situ thermistor on acoustic doppler current profiler (ADCP) transducer",
    "sdn_parameter_urn": "SDN:P01::TEMPTADC",
    "sdn_uom_name": "Degrees Celsius",
    "sdn_uom_urn": "SDN:P06::UPAA",
    "standard_name": "sea_surface_temperature",
    "units": "degrees celsius"
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_sdn/context.jsonld",
  "_ARRAY_DIMENSIONS": [
    "INSTANCE",
    "MAXT"
  ],
  "ancillary_variables": "TEMPTADC_SEADATANET_QC",
  "coordinates": "TIME DEPTH LATITUDE LONGITUDE",
  "long_name": "SST",
  "sdn_parameter_name": "Temperature of the water body by in-situ thermistor on acoustic doppler current profiler (ADCP) transducer",
  "sdn_parameter_urn": {
    "@id": "http://vocab.nerc.ac.uk/collection/P01/TEMPTADC"
  },
  "sdn_uom_name": "Degrees Celsius",
  "sdn_uom_urn": {
    "@id": "http://vocab.nerc.ac.uk/collection/P06/UPAA"
  },
  "standard_name": "sea_surface_temperature",
  "units": "degrees celsius"
}
```

#### ttl
```ttl
@prefix : <https://w3id.org/iliad/oim/default-context/> .

[] :_ARRAY_DIMENSIONS "INSTANCE",
        "MAXT" ;
    :ancillary_variables "TEMPTADC_SEADATANET_QC" ;
    :coordinates "TIME DEPTH LATITUDE LONGITUDE" ;
    :long_name "SST" ;
    :sdn_parameter_name "Temperature of the water body by in-situ thermistor on acoustic doppler current profiler (ADCP) transducer" ;
    :sdn_parameter_urn <http://vocab.nerc.ac.uk/collection/P01/TEMPTADC> ;
    :sdn_uom_name "Degrees Celsius" ;
    :sdn_uom_urn <http://vocab.nerc.ac.uk/collection/P06/UPAA> ;
    :standard_name "sea_surface_temperature" ;
    :units "degrees celsius" .


```

## Schema

```yaml
$schema: http://json-schema.org/draft-07/schema#
title: Zarr Attributes Metadata for SeaDataNet
type: object
properties:
  long_name:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/long_name
  standard_name:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/standard_name
  units:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/units
  _ARRAY_DIMENSIONS:
    type: array
    items:
      type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/_ARRAY_DIMENSIONS
  Conventions:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/Conventions
  units_metadata:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/units_metadata
  cell_methods:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/cell_methods
  created_by:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/created_by
  date:
    type: string
    x-jsonld-id: http://purl.org/dc/terms/date
  crs_wkt:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/crs_wkt
  geotransform:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/geotransform
  proj4:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/proj4
  spatial_ref:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/spatial_ref
  epsg_code:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/epsg_code
  grid_mapping_name:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/grid_mapping_name
  inverse_flattening:
    type: number
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/inverse_flattening
  semi_major_axis:
    type: number
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/semi_major_axis
  ancillary_variables:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/ancillary_variables
  axis:
    type: string
    x-jsonld-id: http://www.opengis.net/cis/1.1/axis
    x-jsonld-type: '@id'
  grid_mapping:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/grid_mapping
  sdn_parameter_name:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/sdn_parameter_name
  sdn_parameter_urn:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/sdn_parameter_urn
  sdn_uom_name:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/sdn_uom_name
  sdn_uom_urn:
    type: string
    x-jsonld-id: https://w3id.org/iliad/oim/default-context/sdn_uom_urn
x-jsonld-extra-terms:
  id: '@id'
  type: '@type'
  value: '@value'
  label:
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#label
    x-jsonld-container: '@language'
  title:
    x-jsonld-id: http://purl.org/dc/terms/title
    x-jsonld-container: '@language'
  description:
    x-jsonld-id: http://purl.org/dc/terms/description
    x-jsonld-container: '@language'
  unit: http://qudt.org/schema/qudt#unit
  symbol: http://qudt.org/schema/qudt#symbol
  Domain: https://covjson.org/def/core#Domain
  domain: https://covjson.org/def/core#domain
  domainType:
    x-jsonld-id: https://covjson.org/def/core#domainType
    x-jsonld-type: '@vocab'
  axes:
    x-jsonld-id: https://covjson.org/def/core#axis
    x-jsonld-container: '@index'
  dataType:
    x-jsonld-id: https://w3id.org/idsa/core/dataType
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  primitive: https://covjson.org/def/core#primitive
  tuple: https://covjson.org/def/core#tuple
  polygon: https://covjson.org/def/core#polygon
  num: https://covjson.org/def/core#num
  start: https://covjson.org/def/core#start
  stop: https://covjson.org/def/core#stop
  referencing:
    x-jsonld-id: https://covjson.org/def/core#referencing
    x-jsonld-container: '@set'
  components:
    x-jsonld-id: https://covjson.org/def/core#components
    x-jsonld-container: '@list'
  system: https://covjson.org/def/core#referenceSystem
  RS: https://covjson.org/def/core#ReferenceSystem
  CRS: https://covjson.org/def/core#CoordinateReferenceSystem
  cs: http://data.ign.fr/def/ignf#coordinateSystem
  CS: http://data.ign.fr/def/ignf#CoordinateSystem
  TemporalRS: http://inspire.ec.europa.eu/glossary/TemporalReferenceSystem
  TemporalCRS: https://covjson.org/def/core#TemporalCRS
  calendar:
    x-jsonld-id: https://covjson.org/def/core#calendar
    x-jsonld-type: '@vocab'
  Gregorian: http://www.opengis.net/def/uom/ISO-8601/0/Gregorian
  timeScale: https://covjson.org/def/core#timeScale
  SpatialRS: http://inspire.ec.europa.eu/glossary/SpatialReferenceSystem
  SpatialCRS: http://data.ign.fr/def/ignf#CRS
  GeodeticCRS: http://data.ign.fr/def/ignf#GeodeticCRS
  ProjectedCRS: http://data.ign.fr/def/ignf#ProjectedCRS
  VerticalCRS: http://data.ign.fr/def/ignf#VerticalCRS
  datum: http://data.ign.fr/def/ignf#datum
  csAxes:
    x-jsonld-id: https://covjson.org/def/core#coordinateSystemAxes
    x-jsonld-container: '@list'
  direction: http://data.ign.fr/def/ignf#axisDirection
  IdentifierRS: https://covjson.org/def/core#IdentifierReferenceSystem
  targetConcept: https://covjson.org/def/core#targetConcept
  identifiers:
    x-jsonld-id: https://covjson.org/def/core#identifier
    x-jsonld-type: '@id'
    x-jsonld-container: '@index'
  Parameter: https://covjson.org/def/core#Parameter
  parameters:
    x-jsonld-id: https://covjson.org/def/core#parameter
    x-jsonld-type: '@id'
    x-jsonld-container: '@index'
  observedProperty: http://www.w3.org/2005/Incubator/ssn/ssnx/ssn#observedProperty
  categoryEncoding: https://covjson.org/def/core#categoryEncoding
  ParameterGroup: https://covjson.org/def/core#ParameterGroup
  members:
    x-jsonld-id: https://covjson.org/def/core#member
    x-jsonld-type: '@vocab'
    x-jsonld-container: '@set'
  ranges:
    x-jsonld-id: https://covjson.org/def/core#range
    x-jsonld-type: '@id'
    x-jsonld-container: '@index'
  NdArray: https://covjson.org/def/core#NdArray
  TiledNdArray: https://covjson.org/def/core#TiledNdArray
  shape:
    x-jsonld-id: https://covjson.org/def/core#shape
    x-jsonld-container: '@list'
  tileShape:
    x-jsonld-id: https://covjson.org/def/core#tileShape
    x-jsonld-container: '@list'
  axisNames:
    x-jsonld-id: https://covjson.org/def/core#axisNames
    x-jsonld-container: '@list'
  urlTemplate: https://covjson.org/def/core#urlTemplate
  tileSets:
    x-jsonld-id: https://covjson.org/def/core#tileSet
    x-jsonld-container: '@set'
  float: http://www.w3.org/2001/XMLSchema#double
  integer: http://www.w3.org/2001/XMLSchema#integer
  string: http://www.w3.org/2001/XMLSchema#string
  Coverage: https://covjson.org/def/core#Coverage
  coverages:
    x-jsonld-id: http://www.w3.org/ns/hydra/core#member
    x-jsonld-container: '@set'
  CoverageCollection: https://covjson.org/def/core#CoverageCollection
  Grid: https://covjson.org/def/domainTypes#Grid
  VerticalProfile: https://covjson.org/def/domainTypes#VerticalProfile
  MultiPointSeries: https://covjson.org/def/domainTypes#MultiPointSeries
  MultiPoint: https://covjson.org/def/domainTypes#MultiPoint
  PointSeries: https://covjson.org/def/domainTypes#PointSeries
  Point: https://covjson.org/def/domainTypes#Point
  Trajectory: https://covjson.org/def/domainTypes#Trajectory
  Section: https://covjson.org/def/domainTypes#Section
  MultiPolygonSeries: https://covjson.org/def/domainTypes#MultiPolygonSeries
  MultiPolygon: https://covjson.org/def/domainTypes#MultiPolygon
  Polygon: https://covjson.org/def/domainTypes#Polygon
  broader:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#broader
    x-jsonld-type: '@id'
  prefLabel: http://www.w3.org/2004/02/skos/core#prefLabel
  identifier: http://purl.org/dc/terms/identifier
  inDataset:
    x-jsonld-id: http://rdfs.org/ns/void#inDataset
    x-jsonld-type: '@id'
  related:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#related
    x-jsonld-type: '@id'
  altLabel: http://www.w3.org/2004/02/skos/core#altLabel
  definition: http://www.w3.org/2004/02/skos/core#definition
  note: http://www.w3.org/2004/02/skos/core#note
  authoredOn: http://purl.org/pav/authoredOn
  notation: http://www.w3.org/2004/02/skos/core#notation
  version: http://www.w3.org/ns/dcat#version
  hasVersion:
    x-jsonld-id: http://purl.org/dc/terms/hasVersion
    x-jsonld-type: '@id'
  versionInfo: http://www.w3.org/2002/07/owl#versionInfo
  deprecated: http://www.w3.org/2002/07/owl#deprecated
  hasCurrentVersion:
    x-jsonld-id: http://purl.org/pav/hasCurrentVersion
    x-jsonld-type: '@id'
  inScheme:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
    x-jsonld-type: '@id'
  sameAs:
    x-jsonld-id: http://www.w3.org/2002/07/owl#sameAs
    x-jsonld-type: '@id'
  narrower:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#narrower
    x-jsonld-type: '@id'
  isReplacedBy:
    x-jsonld-id: http://purl.org/dc/terms/isReplacedBy
    x-jsonld-type: '@id'
  replaces:
    x-jsonld-id: http://purl.org/dc/terms/replaces
    x-jsonld-type: '@id'
  member:
    x-jsonld-id: http://rs.tdwg.org/dwc/terms/member
    x-jsonld-type: '@id'
  conformsTo:
    x-jsonld-id: http://purl.org/dc/terms/conformsTo
    x-jsonld-type: '@id'
  creator: http://purl.org/dc/terms/creator
  seeAlso:
    x-jsonld-id: http://www.w3.org/2000/01/rdf-schema#seeAlso
    x-jsonld-type: '@id'
  RE_RegisterManager: http://www.isotc211.org/schemas/grg/RE_RegisterManager
  publisher: http://purl.org/dc/terms/publisher
  comment: http://www.w3.org/2000/01/rdf-schema#comment
  RE_RegisterOwner: http://www.isotc211.org/schemas/grg/RE_RegisterOwner
  license:
    x-jsonld-id: http://purl.org/dc/terms/license
    x-jsonld-type: '@id'
  alternative: http://purl.org/dc/terms/alternative
  IndexAxisType: http://www.opengis.net/cis/1.1/IndexAxisType
  spatial: http://purl.org/dc/terms/spatial
  previewInfo:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/previewInfo
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  hasEmail:
    x-jsonld-id: http://www.w3.org/2006/vcard/ns#hasEmail
    x-jsonld-type: '@id'
  QualityMeasurement: http://www.w3.org/ns/dqv#QualityMeasurement
  coverage:
    x-jsonld-id: http://www.opengis.net/cis/1.1/coverage
    x-jsonld-type: '@id'
  VideoResource: https://w3id.org/idsa/core/VideoResource
  scopeNote: http://www.w3.org/2004/02/skos/core#scopeNote
  endpointDescription:
    x-jsonld-id: http://www.w3.org/ns/dcat#endpointDescription
    x-jsonld-type: '@id'
  DigitalContent: https://w3id.org/idsa/core/DigitalContent
  affiliation: https://schema.org/affiliation
  endpointArtifact:
    x-jsonld-id: https://w3id.org/idsa/core/endpointArtifact
    x-jsonld-type: '@id'
  Unit: http://qudt.org/schema/qudt/Unit
  wasGeneratedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
    x-jsonld-type: '@id'
  created: http://purl.org/dc/terms/created
  VDataBlockType: http://www.opengis.net/cis/1.1/VDataBlockType
  ImageRepresentation: https://w3id.org/idsa/core/ImageRepresentation
  lowerBound:
    x-jsonld-id: http://www.opengis.net/cis/1.1/lowerBound
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
  GeoPoint: https://w3id.org/idsa/core/GeoPoint
  qualifiedAttribution:
    x-jsonld-id: http://www.w3.org/ns/prov#qualifiedAttribution
    x-jsonld-type: '@id'
  Dataset: http://www.w3.org/ns/dcat#Dataset
  EnvelopeByAxisType: http://www.opengis.net/cis/1.1/EnvelopeByAxisType
  width:
    x-jsonld-id: https://w3id.org/idsa/core/width
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  compressFormat:
    x-jsonld-id: http://www.w3.org/ns/dcat#compressFormat
    x-jsonld-type: '@id'
  Relationship: https://uri.etsi.org/ngsi-ld/Relationship
  concept:
    x-jsonld-id: http://purl.org/linked-data/cube#concept
    x-jsonld-type: '@id'
  ProvenanceStatement: http://purl.org/dc/terms/ProvenanceStatement
  accrualPeriodicity: http://purl.org/dc/terms/accrualPeriodicity
  Asset: http://www.w3.org/ns/odrl/2/Asset
  adms.Asset: http://www.w3.org/ns/adms#Asset
  model:
    x-jsonld-id: http://www.opengis.net/cis/1.1/model
    x-jsonld-type: '@id'
  Type: http://www.w3.org/2006/vcard/ns#Type
  MediaType: http://purl.org/dc/terms/MediaType
  Organization: https://schema.org/Organization
  vcard.Organization: http://www.w3.org/2006/vcard/ns#Organization
  Distribution: http://www.w3.org/ns/dcat#Distribution
  issued: http://purl.org/dc/terms/issued
  dataset:
    x-jsonld-id: http://www.w3.org/ns/dcat#dataset
    x-jsonld-type: '@id'
  AudioRepresentation: https://w3id.org/idsa/core/AudioRepresentation
  wasRevisionOf:
    x-jsonld-id: http://www.w3.org/ns/prov#wasRevisionOf
    x-jsonld-type: '@id'
  usageNote: http://purl.org/vocab/vann/usageNote
  AxisExtendType: http://www.opengis.net/cis/1.1/AxisExtendType
  height:
    x-jsonld-id: https://w3id.org/idsa/core/height
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  distribution:
    x-jsonld-id: http://www.w3.org/ns/dcat#distribution
    x-jsonld-type: '@id'
  downloadURL:
    x-jsonld-id: http://www.w3.org/ns/dcat#downloadURL
    x-jsonld-type: '@id'
  hasQualityMetadata:
    x-jsonld-id: http://www.w3.org/ns/dqv#hasQualityMetadata
    x-jsonld-type: '@id'
  coordinate:
    x-jsonld-id: http://www.opengis.net/cis/1.1/coordinate
    x-jsonld-type: '@id'
  ComponentProperty: http://purl.org/linked-data/cube#ComponentProperty
  dcat.hasVersion:
    x-jsonld-id: http://www.w3.org/ns/dcat#hasVersion
    x-jsonld-type: '@id'
  wasAttributedTo:
    x-jsonld-id: http://www.w3.org/ns/prov#wasAttributedTo
    x-jsonld-type: '@id'
  frameRate:
    x-jsonld-id: https://w3id.org/idsa/core/frameRate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  QualityMetadata: http://www.w3.org/ns/dqv#QualityMetadata
  Geometry: http://www.opengis.net/ont/geosparql#Geometry
  locn.Geometry: http://www.w3.org/ns/locn#Geometry
  GridLimitsType: http://www.opengis.net/cis/1.1/GridLimitsType
  hasValue:
    x-jsonld-id: https://saref.etsi.org/core/hasValue
    x-jsonld-type: '@id'
  temporalResolution: http://www.w3.org/ns/dcat#temporalResolution
  versionNotes:
    x-jsonld-id: http://www.w3.org/ns/adms#versionNotes
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  VideoRepresentation: https://w3id.org/idsa/core/VideoRepresentation
  GeoFeature: https://w3id.org/idsa/core/GeoFeature
  landingPage:
    x-jsonld-id: http://www.w3.org/ns/dcat#landingPage
    x-jsonld-type: '@id'
  maker:
    x-jsonld-id: http://xmlns.com/foaf/0.1/maker
    x-jsonld-type: '@id'
  isPrimaryTopicOf:
    x-jsonld-id: http://xmlns.com/foaf/0.1/isPrimaryTopicOf
    x-jsonld-type: '@id'
  fileReference: http://www.opengis.net/cis/1.1/fileReference
  hasAddress:
    x-jsonld-id: http://www.w3.org/2006/vcard/ns#hasAddress
    x-jsonld-type: '@id'
  DataRepresentation: https://w3id.org/idsa/core/DataRepresentation
  sensorInstanceRef:
    x-jsonld-id: http://www.sensorml.com/sensorML-2.0/sensorInstanceRef
    x-jsonld-type: '@id'
  generalGrid:
    x-jsonld-id: http://www.opengis.net/cis/1.1/generalGrid
    x-jsonld-type: '@id'
  structure:
    x-jsonld-id: http://purl.org/linked-data/cube#structure
    x-jsonld-type: '@id'
  positionValuePair:
    x-jsonld-id: http://www.opengis.net/cis/1.1/positionValuePair
    x-jsonld-type: '@id'
  PVPType: http://www.opengis.net/cis/1.1/PVPType
  hasTelephone:
    x-jsonld-id: http://www.w3.org/2006/vcard/ns#hasTelephone
    x-jsonld-type: '@id'
  scaleFactor:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/scaleFactor
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#float
  AllowedValues: http://www.opengis.net/swe/2.0/AllowedValues
  DescribedSemantically: https://w3id.org/idsa/core/DescribedSemantically
  isPartOf: http://purl.org/dc/terms/isPartOf
  filenameExtension:
    x-jsonld-id: https://w3id.org/idsa/core/filenameExtension
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  project: https://w3id.org/iliad/oim/metadata/project
  Concept: http://www.w3.org/2004/02/skos/core#Concept
  component:
    x-jsonld-id: http://purl.org/linked-data/cube#component
    x-jsonld-type: '@id'
  measure:
    x-jsonld-id: http://purl.org/linked-data/cube#measure
    x-jsonld-type: '@id'
  gridLimits:
    x-jsonld-id: http://www.opengis.net/cis/1.1/gridLimits
    x-jsonld-type: '@id'
  user:
    x-jsonld-id: http://data.europa.eu/930/user
    x-jsonld-type: '@id'
  TextRepresentation: https://w3id.org/idsa/core/TextRepresentation
  TextResource: https://w3id.org/idsa/core/TextResource
  DataResource: https://w3id.org/idsa/core/DataResource
  rangeSet:
    x-jsonld-id: http://www.opengis.net/cis/1.1/rangeSet
    x-jsonld-type: '@id'
  Location: http://purl.org/dc/terms/Location
  idsa.Location: https://w3id.org/idsa/core/Location
  rangeType:
    x-jsonld-id: http://www.opengis.net/cis/1.1/rangeType
    x-jsonld-type: '@id'
  axisLabels:
    x-jsonld-id: http://www.opengis.net/cis/1.1/axisLabels
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  path:
    x-jsonld-id: https://w3id.org/idsa/core/path
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  interpolationRestriction:
    x-jsonld-id: http://www.opengis.net/cis/1.1/interpolationRestriction
    x-jsonld-type: '@id'
  Activity: http://www.w3.org/ns/prov#Activity
  ImageResource: https://w3id.org/idsa/core/ImageResource
  spatialResolutionInMeters: http://www.w3.org/ns/dcat#spatialResolutionInMeters
  partition:
    x-jsonld-id: http://www.opengis.net/cis/1.1/partition
    x-jsonld-type: '@id'
  fn:
    x-jsonld-id: http://www.w3.org/2006/vcard/ns#fn
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  used:
    x-jsonld-id: http://www.w3.org/ns/prov#used
    x-jsonld-type: '@id'
  CoverageByPartitioningType: http://www.opengis.net/cis/1.1/CoverageByPartitioningType
  GeneralGridCoverageType: http://www.opengis.net/cis/1.1/GeneralGridCoverageType
  homepage:
    x-jsonld-id: http://xmlns.com/foaf/0.1/homepage
    x-jsonld-type: '@id'
  maxValue: https://w3id.org/iliad/oim/metadata/maxValue
  sensorModelRef:
    x-jsonld-id: http://www.sensorml.com/sensorML-2.0/sensorModelRef
    x-jsonld-type: '@id'
  Axis: http://www.opengis.net/cis/1.1/Axis
  appliedModel:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/appliedModel
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  hasQualityMeasurement:
    x-jsonld-id: http://www.w3.org/ns/dqv#hasQualityMeasurement
    x-jsonld-type: '@id'
  Graph: http://www.w3.org/2004/03/trix/rdfg-1/Graph
  Person: https://schema.org/Person
  unitsDescription:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/unitsDescription
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  Artifact: https://w3id.org/idsa/core/Artifact
  filters:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/filters
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  rightsHolder: http://purl.org/dc/terms/rightsHolder
  noDataValue:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/noDataValue
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  QualityAnnotation: http://www.w3.org/ns/dqv#QualityAnnotation
  searchText:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/searchText
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  Participant: https://w3id.org/idsa/core/Participant
  profileSchema:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/profileSchema
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  Described: https://w3id.org/idsa/core/Described
  coverageRef:
    x-jsonld-id: http://www.opengis.net/cis/1.1/coverageRef
    x-jsonld-type: '@id'
  Agent: http://xmlns.com/foaf/0.1/Agent
  dct.Agent: http://purl.org/dc/terms/Agent
  prov.Agent: http://www.w3.org/ns/prov#Agent
  ContentType: https://w3id.org/idsa/core/ContentType
  name:
    x-jsonld-id: https://schema.org/name
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  swe.name: http://www.opengis.net/swe/2.0/name
  dataBlock:
    x-jsonld-id: http://www.opengis.net/cis/1.1/dataBlock
    x-jsonld-type: '@id'
  DataService: http://www.w3.org/ns/dcat#DataService
  Individual: http://www.w3.org/2006/vcard/ns#Individual
  representation:
    x-jsonld-id: https://w3id.org/idsa/core/representation
    x-jsonld-type: '@id'
  minDate:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/minDate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTimeStamp
  Attribution: http://www.w3.org/ns/prov#Attribution
  interval:
    x-jsonld-id: http://www.opengis.net/swe/2.0/interval
    x-jsonld-type: '@id'
  wasDerivedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
    x-jsonld-type: '@id'
  uomLabel:
    x-jsonld-id: http://www.opengis.net/cis/1.1/uomLabel
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  schemaAgency:
    x-jsonld-id: http://www.w3.org/ns/adms#schemaAgency
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  RangeSetType: http://www.opengis.net/cis/1.1/RangeSetType
  allowedInterpolation:
    x-jsonld-id: http://www.opengis.net/cis/1.1/allowedInterpolation
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  geometry:
    x-jsonld-id: http://www.w3.org/ns/locn#geometry
    x-jsonld-type: '@id'
  ComponentSpecification: http://purl.org/linked-data/cube#ComponentSpecification
  axisLabel:
    x-jsonld-id: http://www.opengis.net/cis/1.1/axisLabel
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  rights: http://purl.org/dc/terms/rights
  Work: http://www.w3.org/2006/vcard/ns#Work
  TemporalEntity: http://www.w3.org/2006/time#TemporalEntity
  DataRecordType: http://www.opengis.net/swe/2.0/DataRecordType
  IrregularAxisType: http://www.opengis.net/cis/1.1/IrregularAxisType
  field:
    x-jsonld-id: http://www.opengis.net/swe/2.0/field
    x-jsonld-type: '@id'
  hadPrimarySource:
    x-jsonld-id: http://www.w3.org/ns/prov#hadPrimarySource
    x-jsonld-type: '@id'
  PartitionSetType: http://www.opengis.net/cis/1.1/PartitionSetType
  adms.identifier:
    x-jsonld-id: http://www.w3.org/ns/adms#identifier
    x-jsonld-type: '@id'
  keyword:
    x-jsonld-id: http://www.w3.org/ns/dcat#keyword
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  envelope:
    x-jsonld-id: http://www.opengis.net/cis/1.1/envelope
    x-jsonld-type: '@id'
  processor:
    x-jsonld-id: http://data.europa.eu/930/processor
    x-jsonld-type: '@id'
  bbox:
    x-jsonld-id: http://www.w3.org/ns/dcat#bbox
    x-jsonld-type: http://www.w3.org/2000/01/rdf-schema#Literal
  endpointInformation:
    x-jsonld-id: https://w3id.org/idsa/core/endpointInformation
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  subject: http://purl.org/dc/terms/subject
  fileName:
    x-jsonld-id: https://w3id.org/idsa/core/fileName
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  qualifiedRelation:
    x-jsonld-id: http://www.w3.org/ns/dcat#qualifiedRelation
    x-jsonld-type: '@id'
  metadata:
    x-jsonld-id: http://www.opengis.net/cis/1.1/metadata
    x-jsonld-type: '@id'
  byteSize: http://www.w3.org/ns/dcat#byteSize
  idsa.byteSize:
    x-jsonld-id: https://w3id.org/idsa/core/byteSize
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
  instance:
    x-jsonld-id: https://w3id.org/idsa/core/instance
    x-jsonld-type: '@id'
  isDefinedBy: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
  swe.definition:
    x-jsonld-id: http://www.opengis.net/swe/2.0/definition
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  RangeSetRefType: http://www.opengis.net/cis/1.1/RangeSetRefType
  srsName:
    x-jsonld-id: http://www.opengis.net/cis/1.1/srsName
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  principalInvestigator:
    x-jsonld-id: http://data.europa.eu/930/principalInvestigator
    x-jsonld-type: '@id'
  QuantityType: http://www.opengis.net/swe/2.0/QuantityType
  technicalManagerInfo:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/technicalManagerInfo
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  colorTable:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/colorTable
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  names:
    x-jsonld-id: http://www.opengis.net/swe/2.0/names
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  Property: https://saref.etsi.org/core/Property
  source: https://smartdatamodels.org/source
  MeasureProperty: http://purl.org/linked-data/cube#MeasureProperty
  mediaType: http://purl.org/dc/terms/mediaType
  uom:
    x-jsonld-id: http://www.opengis.net/swe/2.0/uom
    x-jsonld-type: '@id'
  subDatasetName: https://w3id.org/iliad/oim/metadata/subDatasetName
  upperBound:
    x-jsonld-id: http://www.opengis.net/cis/1.1/upperBound
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
  modified: http://purl.org/dc/terms/modified
  Frequency: http://purl.org/dc/terms/Frequency
  idsa.Frequency: https://w3id.org/idsa/core/Frequency
  Endpoint: https://w3id.org/idsa/core/Endpoint
  endpointURL:
    x-jsonld-id: http://www.w3.org/ns/dcat#endpointURL
    x-jsonld-type: '@id'
  provenance: http://purl.org/dc/terms/provenance
  samplingRate:
    x-jsonld-id: https://w3id.org/idsa/core/samplingRate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  CoverageByDomainAndRangeType: http://www.opengis.net/cis/1.1/CoverageByDomainAndRangeType
  inSeries:
    x-jsonld-id: http://www.w3.org/ns/dcat#inSeries
    x-jsonld-type: '@id'
  endpointDocumentation:
    x-jsonld-id: https://w3id.org/idsa/core/endpointDocumentation
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  distributor:
    x-jsonld-id: http://data.europa.eu/930/distributor
    x-jsonld-type: '@id'
  accessRights: http://purl.org/dc/terms/accessRights
  DCMIType: http://purl.org/dc/terms/DCMIType
  wasUsedBy:
    x-jsonld-id: http://www.w3.org/ns/prov#wasUsedBy
    x-jsonld-type: '@id'
  checkSum:
    x-jsonld-id: https://w3id.org/idsa/core/checkSum
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  contentType:
    x-jsonld-id: https://w3id.org/idsa/core/contentType
    x-jsonld-type: '@id'
  RepresentationInstance: https://w3id.org/idsa/core/RepresentationInstance
  partitionSet:
    x-jsonld-id: http://www.opengis.net/cis/1.1/partitionSet
    x-jsonld-type: '@id'
  datasetManagerInfo:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/datasetManagerInfo
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  contentStandard:
    x-jsonld-id: https://w3id.org/idsa/core/contentStandard
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#anyURI
  Entity: https://uri.etsi.org/ngsi-ld/Entity
  dataTypeSchema:
    x-jsonld-id: https://w3id.org/idsa/core/dataTypeSchema
    x-jsonld-type: '@id'
  Language: https://w3id.org/idsa/core/Language
  resourceProvider:
    x-jsonld-id: http://data.europa.eu/930/resourceProvider
    x-jsonld-type: '@id'
  contactPoint:
    x-jsonld-id: http://www.w3.org/ns/dcat#contactPoint
    x-jsonld-type: '@id'
  Resource: http://www.w3.org/ns/dcat#Resource
  idsa.Resource: https://w3id.org/idsa/core/Resource
  rdfs.Resource: http://www.w3.org/2000/01/rdf-schema#Resource
  hasQualityAnnotation:
    x-jsonld-id: http://www.w3.org/ns/dqv#hasQualityAnnotation
    x-jsonld-type: '@id'
  domainSet:
    x-jsonld-id: http://www.opengis.net/cis/1.1/domainSet
    x-jsonld-type: '@id'
  SpatialThing: http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing
  theme:
    x-jsonld-id: http://www.w3.org/ns/dcat#theme
    x-jsonld-type: '@id'
  Party: http://www.w3.org/ns/odrl/2/Party
  wasQuotedFrom:
    x-jsonld-id: http://www.w3.org/ns/prov#wasQuotedFrom
    x-jsonld-type: '@id'
  custodian:
    x-jsonld-id: http://data.europa.eu/930/custodian
    x-jsonld-type: '@id'
  Document: http://xmlns.com/foaf/0.1/Document
  language: http://purl.org/dc/terms/language
  page:
    x-jsonld-id: http://xmlns.com/foaf/0.1/page
    x-jsonld-type: '@id'
  Group: http://xmlns.com/foaf/0.1/Group
  TransformationBySensorModelType: http://www.opengis.net/cis/1.1/TransformationBySensorModelType
  uomLabels:
    x-jsonld-id: http://www.opengis.net/cis/1.1/uomLabels
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  contributor: http://purl.org/dc/terms/contributor
  originator:
    x-jsonld-id: http://data.europa.eu/930/originator
    x-jsonld-type: '@id'
  resolutionUnit:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/resolutionUnit
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  AudioResource: https://w3id.org/idsa/core/AudioResource
  DisplacementAxisNestType: http://www.opengis.net/cis/1.1/DisplacementAxisNestType
  DomainSetType: http://www.opengis.net/cis/1.1/DomainSetType
  generalizationOf:
    x-jsonld-id: http://www.w3.org/ns/prov#generalizationOf
    x-jsonld-type: '@id'
  displacement:
    x-jsonld-id: http://www.opengis.net/cis/1.1/displacement
    x-jsonld-type: '@id'
  minValue: https://w3id.org/iliad/oim/metadata/minValue
  UnitReference: http://www.opengis.net/swe/2.0/UnitReference
  specializationOf:
    x-jsonld-id: http://www.w3.org/ns/prov#specializationOf
    x-jsonld-type: '@id'
  code:
    x-jsonld-id: http://www.opengis.net/swe/2.0/code
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  Identifier: http://www.w3.org/ns/adms#Identifier
  epsg:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/epsg
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  Home: http://www.w3.org/2006/vcard/ns#Home
  ManagedEntity: https://w3id.org/idsa/core/ManagedEntity
  format: http://purl.org/dc/terms/format
  accessURL:
    x-jsonld-id: http://www.w3.org/ns/dcat#accessURL
    x-jsonld-type: '@id'
  credits:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/credits
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  sample:
    x-jsonld-id: http://www.w3.org/ns/adms#sample
    x-jsonld-type: '@id'
  BoundingPolygon: https://w3id.org/idsa/core/BoundingPolygon
  Kind: http://www.w3.org/2006/vcard/ns#Kind
  relation: http://purl.org/dc/terms/relation
  temporal: http://purl.org/dc/terms/temporal
  accrualPolicy: http://purl.org/dc/terms/accrualPolicy
  resolution:
    x-jsonld-id: http://www.opengis.net/cis/1.1/resolution
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  maxDate:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/maxDate
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTimeStamp
  constraint:
    x-jsonld-id: http://www.opengis.net/swe/2.0/constraint
    x-jsonld-type: '@id'
  ConnectorEndpoint: https://w3id.org/idsa/core/ConnectorEndpoint
  DataStructureDefinition: http://purl.org/linked-data/cube#DataStructureDefinition
  numberOfRecords:
    x-jsonld-id: https://w3id.org/iliad/oim/metadata/numberOfRecords
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
  RegularAxisType: http://www.opengis.net/cis/1.1/RegularAxisType
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
  Line: http://www.opengis.net/ont/sf#Line
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
  Deployment: http://www.w3.org/ns/ssn/Deployment
  MultiSurface: http://www.opengis.net/ont/sf#MultiSurface
  TemporalDuration: http://www.w3.org/2006/time#TemporalDuration
  Procedure: http://www.w3.org/ns/sosa/Procedure
  DiffusionCoefficient: http://purl.oclc.org/NET/ssnx/qu/dim#DiffusionCoefficient
  asGeoJSON:
    x-jsonld-id: http://www.opengis.net/ont/geosparql#asGeoJSON
    x-jsonld-type: http://www.opengis.net/ont/geosparql#geoJSONLiteral
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
  Class: http://www.w3.org/2000/01/rdf-schema#Class
  ObservationCollection: http://www.w3.org/ns/sosa/ObservationCollection
  NumberPerArea: http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerArea
  depiction: http://xmlns.com/foaf/0.1/depiction
  Curve: http://www.opengis.net/ont/sf#Curve
  Instant: http://www.w3.org/2006/time#Instant
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
  LineString: http://www.opengis.net/ont/sf#LineString
  numericValue: http://qudt.org/schema/qudt/numericValue
  attribute:
    x-jsonld-id: http://purl.org/linked-data/cube#attribute
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
  hasProperty:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasProperty
    x-jsonld-type: '@id'
  Measure: http://def.seegrid.csiro.au/isotc211/iso19103/2005/basic#Measure
  Triangle: http://www.opengis.net/ont/sf#Triangle
  observationGroup:
    x-jsonld-id: http://purl.org/linked-data/cube#observationGroup
    x-jsonld-type: '@id'
  Interval: http://www.w3.org/2006/time#Interval
  EnergyFlux: http://purl.oclc.org/NET/ssnx/qu/dim#EnergyFlux
  StressOrPressure: http://purl.oclc.org/NET/ssnx/qu/dim#StressOrPressure
  resultTime:
    x-jsonld-id: http://www.w3.org/ns/sosa/resultTime
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  VolumeDensityRate: http://purl.oclc.org/NET/ssnx/qu/dim#VolumeDensityRate
  phenomenonTime:
    x-jsonld-id: http://www.w3.org/ns/sosa/phenomenonTime
    x-jsonld-type: '@id'
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
  Scheme: http://www.w3.org/2004/02/skos/core#Scheme
  hasEnd:
    x-jsonld-id: http://www.w3.org/2006/time#hasEnd
    x-jsonld-type: '@id'
  GeometryCollection: http://www.opengis.net/ont/sf#GeometryCollection
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
  hasSubSystem:
    x-jsonld-id: http://www.w3.org/ns/ssn/hasSubSystem
    x-jsonld-type: '@id'
  Quantity: http://qudt.org/schema/qudt/Quantity
  MassFlowRate: http://purl.oclc.org/NET/ssnx/qu/dim#MassFlowRate
  qu.QuantityKind: http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind
  SpatialObjectCollection: http://www.opengis.net/ont/geosparql#SpatialObjectCollection
  Distance: http://purl.oclc.org/NET/ssnx/qu/dim#Distance
  Radiance: http://purl.oclc.org/NET/ssnx/qu/dim#Radiance
  Duration: http://purl.oclc.org/NET/ssnx/qu/dim#Duration
  TIN: http://www.opengis.net/ont/sf#TIN
  SurfaceDensity: http://purl.oclc.org/NET/ssnx/qu/dim#SurfaceDensity
  wgs84.Point: http://www.w3.org/2003/01/geo/wgs84_pos#Point
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
    x-jsonld-id: http://rs.tdwg.org/dwc/terms/order
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
  Density: http://purl.oclc.org/NET/ssnx/qu/dim#Density
  LinearRing: http://www.opengis.net/ont/sf#LinearRing
  Molality: http://purl.oclc.org/NET/ssnx/qu/dim#Molality
  inXSDDateTimeStamp:
    x-jsonld-id: http://www.w3.org/2006/time#inXSDDateTimeStamp
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTimeStamp
  PropertyKind: http://purl.oclc.org/NET/ssnx/qu/qu#PropertyKind
  SpatialObject: http://www.opengis.net/ont/geosparql#SpatialObject
  sliceStructure:
    x-jsonld-id: http://purl.org/linked-data/cube#sliceStructure
    x-jsonld-type: '@id'
  hasFeatureOfInterest:
    x-jsonld-id: https://saref.etsi.org/core/hasFeatureOfInterest
    x-jsonld-type: '@id'
  NumberPerLength: http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerLength
  lat: http://www.w3.org/2003/01/geo/wgs84_pos#lat
  VolumeFlowRate: http://purl.oclc.org/NET/ssnx/qu/dim#VolumeFlowRate
  SpecificEntropy: http://purl.oclc.org/NET/ssnx/qu/dim#SpecificEntropy
  CodedProperty: http://purl.org/linked-data/cube#CodedProperty
  slice:
    x-jsonld-id: http://purl.org/linked-data/cube#slice
    x-jsonld-type: '@id'
  madeObservation:
    x-jsonld-id: http://www.w3.org/ns/sosa/madeObservation
    x-jsonld-type: '@id'
  FeatureCollection: http://www.opengis.net/ont/geosparql#FeatureCollection
  isPropertyOf:
    x-jsonld-id: https://saref.etsi.org/core/isPropertyOf
    x-jsonld-type: '@id'
  ObservationGroup: http://purl.org/linked-data/cube#ObservationGroup
  Sample: http://www.w3.org/ns/sosa/Sample
  DataSet: http://purl.org/linked-data/cube#DataSet
  PolyhedralSurface: http://www.opengis.net/ont/sf#PolyhedralSurface
  ObservableProperty: http://www.w3.org/ns/sosa/ObservableProperty
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
  Surface: http://purl.oclc.org/NET/ssnx/cf/cf-feature#Surface
  sliceKey:
    x-jsonld-id: http://purl.org/linked-data/cube#sliceKey
    x-jsonld-type: '@id'
  dct.description: http://purl.org/dc/terms/description
  MultiCurve: http://www.opengis.net/ont/sf#MultiCurve
  hasQuantityKind:
    x-jsonld-id: http://qudt.org/schema/qudt/hasQuantityKind
    x-jsonld-type: '@id'
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
  schema.name: https://schema.org/name
  QuantityKind: http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind
  sampleSizeUnit: http://rs.tdwg.org/dwc/terms/sampleSizeUnit
  recordNumber: http://rs.tdwg.org/dwc/terms/recordNumber
  verbatimLongitude: http://rs.tdwg.org/dwc/terms/verbatimLongitude
  behavior: http://rs.tdwg.org/dwc/terms/behavior
  organismQuantity: http://rs.tdwg.org/dwc/terms/organismQuantity
  scientificNameID: http://rs.tdwg.org/dwc/terms/scientificNameID
  lowestBiostratigraphicZone: http://rs.tdwg.org/dwc/terms/lowestBiostratigraphicZone
  earliestEonOrLowestEonothem: http://rs.tdwg.org/dwc/terms/earliestEonOrLowestEonothem
  originalNameUsageID: http://rs.tdwg.org/dwc/terms/originalNameUsageID
  GeologicalContext: http://rs.tdwg.org/dwc/terms/GeologicalContext
  countryCode: http://rs.tdwg.org/dwc/terms/countryCode
  UnitOfMeasure: https://saref.etsi.org/core/UnitOfMeasure
  verbatimCoordinates: http://rs.tdwg.org/dwc/terms/verbatimCoordinates
  recordType: http://mmisw.org/ont/ioos/marine_biogeography/recordType
  maximumDistanceAboveSurfaceInMeters: http://rs.tdwg.org/dwc/terms/maximumDistanceAboveSurfaceInMeters
  verbatimLocality: http://rs.tdwg.org/dwc/terms/verbatimLocality
  identificationReferences: http://rs.tdwg.org/dwc/terms/identificationReferences
  isControlledByDevice:
    x-jsonld-id: https://saref.etsi.org/core/isControlledByDevice
    x-jsonld-type: '@id'
  verbatimCoordinateSystem: http://rs.tdwg.org/dwc/terms/verbatimCoordinateSystem
  sampleLengthInMeters: http://mmisw.org/ont/ioos/marine_biogeography/sampleLengthInMeters
  measurementType: http://rs.tdwg.org/dwc/terms/measurementType
  sampleWidthInMeters: http://mmisw.org/ont/ioos/marine_biogeography/sampleWidthInMeters
  measurementAccuracy: http://rs.tdwg.org/dwc/terms/measurementAccuracy
  genus: http://rs.tdwg.org/dwc/terms/genus
  coordinatePrecision: http://rs.tdwg.org/dwc/terms/coordinatePrecision
  weightInKg: http://mmisw.org/ont/ioos/marine_biogeography/weightInKg
  georeferencedDate: http://rs.tdwg.org/dwc/terms/georeferencedDate
  taxonomicStatus: http://rs.tdwg.org/dwc/terms/taxonomicStatus
  validFrom:
    x-jsonld-id: http://portele.de/ont/inspire/baseInspire#validFrom
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  SurfaceMediumMedium: http://purl.oclc.org/NET/ssnx/cf/cf-feature#SurfaceMediumMedium
  Humidity: https://saref.etsi.org/core/Humidity
  previousIdentifications: http://rs.tdwg.org/dwc/terms/previousIdentifications
  Period: http://def.seegrid.csiro.au/isotc211/iso19108/2002/temporal#Period
  startDayOfYear: http://rs.tdwg.org/dwc/terms/startDayOfYear
  otherCatalogNumbers: http://rs.tdwg.org/dwc/terms/otherCatalogNumbers
  MachineObservation: http://rs.tdwg.org/dwc/terms/MachineObservation
  coordinateUncertaintyInMeters: http://rs.tdwg.org/dwc/terms/coordinateUncertaintyInMeters
  eventID: http://rs.tdwg.org/dwc/terms/eventID
  Organism: http://rs.tdwg.org/dwc/terms/Organism
  identificationID: http://rs.tdwg.org/dwc/terms/identificationID
  recordedByID: http://rs.tdwg.org/dwc/terms/recordedByID
  dateCreated:
    x-jsonld-id: https://smartdatamodels.org/dateCreated
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  Identification: http://rs.tdwg.org/dwc/terms/Identification
  WeatherObserved: https://smartdatamodels.org/dataModel.Weather/WeatherObserved
  quantificationUnit: http://mmisw.org/ont/ioos/marine_biogeography/quantificationUnit
  country: http://rs.tdwg.org/dwc/terms/country
  genericName: http://rs.tdwg.org/dwc/terms/genericName
  bibliographicCitation: http://purl.org/dc/terms/bibliographicCitation
  decimalLongitude: http://rs.tdwg.org/dwc/terms/decimalLongitude
  scientificName: http://rs.tdwg.org/dwc/terms/scientificName
  organismQuantityType: http://rs.tdwg.org/dwc/terms/organismQuantityType
  catalogNumber: http://rs.tdwg.org/dwc/terms/catalogNumber
  continent: http://rs.tdwg.org/dwc/terms/continent
  minimumDistanceAboveSurfaceInMeters: http://rs.tdwg.org/dwc/terms/minimumDistanceAboveSurfaceInMeters
  dateModified:
    x-jsonld-id: https://smartdatamodels.org/dateModified
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  decimalLatitude: http://rs.tdwg.org/dwc/terms/decimalLatitude
  references: http://purl.org/dc/terms/references
  agroVocConcept:
    x-jsonld-id: https://smartdatamodels.org/dataModel.Agrifood/agroVocConcept
    x-jsonld-type: '@id'
  higherGeographyID: http://rs.tdwg.org/dwc/terms/higherGeographyID
  addressRegion: https://schema.org/addressRegion
  measurementDeterminedBy: http://rs.tdwg.org/dwc/terms/measurementDeterminedBy
  sampleShape: http://mmisw.org/ont/ioos/marine_biogeography/sampleShape
  geodeticDatum: http://rs.tdwg.org/dwc/terms/geodeticDatum
  verbatimSiteDescriptions: http://rs.tdwg.org/hc/terms/verbatimSiteDescriptions
  dataProvider: https://smartdatamodels.org/dataProvider
  maximumDepthInMeters: http://rs.tdwg.org/dwc/terms/maximumDepthInMeters
  measuresProperty:
    x-jsonld-id: https://saref.etsi.org/core/measuresProperty
    x-jsonld-type: '@id'
  locationAccordingTo: http://rs.tdwg.org/dwc/terms/locationAccordingTo
  nameAccordingTo: http://rs.tdwg.org/dwc/terms/nameAccordingTo
  group: http://rs.tdwg.org/dwc/terms/group
  class: http://rs.tdwg.org/dwc/terms/class
  footprintWKT: http://rs.tdwg.org/dwc/terms/footprintWKT
  FossilSpecimen: http://rs.tdwg.org/dwc/terms/FossilSpecimen
  snowHeight: https://smartdatamodels.org/dataModel.Weather/snowHeight
  Medium: http://purl.oclc.org/NET/ssnx/cf/cf-feature#Medium
  typeStatus: http://rs.tdwg.org/dwc/terms/typeStatus
  acceptedNameUsage: http://rs.tdwg.org/dwc/terms/acceptedNameUsage
  earliestEpochOrLowestSeries: http://rs.tdwg.org/dwc/terms/earliestEpochOrLowestSeries
  streamGauge: https://smartdatamodels.org/dataModel.Weather/streamGauge
  parentNameUsageID: http://rs.tdwg.org/dwc/terms/parentNameUsageID
  dynamicProperties: http://rs.tdwg.org/dwc/terms/dynamicProperties
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
  identificationVerificationStatus: http://rs.tdwg.org/dwc/terms/identificationVerificationStatus
  Measurement: https://saref.etsi.org/core/Measurement
  footprintSRS: http://rs.tdwg.org/dwc/terms/footprintSRS
  individualCount: http://rs.tdwg.org/dwc/terms/individualCount
  collectionCode: http://rs.tdwg.org/dwc/terms/collectionCode
  lithostratigraphicTerms: http://rs.tdwg.org/dwc/terms/lithostratigraphicTerms
  subfamily: http://rs.tdwg.org/dwc/terms/subfamily
  eventType: http://rs.tdwg.org/dwc/terms/eventType
  associatedMedia: http://rs.tdwg.org/dwc/terms/associatedMedia
  Taxon: http://rs.tdwg.org/dwc/terms/Taxon
  vernacularName: http://rs.tdwg.org/dwc/terms/vernacularName
  windDirection: https://smartdatamodels.org/dataModel.Weather/windDirection
  preparations: http://rs.tdwg.org/dwc/terms/preparations
  Event: http://rs.tdwg.org/dwc/terms/Event
  observationLocation: http://mmisw.org/ont/ioos/marine_biogeography/observationLocation
  institutionID: http://rs.tdwg.org/dwc/terms/institutionID
  WeatherForecast: https://smartdatamodels.org/dataModel.Weather/WeatherForecast
  verbatimDepth: http://rs.tdwg.org/dwc/terms/verbatimDepth
  county: http://rs.tdwg.org/dwc/terms/county
  measurementMadeBy:
    x-jsonld-id: https://saref.etsi.org/core/measurementMadeBy
    x-jsonld-type: '@id'
  earliestEraOrLowestErathem: http://rs.tdwg.org/dwc/terms/earliestEraOrLowestErathem
  occurrenceStatus: http://rs.tdwg.org/dwc/terms/occurrenceStatus
  LocationRelationship: https://uri.etsi.org/ngsi-ld/LocationRelationship
  observedMinLengthInCm: http://mmisw.org/ont/ioos/marine_biogeography/observedMinLengthInCm
  verbatimTaxonRank: http://rs.tdwg.org/dwc/terms/verbatimTaxonRank
  disposition: http://rs.tdwg.org/dwc/terms/disposition
  visibility: https://smartdatamodels.org/dataModel.Weather/visibility
  namePublishedInID: http://rs.tdwg.org/dwc/terms/namePublishedInID
  dateIdentified: http://rs.tdwg.org/dwc/terms/dateIdentified
  ImageObject: https://schema.org/ImageObject
  organismRemarks: http://rs.tdwg.org/dwc/terms/organismRemarks
  latestPeriodOrHighestSystem: http://rs.tdwg.org/dwc/terms/latestPeriodOrHighestSystem
  Precipitation: http://purl.oclc.org/NET/ssnx/cf/cf-feature#Precipitation
  taxonRemarks: http://rs.tdwg.org/dwc/terms/taxonRemarks
  georeferencedBy: http://rs.tdwg.org/dwc/terms/georeferencedBy
  verbatimElevation: http://rs.tdwg.org/dwc/terms/verbatimElevation
  higherClassification: http://rs.tdwg.org/dwc/terms/higherClassification
  waterBody: http://rs.tdwg.org/dwc/terms/waterBody
  Layer: http://purl.oclc.org/NET/ssnx/cf/cf-feature#Layer
  GeoProperty: https://uri.etsi.org/ngsi-ld/GeoProperty
  namePublishedIn: http://rs.tdwg.org/dwc/terms/namePublishedIn
  organismID: http://rs.tdwg.org/dwc/terms/organismID
  stateProvince: http://rs.tdwg.org/dwc/terms/stateProvince
  endDayOfYear: http://rs.tdwg.org/dwc/terms/endDayOfYear
  geologicalContextID: http://rs.tdwg.org/dwc/terms/geologicalContextID
  pathway: http://rs.tdwg.org/dwc/terms/pathway
  verbatimSiteNames: http://rs.tdwg.org/hc/terms/verbatimSiteNames
  parentEventID: http://rs.tdwg.org/dwc/terms/parentEventID
  datasetName: http://rs.tdwg.org/dwc/terms/datasetName
  temperature: https://smartdatamodels.org/dataModel.Weather/temperature
  measurementMethod: http://rs.tdwg.org/dwc/terms/measurementMethod
  verbatimLatitude: http://rs.tdwg.org/dwc/terms/verbatimLatitude
  parentMeasurementID: http://rs.tdwg.org/dwc/terms/parentMeasurementID
  sightingCue: http://mmisw.org/ont/ioos/marine_biogeography/sightingCue
  waterTemperatureInCelsius: http://mmisw.org/ont/ioos/marine_biogeography/waterTemperatureInCelsius
  tribe: http://rs.tdwg.org/dwc/terms/tribe
  status: https://schema.org/status
  superfamily: http://rs.tdwg.org/dwc/terms/superfamily
  sampleSizeValue: http://rs.tdwg.org/dwc/terms/sampleSizeValue
  LivingSpecimen: http://rs.tdwg.org/dwc/terms/LivingSpecimen
  visibilityType: http://mmisw.org/ont/ioos/marine_biogeography/visibilityType
  locationRemarks: http://rs.tdwg.org/dwc/terms/locationRemarks
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
  institutionCode: http://rs.tdwg.org/dwc/terms/institutionCode
  isMeasuredByDevice:
    x-jsonld-id: https://saref.etsi.org/core/isMeasuredByDevice
    x-jsonld-type: '@id'
  occurrenceID: http://rs.tdwg.org/dwc/terms/occurrenceID
  quantificationMethod: http://mmisw.org/ont/ioos/marine_biogeography/quantificationMethod
  measurementUnit: http://rs.tdwg.org/dwc/terms/measurementUnit
  lengthType: http://mmisw.org/ont/ioos/marine_biogeography/lengthType
  HumanObservation: http://rs.tdwg.org/dwc/terms/HumanObservation
  associatedSequences: http://rs.tdwg.org/dwc/terms/associatedSequences
  phylum: http://rs.tdwg.org/dwc/terms/phylum
  fieldNumber: http://rs.tdwg.org/dwc/terms/fieldNumber
  relationshipRemarks: http://rs.tdwg.org/dwc/terms/relationshipRemarks
  infragenericEpithet: http://rs.tdwg.org/dwc/terms/infragenericEpithet
  sampleVolumeInCubicMeters: http://mmisw.org/ont/ioos/marine_biogeography/sampleVolumeInCubicMeters
  resourceRelationshipID: http://rs.tdwg.org/dwc/terms/resourceRelationshipID
  relationshipOfResource: http://rs.tdwg.org/dwc/terms/relationshipOfResource
  habitat: http://rs.tdwg.org/dwc/terms/habitat
  userName:
    x-jsonld-id: https://w3id.org/demeter/agri/agriCommon#userName
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  materialSampleID: http://rs.tdwg.org/dwc/terms/materialSampleID
  georeferenceVerificationStatus: http://rs.tdwg.org/dwc/terms/georeferenceVerificationStatus
  bed: http://rs.tdwg.org/dwc/terms/bed
  locality: http://rs.tdwg.org/dwc/terms/locality
  MaterialCitation: http://rs.tdwg.org/dwc/terms/MaterialCitation
  samplingPerformedBy: http://rs.tdwg.org/hc/terms/samplingPerformedBy
  makesMeasurement:
    x-jsonld-id: https://saref.etsi.org/core/makesMeasurement
    x-jsonld-type: '@id'
  associatedTaxa: http://rs.tdwg.org/dwc/terms/associatedTaxa
  measurementDeterminedDate: http://rs.tdwg.org/dwc/terms/measurementDeterminedDate
  eventDurationUnit: http://rs.tdwg.org/hc/terms/eventDurationUnit
  vitality: http://rs.tdwg.org/dwc/terms/vitality
  minimumDepthInMeters: http://rs.tdwg.org/dwc/terms/minimumDepthInMeters
  samplingEffort: http://rs.tdwg.org/dwc/terms/samplingEffort
  pressureTendency: https://smartdatamodels.org/dataModel.Weather/pressureTendency
  streetAddress: https://schema.org/streetAddress
  eventDate: http://rs.tdwg.org/dwc/terms/eventDate
  validTo:
    x-jsonld-id: http://portele.de/ont/inspire/baseInspire#validTo
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#dateTime
  Occurrence: http://rs.tdwg.org/dwc/terms/Occurrence
  year: http://rs.tdwg.org/dwc/terms/year
  family: http://rs.tdwg.org/dwc/terms/family
  eppoConcept:
    x-jsonld-id: https://w3id.org/demeter/agri/agriCommon#eppoConcept
    x-jsonld-type: '@id'
  georeferenceSources: http://rs.tdwg.org/dwc/terms/georeferenceSources
  resourceType: http://purl.org/dc/terms/type
  weatherType: https://smartdatamodels.org/dataModel.Weather/weatherType
  MaterialSample: http://rs.tdwg.org/dwc/terms/MaterialSample
  isMeasuredIn:
    x-jsonld-id: https://saref.etsi.org/core/isMeasuredIn
    x-jsonld-type: '@id'
  island: http://rs.tdwg.org/dwc/terms/island
  dewPoint: https://smartdatamodels.org/dataModel.Weather/dewPoint
  sightingDistanceInMeters: http://mmisw.org/ont/ioos/marine_biogeography/sightingDistanceInMeters
  taxonRank: http://rs.tdwg.org/dwc/terms/taxonRank
  locationID: http://rs.tdwg.org/dwc/terms/locationID
  TemporalProperty: https://uri.etsi.org/ngsi-ld/TemporalProperty
  identificationRemarks: http://rs.tdwg.org/dwc/terms/identificationRemarks
  eventDuration: http://rs.tdwg.org/hc/terms/eventDuration
  associatedOrganisms: http://rs.tdwg.org/dwc/terms/associatedOrganisms
  sampleAreaInSquareMeters: http://mmisw.org/ont/ioos/marine_biogeography/sampleAreaInSquareMeters
  password:
    x-jsonld-id: https://w3id.org/demeter/agri/agriCommon#password
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  subgenus: http://rs.tdwg.org/dwc/terms/subgenus
  observedMaxLengthInCm: http://mmisw.org/ont/ioos/marine_biogeography/observedMaxLengthInCm
  aphiaID: http://mmisw.org/ont/ioos/marine_biogeography/aphiaID
  relationshipOfResourceID: http://rs.tdwg.org/dwc/terms/relationshipOfResourceID
  siteCount: http://rs.tdwg.org/hc/terms/siteCount
  solarRadiation: https://smartdatamodels.org/dataModel.Weather/solarRadiation
  SurfaceMedium: http://purl.oclc.org/NET/ssnx/cf/cf-feature#SurfaceMedium
  sampleHeightInMeters: http://mmisw.org/ont/ioos/marine_biogeography/sampleHeightInMeters
  earliestAgeOrLowestStage: http://rs.tdwg.org/dwc/terms/earliestAgeOrLowestStage
  relativeHumidity: https://smartdatamodels.org/dataModel.Weather/relativeHumidity
  kingdom: http://rs.tdwg.org/dwc/terms/kingdom
  totalInSample: http://mmisw.org/ont/ioos/marine_biogeography/totalInSample
  latestEonOrHighestEonothem: http://rs.tdwg.org/dwc/terms/latestEonOrHighestEonothem
  taxonConceptID: http://rs.tdwg.org/dwc/terms/taxonConceptID
  islandGroup: http://rs.tdwg.org/dwc/terms/islandGroup
  establishmentMeans: http://rs.tdwg.org/dwc/terms/establishmentMeans
  relationshipEstablishedDate: http://rs.tdwg.org/dwc/terms/relationshipEstablishedDate
  identifiedBy: http://rs.tdwg.org/dwc/terms/identifiedBy
  sex: http://rs.tdwg.org/dwc/terms/sex
  verbatimLabel: http://rs.tdwg.org/dwc/terms/verbatimLabel
  relatesToProperty:
    x-jsonld-id: https://saref.etsi.org/core/relatesToProperty
    x-jsonld-type: '@id'
  verbatimEventDate: http://rs.tdwg.org/dwc/terms/verbatimEventDate
  month: http://rs.tdwg.org/dwc/terms/month
  taxonID: http://rs.tdwg.org/dwc/terms/taxonID
  addressLocality: https://schema.org/addressLocality
  municipality: http://rs.tdwg.org/dwc/terms/municipality
  reportedWeather: http://rs.tdwg.org/hc/terms/reportedWeather
  airTemperatureForecast: https://smartdatamodels.org/dataModel.Weather/airTemperatureForecast
  nomenclaturalStatus: http://rs.tdwg.org/dwc/terms/nomenclaturalStatus
  observedIndividualLengthInCm: http://mmisw.org/ont/ioos/marine_biogeography/observedIndividualLengthInCm
  samplingProtocol: http://rs.tdwg.org/dwc/terms/samplingProtocol
  earliestPeriodOrLowestSystem: http://rs.tdwg.org/dwc/terms/earliestPeriodOrLowestSystem
  lifeStage: http://rs.tdwg.org/dwc/terms/lifeStage
  basisOfRecord: http://rs.tdwg.org/dwc/terms/basisOfRecord
  day: http://rs.tdwg.org/dwc/terms/day
  controlsProperty:
    x-jsonld-id: https://saref.etsi.org/core/controlsProperty
    x-jsonld-type: '@id'
  verticalDatum: http://rs.tdwg.org/dwc/terms/verticalDatum
  latestEpochOrHighestSeries: http://rs.tdwg.org/dwc/terms/latestEpochOrHighestSeries
  originalNameUsage: http://rs.tdwg.org/dwc/terms/originalNameUsage
  cultivarEpithet: http://rs.tdwg.org/dwc/terms/cultivarEpithet
  identifiedByID: http://rs.tdwg.org/dwc/terms/identifiedByID
  reproductiveCondition: http://rs.tdwg.org/dwc/terms/reproductiveCondition
  latestEraOrHighestErathem: http://rs.tdwg.org/dwc/terms/latestEraOrHighestErathem
  datasetID: http://rs.tdwg.org/dwc/terms/datasetID
  scientificNameAuthorship: http://rs.tdwg.org/dwc/terms/scientificNameAuthorship
  Device: https://saref.etsi.org/core/Device
  collectionID: http://rs.tdwg.org/dwc/terms/collectionID
  pointRadiusSpatialFit: http://rs.tdwg.org/dwc/terms/pointRadiusSpatialFit
  nameAccordingToID: http://rs.tdwg.org/dwc/terms/nameAccordingToID
  subtribe: http://rs.tdwg.org/dwc/terms/subtribe
  georeferenceProtocol: http://rs.tdwg.org/dwc/terms/georeferenceProtocol
  eventRemarks: http://rs.tdwg.org/dwc/terms/eventRemarks
  minimumElevationInMeters: http://rs.tdwg.org/dwc/terms/minimumElevationInMeters
  verbatimSRS: http://rs.tdwg.org/dwc/terms/verbatimSRS
  degreeOfEstablishment: http://rs.tdwg.org/dwc/terms/degreeOfEstablishment
  MeasurementOrFact: http://rs.tdwg.org/dwc/terms/MeasurementOrFact
  hasTimestamp: https://saref.etsi.org/core/hasTimestamp
  identificationQualifier: http://rs.tdwg.org/dwc/terms/identificationQualifier
  infraspecificEpithet: http://rs.tdwg.org/dwc/terms/infraspecificEpithet
  precipitation: https://smartdatamodels.org/dataModel.Weather/precipitation
  latestAgeOrHighestStage: http://rs.tdwg.org/dwc/terms/latestAgeOrHighestStage
  alternateName: https://smartdatamodels.org/alternateName
  addressCountry: https://schema.org/addressCountry
  dataGeneralizations: http://rs.tdwg.org/dwc/terms/dataGeneralizations
  SurfaceLayer: http://purl.oclc.org/NET/ssnx/cf/cf-feature#SurfaceLayer
  ResourceRelationship: http://rs.tdwg.org/dwc/terms/ResourceRelationship
  eventTime: http://rs.tdwg.org/dwc/terms/eventTime
  verbatimIdentification: http://rs.tdwg.org/dwc/terms/verbatimIdentification
  PeriodOfTime: http://purl.org/dc/terms/PeriodOfTime
  PreservedSpecimen: http://rs.tdwg.org/dwc/terms/PreservedSpecimen
  associatedReferences: http://rs.tdwg.org/dwc/terms/associatedReferences
  recordedBy: http://rs.tdwg.org/dwc/terms/recordedBy
  specificEpithet: http://rs.tdwg.org/dwc/terms/specificEpithet
  formation: http://rs.tdwg.org/dwc/terms/formation
  nomenclaturalCode: http://rs.tdwg.org/dwc/terms/nomenclaturalCode
  ResponsibleParty: http://def.seegrid.csiro.au/isotc211/iso19115/2003/citation#ResponsibleParty
  observedMeanLengthInCm: http://mmisw.org/ont/ioos/marine_biogeography/observedMeanLengthInCm
  ownerInstitutionCode: http://rs.tdwg.org/dwc/terms/ownerInstitutionCode
  relatedResourceID: http://rs.tdwg.org/dwc/terms/relatedResourceID
  windSpeed: https://smartdatamodels.org/dataModel.Weather/windSpeed
  measurementValue: http://rs.tdwg.org/dwc/terms/measurementValue
  occurrenceRemarks: http://rs.tdwg.org/dwc/terms/occurrenceRemarks
  measurementRemarks: http://rs.tdwg.org/dwc/terms/measurementRemarks
  illuminance: https://smartdatamodels.org/dataModel.Weather/illuminance
  georeferenceRemarks: http://rs.tdwg.org/dwc/terms/georeferenceRemarks
  organismScope: http://rs.tdwg.org/dwc/terms/organismScope
  resourceID: http://rs.tdwg.org/dwc/terms/resourceID
  associatedOccurrences: http://rs.tdwg.org/dwc/terms/associatedOccurrences
  relationshipAccordingTo: http://rs.tdwg.org/dwc/terms/relationshipAccordingTo
x-jsonld-vocab: https://w3id.org/iliad/oim/default-context/
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  dct: http://purl.org/dc/terms/
  qudt: http://qudt.org/schema/qudt#
  covjson: https://covjson.org/def/core#
  ignf: http://data.ign.fr/def/ignf#
  inspiregloss: http://inspire.ec.europa.eu/glossary/
  ssn: http://www.w3.org/2005/Incubator/ssn/ssnx/ssn#
  xsd: http://www.w3.org/2001/XMLSchema#
  hydra: http://www.w3.org/ns/hydra/core#
  covjsondt: https://covjson.org/def/domainTypes#
  rel: http://www.iana.org/assignments/relation/
  owl: http://www.w3.org/2002/07/owl#
  dce: http://purl.org/dc/elements/1.1/
  ns0: http://www.w3.org/ns/dx/conneg/altr#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  iop: https://w3id.org/iadopt/ont#
  ns1: http://www.w3.org/ns/dx/prof/
  puv: https://w3id.org/env/puv#
  semapv: http://w3id.org/semapv/vocab/
  reg: http://purl.org/linked-data/registry#
  dcat: http://www.w3.org/ns/dcat#
  grg: http://www.isotc211.org/schemas/grg/
  prov: https://www.w3.org/ns/prov#
  cpm: http://purl.org/voc/cpm#
  void: http://rdfs.org/ns/void#
  pav: http://purl.org/pav/
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  sssom: https://w3id.org/sssom/schema/
  dc: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_sdn/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_sdn/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "https://w3id.org/iliad/oim/default-context/",
    "long_name": "https://w3id.org/iliad/oim/default-context/long_name",
    "standard_name": "https://w3id.org/iliad/oim/default-context/standard_name",
    "units": "https://w3id.org/iliad/oim/default-context/units",
    "_ARRAY_DIMENSIONS": "https://w3id.org/iliad/oim/default-context/_ARRAY_DIMENSIONS",
    "Conventions": "https://w3id.org/iliad/oim/default-context/Conventions",
    "units_metadata": "https://w3id.org/iliad/oim/default-context/units_metadata",
    "cell_methods": "https://w3id.org/iliad/oim/default-context/cell_methods",
    "created_by": "https://w3id.org/iliad/oim/default-context/created_by",
    "date": "dct:date",
    "crs_wkt": "https://w3id.org/iliad/oim/default-context/crs_wkt",
    "geotransform": "https://w3id.org/iliad/oim/default-context/geotransform",
    "proj4": "https://w3id.org/iliad/oim/default-context/proj4",
    "spatial_ref": "https://w3id.org/iliad/oim/default-context/spatial_ref",
    "epsg_code": "https://w3id.org/iliad/oim/default-context/epsg_code",
    "grid_mapping_name": "https://w3id.org/iliad/oim/default-context/grid_mapping_name",
    "inverse_flattening": "https://w3id.org/iliad/oim/default-context/inverse_flattening",
    "semi_major_axis": "https://w3id.org/iliad/oim/default-context/semi_major_axis",
    "ancillary_variables": "https://w3id.org/iliad/oim/default-context/ancillary_variables",
    "axis": {
      "@id": "http://www.opengis.net/cis/1.1/axis",
      "@type": "@id"
    },
    "grid_mapping": "https://w3id.org/iliad/oim/default-context/grid_mapping",
    "sdn_parameter_name": "https://w3id.org/iliad/oim/default-context/sdn_parameter_name",
    "sdn_parameter_urn": "https://w3id.org/iliad/oim/default-context/sdn_parameter_urn",
    "sdn_uom_name": "https://w3id.org/iliad/oim/default-context/sdn_uom_name",
    "sdn_uom_urn": "https://w3id.org/iliad/oim/default-context/sdn_uom_urn",
    "id": "@id",
    "type": "@type",
    "value": "@value",
    "label": {
      "@id": "rdfs:label",
      "@container": "@language"
    },
    "title": {
      "@id": "dct:title",
      "@container": "@language"
    },
    "description": {
      "@id": "dct:description",
      "@container": "@language"
    },
    "unit": "qudt:unit",
    "symbol": "qudt:symbol",
    "Domain": "covjson:Domain",
    "domain": "covjson:domain",
    "domainType": {
      "@id": "covjson:domainType",
      "@type": "@vocab"
    },
    "axes": {
      "@id": "covjson:axis",
      "@container": "@index"
    },
    "dataType": {
      "@id": "https://w3id.org/idsa/core/dataType",
      "@type": "xsd:anyURI"
    },
    "primitive": "covjson:primitive",
    "tuple": "covjson:tuple",
    "polygon": "covjson:polygon",
    "num": "covjson:num",
    "start": "covjson:start",
    "stop": "covjson:stop",
    "referencing": {
      "@id": "covjson:referencing",
      "@container": "@set"
    },
    "components": {
      "@id": "covjson:components",
      "@container": "@list"
    },
    "system": "covjson:referenceSystem",
    "RS": "covjson:ReferenceSystem",
    "CRS": "covjson:CoordinateReferenceSystem",
    "cs": "ignf:coordinateSystem",
    "CS": "ignf:CoordinateSystem",
    "TemporalRS": "inspiregloss:TemporalReferenceSystem",
    "TemporalCRS": "covjson:TemporalCRS",
    "calendar": {
      "@id": "covjson:calendar",
      "@type": "@vocab"
    },
    "Gregorian": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian",
    "timeScale": "covjson:timeScale",
    "SpatialRS": "inspiregloss:SpatialReferenceSystem",
    "SpatialCRS": "ignf:CRS",
    "GeodeticCRS": "ignf:GeodeticCRS",
    "ProjectedCRS": "ignf:ProjectedCRS",
    "VerticalCRS": "ignf:VerticalCRS",
    "datum": "ignf:datum",
    "csAxes": {
      "@id": "covjson:coordinateSystemAxes",
      "@container": "@list"
    },
    "direction": "ignf:axisDirection",
    "IdentifierRS": "covjson:IdentifierReferenceSystem",
    "targetConcept": "covjson:targetConcept",
    "identifiers": {
      "@id": "covjson:identifier",
      "@type": "@id",
      "@container": "@index"
    },
    "Parameter": "covjson:Parameter",
    "parameters": {
      "@id": "covjson:parameter",
      "@type": "@id",
      "@container": "@index"
    },
    "observedProperty": "ssn:observedProperty",
    "categoryEncoding": "covjson:categoryEncoding",
    "ParameterGroup": "covjson:ParameterGroup",
    "members": {
      "@id": "covjson:member",
      "@type": "@vocab",
      "@container": "@set"
    },
    "ranges": {
      "@id": "covjson:range",
      "@type": "@id",
      "@container": "@index"
    },
    "NdArray": "covjson:NdArray",
    "TiledNdArray": "covjson:TiledNdArray",
    "shape": {
      "@id": "covjson:shape",
      "@container": "@list"
    },
    "tileShape": {
      "@id": "covjson:tileShape",
      "@container": "@list"
    },
    "axisNames": {
      "@id": "covjson:axisNames",
      "@container": "@list"
    },
    "urlTemplate": "covjson:urlTemplate",
    "tileSets": {
      "@id": "covjson:tileSet",
      "@container": "@set"
    },
    "float": "xsd:double",
    "integer": "xsd:integer",
    "string": "xsd:string",
    "Coverage": "covjson:Coverage",
    "coverages": {
      "@id": "hydra:member",
      "@container": "@set"
    },
    "CoverageCollection": "covjson:CoverageCollection",
    "Grid": "covjsondt:Grid",
    "VerticalProfile": "covjsondt:VerticalProfile",
    "MultiPointSeries": "covjsondt:MultiPointSeries",
    "MultiPoint": "covjsondt:MultiPoint",
    "PointSeries": "covjsondt:PointSeries",
    "Point": "covjsondt:Point",
    "Trajectory": "covjsondt:Trajectory",
    "Section": "covjsondt:Section",
    "MultiPolygonSeries": "covjsondt:MultiPolygonSeries",
    "MultiPolygon": "covjsondt:MultiPolygon",
    "Polygon": "covjsondt:Polygon",
    "broader": {
      "@id": "skos:broader",
      "@type": "@id"
    },
    "prefLabel": "skos:prefLabel",
    "identifier": "dct:identifier",
    "inDataset": {
      "@id": "void:inDataset",
      "@type": "@id"
    },
    "related": {
      "@id": "skos:related",
      "@type": "@id"
    },
    "altLabel": "skos:altLabel",
    "definition": "skos:definition",
    "note": "skos:note",
    "authoredOn": "pav:authoredOn",
    "notation": "skos:notation",
    "version": "dcat:version",
    "hasVersion": {
      "@id": "dct:hasVersion",
      "@type": "@id"
    },
    "versionInfo": "owl:versionInfo",
    "deprecated": "owl:deprecated",
    "hasCurrentVersion": {
      "@id": "pav:hasCurrentVersion",
      "@type": "@id"
    },
    "inScheme": {
      "@id": "skos:inScheme",
      "@type": "@id"
    },
    "sameAs": {
      "@id": "owl:sameAs",
      "@type": "@id"
    },
    "narrower": {
      "@id": "skos:narrower",
      "@type": "@id"
    },
    "isReplacedBy": {
      "@id": "dct:isReplacedBy",
      "@type": "@id"
    },
    "replaces": {
      "@id": "dct:replaces",
      "@type": "@id"
    },
    "member": {
      "@id": "http://rs.tdwg.org/dwc/terms/member",
      "@type": "@id"
    },
    "conformsTo": {
      "@id": "dct:conformsTo",
      "@type": "@id"
    },
    "creator": "dct:creator",
    "seeAlso": {
      "@id": "rdfs:seeAlso",
      "@type": "@id"
    },
    "RE_RegisterManager": "grg:RE_RegisterManager",
    "publisher": "dct:publisher",
    "comment": "rdfs:comment",
    "RE_RegisterOwner": "grg:RE_RegisterOwner",
    "license": {
      "@id": "dct:license",
      "@type": "@id"
    },
    "alternative": "dct:alternative",
    "IndexAxisType": "http://www.opengis.net/cis/1.1/IndexAxisType",
    "spatial": "dct:spatial",
    "previewInfo": {
      "@id": "https://w3id.org/iliad/oim/metadata/previewInfo",
      "@type": "xsd:string"
    },
    "hasEmail": {
      "@id": "http://www.w3.org/2006/vcard/ns#hasEmail",
      "@type": "@id"
    },
    "QualityMeasurement": "http://www.w3.org/ns/dqv#QualityMeasurement",
    "coverage": {
      "@id": "http://www.opengis.net/cis/1.1/coverage",
      "@type": "@id"
    },
    "VideoResource": "https://w3id.org/idsa/core/VideoResource",
    "scopeNote": "skos:scopeNote",
    "endpointDescription": {
      "@id": "dcat:endpointDescription",
      "@type": "@id"
    },
    "DigitalContent": "https://w3id.org/idsa/core/DigitalContent",
    "affiliation": "https://schema.org/affiliation",
    "endpointArtifact": {
      "@id": "https://w3id.org/idsa/core/endpointArtifact",
      "@type": "@id"
    },
    "Unit": "http://qudt.org/schema/qudt/Unit",
    "wasGeneratedBy": {
      "@id": "http://www.w3.org/ns/prov#wasGeneratedBy",
      "@type": "@id"
    },
    "created": "dct:created",
    "VDataBlockType": "http://www.opengis.net/cis/1.1/VDataBlockType",
    "ImageRepresentation": "https://w3id.org/idsa/core/ImageRepresentation",
    "lowerBound": {
      "@id": "http://www.opengis.net/cis/1.1/lowerBound",
      "@type": "xsd:integer"
    },
    "GeoPoint": "https://w3id.org/idsa/core/GeoPoint",
    "qualifiedAttribution": {
      "@id": "http://www.w3.org/ns/prov#qualifiedAttribution",
      "@type": "@id"
    },
    "Dataset": "dcat:Dataset",
    "EnvelopeByAxisType": "http://www.opengis.net/cis/1.1/EnvelopeByAxisType",
    "width": {
      "@id": "https://w3id.org/idsa/core/width",
      "@type": "xsd:decimal"
    },
    "compressFormat": {
      "@id": "dcat:compressFormat",
      "@type": "@id"
    },
    "Relationship": "https://uri.etsi.org/ngsi-ld/Relationship",
    "concept": {
      "@id": "http://purl.org/linked-data/cube#concept",
      "@type": "@id"
    },
    "ProvenanceStatement": "dct:ProvenanceStatement",
    "accrualPeriodicity": "dct:accrualPeriodicity",
    "Asset": "http://www.w3.org/ns/odrl/2/Asset",
    "adms.Asset": "http://www.w3.org/ns/adms#Asset",
    "model": {
      "@id": "http://www.opengis.net/cis/1.1/model",
      "@type": "@id"
    },
    "Type": "http://www.w3.org/2006/vcard/ns#Type",
    "MediaType": "dct:MediaType",
    "Organization": "https://schema.org/Organization",
    "vcard.Organization": "http://www.w3.org/2006/vcard/ns#Organization",
    "Distribution": "dcat:Distribution",
    "issued": "dct:issued",
    "dataset": {
      "@id": "dcat:dataset",
      "@type": "@id"
    },
    "AudioRepresentation": "https://w3id.org/idsa/core/AudioRepresentation",
    "wasRevisionOf": {
      "@id": "http://www.w3.org/ns/prov#wasRevisionOf",
      "@type": "@id"
    },
    "usageNote": "http://purl.org/vocab/vann/usageNote",
    "AxisExtendType": "http://www.opengis.net/cis/1.1/AxisExtendType",
    "height": {
      "@id": "https://w3id.org/idsa/core/height",
      "@type": "xsd:decimal"
    },
    "distribution": {
      "@id": "dcat:distribution",
      "@type": "@id"
    },
    "downloadURL": {
      "@id": "dcat:downloadURL",
      "@type": "@id"
    },
    "hasQualityMetadata": {
      "@id": "http://www.w3.org/ns/dqv#hasQualityMetadata",
      "@type": "@id"
    },
    "coordinate": {
      "@id": "http://www.opengis.net/cis/1.1/coordinate",
      "@type": "@id"
    },
    "ComponentProperty": "http://purl.org/linked-data/cube#ComponentProperty",
    "dcat.hasVersion": {
      "@id": "dcat:hasVersion",
      "@type": "@id"
    },
    "wasAttributedTo": {
      "@id": "http://www.w3.org/ns/prov#wasAttributedTo",
      "@type": "@id"
    },
    "frameRate": {
      "@id": "https://w3id.org/idsa/core/frameRate",
      "@type": "xsd:decimal"
    },
    "QualityMetadata": "http://www.w3.org/ns/dqv#QualityMetadata",
    "Geometry": "http://www.opengis.net/ont/geosparql#Geometry",
    "locn.Geometry": "http://www.w3.org/ns/locn#Geometry",
    "GridLimitsType": "http://www.opengis.net/cis/1.1/GridLimitsType",
    "hasValue": {
      "@id": "https://saref.etsi.org/core/hasValue",
      "@type": "@id"
    },
    "temporalResolution": "dcat:temporalResolution",
    "versionNotes": {
      "@id": "http://www.w3.org/ns/adms#versionNotes",
      "@type": "rdfs:Literal"
    },
    "VideoRepresentation": "https://w3id.org/idsa/core/VideoRepresentation",
    "GeoFeature": "https://w3id.org/idsa/core/GeoFeature",
    "landingPage": {
      "@id": "dcat:landingPage",
      "@type": "@id"
    },
    "maker": {
      "@id": "http://xmlns.com/foaf/0.1/maker",
      "@type": "@id"
    },
    "isPrimaryTopicOf": {
      "@id": "http://xmlns.com/foaf/0.1/isPrimaryTopicOf",
      "@type": "@id"
    },
    "fileReference": "http://www.opengis.net/cis/1.1/fileReference",
    "hasAddress": {
      "@id": "http://www.w3.org/2006/vcard/ns#hasAddress",
      "@type": "@id"
    },
    "DataRepresentation": "https://w3id.org/idsa/core/DataRepresentation",
    "sensorInstanceRef": {
      "@id": "http://www.sensorml.com/sensorML-2.0/sensorInstanceRef",
      "@type": "@id"
    },
    "generalGrid": {
      "@id": "http://www.opengis.net/cis/1.1/generalGrid",
      "@type": "@id"
    },
    "structure": {
      "@id": "http://purl.org/linked-data/cube#structure",
      "@type": "@id"
    },
    "positionValuePair": {
      "@id": "http://www.opengis.net/cis/1.1/positionValuePair",
      "@type": "@id"
    },
    "PVPType": "http://www.opengis.net/cis/1.1/PVPType",
    "hasTelephone": {
      "@id": "http://www.w3.org/2006/vcard/ns#hasTelephone",
      "@type": "@id"
    },
    "scaleFactor": {
      "@id": "https://w3id.org/iliad/oim/metadata/scaleFactor",
      "@type": "xsd:float"
    },
    "AllowedValues": "http://www.opengis.net/swe/2.0/AllowedValues",
    "DescribedSemantically": "https://w3id.org/idsa/core/DescribedSemantically",
    "isPartOf": "dct:isPartOf",
    "filenameExtension": {
      "@id": "https://w3id.org/idsa/core/filenameExtension",
      "@type": "xsd:string"
    },
    "project": "https://w3id.org/iliad/oim/metadata/project",
    "Concept": "skos:Concept",
    "component": {
      "@id": "http://purl.org/linked-data/cube#component",
      "@type": "@id"
    },
    "measure": {
      "@id": "http://purl.org/linked-data/cube#measure",
      "@type": "@id"
    },
    "gridLimits": {
      "@id": "http://www.opengis.net/cis/1.1/gridLimits",
      "@type": "@id"
    },
    "user": {
      "@id": "http://data.europa.eu/930/user",
      "@type": "@id"
    },
    "TextRepresentation": "https://w3id.org/idsa/core/TextRepresentation",
    "TextResource": "https://w3id.org/idsa/core/TextResource",
    "DataResource": "https://w3id.org/idsa/core/DataResource",
    "rangeSet": {
      "@id": "http://www.opengis.net/cis/1.1/rangeSet",
      "@type": "@id"
    },
    "Location": "dct:Location",
    "idsa.Location": "https://w3id.org/idsa/core/Location",
    "rangeType": {
      "@id": "http://www.opengis.net/cis/1.1/rangeType",
      "@type": "@id"
    },
    "axisLabels": {
      "@id": "http://www.opengis.net/cis/1.1/axisLabels",
      "@type": "xsd:string"
    },
    "path": {
      "@id": "https://w3id.org/idsa/core/path",
      "@type": "xsd:string"
    },
    "interpolationRestriction": {
      "@id": "http://www.opengis.net/cis/1.1/interpolationRestriction",
      "@type": "@id"
    },
    "Activity": "http://www.w3.org/ns/prov#Activity",
    "ImageResource": "https://w3id.org/idsa/core/ImageResource",
    "spatialResolutionInMeters": "dcat:spatialResolutionInMeters",
    "partition": {
      "@id": "http://www.opengis.net/cis/1.1/partition",
      "@type": "@id"
    },
    "fn": {
      "@id": "http://www.w3.org/2006/vcard/ns#fn",
      "@type": "xsd:string"
    },
    "used": {
      "@id": "http://www.w3.org/ns/prov#used",
      "@type": "@id"
    },
    "CoverageByPartitioningType": "http://www.opengis.net/cis/1.1/CoverageByPartitioningType",
    "GeneralGridCoverageType": "http://www.opengis.net/cis/1.1/GeneralGridCoverageType",
    "homepage": {
      "@id": "http://xmlns.com/foaf/0.1/homepage",
      "@type": "@id"
    },
    "maxValue": "https://w3id.org/iliad/oim/metadata/maxValue",
    "sensorModelRef": {
      "@id": "http://www.sensorml.com/sensorML-2.0/sensorModelRef",
      "@type": "@id"
    },
    "Axis": "http://www.opengis.net/cis/1.1/Axis",
    "appliedModel": {
      "@id": "https://w3id.org/iliad/oim/metadata/appliedModel",
      "@type": "xsd:string"
    },
    "hasQualityMeasurement": {
      "@id": "http://www.w3.org/ns/dqv#hasQualityMeasurement",
      "@type": "@id"
    },
    "Graph": "http://www.w3.org/2004/03/trix/rdfg-1/Graph",
    "Person": "https://schema.org/Person",
    "unitsDescription": {
      "@id": "https://w3id.org/iliad/oim/metadata/unitsDescription",
      "@type": "xsd:string"
    },
    "Artifact": "https://w3id.org/idsa/core/Artifact",
    "filters": {
      "@id": "https://w3id.org/iliad/oim/metadata/filters",
      "@type": "xsd:string"
    },
    "rightsHolder": "dct:rightsHolder",
    "noDataValue": {
      "@id": "https://w3id.org/iliad/oim/metadata/noDataValue",
      "@type": "xsd:string"
    },
    "QualityAnnotation": "http://www.w3.org/ns/dqv#QualityAnnotation",
    "searchText": {
      "@id": "https://w3id.org/iliad/oim/metadata/searchText",
      "@type": "xsd:string"
    },
    "Participant": "https://w3id.org/idsa/core/Participant",
    "profileSchema": {
      "@id": "https://w3id.org/iliad/oim/metadata/profileSchema",
      "@type": "xsd:string"
    },
    "Described": "https://w3id.org/idsa/core/Described",
    "coverageRef": {
      "@id": "http://www.opengis.net/cis/1.1/coverageRef",
      "@type": "@id"
    },
    "Agent": "http://xmlns.com/foaf/0.1/Agent",
    "dct.Agent": "dct:Agent",
    "prov.Agent": "http://www.w3.org/ns/prov#Agent",
    "ContentType": "https://w3id.org/idsa/core/ContentType",
    "name": {
      "@id": "https://schema.org/name",
      "@type": "rdfs:Literal"
    },
    "swe.name": "http://www.opengis.net/swe/2.0/name",
    "dataBlock": {
      "@id": "http://www.opengis.net/cis/1.1/dataBlock",
      "@type": "@id"
    },
    "DataService": "dcat:DataService",
    "Individual": "http://www.w3.org/2006/vcard/ns#Individual",
    "representation": {
      "@id": "https://w3id.org/idsa/core/representation",
      "@type": "@id"
    },
    "minDate": {
      "@id": "https://w3id.org/iliad/oim/metadata/minDate",
      "@type": "xsd:dateTimeStamp"
    },
    "Attribution": "http://www.w3.org/ns/prov#Attribution",
    "interval": {
      "@id": "http://www.opengis.net/swe/2.0/interval",
      "@type": "@id"
    },
    "wasDerivedFrom": {
      "@id": "http://www.w3.org/ns/prov#wasDerivedFrom",
      "@type": "@id"
    },
    "uomLabel": {
      "@id": "http://www.opengis.net/cis/1.1/uomLabel",
      "@type": "xsd:string"
    },
    "schemaAgency": {
      "@id": "http://www.w3.org/ns/adms#schemaAgency",
      "@type": "rdfs:Literal"
    },
    "RangeSetType": "http://www.opengis.net/cis/1.1/RangeSetType",
    "allowedInterpolation": {
      "@id": "http://www.opengis.net/cis/1.1/allowedInterpolation",
      "@type": "xsd:anyURI"
    },
    "geometry": {
      "@id": "http://www.w3.org/ns/locn#geometry",
      "@type": "@id"
    },
    "ComponentSpecification": "http://purl.org/linked-data/cube#ComponentSpecification",
    "axisLabel": {
      "@id": "http://www.opengis.net/cis/1.1/axisLabel",
      "@type": "xsd:string"
    },
    "rights": "dct:rights",
    "Work": "http://www.w3.org/2006/vcard/ns#Work",
    "TemporalEntity": "http://www.w3.org/2006/time#TemporalEntity",
    "DataRecordType": "http://www.opengis.net/swe/2.0/DataRecordType",
    "IrregularAxisType": "http://www.opengis.net/cis/1.1/IrregularAxisType",
    "field": {
      "@id": "http://www.opengis.net/swe/2.0/field",
      "@type": "@id"
    },
    "hadPrimarySource": {
      "@id": "http://www.w3.org/ns/prov#hadPrimarySource",
      "@type": "@id"
    },
    "PartitionSetType": "http://www.opengis.net/cis/1.1/PartitionSetType",
    "adms.identifier": {
      "@id": "http://www.w3.org/ns/adms#identifier",
      "@type": "@id"
    },
    "keyword": {
      "@id": "dcat:keyword",
      "@type": "rdfs:Literal"
    },
    "envelope": {
      "@id": "http://www.opengis.net/cis/1.1/envelope",
      "@type": "@id"
    },
    "processor": {
      "@id": "http://data.europa.eu/930/processor",
      "@type": "@id"
    },
    "bbox": {
      "@id": "dcat:bbox",
      "@type": "rdfs:Literal"
    },
    "endpointInformation": {
      "@id": "https://w3id.org/idsa/core/endpointInformation",
      "@type": "xsd:string"
    },
    "subject": "dct:subject",
    "fileName": {
      "@id": "https://w3id.org/idsa/core/fileName",
      "@type": "xsd:string"
    },
    "qualifiedRelation": {
      "@id": "dcat:qualifiedRelation",
      "@type": "@id"
    },
    "metadata": {
      "@id": "http://www.opengis.net/cis/1.1/metadata",
      "@type": "@id"
    },
    "byteSize": "dcat:byteSize",
    "idsa.byteSize": {
      "@id": "https://w3id.org/idsa/core/byteSize",
      "@type": "xsd:integer"
    },
    "instance": {
      "@id": "https://w3id.org/idsa/core/instance",
      "@type": "@id"
    },
    "isDefinedBy": "rdfs:isDefinedBy",
    "swe.definition": {
      "@id": "http://www.opengis.net/swe/2.0/definition",
      "@type": "xsd:string"
    },
    "RangeSetRefType": "http://www.opengis.net/cis/1.1/RangeSetRefType",
    "srsName": {
      "@id": "http://www.opengis.net/cis/1.1/srsName",
      "@type": "xsd:anyURI"
    },
    "principalInvestigator": {
      "@id": "http://data.europa.eu/930/principalInvestigator",
      "@type": "@id"
    },
    "QuantityType": "http://www.opengis.net/swe/2.0/QuantityType",
    "technicalManagerInfo": {
      "@id": "https://w3id.org/iliad/oim/metadata/technicalManagerInfo",
      "@type": "xsd:string"
    },
    "colorTable": {
      "@id": "https://w3id.org/iliad/oim/metadata/colorTable",
      "@type": "xsd:string"
    },
    "names": {
      "@id": "http://www.opengis.net/swe/2.0/names",
      "@type": "xsd:string"
    },
    "Property": "https://saref.etsi.org/core/Property",
    "source": "https://smartdatamodels.org/source",
    "MeasureProperty": "http://purl.org/linked-data/cube#MeasureProperty",
    "mediaType": "dct:mediaType",
    "uom": {
      "@id": "http://www.opengis.net/swe/2.0/uom",
      "@type": "@id"
    },
    "subDatasetName": "https://w3id.org/iliad/oim/metadata/subDatasetName",
    "upperBound": {
      "@id": "http://www.opengis.net/cis/1.1/upperBound",
      "@type": "xsd:integer"
    },
    "modified": "dct:modified",
    "Frequency": "dct:Frequency",
    "idsa.Frequency": "https://w3id.org/idsa/core/Frequency",
    "Endpoint": "https://w3id.org/idsa/core/Endpoint",
    "endpointURL": {
      "@id": "dcat:endpointURL",
      "@type": "@id"
    },
    "provenance": "dct:provenance",
    "samplingRate": {
      "@id": "https://w3id.org/idsa/core/samplingRate",
      "@type": "xsd:decimal"
    },
    "CoverageByDomainAndRangeType": "http://www.opengis.net/cis/1.1/CoverageByDomainAndRangeType",
    "inSeries": {
      "@id": "dcat:inSeries",
      "@type": "@id"
    },
    "endpointDocumentation": {
      "@id": "https://w3id.org/idsa/core/endpointDocumentation",
      "@type": "xsd:anyURI"
    },
    "distributor": {
      "@id": "http://data.europa.eu/930/distributor",
      "@type": "@id"
    },
    "accessRights": "dct:accessRights",
    "DCMIType": "dct:DCMIType",
    "wasUsedBy": {
      "@id": "http://www.w3.org/ns/prov#wasUsedBy",
      "@type": "@id"
    },
    "checkSum": {
      "@id": "https://w3id.org/idsa/core/checkSum",
      "@type": "xsd:string"
    },
    "contentType": {
      "@id": "https://w3id.org/idsa/core/contentType",
      "@type": "@id"
    },
    "RepresentationInstance": "https://w3id.org/idsa/core/RepresentationInstance",
    "partitionSet": {
      "@id": "http://www.opengis.net/cis/1.1/partitionSet",
      "@type": "@id"
    },
    "datasetManagerInfo": {
      "@id": "https://w3id.org/iliad/oim/metadata/datasetManagerInfo",
      "@type": "xsd:string"
    },
    "contentStandard": {
      "@id": "https://w3id.org/idsa/core/contentStandard",
      "@type": "xsd:anyURI"
    },
    "Entity": "https://uri.etsi.org/ngsi-ld/Entity",
    "dataTypeSchema": {
      "@id": "https://w3id.org/idsa/core/dataTypeSchema",
      "@type": "@id"
    },
    "Language": "https://w3id.org/idsa/core/Language",
    "resourceProvider": {
      "@id": "http://data.europa.eu/930/resourceProvider",
      "@type": "@id"
    },
    "contactPoint": {
      "@id": "dcat:contactPoint",
      "@type": "@id"
    },
    "Resource": "dcat:Resource",
    "idsa.Resource": "https://w3id.org/idsa/core/Resource",
    "rdfs.Resource": "rdfs:Resource",
    "hasQualityAnnotation": {
      "@id": "http://www.w3.org/ns/dqv#hasQualityAnnotation",
      "@type": "@id"
    },
    "domainSet": {
      "@id": "http://www.opengis.net/cis/1.1/domainSet",
      "@type": "@id"
    },
    "SpatialThing": "http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing",
    "theme": {
      "@id": "dcat:theme",
      "@type": "@id"
    },
    "Party": "http://www.w3.org/ns/odrl/2/Party",
    "wasQuotedFrom": {
      "@id": "http://www.w3.org/ns/prov#wasQuotedFrom",
      "@type": "@id"
    },
    "custodian": {
      "@id": "http://data.europa.eu/930/custodian",
      "@type": "@id"
    },
    "Document": "http://xmlns.com/foaf/0.1/Document",
    "language": "dct:language",
    "page": {
      "@id": "http://xmlns.com/foaf/0.1/page",
      "@type": "@id"
    },
    "Group": "http://xmlns.com/foaf/0.1/Group",
    "TransformationBySensorModelType": "http://www.opengis.net/cis/1.1/TransformationBySensorModelType",
    "uomLabels": {
      "@id": "http://www.opengis.net/cis/1.1/uomLabels",
      "@type": "xsd:string"
    },
    "contributor": "dct:contributor",
    "originator": {
      "@id": "http://data.europa.eu/930/originator",
      "@type": "@id"
    },
    "resolutionUnit": {
      "@id": "https://w3id.org/iliad/oim/metadata/resolutionUnit",
      "@type": "xsd:string"
    },
    "AudioResource": "https://w3id.org/idsa/core/AudioResource",
    "DisplacementAxisNestType": "http://www.opengis.net/cis/1.1/DisplacementAxisNestType",
    "DomainSetType": "http://www.opengis.net/cis/1.1/DomainSetType",
    "generalizationOf": {
      "@id": "http://www.w3.org/ns/prov#generalizationOf",
      "@type": "@id"
    },
    "displacement": {
      "@id": "http://www.opengis.net/cis/1.1/displacement",
      "@type": "@id"
    },
    "minValue": "https://w3id.org/iliad/oim/metadata/minValue",
    "UnitReference": "http://www.opengis.net/swe/2.0/UnitReference",
    "specializationOf": {
      "@id": "http://www.w3.org/ns/prov#specializationOf",
      "@type": "@id"
    },
    "code": {
      "@id": "http://www.opengis.net/swe/2.0/code",
      "@type": "xsd:string"
    },
    "Identifier": "http://www.w3.org/ns/adms#Identifier",
    "epsg": {
      "@id": "https://w3id.org/iliad/oim/metadata/epsg",
      "@type": "xsd:string"
    },
    "Home": "http://www.w3.org/2006/vcard/ns#Home",
    "ManagedEntity": "https://w3id.org/idsa/core/ManagedEntity",
    "format": "dct:format",
    "accessURL": {
      "@id": "dcat:accessURL",
      "@type": "@id"
    },
    "credits": {
      "@id": "https://w3id.org/iliad/oim/metadata/credits",
      "@type": "xsd:string"
    },
    "sample": {
      "@id": "http://www.w3.org/ns/adms#sample",
      "@type": "@id"
    },
    "BoundingPolygon": "https://w3id.org/idsa/core/BoundingPolygon",
    "Kind": "http://www.w3.org/2006/vcard/ns#Kind",
    "relation": "dct:relation",
    "temporal": "dct:temporal",
    "accrualPolicy": "dct:accrualPolicy",
    "resolution": {
      "@id": "http://www.opengis.net/cis/1.1/resolution",
      "@type": "xsd:string"
    },
    "maxDate": {
      "@id": "https://w3id.org/iliad/oim/metadata/maxDate",
      "@type": "xsd:dateTimeStamp"
    },
    "constraint": {
      "@id": "http://www.opengis.net/swe/2.0/constraint",
      "@type": "@id"
    },
    "ConnectorEndpoint": "https://w3id.org/idsa/core/ConnectorEndpoint",
    "DataStructureDefinition": "http://purl.org/linked-data/cube#DataStructureDefinition",
    "numberOfRecords": {
      "@id": "https://w3id.org/iliad/oim/metadata/numberOfRecords",
      "@type": "xsd:integer"
    },
    "RegularAxisType": "http://www.opengis.net/cis/1.1/RegularAxisType",
    "PhotonFluxDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#PhotonFluxDensity",
    "implements": {
      "@id": "http://www.w3.org/ns/ssn/implements",
      "@type": "@id"
    },
    "invalidatedAtTime": {
      "@id": "http://www.w3.org/ns/prov#invalidatedAtTime",
      "@type": "xsd:dateTime"
    },
    "MultiLineString": "http://www.opengis.net/ont/sf#MultiLineString",
    "Attachable": "http://purl.org/linked-data/cube#Attachable",
    "QuantityValue": "http://qudt.org/schema/qudt/QuantityValue",
    "Line": "http://www.opengis.net/ont/sf#Line",
    "generatedAtTime": {
      "@id": "http://www.w3.org/ns/prov#generatedAtTime",
      "@type": "xsd:dateTime"
    },
    "example": "skos:example",
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
    "Deployment": "http://www.w3.org/ns/ssn/Deployment",
    "MultiSurface": "http://www.opengis.net/ont/sf#MultiSurface",
    "TemporalDuration": "http://www.w3.org/2006/time#TemporalDuration",
    "Procedure": "http://www.w3.org/ns/sosa/Procedure",
    "DiffusionCoefficient": "http://purl.oclc.org/NET/ssnx/qu/dim#DiffusionCoefficient",
    "asGeoJSON": {
      "@id": "http://www.opengis.net/ont/geosparql#asGeoJSON",
      "@type": "http://www.opengis.net/ont/geosparql#geoJSONLiteral"
    },
    "Volume": "http://purl.oclc.org/NET/ssnx/qu/dim#Volume",
    "Thing": "owl:Thing",
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
    "Class": "rdfs:Class",
    "ObservationCollection": "http://www.w3.org/ns/sosa/ObservationCollection",
    "NumberPerArea": "http://purl.oclc.org/NET/ssnx/qu/dim#NumberPerArea",
    "depiction": "http://xmlns.com/foaf/0.1/depiction",
    "Curve": "http://www.opengis.net/ont/sf#Curve",
    "Instant": "http://www.w3.org/2006/time#Instant",
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
    "LineString": "http://www.opengis.net/ont/sf#LineString",
    "numericValue": "http://qudt.org/schema/qudt/numericValue",
    "attribute": {
      "@id": "http://purl.org/linked-data/cube#attribute",
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
      "@type": "xsd:decimal"
    },
    "ElectricConductivity": "http://purl.oclc.org/NET/ssnx/qu/dim#ElectricConductivity",
    "Temperature": "http://purl.oclc.org/NET/ssnx/qu/dim#Temperature",
    "hasProperty": {
      "@id": "http://www.w3.org/ns/ssn/hasProperty",
      "@type": "@id"
    },
    "Measure": "http://def.seegrid.csiro.au/isotc211/iso19103/2005/basic#Measure",
    "Triangle": "http://www.opengis.net/ont/sf#Triangle",
    "observationGroup": {
      "@id": "http://purl.org/linked-data/cube#observationGroup",
      "@type": "@id"
    },
    "Interval": "http://www.w3.org/2006/time#Interval",
    "EnergyFlux": "http://purl.oclc.org/NET/ssnx/qu/dim#EnergyFlux",
    "StressOrPressure": "http://purl.oclc.org/NET/ssnx/qu/dim#StressOrPressure",
    "resultTime": {
      "@id": "http://www.w3.org/ns/sosa/resultTime",
      "@type": "xsd:dateTime"
    },
    "VolumeDensityRate": "http://purl.oclc.org/NET/ssnx/qu/dim#VolumeDensityRate",
    "phenomenonTime": {
      "@id": "http://www.w3.org/ns/sosa/phenomenonTime",
      "@type": "@id"
    },
    "Energy": "http://purl.oclc.org/NET/ssnx/qu/dim#Energy",
    "foaf.name": "http://xmlns.com/foaf/0.1/name",
    "Role": "https://schema.org/Role",
    "hasSerialization": {
      "@id": "http://www.opengis.net/ont/geosparql#hasSerialization",
      "@type": "rdfs:Literal"
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
    "Scheme": "skos:Scheme",
    "hasEnd": {
      "@id": "http://www.w3.org/2006/time#hasEnd",
      "@type": "@id"
    },
    "GeometryCollection": "http://www.opengis.net/ont/sf#GeometryCollection",
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
    "hasSubSystem": {
      "@id": "http://www.w3.org/ns/ssn/hasSubSystem",
      "@type": "@id"
    },
    "Quantity": "http://qudt.org/schema/qudt/Quantity",
    "MassFlowRate": "http://purl.oclc.org/NET/ssnx/qu/dim#MassFlowRate",
    "qu.QuantityKind": "http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind",
    "SpatialObjectCollection": "http://www.opengis.net/ont/geosparql#SpatialObjectCollection",
    "Distance": "http://purl.oclc.org/NET/ssnx/qu/dim#Distance",
    "Radiance": "http://purl.oclc.org/NET/ssnx/qu/dim#Radiance",
    "Duration": "http://purl.oclc.org/NET/ssnx/qu/dim#Duration",
    "TIN": "http://www.opengis.net/ont/sf#TIN",
    "SurfaceDensity": "http://purl.oclc.org/NET/ssnx/qu/dim#SurfaceDensity",
    "wgs84.Point": "http://www.w3.org/2003/01/geo/wgs84_pos#Point",
    "editorialNote": "skos:editorialNote",
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
      "@id": "http://rs.tdwg.org/dwc/terms/order",
      "@type": "xsd:int"
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
    "Density": "http://purl.oclc.org/NET/ssnx/qu/dim#Density",
    "LinearRing": "http://www.opengis.net/ont/sf#LinearRing",
    "Molality": "http://purl.oclc.org/NET/ssnx/qu/dim#Molality",
    "inXSDDateTimeStamp": {
      "@id": "http://www.w3.org/2006/time#inXSDDateTimeStamp",
      "@type": "xsd:dateTimeStamp"
    },
    "PropertyKind": "http://purl.oclc.org/NET/ssnx/qu/qu#PropertyKind",
    "SpatialObject": "http://www.opengis.net/ont/geosparql#SpatialObject",
    "sliceStructure": {
      "@id": "http://purl.org/linked-data/cube#sliceStructure",
      "@type": "@id"
    },
    "hasFeatureOfInterest": {
      "@id": "https://saref.etsi.org/core/hasFeatureOfInterest",
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
    "madeObservation": {
      "@id": "http://www.w3.org/ns/sosa/madeObservation",
      "@type": "@id"
    },
    "FeatureCollection": "http://www.opengis.net/ont/geosparql#FeatureCollection",
    "isPropertyOf": {
      "@id": "https://saref.etsi.org/core/isPropertyOf",
      "@type": "@id"
    },
    "ObservationGroup": "http://purl.org/linked-data/cube#ObservationGroup",
    "Sample": "http://www.w3.org/ns/sosa/Sample",
    "DataSet": "http://purl.org/linked-data/cube#DataSet",
    "PolyhedralSurface": "http://www.opengis.net/ont/sf#PolyhedralSurface",
    "ObservableProperty": "http://www.w3.org/ns/sosa/ObservableProperty",
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
      "@type": "xsd:date"
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
    "Surface": "http://purl.oclc.org/NET/ssnx/cf/cf-feature#Surface",
    "sliceKey": {
      "@id": "http://purl.org/linked-data/cube#sliceKey",
      "@type": "@id"
    },
    "dct.description": "dct:description",
    "MultiCurve": "http://www.opengis.net/ont/sf#MultiCurve",
    "hasQuantityKind": {
      "@id": "http://qudt.org/schema/qudt/hasQuantityKind",
      "@type": "@id"
    },
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
    "schema.name": "https://schema.org/name",
    "QuantityKind": "http://purl.oclc.org/NET/ssnx/qu/qu#QuantityKind",
    "sampleSizeUnit": "http://rs.tdwg.org/dwc/terms/sampleSizeUnit",
    "recordNumber": "http://rs.tdwg.org/dwc/terms/recordNumber",
    "verbatimLongitude": "http://rs.tdwg.org/dwc/terms/verbatimLongitude",
    "behavior": "http://rs.tdwg.org/dwc/terms/behavior",
    "organismQuantity": "http://rs.tdwg.org/dwc/terms/organismQuantity",
    "scientificNameID": "http://rs.tdwg.org/dwc/terms/scientificNameID",
    "lowestBiostratigraphicZone": "http://rs.tdwg.org/dwc/terms/lowestBiostratigraphicZone",
    "earliestEonOrLowestEonothem": "http://rs.tdwg.org/dwc/terms/earliestEonOrLowestEonothem",
    "originalNameUsageID": "http://rs.tdwg.org/dwc/terms/originalNameUsageID",
    "GeologicalContext": "http://rs.tdwg.org/dwc/terms/GeologicalContext",
    "countryCode": "http://rs.tdwg.org/dwc/terms/countryCode",
    "UnitOfMeasure": "https://saref.etsi.org/core/UnitOfMeasure",
    "verbatimCoordinates": "http://rs.tdwg.org/dwc/terms/verbatimCoordinates",
    "recordType": "http://mmisw.org/ont/ioos/marine_biogeography/recordType",
    "maximumDistanceAboveSurfaceInMeters": "http://rs.tdwg.org/dwc/terms/maximumDistanceAboveSurfaceInMeters",
    "verbatimLocality": "http://rs.tdwg.org/dwc/terms/verbatimLocality",
    "identificationReferences": "http://rs.tdwg.org/dwc/terms/identificationReferences",
    "isControlledByDevice": {
      "@id": "https://saref.etsi.org/core/isControlledByDevice",
      "@type": "@id"
    },
    "verbatimCoordinateSystem": "http://rs.tdwg.org/dwc/terms/verbatimCoordinateSystem",
    "sampleLengthInMeters": "http://mmisw.org/ont/ioos/marine_biogeography/sampleLengthInMeters",
    "measurementType": "http://rs.tdwg.org/dwc/terms/measurementType",
    "sampleWidthInMeters": "http://mmisw.org/ont/ioos/marine_biogeography/sampleWidthInMeters",
    "measurementAccuracy": "http://rs.tdwg.org/dwc/terms/measurementAccuracy",
    "genus": "http://rs.tdwg.org/dwc/terms/genus",
    "coordinatePrecision": "http://rs.tdwg.org/dwc/terms/coordinatePrecision",
    "weightInKg": "http://mmisw.org/ont/ioos/marine_biogeography/weightInKg",
    "georeferencedDate": "http://rs.tdwg.org/dwc/terms/georeferencedDate",
    "taxonomicStatus": "http://rs.tdwg.org/dwc/terms/taxonomicStatus",
    "validFrom": {
      "@id": "http://portele.de/ont/inspire/baseInspire#validFrom",
      "@type": "xsd:dateTime"
    },
    "SurfaceMediumMedium": "http://purl.oclc.org/NET/ssnx/cf/cf-feature#SurfaceMediumMedium",
    "Humidity": "https://saref.etsi.org/core/Humidity",
    "previousIdentifications": "http://rs.tdwg.org/dwc/terms/previousIdentifications",
    "Period": "http://def.seegrid.csiro.au/isotc211/iso19108/2002/temporal#Period",
    "startDayOfYear": "http://rs.tdwg.org/dwc/terms/startDayOfYear",
    "otherCatalogNumbers": "http://rs.tdwg.org/dwc/terms/otherCatalogNumbers",
    "MachineObservation": "http://rs.tdwg.org/dwc/terms/MachineObservation",
    "coordinateUncertaintyInMeters": "http://rs.tdwg.org/dwc/terms/coordinateUncertaintyInMeters",
    "eventID": "http://rs.tdwg.org/dwc/terms/eventID",
    "Organism": "http://rs.tdwg.org/dwc/terms/Organism",
    "identificationID": "http://rs.tdwg.org/dwc/terms/identificationID",
    "recordedByID": "http://rs.tdwg.org/dwc/terms/recordedByID",
    "dateCreated": {
      "@id": "https://smartdatamodels.org/dateCreated",
      "@type": "xsd:dateTime"
    },
    "Identification": "http://rs.tdwg.org/dwc/terms/Identification",
    "WeatherObserved": "https://smartdatamodels.org/dataModel.Weather/WeatherObserved",
    "quantificationUnit": "http://mmisw.org/ont/ioos/marine_biogeography/quantificationUnit",
    "country": "http://rs.tdwg.org/dwc/terms/country",
    "genericName": "http://rs.tdwg.org/dwc/terms/genericName",
    "bibliographicCitation": "dct:bibliographicCitation",
    "decimalLongitude": "http://rs.tdwg.org/dwc/terms/decimalLongitude",
    "scientificName": "http://rs.tdwg.org/dwc/terms/scientificName",
    "organismQuantityType": "http://rs.tdwg.org/dwc/terms/organismQuantityType",
    "catalogNumber": "http://rs.tdwg.org/dwc/terms/catalogNumber",
    "continent": "http://rs.tdwg.org/dwc/terms/continent",
    "minimumDistanceAboveSurfaceInMeters": "http://rs.tdwg.org/dwc/terms/minimumDistanceAboveSurfaceInMeters",
    "dateModified": {
      "@id": "https://smartdatamodels.org/dateModified",
      "@type": "xsd:dateTime"
    },
    "decimalLatitude": "http://rs.tdwg.org/dwc/terms/decimalLatitude",
    "references": "dct:references",
    "agroVocConcept": {
      "@id": "https://smartdatamodels.org/dataModel.Agrifood/agroVocConcept",
      "@type": "@id"
    },
    "higherGeographyID": "http://rs.tdwg.org/dwc/terms/higherGeographyID",
    "addressRegion": "https://schema.org/addressRegion",
    "measurementDeterminedBy": "http://rs.tdwg.org/dwc/terms/measurementDeterminedBy",
    "sampleShape": "http://mmisw.org/ont/ioos/marine_biogeography/sampleShape",
    "geodeticDatum": "http://rs.tdwg.org/dwc/terms/geodeticDatum",
    "verbatimSiteDescriptions": "http://rs.tdwg.org/hc/terms/verbatimSiteDescriptions",
    "dataProvider": "https://smartdatamodels.org/dataProvider",
    "maximumDepthInMeters": "http://rs.tdwg.org/dwc/terms/maximumDepthInMeters",
    "measuresProperty": {
      "@id": "https://saref.etsi.org/core/measuresProperty",
      "@type": "@id"
    },
    "locationAccordingTo": "http://rs.tdwg.org/dwc/terms/locationAccordingTo",
    "nameAccordingTo": "http://rs.tdwg.org/dwc/terms/nameAccordingTo",
    "group": "http://rs.tdwg.org/dwc/terms/group",
    "class": "http://rs.tdwg.org/dwc/terms/class",
    "footprintWKT": "http://rs.tdwg.org/dwc/terms/footprintWKT",
    "FossilSpecimen": "http://rs.tdwg.org/dwc/terms/FossilSpecimen",
    "snowHeight": "https://smartdatamodels.org/dataModel.Weather/snowHeight",
    "Medium": "http://purl.oclc.org/NET/ssnx/cf/cf-feature#Medium",
    "typeStatus": "http://rs.tdwg.org/dwc/terms/typeStatus",
    "acceptedNameUsage": "http://rs.tdwg.org/dwc/terms/acceptedNameUsage",
    "earliestEpochOrLowestSeries": "http://rs.tdwg.org/dwc/terms/earliestEpochOrLowestSeries",
    "streamGauge": "https://smartdatamodels.org/dataModel.Weather/streamGauge",
    "parentNameUsageID": "http://rs.tdwg.org/dwc/terms/parentNameUsageID",
    "dynamicProperties": "http://rs.tdwg.org/dwc/terms/dynamicProperties",
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
    "identificationVerificationStatus": "http://rs.tdwg.org/dwc/terms/identificationVerificationStatus",
    "Measurement": "https://saref.etsi.org/core/Measurement",
    "footprintSRS": "http://rs.tdwg.org/dwc/terms/footprintSRS",
    "individualCount": "http://rs.tdwg.org/dwc/terms/individualCount",
    "collectionCode": "http://rs.tdwg.org/dwc/terms/collectionCode",
    "lithostratigraphicTerms": "http://rs.tdwg.org/dwc/terms/lithostratigraphicTerms",
    "subfamily": "http://rs.tdwg.org/dwc/terms/subfamily",
    "eventType": "http://rs.tdwg.org/dwc/terms/eventType",
    "associatedMedia": "http://rs.tdwg.org/dwc/terms/associatedMedia",
    "Taxon": "http://rs.tdwg.org/dwc/terms/Taxon",
    "vernacularName": "http://rs.tdwg.org/dwc/terms/vernacularName",
    "windDirection": "https://smartdatamodels.org/dataModel.Weather/windDirection",
    "preparations": "http://rs.tdwg.org/dwc/terms/preparations",
    "Event": "http://rs.tdwg.org/dwc/terms/Event",
    "observationLocation": "http://mmisw.org/ont/ioos/marine_biogeography/observationLocation",
    "institutionID": "http://rs.tdwg.org/dwc/terms/institutionID",
    "WeatherForecast": "https://smartdatamodels.org/dataModel.Weather/WeatherForecast",
    "verbatimDepth": "http://rs.tdwg.org/dwc/terms/verbatimDepth",
    "county": "http://rs.tdwg.org/dwc/terms/county",
    "measurementMadeBy": {
      "@id": "https://saref.etsi.org/core/measurementMadeBy",
      "@type": "@id"
    },
    "earliestEraOrLowestErathem": "http://rs.tdwg.org/dwc/terms/earliestEraOrLowestErathem",
    "occurrenceStatus": "http://rs.tdwg.org/dwc/terms/occurrenceStatus",
    "LocationRelationship": "https://uri.etsi.org/ngsi-ld/LocationRelationship",
    "observedMinLengthInCm": "http://mmisw.org/ont/ioos/marine_biogeography/observedMinLengthInCm",
    "verbatimTaxonRank": "http://rs.tdwg.org/dwc/terms/verbatimTaxonRank",
    "disposition": "http://rs.tdwg.org/dwc/terms/disposition",
    "visibility": "https://smartdatamodels.org/dataModel.Weather/visibility",
    "namePublishedInID": "http://rs.tdwg.org/dwc/terms/namePublishedInID",
    "dateIdentified": "http://rs.tdwg.org/dwc/terms/dateIdentified",
    "ImageObject": "https://schema.org/ImageObject",
    "organismRemarks": "http://rs.tdwg.org/dwc/terms/organismRemarks",
    "latestPeriodOrHighestSystem": "http://rs.tdwg.org/dwc/terms/latestPeriodOrHighestSystem",
    "Precipitation": "http://purl.oclc.org/NET/ssnx/cf/cf-feature#Precipitation",
    "taxonRemarks": "http://rs.tdwg.org/dwc/terms/taxonRemarks",
    "georeferencedBy": "http://rs.tdwg.org/dwc/terms/georeferencedBy",
    "verbatimElevation": "http://rs.tdwg.org/dwc/terms/verbatimElevation",
    "higherClassification": "http://rs.tdwg.org/dwc/terms/higherClassification",
    "waterBody": "http://rs.tdwg.org/dwc/terms/waterBody",
    "Layer": "http://purl.oclc.org/NET/ssnx/cf/cf-feature#Layer",
    "GeoProperty": "https://uri.etsi.org/ngsi-ld/GeoProperty",
    "namePublishedIn": "http://rs.tdwg.org/dwc/terms/namePublishedIn",
    "organismID": "http://rs.tdwg.org/dwc/terms/organismID",
    "stateProvince": "http://rs.tdwg.org/dwc/terms/stateProvince",
    "endDayOfYear": "http://rs.tdwg.org/dwc/terms/endDayOfYear",
    "geologicalContextID": "http://rs.tdwg.org/dwc/terms/geologicalContextID",
    "pathway": "http://rs.tdwg.org/dwc/terms/pathway",
    "verbatimSiteNames": "http://rs.tdwg.org/hc/terms/verbatimSiteNames",
    "parentEventID": "http://rs.tdwg.org/dwc/terms/parentEventID",
    "datasetName": "http://rs.tdwg.org/dwc/terms/datasetName",
    "temperature": "https://smartdatamodels.org/dataModel.Weather/temperature",
    "measurementMethod": "http://rs.tdwg.org/dwc/terms/measurementMethod",
    "verbatimLatitude": "http://rs.tdwg.org/dwc/terms/verbatimLatitude",
    "parentMeasurementID": "http://rs.tdwg.org/dwc/terms/parentMeasurementID",
    "sightingCue": "http://mmisw.org/ont/ioos/marine_biogeography/sightingCue",
    "waterTemperatureInCelsius": "http://mmisw.org/ont/ioos/marine_biogeography/waterTemperatureInCelsius",
    "tribe": "http://rs.tdwg.org/dwc/terms/tribe",
    "status": "https://schema.org/status",
    "superfamily": "http://rs.tdwg.org/dwc/terms/superfamily",
    "sampleSizeValue": "http://rs.tdwg.org/dwc/terms/sampleSizeValue",
    "LivingSpecimen": "http://rs.tdwg.org/dwc/terms/LivingSpecimen",
    "visibilityType": "http://mmisw.org/ont/ioos/marine_biogeography/visibilityType",
    "locationRemarks": "http://rs.tdwg.org/dwc/terms/locationRemarks",
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
    "institutionCode": "http://rs.tdwg.org/dwc/terms/institutionCode",
    "isMeasuredByDevice": {
      "@id": "https://saref.etsi.org/core/isMeasuredByDevice",
      "@type": "@id"
    },
    "occurrenceID": "http://rs.tdwg.org/dwc/terms/occurrenceID",
    "quantificationMethod": "http://mmisw.org/ont/ioos/marine_biogeography/quantificationMethod",
    "measurementUnit": "http://rs.tdwg.org/dwc/terms/measurementUnit",
    "lengthType": "http://mmisw.org/ont/ioos/marine_biogeography/lengthType",
    "HumanObservation": "http://rs.tdwg.org/dwc/terms/HumanObservation",
    "associatedSequences": "http://rs.tdwg.org/dwc/terms/associatedSequences",
    "phylum": "http://rs.tdwg.org/dwc/terms/phylum",
    "fieldNumber": "http://rs.tdwg.org/dwc/terms/fieldNumber",
    "relationshipRemarks": "http://rs.tdwg.org/dwc/terms/relationshipRemarks",
    "infragenericEpithet": "http://rs.tdwg.org/dwc/terms/infragenericEpithet",
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
    "bed": "http://rs.tdwg.org/dwc/terms/bed",
    "locality": "http://rs.tdwg.org/dwc/terms/locality",
    "MaterialCitation": "http://rs.tdwg.org/dwc/terms/MaterialCitation",
    "samplingPerformedBy": "http://rs.tdwg.org/hc/terms/samplingPerformedBy",
    "makesMeasurement": {
      "@id": "https://saref.etsi.org/core/makesMeasurement",
      "@type": "@id"
    },
    "associatedTaxa": "http://rs.tdwg.org/dwc/terms/associatedTaxa",
    "measurementDeterminedDate": "http://rs.tdwg.org/dwc/terms/measurementDeterminedDate",
    "eventDurationUnit": "http://rs.tdwg.org/hc/terms/eventDurationUnit",
    "vitality": "http://rs.tdwg.org/dwc/terms/vitality",
    "minimumDepthInMeters": "http://rs.tdwg.org/dwc/terms/minimumDepthInMeters",
    "samplingEffort": "http://rs.tdwg.org/dwc/terms/samplingEffort",
    "pressureTendency": "https://smartdatamodels.org/dataModel.Weather/pressureTendency",
    "streetAddress": "https://schema.org/streetAddress",
    "eventDate": "http://rs.tdwg.org/dwc/terms/eventDate",
    "validTo": {
      "@id": "http://portele.de/ont/inspire/baseInspire#validTo",
      "@type": "xsd:dateTime"
    },
    "Occurrence": "http://rs.tdwg.org/dwc/terms/Occurrence",
    "year": "http://rs.tdwg.org/dwc/terms/year",
    "family": "http://rs.tdwg.org/dwc/terms/family",
    "eppoConcept": {
      "@id": "https://w3id.org/demeter/agri/agriCommon#eppoConcept",
      "@type": "@id"
    },
    "georeferenceSources": "http://rs.tdwg.org/dwc/terms/georeferenceSources",
    "resourceType": "dct:type",
    "weatherType": "https://smartdatamodels.org/dataModel.Weather/weatherType",
    "MaterialSample": "http://rs.tdwg.org/dwc/terms/MaterialSample",
    "isMeasuredIn": {
      "@id": "https://saref.etsi.org/core/isMeasuredIn",
      "@type": "@id"
    },
    "island": "http://rs.tdwg.org/dwc/terms/island",
    "dewPoint": "https://smartdatamodels.org/dataModel.Weather/dewPoint",
    "sightingDistanceInMeters": "http://mmisw.org/ont/ioos/marine_biogeography/sightingDistanceInMeters",
    "taxonRank": "http://rs.tdwg.org/dwc/terms/taxonRank",
    "locationID": "http://rs.tdwg.org/dwc/terms/locationID",
    "TemporalProperty": "https://uri.etsi.org/ngsi-ld/TemporalProperty",
    "identificationRemarks": "http://rs.tdwg.org/dwc/terms/identificationRemarks",
    "eventDuration": "http://rs.tdwg.org/hc/terms/eventDuration",
    "associatedOrganisms": "http://rs.tdwg.org/dwc/terms/associatedOrganisms",
    "sampleAreaInSquareMeters": "http://mmisw.org/ont/ioos/marine_biogeography/sampleAreaInSquareMeters",
    "password": {
      "@id": "https://w3id.org/demeter/agri/agriCommon#password",
      "@type": "xsd:string"
    },
    "subgenus": "http://rs.tdwg.org/dwc/terms/subgenus",
    "observedMaxLengthInCm": "http://mmisw.org/ont/ioos/marine_biogeography/observedMaxLengthInCm",
    "aphiaID": "http://mmisw.org/ont/ioos/marine_biogeography/aphiaID",
    "relationshipOfResourceID": "http://rs.tdwg.org/dwc/terms/relationshipOfResourceID",
    "siteCount": "http://rs.tdwg.org/hc/terms/siteCount",
    "solarRadiation": "https://smartdatamodels.org/dataModel.Weather/solarRadiation",
    "SurfaceMedium": "http://purl.oclc.org/NET/ssnx/cf/cf-feature#SurfaceMedium",
    "sampleHeightInMeters": "http://mmisw.org/ont/ioos/marine_biogeography/sampleHeightInMeters",
    "earliestAgeOrLowestStage": "http://rs.tdwg.org/dwc/terms/earliestAgeOrLowestStage",
    "relativeHumidity": "https://smartdatamodels.org/dataModel.Weather/relativeHumidity",
    "kingdom": "http://rs.tdwg.org/dwc/terms/kingdom",
    "totalInSample": "http://mmisw.org/ont/ioos/marine_biogeography/totalInSample",
    "latestEonOrHighestEonothem": "http://rs.tdwg.org/dwc/terms/latestEonOrHighestEonothem",
    "taxonConceptID": "http://rs.tdwg.org/dwc/terms/taxonConceptID",
    "islandGroup": "http://rs.tdwg.org/dwc/terms/islandGroup",
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
    "addressLocality": "https://schema.org/addressLocality",
    "municipality": "http://rs.tdwg.org/dwc/terms/municipality",
    "reportedWeather": "http://rs.tdwg.org/hc/terms/reportedWeather",
    "airTemperatureForecast": "https://smartdatamodels.org/dataModel.Weather/airTemperatureForecast",
    "nomenclaturalStatus": "http://rs.tdwg.org/dwc/terms/nomenclaturalStatus",
    "observedIndividualLengthInCm": "http://mmisw.org/ont/ioos/marine_biogeography/observedIndividualLengthInCm",
    "samplingProtocol": "http://rs.tdwg.org/dwc/terms/samplingProtocol",
    "earliestPeriodOrLowestSystem": "http://rs.tdwg.org/dwc/terms/earliestPeriodOrLowestSystem",
    "lifeStage": "http://rs.tdwg.org/dwc/terms/lifeStage",
    "basisOfRecord": "http://rs.tdwg.org/dwc/terms/basisOfRecord",
    "day": "http://rs.tdwg.org/dwc/terms/day",
    "controlsProperty": {
      "@id": "https://saref.etsi.org/core/controlsProperty",
      "@type": "@id"
    },
    "verticalDatum": "http://rs.tdwg.org/dwc/terms/verticalDatum",
    "latestEpochOrHighestSeries": "http://rs.tdwg.org/dwc/terms/latestEpochOrHighestSeries",
    "originalNameUsage": "http://rs.tdwg.org/dwc/terms/originalNameUsage",
    "cultivarEpithet": "http://rs.tdwg.org/dwc/terms/cultivarEpithet",
    "identifiedByID": "http://rs.tdwg.org/dwc/terms/identifiedByID",
    "reproductiveCondition": "http://rs.tdwg.org/dwc/terms/reproductiveCondition",
    "latestEraOrHighestErathem": "http://rs.tdwg.org/dwc/terms/latestEraOrHighestErathem",
    "datasetID": "http://rs.tdwg.org/dwc/terms/datasetID",
    "scientificNameAuthorship": "http://rs.tdwg.org/dwc/terms/scientificNameAuthorship",
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
    "MeasurementOrFact": "http://rs.tdwg.org/dwc/terms/MeasurementOrFact",
    "hasTimestamp": "https://saref.etsi.org/core/hasTimestamp",
    "identificationQualifier": "http://rs.tdwg.org/dwc/terms/identificationQualifier",
    "infraspecificEpithet": "http://rs.tdwg.org/dwc/terms/infraspecificEpithet",
    "precipitation": "https://smartdatamodels.org/dataModel.Weather/precipitation",
    "latestAgeOrHighestStage": "http://rs.tdwg.org/dwc/terms/latestAgeOrHighestStage",
    "alternateName": "https://smartdatamodels.org/alternateName",
    "addressCountry": "https://schema.org/addressCountry",
    "dataGeneralizations": "http://rs.tdwg.org/dwc/terms/dataGeneralizations",
    "SurfaceLayer": "http://purl.oclc.org/NET/ssnx/cf/cf-feature#SurfaceLayer",
    "ResourceRelationship": "http://rs.tdwg.org/dwc/terms/ResourceRelationship",
    "eventTime": "http://rs.tdwg.org/dwc/terms/eventTime",
    "verbatimIdentification": "http://rs.tdwg.org/dwc/terms/verbatimIdentification",
    "PeriodOfTime": "dct:PeriodOfTime",
    "PreservedSpecimen": "http://rs.tdwg.org/dwc/terms/PreservedSpecimen",
    "associatedReferences": "http://rs.tdwg.org/dwc/terms/associatedReferences",
    "recordedBy": "http://rs.tdwg.org/dwc/terms/recordedBy",
    "specificEpithet": "http://rs.tdwg.org/dwc/terms/specificEpithet",
    "formation": "http://rs.tdwg.org/dwc/terms/formation",
    "nomenclaturalCode": "http://rs.tdwg.org/dwc/terms/nomenclaturalCode",
    "ResponsibleParty": "http://def.seegrid.csiro.au/isotc211/iso19115/2003/citation#ResponsibleParty",
    "observedMeanLengthInCm": "http://mmisw.org/ont/ioos/marine_biogeography/observedMeanLengthInCm",
    "ownerInstitutionCode": "http://rs.tdwg.org/dwc/terms/ownerInstitutionCode",
    "relatedResourceID": "http://rs.tdwg.org/dwc/terms/relatedResourceID",
    "windSpeed": "https://smartdatamodels.org/dataModel.Weather/windSpeed",
    "measurementValue": "http://rs.tdwg.org/dwc/terms/measurementValue",
    "occurrenceRemarks": "http://rs.tdwg.org/dwc/terms/occurrenceRemarks",
    "measurementRemarks": "http://rs.tdwg.org/dwc/terms/measurementRemarks",
    "illuminance": "https://smartdatamodels.org/dataModel.Weather/illuminance",
    "georeferenceRemarks": "http://rs.tdwg.org/dwc/terms/georeferenceRemarks",
    "organismScope": "http://rs.tdwg.org/dwc/terms/organismScope",
    "resourceID": "http://rs.tdwg.org/dwc/terms/resourceID",
    "associatedOccurrences": "http://rs.tdwg.org/dwc/terms/associatedOccurrences",
    "relationshipAccordingTo": "http://rs.tdwg.org/dwc/terms/relationshipAccordingTo",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dct": "http://purl.org/dc/terms/",
    "qudt": "http://qudt.org/schema/qudt#",
    "covjson": "https://covjson.org/def/core#",
    "ignf": "http://data.ign.fr/def/ignf#",
    "inspiregloss": "http://inspire.ec.europa.eu/glossary/",
    "ssn": "http://www.w3.org/2005/Incubator/ssn/ssnx/ssn#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "hydra": "http://www.w3.org/ns/hydra/core#",
    "covjsondt": "https://covjson.org/def/domainTypes#",
    "rel": "http://www.iana.org/assignments/relation/",
    "owl": "http://www.w3.org/2002/07/owl#",
    "dce": "http://purl.org/dc/elements/1.1/",
    "ns0": "http://www.w3.org/ns/dx/conneg/altr#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "iop": "https://w3id.org/iadopt/ont#",
    "ns1": "http://www.w3.org/ns/dx/prof/",
    "puv": "https://w3id.org/env/puv#",
    "semapv": "http://w3id.org/semapv/vocab/",
    "reg": "http://purl.org/linked-data/registry#",
    "dcat": "http://www.w3.org/ns/dcat#",
    "grg": "http://www.isotc211.org/schemas/grg/",
    "prov": "https://www.w3.org/ns/prov#",
    "cpm": "http://purl.org/voc/cpm#",
    "void": "http://rdfs.org/ns/void#",
    "pav": "http://purl.org/pav/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "sssom": "https://w3id.org/sssom/schema/",
    "dc": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_sdn/context.jsonld)

## Sources

* [Zarr spcification](https://zarr.readthedocs.io/en/v2.1.2/spec/v2.html#arrays)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/iliad-apis-features](https://github.com/ogcincubator/iliad-apis-features)
* Path: `_sources/zarr_attrs_sdn`

