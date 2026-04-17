# ESRI Client MCP Skill

This skill enables interaction with ESRI ArcGIS services using MCP servers to execute API commands for geospatial data and mapping.

## Overview
Use this skill for accessing ArcGIS Online, ArcGIS Server, or Enterprise services, including feature services, map services, and image services.

## Capabilities
- Query ArcGIS REST API endpoints for data retrieval.
- Execute spatial queries, filters, and aggregations.
- Access map tiles, features, and imagery.
- Handle authentication via tokens or OAuth.
- Parse EsriJSON, GeoJSON, and other formats.
- Return all executed ArcGIS REST URLs, including parameters (e.g., /query?where=...&outFields=...), for provenance tracking.

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
Useful for the marine data agent if ESRI services are part of the data sources, providing access to ArcGIS-hosted geospatial data.
- Retrieved data should include documentation of property semantics and available vocabulary references if available.
- This skill returns executed ArcGIS REST URLs and retrieved data; it supports the calling agent in constructing complete JSON-LD contexts with proper vocabulary annotations.
