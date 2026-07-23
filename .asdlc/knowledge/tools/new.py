"""kb new <type> <id> [--title "..."] — stamp a page from its template.

Copies `_templates/<type>.md`, fills in `id`, `title`, today's `created`/
`updated`, and writes it under `wiki/<folder>/<id>.md`. Everything else
(sources, status: draft, required fields) is left for the agent to fill in —
this only removes the bookkeeping, not the judgement.
"""
from __future__ import annotations

import datetime
import re
import sys
from pathlib import Path

from _common import KB_ROOT, load_manifest

ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def run(type_: str, id_: str, title: str | None = None) -> int:
    m = load_manifest()
    page_types = m["page_types"]
    if type_ not in page_types:
        print(f"unknown page type: {type_!r} (known: {', '.join(page_types)})",
              file=sys.stderr)
        return 2
    if not ID_RE.match(id_):
        print(f"invalid id: {id_!r} (must be kebab-case, e.g. my-page-id)",
              file=sys.stderr)
        return 2

    tspec = page_types[type_]
    dest = KB_ROOT / m["paths"]["wiki"] / tspec["folder"] / f"{id_}.md"
    if dest.exists():
        print(f"already exists: {dest.relative_to(KB_ROOT)}", file=sys.stderr)
        return 1

    tpl_path = KB_ROOT / m["paths"]["templates"] / f"{type_}.md"
    if not tpl_path.exists():
        print(f"no template for {type_!r} — run `kb scaffold` first", file=sys.stderr)
        return 1

    text = tpl_path.read_text()
    today = datetime.date.today().isoformat()
    display_title = title or id_
    text = text.replace(f"REPLACE-ME-{type_}", id_)
    text = text.replace("REPLACE ME", display_title)
    text = text.replace("YYYY-MM-DD", today)
    text = text.replace("{{title}}", display_title)
    # Drop still-blank optional fields (`key: # comment`) rather than write
    # them out as YAML null, which fails the generated schema's `type: string`.
    text = "\n".join(
        line for line in text.splitlines()
        if not re.match(r"^\w+:\s*#", line)
    )

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text)
    print(f"created {dest.relative_to(KB_ROOT)}")
    return 0
