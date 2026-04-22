---
name: lifewatch-data-service
description: Use when querying the LifeWatch Data Service API / Data Explorer for biodiversity, environmental, or tracking datasets. Prompts the user to select one of the available datasets, asks only for the parameters needed for that dataset, checks the workspace root .env for LifeWatch credentials or API key settings, and maps the selected parameters programmatically to the LifeWatch API.
---

# LifeWatch Data Service Skill

Use this skill when querying the LifeWatch Data Service API / Data Explorer.

Core behavior:

- prompt the user to select one of the available datasets
- prompt only for the parameters required by that dataset
- check the workspace root `.env` for `LIFEWATCH_API_KEY`, `LIFEWATCH_DATA_API_KEY`, `LIFEWATCH_API_TOKEN`, `LIFEWATCH_USERNAME`, `LIFEWATCH_PASSWORD`, `LIFEWATCH_BASE_URL`, or `BASE_PATH`
- if the needed API key or credentials are not in `.env`, ask the user where to get them from or ask them to provide them
- map the selected parameters programmatically to the LifeWatch API payload
- execute the request and return the executed endpoint plus request payload for provenance

Available dataset choices:

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

Use the helper script:

```bash
python3 .claude/skills/lifewatch-data-service/scripts/query_lifewatch_api.py --list-datasets
```

Query example:

```bash
python3 .claude/skills/lifewatch-data-service/scripts/query_lifewatch_api.py \
  --workspace-root /path/to/workspace \
  --dataset station \
  --param startdate=2024-01-01 \
  --param stopdate=2024-01-31 \
  --param stations=all \
  --param categories=all
```

Discovery helpers:

- `etn`: `--list-options etn`
- `mvb`: `--list-options mvb`
- `uva-bird`: `--list-options uva-bird`

For missing API key, ask:

`I couldn't find a LifeWatch API key in the workspace root .env file. Where should I read it from, or would you like to provide it now?`
