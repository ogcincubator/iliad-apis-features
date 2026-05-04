# Dynamic Shoreline Feature

Feature type for tide-dependent shoreline vectors, encoding shoreline type, water level at capture, tidal datum reference, sensor platform, and spatial/temporal uncertainty. Based on the TCarta demonstrator from the OGC FMSDI 2024 Pilot at Hurst Spit, The Solent (UK).

## Why Static Shorelines Are Inadequate

A shoreline without water-level attribution is an incomplete observation. The TCarta FMSDI demonstrator showed that the same coastal area at Hurst Spit produces substantially different shoreline positions depending on the tidal state at time of satellite acquisition. The NOAA CUSP vs Historical Composite Shoreline comparison in the Compusult demonstrator showed further discrepancies from differing capture methodologies.

Static shoreline products cannot be reused for:
- **Flood modelling**: requires knowledge of the datum to which the boundary is referenced
- **Navigation**: requires confirmation that the low-water boundary represents a navigable depth contour
- **Multi-temporal comparison**: requires all observations to reference a common datum or at least record their individual water levels
- **Inundation risk**: the exact position of the MHWS boundary determines legal and engineering thresholds

## IHO Tidal Datum Hierarchy

The `tidalDatumReference` field uses IHO S-32 terminology. The ascending hierarchy of datums (increasing water level) is:

```
LAT  (Lowest Astronomical Tide)   ← chart datum reference
MLWS (Mean Low Water Springs)
MLW  (Mean Low Water)
MSL  (Mean Sea Level)             ← geodetic reference
MHW  (Mean High Water)
MHWS (Mean High Water Springs)    ← land/sea jurisdictional boundary (UK)
HAT  (Highest Astronomical Tide)
```

CD (Chart Datum) is typically close to LAT but defined operationally by national hydrographic offices.

## Instantaneous vs Datum Contour Shorelines

The `shorelineType` field distinguishes these fundamentally different products:

- **instantaneous**: a satellite snapshot of the actual land-water boundary at a specific moment. The water level at that moment must be recorded in `waterLevelAtCapture`. This shoreline CANNOT be used as a datum contour without tidal modelling.
- **tidalDatumContour**, **meanHighWater**, **chartDatumContour** etc.: derived/modelled surfaces, typically computed from multiple instantaneous observations or from a topo-bathymetric model. These represent a statistical or modelled surface, not a direct observation.

Never mix these two categories in analysis without explicit labelling. The Compusult demonstrator documented discrepancies between NOAA CUSP (a datum contour product) and NOAA Historical Composite Shoreline (a compilation from multiple methods), attributed to this category confusion.

## NDWI

The Normalized Difference Water Index (NDWI = (Green − NIR) / (Green + NIR)) is a spectral index applied to optical satellite imagery to delineate the water/land boundary. The TCarta demonstrator used Planet Labs SuperDove imagery with NDWI thresholding. Key sensitivities:

- Threshold choice: a change of ±0.05 in threshold can move the shoreline horizontally by tens of metres on low-gradient beaches
- Vegetation: salt marsh and mangrove vegetation produces NDWI values similar to wet soil, causing false positives
- Turbidity: highly turbid water may be misclassified as land
- Intra-scene variation: wide-swath sensors (Sentinel-2, 290km) span multiple tidal states within a single scene

Always record `ndwiThreshold` when `captureMethod = "opticalSatellite_NDWI"`.

## Usage for Consistency

1. Always pair `captureDateTime` with `waterLevelAtCapture` for instantaneous shorelines
2. When aggregating shorelines across time, normalise to a common `tidalDatumReference` before analysis
3. `horizontalUncertainty` must account for both sensor accuracy AND slope effect: water level uncertainty × inverse coastal slope gives additional positional uncertainty
4. Never use `shorelineType="instantaneous"` as a proxy for a tidal datum contour without explicit modelling
5. Record `tideGaugeRef` or `waterLevelModelRef` to enable future datum conversion

## References

- TCarta D100 demonstrator (Hurst Spit, NDWI + SAR + tide gauges), FMSDI 2024 Pilot
- Compusult D100 (shoreline model differences: NOAA CUSP vs Historical Composite)
- FMSDI BP1 (common reference — all shorelines need an explicit datum)
- FMSDI BP3 (mind the gap — shoreline position IS the gap boundary)
- IHO S-32 Hydrographic Dictionary (tidal datum terminology)
- IHO S-44 / CATZOC (accuracy zone classification)
- OGC documents: D001=24-061, D002=24-064
