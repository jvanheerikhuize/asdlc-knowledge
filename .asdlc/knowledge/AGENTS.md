# AGENTS.md — Single Point of Entry

> **You are the maintainer of this knowledge base.** Read this file fully before
> doing anything. It is agent-agnostic and tool-agnostic: any coding/agent
> runtime (Claude Code, Cursor, Copilot, Aider, a cron job, a human) operates
> the KB through the same contract described here. This is the equivalent of the
> `CLAUDE.md` "schema" in the LLM-wiki pattern — but vendor-neutral.

## 1. What this is

A **persistent, file-based wiki** that an agent builds and maintains. Instead of
re-deriving knowledge on every query (RAG), knowledge is *compiled once* into
interlinked markdown and kept current. Three layers:

| Layer      | Directory        | Who writes it        | Mutability |
|------------|------------------|----------------------|------------|
| Raw        | `raw/`           | Humans / ingestion   | **Immutable** — never edit |
| Wiki       | `wiki/`          | You (the agent)      | Continuously maintained |
| Schema     | `manifest.yaml` + this file | Humans   | The rules you obey |

`manifest.yaml` is the **single source of truth**. The directory layout,
frontmatter schema, templates, lint rules, and viz config are all *generated*
from it via `tools/scaffold.py`. If a rule here conflicts with `manifest.yaml`,
the manifest wins.

## 2. The operations (your job)

Everything you do is one of six verbs. Each has a CLI entry (`tools/kb.py`)
that handles the deterministic bookkeeping; you provide the judgement.

### `ingest` — a new source arrived
1. A file lands in `inbox/` (drop-zone) or `raw/`. Run `kb ingest` with no args
   to batch-ingest the whole inbox — each file is copied into `raw/`, converted,
   and given a draft source page — or `kb ingest <path>` for one explicit file.
2. Steps 1's scaffolding writes one **source page** per file under `wiki/sources/`
   (`origin`, `media_type`, `ingested_with`, `checksum` are filled in for you).
   The pages land as `status: draft` — the steps below turn them into real wiki.
3. Read the extracted text. Update **entity** and **concept** pages it touches
   (typically 10–15 pages). Add `[[wikilinks]]` both ways.
4. For every claim you write on an entity/concept page, add the source page's
   `id` to that page's `sources:` list.
5. Append one line to `log.md`: `## [YYYY-MM-DD] ingest | <source title>`.
6. Run `kb lint` and fix what you introduced.

### `query` — someone asks a question
1. Search `wiki/` (grep/index) for relevant pages; read them.
2. Synthesise an answer **with citations** to page ids and their `sources`.
3. State confidence honestly. If pages disagree, say so and mark them
   `status: disputed`.
4. If the analysis is durably useful, file it back as a new wiki page rather
   than letting it vanish into chat history.

### `lint` — health check
Run `kb lint`. It reports: schema violations, orphan pages, broken wikilinks,
unsourced claims, stale pages, and confidence-cap violations. Fix or file
follow-ups. This is safe to run in CI (see `.github/workflows/validate.yml`).

### `verify` — fact-check & (re)score confidence
1. For a page, re-read every source in its `sources:` list from `raw/`.
2. Check each claim is actually supported. Downgrade/annotate unsupported ones.
3. Set `confidence` per the rubric in §5 and update `last_verified` to today.
4. If all claims hold and coverage is good, set `status: verified`.
`kb verify <page>` prints the claims + cited source excerpts to check against;
the *judgement* is yours, the *scoring math and caps* are enforced by the tool.

### `scaffold` — regenerate structure from the manifest
Run `kb scaffold` after editing `manifest.yaml`. Idempotent. Never hand-edit
files under `_schema/` or `_templates/` — change the manifest and re-run.

### `purge` — empty the KB back to a clean state
`kb purge` clears `raw/` and the `wiki/` page folders and regenerates the
derived views (`index.md` blocks, `wiki/index.md`, `mkdocs.yml`); the manifest,
schema, templates, `AGENTS.md`, and `tools/` are left untouched. It is **dry-run
by default** — it prints what it would remove and changes nothing until you pass
`--yes`. Scope it with `--raw` or `--wiki` to purge a single layer. This is
destructive: confirm you mean it before adding `--yes`.

## 3. Page conventions

- One page = one file = one stable `id` (kebab-case, also the filename).
- Every page starts with YAML frontmatter matching `_schema/frontmatter.schema.json`.
- Link with `[[page-id]]` or `[[page-id|display text]]`.
- Keep prose human-readable: short sections, tables over walls of text.
- Cite inline where a claim is non-obvious: `... (see [[source-id]])`.

## 4. Ingestion layer (binaries)

Binaries never go into `wiki/`. They are converted at the boundary by a
pluggable adapter implementing `ingest/adapters/base.py::IngestAdapter`.
Priority order and default come from `manifest.yaml -> ingest`. Shipped
adapters: `plaintext`, `markitdown` (Microsoft), `docling` (IBM). Add your own
by dropping a module in `ingest/adapters/` — the interface is the only contract.

## 5. Confidence rubric (0.0–1.0)

Start from source quality and coverage, then apply policy caps from
`manifest.yaml -> confidence_policy`:

- **0.75–1.0 (high)** — multiple independent sources, recently verified, no
  known contradictions.
- **0.45–0.74 (medium)** — a single credible source, or verified but aging.
- **0.0–0.44 (low)** — inference, weak/secondary sourcing, or unverified.
- **Hard cap:** a page with an empty `sources:` list is capped at
  `unsourced_confidence_cap` (0.3). The linter enforces this.

## 6. Guardrails

- Never modify anything under `raw/`.
- Never invent a source id. If you have no source, say so and keep confidence low.
- Prefer updating an existing page over creating a near-duplicate.
- Every content change gets a `log.md` line and bumps `updated:`.
- Leave the tree green: `kb lint` must pass before you consider work done.
