
# OGC Coverage Implementation Schema (Schema)

`ogc.hosted.iliad.api.features.coverage_information_model` *v0.1*

Coverages represent homogeneous collections of values located in space/time, such as spatio-temporal sensor, image, simulation, and statistics data. Common examples include 1-D timeseries, 2-D imagery, 3-D x/y/t image timeseries and x/y/z geophysical voxel models, as well as 4-D x/y/z/t climate and ocean data. Generally, coverages encompass multi-dimen­sional regular and irregular grids, point clouds, and general meshes. This Coverage Implementation Schema (CIS) specifies the OGC coverage model by establishing a concrete, interoperable, conformance-testable coverage structure. It is based on the abstract concepts of OGC Abstract Topic 6 [1] (which is identical to ISO 19123) which spec­i­fies an abstract model which is not per se interoperable – in other words, many different and incompatible implementations of the abstract model are possible. CIS, on the other hand, is interoperable in the sense that coverages can be conformance tested, regardless of their data format encoding, down to the level of single pixels or voxels.Coverages can be encoded in any suitable format (such as GML, JSON, GeoTIFF, or Net­CDF) and can be partitioned, e.g., for a time-interleaved representation. Coverages are independent from service definitions and, therefore, can be accessed through a variety of OGC services types, such as the Web Coverage Service (WCS) Standard [8]. The coverage structure can serve a wide range of coverage application domains, thereby contributing to harmon­ization and interoperability between and across these domains.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## OGC Coverage Implementation Schema

Coverages represent homogeneous collections of values located in space/time, such as spatio-temporal sensor, image, simulation, and statistics data. Common examples include 1-D timeseries, 2-D imagery, 3-D x/y/t image timeseries and x/y/z geophysical voxel models, as well as 4-D x/y/z/t climate and ocean data. Generally, coverages encompass multi-dimen­sional regular and irregular grids, point clouds, and general meshes.

This Coverage Implementation Schema (CIS) specifies the OGC coverage model by establishing a concrete, interoperable, conformance-testable coverage structure. It is based on the abstract concepts of OGC Abstract Topic 6 [1] (which is identical to ISO 19123) which spec­i­fies an abstract model which is not per se interoperable – in other words, many different and incompatible implementations of the abstract model are possible. CIS, on the other hand, is interoperable in the sense that coverages can be conformance tested, regardless of their data format encoding, down to the level of single “pixels” or “voxels.”

Coverages can be encoded in any suitable format (such as GML, JSON, GeoTIFF, or Net­CDF) and can be partitioned, e.g., for a time-interleaved representation. Coverages are independent from service definitions and, therefore, can be accessed through a variety of OGC services types, such as the Web Coverage Service (WCS) Standard [8]. The coverage structure can serve a wide range of coverage application domains, thereby contributing to harmon­ization and interoperability between and across these domains.

## Key features of this profile:

- a schema for the coverage, domainset, rangeset and rangetype
- a JSON-LD context for this result schema

## Examples

