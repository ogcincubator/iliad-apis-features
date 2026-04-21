# GeoJSON to JSON-FG Converter Skill

## Purpose

Convert GeoJSON features to JSON-FG (JSON Feature and Geometry) format, enriching features with OIM (Oceans Information Model) semantic context and linked data annotations.

## Overview

JSON-FG extends GeoJSON with:
- Feature links (`links` property)
- Place references (`place` property with URIs)
- Feature association contexts
- Enhanced metadata compatible with OIM structure

This skill leverages OGC building block dependencies to ensure semantic consistency:
- `ogc.hosted.iliad.api.features.oim` - Base OIM semantic model
- `ogc.hosted.iliad.api.features.oim-bio-tdwg` - Biological/TDWG vocabularies
- `ogc.hosted.iliad.api.features.oim-obs` - Observation model (SOSA)
- `ogc.geo.json-fg.feature` - JSON-FG specification compliance

## Conversion Process

### Input Requirements
- Valid GeoJSON FeatureCollection or Feature
- Properties aligned with OIM schema
- Recommended: OIM context.jsonld mappings

### Step 1: Validate GeoJSON
- Verify JSON-schema compliance
- Check geometry types (Point, LineString, Polygon, etc.)
- Validate feature properties

### Step 2: Enrich with OIM Context
- Map feature properties to OIM semantic properties
- Add biological/TDWG context if applicable
- Inject observation semantics (SOSA: FeatureOfInterest, ObservedProperty, etc.)

### Step 3: Add JSON-FG Extensions
- Create feature `links` array with:
  - `rel: "data-source"` - link to provenance
  - `rel: "semantic-context"` - link to context.jsonld
  - `rel: "conformsTo"` - links to OGC dependencies
- Add `place` object with geographic/thematic URIs
- Preserve geometry in `geometry` property
- Add `geometry-derived` properties if applicable

### Step 4: Generate JSON-FG Output
```json
{
  "type": "Feature",
  "@context": ["https://geojson.org/geojson-ld/geojson-context.jsonld", "context.jsonld"],
  "geometry": {...},
  "properties": {...},
  "links": [...],
  "place": {...}
}
```

## Python Implementation Template

```python
import json
from typing import Dict, Any, List

class GeoJSONtoJSONFGConverter:
    """Convert GeoJSON features to JSON-FG with OIM context."""
    
    def __init__(self, context_url: str = None):
        self.context_url = context_url or "context.jsonld"
        self.dependencies = [
            "ogc.hosted.iliad.api.features.oim",
            "ogc.hosted.iliad.api.features.oim-bio-tdwg",
            "ogc.hosted.iliad.api.features.oim-obs",
            "ogc.geo.json-fg.feature"
        ]
    
    def convert(self, geojson_feature: Dict[str, Any]) -> Dict[str, Any]:
        """Convert GeoJSON feature to JSON-FG."""
        jsonfg = {
            "type": "Feature",
            "@context": [
                "https://geojson.org/geojson-ld/geojson-context.jsonld",
                self.context_url
            ],
            "geometry": geojson_feature.get("geometry"),
            "properties": geojson_feature.get("properties", {}),
            "links": self._build_links(geojson_feature),
            "place": self._build_place(geojson_feature)
        }
        return jsonfg
    
    def _build_links(self, feature: Dict[str, Any]) -> List[Dict[str, str]]:
        """Build links array for JSON-FG."""
        links = [
            {
                "rel": "conformsTo",
                "href": "https://www.opengis.net/def/featureType/OGC-1.1/Point",
                "type": "application/json"
            }
        ]
        
        # Add OIM dependencies
        for dep in self.dependencies:
            links.append({
                "rel": "conformsTo",
                "href": f"https://opengeospatial.github.io/bblocks/{dep}",
                "type": "application/json"
            })
        
        return links
    
    def _build_place(self, feature: Dict[str, Any]) -> Dict[str, Any]:
        """Build place object with semantic references."""
        geometry = feature.get("geometry", {})
        coords = geometry.get("coordinates", [])
        
        return {
            "type": "Point",
            "coordinates": coords if geometry.get("type") == "Point" else coords[0],
            "vocab": {
                "location": "http://www.opengis.net/ont/sf#Point"
            }
        }
    
    def convert_collection(self, geojson_collection: Dict[str, Any]) -> Dict[str, Any]:
        """Convert GeoJSON FeatureCollection to JSON-FG collection."""
        return {
            "type": "FeatureCollection",
            "@context": [
                "https://geojson.org/geojson-ld/geojson-context.jsonld",
                self.context_url
            ],
            "features": [
                self.convert(feature) 
                for feature in geojson_collection.get("features", [])
            ]
        }
```

## Usage Examples

### Command Line
```bash
# Convert single GeoJSON file to JSON-FG
python geojson_to_jsonfg.py input.geojson output.jsonfg --context context.jsonld

# Convert with OIM observations
python geojson_to_jsonfg.py observations.geojson obs.jsonfg --oim-obs
```

### Python API
```python
from converter import GeoJSONtoJSONFGConverter

converter = GeoJSONtoJSONFGConverter(context_url="path/to/context.jsonld")
jsonfg_feature = converter.convert(geojson_feature)
jsonfg_collection = converter.convert_collection(geojson_featurecollection)
```

## Validation

After conversion, validate against:
1. JSON-FG schema: https://raw.githubusercontent.com/opengeospatial/ogc-features-and-geometries/main/json-fg/spec/schema.json
2. OIM context: verify all properties have OIM semantic mappings
3. Example compliance: test features conform to target OIM building block schema

## Dependencies

- `ogc.hosted.iliad.api.features.oim` - Core OIM semantics
- `ogc.hosted.iliad.api.features.oim-bio-tdwg` - Biological data mappings
- `ogc.hosted.iliad.api.features.oim-obs` - Observation properties (SOSA)
- `ogc.geo.json-fg.feature` - JSON-FG feature specification

## References

- [OGC JSON-FG Specification](https://docs.opengeospatial.org/is/21-017/21-017.html)
- [ILIAD OIM Repository](https://github.com/ILIAD-ocean-twin/OIM)
- [GeoJSON-LD](https://geojson.org/geojson-ld/)
