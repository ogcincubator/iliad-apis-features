---
title: OGC CoverageJSON (Schema)

language_tabs:
  - json: JSON
  - jsonld: JSON-LD
  - turtle: RDF/Turtle

toc_footers:
  - Version 0.1
  - <a href='#'>OGC CoverageJSON</a>
  - <a href='https://blocks.ogc.org/register.html'>Building Blocks register</a>

search: true

code_clipboard: true

meta:
  - name: OGC CoverageJSON (Schema)
---


# OGC CoverageJSON `ogc.hosted.iliad.api.features.coverageJSON`

Based on JavaScript Object Notation (JSON), CoverageJSON is a format for publishing spatiotemporal data to the Web. The primary design goals are simplicity, machine and human readability and efficiency. While other use cases are possible, the primary CoverageJSON use case is enabling the development of interactive visual websites that display and manipulate environmental data within a web browser.

<p class="status">
    <span data-rainbow-uri="http://www.opengis.net/def/status">Status</span>:
    <a href="http://www.opengis.net/def/status/under-development" target="_blank" data-rainbow-uri>Under development</a>
</p>

<aside class="warning">
Validation for this building block has <strong><a href="https://github.com/ogcincubator/iliad-apis-features/blob/master/build/tests/hosted/iliad/api/features/coverageJSON/" target="_blank">failed</a></strong>
</aside>

# Description

## OGC Coverage JSON

[OGC CoverageJSON Community Standard ](https://docs.ogc.org/cs/21-069r2/21-069r2.html#_a4083c6e-e633-49c0-9f94-193224cf3ccb)

"Based on JavaScript Object Notation (JSON), CoverageJSON is a format for publishing spatiotemporal data to the Web. The primary design goals are simplicity, machine and human readability and efficiency. While other use cases are possible, the primary CoverageJSON use case is enabling the development of interactive visual websites that display and manipulate environmental data within a web browser.

CoverageJSON can be used to encode coverages and collections of coverages. Coverage data may be gridded or non-gridded, and data values may represent continuous values (such as temperature) or discrete categories (such as land cover classes). CoverageJSON uses JSON-LD to provide interoperability with RDF and Semantic Web applications and to reduce the potential size of the payload.

Relatively large datasets can be handled efficiently in a “web-friendly” way by partitioning information among several CoverageJSON documents, including a tiling mechanism. Nevertheless, CoverageJSON is not intended to be a replacement for efficient binary formats such as NetCDF, HDF or GRIB, and is not intended primarily to store or transfer very large datasets in bulk.""


## Key features of this profile:

- a default schema for the coverage, domainset, rangeset and rangetype
- default JSON-LD context for this result schema

# Examples

## Coverage JSON Collection representing snapshot series of PointClouds with LD



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

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/iliad-apis-features/build/tests/hosted/iliad/api/features/coverageJSON/example_1_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Ftests%2Fhosted%2Filiad%2Fapi%2Ffeatures%2FcoverageJSON%2Fexample_1_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
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
  ],
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverageJSON/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/iliad-apis-features/build/tests/hosted/iliad/api/features/coverageJSON/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Ftests%2Fhosted%2Filiad%2Fapi%2Ffeatures%2FcoverageJSON%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




## Coverage JSON Collection representing collection of PointSeries with LD



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

<blockquote class="lang-specific json">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/iliad-apis-features/build/tests/hosted/iliad/api/features/coverageJSON/example_2_1.json">Open in new window</a>
    <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=json&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Ftests%2Fhosted%2Filiad%2Fapi%2Ffeatures%2FcoverageJSON%2Fexample_2_1.json&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on JSON Viewer</a></p>
</blockquote>




```jsonld
{
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
  ],
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverageJSON/context.jsonld"
}
```

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/iliad-apis-features/build/tests/hosted/iliad/api/features/coverageJSON/example_2_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Ftests%2Fhosted%2Filiad%2Fapi%2Ffeatures%2FcoverageJSON%2Fexample_2_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