### JSON encoded coverage from https://docs.ogc.org/is/09-146r6/09-146r6.html
#### json
```json
{
  "type": "CoverageByDomainAndRangeType",
  "domainSet": {
    "type": "DomainSetType",
    "generalGrid": {
      "type": "GeneralGridCoverageType",
      "srsName": "http://www.opengis.net/def/crs/OGC/0/Index2D",
      "axisLabels": [
        "i",
        "j"
      ],
      "axis": [
        {
          "type": "IndexAxisType",
          "axisLabel": "i",
          "lowerBound": 0,
          "upperBound": 2
        },
        {
          "type": "IndexAxisType",
          "axisLabel": "j",
          "lowerBound": 0,
          "upperBound": 2
        }
      ]
    }
  },
  "rangeSet": {
    "type": "RangeSetType",
    "dataBlock": {
      "type": "VDataBlockType",
      "values": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9
      ]
    }
  },
  "rangeType": {
    "type": "DataRecordType",
    "field": [
      {
        "type": "QuantityType",
        "definition": "ogcType:unsignedInt",
        "uom": {
          "type": "UnitReference",
          "code": "10^0"
        }
      }
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverage_information_model/context.jsonld",
  "type": "CoverageByDomainAndRangeType",
  "domainSet": {
    "type": "DomainSetType",
    "generalGrid": {
      "type": "GeneralGridCoverageType",
      "srsName": "http://www.opengis.net/def/crs/OGC/0/Index2D",
      "axisLabels": [
        "i",
        "j"
      ],
      "axis": [
        {
          "type": "IndexAxisType",
          "axisLabel": "i",
          "lowerBound": 0,
          "upperBound": 2
        },
        {
          "type": "IndexAxisType",
          "axisLabel": "j",
          "lowerBound": 0,
          "upperBound": 2
        }
      ]
    }
  },
  "rangeSet": {
    "type": "RangeSetType",
    "dataBlock": {
      "type": "VDataBlockType",
      "values": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9
      ]
    }
  },
  "rangeType": {
    "type": "DataRecordType",
    "field": [
      {
        "type": "QuantityType",
        "definition": "ogcType:unsignedInt",
        "uom": {
          "type": "UnitReference",
          "code": "10^0"
        }
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix cis: <http://www.opengis.net/cis/1.1/> .
@prefix ogcType: <http://www.opengis.net/def/dataType/OGC/0/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix swe: <http://www.opengis.net/swe/2.0/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a cis:CoverageByDomainAndRangeType ;
    cis:domainSet [ a cis:DomainSetType ;
            cis:generalGrid [ a cis:GeneralGridCoverageType ;
                    cis:axis [ a cis:IndexAxisType ;
                            cis:axisLabel "j" ;
                            cis:lowerBound 0 ;
                            cis:upperBound 2 ],
                        [ a cis:IndexAxisType ;
                            cis:axisLabel "i" ;
                            cis:lowerBound 0 ;
                            cis:upperBound 2 ] ;
                    cis:axisLabels ( "i" "j" ) ;
                    cis:srsName <http://www.opengis.net/def/crs/OGC/0/Index2D> ] ] ;
    cis:rangeSet [ a cis:RangeSetType ;
            cis:dataBlock [ a cis:VDataBlockType ] ] ;
    cis:rangeType [ a swe:DataRecordType ;
            swe:field [ a swe:QuantityType ;
                    swe:definition ogcType:unsignedInt ;
                    swe:uom [ a swe:UnitReference ;
                            swe:code "10^0" ] ] ] .


```


