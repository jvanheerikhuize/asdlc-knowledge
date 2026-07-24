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

1. ~~**Backlinks**~~ — superseded by *Wiki-grade* item 5 ("Referenced by"
   backlinks), which computes the same block at build time with no marker
   comments to drift. See Shipped.
_(All Next items above are now shipped — see below. The remaining roadmap is the
Wiki-grade distribution work.)_

### Wiki-grade distribution (planned)

**Problem.** The `wiki/` source is genuinely wiki-shaped — every page cross-links
its neighbours with `[[page-id]]` / `[[page-id|display]]`. But the *published*
MkDocs site is not: Python-Markdown has no idea what `[[…]]` means, so every
cross-reference renders as dead literal text (`[[llm-wiki-pattern]]`) instead of
a clickable link. The homepage graph is the only way to navigate; individual
pages are leaf documents, not a web. That is the gap between "a folder of
markdown" and "a wiki."

**Design constraint.** Keep the source canonical. The `[[…]]` syntax stays in
`wiki/` untouched (so pages still work in Obsidian/Foam and stay diff-friendly);
all wiki behaviour is *added at build time* from the same manifest + link graph
the linter already walks. No new runtime, no infra — a generated MkDocs hook and
richer `viz.py` output, consistent with everything else here.

Ordered by value-for-effort:

1. **Resolve `[[wikilinks]]` → real links (the core fix).** Add a generated
   MkDocs build hook (`tools/mkdocs_hooks.py`, wired via `hooks:` in the
   `viz.py`-emitted `mkdocs.yml`). On `on_page_markdown`, rewrite each
   `[[id]]` / `[[id|display]]` into a relative Markdown link to
   `../<folder>/<id>.md`, using an id→(folder, title) map built once from the
   wiki tree. `[[id|display]]` keeps its display text; a bare `[[id]]` renders
   the page's real title. Reuses `WIKILINK_RE` from `_common.py` verbatim, so
   the site and `kb lint`'s broken-link check agree by construction. This alone
   turns the site into a navigable wiki.
2. **Wanted-links, not dead text.** An `[[id]]` with no target page renders as a
   distinct "wanted page" span (MediaWiki red-link style) rather than a link or
   raw brackets — the same set `kb lint --broken_links` already reports, now
   visible to a reader instead of only to CI.
3. **Clickable graph.** Make the homepage graph a navigation surface: emit
   Mermaid `click <node> "<url>"` directives so a 2D node jumps to its page, and
   give the 3D `onNodeClick` a shift/modifier path (or a "open page" affordance)
   that navigates to `../<folder>/<id>/`. The graph stops being a picture and
   becomes a map.
4. **Titles in the nav.** `build_mkdocs` currently lists pages by `f.stem` (the
   kebab id). Read each page's frontmatter `title` and use it for the nav label,
   grouped by type — a wiki's sidebar reads in prose, not slugs.
5. **"Referenced by" backlinks (supersedes the standalone Backlinks item
   above).** Append a build-time "Referenced by" block to each page from the
   inbound-link graph — computed in the same hook, so it needs no marker
   comments in source and can't drift. This is the file-clean version of item 1
   in *Next (proposed)*; prefer it for the published site.
6. **Sources as citations.** Render each page's `sources:` frontmatter as a
   linked "Sources" section (source id → its `wiki/sources/<id>` page), so the
   provenance the model already tracks becomes visible, clickable apparatus on
   the page — the thing that makes a wiki trustworthy rather than just linked.
7. **Discovery polish (later).** Tag index pages (Material's `tags` plugin) and
   `aliases:` handled as redirects, so the free-form `tags`/`aliases` frontmatter
   becomes real browse/lookup surfaces.

**Phasing.** Item 1 is the whole ask ("cross-references should be linked") and
ships on its own. 2–4 are small, high-visibility follow-ons in the same hook +
`viz.py` change. 5–6 add the depth (backlinks, citations) that distinguishes a
wiki from a linked document set. 7 is optional discovery polish. Every step is
regenerated from the manifest and the existing link graph, and gated by the same
`mkdocs build --strict` the Publish stage already runs.

### Shipped

- **Near-duplicate warning on ingest.** ✅ Shipped. Checksums only catch a
  byte-identical file re-ingested under the *same* name (a hard skip). Ingest now
  also scans existing source pages and prints a non-blocking `⚠` warning when an
  incoming source shares an existing page's content `checksum` (same document
  re-ingested under a new name) or scores a high id/title similarity (≥ 0.85, a
  lightly-renamed or re-downloaded variant checksums miss). Both are advisory —
  the user may genuinely want a second copy — so ingestion still proceeds; the
  warning just surfaces the likely duplicate instead of silently forking a second
  source page. Reuses `iter_pages` + stdlib `difflib`; no new dependency.
- **URL ingestion — `kb ingest <url>`.** ✅ Shipped. Most new knowledge arrives
  as a link, not a file. `kb ingest <url>` fetches the page once with stdlib
  `urllib` (no new dependency — honours the stdlib+PyYAML constraint), snapshots
  the raw HTML into `raw/` (immutable, so the source stays fixed even if the site
  later changes), and hands the saved `.html` to the ordinary adapter chain,
  where the existing markitdown adapter converts it. The source page records the
  original URL as `origin` and prefers the document's embedded `<title>` over the
  filename stem. Re-running on an already-snapshotted URL reuses the existing raw
  copy, preserving immutability. Reuses the whole ingest pipeline — no new infra.
- **`kb verify --all` + scheduled staleness sweep.** ✅ Shipped. `verify --all`
  classifies every page's verification health (`reverify` / `no-date` / `stale`
  / `unsourced` / `unverified` / `ok`) and prints a triage list, most-actionable
  first — the complement to `kb lint`'s pass/fail gate. `--strict` exits non-zero
  when any page needs attention. A weekly `schedule:` cron on `validate.yml` (and
  the `schedules:` block on `azure-pipelines.yml`) now runs the lint + sweep even
  with no new commits, so the time-relative windows (`verified_max_age_days`,
  `stale_after_days`) actually trip as pages age instead of waiting for a push.
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
