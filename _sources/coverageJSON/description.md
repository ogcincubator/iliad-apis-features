## OGC Coverage JSON

[OGC CoverageJSON Community Standard ](https://docs.ogc.org/cs/21-069r2/21-069r2.html#_a4083c6e-e633-49c0-9f94-193224cf3ccb)

"Based on JavaScript Object Notation (JSON), CoverageJSON is a format for publishing spatiotemporal data to the Web. The primary design goals are simplicity, machine and human readability and efficiency. While other use cases are possible, the primary CoverageJSON use case is enabling the development of interactive visual websites that display and manipulate environmental data within a web browser.

CoverageJSON can be used to encode coverages and collections of coverages. Coverage data may be gridded or non-gridded, and data values may represent continuous values (such as temperature) or discrete categories (such as land cover classes). CoverageJSON uses JSON-LD to provide interoperability with RDF and Semantic Web applications and to reduce the potential size of the payload.

Relatively large datasets can be handled efficiently in a “web-friendly” way by partitioning information among several CoverageJSON documents, including a tiling mechanism. Nevertheless, CoverageJSON is not intended to be a replacement for efficient binary formats such as NetCDF, HDF or GRIB, and is not intended primarily to store or transfer very large datasets in bulk.""


## Key features of this profile:

- a default schema for the coverage, domainset, rangeset and rangetype
- default JSON-LD context for this result schema
