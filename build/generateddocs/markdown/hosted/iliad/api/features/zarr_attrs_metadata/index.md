
# GeoZarr Attributes description metadata (Schema)

`ogc.hosted.iliad.api.features.zarr_attrs_metadata` *v0.1*

based on the https://zarr.readthedocs.io/en/v2.1.2/spec/v2.html, tooling support constraints and Iliad requiremnts

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## OGC Coverage JSON


long_name:
    type: string
  standard_name:
    type: string
  units:
    type: string
    enum:
    - degrees_north
    - degreesN
  _ARRAY_DIMENSIONS:
    type: array
    items:
      type: string
  "Conventions":
    "type": "string"
  "units_metadata":
    "type": "string"
  "cell_methods":
    "type": "string"
  "created_by":
    "type": "string"
  "date":
    "type": "string"
  "crs_wkt":
    "type": "string"
  "geotransform":
    "type": "string"
  "proj4": 
    "type": "string"
  "spatial_ref": 
    "type": "string"
## Examples

### Zarr v2 attributes metadata for CRS
#### json
```json
{
            "_ARRAY_DIMENSIONS": [],
            "crs_wkt": "GEOGCRS[\"WGS 84\",    ENSEMBLE[\"World Geodetic System 1984 ensemble\",        MEMBER[\"World Geodetic System 1984 (Transit)\"],        MEMBER[\"World Geodetic System 1984 (G730)\"],        MEMBER[\"World Geodetic System 1984 (G873)\"],        MEMBER[\"World Geodetic System 1984 (G1150)\"],        MEMBER[\"World Geodetic System 1984 (G1674)\"],        MEMBER[\"World Geodetic System 1984 (G1762)\"],        MEMBER[\"World Geodetic System 1984 (G2139)\"],        ELLIPSOID[\"WGS 84\",6378137,298.257223563,            LENGTHUNIT[\"metre\",1]],        ENSEMBLEACCURACY[2.0]],    PRIMEM[\"Greenwich\",0,        ANGLEUNIT[\"degree\",0.0174532925199433]],    CS[ellipsoidal,2],        AXIS[\"geodetic latitude (Lat)\",north,            ORDER[1],            ANGLEUNIT[\"degree\",0.0174532925199433]],        AXIS[\"geodetic longitude (Lon)\",east,            ORDER[2],            ANGLEUNIT[\"degree\",0.0174532925199433]],    USAGE[        SCOPE[\"Horizontal component of 3D system.\"],        AREA[\"World.\"],        BBOX[-90,-180,90,180]],    ID[\"EPSG\",4326]]",
            "epsg_code": "4326",
            "geotransform": "-15.01856792000000062615 0.03703666616296295843735 0 61.30106364000000240821 0 -0.02222333317851959630373",
            "proj4": "+proj=longlat +datum=WGS84 +no_defs",
            "spatial_ref": "GEOGCRS[\"WGS 84\",    ENSEMBLE[\"World Geodetic System 1984 ensemble\",        MEMBER[\"World Geodetic System 1984 (Transit)\"],        MEMBER[\"World Geodetic System 1984 (G730)\"],        MEMBER[\"World Geodetic System 1984 (G873)\"],        MEMBER[\"World Geodetic System 1984 (G1150)\"],        MEMBER[\"World Geodetic System 1984 (G1674)\"],        MEMBER[\"World Geodetic System 1984 (G1762)\"],        MEMBER[\"World Geodetic System 1984 (G2139)\"],        ELLIPSOID[\"WGS 84\",6378137,298.257223563,            LENGTHUNIT[\"metre\",1]],        ENSEMBLEACCURACY[2.0]],    PRIMEM[\"Greenwich\",0,        ANGLEUNIT[\"degree\",0.0174532925199433]],    CS[ellipsoidal,2],        AXIS[\"geodetic latitude (Lat)\",north,            ORDER[1],            ANGLEUNIT[\"degree\",0.0174532925199433]],        AXIS[\"geodetic longitude (Lon)\",east,            ORDER[2],            ANGLEUNIT[\"degree\",0.0174532925199433]],    USAGE[        SCOPE[\"Horizontal component of 3D system.\"],        AREA[\"World.\"],        BBOX[-90,-180,90,180]],    ID[\"EPSG\",4326]]"
        }
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_metadata/context.jsonld",
  "_ARRAY_DIMENSIONS": [],
  "crs_wkt": "GEOGCRS[\"WGS 84\",    ENSEMBLE[\"World Geodetic System 1984 ensemble\",        MEMBER[\"World Geodetic System 1984 (Transit)\"],        MEMBER[\"World Geodetic System 1984 (G730)\"],        MEMBER[\"World Geodetic System 1984 (G873)\"],        MEMBER[\"World Geodetic System 1984 (G1150)\"],        MEMBER[\"World Geodetic System 1984 (G1674)\"],        MEMBER[\"World Geodetic System 1984 (G1762)\"],        MEMBER[\"World Geodetic System 1984 (G2139)\"],        ELLIPSOID[\"WGS 84\",6378137,298.257223563,            LENGTHUNIT[\"metre\",1]],        ENSEMBLEACCURACY[2.0]],    PRIMEM[\"Greenwich\",0,        ANGLEUNIT[\"degree\",0.0174532925199433]],    CS[ellipsoidal,2],        AXIS[\"geodetic latitude (Lat)\",north,            ORDER[1],            ANGLEUNIT[\"degree\",0.0174532925199433]],        AXIS[\"geodetic longitude (Lon)\",east,            ORDER[2],            ANGLEUNIT[\"degree\",0.0174532925199433]],    USAGE[        SCOPE[\"Horizontal component of 3D system.\"],        AREA[\"World.\"],        BBOX[-90,-180,90,180]],    ID[\"EPSG\",4326]]",
  "epsg_code": "4326",
  "geotransform": "-15.01856792000000062615 0.03703666616296295843735 0 61.30106364000000240821 0 -0.02222333317851959630373",
  "proj4": "+proj=longlat +datum=WGS84 +no_defs",
  "spatial_ref": "GEOGCRS[\"WGS 84\",    ENSEMBLE[\"World Geodetic System 1984 ensemble\",        MEMBER[\"World Geodetic System 1984 (Transit)\"],        MEMBER[\"World Geodetic System 1984 (G730)\"],        MEMBER[\"World Geodetic System 1984 (G873)\"],        MEMBER[\"World Geodetic System 1984 (G1150)\"],        MEMBER[\"World Geodetic System 1984 (G1674)\"],        MEMBER[\"World Geodetic System 1984 (G1762)\"],        MEMBER[\"World Geodetic System 1984 (G2139)\"],        ELLIPSOID[\"WGS 84\",6378137,298.257223563,            LENGTHUNIT[\"metre\",1]],        ENSEMBLEACCURACY[2.0]],    PRIMEM[\"Greenwich\",0,        ANGLEUNIT[\"degree\",0.0174532925199433]],    CS[ellipsoidal,2],        AXIS[\"geodetic latitude (Lat)\",north,            ORDER[1],            ANGLEUNIT[\"degree\",0.0174532925199433]],        AXIS[\"geodetic longitude (Lon)\",east,            ORDER[2],            ANGLEUNIT[\"degree\",0.0174532925199433]],    USAGE[        SCOPE[\"Horizontal component of 3D system.\"],        AREA[\"World.\"],        BBOX[-90,-180,90,180]],    ID[\"EPSG\",4326]]"
}
```

