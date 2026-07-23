---
id: karpathy-llm-wiki
title: "Karpathy — LLM Wiki gist"
type: source
status: verified
confidence: 0.9
sources: [karpathy-llm-wiki]
created: 2026-07-23
updated: 2026-07-23
last_verified: 2026-07-23
origin: raw/karpathy-llm-wiki.md
media_type: text
ingested_with: plaintext
tags: [pattern, knowledge-management, llm]
---

# Karpathy — LLM Wiki gist

> The originating source for this knowledge base's design. Defines the
> "persistent LLM wiki" pattern as an alternative to RAG.

Andrej Karpathy (see [[andrej-karpathy]]) describes the [[llm-wiki-pattern]]:
knowledge is compiled once into an interlinked markdown wiki and kept current,
rather than re-derived per query. It defines three layers (raw / wiki / schema)
and three operations (ingest / query / lint), with `index.md` and `log.md` as
supporting files.

Key quote: *"The tedious part of maintaining a knowledge base is not the reading
or the thinking — it's the bookkeeping."*

Original: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
