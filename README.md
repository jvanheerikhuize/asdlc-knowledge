# ASDLC Knowledge Base

A **persistent, file-based knowledge base** for AI-assisted software delivery,
implementing Andrej Karpathy's ["LLM wiki"](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
pattern: knowledge is *compiled once* into an interlinked markdown wiki and kept
current by an agent — rather than re-derived from scratch on every query (RAG).

Everything lives in [`.asdlc/knowledge/`](.asdlc/knowledge/). It is plain files —
no database, no server, no infrastructure. Humans read it in any editor or on
GitHub; agents read and maintain it through one entry point.

## Why

> "The tedious part of maintaining a knowledge base is not the reading or the
> thinking — it's the bookkeeping." — Karpathy

That bookkeeping is exactly what an agent does well. This repo gives the agent a
**schema**, a **toolchain**, and a **contract** so the wiki stays consistent,
sourced, and trustworthy over time.

## Layout

| Path | Role |
|------|------|
| `.asdlc/knowledge/manifest.yaml` | **Single source of truth.** Defines page types, fields, confidence policy, ingestion + viz config. |
| `.asdlc/knowledge/AGENTS.md` | **Single entry point** for any agent — vendor-neutral contract of how to read/write the KB. |
| `.asdlc/knowledge/index.md` | Human/agent catalog, auto-rebuilt from page frontmatter. |
| `.asdlc/knowledge/log.md` | Append-only change log. |
| `.asdlc/knowledge/inbox/` | Drop-zone for new files. `kb ingest` (no args) empties it into `raw/`. |
| `.asdlc/knowledge/raw/` | Immutable ingested source artifacts. Never edited. |
| `.asdlc/knowledge/wiki/` | The LLM-maintained wiki: `sources/`, `entities/`, `concepts/`. |
| `.asdlc/knowledge/_schema/` | JSON Schema generated from the manifest. |
| `.asdlc/knowledge/_templates/` | Page templates generated from the manifest. |
| `.asdlc/knowledge/ingest/` | Pluggable binary-ingestion adapters (plaintext, MarkItDown, Docling). |
| `.asdlc/knowledge/tools/` | The `kb` CLI — the interaction interface. |

## Quickstart

```bash
pip install -e ".[all]"          # or just: pip install pyyaml
cd .asdlc/knowledge

python3 tools/kb.py scaffold      # regenerate schema + templates from manifest
python3 tools/kb.py new <type> <id> [--title "..."]  # stamp a new page from its template
python3 tools/kb.py search <term> # ranked grep over frontmatter + body, with excerpts
python3 tools/kb.py ingest        # drop file(s) in inbox/, then batch-ingest them all
python3 tools/kb.py ingest <file> # or convert one explicit binary/text source
python3 tools/kb.py index         # rebuild index.md from frontmatter
python3 tools/kb.py lint          # deterministic health checks
python3 tools/kb.py verify <id>   # assemble a page + sources for fact-checking
python3 tools/kb.py viz           # regenerate mkdocs.yml + the Mermaid graph
mkdocs build                      # render the static visualization site
```

## The `kb` operations

- **scaffold** — regenerate `_schema/` and `_templates/` from `manifest.yaml`. Run in CI on manifest change.
- **new** — stamp a page from `_templates/<type>.md` with `id`, today's dates, and `status: draft` pre-filled.
- **search** — ranked grep over frontmatter + body; prints page ids with matching excerpts.
- **ingest** — with no args, batch-ingest everything dropped in `inbox/` (copy into `raw/`, convert, scaffold a `source` page, clear the inbox); with a path, ingest that one file. Auto-uses a local `.venv` for the optional adapters, so a single command "just works".
- **index** — rebuild the catalog blocks in `index.md`.
- **lint** — schema, broken-link, orphan, unsourced, confidence-cap, and staleness checks.
- **verify** — assemble a page with its cited sources so an agent can fact-check it.
- **viz** — emit `mkdocs.yml` + a confidence-colored Mermaid link graph.
- **purge** — empty the KB back to a clean state (dry-run by default; `--yes` to apply, `--raw`/`--wiki` to scope one layer).

## Confidence & fact-checking

Every page carries a `confidence` (0–1), a `status`
(`draft`/`verified`/`stale`/`disputed`), and `last_verified`. The policy in
`manifest.yaml` caps unsourced claims, ages out verifications, and bands
confidence (high/medium/low) — enforced deterministically by `lint` and
judged at the claim level by `verify`. See `AGENTS.md` §5.

## Design

See [`PLAN.md`](PLAN.md) for the research and plan, and
[`SOLUTION.md`](SOLUTION.md) for the solution design and how each requirement is met.

## License

MIT — see [LICENSE](LICENSE).
