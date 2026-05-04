# OIM Coastal Feature

OIM profile for features in the intertidal and coastal zone — the "white ribbon" — as defined by the OGC Federated Marine SDI 2024 Pilot. Implements FMSDI Best Practices 1 (Unified Geospatial Reference), 3 (Mind the Gap), and 5 (Scalable Resolution Management).

## The White Ribbon

The intertidal zone — first coined as the "white ribbon" by the British Geological Survey — is the strip of coastline that alternates between being exposed during low tide and submerged during high tide. It is poorly surveyed due to overlapping jurisdictional responsibilities and challenging environmental conditions, creating persistent data voids that hinder coastal modelling, flood risk assessment, and infrastructure planning.

The `featureDomain` discriminator (`land` / `intertidal` / `marine`) is critical for any downstream harmonization: land data and marine data use different vertical datum conventions, different coordinate reference systems, and different accuracy standards. Without an explicit domain label, merging land elevation with bathymetric soundings requires assumptions that are frequently wrong.

## The 4D Nature of Intertidal Data

FMSDI identifies four critical dimensions for intertidal feature representation:

1. **Elevation** — the vertical position, which is meaningless without a datum
2. **Time** — the capture date/time, because the intertidal zone is dynamic
3. **Uncertainty** — quantified accuracy, required for fitness-for-purpose assessment
4. **Domain** — whether the observation was land-side or marine-side

All four must be present. A depth observation without a datum, or an elevation without an uncertainty, cannot be reliably integrated with other datasets.

## Gap Filling (FMSDI Best Practice 3)

The `gapFilled` flag and `interpolationMethod` fields document when a feature fills a data void in the white ribbon. FMSDI BP3 mandates:

- Prefer new observations (satellite-derived elevation, airborne topo-bathy LiDAR, targeted sonar/UAV surveys) over interpolation
- If interpolation is unavoidable, it is a **last resort**; select the method based on geomorphology
- Document all assumptions and error metrics in metadata

When `gapFilled=true`, the `interpolationMethod` field becomes required. Typical values: TIN, cubicSpline, kriging, IDW.

## Vertical Orientation Consistency Rule

The `verticalOrientation` field in the embedded `verticalDatum` object is critical. Land surveys use `up` (positive = higher elevation); hydrographic surveys use `down` (positive = greater depth). Before combining data from both domains, normalize to a single orientation. A positive depth value (down convention) must be negated before arithmetic comparison with a positive height (up convention).

## References

- FMSDI BP1 (Unified Geospatial Reference), BP3 (Mind the Gap), BP5 (Scalable Resolution Management) — OGC document 24-064
- Compusult D100 (data gaps between land and marine datasets, interpolation across the intertidal)
- Pangaea D100 (DGGS integration, dggsCellRef for scalable multi-resolution querying)
- TCarta D100 (satellite-derived elevation and bathymetry for white ribbon)
