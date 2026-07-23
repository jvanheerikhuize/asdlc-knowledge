# LLM Wiki (source: gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

An alternative to RAG: instead of rediscovering knowledge on each query, an LLM
incrementally builds and maintains a persistent wiki — a structured, interlinked
collection of markdown files. Knowledge is compiled once and kept current.

Three layers: raw sources (immutable), the wiki (LLM-maintained markdown), and
the schema (a config document like CLAUDE.md encoding conventions/workflows).

Three operations: Ingest (read a new source, extract takeaways, write a summary
page, update index, revise 10-15 entity/concept pages, log it); Query (search
pages, synthesise an answer with citations, optionally file the analysis back);
Lint (health-check for contradictions, stale claims, orphan pages, missing
cross-references, data gaps).

Supplementary files: index.md (catalog for navigation) and log.md (append-only
record of changes). "The tedious part of maintaining a knowledge base is not the
reading or the thinking — it's the bookkeeping," which is exactly what LLMs are
good at.
