"""Fact-check scaffolding: assemble a page's claims next to its cited sources.

Truth is an agent judgement, so this tool does the *bookkeeping* around it:
  - loads a wiki page and every source it cites (from wiki/sources/ -> raw/)
  - prints an inspection report the agent (or a human) checks claim-by-claim
  - enforces the scoring caps from manifest.yaml so a "verified" stamp can't
    lie about coverage.

Usage: python tools/kb.py verify <page-id>
"""
from __future__ import annotations

import sys

from _common import KB_ROOT, iter_pages, load_manifest, parse_page


def find_page(page_id: str):
    for p in iter_pages():
        if p.id == page_id:
            return p
    return None


def run(page_id: str) -> int:
    m = load_manifest()
    page = find_page(page_id)
    if page is None:
        print(f"no page with id '{page_id}'", file=sys.stderr)
        return 2

    print(f"# Verify: {page.id}\n")
    print(f"status={page.frontmatter.get('status')}  "
          f"confidence={page.frontmatter.get('confidence')}  "
          f"last_verified={page.frontmatter.get('last_verified')}\n")

    srcs = page.frontmatter.get("sources") or []
    if not srcs:
        cap = m["confidence_policy"]["unsourced_confidence_cap"]
        print(f"!! No sources cited. Confidence must be <= {cap}. "
              f"Cannot be marked 'verified'.\n")

    print("## Cited sources")
    src_pages = {p.id: p for p in iter_pages() if p.type == "source"}
    for sid in srcs:
        sp = src_pages.get(sid)
        if sp is None:
            print(f"- [[{sid}]] -- MISSING source page!")
            continue
        origin = sp.frontmatter.get("origin", "?")
        print(f"- [[{sid}]] origin={origin}")

    print("\n## Checklist for the agent")
    print("1. Read each cited source above from raw/.")
    print("2. For every claim on this page, confirm a source supports it.")
    print("3. Annotate unsupported claims; move them out or lower confidence.")
    print("4. Set confidence per the rubric in AGENTS.md sec.5 (respect caps).")
    print("5. If all claims hold: set status=verified, last_verified=today.")
    print("6. Append a `verify` line to log.md.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: verify.py <page-id>", file=sys.stderr)
        sys.exit(2)
    sys.exit(run(sys.argv[1]))
