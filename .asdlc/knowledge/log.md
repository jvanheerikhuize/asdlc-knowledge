---
title: Activity Log
description: Append-only, chronological record of KB operations. Newest at top.
---

# Log

Format: `## [YYYY-MM-DD] operation | Title` followed by a short note.

## [2026-07-23] ingest | ASDLC Knowledge Base (self-describe)
Ingested the repo's own README into [[asdlc-knowledge-readme]] and added the
[[asdlc-knowledge-base]] system entity, linked to [[llm-wiki-pattern]],
[[retrieval-augmented-generation]], and [[andrej-karpathy]]. The KB now
documents itself.

## [2026-07-23] ingest | Retrieval-Augmented Generation (Lewis et al. 2020)
Ingested arXiv:2005.11401 into [[rag-lewis-2020]]. Added the
[[retrieval-augmented-generation]] concept (contrasted with [[llm-wiki-pattern]])
and the [[patrick-lewis]] entity, with bidirectional links.

## [2026-07-23] scaffold | Initial knowledge base
Bootstrapped the KB from `manifest.yaml`. Generated schema, templates, and the
three seed pages demonstrating the ingest -> wiki -> confidence flow.

## [2026-07-23] ingest | Karpathy LLM-wiki gist
Ingested the source gist defining the pattern. Created [[karpathy-llm-wiki]],
[[andrej-karpathy]], and [[llm-wiki-pattern]] with cross-links.
