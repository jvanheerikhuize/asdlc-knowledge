---
id: approximate-nearest-neighbor
title: Approximate Nearest Neighbor Search
type: concept
status: draft
confidence: 0.65
sources: [hnsw-malkov-2016, faiss-johnson-2017]
created: 2026-07-24
updated: 2026-07-24
category: algorithm
tags: [ann, indexing, algorithm, vector-search]
---

# Approximate Nearest Neighbor Search

> Algorithms that find *almost* the closest [[embeddings]] to a query vector,
> trading a small amount of recall for enormous speed. Exact nearest-neighbour
> search is too slow at scale, so ANN is what makes a [[vector-database]] and
> [[semantic-search]] practical.

## Main families
- **Graph-based** — [[hnsw-malkov-2016|HNSW]] builds a navigable multi-layer
  proximity graph; best recall/latency, higher memory.
- **Inverted-file (IVF)** — partition vectors into clusters, search only the
  nearest few; from the [[faiss-johnson-2017|FAISS]] line.
- **Quantization** — product quantization compresses vectors so billion-scale
  indexes fit in memory, at some accuracy cost.
- **Hashing** — locality-sensitive hashing; simpler but generally lower recall.

## The core trade-off
Three knobs pull against each other: **recall**, **latency**, and **memory**. HNSW
favours recall and latency at memory cost; IVF+PQ favours memory. Tuning them is
the main operational task in running [[knowledge-management-for-llms|LLM
retrieval infrastructure]].
