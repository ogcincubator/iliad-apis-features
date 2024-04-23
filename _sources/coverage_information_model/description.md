## OGC Coverage Implementation Schema

Coverages represent homogeneous collections of values located in space/time, such as spatio-temporal sensor, image, simulation, and statistics data. Common examples include 1-D timeseries, 2-D imagery, 3-D x/y/t image timeseries and x/y/z geophysical voxel models, as well as 4-D x/y/z/t climate and ocean data. Generally, coverages encompass multi-dimen­sional regular and irregular grids, point clouds, and general meshes.

This Coverage Implementation Schema (CIS) specifies the OGC coverage model by establishing a concrete, interoperable, conformance-testable coverage structure. It is based on the abstract concepts of OGC Abstract Topic 6 [1] (which is identical to ISO 19123) which spec­i­fies an abstract model which is not per se interoperable – in other words, many different and incompatible implementations of the abstract model are possible. CIS, on the other hand, is interoperable in the sense that coverages can be conformance tested, regardless of their data format encoding, down to the level of single “pixels” or “voxels.”

Coverages can be encoded in any suitable format (such as GML, JSON, GeoTIFF, or Net­CDF) and can be partitioned, e.g., for a time-interleaved representation. Coverages are independent from service definitions and, therefore, can be accessed through a variety of OGC services types, such as the Web Coverage Service (WCS) Standard [8]. The coverage structure can serve a wide range of coverage application domains, thereby contributing to harmon­ization and interoperability between and across these domains.

## Key features of this profile:

- a schema for the coverage, domainset, rangeset and rangetype
- a JSON-LD context for this result schema
