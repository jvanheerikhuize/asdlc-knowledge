"""MkDocs build hook: turn the canonical `wiki/` source into a real wiki.

The `wiki/` files stay canonical Obsidian-style on disk — `[[page-id]]`,
`[[page-id|display]]`, `[[page-id#heading]]` and `sources:` frontmatter are left
untouched (so pages still work in Obsidian/Foam and stay diff-friendly). This
hook adds all the *wiki* behaviour while MkDocs renders the HTML site, from one
link index built once per build:

  - `[[id]]`            -> a link to that page, using the page's real title.
  - `[[id|display]]`    -> a link with the given display text.
  - `[[id#heading]]`    -> a link to a heading anchor on that page.
  - `[[alias]]`         -> resolves through each page's `aliases:` frontmatter.
  - `[[unknown]]`       -> a "wanted page" span (red-link style) — the same set
                          `kb lint --broken_links` reports, visible to a reader.
  - `sources:` frontmatter -> a rendered, linked **Sources** section per page.
  - inbound links      -> a generated **Referenced by** (backlinks) section.

Hardening (why this file is more than a regex):

  - Rewrites happen *only outside* fenced/inline code, so `[[…]]` shown in a code
    sample is left as literal text.
  - Ids are matched exactly, then by `aliases:`, then case-insensitively, with
    surrounding whitespace tolerated (`[[ id | text ]]`).
  - Titles/aliases/sources come from a real YAML parse of the frontmatter (with a
    stdlib fallback), not an ad-hoc line match.
  - The id set is derived from the same wiki tree the linter walks, so the site
    and `kb lint --broken_links` agree by construction.

Wired in via `hooks:` in the viz.py-generated mkdocs.yml.
"""
from __future__ import annotations

import posixpath
import re
from pathlib import Path

try:  # PyYAML is present in the docs build env; degrade gracefully if not.
    import yaml
except Exception:  # pragma: no cover - fallback path
    yaml = None

# `[[ id (#heading)? (| display)? ]]` with whitespace tolerated around each part.
# group 1 = id, group 2 = heading (optional), group 3 = display text (optional).
WIKILINK_RE = re.compile(
    r"\[\[\s*([^\]|#]+?)\s*(?:#\s*([^\]|]+?)\s*)?(?:\|\s*(.*?)\s*)?\]\]"
)

# Fenced code blocks (``` or ~~~, any indent) and inline code spans — regions the
# wikilink rewrite must skip so code samples keep their literal `[[…]]`.
_CODE_RE = re.compile(
    r"(?P<fence>^[ \t]*(?P<ticks>`{3,}|~{3,})[^\n]*\n.*?^[ \t]*(?P=ticks)[ \t]*$)"
    r"|(?P<inline>`+[^`\n]*`+)",
    re.DOTALL | re.MULTILINE,
)

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
_TITLE_RE = re.compile(r"^title:\s*(.+?)\s*$", re.MULTILINE)


class _Index:
    """Everything the hook needs about the wiki tree, computed once per build:
    id -> (src_uri, title), a lowercased alias/id lookup, and the inbound-link
    (backlink) graph. Keyed by docs_dir so a single build reuses one instance."""

    __slots__ = ("by_id", "lookup", "backlinks")

    def __init__(self, docs_dir: str) -> None:
        root = Path(docs_dir)
        self.by_id: dict[str, tuple[str, str]] = {}
        self.lookup: dict[str, str] = {}          # lower(id|alias) -> id
        self.backlinks: dict[str, list[str]] = {}

        pages = []  # (id, src_uri, title, body, sources)
        for path in sorted(root.rglob("*.md")):
            fm, body = _split_frontmatter(path)
            pid = str(fm.get("id") or path.stem)
            src = path.relative_to(root).as_posix()
            title = str(fm.get("title") or pid)
            self.by_id[pid] = (src, title)
            self.lookup.setdefault(pid.lower(), pid)
            for alias in _as_list(fm.get("aliases")):
                self.lookup.setdefault(str(alias).lower(), pid)
            pages.append((pid, src, title, body, _as_list(fm.get("sources"))))

        # Inbound graph: a page is "referenced by" any page that links to it in
        # prose (outside code) or cites it in `sources:`. Skip the generated
        # homepage so it never appears as a backlink.
        back: dict[str, set[str]] = {}
        for pid, src, _title, body, sources in pages:
            if src == "index.md":
                continue
            targets = set(sources)
            for m in WIKILINK_RE.finditer(_strip_code(body)):
                targets.add(m.group(1).strip())
            for tgt in targets:
                rid = self.resolve(tgt)
                if rid and rid != pid:
                    back.setdefault(rid, set()).add(pid)
        self.backlinks = {k: sorted(v) for k, v in back.items()}

    def resolve(self, raw: str) -> str | None:
        """Map a raw `[[target]]` id/alias to a real page id, or None."""
        raw = raw.strip()
        if raw in self.by_id:
            return raw
        return self.lookup.get(raw.lower())