```turtle
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

<http://www.opengis.net/def/crs/OGC/1.3/CRS84> a <https://w3id.org/ogcincubator/coverageJSON/GeographicCRS> .

<https://qudt.org/vocab/unit/NanoM> skos:prefLabel "0.000000001-fold of the SI base unit metre"@en .

<https://w3id.org/ogcincubator/coverageJSON/POTM_range> a covjson:NdArray ;
    dcterms:identifier "POTM" ;
    covjson:axisNames ( "composite" ) ;
    covjson:dataType <https://w3id.org/ogcincubator/coverageJSON/float> ;
    covjson:shape ( 2 ) ;
    covjson:values "[23.8,23.8]"^^rdf:JSON .

[] a covjson:CoverageCollection ;
    hydra:member [ a covjson:Coverage ;
            covjson:domain [ a covjson:Domain ;
                    covjson:axis [ dcterms:identifier "composite" ;
                            covjson:coordinates "[\"x\",\"y\",\"z\"]"^^rdf:JSON ;
                            covjson:dataType <https://w3id.org/ogcincubator/coverageJSON/tuple> ;
                            covjson:values "[[1,20,1],[2,21,3]]"^^rdf:JSON ],
                        [ dcterms:identifier "t" ;
                            covjson:values "[\"2008-01-02T04:00:00Z\"]"^^rdf:JSON ] ] ;
            covjson:range [ a covjson:NdArray ;
                    dcterms:identifier "POTM" ;
                    covjson:axisNames ( "composite" ) ;
                    covjson:dataType <https://w3id.org/ogcincubator/coverageJSON/float> ;
                    covjson:shape ( 2 ) ;
                    covjson:values "[23.8,23.8]"^^rdf:JSON ],
                [ a covjson:NdArray ;
                    dcterms:identifier "particle_class" ;
                    covjson:axisNames ( "composite" ) ;
                    covjson:dataType <https://w3id.org/ogcincubator/coverageJSON/integer> ;
                    covjson:shape ( 2 ) ;
                    covjson:values "[1,2]"^^rdf:JSON ] ],
        [ a covjson:Coverage ;
            covjson:domain [ a covjson:Domain ;
                    covjson:axis [ dcterms:identifier "composite" ;
                            covjson:coordinates "[\"x\",\"y\",\"z\"]"^^rdf:JSON ;
                            covjson:dataType <https://w3id.org/ogcincubator/coverageJSON/tuple> ;
                            covjson:values "[[1,20,1],[2,21,3]]"^^rdf:JSON ],
                        [ dcterms:identifier "t" ;
                            covjson:values "[\"2008-01-01T04:00:00Z\"]"^^rdf:JSON ] ] ;
            covjson:range [ a covjson:NdArray ;
                    dcterms:identifier "particle_class" ;
                    covjson:axisNames ( "composite" ) ;
                    covjson:dataType <https://w3id.org/ogcincubator/coverageJSON/integer> ;
                    covjson:shape ( 2 ) ;
                    covjson:values "[1,3]"^^rdf:JSON ],
                <https://w3id.org/ogcincubator/coverageJSON/POTM_range> ] ;
    covjson:domain [ a covjson:Domain ;
            covjson:axis [ dcterms:identifier "t" ;
                    covjson:values "[\"2008-01-01T04:00:00Z\",\"2008-01-02T04:00:00Z\"]"^^rdf:JSON ] ] ;
    covjson:domainType covjsondt:MultiPoint ;
    covjson:parameter [ a covjson:Parameter ;
            dcterms:identifier "particle_class" ;
            ssn1:observedProperty <http://example.com/particletypes> ;
            covjson:categoryEncoding [ ns1:_0 0 ;
                    ns1:_1 1 ;
                    ns1:_4 2 ] ],
        [ a covjson:Parameter ;
            dcterms:description "particle diameter"@en ;
            dcterms:identifier "diameter" ;
            qudt:unit [ qudt:symbol "nm"^^<http://www.opengis.net/def/uom/UCUM/> ;
                    skos:prefLabel "nanometers"@en ] ;
            ssn1:observedProperty <https://qudt.org/vocab/unit/NanoM> ] ;
    covjson:referencing [ covjson:coordinates "[\"z\"]"^^rdf:JSON ;
            covjson:referenceSystem [ a ignf:VerticalCRS ;
                    ignf:coordinateSystem [ covjson:coordinateSystemAxes ( [ ignf:axisDirection "down" ] ) ] ] ],
        [ covjson:coordinates "[\"x\",\"y\"]"^^rdf:JSON ;
            covjson:referenceSystem <http://www.opengis.net/def/crs/OGC/1.3/CRS84> ],
        [ covjson:coordinates "[\"t\"]"^^rdf:JSON ;
            covjson:referenceSystem [ a inspiregloss:TemporalReferenceSystem ;
                    covjson:calendar <http://www.opengis.net/def/uom/ISO-8601/0/Gregorian> ] ] .


```

<blockquote class="lang-specific turtle">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/iliad-apis-features/build/tests/hosted/iliad/api/features/coverageJSON/example_2_1.ttl">Open in new window</a>
</blockquote>



# JSON Schema

