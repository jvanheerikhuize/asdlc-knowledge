---
id: graphrag-edge-2024
title: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization"
type: source
status: verified
confidence: 0.75
sources: [graphrag-edge-2024]
created: 2026-07-24
updated: 2026-07-24
last_verified: 2026-07-24
origin: https://arxiv.org/abs/2404.16130
media_type: pdf
author: "Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Mody, Steven Truitt, Dasha Metropolitansky, Robert Osazuwa Ness, Jonathan Larson"
published: 2024-04-24
url: https://arxiv.org/abs/2404.16130
tags: [rag, knowledge-graph, summarization, microsoft]
---

# From Local to Global: A Graph RAG Approach to Query-Focused Summarization

> The Microsoft Research paper that introduced [[graph-rag|GraphRAG]] ([[darren-edge]]
> et al., [[microsoft-research]], April 2024). It builds an LLM-derived
> [[knowledge-graph]] over a corpus, pre-computes community summaries with graph
> clustering, and answers *global* "sensemaking" questions that plain
> [[retrieval-augmented-generation]] handles poorly.

## The problem it targets
Baseline RAG retrieves the top-k text chunks most similar to a query. That works
for *local* questions ("what did X say about Y?") but fails on *global* ones
("what are the main themes across the whole corpus?") — no single chunk contains
the answer, and naive retrieval cannot aggregate over an entire dataset.

## Method
1. Use an LLM to extract entities and relationships from source text, forming a
   [[knowledge-graph]].
2. Detect **communities** of closely related entities (Leiden hierarchical
   clustering).
3. Pre-generate a summary for each community, bottom-up.
4. At query time, answer from community summaries in a map-reduce pass, combining
   partial answers into a global response.

## Reported result
On global sensemaking questions over ~1M-token corpora, Graph RAG produced
substantially more **comprehensive** and **diverse** answers than a vector-RAG
baseline, at lower token cost than naively summarizing the source. The method was
released as the open-source GraphRAG library.

Original: https://arxiv.org/abs/2404.16130
