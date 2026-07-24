---
id: embeddings
title: Embeddings
type: concept
status: draft
confidence: 0.65
sources: [sentence-bert-2019, dpr-karpukhin-2020]
created: 2026-07-24
updated: 2026-07-24
category: representation
tags: [embeddings, vectors, nlp]
---

# Embeddings

> Dense numeric vectors that place text (or images, code, audio) in a space where
> **distance encodes meaning** — semantically similar items land close together.
> Embeddings are the substrate under [[semantic-search]], the
> [[vector-database]], and modern [[retrieval-augmented-generation]].

## How they work
A neural encoder maps an input to a fixed-length vector (typically 384–3072
dimensions). Training pulls related pairs together and pushes unrelated ones
apart. [[sentence-bert-2019|Sentence-BERT]] made *sentence*-level embeddings cheap
via a Siamese architecture; [[dpr-karpukhin-2020|DPR]] trained question/passage
encoders that beat lexical retrieval for QA.

## Properties that matter
- **Similarity metric** — cosine similarity or dot product; the index must match
  how the model was trained.
- **Dimensionality** — higher can capture more nuance but costs memory in the
  [[vector-database]] and slows [[approximate-nearest-neighbor]] search.
- **Model choice** — general vs domain-tuned; embeddings from different models are
  not comparable and re-embedding a corpus is the main migration cost.

## In this knowledge base
Retrieval here is wiki-structural ([[llm-wiki-pattern]] wikilinks) rather than
embedding-based, but embeddings are the natural next layer for
[[semantic-search]] across [[knowledge-management-for-llms|the corpus]].
