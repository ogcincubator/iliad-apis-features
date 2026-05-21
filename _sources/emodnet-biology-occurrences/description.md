# EMODnet Biology Occurrences (GeoParquet)

Darwin Core occurrence records of marine biodiversity from the EMODnet Biology programme, distributed as GeoParquet 1.0.0 via the EDITO/CloudFerro S3 infrastructure.

## Source

- **Full dataset**: `https://s3.waw3-1.cloudferro.com/emodnet/emodnet_biology/12639/marine_biodiversity_observations_occurrence_2026-05-13.parquet` (65.4 M rows)
- **EDITO STAC collection**: `https://api.dive.edito.eu/data/collections/emodnet-occurrence_data`
- **Sample used**: `/tmp/edito-sample/emodnet_occurrences_sample.parquet` (1000 rows, 91.6 KB slice)

## Geometry

WKB-encoded Point geometries in a `geometry` column (GeoParquet primary column). Bounding box: [-180, -81.9953, 180, 90] — global coverage.

## Schema

81 columns total. This building block formalises the most useful ~35 columns:

| Column | Darwin Core / Vocabulary mapping |
|---|---|
| `occurrenceID` | `dwc:occurrenceID` |
| `acceptedScientificName` | `dwc:acceptedNameUsage` |
| `aphiaid` | `dwc:taxonID` (WoRMS AphiaID) |
| `aphia_uri` | `dwc:taxonConceptID` (WoRMS URI) |
| `aphia_urn` | `dwc:nameAccordingToID` (WoRMS LSID) |
| `basisOfRecord` | `dwc:basisOfRecord` |
| `kingdom`–`genus` | DwC taxon-rank terms |
| `scientificName` | `dwc:scientificName` |
| `decimalLatitude/Longitude` | `dwc:decimalLatitude/Longitude` |
| `eventDate` | `dwc:eventDate` |
| `occurrenceStatus` | `dwc:occurrenceStatus` |
| `minimumdepth/maximumdepth` | `dwc:minimumDepthInMeters/maximumDepthInMeters` |
| `samplingProtocol` | `dwc:samplingProtocol` |
| `IMISDatasetURI` | `dcterms:source` |

## License

EMODnet Biology data is published under Creative Commons Attribution (CC-BY 4.0). Attribution: EMODnet Biology consortium / VLIZ.

## Source-property coverage gaps

The following 81-column source properties are present in the parquet but not formalised in the schema (they are preserved in `dynamicProperties` or dropped on projection):

| Property | Reason not mapped | Recommended fallback |
|---|---|---|
| `eventIDLevel2`–`eventIDLevel7` | Hierarchical IMIS-specific event identifiers not in DwC | `dwc:parentEventID` |
| `associatedMedia` | Variable-format media references | `dwc:associatedMedia` (string) |
| `fieldNumber` | Rarely populated | `dwc:fieldNumber` |
| `identificationReferences` | Rarely populated | `dwc:identificationReferences` |
| `locationRemarks` | Rarely populated | `dwc:locationRemarks` |
| `materialSampleID` | Rarely populated | `dwc:materialSampleID` |
| `otherCatalogNumbers` | Rarely populated | `dwc:otherCatalogNumbers` |
| `preparationtype` | IMIS-specific | `dwc:preparations` |
| `relatedcatalogitem` | IMIS-specific linkage | `dwc:associatedOccurrences` |
| `samplesize` | Duplicate of `sampleSizeValue`+`sampleSizeUnit` | omit |
| `subGenus` | Rarely populated | `dwc:subgenus` |
| `subspecies` | Rarely populated | `dwc:infraspecificEpithet` |
| `timeofday` | Non-standard IMIS column | embed in `dwc:eventTime` |
| `timezone` | Auxiliary to timestamp | embed in `dwc:eventDate` |
| `verbatimpositiondetail` | IMIS freetext position | `dwc:verbatimLocality` |
| `county` | Rarely populated | `dwc:county` |
| `eventRemarks` | Rarely populated | `dwc:eventRemarks` |
| `occurrenceRemarks` | Rarely populated | `dwc:occurrenceRemarks` |
| `organismID` | Rarely populated | `dwc:organismID` |
| `taxonrankid` (WoRMS numeric rank) | No standard DwC mapping | `emodnet:taxonrankid` |
