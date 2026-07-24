---
id: knowledge-graph
title: Knowledge Graph
type: concept
status: draft
confidence: 0.6
sources: [graphrag-edge-2024]
created: 2026-07-24
updated: 2026-07-24
category: representation
tags: [knowledge-graph, entities, relationships, structure]
---

# Knowledge Graph

> A structured representation of knowledge as **entities** (nodes) connected by
> typed **relationships** (edges). Where [[embeddings]] capture fuzzy similarity, a
> knowledge graph captures explicit, queryable structure — the basis of
> [[graph-rag]].

## Structure
Facts are stored as triples — *(subject, predicate, object)*, e.g.
*(Patrick Lewis, co-authored, DPR)*. Nodes and edges can carry attributes, and the
graph can be queried by traversal (following relationships) rather than by
similarity alone.

## Why LLMs use them
- **Multi-hop reasoning** — answer questions that require chaining several facts.
- **Aggregation** — [[graph-rag|GraphRAG]] clusters the graph into communities and
  summarises each, enabling *global* questions plain
  [[retrieval-augmented-generation]] cannot answer.
- **Provenance & consistency** — explicit edges make contradictions and sources
  visible.

## Relation to a wiki
An [[llm-wiki-pattern|LLM wiki]]'s wiki-links form a lightweight, human-
readable knowledge graph: pages are nodes, links are edges. This knowledge base's
`kb viz` renders exactly that graph, tying the idea back to
[[knowledge-management-for-llms]] and [[zettelkasten]].
