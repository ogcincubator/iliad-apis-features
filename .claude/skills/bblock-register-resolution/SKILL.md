---
name: bblock-register-resolution
description: Use when resolving OGC Building Block dependencies or repository imports from a published URL. Normalizes a human-facing site URL to machine-readable register endpoints by trying `<url>/build/register.json` first, then `<url>/register.json`, and only treating the base URL as documentation unless it already returns JSON.
---

# Building Block Register Resolution Skill

Use this skill when a building block dependency, `imports:` entry, or external bblock reference is given as a site URL and you need the actual machine-readable register.

## Resolution Order

Given a base URL `u`:

1. Normalize by removing a trailing slash for testing, then reconstruct candidate URLs.
2. Try `u/build/register.json`.
3. Try `u/register.json`.
4. Only use `u` directly if it already returns JSON.

For each candidate:

- Prefer `HEAD` or `GET` checks.
- Treat it as valid when it returns `200` and `Content-Type` includes `application/json`.
- Do not assume `Accept: application/json` on the base URL will work; GitHub Pages sites often still return HTML.

## Expected Output

Return:

- the original URL
- the resolved register URL
- the check performed
- whether JSON was confirmed

Example:

- input: `https://ogcincubator.github.io/bblocks-openscience/`
- resolved: `https://ogcincubator.github.io/bblocks-openscience/build/register.json`

## When To Apply

- `Invalid reference to bblock ... perhaps an import is missing?`
- adding or fixing `bblocks-config.yaml` `imports:`
- resolving remote dependencies for validation
- mapping user-provided documentation URLs to actual bblock registers

## Notes

- Prefer explicit JSON register URLs in machine-facing config.
- Keep the human-facing site URL only for documentation or provenance.
- If both `/build/register.json` and `/register.json` fail, report that clearly rather than guessing.
