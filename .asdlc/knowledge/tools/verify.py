"""Fact-check scaffolding: assemble a page's claims next to its cited sources.

Truth is an agent judgement, so this tool does the *bookkeeping* around it:
  - loads a wiki page and every source it cites (from wiki/sources/ -> raw/)
  - prints an inspection report the agent (or a human) checks claim-by-claim
  - enforces the scoring caps from manifest.yaml so a "verified" stamp can't
    lie about coverage.

Usage:
  python tools/kb.py verify <page-id>      one page + its sources, for fact-checking
  python tools/kb.py verify --all [--strict]  sweep every page's verification health
"""
from __future__ import annotations

import datetime as dt
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


def _parse_date(v):
    try:
        return dt.date.fromisoformat(str(v))
    except (ValueError, TypeError):
        return None


# Sweep states, ordered most-actionable first. The first four mirror the failures
# `kb lint --strict` already gates on; `unverified`/`ok` are informational.
_ORDER = ["reverify", "no-date", "stale", "unsourced", "unverified", "ok"]
_ATTENTION = {"reverify", "no-date", "stale", "unsourced"}


def _page_state(page, pol, today):
    """Classify one page's verification health -> (state, human note)."""
    fm = page.frontmatter
    status = fm.get("status")
    srcs = fm.get("sources") or []
    lv = _parse_date(fm.get("last_verified"))
    updated = _parse_date(fm.get("updated"))

    if page.type != "source" and not srcs:
        return "unsourced", "no sources cited — cannot be verified"
    if status == "verified":
        if lv is None:
            return "no-date", "status=verified but no last_verified date"
        age = (today - lv).days
        if age > pol["verified_max_age_days"]:
            return "reverify", f"verified {age}d ago (> {pol['verified_max_age_days']}d)"
        return "ok", f"verified {age}d ago"
    if updated and lv is None and (today - updated).days > pol["stale_after_days"]:
        return "stale", f"untouched {(today - updated).days}d, never verified"
    return "unverified", f"status={status or '?'}, not yet verified"


def run_all(strict: bool = False) -> int:
    """Sweep every page's verification health, most-actionable first.

    Complements the pass/fail `kb lint`: this is the triage view a human or agent
    reads to see *which* pages to re-verify next. `--strict` exits non-zero when
    any page needs attention, so a scheduled run can flag drift over time.
    """
    m = load_manifest()
    pol = m["confidence_policy"]
    today = dt.date.today()

    rows = []
    for p in iter_pages():
        state, note = _page_state(p, pol, today)
        rows.append((state, p.id, note))
    rows.sort(key=lambda r: (_ORDER.index(r[0]), r[1]))

    print(f"# Verify sweep — {len(rows)} pages\n")
    for state, pid, note in rows:
        print(f"{state:<10} {pid:<34} {note}")

    counts = {s: sum(1 for r in rows if r[0] == s) for s in _ORDER}
    summary = ", ".join(f"{counts[s]} {s}" for s in _ORDER if counts[s])
    attention = sum(counts[s] for s in _ATTENTION)
    print(f"\nsummary: {summary}  ({attention} need attention)")

    if strict and attention:
        print(f"\nFAIL: {attention} page(s) need attention (--strict).", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--all" in args:
        sys.exit(run_all(strict="--strict" in args))
    if not args:
        print("usage: verify.py <page-id> | verify.py --all [--strict]", file=sys.stderr)
        sys.exit(2)
    sys.exit(run(args[0]))
