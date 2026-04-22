---
name: lifewatch-data-service
description: Use when querying the LifeWatch Data Service API / Data Explorer for biodiversity, environmental, or tracking datasets. Prompts the user to select one of the available datasets, asks only for the parameters needed for that dataset, checks the workspace root .env for LifeWatch credentials or API key settings, and maps the selected parameters programmatically to the LifeWatch API.
---

# LifeWatch Data Service Skill

## Purpose

Query the LifeWatch Data Service programmatically, with dataset-aware prompting and parameter mapping.

Use this skill to:

- list available LifeWatch datasets
- ask the user to choose one dataset before querying
- ask only for the parameters needed by that dataset
- check the workspace root `.env` for LifeWatch credentials or API settings
- call the API programmatically and return the executed URL and payload for provenance

## Activation

Use this skill when the user asks to:

- query LifeWatch data
- browse available LifeWatch datasets
- retrieve LifeWatch observations, station data, ETN data, buoy data, or similar
- build a LifeWatch API request from user inputs

Do not use this skill for:

- generic CSV metadata generation
- non-LifeWatch web APIs
- OGC WMS/WFS endpoints unless the user explicitly switches to those services

## Supported Dataset Choices

Start by presenting the available dataset choices and asking the user to select one:

- `buoy`
- `station`
- `underway`
- `etn`
- `cpod`
- `mvb`
- `uva-bird`
- `bats`
- `flowcam`
- `zooscan`
- `ctd`

Use the helper script when possible:

```bash
python3 .claude/skills/lifewatch-data-service/scripts/query_lifewatch_api.py --list-datasets
```

## Required Interaction Pattern

Always follow this sequence:

1. determine the workspace root
2. check for `.env` in that root
3. inspect available LifeWatch auth settings
4. present dataset choices if the user did not already pick one
5. ask for only the parameters needed for the selected dataset
6. map the answers to the API payload
7. execute the API call programmatically
8. return the result together with the executed endpoint and payload

## Authentication Rules

First check the workspace root `.env` for any of these keys:

- `LIFEWATCH_API_KEY`
- `LIFEWATCH_DATA_API_KEY`
- `LIFEWATCH_API_TOKEN`
- `LIFEWATCH_USERNAME`
- `LIFEWATCH_PASSWORD`
- `LIFEWATCH_BASE_URL`
- `BASE_PATH`

If the needed credentials are not present, ask the user.

If an API key is missing, ask:

`I couldn't find a LifeWatch API key in the workspace root .env file. Where should I read it from, or would you like to provide it now?`

If the selected dataset is one of the restricted datasets that commonly uses user credentials, also ask for username and password when missing.

Do not fabricate credentials or assume hidden defaults beyond the documented endpoint base URL.

## Dataset-Specific Parameter Rules

Ask only for the parameters needed by the selected dataset.

### Common parameters

Most datasets need:

- `startdate`
- `stopdate`

### Dataset-specific prompts

- `buoy`: ask for `stations` if the user did not specify them
- `station`: ask for `stations` and `categories`
- `underway`: ask for `by`
- `etn`: ask for `action`, `by`, `networks`, `projects`
- `cpod`: ask for `processing`, optional `quality`, and `by`
- `mvb`: ask for `stations`, `parameters`, `by`, `calc`
- `uva-bird`: ask for tag or project filters when needed
- `bats`: ask for binning and available filters when needed
- `flowcam`: ask for project or filter parameters when needed
- `zooscan`: ask for taxonomy or filter parameters when needed
- `ctd`: ask for `stations` and `by`

If the API exposes a supporting list endpoint, use it to help the user choose valid values:

- `etn`: use `listEtnProjects`
- `mvb`: use `listMvbStations`
- `uva-bird`: use `listUvaTags`

## Programmatic Mapping

Use the helper script to build the payload and execute the API request:

```bash
python3 .claude/skills/lifewatch-data-service/scripts/query_lifewatch_api.py \
  --workspace-root /path/to/workspace \
  --dataset station \
  --param startdate=2024-01-01 \
  --param stopdate=2024-01-31 \
  --param stations=all \
  --param categories=all
```

The script maps friendly dataset names to the LifeWatch API payload fields and posts to the OpenCPU endpoint.

Default base endpoint:

`https://opencpu.lifewatch.be/library/lwdataserver/R/getLWdata/json`

If `BASE_PATH` or `LIFEWATCH_BASE_URL` is set, prefer that instead.

## Output Contract

Always report:

- selected dataset
- prompted parameters
- values supplied by the user
- values sourced from `.env`
- executed endpoint URL
- executed request payload
- whether theme-specific or restricted access limitations may apply

When the API response includes applied server parameters, surface them because LifeWatch may coerce restricted queries.

## Notes

- Some LifeWatch datasets are open, while others are partially restricted or moratorium-protected.
- The LifeWatch Data Explorer / `lwdataexplorer` documentation shows dataset-specific parameter sets and an OpenCPU-backed request flow.
- The helper script is intentionally conservative: it knows the common datasets and core parameters, and can be extended as new dataset variants are needed.

## References

- LifeWatch Data Explorer package overview: https://lifewatch.github.io/lwdataexplorer/
- LifeWatch helper source showing default OpenCPU base path: https://rdrr.io/github/lifewatch/lwdataexplorer/src/R/helpers.R
- ETN dataset reference: https://lifewatch.github.io/lwdataexplorer/reference/getEtnData.html
- Station dataset reference: https://lifewatch.github.io/lwdataexplorer/reference/getStationData.html
