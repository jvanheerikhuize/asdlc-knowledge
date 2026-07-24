---
id: docling
title: Docling
type: entity
entity_type: system
status: draft
confidence: 0.55
sources: [asdlc-knowledge-readme]
created: 2026-07-24
updated: 2026-07-24
aliases: []
tags: [tool, ingestion, document-parsing]
---

# Docling

> A document-parsing toolkit that converts complex documents (with tables, layout,
> and structure) into structured Markdown/JSON for LLM use — the higher-fidelity
> ingestion adapter in the [[asdlc-knowledge-base]], alongside [[markitdown]].

## Relevance to this cluster
Docling handles layout-rich PDFs where structure matters (tables, columns, reading
order), feeding clean text into the [[chunking]] and [[embeddings]] steps of a
retrieval pipeline, or into the `raw/` layer of the [[llm-wiki-pattern|wiki]]. It
is part of the ingestion front end of
[[knowledge-management-for-llms|knowledge management]] in this repo.
