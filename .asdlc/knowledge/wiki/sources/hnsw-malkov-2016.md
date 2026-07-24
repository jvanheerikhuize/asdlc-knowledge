---
id: hnsw-malkov-2016
title: "Efficient and Robust ANN Search Using Hierarchical Navigable Small World Graphs"
type: source
status: verified
confidence: 0.75
sources: [hnsw-malkov-2016]
created: 2026-07-24
updated: 2026-07-24
last_verified: 2026-07-24
origin: https://arxiv.org/abs/1603.09320
media_type: pdf
author: "Yu A. Malkov, Dmitry A. Yashunin"
published: 2016-03-30
url: https://arxiv.org/abs/1603.09320
tags: [ann, vector-search, indexing, algorithm]
---

# Efficient and Robust ANN Search Using Hierarchical Navigable Small World Graphs

> The paper introducing **HNSW** ([[yury-malkov]] & Dmitry Yashunin, 2016), the
> graph index that became the default algorithm for
> [[approximate-nearest-neighbor]] search in nearly every modern
> [[vector-database]]. Later published in IEEE TPAMI (2018).

## Idea
HNSW builds a multi-layer proximity graph. Upper layers are sparse (long-range
links for fast traversal); lower layers are dense (short-range links for
accuracy). A search greedily descends from an entry point in the top layer to the
target's neighbourhood in the bottom layer — giving **logarithmic-scaling**
search complexity.

## Why it matters
- **State-of-the-art recall/speed trade-off** on high-dimensional vectors,
  outperforming earlier tree- and hashing-based methods.
- **Incremental** — vectors can be inserted without rebuilding the whole index.
- Ships in [[faiss]], and underpins pgvector, Qdrant, Weaviate, Milvus, and
  Elasticsearch's vector search. It is the workhorse behind [[semantic-search]]
  and [[embeddings]]-based retrieval at scale.

## Known trade-offs
High memory footprint (the graph links are stored alongside the vectors) and
slower index build than flat indexes; parameters `M` and `efConstruction` trade
memory/build-time for recall.

Original: https://arxiv.org/abs/1603.09320
