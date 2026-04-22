---
name: jsonfg-conversion
description: Use when converting GeoJSON features or FeatureCollections to JSON-FG with OIM semantic enrichment (links, place, conformsTo). Supports oim, oim-bio-tdwg, oim-obs profiles. Provides the Python conversion template used by the geojson-to-jsonfg-converter agent.
---

# GeoJSON to JSON-FG Conversion Skill

## Purpose

Convert GeoJSON features to JSON-FG (JSON Feature and Geometry) format, enriching features with OIM (Oceans Information Model) semantic context and linked data annotations.

## Inputs

- `geojson`: GeoJSON Feature or FeatureCollection (object or file path)
- `context_url`: optional path to context.jsonld for property mappings
- `profile`: oim | oim-obs | oim-bio-tdwg | auto (default: auto)
- `output`: file path for converted JSON-FG, or omit to return inline

## Overview

JSON-FG extends GeoJSON with:
- Feature links (`links` property) for conformance and provenance
- Place references (`place` property with URIs)
- Feature association contexts (`@context`)
- Enhanced metadata compatible with OIM structure

OGC building block dependencies:
- `ogc.hosted.iliad.api.features.oim` - Base OIM semantic model
- `ogc.hosted.iliad.api.features.oim-bio-tdwg` - Biological/TDWG vocabularies
- `ogc.hosted.iliad.api.features.oim-obs` - Observation model (SOSA)
- `ogc.geo.json-fg.feature` - JSON-FG specification compliance

## Conversion Process

### Step 1: Validate GeoJSON
- Verify JSON-schema compliance
- Check geometry types (Point, LineString, Polygon, etc.)
- Validate feature properties

### Step 2: Enrich with OIM Context
- Map feature properties to OIM semantic properties
- Add biological/TDWG context if applicable
- Inject observation semantics (SOSA: FeatureOfInterest, ObservedProperty, etc.)

### Step 3: Add JSON-FG Extensions

Generate `links` array:
- `rel: "conformsTo"` → ogc.geo.json-fg.feature
- `rel: "conformsTo"` → ogc.hosted.iliad.api.features.oim (and profile-specific)

Generate `place` object with geographic/thematic URIs.

Add `@context` array linking to geojson-ld and context.jsonld.

### Step 4: Output

```json
{
  "type": "Feature",
  "@context": ["https://geojson.org/geojson-ld/geojson-context.jsonld", "context.jsonld"],
  "geometry": {},
  "properties": {},
  "links": [],
  "place": {}
}
```

## Python Implementation Template

```python
import json
from typing import Dict, Any, List

class GeoJSONtoJSONFGConverter:
    
    def __init__(self, context_url: str = None):
        self.context_url = context_url or "context.jsonld"
        self.oim_base = "https://opengeospatial.github.io/bblocks/"
        self.dependencies = [
            "ogc.hosted.iliad.api.features.oim",
            "ogc.hosted.iliad.api.features.oim-bio-tdwg",
            "ogc.hosted.iliad.api.features.oim-obs",
            "ogc.geo.json-fg.feature"
        ]
    
    def convert(self, geojson_feature: Dict[str, Any], profile: str = "auto") -> Dict[str, Any]:
        selected_deps = self._select_deps(geojson_feature, profile)
        return {
            "type": "Feature",
            "@context": [
                "https://geojson.org/geojson-ld/geojson-context.jsonld",
                self.context_url
            ],
            "geometry": geojson_feature.get("geometry"),
            "properties": geojson_feature.get("properties", {}),
            "links": self._build_links(selected_deps),
            "place": self._build_place(geojson_feature)
        }
    
    def _select_deps(self, feature: Dict[str, Any], profile: str) -> List[str]:
        deps = ["ogc.geo.json-fg.feature", "ogc.hosted.iliad.api.features.oim"]
        if profile == "auto":
            props = feature.get("properties", {})
            prop_names = " ".join(str(k).lower() for k in props.keys())
            if any(x in prop_names for x in ["species", "taxon", "occurrence", "scientificname"]):
                deps.append("ogc.hosted.iliad.api.features.oim-bio-tdwg")
            if any(x in prop_names for x in ["observation", "result", "sensor", "procedure"]):
                deps.append("ogc.hosted.iliad.api.features.oim-obs")
        elif profile == "oim-bio-tdwg":
            deps.append("ogc.hosted.iliad.api.features.oim-bio-tdwg")
        elif profile == "oim-obs":
            deps.append("ogc.hosted.iliad.api.features.oim-obs")
        return deps
    
    def _build_links(self, deps: List[str]) -> List[Dict[str, str]]:
        return [{"rel": "conformsTo", "href": f"{self.oim_base}{dep}", "type": "application/json"} for dep in deps]
    
    def _build_place(self, feature: Dict[str, Any]) -> Dict[str, Any]:
        geometry = feature.get("geometry", {})
        coords = geometry.get("coordinates", [])
        return {
            "type": geometry.get("type", "Point"),
            "coordinates": coords if geometry.get("type") == "Point" else coords[0] if coords else [],
            "vocab": {"location": "http://www.opengis.net/ont/sf#Point"}
        }
    
    def convert_collection(self, geojson_collection: Dict[str, Any], profile: str = "auto") -> Dict[str, Any]:
        return {
            "type": "FeatureCollection",
            "@context": ["https://geojson.org/geojson-ld/geojson-context.jsonld", self.context_url],
            "features": [self.convert(feature, profile) for feature in geojson_collection.get("features", [])]
        }
```

## Command Line Usage

```bash
# Convert single GeoJSON file to JSON-FG
python geojson_to_jsonfg.py input.geojson output.jsonfg --context context.jsonld

# Convert with OIM observations profile
python geojson_to_jsonfg.py observations.geojson obs.jsonfg --profile oim-obs

# Convert with biodiversity profile
python geojson_to_jsonfg.py species.geojson bio.jsonfg --profile oim-bio-tdwg
```

## Validation After Conversion

1. JSON-FG schema: https://raw.githubusercontent.com/opengeospatial/ogc-features-and-geometries/main/json-fg/spec/schema.json
2. OIM context: verify all properties have OIM semantic mappings
3. Example compliance: test features conform to target OIM building block schema

## References

- [OGC JSON-FG Specification](https://docs.opengeospatial.org/is/21-017/21-017.html)
- [ILIAD OIM Repository](https://github.com/ILIAD-ocean-twin/OIM)
- [GeoJSON-LD](https://geojson.org/geojson-ld/)
