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