#### ttl
```ttl


```


### Zarr v2 attributes metadata for latitude
#### json
```json
{
            "_ARRAY_DIMENSIONS": [
                "latitude"
            ],
            "long_name": "latitude",
            "units": "degrees_north",
            "standard_name": "latitude"
        }
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_metadata/context.jsonld",
  "_ARRAY_DIMENSIONS": [
    "latitude"
  ],
  "long_name": "latitude",
  "units": "degrees_north",
  "standard_name": "latitude"
}
```

#### ttl
```ttl


```


### Zarr v2 attributes metadata for longitude
#### json
```json
{
            "_ARRAY_DIMENSIONS": [
                "longitude"
            ],
            "long_name": "longitude",
            "units": "degrees_east"
        }
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_metadata/context.jsonld",
  "_ARRAY_DIMENSIONS": [
    "longitude"
  ],
  "long_name": "longitude",
  "units": "degrees_east"
}
```

#### ttl
```ttl


```


### Zarr v2 attributes metadata for root
#### json
```json
{
            "Conventions": "CF-1.4",
            "created_by": "R packages ncdf4 and terra (version 1.7-71)",
            "date": "2024-04-18 15:50:45"
        }
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_metadata/context.jsonld",
  "Conventions": "CF-1.4",
  "created_by": "R packages ncdf4 and terra (version 1.7-71)",
  "date": "2024-04-18 15:50:45"
}
```

#### ttl
```ttl


```


