# Transform: OBIS flat JSON occurrence response → OIM GeoJSON FeatureCollection
#
# Input:  { total: N, results: [ <flat OBIS occurrence record>, ... ] }
# Output: GeoJSON FeatureCollection conforming to nina-seapop-oim
#
# Mapping rules:
#   geometry       ← decimalLongitude, decimalLatitude (Point)
#   id             ← occurrenceID
#   colonyID       ← locality (slugified to https://seapop.no/colony/<slug>)
#   properties     ← source Darwin Core fields only; OBIS enrichment excluded
#
# Excluded fields (OBIS enrichment / pipeline — not original source data):
#   aphiaID, bathymetry, shoredistance, sst, sss,
#   id, dataset_id, node_id, dropped, absence, flags,
#   marine, brackish, category, unaccepted,
#   *id (taxonomy WoRMS IDs: kingdomid, phylumid, classid, ...)

{
  type: "FeatureCollection",
  features: [
    .results[]
    | select(.decimalLatitude != null and .decimalLongitude != null)
    | {
        type: "Feature",
        id: .occurrenceID,
        geometry: {
          type: "Point",
          coordinates: [.decimalLongitude, .decimalLatitude]
        },
        properties: {
          colonyID: (
            "https://seapop.no/colony/" +
            (
              (.locality // "unknown")
              | ascii_downcase
              | gsub("[^a-z0-9]+"; "-")
              | ltrimstr("-")
              | rtrimstr("-")
            )
          ),
          basisOfRecord:                  .basisOfRecord,
          catalogNumber:                  .catalogNumber,
          collectionCode:                 .collectionCode,
          institutionCode:                .institutionCode,
          datasetID:                      .datasetID,
          occurrenceID:                   .occurrenceID,
          occurrenceStatus:               .occurrenceStatus,
          scientificName:                 .scientificName,
          scientificNameID:               .scientificNameID,
          originalScientificName:         .originalScientificName,
          kingdom:                        .kingdom,
          phylum:                         .phylum,
          class:                          .class,
          order:                          .order,
          family:                         .family,
          genus:                          .genus,
          species:                        .species,
          decimalLatitude:                .decimalLatitude,
          decimalLongitude:               .decimalLongitude,
          coordinateUncertaintyInMeters:  .coordinateUncertaintyInMeters,
          country:                        .country,
          stateProvince:                  .stateProvince,
          locality:                       .locality,
          modified:                       .modified
        }
      }
  ]
}
