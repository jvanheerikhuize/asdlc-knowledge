# Solution Design

## Overview

The ASDLC Knowledge Base is a **data-first repository**: the knowledge is a tree
of plain markdown files, and a small stdlib+PyYAML toolchain keeps that tree
consistent. Nothing runs as a service. The whole system is four moving parts:

1. **Manifest** — the single source of truth (`manifest.yaml`).
2. **Generated schema & templates** — derived from the manifest (`_schema/`, `_templates/`).
3. **The wiki** — human/agent-authored content (`raw/`, `wiki/`, `index.md`, `log.md`).
4. **The toolchain** — `kb` CLI + ingestion adapters, plus the `AGENTS.md` contract.

```
.asdlc/knowledge/
├── manifest.yaml         # (1) single source of truth
├── AGENTS.md             # agent entry point / contract
├── index.md              # catalog (generated blocks)
├── log.md                # append-only history
├── _schema/              # (2) JSON Schema, generated
├── _templates/           # (2) page templates, generated
├── raw/                  # (3) immutable sources
├── wiki/                 # (3) sources/ entities/ concepts/ + _graph.md
├── ingest/               # (4) adapter interface + backends
└── tools/                # (4) kb CLI: scaffold/ingest/index/lint/verify/viz
```

## 1. Single source of truth → scaffolding

`manifest.yaml` declares: page types and their extra fields, base fields, the
confidence policy, lint toggles, ingestion adapter order, and viz config.

`kb scaffold` reads it and (re)generates:
- `_schema/frontmatter.schema.json` — a `oneOf` over page types (draft 2020-12),
  `required` derived from base + per-type fields.
- `_templates/<type>.md` — a ready-to-fill page per type.

Because schema and templates are *generated*, they can never drift from the
manifest. CI re-runs scaffold on any manifest change and fails if the working
tree then differs (see `.github/workflows/scaffold.yml`) — this is how the
"scaffolder triggerable from a pipeline" requirement is enforced, not just offered.

## 2. Agent entry point & agnosticism

`AGENTS.md` is the one document an agent reads first. It is deliberately
vendor-neutral (the `AGENTS.md` convention, not a `CLAUDE.md`/Cursor/Copilot-specific
file), so any agent or human follows the same contract. It documents the layers,
the six operations, the page conventions, the confidence rubric, and hard
guardrails (never edit `raw/`, never invent source IDs). The *interaction* happens
through the `kb` CLI, which is equally agent- and human-usable.

## 3. Page model

Every page is markdown with YAML frontmatter and `[[wikilinks]]` in the body.
Base fields: `id, title, type, status, confidence, sources, created, updated,
last_verified, tags`. Page types add fields:
- **source** — `origin, media_type, ingested_with, checksum`
- **entity** — `entity_type, aliases`
- **concept** — `category`

`status ∈ {draft, verified, stale, disputed}`; `confidence ∈ [0,1]`.

## 4. Ingestion layer (binaries, behind an interface)

`ingest/adapters/base.py` defines the contract:

```python
class IngestAdapter(Protocol):
    name: str
    def accepts(self, path: Path, media_type: str | None) -> bool: ...
    def extract(self, path: Path) -> IngestResult: ...   # -> markdown + checksum + meta
```

Three shipped backends, all optional and lazy-imported:
- **plaintext** — stdlib, always available; `.md/.txt/...`.
- **markitdown** — Microsoft MarkItDown; broad, fast Office/PDF/HTML → markdown.
- **docling** — IBM Docling; highest fidelity for complex PDFs (tables/formulas).

`kb ingest <file>` walks the manifest's adapter order, picks the first that
`accepts()` the file, calls `extract()`, and writes a `source` page under
`wiki/sources/` with a sha256 checksum linking it to the immutable `raw/` copy.
Adding a format = dropping in a new adapter class; nothing else changes.

## 5. Fact-checking & confidence

Defined once in `manifest.yaml` → `confidence_policy`:
- `unsourced_confidence_cap` (0.3) — a page with empty `sources[]` cannot claim more.
- `verified_max_age_days` (180) — a `verified` page older than this is flagged.
- `stale_after_days` (365) — untouched pages are flagged stale.
- **bands** — high ≥ 0.75, medium ≥ 0.45, low ≥ 0 (with colors for viz).

Two enforcement layers:
- **`kb lint`** (deterministic) — JSON-Schema validation, broken `[[links]]`,
  orphans, unsourced pages, confidence-cap violations, and age/staleness. Exit
  non-zero under `--strict` for CI gating.
- **`kb verify <id>`** (judgement) — assembles the page plus its cited raw
  sources and a checklist so an agent fact-checks each claim and sets confidence
  per the AGENTS.md §5 rubric, then logs it.

## 6. Visualization layer

`kb viz` emits:
- `mkdocs.yml` — MkDocs Material config (search, navigation).
- `wiki/_graph.md` — a Mermaid graph of pages linked by `[[wikilinks]]`, nodes
  colored by confidence band.

`mkdocs build` renders a static HTML site (publishable to GitHub Pages via
`.github/workflows/publish.yml`). No server, consistent with the file-based
constraint. `_graph.md` is a generated *view* and is excluded from page linting.

## 7. Interaction interface

`tools/kb.py` is the single CLI dispatching all six operations. It is the
programmatic surface for humans and agents alike; `AGENTS.md` is its prose
counterpart. All logic is stdlib + PyYAML, with optional extras (jsonschema,
markitdown, docling, mkdocs-material) declared in `pyproject.toml`.

## 8. CI/CD

- `scaffold.yml` — on manifest change, re-run scaffold; fail if artifacts drift.
- `validate.yml` — run `kb lint --strict` on every push/PR.
- `publish.yml` — build the MkDocs site and deploy to GitHub Pages.

## 9. Verification

All operations were run against the seed content and lint reports **0 issues**
across the three seed pages, which are mutually cross-linked and sourced to the
ingested Karpathy gist in `raw/`.
