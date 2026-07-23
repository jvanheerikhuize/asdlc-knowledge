"""MkDocs build hook: resolve `[[wikilinks]]` into real links at render time.

The `wiki/` source stays canonical Obsidian-style — `[[page-id]]` and
`[[page-id|display]]` are left untouched on disk (so pages still work in
Obsidian/Foam and stay diff-friendly). This hook rewrites them only while
MkDocs builds the HTML site:

  - `[[id]]`            -> a link to that page, using the page's real title.
  - `[[id|display]]`    -> a link with the given display text.
  - `[[unknown]]`       -> a "wanted page" span (red-link style), the same set
                          `kb lint` reports as broken links — visible to a reader
                          instead of only to CI.

Wired in via `hooks:` in the viz.py-generated mkdocs.yml. Because the id set it
detects comes from the same `[[…]]` grammar the linter uses, the site and
`kb lint --broken_links` agree by construction.
"""
from __future__ import annotations

import posixpath
import re
from pathlib import Path

# id group `[^\]|]+` matches tools/_common.py::WIKILINK_RE exactly; the optional
# display half is captured here (group 2) so we can honour `[[id|display]]`.
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\]")

# docs_dir -> {page-id: (src_uri, title)}. Built once per build.
_INDEX: dict[str, dict[str, tuple[str, str]]] = {}

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
_TITLE_RE = re.compile(r"^title:\s*(.+?)\s*$", re.MULTILINE)


def _read_title(path: Path) -> str | None:
    try:
        head = path.read_text(encoding="utf-8")[:4096]
    except OSError:
        return None
    fm = _FM_RE.match(head)
    if not fm:
        return None
    t = _TITLE_RE.search(fm.group(1))
    if not t:
        return None
    return t.group(1).strip().strip("'\"") or None


def _index_for(docs_dir: str) -> dict[str, tuple[str, str]]:
    idx = _INDEX.get(docs_dir)
    if idx is None:
        idx = {}
        root = Path(docs_dir)
        for path in root.rglob("*.md"):
            pid = path.stem
            src = path.relative_to(root).as_posix()
            idx[pid] = (src, _read_title(path) or pid)
        _INDEX[docs_dir] = idx
    return idx


def on_page_markdown(markdown, page, config, files):  # noqa: ARG001 (mkdocs signature)
    index = _index_for(config["docs_dir"])
    src_uri = getattr(page.file, "src_uri", None) or page.file.src_path
    src_dir = posixpath.dirname(src_uri) or "."

    def _repl(match: re.Match) -> str:
        pid = match.group(1)
        display = match.group(2)
        target = index.get(pid)
        if target is not None:
            src, title = target
            text = display if display is not None else title
            rel = posixpath.relpath(src, src_dir)
            return f"[{text}]({rel})"
        # Unknown target: render as a visible "wanted page" rather than dead text.
        text = display if display is not None else pid
        return (f'<span class="kb-wanted" '
                f'style="color:#e03131;border-bottom:1px dotted #e03131;cursor:help" '
                f'title="wanted page: {pid} — no page exists yet">{text}</span>')

    return WIKILINK_RE.sub(_repl, markdown)