### Zarr v2 attributes metadata for time
#### json
```json
{
            "_ARRAY_DIMENSIONS": [
                "time"
            ],
            "calendar": "standard",
            "long_name": "time",
            "units": "seconds since 1970-01-01"
        }
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_metadata/context.jsonld",
  "_ARRAY_DIMENSIONS": [
    "time"
  ],
  "calendar": "standard",
  "long_name": "time",
  "units": "seconds since 1970-01-01"
}
```

#### ttl
```ttl
@prefix covjson: <https://covjson.org/def/core#> .

[] covjson:calendar [ ] .


```


### Zarr v2 attributes metadata for variable like temperature
#### json
```json
{
    "standard_name": "surface_temperature",
    "long_name": "global-mean surface temperature",
    "units_metadata": "temperature: on_scale",
    "cell_methods": "area: mean",
    "units": "degC"
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_metadata/context.jsonld",
  "standard_name": "surface_temperature",
  "long_name": "global-mean surface temperature",
  "units_metadata": "temperature: on_scale",
  "cell_methods": "area: mean",
  "units": "degC"
}
```

#### ttl
```ttl


```


### Zarr v2 attributes metadata for variable
#### json
```json
{
  "_ARRAY_DIMENSIONS": [
      "time",
      "latitude",
      "longitude"
  ],
  "grid_mapping": "crs",
  "long_name": "Suitability of good catch (>200 kg) for Pleuronectes platessa",
  "units": "percent"
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_metadata/context.jsonld",
  "_ARRAY_DIMENSIONS": [
    "time",
    "latitude",
    "longitude"
  ],
  "grid_mapping": "crs",
  "long_name": "Suitability of good catch (>200 kg) for Pleuronectes platessa",
  "units": "percent"
}
```

#### ttl
```ttl


```


### Zarr v2 group metadata
#### json
```json
{
    "zarr_format": 2
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_metadata/context.jsonld",
  "zarr_format": 2
}
```

#### ttl
```ttl


```

## Schema

```yaml
$schema: http://json-schema.org/draft-07/schema#
title: Zarr Attributes Metadata
type: object
properties:
  long_name:
    type: string
    x-jsonld-id: _:_:long_name
  standard_name:
    type: string
    x-jsonld-id: _:_:standard_name
  units:
    type: string
    enum:
    - degrees_north
    - degreesN
    x-jsonld-id: _:_:units
  _ARRAY_DIMENSIONS:
    type: array
    items:
      type: string
    x-jsonld-id: _:_:_ARRAY_DIMENSIONS
  Conventions:
    type: string
    x-jsonld-id: _:_:Conventions
  units_metadata:
    type: string
    x-jsonld-id: _:_:units_metadata
  cell_methods:
    type: string
    x-jsonld-id: _:_:cell_methods
  created_by:
    type: string
    x-jsonld-id: _:_:created_by
  date:
    type: string
    x-jsonld-id: _:_:date
  crs_wkt:
    type: string
    x-jsonld-id: _:_:crs_wkt
  geotransform:
    type: string
    x-jsonld-id: _:_:geotransform
  proj4:
    type: string
    x-jsonld-id: _:_:proj4
  spatial_ref:
    type: string
    x-jsonld-id: _:_:spatial_ref
x-jsonld-extra-terms:
  id: '@id'
  type: '@type'
  value: '@value'
  label:
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
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
    x-jsonld-id: https://covjson.org/def/core#dataType
    x-jsonld-type: '@vocab'
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
x-jsonld-vocab: '_:_:'
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

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_metadata/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_metadata/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "_:_:",
    "long_name": "_:_:long_name",
    "standard_name": "_:_:standard_name",
    "units": "_:_:units",
    "_ARRAY_DIMENSIONS": "_:_:_ARRAY_DIMENSIONS",
    "Conventions": "_:_:Conventions",
    "units_metadata": "_:_:units_metadata",
    "cell_methods": "_:_:cell_methods",
    "created_by": "_:_:created_by",
    "date": "_:_:date",
    "crs_wkt": "_:_:crs_wkt",
    "geotransform": "_:_:geotransform",
    "proj4": "_:_:proj4",
    "spatial_ref": "_:_:spatial_ref",
    "id": "@id",
    "type": "@type",
    "value": "@value",
    "label": {
      "@id": "skos:prefLabel",
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
      "@id": "covjson:dataType",
      "@type": "@vocab"
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
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_attrs_metadata/context.jsonld)

## Sources

* [Zarr spcification](https://zarr.readthedocs.io/en/v2.1.2/spec/v2.html#arrays)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/iliad-apis-features](https://github.com/ogcincubator/iliad-apis-features)
* Path: `_sources/zarr_attrs_metadata`

