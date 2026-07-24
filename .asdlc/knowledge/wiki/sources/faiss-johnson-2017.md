---
id: faiss-johnson-2017
title: "Billion-scale Similarity Search with GPUs"
type: source
status: verified
confidence: 0.75
sources: [faiss-johnson-2017]
created: 2026-07-24
updated: 2026-07-24
last_verified: 2026-07-24
origin: https://arxiv.org/abs/1702.08734
media_type: pdf
author: "Jeff Johnson, Matthijs Douze, Hervé Jégou"
published: 2017-02-28
url: https://arxiv.org/abs/1702.08734
tags: [faiss, ann, gpu, vector-search, meta]
---

# Billion-scale Similarity Search with GPUs

> The paper behind **FAISS** (Johnson, Douze & Jégou, [[meta-ai]], 2017) — the
> library that made [[approximate-nearest-neighbor]] search over *billions* of
> [[embeddings]] practical on GPUs. FAISS is the reference engine underneath many
> a [[vector-database]].

## Contribution
A GPU-optimised design for k-nearest-neighbour and k-means at scale: a fast exact
brute-force mode, an efficient GPU implementation of **IVF** (inverted-file)
and **product quantization** for compressed indexes, and multi-GPU sharding. It
reported building a billion-vector index and answering queries in milliseconds —
orders of magnitude faster than prior GPU baselines.

## Why it matters
- **[[faiss|FAISS]]** became the de-facto open-source ANN toolkit; Qdrant, Milvus,
  and countless research systems build on or benchmark against it.
- Product quantization keeps huge indexes in memory by storing compressed vector
  codes — the standard technique for scaling [[semantic-search]] cheaply.
- Complements graph indexes like [[hnsw-malkov-2016|HNSW]]: IVF+PQ trades a little
  recall for much lower memory; HNSW trades memory for top recall.

Original: https://arxiv.org/abs/1702.08734
