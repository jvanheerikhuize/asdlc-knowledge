---
id: knowledge-management-for-llms
title: Knowledge Management for LLMs
type: concept
status: draft
confidence: 0.6
sources: [llm-wiki-setup-guide-2026, karpathy-llm-wiki]
created: 2026-07-24
updated: 2026-07-24
category: knowledge-management
tags: [hub, knowledge-management, rag, memory]
---

# Knowledge Management for LLMs

> The umbrella problem of giving language models durable, trustworthy access to
> knowledge they were not trained on. This page is the **hub** for the cluster:
> it connects the storage-and-retrieval branch ([[retrieval-augmented-generation]],
> [[embeddings]], [[vector-database]], [[semantic-search]]), the
> structure branch ([[knowledge-graph]], [[graph-rag]], [[zettelkasten]]), the
> authoring branch ([[llm-wiki-pattern]], [[context-engineering]]), and the
> agent-facing branch ([[agentic-memory]], [[model-context-protocol]]).

## Why it exists
An LLM's weights are a lossy, frozen snapshot. To answer questions about private,
recent, or high-stakes information it needs an **external** knowledge store that
is current, attributable, and cheap to update. The field spans two broad styles:

- **Retrieval-first (horizontal):** index a large corpus and fetch relevant
  fragments at query time — [[retrieval-augmented-generation]] over a
  [[vector-database]], using [[embeddings]] and [[semantic-search]], often refined
  with [[reranking]], [[hybrid-search]], and [[chunking]] strategy.
- **Curated / structured (vertical):** maintain a deliberately organised body of
  knowledge — an [[llm-wiki-pattern|LLM wiki]], a [[knowledge-graph]], or
  [[zettelkasten]]-style linked notes — that the model reads and edits.

## The quality problems it must solve
- **[[hallucination]]** — grounding output in retrieved evidence, and checking it
  (see [[self-rag-asai-2023|Self-RAG]]).
- **Staleness & provenance** — every claim traceable to a source, with an age;
  the discipline this very knowledge base enforces via its lint gates.
- **Scale limits** — flat context and flat retrieval both degrade; structure
  (directory indexes, graphs, community summaries) restores it.

## Where the pieces fit
[[embeddings]] turn text into vectors → stored in a [[vector-database]] indexed
with [[approximate-nearest-neighbor]] methods → queried by [[semantic-search]] →
assembled into a prompt by [[context-engineering]] → generated and grounded by
[[retrieval-augmented-generation]]. When relationships matter more than
similarity, a [[knowledge-graph]] and [[graph-rag]] take over. When the consumer
is an autonomous agent, [[agentic-memory]] and [[model-context-protocol]] frame
the same store as long-term memory and a tool interface. The
[[asdlc-knowledge-base]] is one concrete implementation of the curated style.
