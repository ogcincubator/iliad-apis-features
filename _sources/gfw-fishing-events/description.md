# Global Fishing Watch Gulf of Gdansk Fishing Events

This building block captures the structure of a recent sample returned by the Global Fishing Watch Events API for apparent fishing activity. Examples are from the Gulf of Gdansk.

The current example payload reflects a polygon-filtered query against:

- `POST https://gateway.api.globalfishingwatch.org/v3/events?limit=50&offset=0&sort=-start`
- dataset `public-global-fishing-events:latest`
- date range `2026-04-14` to `2026-04-19`
- polygon `[[[18.0,54.2],[20.2,54.2],[20.2,55.2],[18.0,55.2],[18.0,54.2]]]`
- response sample size `50` events from `136` total matches

The schema covers:

- top-level response metadata
- paged event collections
- event timing and position
- region memberships
- vessel identity summary
- fishing-specific distance and risk metrics

The example payload is intended as a source-level schema seed for downstream profiling and interoperability work. The example provenance is also recorded in `examples.yaml`, including the exact request URL and request body used by the `global-fishing-watch-data-service` retriever skill.
