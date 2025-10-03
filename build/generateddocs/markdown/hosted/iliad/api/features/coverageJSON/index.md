
# OGC CoverageJSON (Schema)

`ogc.hosted.iliad.api.features.coverageJSON` *v0.1*

Based on JavaScript Object Notation (JSON), CoverageJSON is a format for publishing spatiotemporal data to the Web. The primary design goals are simplicity, machine and human readability and efficiency. While other use cases are possible, the primary CoverageJSON use case is enabling the development of interactive visual websites that display and manipulate environmental data within a web browser.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## OGC Coverage JSON

[OGC CoverageJSON Community Standard ](https://docs.ogc.org/cs/21-069r2/21-069r2.html#_a4083c6e-e633-49c0-9f94-193224cf3ccb)

"Based on JavaScript Object Notation (JSON), CoverageJSON is a format for publishing spatiotemporal data to the Web. The primary design goals are simplicity, machine and human readability and efficiency. While other use cases are possible, the primary CoverageJSON use case is enabling the development of interactive visual websites that display and manipulate environmental data within a web browser.

CoverageJSON can be used to encode coverages and collections of coverages. Coverage data may be gridded or non-gridded, and data values may represent continuous values (such as temperature) or discrete categories (such as land cover classes). CoverageJSON uses JSON-LD to provide interoperability with RDF and Semantic Web applications and to reduce the potential size of the payload.

Relatively large datasets can be handled efficiently in a “web-friendly” way by partitioning information among several CoverageJSON documents, including a tiling mechanism. Nevertheless, CoverageJSON is not intended to be a replacement for efficient binary formats such as NetCDF, HDF or GRIB, and is not intended primarily to store or transfer very large datasets in bulk.""


## Key features of this profile:

- a default schema for the coverage, domainset, rangeset and rangetype
- default JSON-LD context for this result schema

## Examples

### Coverage JSON Collection representing snapshot series of PointClouds with LD
#### json
```json
{
  "@id":"CoverageCollection of Multipoints",
  "type" : "CoverageCollection",
  "domainType" : "MultiPoint",

  "parameters" : {
    "diameter": {
      "@id": "diameter definition",
      "type" : "Parameter",
      "description" : {
      	"en": "particle diameter"
      },
      "unit" : {
        "label": {
          "en": "nanometers"
        },
        "symbol": {
          "value": "nm",
          "type": "http://www.opengis.net/def/uom/UCUM/"
        }
      },
      "observedProperty" : {
        "id" : "https://qudt.org/vocab/unit/NanoM",
        "label" : {
          "en": "0.000000001-fold of the SI base unit metre"
        }
      }
    },
    "particle_class": {
      "type" : "Parameter",
      "observedProperty" : {
        "id": "http://example.com/particletypes",
        "label" : {
          "en": "Particle class"
        },
        "categories": [{
          "id": "http://example.com/particletypes/0",
          "label": {
            "en": "Oil droplet"
          }
        }, {
          "id": "http://example.com/particletypes/1",
          "label": {
            "en": "Microplastic"
          }
        }, {
          "id": "http://example.com/particletypes/2",
          "label": {
            "en": "Codepod"
          }
        }]
      },
      "categoryEncoding": {
        "http://mmisw.org/ont/argo/qualityFlag/_0": 0,
        "http://mmisw.org/ont/argo/qualityFlag/_1": 1,
        "http://mmisw.org/ont/argo/qualityFlag/_4": 2
      }
    }
  },
    "referencing": [{
      "coordinates": ["x","y"],
      "system": {
        "type": "GeographicCRS",
        "id": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
      }
    }, {
      "coordinates": ["z"],
      "system": {
        "type": "VerticalCRS",
        "cs": {
          "csAxes": [{
            "name": {
              "en": "Pressure"
            },
            "direction": "down",
            "unit": {
              "symbol": "Pa"
            }
          }]
        }
      }
    }, {
      "coordinates": ["t"],
      "system": {
        "type": "TemporalRS",
        "calendar": "Gregorian"
      }
    }],

    "domain":{
      "type" : "Domain",
      "axes": {
      "t": { "values": ["2008-01-01T04:00:00Z","2008-01-02T04:00:00Z"] }
      }
    },
  "coverages":[{
    "type" : "Coverage",
  "domain" : {
    "type" : "Domain",
    "axes": {
    "t": { "values": ["2008-01-01T04:00:00Z"] },
    "composite": {
      "dataType": "tuple",
      "coordinates": ["x","y","z"],
      "values": [
        [1, 20, 1],
        [2, 21, 3]
      ]
    }
  }
  },
  "ranges" : {
    "POTM" : {
      "type" : "NdArray",
      "dataType": "float",
      "shape":[2],
      "axisNames": ["composite"],
      "values" : [ 23.8, 23.8 ]
    },
    "particle_class" : {
      "type" : "NdArray",
      "dataType": "integer",
      "shape":[2],
      "axisNames": ["composite"],
      "values" : [ 1, 3 ]
    }
  }
  },
  {
    "type" : "Coverage",
  "domain" : {
    "type" : "Domain",
    "axes": {
    "t": { "values": ["2008-01-02T04:00:00Z"] },
    "composite": {
      "dataType": "tuple",
      "coordinates": ["x","y","z"],
      "values": [
        [1, 20, 1],
        [2, 21, 3]
      ]
    }
  }
  },
  "ranges" : {
    "POTM" : {
      "type" : "NdArray",
      "dataType": "float",
      "shape":[2],
      "axisNames": ["composite"],
      "values" : [ 23.8, 23.8 ]
    },
    "particle_class" : {
      "type" : "NdArray",
      "dataType": "integer",
      "shape":[2],
      "axisNames": ["composite"],
      "values" : [ 1, 2 ]
    }
  }
  }
]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverageJSON/context.jsonld",
  "@id": "CoverageCollection of Multipoints",
  "type": "CoverageCollection",
  "domainType": "MultiPoint",
  "parameters": {
    "diameter": {
      "@id": "diameter definition",
      "type": "Parameter",
      "description": {
        "en": "particle diameter"
      },
      "unit": {
        "label": {
          "en": "nanometers"
        },
        "symbol": {
          "value": "nm",
          "type": "http://www.opengis.net/def/uom/UCUM/"
        }
      },
      "observedProperty": {
        "id": "https://qudt.org/vocab/unit/NanoM",
        "label": {
          "en": "0.000000001-fold of the SI base unit metre"
        }
      }
    },
    "particle_class": {
      "type": "Parameter",
      "observedProperty": {
        "id": "http://example.com/particletypes",
        "label": {
          "en": "Particle class"
        },
        "categories": [
          {
            "id": "http://example.com/particletypes/0",
            "label": {
              "en": "Oil droplet"
            }
          },
          {
            "id": "http://example.com/particletypes/1",
            "label": {
              "en": "Microplastic"
            }
          },
          {
            "id": "http://example.com/particletypes/2",
            "label": {
              "en": "Codepod"
            }
          }
        ]
      },
      "categoryEncoding": {
        "http://mmisw.org/ont/argo/qualityFlag/_0": 0,
        "http://mmisw.org/ont/argo/qualityFlag/_1": 1,
        "http://mmisw.org/ont/argo/qualityFlag/_4": 2
      }
    }
  },
  "referencing": [
    {
      "coordinates": [
        "x",
        "y"
      ],
      "system": {
        "type": "GeographicCRS",
        "id": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
      }
    },
    {
      "coordinates": [
        "z"
      ],
      "system": {
        "type": "VerticalCRS",
        "cs": {
          "csAxes": [
            {
              "name": {
                "en": "Pressure"
              },
              "direction": "down",
              "unit": {
                "symbol": "Pa"
              }
            }
          ]
        }
      }
    },
    {
      "coordinates": [
        "t"
      ],
      "system": {
        "type": "TemporalRS",
        "calendar": "Gregorian"
      }
    }
  ],
  "domain": {
    "type": "Domain",
    "axes": {
      "t": {
        "values": [
          "2008-01-01T04:00:00Z",
          "2008-01-02T04:00:00Z"
        ]
      }
    }
  },
  "coverages": [
    {
      "type": "Coverage",
      "domain": {
        "type": "Domain",
        "axes": {
          "t": {
            "values": [
              "2008-01-01T04:00:00Z"
            ]
          },
          "composite": {
            "dataType": "tuple",
            "coordinates": [
              "x",
              "y",
              "z"
            ],
            "values": [
              [
                1,
                20,
                1
              ],
              [
                2,
                21,
                3
              ]
            ]
          }
        }
      },
      "ranges": {
        "POTM": {
          "type": "NdArray",
          "dataType": "float",
          "shape": [
            2
          ],
          "axisNames": [
            "composite"
          ],
          "values": [
            23.8,
            23.8
          ]
        },
        "particle_class": {
          "type": "NdArray",
          "dataType": "integer",
          "shape": [
            2
          ],
          "axisNames": [
            "composite"
          ],
          "values": [
            1,
            3
          ]
        }
      }
    },
    {
      "type": "Coverage",
      "domain": {
        "type": "Domain",
        "axes": {
          "t": {
            "values": [
              "2008-01-02T04:00:00Z"
            ]
          },
          "composite": {
            "dataType": "tuple",
            "coordinates": [
              "x",
              "y",
              "z"
            ],
            "values": [
              [
                1,
                20,
                1
              ],
              [
                2,
                21,
                3
              ]
            ]
          }
        }
      },
      "ranges": {
        "POTM": {
          "type": "NdArray",
          "dataType": "float",
          "shape": [
            2
          ],
          "axisNames": [
            "composite"
          ],
          "values": [
            23.8,
            23.8
          ]
        },
        "particle_class": {
          "type": "NdArray",
          "dataType": "integer",
          "shape": [
            2
          ],
          "axisNames": [
            "composite"
          ],
          "values": [
            1,
            2
          ]
        }
      }
    }
  ]
}
```

#### ttl
```ttl


```


### Coverage JSON Collection representing collection of PointSeries with LD
#### json
```json
{
  "type" : "CoverageCollection",
  "domainType" : "MultiPoint",

  "parameters" : {
    "diameter": {
      "type" : "Parameter",
      "description" : {
      	"en": "particle diameter"
      },
      "unit" : {
        "label": {
          "en": "nanometers"
        },
        "symbol": {
          "value": "nm",
          "type": "http://www.opengis.net/def/uom/UCUM/"
        }
      },
      "observedProperty" : {
        "id" : "https://qudt.org/vocab/unit/NanoM",
        "label" : {
          "en": "0.000000001-fold of the SI base unit metre"
        }
      }
    },
    "particle_class": {
      "type" : "Parameter",
      "observedProperty" : {
        "id": "http://example.com/particletypes",
        "label" : {
          "en": "Particle class"
        },
        "categories": [{
          "id": "http://example.com/particletypes/0",
          "label": {
            "en": "Oil droplet"
          }
        }, {
          "id": "http://example.com/particletypes/1",
          "label": {
            "en": "Microplastic"
          }
        }, {
          "id": "http://example.com/particletypes/2",
          "label": {
            "en": "Codepod"
          }
        }]
      },
      "categoryEncoding": {
        "http://mmisw.org/ont/argo/qualityFlag/_0": 0,
        "http://mmisw.org/ont/argo/qualityFlag/_1": 1,
        "http://mmisw.org/ont/argo/qualityFlag/_4": 2
      }
    }
  },
    "referencing": [{
      "coordinates": ["x","y"],
      "system": {
        "type": "GeographicCRS",
        "id": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
      }
    }, {
      "coordinates": ["z"],
      "system": {
        "type": "VerticalCRS",
        "cs": {
          "csAxes": [{
            "name": {
              "en": "Pressure"
            },
            "direction": "down",
            "unit": {
              "symbol": "Pa"
            }
          }]
        }
      }
    }, {
      "coordinates": ["t"],
      "system": {
        "type": "TemporalRS",
        "calendar": "Gregorian"
      }
    }],

    "domain":{
      "type" : "Domain",
      "axes": {
      "t": { "values": ["2008-01-01T04:00:00Z","2008-01-02T04:00:00Z"] }
      }
    },
  "coverages":[{
    "type" : "Coverage",
  "domain" : {
    "type" : "Domain",
    "axes": {
    "t": { "values": ["2008-01-01T04:00:00Z"] },
    "composite": {
      "dataType": "tuple",
      "coordinates": ["x","y","z"],
      "values": [
        [1, 20, 1],
        [2, 21, 3]
      ]
    }
  }
  },
  "ranges" : {
    "POTM" : {"@id":"POTM_range",
      "type" : "NdArray",
      "dataType": "float",
      "shape":[2],
      "axisNames": ["composite"],
      "values" : [ 23.8, 23.8 ]
    },
    "particle_class" : {
      "type" : "NdArray",
      "dataType": "integer",
      "shape":[2],
      "axisNames": ["composite"],
      "values" : [ 1, 3 ]
    }
  }
  },
  {
    "type" : "Coverage",
  "domain" : {
    "type" : "Domain",
    "axes": {
    "t": { "values": ["2008-01-02T04:00:00Z"] },
    "composite": {
      "dataType": "tuple",
      "coordinates": ["x","y","z"],
      "values": [
        [1, 20, 1],
        [2, 21, 3]
      ]
    }
  }
  },
  "ranges" : {
    "POTM" : {
      "type" : "NdArray",
      "dataType": "float",
      "shape":[2],
      "axisNames": ["composite"],
      "values" : [ 23.8, 23.8 ]
    },
    "particle_class" : {
      "type" : "NdArray",
      "dataType": "integer",
      "shape":[2],
      "axisNames": ["composite"],
      "values" : [ 1, 2 ]
    }
  }
  }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverageJSON/context.jsonld",
  "type": "CoverageCollection",
  "domainType": "MultiPoint",
  "parameters": {
    "diameter": {
      "type": "Parameter",
      "description": {
        "en": "particle diameter"
      },
      "unit": {
        "label": {
          "en": "nanometers"
        },
        "symbol": {
          "value": "nm",
          "type": "http://www.opengis.net/def/uom/UCUM/"
        }
      },
      "observedProperty": {
        "id": "https://qudt.org/vocab/unit/NanoM",
        "label": {
          "en": "0.000000001-fold of the SI base unit metre"
        }
      }
    },
    "particle_class": {
      "type": "Parameter",
      "observedProperty": {
        "id": "http://example.com/particletypes",
        "label": {
          "en": "Particle class"
        },
        "categories": [
          {
            "id": "http://example.com/particletypes/0",
            "label": {
              "en": "Oil droplet"
            }
          },
          {
            "id": "http://example.com/particletypes/1",
            "label": {
              "en": "Microplastic"
            }
          },
          {
            "id": "http://example.com/particletypes/2",
            "label": {
              "en": "Codepod"
            }
          }
        ]
      },
      "categoryEncoding": {
        "http://mmisw.org/ont/argo/qualityFlag/_0": 0,
        "http://mmisw.org/ont/argo/qualityFlag/_1": 1,
        "http://mmisw.org/ont/argo/qualityFlag/_4": 2
      }
    }
  },
  "referencing": [
    {
      "coordinates": [
        "x",
        "y"
      ],
      "system": {
        "type": "GeographicCRS",
        "id": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
      }
    },
    {
      "coordinates": [
        "z"
      ],
      "system": {
        "type": "VerticalCRS",
        "cs": {
          "csAxes": [
            {
              "name": {
                "en": "Pressure"
              },
              "direction": "down",
              "unit": {
                "symbol": "Pa"
              }
            }
          ]
        }
      }
    },
    {
      "coordinates": [
        "t"
      ],
      "system": {
        "type": "TemporalRS",
        "calendar": "Gregorian"
      }
    }
  ],
  "domain": {
    "type": "Domain",
    "axes": {
      "t": {
        "values": [
          "2008-01-01T04:00:00Z",
          "2008-01-02T04:00:00Z"
        ]
      }
    }
  },
  "coverages": [
    {
      "type": "Coverage",
      "domain": {
        "type": "Domain",
        "axes": {
          "t": {
            "values": [
              "2008-01-01T04:00:00Z"
            ]
          },
          "composite": {
            "dataType": "tuple",
            "coordinates": [
              "x",
              "y",
              "z"
            ],
            "values": [
              [
                1,
                20,
                1
              ],
              [
                2,
                21,
                3
              ]
            ]
          }
        }
      },
      "ranges": {
        "POTM": {
          "@id": "POTM_range",
          "type": "NdArray",
          "dataType": "float",
          "shape": [
            2
          ],
          "axisNames": [
            "composite"
          ],
          "values": [
            23.8,
            23.8
          ]
        },
        "particle_class": {
          "type": "NdArray",
          "dataType": "integer",
          "shape": [
            2
          ],
          "axisNames": [
            "composite"
          ],
          "values": [
            1,
            3
          ]
        }
      }
    },
    {
      "type": "Coverage",
      "domain": {
        "type": "Domain",
        "axes": {
          "t": {
            "values": [
              "2008-01-02T04:00:00Z"
            ]
          },
          "composite": {
            "dataType": "tuple",
            "coordinates": [
              "x",
              "y",
              "z"
            ],
            "values": [
              [
                1,
                20,
                1
              ],
              [
                2,
                21,
                3
              ]
            ]
          }
        }
      },
      "ranges": {
        "POTM": {
          "type": "NdArray",
          "dataType": "float",
          "shape": [
            2
          ],
          "axisNames": [
            "composite"
          ],
          "values": [
            23.8,
            23.8
          ]
        },
        "particle_class": {
          "type": "NdArray",
          "dataType": "integer",
          "shape": [
            2
          ],
          "axisNames": [
            "composite"
          ],
          "values": [
            1,
            2
          ]
        }
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix covjson: <https://covjson.org/def/core#> .
@prefix covjsondt: <https://covjson.org/def/domainTypes#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix hydra: <http://www.w3.org/ns/hydra/core#> .
@prefix ignf: <http://data.ign.fr/def/ignf#> .
@prefix inspiregloss: <http://inspire.ec.europa.eu/glossary/> .
@prefix ns1: <http://mmisw.org/ont/argo/qualityFlag/> .
@prefix qudt: <http://qudt.org/schema/qudt#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix ssn1: <http://www.w3.org/2005/Incubator/ssn/ssnx/ssn#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://example.com/particletypes> skos:prefLabel "Particle class"@en .

<http://www.opengis.net/def/crs/OGC/1.3/CRS84> a [ ] .

<https://qudt.org/vocab/unit/NanoM> skos:prefLabel "0.000000001-fold of the SI base unit metre"@en .

<https://w3id.org/ogcincubator/coverageJSON/POTM_range> a covjson:NdArray ;
    covjson:axisNames ( "composite" ) ;
    covjson:dataType xsd:double ;
    covjson:shape ( 2 ) .

[] a covjson:CoverageCollection ;
    hydra:member [ a covjson:Coverage ;
            covjson:domain [ a covjson:Domain ;
                    covjson:axis [ covjson:dataType covjson:tuple ],
                        [ ] ] ;
            covjson:range [ a covjson:NdArray ;
                    covjson:axisNames ( "composite" ) ;
                    covjson:dataType xsd:integer ;
                    covjson:shape ( 2 ) ],
                <https://w3id.org/ogcincubator/coverageJSON/POTM_range> ],
        [ a covjson:Coverage ;
            covjson:domain [ a covjson:Domain ;
                    covjson:axis [ covjson:dataType covjson:tuple ],
                        [ ] ] ;
            covjson:range [ a covjson:NdArray ;
                    covjson:axisNames ( "composite" ) ;
                    covjson:dataType xsd:integer ;
                    covjson:shape ( 2 ) ],
                [ a covjson:NdArray ;
                    covjson:axisNames ( "composite" ) ;
                    covjson:dataType xsd:double ;
                    covjson:shape ( 2 ) ] ] ;
    covjson:domain [ a covjson:Domain ;
            covjson:axis [ ] ] ;
    covjson:domainType covjsondt:MultiPoint ;
    covjson:parameter [ a covjson:Parameter ;
            ssn1:observedProperty <http://example.com/particletypes> ;
            covjson:categoryEncoding [ ns1:_0 0 ;
                    ns1:_1 1 ;
                    ns1:_4 2 ] ],
        [ a covjson:Parameter ;
            dcterms:description "particle diameter"@en ;
            qudt:unit [ qudt:symbol "nm"^^<http://www.opengis.net/def/uom/UCUM/> ;
                    skos:prefLabel "nanometers"@en ] ;
            ssn1:observedProperty <https://qudt.org/vocab/unit/NanoM> ] ;
    covjson:referencing [ covjson:referenceSystem [ a inspiregloss:TemporalReferenceSystem ;
                    covjson:calendar <http://www.opengis.net/def/uom/ISO-8601/0/Gregorian> ] ],
        [ covjson:referenceSystem <http://www.opengis.net/def/crs/OGC/1.3/CRS84> ],
        [ covjson:referenceSystem [ a ignf:VerticalCRS ;
                    ignf:coordinateSystem [ covjson:coordinateSystemAxes ( [ ignf:axisDirection "down" ;
                                        qudt:unit [ qudt:symbol "Pa" ] ] ) ] ] ] .


```

## Schema

```yaml
$schema: http://json-schema.org/draft-07/schema#
title: A CoverageJSON object
description: 'Component of OGC Coverage Implementation Schema 1.0. Last updated: 2023-05-10.
  Copyright (c) 2023 Open Geospatial Consortium, Inc. All Rights Reserved. To obtain
  additional rights of use, visit http://www.opengeospatial.org/legal/.'
$ref: https://schemas.opengis.net/covjson/1.0/coveragejson.json
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

* YAML version: [schema.yaml](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverageJSON/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverageJSON/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "_:_:",
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
[context.jsonld](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverageJSON/context.jsonld)

## Sources

* [CoverageJSON context](https://docs.ogc.org/cs/21-069r2/21-069r2.html)
* [Coverage Implementation Schema that CoverageJSON is based on](https://docs.ogc.org/is/09-146r8/09-146r8.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/iliad-apis-features](https://github.com/ogcincubator/iliad-apis-features)
* Path: `_sources/coverageJSON`

