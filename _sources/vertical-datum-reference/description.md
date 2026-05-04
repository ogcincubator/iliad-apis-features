# Vertical Datum Reference

Reusable schema component for encoding vertical datum metadata required for unambiguous height referencing across land and marine domains. Mandated by FMSDI Best Practice 1 (Unified Geospatial Reference).

## Purpose

The vertical datum is the single most consequential piece of metadata for any elevation or depth observation in the coastal zone. The FMSDI 2024 Pilot (OGC document 24-064) identified disconnected vertical datums as "one of the most persistent technical barriers to land-sea integration". The Compusult demonstrator encountered this problem directly: early iterations assumed Ordnance Datum Newlyn (ODN) for tidal data that was actually referenced to Southampton Chart Datum (offset -2.74m below ODN), causing water depths to display incorrectly.

## Common Datums in Intertidal Work

| Datum | Abbreviation | Orientation | Typical Use |
|---|---|---|---|
| Ordnance Datum Newlyn | ODN | up | UK land surveys, LiDAR |
| Mean Sea Level | MSL | up | General geodetic reference |
| Chart Datum | CD | down | UK navigational charts |
| Lowest Astronomical Tide | LAT | down | IHO standard for chart datum |
| WGS84 Ellipsoid | WGS84 | up | GNSS, satellite imagery |
| Southampton Chart Datum | SCD | down | Southampton Water and The Solent |
| Mean High Water Springs | MHWS | up or down | Jurisdictional boundary |

## Vertical Separation Surfaces Hierarchy

Transformations between datums follow this hierarchy:

```
Ellipsoid (WGS84 / ETRS89)
   └─► Geoid (EGM2008, OSGM15)  — apply geoid undulation
        └─► Tidal datum (MSL, MHWS, MLW)  — apply tidal model
             └─► Chart datum (CD, LAT)  — apply tidal datum offset
```

National models implement this hierarchy: NOAA VDatum (USA), UKHO VORF (UK), CHS HyVSEPs (Canada). Always prefer these over manual offsets.

## Usage Guidance

1. Include this object as a property (`verticalDatum`) in any feature or observation that carries elevation, depth, or height values.
2. Always set `verticalOrientation`. Never assume it from context — the same numerical value means opposite things under "up" (land) and "down" (marine) conventions.
3. Always record `transformationMethod` when datum conversion was applied. Absence of this field implies no conversion or unknown provenance.
4. If `separationSurface.type = "tidal"`, specify `modelReference` (e.g. "UKHO VORF 2022").
5. Before merging land and marine elevation grids, normalize both to the same `verticalOrientation`. Positive depths (down convention) must be negated before comparison with positive heights (up convention).

## Reference

- FMSDI Best Practice 1 (Unified Geospatial Reference), OGC document 24-064 D002 executive summary
- Compusult D100 Gaps and Lessons Learned: datum inconsistency (ODN vs Southampton Chart Datum -2.74m) caused depth display errors
- Pangaea D100: "Inconsistent or missing vertical datum metadata remains a major barrier to automation"
