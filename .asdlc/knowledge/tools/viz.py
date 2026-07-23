"""Visualization layer: generate a static-site config + a Mermaid link graph.

No server or infra needed to build. Emits:
  - mkdocs.yml         (MkDocs Material config; nav derived from wiki/)
  - wiki/index.md      (site homepage: a Mermaid graph of [[wikilinks]], nodes
                        colored by confidence band — MkDocs serves it at the
                        site root)

`mkdocs build` then produces a searchable, browsable HTML site; the publish
GitHub Action deploys it to Pages. Everything is regenerated from files, so the
viz never drifts from the source of truth.
"""
from __future__ import annotations

from pathlib import Path

from _common import KB_ROOT, confidence_band, iter_pages, load_manifest


# How each page type is drawn. `shape` is a (prefix, suffix) pair wrapping the
# node label so the type is legible from the silhouette alone: concepts are
# rounded, entities are stadiums, sources are document/parallelograms.
TYPE_SHAPE = {
    "concept": ("(", ")"),
    "entity": ("([", "])"),
    "source": ("[/", "/]"),
}
TYPE_ORDER = ["concept", "entity", "source"]  # abstract idea -> who -> evidence
TYPE_TITLE = {"concept": "Concepts", "entity": "Entities", "source": "Sources"}


def _safe(node_id: str) -> str:
    return node_id.replace("-", "_")


def _node(p, m: dict, band_color: dict) -> tuple[str, str]:
    """Return (declaration, style) lines for one page node."""
    conf = float(p.frontmatter.get("confidence", 0.0) or 0.0)
    band = confidence_band(conf, m)
    title = str(p.frontmatter.get("title", p.id)).replace('"', "'")
    pre, suf = TYPE_SHAPE.get(p.type, ("[", "]"))
    sid = _safe(p.id)
    decl = f'    {sid}{pre}"{title}<br/><small>{conf} · {band}</small>"{suf}'
    style = (f'  style {sid} fill:{band_color[band]}18,'
             f'stroke:{band_color[band]},stroke-width:1px')
    return decl, style


def build_graph(m: dict) -> str:
    pages = list(iter_pages(m))
    band_color = {b["label"]: b["color"] for b in m["confidence_policy"]["bands"]}
    by_id = {p.id: p for p in pages}
    ids = set(by_id)

    lines = ["```mermaid", "graph LR"]

    # 1) Nodes, grouped into one subgraph per layer so the wiki's structure
    #    (concepts synthesised from entities and sources) reads at a glance.
    styles: list[str] = []
    for ptype in TYPE_ORDER:
        group = [p for p in pages if p.type == ptype]
        if not group:
            continue
        lines.append(f'  subgraph {ptype}_layer["{TYPE_TITLE[ptype]}"]')
        lines.append("    direction LR")
        for p in group:
            decl, style = _node(p, m, band_color)
            lines.append(decl)
            styles.append(style)
        lines.append("  end")
    # Any page type not in TYPE_ORDER still gets drawn (ungrouped).
    for p in pages:
        if p.type not in TYPE_ORDER:
            decl, style = _node(p, m, band_color)
            lines.append("  " + decl.strip())
            styles.append(style)

    # 2) Edges. Collapse reciprocal wikilinks into a single line, and draw
    #    citations (a page pointing at a source) dotted to set them apart from
    #    solid concept<->entity "relates-to" links.
    pair_dirs: dict[tuple[str, str], set[str]] = {}
    for p in pages:
        for tgt in p.links():
            if tgt in ids and tgt != p.id:
                key = tuple(sorted((p.id, tgt)))
                pair_dirs.setdefault(key, set()).add(p.id)

    for (a, b), origins in sorted(pair_dirs.items()):
        both = len(origins) == 2
        is_cite = "source" in (by_id[a].type, by_id[b].type)
        # Orient a single-direction arrow from the actual source of the link.
        src, dst = (a, b) if a in origins else (b, a)
        if is_cite:
            arrow = "<-.->" if both else "-.->"
        else:
            arrow = "<-->" if both else "-->"
        lines.append(f'  {_safe(src)} {arrow} {_safe(dst)}')

    lines.extend(styles)

    # 3) Legend: one example of each shape + a note on what colour/line mean.
    lines.append('  subgraph legend["Legend"]')
    lines.append("    direction LR")
    lines.append('    lg_c("Concept")')
    lines.append('    lg_e(["Entity"])')
    lines.append('    lg_s[/"Source"/]')
    lines.append('    lg_c -.->|cites| lg_s')
    lines.append('    lg_c <--> lg_e')
    lines.append("  end")
    lines.append("  style legend fill:none,stroke:#adb5bd,stroke-dasharray:3 3")
    for lg in ("lg_c", "lg_e", "lg_s"):
        lines.append(f"  style {lg} fill:#f1f3f5,stroke:#adb5bd")

    lines.append("```")
    return "\n".join(lines)


def build_mkdocs(m: dict) -> str:
    wiki = KB_ROOT / m["paths"]["wiki"]
    # Enumerate real files so `mkdocs build --strict` never sees an unlisted page.
    # index.md is the homepage MkDocs serves at the site root.
    nav = ["  - Overview: index.md"]
    for tspec in m["page_types"].values():
        folder = tspec["folder"]
        files = sorted((wiki / folder).glob("*.md"))
        if not files:
            continue
        nav.append(f"  - {folder.capitalize()}:")
        for f in files:
            nav.append(f"      - {f.stem}: {folder}/{f.name}")
    return f"""# GENERATED by tools/viz.py from manifest.yaml. Do not hand-edit.
site_name: {m['name']!r}
site_description: {m['description'].strip()!r}
docs_dir: wiki
theme:
  name: material
  features: [navigation.instant, navigation.top, search.suggest, content.code.copy]
  palette:
    - scheme: default
      toggle: {{icon: material/brightness-7, name: dark}}
    - scheme: slate
      toggle: {{icon: material/brightness-4, name: light}}
markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
plugins:
  - search
nav:
{chr(10).join(nav)}
"""


def main() -> int:
    m = load_manifest()
    # The homepage (site root) is the knowledge graph itself.
    home_path = KB_ROOT / m["paths"]["wiki"] / "index.md"
    intro = (
        "---\ntitle: Knowledge Graph\n---\n\n# Knowledge Graph\n\n"
        "Every page in the wiki and how it links to the others. Read it as:\n\n"
        "- **Shape = layer** — `(concept)` rounded, `([entity])` stadium, "
        "`[/source/]` document. Pages are grouped into their layer.\n"
        "- **Colour = confidence** — green `high` (≥0.75), orange `medium` "
        "(≥0.45), red `low`. The `0.0 · band` under each title is the score.\n"
        "- **Line = relationship** — solid `↔` is a concept/entity cross-link; "
        "dotted `⋯▸` is a **citation** to a source. Double-headed means both "
        "pages link back to each other.\n\n"
        "Regenerate after any content change with `python tools/kb.py viz`.\n\n"
    )
    home_path.write_text(intro + build_graph(m) + "\n")
    print(f"generated {home_path.relative_to(KB_ROOT)}")
    mk = KB_ROOT / "mkdocs.yml"
    mk.write_text(build_mkdocs(m))
    print(f"generated {mk.relative_to(KB_ROOT)}")
    print("build the site with:  cd .asdlc/knowledge && mkdocs build")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
