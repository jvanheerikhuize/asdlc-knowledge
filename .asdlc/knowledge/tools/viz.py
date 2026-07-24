"""Visualization layer: generate a static-site config + a Mermaid link graph.

No server or infra needed to build. Emits:
  - mkdocs.yml         (MkDocs Material config; nav derived from wiki/)
  - wiki/index.md      (site homepage: a Mermaid graph of [[wikilinks]], nodes
                        colored by confidence band — MkDocs serves it at the
                        site root)

`mkdocs build` then produces a searchable, browsable HTML site; CI publishes it
(ADO pipeline artifact / GitHub Pages). Everything is regenerated from files, so the
viz never drifts from the source of truth.
"""
from __future__ import annotations

import json
from pathlib import Path

from _common import KB_ROOT, confidence_band, iter_pages, load_manifest, parse_page


TYPE_LABEL = {"concept": "concept", "entity": "entity", "source": "source"}


def _folder_map(m: dict) -> dict[str, str]:
    """type -> wiki subfolder, from the manifest (single source of truth)."""
    return {t: spec["folder"] for t, spec in m["page_types"].items()}


def _page_url(p, folders: dict[str, str]) -> str:
    """Directory-style URL of a page relative to the site root (where the graph
    homepage lives), matching MkDocs' default use_directory_urls."""
    folder = folders.get(p.type, p.type or "page")
    return f"{folder}/{p.id}/"


def _neighbours(pages, ids) -> dict[str, set[str]]:
    """Undirected connectivity: for each page, the set of distinct other pages
    it links to or is linked from. Used to build the Connections table."""
    nb: dict[str, set[str]] = {p.id: set() for p in pages}
    for p in pages:
        for tgt in p.links():
            if tgt in ids and tgt != p.id:
                nb[p.id].add(tgt)
                nb[tgt].add(p.id)
    return nb


def build_graph(m: dict) -> str:
    pages = list(iter_pages(m))
    folders = _folder_map(m)
    band_color = {b["label"]: b["color"] for b in m["confidence_policy"]["bands"]}
    lines = ["```mermaid", "graph LR"]
    for p in pages:
        conf = p.frontmatter.get("confidence", 0.0) or 0.0
        band = confidence_band(float(conf), m)
        label = p.frontmatter.get("title", p.id).replace('"', "'")
        node = p.id.replace("-", "_")
        lines.append(f'  {node}["{label}<br/>{conf} · {band}"]')
        lines.append(f'  style {node} fill:{band_color[band]}22,'
                     f'stroke:{band_color[band]}')
        # Make each node navigate to its page (the graph becomes a map, not a
        # picture). "_self" so it opens in place; MkDocs uses directory URLs.
        lines.append(f'  click {node} "{_page_url(p, folders)}" "Open page" _self')
    seen = set()
    ids = {p.id for p in pages}
    for p in pages:
        for tgt in p.links():
            if tgt in ids and (p.id, tgt) not in seen:
                seen.add((p.id, tgt))
                lines.append(f'  {p.id.replace("-", "_")} --> {tgt.replace("-", "_")}')
    lines.append("```")
    return "\n".join(lines)


def build_graph_data(m: dict) -> dict:
    """Same nodes/edges as the Mermaid graph, as plain JSON the 3D force graph
    reads at runtime — one source of truth for both the 2D and 3D views.
    Nodes carry title, type, confidence, band color and degree (used for size);
    links are de-duplicated undirected pairs."""
    pages = list(iter_pages(m))
    ids = {p.id for p in pages}
    nb = _neighbours(pages, ids)
    folders = _folder_map(m)
    band_color = {b["label"]: b["color"] for b in m["confidence_policy"]["bands"]}
    nodes = []
    for p in pages:
        conf = float(p.frontmatter.get("confidence", 0.0) or 0.0)
        band = confidence_band(conf, m)
        nodes.append({
            "id": p.id,
            "name": str(p.frontmatter.get("title", p.id)),
            "type": TYPE_LABEL.get(p.type, p.type or "page"),
            "conf": conf,
            "band": band,
            "color": band_color[band],
            "val": max(1, len(nb[p.id])),
            "href": _page_url(p, folders),
        })
    seen, links = set(), []
    for p in pages:
        for tgt in p.links():
            if tgt in ids and tgt != p.id:
                key = tuple(sorted((p.id, tgt)))
                if key not in seen:
                    seen.add(key)
                    links.append({"source": p.id, "target": tgt})
    return {"nodes": nodes, "links": links}


