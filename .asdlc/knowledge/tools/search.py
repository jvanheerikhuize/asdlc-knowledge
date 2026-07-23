"""kb search <term> — ranked grep over frontmatter + body.

The CLI half of the `query` verb in AGENTS.md: instead of an agent ad-hoc
grepping wiki/, this scores every page by where the term hits (id/title
weigh more than a body mention) and prints ranked results with a matching
excerpt, so an agent can jump straight to the relevant pages.

Usage: python tools/kb.py search <term>
"""
from __future__ import annotations

import re
import sys

from _common import iter_pages

ID_WEIGHT = 5
TITLE_WEIGHT = 3
FRONTMATTER_WEIGHT = 2
BODY_WEIGHT = 1
EXCERPT_RADIUS = 40


def _excerpt(text: str, term: str) -> str | None:
    m = re.search(re.escape(term), text, re.IGNORECASE)
    if not m:
        return None
    start = max(0, m.start() - EXCERPT_RADIUS)
    end = min(len(text), m.end() + EXCERPT_RADIUS)
    snippet = " ".join(text[start:end].split())
    prefix = "…" if start > 0 else ""
    suffix = "…" if end < len(text) else ""
    return f"{prefix}{snippet}{suffix}"


def _score(page, term: str) -> tuple[int, str | None]:
    pattern = re.compile(re.escape(term), re.IGNORECASE)
    score = 0
    excerpt = None

    if pattern.search(page.id):
        score += ID_WEIGHT
    title = str(page.frontmatter.get("title", ""))
    if pattern.search(title):
        score += TITLE_WEIGHT
        excerpt = excerpt or _excerpt(title, term)

    for key, value in page.frontmatter.items():
        if key in ("id", "title"):
            continue
        text = " ".join(value) if isinstance(value, list) else str(value)
        hits = len(pattern.findall(text))
        if hits:
            score += FRONTMATTER_WEIGHT * hits
            excerpt = excerpt or _excerpt(text, term)

    body_hits = len(pattern.findall(page.body))
    if body_hits:
        score += BODY_WEIGHT * body_hits
        excerpt = excerpt or _excerpt(page.body, term)

    return score, excerpt


def run(term: str) -> int:
    if not term:
        print("usage: kb search <term>", file=sys.stderr)
        return 2

    results = []
    for page in iter_pages():
        score, excerpt = _score(page, term)
        if score > 0:
            results.append((score, page, excerpt))

    if not results:
        print(f"no matches for '{term}'")
        return 0

    results.sort(key=lambda r: r[0], reverse=True)
    for score, page, excerpt in results:
        title = page.frontmatter.get("title", page.id)
        line = f"{page.id}  ({title}, score={score})"
        if excerpt:
            line += f"\n    {excerpt}"
        print(line)
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: search.py <term>", file=sys.stderr)
        sys.exit(2)
    sys.exit(run(" ".join(sys.argv[1:])))
