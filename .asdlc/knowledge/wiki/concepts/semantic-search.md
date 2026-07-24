---
id: semantic-search
title: Semantic Search
type: concept
status: draft
confidence: 0.65
sources: [dpr-karpukhin-2020, sentence-bert-2019]
created: 2026-07-24
updated: 2026-07-24
category: retrieval
tags: [semantic-search, retrieval, embeddings]
---

# Semantic Search

> Search that matches on **meaning** rather than exact keywords, by comparing
> [[embeddings]] of the query and candidate documents. It is the retrieval step
> that feeds [[retrieval-augmented-generation]].

## How it works
1. Embed every document (usually after [[chunking]]) and store the vectors in a
   [[vector-database]].
2. At query time, embed the query and find its
   [[approximate-nearest-neighbor|nearest neighbours]].
3. Optionally [[reranking|rerank]] the top candidates with a more expensive
   cross-encoder for precision.

## Semantic vs lexical
[[dpr-karpukhin-2020|Dense retrieval]] finds paraphrases and synonyms that keyword
(BM25) search misses, but lexical search still wins on exact terms, names, and
rare tokens. Combining both is [[hybrid-search]].

## Limits
Quality is bounded by the embedding model and by [[chunking]]; a semantically
"relevant" passage is not necessarily a *correct* or *sufficient* one, which is
why grounding and [[self-rag-asai-2023|self-checking]] matter for
[[hallucination]] control.
