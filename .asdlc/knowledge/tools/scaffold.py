"""Generate the KB's structure from manifest.yaml (the single source of truth).

Idempotent. Produces:
  - directory skeleton (raw/, wiki/<folder> per page type, _schema/, _templates/)
  - _schema/frontmatter.schema.json  (JSON Schema, oneOf per page type)
  - _templates/<type>.md             (starter page per type)

Never hand-edit the generated files; edit the manifest and re-run.
"""
from __future__ import annotations

import json
from pathlib import Path

from _common import KB_ROOT, load_manifest

TYPE_MAP = {"string": "string", "number": "number", "array": "array", "boolean": "boolean"}


def _field_schema(spec: dict) -> dict:
    js: dict = {"type": TYPE_MAP.get(spec.get("type", "string"), "string")}
    if js["type"] == "array":
        js["items"] = {"type": "string"}
    if "enum" in spec:
        js["enum"] = spec["enum"]
    if "min" in spec:
        js["minimum"] = spec["min"]
    if "max" in spec:
        js["maximum"] = spec["max"]
    if "desc" in spec:
        js["description"] = spec["desc"]
    return js


def build_schema(m: dict) -> dict:
    base = m["base_fields"]
    branches = []
    for tname, tspec in m["page_types"].items():
        props, required = {}, []
        for fname, fspec in {**base, **tspec.get("fields", {})}.items():
            props[fname] = _field_schema(fspec)
            if fspec.get("required"):
                required.append(fname)
        props["type"] = {"const": tname}
        branches.append({
            "title": tspec["title"],
            "type": "object",
            "properties": props,
            "required": sorted(set(required)),
            "additionalProperties": True,
        })
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://asdlc.dev/knowledge/frontmatter.schema.json",
        "title": f"{m['name']} — page frontmatter",
        "description": "GENERATED from manifest.yaml. Do not edit by hand.",
        "oneOf": branches,
    }


def build_template(tname: str, tspec: dict, m: dict) -> str:
    fields = {**m["base_fields"], **tspec.get("fields", {})}
    lines = ["---"]
    defaults = {
        "id": f"REPLACE-ME-{tname}", "title": "REPLACE ME", "type": tname,
        "status": "draft", "confidence": 0.0, "sources": "[]",
        "created": "YYYY-MM-DD", "updated": "YYYY-MM-DD",
    }
    for fname, fspec in fields.items():
        if fname in defaults:
            val = defaults[fname]
        elif fspec.get("type") == "array":
            val = "[]"
        else:
            val = f"# {fspec.get('desc', '')}"
        req = "" if fspec.get("required") else "   # optional"
        lines.append(f"{fname}: {val}{req}")
    lines.append("---")
    lines.append(f"\n# {{{{title}}}}\n")
    lines.append(f"> {tspec['purpose']}\n")
    lines.append("<!-- Body: human-readable prose. Link with [[page-id]]. "
                 "Cite sources inline. -->\n")
    return "\n".join(lines)


def main() -> int:
    m = load_manifest()
    paths = m["paths"]

    # 1. directories
    (KB_ROOT / paths["raw"]).mkdir(parents=True, exist_ok=True)
    for tspec in m["page_types"].values():
        (KB_ROOT / paths["wiki"] / tspec["folder"]).mkdir(parents=True, exist_ok=True)
    schema_dir = KB_ROOT / paths["schema"]
    tpl_dir = KB_ROOT / paths["templates"]
    schema_dir.mkdir(parents=True, exist_ok=True)
    tpl_dir.mkdir(parents=True, exist_ok=True)

    # 2. JSON Schema
    schema_path = schema_dir / "frontmatter.schema.json"
    schema_path.write_text(json.dumps(build_schema(m), indent=2) + "\n")
    print(f"generated {schema_path.relative_to(KB_ROOT)}")

    # 3. templates
    for tname, tspec in m["page_types"].items():
        tp = tpl_dir / f"{tname}.md"
        tp.write_text(build_template(tname, tspec, m))
        print(f"generated {tp.relative_to(KB_ROOT)}")

    print("scaffold complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
