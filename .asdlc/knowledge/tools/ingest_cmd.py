"""Ingestion dispatcher.

Two ways to run it:

    python tools/kb.py ingest                 # batch: ingest everything in inbox/
    python tools/kb.py ingest <path>          # single file (under raw/ or absolute)
    python tools/kb.py ingest <path> --adapter NAME

Batch mode is the friendly drop-zone workflow: drop files into `inbox/`, run
`kb ingest`, and each file is copied into raw/ (immutable), converted to markdown
by the first manifest-priority adapter that accepts it, scaffolded into a draft
page under wiki/sources/, and then cleared out of the inbox.

The optional `markitdown` / `docling` backends are lazy-imported. If they are
installed only in a local `.venv`, that virtualenv's site-packages are added to
the path automatically so the single `kb ingest` command works without
activating anything.
"""
from __future__ import annotations

import argparse
import datetime as dt
import importlib
import shutil
import sys
from pathlib import Path

from _common import KB_ROOT, load_manifest

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


def _scaffold_source(src: Path, result, m: dict) -> Path:
    """Write a draft source page for an already-extracted result. Returns path."""
    sid = src.stem.lower().replace(" ", "-")
    out = KB_ROOT / m["paths"]["wiki"] / "sources" / f"{sid}.md"
    today = dt.date.today().isoformat()
    origin = src.relative_to(KB_ROOT) if KB_ROOT in src.parents else src
    front = (
        "---\n"
        f"id: {sid}\ntitle: {src.stem}\ntype: source\nstatus: draft\n"
        f"confidence: 0.6\nsources: [{sid}]\n"
        f"created: {today}\nupdated: {today}\n"
        f"origin: {origin}\n"
        f"media_type: {result.media_type}\ningested_with: {result.ingested_with}\n"
        f"checksum: {result.checksum}\n---\n\n"
    )
    body = (
        f"# {src.stem}\n\n"
        "> Auto-ingested source. Summarise below, then update entity/concept pages.\n\n"
        f"{result.markdown}\n"
    )
    out.write_text(front + body)
    return out


def _ingest_file(src: Path, m: dict, adapter: str | None) -> tuple[str, str]:
    """Ingest one raw file. Returns (status, message).

    status is one of: "ok", "skip", "error". `src` must already live under raw/.
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
    page = _scaffold_source(src, result, m)
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
    return _run_single(path, m, adapter)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?")
    ap.add_argument("--adapter", choices=list(ADAPTER_MODULES))
    sys.exit(run(**vars(ap.parse_args())))
