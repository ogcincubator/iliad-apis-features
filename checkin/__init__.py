"""ILIAD check-in tool."""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = REPO_ROOT / "_sources"
STAGING_DIR = SOURCES_DIR / "_staging"
OIM_DIR = REPO_ROOT.parent / "OIM"
TRANSFORMERS_DIR = Path(__file__).resolve().parent / "transformers"
