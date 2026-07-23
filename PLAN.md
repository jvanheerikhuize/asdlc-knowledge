# Plan & Research

## 1. The brief

Build a persistent, file-based knowledge base implementing Karpathy's "LLM wiki"
pattern. Hard requirements (from the original goal):

1. Human-readable.
2. Scaffolds from a **single source of truth**; scaffolder triggerable from a pipeline/action.
3. File-based — no infrastructure.
4. Closest to current industry standards.
5. Lives in `.asdlc/knowledge`.
6. A single point of entry for an agent.
7. Solution- and agent-agnostic.
8. An ingestion layer for binaries, behind an interface.
9. A visualization layer.
10. An interface to interact with the KB.
11. Fact-checking and confidence scoring.

## 2. Research

### The source pattern — Karpathy's "LLM wiki"
An alternative to RAG: instead of re-deriving knowledge per query, an LLM
incrementally builds and maintains a persistent, interlinked markdown wiki.
- **Three layers:** raw sources (immutable) · wiki (LLM-maintained markdown) · schema (config/conventions).
- **Three operations:** ingest · query · lint.
- **Supporting files:** `index.md` (catalog) and `log.md` (append-only history).

### Industry-standard building blocks chosen (2026)
- **`AGENTS.md`** as the agent entry point — a vendor-neutral, widely-adopted
  convention for "how an agent should work in this repo", so requirement (7)
  agent-agnostic is satisfied without tying to any one vendor's `CLAUDE.md`/rules file.
- **YAML frontmatter + `[[wikilinks]]`** — the de-facto markdown knowledge
  convention (Obsidian/Foam/Dendron), readable by humans and trivially parseable.
- **JSON Schema (draft 2020-12)** — the standard for validating the frontmatter,
  *generated* from the manifest so there's a single source of truth.
- **Binary → markdown ingestion:** Microsoft **MarkItDown** (fast, broad format
  coverage) and IBM **Docling** (best fidelity on tables/formulas/multi-column
  PDFs) are the two leading open converters; plus a stdlib **plaintext** fallback.
  All are optional, lazy-imported backends behind one adapter interface.
- **Visualization:** **MkDocs Material** static-site generator + a **Mermaid**
  link graph — renders to static HTML (GitHub Pages), no runtime server.

### Confidence & fact-checking approach
Two complementary layers:
- **Structural** (deterministic): enforced by `lint` — schema validity, no broken
  links, no orphans, sourced claims, confidence caps, staleness windows.
- **Claim-level** (judgement): `verify` assembles a page with its cited raw
  sources so an agent can check each claim against evidence and set confidence
  per a documented rubric.

## 3. Approach

Drive *everything* from `manifest.yaml`. The `scaffold` operation reads the
manifest and generates the JSON Schema and page templates; `lint`, `index`, and
`viz` all read the same manifest. Change the manifest, re-run scaffold, and the
schema/templates/checks move with it — satisfying requirement (2).

Expose all operations through one CLI, `kb` — the interaction interface (10) —
whose prose contract for agents lives beside it in `AGENTS.md` (6).

## 4. Requirement → artifact map

| # | Requirement | Where it's met |
|---|-------------|----------------|
| 1 | Human-readable | Plain markdown + YAML; `index.md`; MkDocs site |
| 2 | Single source of truth + scaffolder in pipeline | `manifest.yaml` → `kb scaffold`; `azure-pipelines.yml` (ScaffoldDrift) / `.github/workflows/scaffold.yml` |
| 3 | File-based, no infra | Only files; CLI is stdlib + PyYAML |
| 4 | Industry standard | AGENTS.md, JSON Schema, frontmatter/wikilinks, MarkItDown/Docling, MkDocs Material |
| 5 | Lives in `.asdlc/knowledge` | Entire KB rooted there |
| 6 | Single agent entry point | `AGENTS.md` |
| 7 | Solution/agent-agnostic | Vendor-neutral AGENTS.md; adapters/CLI are generic |
| 8 | Binary ingestion interface | `ingest/adapters/` `IngestAdapter` protocol; `kb ingest` |
| 9 | Visualization layer | `kb viz` → `mkdocs.yml` + Mermaid graph |
| 10 | Interaction interface | `kb` CLI (`tools/kb.py`) |
| 11 | Fact-check + confidence | `manifest.yaml` `confidence_policy`; `kb lint` + `kb verify` |

## 5. Validation done

All six operations run clean on the seed content: `scaffold`, `ingest`, `index`,
`lint` (0 issues), `verify`, `viz`. Three seed pages (`karpathy-llm-wiki`,
`andrej-karpathy`, `llm-wiki-pattern`) are cross-linked and sourced to the
ingested raw gist.

## 6. Roadmap

### Next (proposed)

Ordered by value-for-effort; each follows the existing manifest-driven,
stdlib+PyYAML, no-infra pattern.

1. **Backlinks** — `kb index` (or a new `kb backlinks`) appends a generated
   "Referenced by" block to each page (marker comments, like `index.md`).
   Makes the graph navigable from any page, not just the homepage.
2. **`kb verify --all` + scheduled staleness sweep** — iterate verify output
   over every page, and add a weekly `schedule:` trigger to `validate.yml` so
   `verified_max_age_days`/`stale_after_days` actually fire over time, not only
   when someone happens to push.
3. **URL ingestion** — let `kb ingest <url>` fetch and snapshot a web page into
   `raw/` (markitdown already converts HTML). Most new knowledge arrives as
   links, not files.
4. **Near-duplicate warning on ingest** — checksums already catch identical
   files; add a slug/title-similarity warning so re-ingesting the same document
   under a new name gets flagged instead of silently forking a second source page.

### Shipped

- **`kb search <term>` — ranked grep over frontmatter + body.** ✅ Shipped.
  Scores every page by where the term hits (id > title > other frontmatter >
  body), prints ranked page ids with a matching excerpt. The CLI half of the
  `query` verb in `AGENTS.md`, replacing ad-hoc `grep`.
- **`kb new <type> <id>` — stamp a page from its template.** ✅ Shipped. Fills
  in `id`, `title`, today's `created`/`updated`, and `status: draft` from
  `_templates/<type>.md`, writing straight into `wiki/<folder>/<id>.md`.
  Removes the manual bookkeeping when starting an entity/concept page by hand
  (as opposed to `kb ingest`, which stamps a source page from a file). Also
  fixed two latent bugs the first real use of the templates surfaced: optional
  blank fields (`key: # comment`) were serializing as YAML `null`, which
  failed the generated schema's `type: string` checks; and the template's
  instructional `[[page-id]]` example was itself a wikilink, tripping the
  broken-link linter on every stamped page.
- **`kb purge` — easily purge the contents.** ✅ Shipped. A single command
  empties the knowledge base back to a clean, scaffolded state: it clears `raw/`
  and the `wiki/` page folders, resets the generated views (`index.md` marker
  blocks, `wiki/index.md`, `mkdocs.yml`), and leaves `manifest.yaml`,
  `AGENTS.md`, and `tools/` untouched. It is guarded behind a `--yes`
  confirmation (dry-run by default, printing what would be removed) so a purge
  is never accidental, and `--raw`/`--wiki` scope it to one layer. Follows the
  same manifest-driven, no-infra pattern as the existing operations.
