---
id: hybrid-search
title: Hybrid Search
type: concept
status: draft
confidence: 0.6
sources: [dpr-karpukhin-2020]
created: 2026-07-24
updated: 2026-07-24
category: retrieval
tags: [hybrid-search, retrieval, bm25, fusion]
---

# Hybrid Search

> Retrieval that combines **lexical** (keyword/BM25) and **semantic**
> ([[embeddings]]-based) matching, taking the strengths of each. A standard
> upgrade over pure [[semantic-search]] in production
> [[retrieval-augmented-generation]].

## Why combine
[[dpr-karpukhin-2020|Dense retrieval]] excels at meaning — synonyms, paraphrase —
but stumbles on exact identifiers, product codes, rare names, and out-of-domain
terms, where sparse BM25 is strong. Running both and fusing the results covers the
blind spots of either alone.

## Fusion methods
- **Reciprocal Rank Fusion (RRF)** — merge two ranked lists by summing reciprocal
  ranks; robust and score-scale-free.
- **Weighted score combination** — normalise and blend the two similarity scores.
- Then optionally [[reranking|rerank]] the fused shortlist with a cross-encoder.

Most modern [[vector-database|vector databases]] expose hybrid search natively via
metadata + vector queries, part of the broader
[[knowledge-management-for-llms|retrieval toolkit]].