### JSON with Ids encoded coverage from https://docs.ogc.org/is/09-146r6/09-146r6.html
#### json
```json
{
  "type": "CoverageByDomainAndRangeType",
  "domainSet": {
    "type": "DomainSetType",
    "generalGrid": {
      "type": "GeneralGridCoverageType",
      "srsName": "http://www.opengis.net/def/crs/OGC/0/Index2D",
      "axisLabels": [
        "i",
        "j"
      ],
      "axis": [
        {
          "type": "IndexAxisType",
          "axisLabel": "i",
          "lowerBound": 0,
          "upperBound": 2
        },
        {
          "type": "IndexAxisType",
          "axisLabel": "j",
          "lowerBound": 0,
          "upperBound": 2
        }
      ]
    }
  },
  "rangeSet": {
    "type": "RangeSetType",
    "dataBlock": {
      "type": "VDataBlockType",
      "values": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9
      ]
    }
  },
  "rangeType": {
    "type": "DataRecordType",
    "field": [
      {
        "type": "QuantityType",
        "definition": "ogcType:unsignedInt",
        "uom": {
          "type": "UnitReference",
          "code": "10^0"
        }
      }
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverage_information_model/context.jsonld",
  "type": "CoverageByDomainAndRangeType",
  "domainSet": {
    "type": "DomainSetType",
    "generalGrid": {
      "type": "GeneralGridCoverageType",
      "srsName": "http://www.opengis.net/def/crs/OGC/0/Index2D",
      "axisLabels": [
        "i",
        "j"
      ],
      "axis": [
        {
          "type": "IndexAxisType",
          "axisLabel": "i",
          "lowerBound": 0,
          "upperBound": 2
        },
        {
          "type": "IndexAxisType",
          "axisLabel": "j",
          "lowerBound": 0,
          "upperBound": 2
        }
      ]
    }
  },
  "rangeSet": {
    "type": "RangeSetType",
    "dataBlock": {
      "type": "VDataBlockType",
      "values": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9
      ]
    }
  },
  "rangeType": {
    "type": "DataRecordType",
    "field": [
      {
        "type": "QuantityType",
        "definition": "ogcType:unsignedInt",
        "uom": {
          "type": "UnitReference",
          "code": "10^0"
        }
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix cis: <http://www.opengis.net/cis/1.1/> .
@prefix ogcType: <http://www.opengis.net/def/dataType/OGC/0/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix swe: <http://www.opengis.net/swe/2.0/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a cis:CoverageByDomainAndRangeType ;
    cis:domainSet [ a cis:DomainSetType ;
            cis:generalGrid [ a cis:GeneralGridCoverageType ;
                    cis:axis [ a cis:IndexAxisType ;
                            cis:axisLabel "i" ;
                            cis:lowerBound 0 ;
                            cis:upperBound 2 ],
                        [ a cis:IndexAxisType ;
                            cis:axisLabel "j" ;
                            cis:lowerBound 0 ;
                            cis:upperBound 2 ] ;
                    cis:axisLabels ( "i" "j" ) ;
                    cis:srsName <http://www.opengis.net/def/crs/OGC/0/Index2D> ] ] ;
    cis:rangeSet [ a cis:RangeSetType ;
            cis:dataBlock [ a cis:VDataBlockType ] ] ;
    cis:rangeType [ a swe:DataRecordType ;
            swe:field [ a swe:QuantityType ;
                    swe:definition ogcType:unsignedInt ;
                    swe:uom [ a swe:UnitReference ;
                            swe:code "10^0" ] ] ] .


```


### RDF encoded coverage from https://docs.ogc.org/is/09-146r6/09-146r6.html
#### ttl
```ttl
<examples:CIS_05_2D> <http://www.opengis.net/cis/1.1/domainSet> <examples:CIS_DS_05_2D> .
<examples:CIS_05_2D> <http://www.opengis.net/cis/1.1/rangeSet> <examples:CIS_RS_05_2D> .
<examples:CIS_05_2D> <http://www.opengis.net/cis/1.1/rangeType> <examples:CIS_RT_05_2D> .
<examples:CIS_05_2D> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.opengis.net/cis/1.1/CoverageByDomainAndRangeType> .
<examples:CIS_DS_05_2D> <http://www.opengis.net/cis/1.1/generalGrid> <examples:CIS_DS_GG_05_2D> .
<examples:CIS_DS_05_2D> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.opengis.net/cis/1.1/DomainSetType> .
<examples:CIS_DS_GG_05_2D> <http://www.opengis.net/cis/1.1/axis> <examples:CIS_DS_GG_I_05_2D> .
<examples:CIS_DS_GG_05_2D> <http://www.opengis.net/cis/1.1/axis> <examples:CIS_DS_GG_J_05_2D> .
<examples:CIS_DS_GG_05_2D> <http://www.opengis.net/cis/1.1/axisLabels> _:b1 .
<examples:CIS_DS_GG_05_2D> <http://www.opengis.net/cis/1.1/srsName> <http://www.opengis.net/def/crs/OGC/0/Index2D> .
<examples:CIS_DS_GG_05_2D> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.opengis.net/cis/1.1/GeneralGridCoverageType> .
<examples:CIS_DS_GG_I_05_2D> <http://www.opengis.net/cis/1.1/axisLabel> "i" .
<examples:CIS_DS_GG_I_05_2D> <http://www.opengis.net/cis/1.1/lowerBound> "0"^^<http://www.w3.org/2001/XMLSchema#integer> .
<examples:CIS_DS_GG_I_05_2D> <http://www.opengis.net/cis/1.1/upperBound> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
<examples:CIS_DS_GG_I_05_2D> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.opengis.net/cis/1.1/IndexAxisType> .
<examples:CIS_DS_GG_J_05_2D> <http://www.opengis.net/cis/1.1/axisLabel> "j" .
<examples:CIS_DS_GG_J_05_2D> <http://www.opengis.net/cis/1.1/lowerBound> "0"^^<http://www.w3.org/2001/XMLSchema#integer> .
<examples:CIS_DS_GG_J_05_2D> <http://www.opengis.net/cis/1.1/upperBound> "2"^^<http://www.w3.org/2001/XMLSchema#integer> .
<examples:CIS_DS_GG_J_05_2D> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.opengis.net/cis/1.1/IndexAxisType> .
<examples:CIS_RS_05_2D> <http://www.opengis.net/cis/1.1/dataBlock> _:b0 .
<examples:CIS_RS_05_2D> <http://www.opengis.net/cis/1.1/fileReference> <http://myserver.com/fileref.tiff> .
<examples:CIS_RS_05_2D> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.opengis.net/cis/1.1/RangeSetType> .
<examples:CIS_RT_05_2D> <http://www.opengis.net/swe/2.0/field> <examples:CIS_RT_F_05_2D> .
<examples:CIS_RT_05_2D> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.opengis.net/swe/2.0/DataRecordType> .
<examples:CIS_RT_F_05_2D> <http://www.opengis.net/swe/2.0/definition> <http://www.opengis.net/def/dataType/OGC/0/unsignedInt> .
<examples:CIS_RT_F_05_2D> <http://www.opengis.net/swe/2.0/uom> <examples:CIS_RT_F_UOM_05_2D> .
<examples:CIS_RT_F_05_2D> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.opengis.net/swe/2.0/QuantityType> .
<examples:CIS_RT_F_UOM_05_2D> <http://www.opengis.net/swe/2.0/code> "10^0" .
<examples:CIS_RT_F_UOM_05_2D> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.opengis.net/swe/2.0/UnitReference> .
_:b0 <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.opengis.net/cis/1.1/VDataBlockType> .
_:b1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#first> "i" .
_:b1 <http://www.w3.org/1999/02/22-rdf-syntax-ns#rest> _:b2 .
_:b2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#first> "j" .
_:b2 <http://www.w3.org/1999/02/22-rdf-syntax-ns#rest> <http://www.w3.org/1999/02/22-rdf-syntax-ns#nil> .

```

