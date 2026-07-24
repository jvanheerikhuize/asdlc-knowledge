---
id: markitdown
title: MarkItDown
type: entity
entity_type: system
status: draft
confidence: 0.55
sources: [asdlc-knowledge-readme, llm-wiki-setup-guide-2026]
created: 2026-07-24
updated: 2026-07-24
aliases: [markitdown]
tags: [tool, ingestion, markdown]
---

# MarkItDown

> A utility that converts documents (PDF, Office files, HTML, images) into Markdown
> suitable for LLM ingestion — one of the ingestion adapters in the
> [[asdlc-knowledge-base]].

## Relevance to this cluster
Turning raw sources into clean Markdown is the first step of the curated
[[knowledge-management-for-llms|knowledge-management]] pipeline: the
[[llm-wiki-pattern|wiki]] layer is only as good as what enters `raw/`. MarkItDown
(and the alternative [[docling]]) handles that conversion in the
[[asdlc-knowledge-base]]; the [[llm-wiki-setup-guide-2026]] source itself was a PDF
ingested this way.