# Raw HTML/JS injected above the Mermaid fence: a 2D/3D switch, a container for
# the 3D graph, the graph data as JSON, and a lazy initializer that boots
# `3d-force-graph` (loaded via extra_javascript) only on first switch to 3D.
# Kept as one contiguous block with no blank lines so Python-Markdown passes it
# through verbatim; the Mermaid fence stays outside so it still renders.
_VIEW_TEMPLATE = """<div class="kb-graph">
<style>
.kb-view-toggle{display:flex;gap:.4rem;margin:.2rem 0 .8rem}
.kb-view-toggle button{font:inherit;cursor:pointer;padding:.35rem .8rem;border-radius:.4rem;border:1px solid var(--md-default-fg-color--lighter,#8888);background:transparent;color:inherit}
.kb-view-toggle button.kb-active{background:var(--md-accent-fg-color,#3b82f6);color:#fff;border-color:transparent}
#kb-graph-3d{width:100%;height:560px;border:1px solid var(--md-default-fg-color--lightest,#8883);border-radius:.5rem;overflow:hidden}
#kb-graph-3d .kb-msg{padding:1rem;opacity:.8}
</style>
<div class="kb-view-toggle" role="tablist">
<button id="kb-btn-2d" class="kb-active" type="button" onclick="kbShowView('2d')">2D · Mermaid</button>
<button id="kb-btn-3d" type="button" onclick="kbShowView('3d')">3D · Force graph</button>
</div>
<div id="kb-graph-3d" style="display:none"></div>
<script id="kb-graph-data" type="application/json">__GRAPH_DATA__</script>
<script>
(function(){
 var g=null;
 window.kbShowView=function(v){
  var pre=document.querySelector('pre.mermaid');
  var box=document.getElementById('kb-graph-3d');
  var b2=document.getElementById('kb-btn-2d'),b3=document.getElementById('kb-btn-3d');
  if(v==='3d'){ if(pre)pre.style.display='none'; box.style.display='block'; b3.classList.add('kb-active'); b2.classList.remove('kb-active'); kbInit(box); }
  else { if(pre)pre.style.display=''; box.style.display='none'; b2.classList.add('kb-active'); b3.classList.remove('kb-active'); }
 };
 function kbInit(box){
  if(g){ g.width(box.clientWidth); return; }
  if(typeof ForceGraph3D==='undefined'){ box.innerHTML='<div class="kb-msg">The 3D force-graph library did not load (offline?). The 2D view above has the full graph.</div>'; return; }
  var data=JSON.parse(document.getElementById('kb-graph-data').textContent);
  g=ForceGraph3D()(box).graphData(data)
    .backgroundColor('rgba(0,0,0,0)')
    .nodeColor(function(n){return n.color;})
    .nodeVal(function(n){return n.val;})
    .nodeRelSize(4)
    .nodeLabel(function(n){return '<b>'+n.name+'</b><br>'+n.type+' · '+n.conf+' '+n.band+'<br><small>click to focus · '+(navigator.platform.indexOf('Mac')>-1?'⌘':'Ctrl')+'/Shift-click to open</small>';})
    .linkColor(function(){return 'rgba(136,136,136,0.4)';})
    .linkWidth(0.5)
    .width(box.clientWidth).height(560);
  g.onNodeClick(function(n,e){
    // Modifier-click opens the page; a plain click focuses the camera on it.
    if(e&&(e.shiftKey||e.ctrlKey||e.metaKey)){ if(n.href)window.location.href=n.href; return; }
    var r=1+90/Math.hypot(n.x||1,n.y||1,n.z||1);
    g.cameraPosition({x:(n.x||0)*r,y:(n.y||0)*r,z:(n.z||0)*r},n,1200);
  });
  window.addEventListener('resize',function(){ if(g)g.width(box.clientWidth); });
 }
})();
</script>
</div>"""


