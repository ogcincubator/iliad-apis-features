---
name: web-browsing-mcp
description: Use for HTTP fetches and API browsing during data discovery — marine data catalogues, vocabulary services (NERC, CF, Darwin Core, OBIS, ICES), and OGC service endpoints. Returns executed URLs for provenance. Use for any task requiring web-based data retrieval, API calls, or vocabulary lookups from authoritative marine sources.
---

# Web Browsing MCP Skill

## Overview

Use this skill when you need to browse websites, access APIs, or fetch web-based data as part of data collection tasks, such as querying marine data catalogues or general web scraping.

## Capabilities

- Browse web pages and extract content.
- Execute HTTP GET/POST requests to APIs.
- Handle authentication (e.g., API keys, OAuth) for protected endpoints.
- Parse JSON/XML responses from web services.
- Follow redirects and handle cookies for session-based browsing.
- Return all executed URLs, including query parameters and request bodies, for provenance tracking.

## Inputs

- `url`: Target URL or API endpoint
- `method`: GET | POST
- `headers`: optional request headers (auth tokens, content-type)
- `params`: optional query parameters
- `body`: optional POST body

## Usage Instructions

1. Identify the target URL or API endpoint.
2. Specify the request method (GET, POST, etc.) and any required parameters.
3. Use MCP server tools like `fetch_webpage` or `run_api_call` to execute the request.
4. Process the response data, extracting relevant information.
5. Handle errors gracefully, such as rate limits or network issues.

## Best Practices

- Respect robots.txt and terms of service for websites.
- Use appropriate user agents to avoid blocking.
- Cache responses when possible to reduce API calls.
- Validate data integrity after retrieval.

## Integration with Agents

Particularly useful for the `marine-data-agent` for discovering and validating authoritative vocabularies and data services.

- When searching for vocabulary references, prioritize queries to NERC (vocab.nerc.ac.uk), CF Convention, Darwin Core (tdwg.org), OBIS, ICES vocabulary services, and EMODnet.
- This skill returns executed URLs and response payloads for provenance tracking and vocabulary lookup; it supports the calling agent in building complete JSON-LD contexts.