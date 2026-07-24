"""Ingestion dispatcher.

Three ways to run it:

    python tools/kb.py ingest                 # batch: ingest everything in inbox/
    python tools/kb.py ingest <path>          # single file (under raw/ or absolute)
    python tools/kb.py ingest <url>           # fetch + snapshot a web page
    python tools/kb.py ingest <path|url> --adapter NAME

Batch mode is the friendly drop-zone workflow: drop files into `inbox/`, run
`kb ingest`, and each file is copied into raw/ (immutable), converted to markdown
by the first manifest-priority adapter that accepts it, scaffolded into a draft
page under wiki/sources/, and then cleared out of the inbox.

URL mode is the same pipeline for the common case where knowledge arrives as a
link: `kb ingest https://…` downloads the page once into raw/ (immutable
snapshot, so the page stays fixed even if the site later changes) and hands the
saved `.html` to the ordinary adapter chain — markitdown converts HTML, so no
new dependency is needed. The source page records the original URL as `origin`.

The optional `markitdown` / `docling` backends are lazy-imported. If they are
installed only in a local `.venv`, that virtualenv's site-packages are added to
the path automatically so the single `kb ingest` command works without
activating anything.
"""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import importlib
import re
import shutil
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

from _common import KB_ROOT, iter_pages, load_manifest

# A new source whose id/title matches an existing one this closely is flagged as
# a likely re-ingest of the same document under a different name (0.0–1.0).
_SIMILARITY_WARN = 0.85

ADAPTER_MODULES = {
    "plaintext": ("ingest.adapters.plaintext_adapter", "PlaintextAdapter"),
    "markitdown": ("ingest.adapters.markitdown_adapter", "MarkitdownAdapter"),
    "docling": ("ingest.adapters.docling_adapter", "DoclingAdapter"),
}

# Files in inbox/ that are project scaffolding, not content to ingest.
INBOX_SKIP = {"README.md", ".gitkeep"}


def _add_local_venv_to_path() -> None:
    """Best-effort: if optional backends live in a sibling `.venv`, expose them.

    Keeps the end-user command a single `kb ingest` — no venv activation. Looks
    for a `.venv` beside the KB (repo root) or the KB root itself. Harmless when
    absent: plaintext still works and missing backends report cleanly.
    """
    for base in (KB_ROOT, KB_ROOT.parent, KB_ROOT.parent.parent):
        for site in (base / ".venv").glob("lib/python*/site-packages"):
            if site.is_dir() and str(site) not in sys.path:
                sys.path.append(str(site))


def _load_adapter(name: str):
    mod_name, cls_name = ADAPTER_MODULES[name]
    # tools/ and KB_ROOT are on the path (see kb.py); import as package.
    sys.path.insert(0, str(KB_ROOT))
    mod = importlib.import_module(mod_name)
    return getattr(mod, cls_name)()


def _dispatch(src: Path, m: dict, adapter: str | None):
    """Return the first accepting adapter for `src`, or None."""
    order = [adapter] if adapter else m["ingest"]["adapters"]
    for name in order:
        a = _load_adapter(name)
        if a.accepts(src, None):
            return a
    return None


def _scaffold_source(src: Path, result, m: dict, origin: str | None = None) -> Path:
    """Write a draft source page for an already-extracted result. Returns path.

    `origin` overrides the provenance line (e.g. the source URL for a snapshot);
    it defaults to the file's path under raw/. The page title prefers a title the
    adapter extracted from the document (markitdown reads a page's <title>),
    falling back to the filename stem.
    """
    sid = src.stem.lower().replace(" ", "-")
    out = KB_ROOT / m["paths"]["wiki"] / "sources" / f"{sid}.md"
    today = dt.date.today().isoformat()
    if origin is None:
        origin = str(src.relative_to(KB_ROOT) if KB_ROOT in src.parents else src)
    title = (result.meta.get("title") or "").strip() or src.stem
    front = (
        "---\n"
        f"id: {sid}\ntitle: {title}\ntype: source\nstatus: draft\n"
        f"confidence: 0.6\nsources: [{sid}]\n"
        f"created: {today}\nupdated: {today}\n"
        f"origin: {origin}\n"
        f"media_type: {result.media_type}\ningested_with: {result.ingested_with}\n"
        f"checksum: {result.checksum}\n---\n\n"
    )
    body = (
        f"# {title}\n\n"
        "> Auto-ingested source. Summarise below, then update entity/concept pages.\n\n"
        f"{result.markdown}\n"
    )
    out.write_text(front + body)
    return out


