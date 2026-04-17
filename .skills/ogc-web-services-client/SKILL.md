# OGC Web Services Client MCP Skill

This skill provides client capabilities for OGC (Open Geospatial Consortium) web services using MCP servers to execute API commands for geospatial data access.

## Overview
Use this skill for interacting with OGC-compliant services like WMS (Web Map Service), WFS (Web Feature Service), WMTS (Web Map Tile Service), and others, commonly used in geospatial data platforms.

## Capabilities
- Connect to OGC service endpoints and retrieve capabilities documents.
- Execute GetMap, GetFeature, and other OGC requests.
- Handle spatial queries with bounding boxes, filters, and coordinate systems.
- Parse GML, GeoJSON, and other geospatial formats.
- Support for authentication and proxy configurations.
- Return all executed OGC service URLs, including parameters (e.g., SERVICE=WFS, REQUEST=GetFeature, BBOX=...), for provenance tracking.

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
Ideal for the marine data agent to access geospatial data services and discover relevant vocabulary and metadata standards.
- Retrieved data should be documented with property-to-vocabulary mappings to support context construction.
- This skill returns executed OGC query URLs, retrieved data, and metadata; it supports building complete JSON-LD contexts with authoritative vocabulary references.
