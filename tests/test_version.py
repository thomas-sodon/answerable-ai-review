"""The version is declared in three places that must agree.

release-please bumps all of them in its release PR; this catches a hand edit
that misses one, which would otherwise release the wrong number.
"""

from __future__ import annotations

import json
import tomllib
from pathlib import Path

import answerable

ROOT = Path(__file__).resolve().parent.parent


def test_versions_agree() -> None:
    pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]["version"]
    manifest = json.loads((ROOT / ".release-please-manifest.json").read_text())["."]
    assert answerable.__version__ == pyproject == manifest
