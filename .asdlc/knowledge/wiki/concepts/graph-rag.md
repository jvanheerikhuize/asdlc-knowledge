---
id: graph-rag
title: GraphRAG
type: concept
status: draft
confidence: 0.6
sources: [graphrag-edge-2024]
created: 2026-07-24
updated: 2026-07-24
category: retrieval
tags: [graph-rag, rag, knowledge-graph]
---

# GraphRAG

> A retrieval style that runs [[retrieval-augmented-generation]] over an
> LLM-constructed [[knowledge-graph]] instead of a flat set of text chunks.
> Introduced by [[microsoft-research]] in [[graphrag-edge-2024]].

## How it differs from baseline RAG
Baseline RAG fetches the top-k similar [[chunking|chunks]] via [[semantic-search]]
— excellent for *local* questions, poor for *global* ones that span the whole
corpus. GraphRAG instead:
1. extracts entities/relationships into a [[knowledge-graph]];
2. clusters the graph into **communities**;
3. pre-summarises each community;
4. answers global queries by map-reduce over those summaries.

## Trade-offs
- **Pro:** far more comprehensive answers to "what are the themes?" style
  questions; built-in provenance via graph structure.
- **Con:** an expensive up-front indexing pass (many LLM calls to build the graph
  and summaries); heavier to keep current than a vector index.

Part of the "structured retrieval" answer to
[[knowledge-management-for-llms|LLM knowledge management]], alongside adaptive
methods like [[self-rag-asai-2023|Self-RAG]].
