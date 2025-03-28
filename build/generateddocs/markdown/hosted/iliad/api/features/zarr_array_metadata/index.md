
# GeoZarr Array description metadata (Schema)

`ogc.hosted.iliad.api.features.zarr_array_metadata` *v0.1*

based on the https://zarr.readthedocs.io/en/v2.1.2/spec/v2.html and Iliad requiremnts

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Zarr Array Metadata

[Source: https://zarr.readthedocs.io/en/v2.1.2/spec/v2.html#arrays](https://zarr.readthedocs.io/en/v2.1.2/spec/v2.html#arrays)

Each array requires essential configuration metadata to be stored, enabling correct interpretation of the stored data. This metadata is encoded using JSON and stored as the value of the ”.zarray” key within an array store.

The metadata resource is a JSON object. The following keys MUST be present within the object:

* zarr_format - 
An integer defining the version of the storage specification to which the array store adheres.
* shape - 
A list of integers defining the length of each dimension of the array.
* chunks - 
A list of integers defining the length of each dimension of a chunk of the array. Note that all chunks within a Zarr array have the same shape.
* dtype - 
A string or list defining a valid data type for the array. See also the subsection below on data type encoding.
* compressor - 
A JSON object identifying the primary compression codec and providing configuration parameters, or null if no compressor is to be used. The object MUST contain an "id" key identifying the codec to be used.
* fill_value - 
A scalar value providing the default value to use for uninitialized portions of the array, or null if no fill_value is to be used.
* order - 
Either “C” or “F”, defining the layout of bytes within each chunk of the array. “C” means row-major order, i.e., the last dimension varies fastest; “F” means column-major order, i.e., the first dimension varies fastest.
* filters - 
A list of JSON objects providing codec configurations, or null if no filters are to be applied. Each codec configuration object MUST contain a "id" key identifying the codec to be used.
Other keys MUST NOT be present within the metadata object.
## Examples

### Zarr v2 array metadata based on https://zarr.readthedocs.io/en/v2.1.2/spec/v2.html#examples
#### json
```json
{
  "chunks": [
      1000,
      1000
  ],
  "compressor": {
      "id": "blosc",
      "cname": "lz4",
      "clevel": 5,
      "shuffle": 1
  },
  "dtype": "<f8",
  "fill_value": "NaN",
  "filters": [
      {"id": "delta", "dtype": "<f8", "astype": "<f4"}
  ],
  "order": "C",
  "shape": [
      10000,
      10000
  ],
  "zarr_format": 2
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_array_metadata/context.jsonld",
  "chunks": [
    1000,
    1000
  ],
  "compressor": {
    "id": "blosc",
    "cname": "lz4",
    "clevel": 5,
    "shuffle": 1
  },
  "dtype": "<f8",
  "fill_value": "NaN",
  "filters": [
    {
      "id": "delta",
      "dtype": "<f8",
      "astype": "<f4"
    }
  ],
  "order": "C",
  "shape": [
    10000,
    10000
  ],
  "zarr_format": 2
}
```

#### ttl
```ttl
@prefix ns1: <http:/w3id.org/iliad/zarr/compressor/> .
@prefix ns2: <http:/w3id.org/iliad/zarr/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] ns2:chunks 1000 ;
    ns2:compressor [ ns1:clevel 5 ;
            ns1:cname "lz4"^^xsd:string ;
            ns1:id "blosc"^^xsd:string ;
            ns1:shuffle 1 ] ;
    ns2:dtype "<f8"^^xsd:string ;
    ns2:fill_value "NaN"^^xsd:string ;
    ns2:filters [ ns1:id "delta"^^xsd:string ;
            ns2:dtype "<f8"^^xsd:string ] ;
    ns2:order "C"^^xsd:string ;
    ns2:shape 10000 ;
    ns2:zarr_format 2 .


```

## Schema

```yaml
$schema: http://json-schema.org/draft-07/schema#
title: Zarr Array Metadata
type: object
properties:
  chunks:
    type: array
    items:
      type: integer
    minItems: 1
    x-jsonld-id: http:/w3id.org/iliad/zarr/chunks
    x-jsonld-type: '@id'
  compressor:
    type: object
    properties:
      id:
        type: string
        x-jsonld-id: http:/w3id.org/iliad/zarr/compressor/id
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
      cname:
        type: string
        x-jsonld-id: http:/w3id.org/iliad/zarr/compressor/cname
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
      clevel:
        type: integer
        x-jsonld-id: http:/w3id.org/iliad/zarr/compressor/clevel
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
      shuffle:
        type: integer
        x-jsonld-id: http:/w3id.org/iliad/zarr/compressor/shuffle
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
    required:
    - id
    x-jsonld-id: http:/w3id.org/iliad/zarr/compressor
    x-jsonld-type: '@id'
  dtype:
    type: object
    x-jsonld-id: http:/w3id.org/iliad/zarr/dtype
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  fill_value:
    type: object
    x-jsonld-id: http:/w3id.org/iliad/zarr/fill_value
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  filters:
    type: array
    items:
      type: object
      properties:
        id:
          type: string
          x-jsonld-id: http:/w3id.org/iliad/zarr/compressor/id
          x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
        dtype:
          type: string
          x-jsonld-id: http:/w3id.org/iliad/zarr/dtype
          x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
        astype:
          type: string
      required:
      - id
    x-jsonld-id: http:/w3id.org/iliad/zarr/filters
    x-jsonld-type: '@id'
  order:
    type: string
    enum:
    - C
    - F
    x-jsonld-id: http:/w3id.org/iliad/zarr/order
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  shape:
    type: array
    items:
      type: integer
    minItems: 1
    x-jsonld-id: http:/w3id.org/iliad/zarr/shape
    x-jsonld-type: '@id'
  zarr_format:
    type: integer
    x-jsonld-id: http:/w3id.org/iliad/zarr/zarr_format
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
required:
- chunks
- compressor
- dtype
- fill_value
- filters
- order
- shape
- zarr_format

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_array_metadata/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_array_metadata/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "chunks": {
      "@id": "http:/w3id.org/iliad/zarr/chunks",
      "@type": "@id"
    },
    "compressor": {
      "@context": {
        "id": {
          "@id": "http:/w3id.org/iliad/zarr/compressor/id",
          "@type": "http://www.w3.org/2001/XMLSchema#string"
        },
        "cname": {
          "@id": "http:/w3id.org/iliad/zarr/compressor/cname",
          "@type": "http://www.w3.org/2001/XMLSchema#string"
        },
        "clevel": {
          "@id": "http:/w3id.org/iliad/zarr/compressor/clevel",
          "@type": "http://www.w3.org/2001/XMLSchema#integer"
        },
        "shuffle": {
          "@id": "http:/w3id.org/iliad/zarr/compressor/shuffle",
          "@type": "http://www.w3.org/2001/XMLSchema#integer"
        }
      },
      "@id": "http:/w3id.org/iliad/zarr/compressor",
      "@type": "@id"
    },
    "dtype": {
      "@id": "http:/w3id.org/iliad/zarr/dtype",
      "@type": "http://www.w3.org/2001/XMLSchema#string"
    },
    "fill_value": {
      "@id": "http:/w3id.org/iliad/zarr/fill_value",
      "@type": "http://www.w3.org/2001/XMLSchema#string"
    },
    "filters": {
      "@context": {
        "id": {
          "@id": "http:/w3id.org/iliad/zarr/compressor/id",
          "@type": "http://www.w3.org/2001/XMLSchema#string"
        }
      },
      "@id": "http:/w3id.org/iliad/zarr/filters",
      "@type": "@id"
    },
    "order": {
      "@id": "http:/w3id.org/iliad/zarr/order",
      "@type": "http://www.w3.org/2001/XMLSchema#string"
    },
    "shape": {
      "@id": "http:/w3id.org/iliad/zarr/shape",
      "@type": "@id"
    },
    "zarr_format": {
      "@id": "http:/w3id.org/iliad/zarr/zarr_format",
      "@type": "http://www.w3.org/2001/XMLSchema#integer"
    },
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/iliad-apis-features/build/annotated/hosted/iliad/api/features/zarr_array_metadata/context.jsonld)

## Sources

* [Zarr specification](https://zarr.readthedocs.io/en/v2.1.2/spec/v2.html#arrays)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/iliad-apis-features](https://github.com/ogcincubator/iliad-apis-features)
* Path: `_sources/zarr_array_metadata`