def _existing_sources(m: dict) -> list[tuple[str, str, str]]:
    """Every existing source page as (id, checksum, title) for dup detection."""
    out = []
    for p in iter_pages(m):
        if p.type != "source":
            continue
        fm = p.frontmatter
        out.append((p.id, str(fm.get("checksum") or ""),
                    str(fm.get("title") or p.id)))
    return out


def _dup_warnings(sid: str, title: str, checksum: str,
                  existing: list[tuple[str, str, str]]) -> list[str]:
    """Advisory warnings if this incoming source looks like an existing one.

    Two independent signals, both non-blocking (the user may genuinely want a
    second copy): an identical content `checksum` already on file catches the
    same document re-ingested under a new name; a high id/title similarity
    catches a lightly-renamed or re-downloaded variant that checksums miss.
    """
    warns = []
    for eid, echecksum, etitle in existing:
        if eid == sid:
            continue  # exact-id re-ingest is handled as a hard skip upstream
        if checksum and checksum == echecksum:
            warns.append(f"identical content already ingested as '{eid}' "
                         f"(same checksum) — prefer updating it over forking a copy")
            continue
        ratio = max(
            difflib.SequenceMatcher(None, sid, eid).ratio(),
            difflib.SequenceMatcher(None, title.lower(), etitle.lower()).ratio(),
        )
        if ratio >= _SIMILARITY_WARN:
            warns.append(f"looks similar to existing source '{eid}' "
                         f"({ratio:.0%} id/title match) — is this a duplicate?")
    return warns


def _ingest_file(src: Path, m: dict, adapter: str | None,
                 origin: str | None = None) -> tuple[str, str]:
    """Ingest one raw file. Returns (status, message).

    status is one of: "ok", "skip", "error". `src` must already live under raw/.
    `origin` overrides the source page's provenance line (used for URL snapshots).
    """
    sid = src.stem.lower().replace(" ", "-")
    out = KB_ROOT / m["paths"]["wiki"] / "sources" / f"{sid}.md"
    if out.exists():
        return "skip", f"{src.name}: source page '{sid}' already exists — skipped"
    chosen = _dispatch(src, m, adapter)
    if chosen is None:
        return "error", f"{src.name}: no adapter accepts this file type"
    try:
        result = chosen.extract(src)
    except Exception as exc:  # backend missing or conversion failed
        return "error", f"{src.name}: {chosen.name} failed — {exc}"
    title = (result.meta.get("title") or "").strip() or src.stem
    for w in _dup_warnings(sid, title, result.checksum, _existing_sources(m)):
        print(f"  ⚠ {w}")
    page = _scaffold_source(src, result, m, origin=origin)
    rel = page.relative_to(KB_ROOT)
    return "ok", f"{src.name}: ingested via '{chosen.name}' -> {rel} ({len(result.markdown)} chars)"


def _run_batch(m: dict, adapter: str | None) -> int:
    """Ingest every file in inbox/: copy into raw/, scaffold, clear the inbox."""
    inbox = KB_ROOT / m["paths"].get("inbox", "inbox")
    raw_root = KB_ROOT / m["paths"]["raw"]
    if not inbox.exists():
        print(f"no inbox folder at {inbox.relative_to(KB_ROOT)}", file=sys.stderr)
        return 2
    files = [p for p in sorted(inbox.iterdir())
             if p.is_file() and p.name not in INBOX_SKIP and not p.name.startswith(".")]
    if not files:
        rel = inbox.relative_to(KB_ROOT)
        print(f"inbox is empty — drop file(s) into {rel}/ then re-run `kb ingest`.")
        return 0

    print(f"ingesting {len(files)} file(s) from {inbox.relative_to(KB_ROOT)}/ ...\n")
    n_ok = n_skip = n_err = 0
    for src in files:
        dest = raw_root / src.name
        if dest.exists():
            # raw/ is immutable; don't clobber. Ingest reflects the existing copy.
            print(f"  • {src.name}: already in raw/ — ingesting existing copy")
        else:
            shutil.copy2(src, dest)
        status, msg = _ingest_file(dest, m, adapter)
        mark = {"ok": "✓", "skip": "–", "error": "✗"}[status]
        print(f"  {mark} {msg}")
        if status == "ok":
            n_ok += 1
            src.unlink()                       # clear from inbox once safely in raw/
        elif status == "skip":
            n_skip += 1
            src.unlink()                       # already ingested; clear it too
        else:
            n_err += 1
            if not dest.exists() or dest.stat().st_size == 0:
                pass                            # nothing landed in raw/
            # leave the original in inbox/ so the user can retry after a fix

    print(f"\ndone: {n_ok} ingested, {n_skip} skipped, {n_err} failed.")
    if n_ok:
        print("Next: summarise the new draft page(s), add [[links]] to entity/"
              "concept pages, append to log.md, run `kb lint --strict`.")
    return 1 if n_err else 0


