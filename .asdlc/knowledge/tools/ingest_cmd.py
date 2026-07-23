"""Ingestion dispatcher: pick the first manifest-priority adapter that accepts
the file, convert it to markdown, and scaffold a source page under wiki/sources/.

Usage: python tools/kb.py ingest <path-under-raw/> [--adapter NAME]
"""
from __future__ import annotations

import argparse
import datetime as dt
import importlib
import sys
from pathlib import Path

from _common import KB_ROOT, load_manifest

ADAPTER_MODULES = {
    "plaintext": ("ingest.adapters.plaintext_adapter", "PlaintextAdapter"),
    "markitdown": ("ingest.adapters.markitdown_adapter", "MarkitdownAdapter"),
    "docling": ("ingest.adapters.docling_adapter", "DoclingAdapter"),
}


def _load_adapter(name: str):
    mod_name, cls_name = ADAPTER_MODULES[name]
    # tools/ and KB_ROOT are on the path (see kb.py); import as package.
    sys.path.insert(0, str(KB_ROOT))
    mod = importlib.import_module(mod_name)
    return getattr(mod, cls_name)()


def run(path: str, adapter: str | None = None) -> int:
    m = load_manifest()
    raw_root = KB_ROOT / m["paths"]["raw"]
    src = Path(path)
    if not src.is_absolute():
        src = raw_root / path
    if not src.exists():
        print(f"file not found: {src}", file=sys.stderr)
        return 2

    order = [adapter] if adapter else m["ingest"]["adapters"]
    chosen = None
    for name in order:
        a = _load_adapter(name)
        if a.accepts(src, None):
            chosen = a
            break
    if chosen is None:
        print(f"no adapter accepts {src.name}", file=sys.stderr)
        return 1

    result = chosen.extract(src)
    sid = src.stem.lower().replace(" ", "-")
    out = KB_ROOT / m["paths"]["wiki"] / "sources" / f"{sid}.md"
    today = dt.date.today().isoformat()
    front = (
        "---\n"
        f"id: {sid}\ntitle: {src.stem}\ntype: source\nstatus: draft\n"
        f"confidence: 0.6\nsources: [{sid}]\n"
        f"created: {today}\nupdated: {today}\n"
        f"origin: {src.relative_to(KB_ROOT) if KB_ROOT in src.parents else src}\n"
        f"media_type: {result.media_type}\ningested_with: {result.ingested_with}\n"
        f"checksum: {result.checksum}\n---\n\n"
    )
    body = f"# {src.stem}\n\n> Auto-ingested source. Summarise below, then update entity/concept pages.\n\n{result.markdown}\n"
    out.write_text(front + body)
    print(f"wrote {out.relative_to(KB_ROOT)} via '{chosen.name}' "
          f"({len(result.markdown)} chars)")
    print("Next: summarise, update entity/concept pages, add [[links]], "
          "append to log.md, run `kb lint`.")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--adapter", choices=list(ADAPTER_MODULES))
    sys.exit(run(**vars(ap.parse_args())))
