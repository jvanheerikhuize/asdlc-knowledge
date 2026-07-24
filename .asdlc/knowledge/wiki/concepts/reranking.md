---
id: reranking
title: Reranking
type: concept
status: draft
confidence: 0.6
sources: [sentence-bert-2019]
created: 2026-07-24
updated: 2026-07-24
category: retrieval
tags: [reranking, retrieval, cross-encoder]
---

# Reranking

> A second retrieval stage that re-scores a shortlist of candidates with a more
> accurate (and more expensive) model, ordering them by true relevance before they
> reach the LLM. The precision half of the standard two-stage
> [[retrieval-augmented-generation]] pipeline.

## Why two stages
A fast **bi-encoder** ([[sentence-bert-2019|Sentence-BERT]] style) embeds queries
and documents independently, enabling [[approximate-nearest-neighbor]] search over
millions of items — high recall, coarse ranking. A **cross-encoder** then reads
each query–document *pair jointly*, scoring relevance far more precisely but far
too slowly to run over the whole corpus. So: retrieve ~100 with the bi-encoder,
rerank to the top ~5 with the cross-encoder.

## Payoff
Reranking often improves answer quality more cheaply than swapping the base
embedding model, and it curbs [[hallucination]] by keeping genuinely irrelevant
passages out of the prompt — a [[context-engineering]] concern. Commonly paired
with [[hybrid-search]] as the fusion-and-refine step.
