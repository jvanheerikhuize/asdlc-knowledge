---
id: sentence-bert-2019
title: "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"
type: source
status: verified
confidence: 0.75
sources: [sentence-bert-2019]
created: 2026-07-24
updated: 2026-07-24
last_verified: 2026-07-24
origin: https://arxiv.org/abs/1908.10084
media_type: pdf
author: "Nils Reimers, Iryna Gurevych"
published: 2019-08-27
url: https://arxiv.org/abs/1908.10084
tags: [embeddings, semantic-search, nlp, sbert]
---

# Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks

> The paper introducing **Sentence-BERT (SBERT)** ([[nils-reimers]] & Iryna
> Gurevych, EMNLP 2019). It made high-quality sentence [[embeddings]] cheap
> enough for practical [[semantic-search]], and seeded the widely used
> `sentence-transformers` library.

## Problem
Vanilla BERT produces token embeddings but no good fixed-size *sentence* vector;
comparing two sentences meant feeding both through the model together
(cross-encoding). Finding the most similar pair among 10,000 sentences that way
needs ~50M forward passes — hours of compute — making it unusable for retrieval.

## Method
SBERT fine-tunes BERT in a **Siamese** (twin-tower) network so each sentence maps
independently to a dense vector. Similarity becomes a cheap cosine distance,
reducing that same search from hours to seconds while keeping most of the
accuracy.

## Impact
- Made **bi-encoder** [[embeddings]] the default for [[semantic-search]] and
  first-stage retrieval, with a cross-encoder [[reranking]] pass on top.
- The `sentence-transformers` library became a standard tool for producing
  vectors to store in a [[vector-database]].

Original: https://arxiv.org/abs/1908.10084
