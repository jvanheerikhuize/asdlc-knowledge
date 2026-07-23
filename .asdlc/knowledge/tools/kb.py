#!/usr/bin/env python3
"""kb — the single CLI to interact with the knowledge base.

    kb scaffold          regenerate structure from manifest.yaml
    kb new <type> <id>   stamp a page from _templates/<type>.md (--title "...")
    kb ingest            batch-ingest every file dropped in inbox/
    kb ingest <path>     convert one raw file and scaffold a source page
    kb lint [--strict]   run deterministic health checks
    kb verify <page-id>  assemble a page + its sources for fact-checking
    kb viz               regenerate mkdocs.yml + the Mermaid graph
    kb index             rebuild index.md from wiki/ frontmatter
    kb purge [--raw|--wiki] [--yes]
                         empty the KB back to a clean state (dry-run without --yes)

This is the interaction interface for humans and agents alike; the agent's
prose contract lives next to it in AGENTS.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Make sibling tool modules and the KB package importable regardless of cwd.
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))


def cmd_index() -> int:
    """Rebuild the per-category lists in index.md from wiki frontmatter."""
    import re
    from _common import KB_ROOT, confidence_band, iter_pages, load_manifest
    m = load_manifest()
    buckets: dict[str, list[str]] = {t: [] for t in m["page_types"]}
    for p in iter_pages(m):
        if p.type not in buckets:
            continue
        conf = float(p.frontmatter.get("confidence", 0.0) or 0.0)
        band = confidence_band(conf, m)
        title = p.frontmatter.get("title", p.id)
        desc = (p.body.strip().splitlines() or [""])
        summary = next((l.lstrip("> ").strip() for l in desc if l.strip()
                        and not l.startswith("#")), "")
        buckets[p.type].append(f"- [[{p.id}]] — {summary[:70] or title} · **{band}**")
    idx = KB_ROOT / m["paths"]["index"]
    text = idx.read_text()
    for tname, tspec in m["page_types"].items():
        folder = tspec["folder"]
        block = "\n".join(buckets[tname]) or "- _(none yet)_"
        text = re.sub(
            rf"(<!-- kb:{folder}:start -->\n).*?(\n<!-- kb:{folder}:end -->)",
            rf"\1{block}\2", text, flags=re.DOTALL)
    idx.write_text(text)
    print(f"rebuilt {idx.relative_to(KB_ROOT)}")
    return 0


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 0
    cmd, rest = argv[0], argv[1:]
    if cmd == "scaffold":
        import scaffold
        return scaffold.main()
    if cmd == "new":
        import new
        if len(rest) < 2:
            print("usage: kb new <type> <id> [--title \"...\"]", file=sys.stderr)
            return 2
        type_, id_ = rest[0], rest[1]
        rest = rest[2:]
        title = None
        if "--title" in rest:
            i = rest.index("--title")
            title = rest[i + 1]
        return new.run(type_, id_, title=title)
    if cmd == "lint":
        import lint
        return lint.run(strict="--strict" in rest)
    if cmd == "viz":
        import viz
        return viz.main()
    if cmd == "index":
        return cmd_index()
    if cmd == "ingest":
        import ingest_cmd as ingest
        ns = {"path": None, "adapter": None}
        if "--adapter" in rest:
            i = rest.index("--adapter")
            ns["adapter"] = rest[i + 1]
            rest = rest[:i] + rest[i + 2:]
        if rest:                       # explicit path => single-file mode
            ns["path"] = rest[0]
        # no path => batch mode: ingest everything in inbox/
        return ingest.run(**ns)
    if cmd == "purge":
        import purge
        raw, wiki = "--raw" in rest, "--wiki" in rest
        # Neither or both flags means "everything".
        scope = "all" if raw == wiki else ("raw" if raw else "wiki")
        return purge.run(scope=scope, yes="--yes" in rest)
    if cmd == "verify":
        import verify
        if not rest:
            print("usage: kb verify <page-id>", file=sys.stderr)
            return 2
        return verify.run(rest[0])
    print(f"unknown command: {cmd}\n{__doc__}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
