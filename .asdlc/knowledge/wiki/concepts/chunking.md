---
id: chunking
title: Chunking
type: concept
status: draft
confidence: 0.55
sources: [llm-wiki-setup-guide-2026, dpr-karpukhin-2020]
created: 2026-07-24
updated: 2026-07-24
category: retrieval
tags: [chunking, preprocessing, retrieval]
---

# Chunking

> Splitting documents into retrievable units before [[embeddings|embedding]] them.
> Chunk boundaries silently determine what [[semantic-search]] can and cannot
> return, making chunking one of the highest-leverage — and most underrated —
> knobs in [[retrieval-augmented-generation]].

## Strategies
- **Fixed-size** — every N tokens with some overlap; simple, but cuts across ideas.
- **Structural** — split on headings, paragraphs, or sentences to keep coherent
  units. A [[llm-wiki-pattern|wiki]] page or section is a natural chunk.
- **Semantic** — group sentences by embedding similarity so each chunk is one
  topic.
- **Hierarchical / late** — index small chunks but return their larger parent for
  context.

## The tension
Chunks too **small** lose context and split answers across fragments; too **large**
dilute the [[embeddings|embedding]] and blow the context budget. This connects to
[[context-engineering]] (what finally reaches the model) and to why a curated
[[knowledge-graph]] or wiki sidesteps chunking entirely — nodes are the units.