_INDEX: dict[str, _Index] = {}


def _index_for(docs_dir: str) -> _Index:
    idx = _INDEX.get(docs_dir)
    if idx is None:
        idx = _Index(docs_dir)
        _INDEX[docs_dir] = idx
    return idx


def _split_frontmatter(path: Path) -> tuple[dict, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {}, ""
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    block, body = m.group(1), text[m.end():]
    if yaml is not None:
        try:
            data = yaml.safe_load(block) or {}
            if isinstance(data, dict):
                return data, body
        except Exception:
            pass
    # Fallback: recover at least the title without a YAML parser.
    t = _TITLE_RE.search(block)
    return ({"title": t.group(1).strip().strip("'\"")} if t else {}), body


def _as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return [v for v in value if v not in (None, "")]
    return [value]


def _strip_code(text: str) -> str:
    """Blank out code regions (keeping length irrelevant) so link scanning never
    sees `[[…]]` inside code."""
    return _CODE_RE.sub(lambda m: "", text)


def _slug(text: str) -> str:
    """Approximate MkDocs/Material's heading slugs for `#heading` anchors."""
    s = re.sub(r"[^\w\s-]", "", text.strip().lower())
    return re.sub(r"[\s_]+", "-", s).strip("-")


def _sub_outside_code(text: str, repl) -> str:
    """Apply the wikilink substitution to every span *except* code regions."""
    out, pos = [], 0
    for m in _CODE_RE.finditer(text):
        out.append(WIKILINK_RE.sub(repl, text[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(WIKILINK_RE.sub(repl, text[pos:]))
    return "".join(out)


def _wanted(text: str, pid: str) -> str:
    return (f'<span class="kb-wanted" '
            f'style="color:#e03131;border-bottom:1px dotted #e03131;cursor:help" '
            f'title="wanted page: {pid} — no page exists yet">{text}</span>')


def _sources_section(idx: _Index, meta: dict, src_dir: str) -> str:
    """A linked **Sources** section from the page's `sources:` frontmatter."""
    items = []
    for sid in _as_list(meta.get("sources")):
        sid = str(sid)
        rid = idx.resolve(sid)
        if rid is not None:
            src, title = idx.by_id[rid]
            rel = posixpath.relpath(src, src_dir)
            items.append(f"- [{title}]({rel})")
        else:
            items.append(f"- {_wanted(sid, sid)}")
    if not items:
        return ""
    return "\n\n## Sources\n\n" + "\n".join(items) + "\n"


def _backlinks_section(idx: _Index, pid: str, src_dir: str) -> str:
    """A generated **Referenced by** section from the inbound-link graph."""
    refs = idx.backlinks.get(pid or "", [])
    items = []
    for rid in refs:
        src, title = idx.by_id[rid]
        rel = posixpath.relpath(src, src_dir)
        items.append(f"- [{title}]({rel})")
    if not items:
        return ""
    return "\n\n## Referenced by\n\n" + "\n".join(items) + "\n"


def on_page_markdown(markdown, page, config, files):  # noqa: ARG001 (mkdocs signature)
    idx = _index_for(config["docs_dir"])
    src_uri = getattr(page.file, "src_uri", None) or page.file.src_path
    src_dir = posixpath.dirname(src_uri) or "."

    def _repl(match: re.Match) -> str:
        raw = match.group(1)
        anchor = match.group(2)
        display = match.group(3)
        rid = idx.resolve(raw)
        if rid is not None:
            src, title = idx.by_id[rid]
            text = display if display is not None else (
                f"{title} § {anchor.strip()}" if anchor else title)
            rel = posixpath.relpath(src, src_dir)
            if anchor:
                rel = f"{rel}#{_slug(anchor)}"
            return f"[{text}]({rel})"
        # Unknown target: render as a visible "wanted page" rather than dead text.
        text = display if display is not None else raw.strip()
        return _wanted(text, raw.strip())

    out = _sub_outside_code(markdown, _repl)

    # The generated homepage is a view, not a page — no Sources/backlinks on it.
    if src_uri != "index.md":
        pid = str(getattr(page, "meta", {}).get("id") or Path(src_uri).stem)
        out += _sources_section(idx, getattr(page, "meta", {}), src_dir)
        out += _backlinks_section(idx, pid, src_dir)

    return out
