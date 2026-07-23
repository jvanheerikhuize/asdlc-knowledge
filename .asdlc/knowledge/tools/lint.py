"""Deterministic health checks — the enforceable half of fact-checking.

Reports (and, with --strict, fails CI on) schema violations, orphan pages,
broken wikilinks, unsourced claims, stale pages, and confidence-cap breaches.
Claim-level truth is an agent job (see verify.py); this guarantees the
*structural* invariants that make the confidence numbers meaningful.
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

from _common import KB_ROOT, iter_pages, load_manifest, parse_page

try:
    from jsonschema import Draft202012Validator
    HAVE_JSONSCHEMA = True
except ImportError:
    HAVE_JSONSCHEMA = False


def _today() -> dt.date:
    return dt.date.today()


def _parse_date(v) -> dt.date | None:
    try:
        return dt.date.fromisoformat(str(v))
    except (ValueError, TypeError):
        return None


def run(strict: bool = False) -> int:
    m = load_manifest()
    cfg = m["lint"]
    pol = m["confidence_policy"]
    pages = list(iter_pages(m))
    ids = {p.id for p in pages}
    findings: list[str] = []

    # inbound link map (for orphan detection)
    inbound: dict[str, int] = {p.id: 0 for p in pages}
    for p in pages:
        for target in p.links():
            if target in inbound:
                inbound[target] += 1

    # schema
    validator = None
    if cfg.get("frontmatter_schema") and HAVE_JSONSCHEMA:
        schema = __import__("json").loads(
            (KB_ROOT / m["paths"]["schema"] / "frontmatter.schema.json").read_text())
        validator = Draft202012Validator(schema)

    for p in pages:
        rel = p.path.relative_to(KB_ROOT)
        fm = p.frontmatter

        if validator is not None:
            for err in validator.iter_errors(fm):
                findings.append(f"[schema] {rel}: {err.message}")

        if cfg.get("broken_links"):
            for target in p.links():
                if target not in ids:
                    findings.append(f"[broken-link] {rel}: [[{target}]] -> no such page")

        if cfg.get("orphan_pages") and inbound.get(p.id, 0) == 0 and p.id != "index":
            findings.append(f"[orphan] {rel}: no inbound [[wikilinks]]")

        conf = fm.get("confidence")
        srcs = fm.get("sources") or []
        if cfg.get("unsourced_claims") and p.type != "source" and not srcs:
            findings.append(f"[unsourced] {rel}: non-source page with empty sources[]")

        if cfg.get("confidence_cap") and not srcs and isinstance(conf, (int, float)):
            cap = pol["unsourced_confidence_cap"]
            if conf > cap:
                findings.append(
                    f"[confidence-cap] {rel}: confidence {conf} exceeds unsourced cap {cap}")

        if cfg.get("stale_pages"):
            updated = _parse_date(fm.get("updated"))
            lv = _parse_date(fm.get("last_verified"))
            if updated and (_today() - updated).days > pol["stale_after_days"] and not lv:
                findings.append(f"[stale] {rel}: unverified and untouched > "
                                f"{pol['stale_after_days']}d")
            if fm.get("status") == "verified":
                if not lv:
                    findings.append(f"[verify] {rel}: status=verified but no last_verified")
                elif (_today() - lv).days > pol["verified_max_age_days"]:
                    findings.append(f"[verify] {rel}: verification older than "
                                    f"{pol['verified_max_age_days']}d")

    if not HAVE_JSONSCHEMA and cfg.get("frontmatter_schema"):
        findings.append("[info] jsonschema not installed — schema check skipped "
                        "(`pip install jsonschema` to enable)")

    for f in findings:
        print(f)
    hard = [f for f in findings if not f.startswith("[info]")]
    print(f"\n{len(pages)} pages checked, {len(hard)} issue(s).")
    return 1 if (strict and hard) else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="exit non-zero on issues (CI)")
    sys.exit(run(**vars(ap.parse_args())))
