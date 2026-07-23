"""Shared helpers: locate the KB root, load the manifest, parse frontmatter.

Only dependency is PyYAML. Everything else is stdlib so the KB stays
"no infra": a checkout + Python is enough to scaffold, lint, and score.
"""
from __future__ import annotations

import datetime
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

# tools/ lives directly under the KB root (.asdlc/knowledge/).
KB_ROOT = Path(__file__).resolve().parent.parent
MANIFEST = KB_ROOT / "manifest.yaml"

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")


def load_manifest() -> dict[str, Any]:
    with MANIFEST.open() as fh:
        return yaml.safe_load(fh)


@dataclass
class Page:
    path: Path
    frontmatter: dict[str, Any]
    body: str

    @property
    def id(self) -> str:
        return self.frontmatter.get("id", self.path.stem)

    @property
    def type(self) -> str:
        return self.frontmatter.get("type", "")

    def links(self) -> list[str]:
        return WIKILINK_RE.findall(self.body)


def _coerce_dates(value):
    """YAML parses ISO dates into date objects; the schema (and JSON) want
    strings. Normalise date/datetime back to ISO-8601 strings recursively."""
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: _coerce_dates(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_coerce_dates(v) for v in value]
    return value


def parse_page(path: Path) -> Page:
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        return Page(path=path, frontmatter={}, body=text)
    fm = _coerce_dates(yaml.safe_load(m.group(1)) or {})
    return Page(path=path, frontmatter=fm, body=m.group(2))


def wiki_dir() -> Path:
    return KB_ROOT / load_manifest()["paths"]["wiki"]


def iter_pages(manifest: dict | None = None):
    """Yield every markdown page under wiki/."""
    manifest = manifest or load_manifest()
    root = KB_ROOT / manifest["paths"]["wiki"]
    for p in sorted(root.rglob("*.md")):
        # Skip generated artifacts (e.g. _graph.md) — they are views, not pages.
        if p.name.startswith("_"):
            continue
        yield parse_page(p)


def confidence_band(value: float, manifest: dict) -> str:
    for band in manifest["confidence_policy"]["bands"]:
        if value >= band["min"]:
            return band["label"]
    return "low"
