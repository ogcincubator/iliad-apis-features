---
name: esri-client
description: Use when the task involves ArcGIS REST services (FeatureServer, MapServer, ImageServer). Builds queries with where/outFields/bbox, handles tokens, and returns executed URLs for provenance. Use when marine or coastal data providers expose data via ArcGIS Online or ArcGIS Server.
---

# ESRI Client MCP Skill

## Overview

Use this skill for accessing ArcGIS Online, ArcGIS Server, or Enterprise services, including feature services, map services, and image services.

## Capabilities

- Query ArcGIS REST API endpoints for data retrieval.
- Execute spatial queries, filters, and aggregations.
- Access map tiles, features, and imagery.
- Handle authentication via tokens or OAuth.
- Parse EsriJSON, GeoJSON, and other formats.
- Return all executed ArcGIS REST URLs, including parameters (e.g., /query?where=...&outFields=...), for provenance tracking.

## Inputs

- `service_url`: ArcGIS REST service URL (FeatureServer, MapServer, ImageServer)
- `operation`: query | identify | find
- `where`: SQL-like where clause for filtering features
- `outFields`: comma-separated list of fields to return (default: *)
- `bbox`: optional spatial filter [minx, miny, maxx, maxy]
- `token`: optional ArcGIS authentication token
- `output_format`: GeoJSON | EsriJSON (default: GeoJSON)

## Usage Instructions

1. Identify the ArcGIS service URL or portal.
2. Authenticate if required (e.g., obtain access token).
3. Construct API requests for specific operations (e.g., query features within a bbox).
4. Use MCP server tools to execute HTTP requests to ArcGIS APIs.
5. Process returned data, handling pagination for large result sets.

## Best Practices

- Use ArcGIS API for JavaScript or REST API standards.
- Optimize queries to minimize data volume (e.g., use outFields and where clauses).
- Handle spatial references and projections.
- Comply with ESRI terms of service and usage limits.

## Integration with Agents

Useful for the `marine-data-agent` if ESRI services are part of the data sources, providing access to ArcGIS-hosted geospatial data.

- Retrieved data should include documentation of property semantics and available vocabulary references if available.
- This skill returns executed ArcGIS REST URLs and retrieved data; it supports the calling agent in constructing complete JSON-LD contexts with proper vocabulary annotations.