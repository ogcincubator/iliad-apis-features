---
title: OGC CoverageJSON (Schema)


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
    <a href="http://www.opengis.net/def/status/invalid" target="_blank" data-rainbow-uri>Invalid</a>
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



```jsonld
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

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/iliad-apis-features/build/tests/hosted/iliad/api/features/coverageJSON/example_1_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Ftests%2Fhosted%2Filiad%2Fapi%2Ffeatures%2FcoverageJSON%2Fexample_1_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




## Coverage JSON Collection representing collection of PointSeries with LD



```jsonld
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

<blockquote class="lang-specific jsonld">
  <p class="example-links">
    <a target="_blank" href="https://ogcincubator.github.io/iliad-apis-features/build/tests/hosted/iliad/api/features/coverageJSON/example_2_1.jsonld">Open in new window</a>
    <a target="_blank" href="https://json-ld.org/playground/#json-ld=https%3A%2F%2Fogcincubator.github.io%2Filiad-apis-features%2Fbuild%2Ftests%2Fhosted%2Filiad%2Fapi%2Ffeatures%2FcoverageJSON%2Fexample_2_1.jsonld">View on JSON-LD Playground</a>
</blockquote>




# JSON Schema

```yaml--schema
$schema: http://json-schema.org/draft-07/schema#
title: A CoverageJSON object
description: 'Component of OGC Coverage Implementation Schema 1.0. Last updated: 2023-05-10.
  Copyright (c) 2023 Open Geospatial Consortium, Inc. All Rights Reserved. To obtain
  additional rights of use, visit http://www.opengeospatial.org/legal/.'
$ref: https://schemas.opengis.net/covjson/1.0/coveragejson.json
x-jsonld-prefixes:
  covjson: https://covjson.org/def/core#
  covjsondt: https://covjson.org/def/domainTypes#
  xsd: http://www.w3.org/2001/XMLSchema#
  ssn: http://www.w3.org/2005/Incubator/ssn/ssnx/ssn#
  skos: http://www.w3.org/2004/02/skos/core#
  dct: http://purl.org/dc/terms/
  hydra: http://www.w3.org/ns/hydra/core#
  qudt: http://qudt.org/schema/qudt#
  ignf: http://data.ign.fr/def/ignf#
  inspiregloss: http://inspire.ec.europa.eu/glossary/
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
    "covjson": "https://covjson.org/def/core#",
    "covjsondt": "https://covjson.org/def/domainTypes#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ssn": "http://www.w3.org/2005/Incubator/ssn/ssnx/ssn#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dct": "http://purl.org/dc/terms/",
    "hydra": "http://www.w3.org/ns/hydra/core#",
    "qudt": "http://qudt.org/schema/qudt#",
    "ignf": "http://data.ign.fr/def/ignf#",
    "inspiregloss": "http://inspire.ec.europa.eu/glossary/",
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

