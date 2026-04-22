# Global Fishing Watch Gulf of Gdansk Fishing Events

This building block captures the structure of a recent sample returned by the Global Fishing Watch Events API for apparent fishing activity. Examples are from the Gulf of Gdansk.

The sample reflects a polygon-filtered query against:

- `POST /v3/events`
- dataset `public-global-fishing-events:latest`
- date range `2026-04-14` to `2026-04-19`

The schema covers:

- top-level response metadata
- paged event collections
- event timing and position
- region memberships
- vessel identity summary
- fishing-specific distance and risk metrics

The example payload is intended as a source-level schema seed for downstream profiling and interoperability work.