## Schema

```yaml
$schema: http://json-schema.org/draft-04/schema#
title: Coverage object
description: 'Component of OGC Coverage Implementation Schema 1.1. Last updated: 2016-may-18.
  Copyright (c) 2016 Open Geospatial Consortium, Inc. All Rights Reserved. To obtain
  additional rights of use, visit http://www.opengeospatial.org/legal/.'
$ref: https://schemas.opengis.net/cis/1.1/json/coverage-schema.json
x-jsonld-extra-terms:
  id: '@id'
  type: '@type'
  CoverageByDomainAndRangeType: http://www.opengis.net/cis/1.1/CoverageByDomainAndRangeType
  CoverageByPartitioningType: http://www.opengis.net/cis/1.1/CoverageByPartitioningType
  envelope: http://www.opengis.net/cis/1.1/envelope
  domainSet: http://www.opengis.net/cis/1.1/domainSet
  rangeSet: http://www.opengis.net/cis/1.1/rangeSet
  partitionSet: http://www.opengis.net/cis/1.1/partitionSet
  rangeType: http://www.opengis.net/cis/1.1/rangeType
  metadata: http://www.opengis.net/cis/1.1/metadata
  DomainSetType: http://www.opengis.net/cis/1.1/DomainSetType
  GeneralGridCoverageType: http://www.opengis.net/cis/1.1/GeneralGridCoverageType
  generalGrid: http://www.opengis.net/cis/1.1/generalGrid
  srsName:
    x-jsonld-id: http://www.opengis.net/cis/1.1/srsName
    x-jsonld-type: '@id'
  axisLabel: http://www.opengis.net/cis/1.1/axisLabel
  axisLabels:
    x-jsonld-id: http://www.opengis.net/cis/1.1/axisLabels
    x-jsonld-container: '@list'
  uomLabel: http://www.opengis.net/cis/1.1/uomLabel
  uomLabels:
    x-jsonld-id: http://www.opengis.net/cis/1.1/uomLabels
    x-jsonld-container: '@list'
  axis: http://www.opengis.net/cis/1.1/axis
  IndexAxisType: http://www.opengis.net/cis/1.1/IndexAxisType
  RegularAxisType: http://www.opengis.net/cis/1.1/RegularAxisType
  IrregularAxisType: http://www.opengis.net/cis/1.1/IrregularAxisType
  DisplacementAxisNestType: http://www.opengis.net/cis/1.1/DisplacementAxisNestType
  lowerBound: http://www.opengis.net/cis/1.1/lowerBound
  upperBound: http://www.opengis.net/cis/1.1/upperBound
  resolution: http://www.opengis.net/cis/1.1/resolution
  GridLimitsType: http://www.opengis.net/cis/1.1/GridLimitsType
  gridLimits: http://www.opengis.net/cis/1.1/gridLimits
  coordinate: http://www.opengis.net/cis/1.1/coordinate
  displacement: http://www.opengis.net/cis/1.1/displacement
  model: http://www.opengis.net/cis/1.1/model
  TransformationBySensorModelType: http://www.opengis.net/cis/1.1/TransformationBySensorModelType
  sensorModelRef: http://www.sensorml.com/sensorML-2.0/sensorModelRef
  sensorInstanceRef: http://www.sensorml.com/sensorML-2.0/sensorInstanceRef
  EnvelopeByAxisType: http://www.opengis.net/cis/1.1/EnvelopeByAxisType
  AxisExtendType: http://www.opengis.net/cis/1.1/AxisExtendType
  PartitionSetType: http://www.opengis.net/cis/1.1/PartitionSetType
  partition: http://www.opengis.net/cis/1.1/partition
  coverage: http://www.opengis.net/cis/1.1/coverage
  coverageRef:
    x-jsonld-id: http://www.opengis.net/cis/1.1/coverageRef
    x-jsonld-type: '@id'
  positionValuePair: http://www.opengis.net/cis/1.1/positionValuePair
  PVPType: http://www.opengis.net/cis/1.1/PVPType
  value: http://www.opengis.net/cis/1.1/value
  RangeSetType: http://www.opengis.net/cis/1.1/RangeSetType
  RangeSetRefType: http://www.opengis.net/cis/1.1/RangeSetRefType
  dataBlock: http://www.opengis.net/cis/1.1/dataBlock
  VDataBlockType: http://www.opengis.net/cis/1.1/VDataBlockType
  fileReference:
    x-jsonld-id: http://www.opengis.net/cis/1.1/fileReference
    x-jsonld-type: '@id'
  DataRecordType: http://www.opengis.net/swe/2.0/DataRecordType
  field: http://www.opengis.net/swe/2.0/field
  names:
    x-jsonld-id: http://www.opengis.net/swe/2.0/names
    x-jsonld-container: '@list'
  name: http://www.opengis.net/swe/2.0/name
  QuantityType: http://www.opengis.net/swe/2.0/QuantityType
  uom: http://www.opengis.net/swe/2.0/uom
  code: http://www.opengis.net/swe/2.0/code
  UnitReference: http://www.opengis.net/swe/2.0/UnitReference
  definition:
    x-jsonld-id: http://www.opengis.net/swe/2.0/definition
    x-jsonld-type: '@id'
  interpolationRestriction: http://www.opengis.net/cis/1.1/interpolationRestriction
  allowedInterpolation:
    x-jsonld-id: http://www.opengis.net/cis/1.1/allowedInterpolation
    x-jsonld-type: '@id'
  constraint: http://www.opengis.net/swe/2.0/constraint
  AllowedValues: http://www.opengis.net/swe/2.0/AllowedValues
  interval: http://www.opengis.net/swe/2.0/interval
x-jsonld-prefixes:
  cis: http://www.opengis.net/cis/1.1/
  sml: http://www.sensorml.com/sensorML-2.0/
  swe: http://www.opengis.net/swe/2.0/
  ogcType: http://www.opengis.net/def/dataType/OGC/0/
  ogcInterpolation: http://www.opengis.net/def/interpolation/OGC/0/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverage_information_model/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverage_information_model/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "id": "@id",
    "type": "@type",
    "CoverageByDomainAndRangeType": "cis:CoverageByDomainAndRangeType",
    "CoverageByPartitioningType": "cis:CoverageByPartitioningType",
    "envelope": "cis:envelope",
    "domainSet": "cis:domainSet",
    "rangeSet": "cis:rangeSet",
    "partitionSet": "cis:partitionSet",
    "rangeType": "cis:rangeType",
    "metadata": "cis:metadata",
    "DomainSetType": "cis:DomainSetType",
    "GeneralGridCoverageType": "cis:GeneralGridCoverageType",
    "generalGrid": "cis:generalGrid",
    "srsName": {
      "@id": "cis:srsName",
      "@type": "@id"
    },
    "axisLabel": "cis:axisLabel",
    "axisLabels": {
      "@id": "cis:axisLabels",
      "@container": "@list"
    },
    "uomLabel": "cis:uomLabel",
    "uomLabels": {
      "@id": "cis:uomLabels",
      "@container": "@list"
    },
    "axis": "cis:axis",
    "IndexAxisType": "cis:IndexAxisType",
    "RegularAxisType": "cis:RegularAxisType",
    "IrregularAxisType": "cis:IrregularAxisType",
    "DisplacementAxisNestType": "cis:DisplacementAxisNestType",
    "lowerBound": "cis:lowerBound",
    "upperBound": "cis:upperBound",
    "resolution": "cis:resolution",
    "GridLimitsType": "cis:GridLimitsType",
    "gridLimits": "cis:gridLimits",
    "coordinate": "cis:coordinate",
    "displacement": "cis:displacement",
    "model": "cis:model",
    "TransformationBySensorModelType": "cis:TransformationBySensorModelType",
    "sensorModelRef": "sml:sensorModelRef",
    "sensorInstanceRef": "sml:sensorInstanceRef",
    "EnvelopeByAxisType": "cis:EnvelopeByAxisType",
    "AxisExtendType": "cis:AxisExtendType",
    "PartitionSetType": "cis:PartitionSetType",
    "partition": "cis:partition",
    "coverage": "cis:coverage",
    "coverageRef": {
      "@id": "cis:coverageRef",
      "@type": "@id"
    },
    "positionValuePair": "cis:positionValuePair",
    "PVPType": "cis:PVPType",
    "value": "cis:value",
    "RangeSetType": "cis:RangeSetType",
    "RangeSetRefType": "cis:RangeSetRefType",
    "dataBlock": "cis:dataBlock",
    "VDataBlockType": "cis:VDataBlockType",
    "fileReference": {
      "@id": "cis:fileReference",
      "@type": "@id"
    },
    "DataRecordType": "swe:DataRecordType",
    "field": "swe:field",
    "names": {
      "@id": "swe:names",
      "@container": "@list"
    },
    "name": "swe:name",
    "QuantityType": "swe:QuantityType",
    "uom": "swe:uom",
    "code": "swe:code",
    "UnitReference": "swe:UnitReference",
    "definition": {
      "@id": "swe:definition",
      "@type": "@id"
    },
    "interpolationRestriction": "cis:interpolationRestriction",
    "allowedInterpolation": {
      "@id": "cis:allowedInterpolation",
      "@type": "@id"
    },
    "constraint": "swe:constraint",
    "AllowedValues": "swe:AllowedValues",
    "interval": "swe:interval",
    "cis": "http://www.opengis.net/cis/1.1/",
    "sml": "http://www.sensorml.com/sensorML-2.0/",
    "swe": "http://www.opengis.net/swe/2.0/",
    "ogcType": "http://www.opengis.net/def/dataType/OGC/0/",
    "ogcInterpolation": "http://www.opengis.net/def/interpolation/OGC/0/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverage_information_model/context.jsonld)

## Sources

* [Coverage Implementation Schema](https://docs.ogc.org/is/09-146r8/09-146r8.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/iliad-apis-features](https://github.com/ogcincubator/iliad-apis-features)
* Path: `_sources/coverage_information_model`

