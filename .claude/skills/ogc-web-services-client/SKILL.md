---
name: ogc-web-services-client
description: Use whenever the task involves querying OGC web services (WMS, WFS, WMTS, CSW, OGC API). Handles GetCapabilities, GetMap, GetFeature, bbox/CRS parameters, and returns executed URLs for provenance. Ideal for marine data agent tasks accessing HELCOM, EMODnet, ICES, and other OGC-compliant geospatial services.
---

# OGC Web Services Client MCP Skill

## Overview

Use this skill for interacting with OGC-compliant services like WMS (Web Map Service), WFS (Web Feature Service), WMTS (Web Map Tile Service), and others, commonly used in geospatial data platforms.

## Capabilities

- Connect to OGC service endpoints and retrieve capabilities documents.
- Execute GetMap, GetFeature, and other OGC requests.
- Handle spatial queries with bounding boxes, filters, and coordinate systems.
- Parse GML, GeoJSON, and other geospatial formats.
- Support for authentication and proxy configurations.
- Return all executed OGC service URLs, including parameters (e.g., SERVICE=WFS, REQUEST=GetFeature, BBOX=...), for provenance tracking.

## Inputs

- `service_url`: OGC endpoint URL (e.g., from a catalog like HELCOM)
- `request_type`: GetCapabilities | GetMap | GetFeature | GetTile
- `bbox`: optional bounding box [minx, miny, maxx, maxy]
- `layer` or `typeName`: target layer/feature type
- `crs`: coordinate reference system (default EPSG:4326)
- `output_format`: GeoJSON | GML | application/json

## Usage Instructions

1. Obtain the OGC service URL (e.g., from a catalog like HELCOM).
2. Query the capabilities to understand available layers and operations.
3. Construct requests with appropriate parameters (e.g., bbox for spatial filtering).
4. Use MCP server tools to send requests and receive responses.
5. Process geospatial data, converting to desired formats if needed.

## Best Practices

- Use standard OGC versions (e.g., 1.1.1 or 2.0) for compatibility.
- Optimize requests to avoid large data transfers (e.g., use sampling for big datasets).
- Handle coordinate reference systems (CRS) conversions.
- Respect service usage policies and rate limits.

## Integration with Agents

Ideal for the `marine-data-agent` to access geospatial data services and discover relevant vocabulary and metadata standards.

- Retrieved data should be documented with property-to-vocabulary mappings to support context construction.
- This skill returns executed OGC query URLs, retrieved data, and metadata; it supports building complete JSON-LD contexts with authoritative vocabulary references.