def build_views(m: dict) -> str:
    """Toggle + 3D container (raw HTML) followed by the Mermaid 2D fence."""
    data = json.dumps(build_graph_data(m), separators=(",", ":"))
    return _VIEW_TEMPLATE.replace("__GRAPH_DATA__", data) + "\n\n" + build_graph(m)


def build_table(m: dict) -> str:
    """Line-free relationship view: each page and what it links to, so the
    connections are legible without any edges drawn on the graph."""
    pages = list(iter_pages(m))
    ids = {p.id for p in pages}
    nb = _neighbours(pages, ids)
    rows = ["| Page | Type | Confidence | 🔗 | Connects to |",
            "| --- | --- | --- | --- | --- |"]
    for p in sorted(pages, key=lambda p: (-len(nb[p.id]), p.id)):
        conf = float(p.frontmatter.get("confidence", 0.0) or 0.0)
        band = confidence_band(conf, m)
        ptype = TYPE_LABEL.get(p.type, p.type or "page")
        # Emit [[wikilinks]]: the mkdocs hook resolves them to real page links,
        # so every reference in this table is clickable (one resolver, no drift).
        page_cell = f"[[{p.id}]]"
        links = ", ".join(f"[[{t}|{t}]]" for t in sorted(nb[p.id])) or "—"
        rows.append(f"| **{page_cell}** | {ptype} | {conf} {band} | "
                    f"{len(nb[p.id])} | {links} |")
    return "\n".join(rows)


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
        # Label each page by its frontmatter title (a wiki sidebar reads in
        # prose, not kebab slugs); fall back to the stem, and sort by the
        # visible label. json.dumps quotes titles that contain YAML-special
        # characters (colons, quotes) into a valid nav entry.
        entries = []
        for f in files:
            title = str(parse_page(f).frontmatter.get("title") or f.stem)
            entries.append((title, f.name))
        for title, name in sorted(entries, key=lambda e: e[0].lower()):
            nav.append(f"      - {json.dumps(title)}: {folder}/{name}")
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
extra_javascript:
  # Powers the homepage 3D view (global ForceGraph3D); bundles three.js.
  - https://cdn.jsdelivr.net/npm/3d-force-graph@1
plugins:
  - search
# Resolve [[wikilinks]] -> real links at build time (tools/mkdocs_hooks.py).
# Keeps wiki/ source canonical while the published site behaves like a wiki.
hooks:
  - tools/mkdocs_hooks.py
nav:
{chr(10).join(nav)}
"""


def main() -> int:
    m = load_manifest()
    # The homepage (site root) is the knowledge graph itself.
    home_path = KB_ROOT / m["paths"]["wiki"] / "index.md"
    intro = ("---\ntitle: Knowledge Graph\n---\n\n# Knowledge Graph\n\n"
             "Nodes colored by confidence band, and every node is a link. Use the "
             "**2D / 3D** toggle to switch between the Mermaid diagram and an "
             "interactive force-directed graph. In **2D**, click a node to open "
             "its page. In **3D**, drag to rotate and scroll to zoom; click a node "
             "to focus the camera, or ⌘/Ctrl/Shift-click to open its page. "
             "Regenerate with `python tools/kb.py viz`.\n\n")
    body = build_views(m) + "\n\n## Connections\n\n" + build_table(m) + "\n"
    home_path.write_text(intro + body)
    print(f"generated {home_path.relative_to(KB_ROOT)}")
    mk = KB_ROOT / "mkdocs.yml"
    mk.write_text(build_mkdocs(m))
    print(f"generated {mk.relative_to(KB_ROOT)}")
    print("build the site with:  cd .asdlc/knowledge && mkdocs build")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