def _slug_from_url(url: str) -> str:
    """A stable, filesystem-safe id for a URL: domain + path, minus noise.

    e.g. https://karpathy.github.io/2019/04/25/recipe/ -> karpathy-github-io-2019-04-25-recipe
    """
    p = urlparse(url)
    host = p.netloc.split("@")[-1].split(":")[0]
    host = re.sub(r"^www\.", "", host)
    slug = re.sub(r"[^a-z0-9]+", "-", f"{host} {p.path}".lower()).strip("-")
    return slug[:60].strip("-") or "page"


def _fetch_url(url: str, dest: Path) -> tuple[bool, str]:
    """Download `url` into `dest` (bytes). Returns (ok, message)."""
    req = urllib.request.Request(
        url, headers={"User-Agent": "asdlc-knowledge kb-ingest (+stdlib urllib)"}
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError, OSError) as exc:
        return False, f"fetch failed: {exc}"
    dest.write_bytes(data)
    return True, f"snapshotted {len(data)} bytes"


def _run_url(url: str, m: dict, adapter: str | None) -> int:
    """Fetch a web page, snapshot it into raw/, then ingest the saved file."""
    raw_root = KB_ROOT / m["paths"]["raw"]
    dest = raw_root / f"{_slug_from_url(url)}.html"
    rel = dest.relative_to(KB_ROOT)
    if dest.exists():
        # raw/ is immutable — keep the original snapshot; ingest reflects it.
        print(f"• {rel} already snapshotted — ingesting existing copy")
    else:
        raw_root.mkdir(parents=True, exist_ok=True)
        ok, msg = _fetch_url(url, dest)
        print(f"• {url}: {msg}")
        if not ok:
            return 1
    status, msg = _ingest_file(dest, m, adapter, origin=url)
    print(msg, file=sys.stderr if status == "error" else sys.stdout)
    if status == "ok":
        print("Next: summarise the draft, set confidence per the rubric, add "
              "[[links]] to entity/concept pages, append to log.md, run `kb lint`.")
        return 0
    return 1 if status == "error" else 0


def _run_single(path: str, m: dict, adapter: str | None) -> int:
    """Ingest one explicit path (relative to raw/, or absolute). Legacy form."""
    raw_root = KB_ROOT / m["paths"]["raw"]
    src = Path(path)
    if not src.is_absolute():
        src = raw_root / path
    if not src.exists():
        print(f"file not found: {src}", file=sys.stderr)
        return 2
    status, msg = _ingest_file(src, m, adapter)
    print(msg, file=sys.stderr if status == "error" else sys.stdout)
    if status == "ok":
        print("Next: summarise, update entity/concept pages, add [[links]], "
              "append to log.md, run `kb lint`.")
        return 0
    return 1 if status == "error" else 0


def run(path: str | None = None, adapter: str | None = None) -> int:
    _add_local_venv_to_path()
    m = load_manifest()
    if path is None:
        return _run_batch(m, adapter)
    if re.match(r"^https?://", path, re.IGNORECASE):
        return _run_url(path, m, adapter)
    return _run_single(path, m, adapter)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?")
    ap.add_argument("--adapter", choices=list(ADAPTER_MODULES))
    sys.exit(run(**vars(ap.parse_args())))