```yaml--schema
$id: https://schemas.opengis.net/covjson/1.0/coveragejson.json
$schema: http://json-schema.org/draft-07/schema
description: A CoverageJSON object
type: object
properties:
  type:
    enum:
    - Domain
    - NdArray
    - TiledNdArray
    - Coverage
    - CoverageCollection
    x-jsonld-id: '@type'
required:
- type
allOf:
- if:
    properties:
      type:
        const: Domain
  then:
    $ref: '#/definitions/domain'
- if:
    properties:
      type:
        const: NdArray
  then:
    $ref: '#/definitions/ndArray'
- if:
    properties:
      type:
        const: TiledNdArray
  then:
    $ref: '#/definitions/tiledNdArray'
- if:
    properties:
      type:
        const: Coverage
  then:
    $ref: '#/definitions/coverage'
- if:
    properties:
      type:
        const: CoverageCollection
  then:
    $ref: '#/definitions/coverageCollection'
definitions:
  anyAxis:
    description: Validates any axis
    if:
      required:
      - values
    then:
      $ref: '#/definitions/valuesAxis'
    else:
      $ref: '#/definitions/numericRegularlySpacedAxis'
  coverage:
    allOf:
    - $ref: '#/definitions/coverageBase'
    - required:
      - parameters
      properties:
        domain:
          if:
            type: object
          then:
            required:
            - referencing
          x-jsonld-id: https://covjson.org/def/core#domain
  coverageBase:
    description: A Coverage, representing a mapping from a domain to sets of data
      values described by parameters.
    type: object
    properties:
      type:
        const: Coverage
        x-jsonld-id: '@type'
      id:
        type: string
        x-jsonld-id: '@id'
      domainType:
        type: string
        x-jsonld-id: https://covjson.org/def/core#domainType
        x-jsonld-type: '@vocab'
      domain:
        allOf:
        - type:
          - string
          - object
        - if:
            type: object
          then:
            $ref: '#/definitions/domainBase'
        x-jsonld-id: https://covjson.org/def/core#domain
      parameters:
        type: object
        patternProperties:
          .+:
            $ref: '#/definitions/parameter'
        x-jsonld-id: https://covjson.org/def/core#parameter
        x-jsonld-type: '@id'
        x-jsonld-container: '@index'
        x-jsonld-index: http://purl.org/dc/terms/identifier
      parameterGroups:
        type: array
        items:
          $ref: '#/definitions/parameterGroup'
      ranges:
        type: object
        patternProperties:
          .+:
            allOf:
            - type:
              - string
              - object
            - if:
                type: object
              then:
                properties:
                  type:
                    enum:
                    - NdArray
                    - TiledNdArray
                    x-jsonld-id: '@type'
                required:
                - type
            - if:
                type: object
                properties:
                  type:
                    const: NdArray
              then:
                $ref: '#/definitions/ndArray'
            - if:
                type: object
                properties:
                  type:
                    const: TiledNdArray
              then:
                $ref: '#/definitions/tiledNdArray'
        x-jsonld-id: https://covjson.org/def/core#range
        x-jsonld-type: '@id'
        x-jsonld-container: '@index'
        x-jsonld-index: http://purl.org/dc/terms/identifier
      rangeAlternates:
        type: object
    required:
    - type
    - domain
    - ranges
  coverageCollection:
    description: A collection of coverage objects
    properties:
      type:
        const: CoverageCollection
        x-jsonld-id: '@type'
      domainType:
        type: string
        x-jsonld-id: https://covjson.org/def/core#domainType
        x-jsonld-type: '@vocab'
      parameters:
        type: object
        patternProperties:
          .+:
            $ref: '#/definitions/parameter'
        x-jsonld-id: https://covjson.org/def/core#parameter
        x-jsonld-type: '@id'
        x-jsonld-container: '@index'
        x-jsonld-index: http://purl.org/dc/terms/identifier
      parameterGroups:
        type: array
        items:
          $ref: '#/definitions/parameterGroup'
      referencing:
        type: array
        items:
          $ref: '#/definitions/referenceSystemConnection'
        x-jsonld-id: https://covjson.org/def/core#referencing
        x-jsonld-container: '@set'
      coverages:
        type: array
        items:
          $ref: '#/definitions/coverageBase'
        x-jsonld-id: http://www.w3.org/ns/hydra/core#member
        x-jsonld-container: '@set'
    required:
    - type
    - coverages
    allOf:
    - $comment: If no parameters are present at collection level then each coverage
        must have their own
      if:
        not:
          required:
          - parameters
      then:
        properties:
          coverages:
            items:
              required:
              - parameters
            x-jsonld-id: http://www.w3.org/ns/hydra/core#member
            x-jsonld-container: '@set'
    - $comment: If no "referencing" member is present at collection level then each
        coverage domain must have its own
      if:
        not:
          required:
          - referencing
      then:
        properties:
          coverages:
            items:
              properties:
                domain:
                  if:
                    type: object
                  then:
                    required:
                    - referencing
            x-jsonld-id: http://www.w3.org/ns/hydra/core#member
            x-jsonld-container: '@set'
  domain:
    allOf:
    - $ref: '#/definitions/domainBase'
    - required:
      - referencing
  domainBase:
    description: A Domain, which defines a set of positions and their extent in one
      or more referencing systems
    type: object
    properties:
      type:
        const: Domain
        x-jsonld-id: '@type'
      domainType:
        type: string
        x-jsonld-id: https://covjson.org/def/core#domainType
        x-jsonld-type: '@vocab'
      axes:
        type: object
        description: Set of Axis objects, keyed by axis identifier
        minProperties: 1
        patternProperties:
          .+:
            $ref: '#/definitions/anyAxis'
        x-jsonld-id: https://covjson.org/def/core#axis
        x-jsonld-container: '@index'
        x-jsonld-index: http://purl.org/dc/terms/identifier
      referencing:
        type: array
        items:
          $ref: '#/definitions/referenceSystemConnection'
        x-jsonld-id: https://covjson.org/def/core#referencing
        x-jsonld-container: '@set'
    required:
    - type
    - axes
    dependencies:
      domainType:
        allOf:
        - if:
            properties:
              domainType:
                const: Grid
          then:
            description: 'Grid domain: x and y are required, z and t optional'
            properties:
              axes:
                properties:
                  x:
                    $ref: '#/definitions/numericAxis'
                  y:
                    $ref: '#/definitions/numericAxis'
                  z:
                    $ref: '#/definitions/numericAxis'
                  t:
                    $ref: '#/definitions/stringValuesAxis'
                required:
                - x
                - y
                additionalProperties: false
        - if:
            properties:
              domainType:
                const: Trajectory
          then:
            description: 'Trajectory domain: mandatory composite axis and optional
              z axis'
            properties:
              axes:
                properties:
                  composite:
                    allOf:
                    - $ref: '#/definitions/tupleValuesAxis'
                    - properties:
                        values:
                          items:
                            $comment: In a Trajectory, tuples always have 3 (txy)
                              or 4 (txyz) values
                            minItems: 3
                            maxItems: 4
                        coordinates:
                          enum:
                          - - t
                            - x
                            - y
                            - z
                          - - t
                            - x
                            - y
                  z:
                    $ref: '#/definitions/numericSingleValueAxis'
                required:
                - composite
                additionalProperties: false
        - if:
            properties:
              domainType:
                const: VerticalProfile
          then:
            description: 'Vertical Profile domain: mandatory x, y and z axis and optional
              t axis'
            properties:
              axes:
                properties:
                  x:
                    $ref: '#/definitions/numericSingleValueAxis'
                  y:
                    $ref: '#/definitions/numericSingleValueAxis'
                  z:
                    $ref: '#/definitions/numericAxis'
                  t:
                    $ref: '#/definitions/stringSingleValueAxis'
                required:
                - x
                - y
                - z
                additionalProperties: false
        - if:
            properties:
              domainType:
                const: Point
          then:
            description: 'Point domain: mandatory x and y axis, optional z and t axis'
            properties:
              axes:
                properties:
                  x:
                    $ref: '#/definitions/numericSingleValueAxis'
                  y:
                    $ref: '#/definitions/numericSingleValueAxis'
                  z:
                    $ref: '#/definitions/numericSingleValueAxis'
                  t:
                    $ref: '#/definitions/stringSingleValueAxis'
                required:
                - x
                - y
                additionalProperties: false
        - if:
            properties:
              domainType:
                const: PointSeries
          then:
            description: 'PointSeries domain: mandatory x, y and t axis, optional
              z axis'
            properties:
              axes:
                properties:
                  x:
                    $ref: '#/definitions/numericSingleValueAxis'
                  y:
                    $ref: '#/definitions/numericSingleValueAxis'
                  z:
                    $ref: '#/definitions/numericSingleValueAxis'
                  t:
                    $ref: '#/definitions/stringValuesAxis'
                required:
                - x
                - y
                - t
                additionalProperties: false
        - if:
            properties:
              domainType:
                const: MultiPoint
          then:
            description: 'MultiPoint domain: mandatory composite axis, optional t
              axis'
            properties:
              axes:
                properties:
                  composite:
                    allOf:
                    - $ref: '#/definitions/tupleValuesAxis'
                    - properties:
                        values:
                          items:
                            $comment: In a MultiPoint, tuples always have 2 (xy) or
                              3 values (xyz)
                            minItems: 2
                            maxItems: 3
                        coordinates:
                          enum:
                          - - x
                            - y
                            - z
                          - - x
                            - y
                  t:
                    $ref: '#/definitions/stringSingleValueAxis'
                required:
                - composite
                additionalProperties: false
        - if:
            properties:
              domainType:
                const: MultiPointSeries
          then:
            description: 'MultiPointSeries domain: mandatory composite and t axes'
            properties:
              axes:
                properties:
                  composite:
                    allOf:
                    - $ref: '#/definitions/tupleValuesAxis'
                    - properties:
                        values:
                          items:
                            $comment: In a MultiPointSeries, tuples always have 2
                              (xy) or 3 values (xyz)
                            minItems: 2
                            maxItems: 3
                        coordinates:
                          enum:
                          - - x
                            - y
                            - z
                          - - x
                            - y
                  t:
                    $ref: '#/definitions/stringValuesAxis'
                required:
                - composite
                - t
                additionalProperties: false
        - if:
            properties:
              domainType:
                const: Section
          then:
            description: 'Section domain: mandatory composite and z axes'
            properties:
              axes:
                properties:
                  composite:
                    allOf:
                    - $ref: '#/definitions/tupleValuesAxis'
                    - properties:
                        values:
                          items:
                            $comment: In a Section, tuples always have 3 values (txy)
                            minItems: 3
                            maxItems: 3
                        coordinates:
                          const:
                          - t
                          - x
                          - y
                  z:
                    $ref: '#/definitions/numericAxis'
                required:
                - composite
                - z
                additionalProperties: false
        - if:
            properties:
              domainType:
                const: Polygon
          then:
            description: 'Polygon domain: mandatory composite axis, optional z and
              t axes'
            properties:
              axes:
                properties:
                  composite:
                    allOf:
                    - $ref: '#/definitions/polygonValuesAxis'
                    - properties:
                        values:
                          $comment: There can only be one polygon in the axis
                          maxItems: 1
                        coordinates:
                          const:
                          - x
                          - y
                  z:
                    $ref: '#/definitions/numericSingleValueAxis'
                  t:
                    $ref: '#/definitions/stringSingleValueAxis'
                required:
                - composite
                additionalProperties: false
        - if:
            properties:
              domainType:
                const: PolygonSeries
          then:
            description: 'PolygonSeries domain: mandatory composite axis, optional
              z and t axes'
            properties:
              axes:
                properties:
                  composite:
                    allOf:
                    - $ref: '#/definitions/polygonValuesAxis'
                    - properties:
                        values:
                          $comment: There can only be one polygon in the axis
                          maxItems: 1
                        coordinates:
                          const:
                          - x
                          - y
                  z:
                    $ref: '#/definitions/numericSingleValueAxis'
                  t:
                    $ref: '#/definitions/stringValuesAxis'
                required:
                - composite
                additionalProperties: false
        - if:
            properties:
              domainType:
                const: MultiPolygon
          then:
            description: 'MultiPolygon domain: mandatory composite axis, optional
              z and t axes'
            properties:
              axes:
                properties:
                  composite:
                    allOf:
                    - $ref: '#/definitions/polygonValuesAxis'
                    - properties:
                        coordinates:
                          const:
                          - x
                          - y
                  z:
                    $ref: '#/definitions/numericSingleValueAxis'
                  t:
                    $ref: '#/definitions/stringSingleValueAxis'
                required:
                - composite
                additionalProperties: false
        - if:
            properties:
              domainType:
                const: MultiPolygonSeries
          then:
            description: 'MultiPolygonSeries domain: mandatory composite axis, optional
              z and t axes'
            properties:
              axes:
                properties:
                  composite:
                    allOf:
                    - $ref: '#/definitions/polygonValuesAxis'
                    - properties:
                        coordinates:
                          const:
                          - x
                          - y
                  z:
                    $ref: '#/definitions/numericSingleValueAxis'
                  t:
                    $ref: '#/definitions/stringValuesAxis'
                required:
                - composite
                additionalProperties: false
  i18n:
    type: object
    description: Object representing an internationalised string where keys are BCP
      47 language tags.
    patternProperties:
      ? ^(((([A-Za-z]{2,3}(-([A-Za-z]{3}(-[A-Za-z]{3}){0,2}))?)|[A-Za-z]{4}|[A-Za-z]{5,8})(-([A-Za-z]{4}))?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-([0-9A-WY-Za-wy-z](-[A-Za-z0-9]{2,8})+))*))$
      : type: string
    additionalProperties: false
  ndArray:
    type: object
    description: Object representing a multidimensional (>= 0D) array with named axes,
      encoded as a flat one-dimensional array in row-major order
    properties:
      type:
        const: NdArray
        x-jsonld-id: '@type'
      dataType:
        enum:
        - float
        - integer
        - string
        x-jsonld-id: https://covjson.org/def/core#dataType
        x-jsonld-type: '@id'
      shape:
        type: array
        items:
          type: number
        x-jsonld-id: https://covjson.org/def/core#shape
        x-jsonld-container: '@list'
      axisNames:
        type: array
        items:
          type: string
        uniqueItems: true
        x-jsonld-id: https://covjson.org/def/core#axisNames
        x-jsonld-container: '@list'
      values:
        type: array
        minItems: 1
        x-jsonld-id: https://covjson.org/def/core#values
        x-jsonld-type: '@json'
    allOf:
    - if:
        properties:
          dataType:
            const: float
      then:
        properties:
          values:
            items:
              type:
              - number
              - 'null'
            x-jsonld-id: https://covjson.org/def/core#values
            x-jsonld-type: '@json'
    - if:
        properties:
          dataType:
            const: integer
      then:
        properties:
          values:
            items:
              type:
              - integer
              - 'null'
            x-jsonld-id: https://covjson.org/def/core#values
            x-jsonld-type: '@json'
    - if:
        properties:
          dataType:
            const: string
      then:
        properties:
          values:
            items:
              type:
              - string
              - 'null'
            x-jsonld-id: https://covjson.org/def/core#values
            x-jsonld-type: '@json'
    - if:
        anyOf:
        - properties:
            values:
              minItems: 2
        - properties:
            shape:
              minItems: 1
          required:
          - shape
        - properties:
            axisNames:
              minItems: 1
          required:
          - axisNames
      then:
        properties:
          shape:
            minItems: 1
            x-jsonld-id: https://covjson.org/def/core#shape
            x-jsonld-container: '@list'
          axisNames:
            minItems: 1
            x-jsonld-id: https://covjson.org/def/core#axisNames
            x-jsonld-container: '@list'
        required:
        - shape
        - axisNames
    required:
    - type
    - dataType
    - values
  numericAxis:
    description: Simple axis with numeric values
    if:
      required:
      - values
    then:
      $ref: '#/definitions/numericValuesAxis'
    else:
      $ref: '#/definitions/numericRegularlySpacedAxis'
  numericRegularlySpacedAxis:
    description: A regularly-spaced numeric axis
    properties:
      start:
        type: number
        x-jsonld-id: https://covjson.org/def/core#start
      stop:
        type: number
        x-jsonld-id: https://covjson.org/def/core#stop
      num:
        type: integer
        minimum: 1
        x-jsonld-id: https://covjson.org/def/core#num
    required:
    - start
    - stop
    - num
    additionalProperties: false
  numericSingleValueAxis:
    description: Axis defined by single numeric value
    allOf:
    - $ref: '#/definitions/numericValuesAxis'
    - properties:
        values:
          maxItems: 1
          x-jsonld-id: https://covjson.org/def/core#values
          x-jsonld-type: '@json'
  numericValuesAxis:
    description: Axis defined by list of numeric axis values and optional bounds
    allOf:
    - $ref: '#/definitions/valuesAxisBase'
    - properties:
        values:
          items:
            type: number
          x-jsonld-id: https://covjson.org/def/core#values
          x-jsonld-type: '@json'
        bounds:
          items:
            type: number
          x-jsonld-id: https://covjson.org/def/core#bounds
          x-jsonld-type: '@json'
      additionalProperties: false
  observedProperty:
    type: object
    description: A definition of the quantity being measured.
    properties:
      id:
        type: string
        x-jsonld-id: '@id'
      label:
        $ref: '#/definitions/i18n'
        x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
        x-jsonld-container: '@language'
      description:
        $ref: '#/definitions/i18n'
        x-jsonld-id: http://purl.org/dc/terms/description
        x-jsonld-container: '@language'
      categories:
        type: array
        items:
          type: object
          properties:
            id:
              type: string
              x-jsonld-id: '@id'
            label:
              $ref: '#/definitions/i18n'
              x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
              x-jsonld-container: '@language'
            description:
              $ref: '#/definitions/i18n'
              x-jsonld-id: http://purl.org/dc/terms/description
              x-jsonld-container: '@language'
          required:
          - id
          - label
        minItems: 1
    required:
    - label
  parameter:
    type: object
    description: Represents metadata about the values of the coverage
    properties:
      id:
        type: string
        x-jsonld-id: '@id'
      type:
        description: Type of the parameter object, must be "Parameter"
        const: Parameter
        x-jsonld-id: '@type'
      description:
        $ref: '#/definitions/i18n'
        x-jsonld-id: http://purl.org/dc/terms/description
        x-jsonld-container: '@language'
      observedProperty:
        $ref: '#/definitions/observedProperty'
        x-jsonld-id: http://www.w3.org/2005/Incubator/ssn/ssnx/ssn#observedProperty
      unit:
        $ref: '#/definitions/unit'
        x-jsonld-id: http://qudt.org/schema/qudt#unit
      categoryEncoding:
        type: object
        description: Maps IDs of categories in the observedProperty to range values
        patternProperties:
          .+:
            oneOf:
            - type: integer
            - type: array
              items:
                type: integer
              minItems: 1
              uniqueItems: true
        x-jsonld-id: https://covjson.org/def/core#categoryEncoding
    required:
    - type
    - observedProperty
  parameterGroup:
    type: object
    description: Represents logical groups of parameters
    properties:
      type:
        description: Type of the parameter group object, must be "ParameterGroup"
        const: ParameterGroup
        x-jsonld-id: '@type'
      id:
        type: string
        x-jsonld-id: '@id'
      label:
        $ref: '#/definitions/i18n'
        x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
        x-jsonld-container: '@language'
      description:
        $ref: '#/definitions/i18n'
        x-jsonld-id: http://purl.org/dc/terms/description
        x-jsonld-container: '@language'
      observedProperty:
        $ref: '#/definitions/observedProperty'
        x-jsonld-id: http://www.w3.org/2005/Incubator/ssn/ssnx/ssn#observedProperty
      members:
        type: array
        items:
          type: string
        minItems: 1
        uniqueItems: true
        x-jsonld-id: https://covjson.org/def/core#member
        x-jsonld-type: '@vocab'
        x-jsonld-container: '@set'
    required:
    - type
    - members
    anyOf:
    - required:
      - label
    - required:
      - observedProperty
  polygonValuesAxis:
    description: Polygon-based axis
    allOf:
    - $ref: '#/definitions/valuesAxisBase'
    - properties:
        dataType:
          const: polygon
          x-jsonld-id: https://covjson.org/def/core#dataType
          x-jsonld-type: '@id'
        values:
          items:
            description: A GeoJSON polygon
            type: array
            items:
              type: array
              items:
                description: 'The inner array: the coordinates themselves'
                type: array
                items:
                  type: number
                minItems: 2
              minItems: 1
            minItems: 1
          x-jsonld-id: https://covjson.org/def/core#values
          x-jsonld-type: '@json'
        coordinates:
          x-jsonld-id: https://covjson.org/def/core#coordinates
          x-jsonld-type: '@json'
      required:
      - dataType
      - values
      - coordinates
      additionalProperties: false
  primitiveValuesAxis:
    description: Validates any axis with primitive values
    allOf:
    - $ref: '#/definitions/valuesAxisBase'
    - $comment: This redundant branch exists to fail early with succinct errors
      properties:
        values:
          items:
            oneOf:
            - type: number
            - type: string
          x-jsonld-id: https://covjson.org/def/core#values
          x-jsonld-type: '@json'
    - if:
        properties:
          values:
            items:
              type: number
      then:
        $ref: '#/definitions/numericValuesAxis'
      else:
        $ref: '#/definitions/stringValuesAxis'
  referenceSystem:
    type: object
    properties:
      type:
        type: string
        x-jsonld-id: '@type'
    required:
    - type
    allOf:
    - if:
        properties:
          type:
            const: TemporalRS
      then:
        description: Temporal reference system
        properties:
          calendar:
            type: string
            oneOf:
            - const: Gregorian
            - pattern: ^https?://
            x-jsonld-id: https://covjson.org/def/core#calendar
            x-jsonld-type: '@vocab'
          timeScale:
            type: string
            x-jsonld-id: https://covjson.org/def/core#timeScale
        required:
        - calendar
    - if:
        properties:
          type:
            const: IdentifierRS
      then:
        description: An identifier-based reference system
        properties:
          id:
            type: string
            x-jsonld-id: '@id'
          label:
            $ref: '#/definitions/i18n'
            x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
            x-jsonld-container: '@language'
          description:
            $ref: '#/definitions/i18n'
            x-jsonld-id: http://purl.org/dc/terms/description
            x-jsonld-container: '@language'
          targetConcept:
            $ref: '#/definitions/targetConcept'
            x-jsonld-id: https://covjson.org/def/core#targetConcept
          identifiers:
            type: object
            patternProperties:
              .+:
                $ref: '#/definitions/targetConcept'
            x-jsonld-id: https://covjson.org/def/core#identifier
            x-jsonld-type: '@id'
            x-jsonld-container: '@index'
        required:
        - targetConcept
  referenceSystemConnection:
    description: 'Reference System Connection object: connects coordinates to reference
      systems'
    type: object
    properties:
      coordinates:
        type: array
        items:
          type: string
        minItems: 1
        x-jsonld-id: https://covjson.org/def/core#coordinates
        x-jsonld-type: '@json'
      system:
        $ref: '#/definitions/referenceSystem'
        x-jsonld-id: https://covjson.org/def/core#referenceSystem
    required:
    - coordinates
    - system
  stringSingleValueAxis:
    description: Axis defined by single string value
    allOf:
    - $ref: '#/definitions/stringValuesAxis'
    - properties:
        values:
          maxItems: 1
          x-jsonld-id: https://covjson.org/def/core#values
          x-jsonld-type: '@json'
  stringValuesAxis:
    description: Simple axis with string values (e.g. time strings)
    allOf:
    - $ref: '#/definitions/valuesAxisBase'
    - properties:
        values:
          items:
            type: string
          x-jsonld-id: https://covjson.org/def/core#values
          x-jsonld-type: '@json'
        bounds:
          items:
            type: string
          x-jsonld-id: https://covjson.org/def/core#bounds
          x-jsonld-type: '@json'
      additionalProperties: false
  targetConcept:
    type: object
    properties:
      id:
        type: string
        x-jsonld-id: '@id'
      label:
        $ref: '#/definitions/i18n'
        x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
        x-jsonld-container: '@language'
      description:
        $ref: '#/definitions/i18n'
        x-jsonld-id: http://purl.org/dc/terms/description
        x-jsonld-container: '@language'
    required:
    - label
  tiledNdArray:
    type: object
    description: Object representing a multidimensional (>= 1D) array with named axes
      split up into sets of linked NdArray documents
    properties:
      type:
        const: TiledNdArray
        x-jsonld-id: '@type'
      dataType:
        enum:
        - float
        - integer
        - string
        x-jsonld-id: https://covjson.org/def/core#dataType
        x-jsonld-type: '@id'
      shape:
        type: array
        items:
          type: number
        minItems: 1
        x-jsonld-id: https://covjson.org/def/core#shape
        x-jsonld-container: '@list'
      axisNames:
        type: array
        items:
          type: string
        minItems: 1
        uniqueItems: true
        x-jsonld-id: https://covjson.org/def/core#axisNames
        x-jsonld-container: '@list'
      tileSets:
        type: array
        minItems: 1
        items:
          type: object
          properties:
            tileShape:
              type: array
              items:
                type:
                - number
                - 'null'
              minItems: 1
              x-jsonld-id: https://covjson.org/def/core#tileShape
              x-jsonld-container: '@list'
            urlTemplate:
              type: string
              description: RFC 6570 Level 1 URI template
              x-jsonld-id: https://covjson.org/def/core#urlTemplate
          required:
          - tileShape
          - urlTemplate
        x-jsonld-id: https://covjson.org/def/core#tileSet
        x-jsonld-container: '@set'
    required:
    - type
    - dataType
    - shape
    - axisNames
    - tileSets
  tupleValuesAxis:
    description: Tuple-based axis
    allOf:
    - $ref: '#/definitions/valuesAxisBase'
    - properties:
        dataType:
          const: tuple
          x-jsonld-id: https://covjson.org/def/core#dataType
          x-jsonld-type: '@id'
        values:
          items:
            description: A tuple of axis values (numbers or strings)
            type: array
            items:
              type:
              - number
              - string
            minItems: 2
          x-jsonld-id: https://covjson.org/def/core#values
          x-jsonld-type: '@json'
        coordinates:
          x-jsonld-id: https://covjson.org/def/core#coordinates
          x-jsonld-type: '@json'
      required:
      - dataType
      - values
      - coordinates
      additionalProperties: false
  unit:
    type: object
    description: The units of measure
    properties:
      id:
        type: string
        x-jsonld-id: '@id'
      label:
        $ref: '#/definitions/i18n'
        x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
        x-jsonld-container: '@language'
      symbol:
        allOf:
        - type:
          - string
          - object
        - if:
            type: object
          then:
            properties:
              type:
                type: string
                x-jsonld-id: '@type'
              value:
                type: string
                x-jsonld-id: '@value'
            required:
            - type
            - value
        x-jsonld-id: http://qudt.org/schema/qudt#symbol
    anyOf:
    - required:
      - label
    - required:
      - symbol
  valuesAxis:
    description: Validates any values-based axis
    allOf:
    - $ref: '#/definitions/valuesAxisBase'
    - if:
        not:
          required:
          - dataType
      then:
        $ref: '#/definitions/primitiveValuesAxis'
    dependencies:
      dataType:
        allOf:
        - if:
            properties:
              dataType:
                const: tuple
          then:
            $ref: '#/definitions/tupleValuesAxis'
        - if:
            properties:
              dataType:
                const: polygon
          then:
            $ref: '#/definitions/polygonValuesAxis'
  valuesAxisBase:
    $comment: Base schema for values-based axis schemas
    properties:
      dataType:
        type: string
        not:
          const: primitive
        x-jsonld-id: https://covjson.org/def/core#dataType
        x-jsonld-type: '@id'
      values:
        type: array
        minItems: 1
        uniqueItems: true
        x-jsonld-id: https://covjson.org/def/core#values
        x-jsonld-type: '@json'
      coordinates:
        type: array
        items:
          type: string
        minItems: 2
        x-jsonld-id: https://covjson.org/def/core#coordinates
        x-jsonld-type: '@json'
      bounds:
        description: Optional axis bounds. Must be twice as long (and same data type)
          as "values"
        type: array
        minItems: 2
        x-jsonld-id: https://covjson.org/def/core#bounds
        x-jsonld-type: '@json'
    required:
    - values
x-jsonld-extra-terms:
  title:
    x-jsonld-id: http://purl.org/dc/terms/title
    x-jsonld-container: '@language'
  Domain: https://covjson.org/def/core#Domain
  primitive: https://covjson.org/def/core#primitive
  tuple: https://covjson.org/def/core#tuple
  polygon: https://covjson.org/def/core#polygon
  components:
    x-jsonld-id: https://covjson.org/def/core#components
    x-jsonld-container: '@list'
  RS: https://covjson.org/def/core#ReferenceSystem
  CRS: https://covjson.org/def/core#CoordinateReferenceSystem
  cs: http://data.ign.fr/def/ignf#coordinateSystem
  CS: http://data.ign.fr/def/ignf#CoordinateSystem
  TemporalRS: http://inspire.ec.europa.eu/glossary/TemporalReferenceSystem
  TemporalCRS: https://covjson.org/def/core#TemporalCRS
  Gregorian: http://www.opengis.net/def/uom/ISO-8601/0/Gregorian
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
  Parameter: https://covjson.org/def/core#Parameter
  ParameterGroup: https://covjson.org/def/core#ParameterGroup
  NdArray: https://covjson.org/def/core#NdArray
  TiledNdArray: https://covjson.org/def/core#TiledNdArray
  float: http://www.w3.org/2001/XMLSchema#double
  integer: http://www.w3.org/2001/XMLSchema#integer
  string: http://www.w3.org/2001/XMLSchema#string
  Coverage: https://covjson.org/def/core#Coverage
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

> <a target="_blank" href="https://avillar.github.io/TreedocViewer/?dataParser=yaml&amp;dataUrl=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Fannotated%2Fhosted%2Filiad%2Fapi%2Ffeatures%2FcoverageJSON%2Fschema.yaml&amp;expand=2&amp;option=%7B%22showTable%22%3A+false%7D">View on YAML Viewer</a>

Links to the schema:

* YAML version: <a href="https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverageJSON/schema.yaml" target="_blank">https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverageJSON/schema.yaml</a>
* JSON version: <a href="https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverageJSON/schema.json" target="_blank">https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverageJSON/schema.json</a>


# JSON-LD Context

```json--ldContext
{
  "@context": {
    "type": "@type",
    "domainType": {
      "@id": "covjson:domainType",
      "@type": "@vocab"
    },
    "axes": {
      "@context": {
        "coordinates": {
          "@id": "covjson:coordinates",
          "@type": "@json"
        },
        "bounds": {
          "@id": "covjson:bounds",
          "@type": "@json"
        },
        "start": "covjson:start",
        "stop": "covjson:stop",
        "num": "covjson:num"
      },
      "@id": "covjson:axis",
      "@container": "@index",
      "@index": "dct:identifier"
    },
    "referencing": {
      "@context": {
        "coordinates": {
          "@id": "covjson:coordinates",
          "@type": "@json"
        },
        "system": {
          "@context": {
            "calendar": {
              "@id": "covjson:calendar",
              "@type": "@vocab"
            },
            "timeScale": "covjson:timeScale",
            "targetConcept": "covjson:targetConcept",
            "identifiers": {
              "@id": "covjson:identifier",
              "@type": "@id",
              "@container": "@index"
            }
          },
          "@id": "covjson:referenceSystem"
        }
      },
      "@id": "covjson:referencing",
      "@container": "@set"
    },
    "dataType": {
      "@id": "covjson:dataType",
      "@type": "@id"
    },
    "shape": {
      "@id": "covjson:shape",
      "@container": "@list"
    },
    "axisNames": {
      "@id": "covjson:axisNames",
      "@container": "@list"
    },
    "values": {
      "@id": "covjson:values",
      "@type": "@json"
    },
    "tileSets": {
      "@context": {
        "tileShape": {
          "@id": "covjson:tileShape",
          "@container": "@list"
        },
        "urlTemplate": "covjson:urlTemplate"
      },
      "@id": "covjson:tileSet",
      "@container": "@set"
    },
    "id": "@id",
    "domain": {
      "@context": {},
      "@id": "covjson:domain"
    },
    "parameters": {
      "@context": {
        "unit": {
          "@context": {
            "symbol": {
              "@context": {
                "value": "@value"
              },
              "@id": "qudt:symbol"
            }
          },
          "@id": "qudt:unit"
        },
        "categoryEncoding": "covjson:categoryEncoding"
      },
      "@id": "covjson:parameter",
      "@type": "@id",
      "@container": "@index",
      "@index": "dct:identifier"
    },
    "label": {
      "@id": "skos:prefLabel",
      "@container": "@language"
    },
    "description": {
      "@id": "dct:description",
      "@container": "@language"
    },
    "observedProperty": {
      "@context": {},
      "@id": "ssn:observedProperty"
    },
    "members": {
      "@id": "covjson:member",
      "@type": "@vocab",
      "@container": "@set"
    },
    "ranges": {
      "@context": {},
      "@id": "covjson:range",
      "@type": "@id",
      "@container": "@index",
      "@index": "dct:identifier"
    },
    "coverages": {
      "@context": {},
      "@id": "hydra:member",
      "@container": "@set"
    },
    "title": {
      "@id": "dct:title",
      "@container": "@language"
    },
    "Domain": "covjson:Domain",
    "primitive": "covjson:primitive",
    "tuple": "covjson:tuple",
    "polygon": "covjson:polygon",
    "components": {
      "@id": "covjson:components",
      "@container": "@list"
    },
    "RS": "covjson:ReferenceSystem",
    "CRS": "covjson:CoordinateReferenceSystem",
    "cs": "ignf:coordinateSystem",
    "CS": "ignf:CoordinateSystem",
    "TemporalRS": "inspiregloss:TemporalReferenceSystem",
    "TemporalCRS": "covjson:TemporalCRS",
    "Gregorian": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian",
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
    "Parameter": "covjson:Parameter",
    "ParameterGroup": "covjson:ParameterGroup",
    "NdArray": "covjson:NdArray",
    "TiledNdArray": "covjson:TiledNdArray",
    "float": "xsd:double",
    "integer": "xsd:integer",
    "string": "xsd:string",
    "Coverage": "covjson:Coverage",
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

> <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Fannotated%2Fhosted%2Filiad%2Fapi%2Ffeatures%2FcoverageJSON%2Fcontext.jsonld">View on JSON-LD Playground</a>

You can find the full JSON-LD context here:
<a href="https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverageJSON/context.jsonld" target="_blank">https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/coverageJSON/context.jsonld</a>

# References

* [CoverageJSON context](https://docs.ogc.org/cs/21-069r2/21-069r2.html)
* [Coverage Implementation Schema that CoverageJSON is based on](https://docs.ogc.org/is/09-146r8/09-146r8.html)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: <a href="https://github.com/ogcincubator/iliad-apis-features" target="_blank">https://github.com/ogcincubator/iliad-apis-features</a>
* Path:
<code><a href="https://github.com/ogcincubator/iliad-apis-features/blob/HEAD/_sources/coverageJSON" target="_blank">_sources/coverageJSON</a></code>

