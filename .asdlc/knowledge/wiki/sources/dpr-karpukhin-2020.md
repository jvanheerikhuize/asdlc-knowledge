---
id: dpr-karpukhin-2020
title: "Dense Passage Retrieval for Open-Domain Question Answering"
type: source
status: verified
confidence: 0.75
sources: [dpr-karpukhin-2020]
created: 2026-07-24
updated: 2026-07-24
last_verified: 2026-07-24
origin: https://arxiv.org/abs/2004.04906
media_type: pdf
author: "Vladimir Karpukhin, Barlas Oğuz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, Wen-tau Yih"
published: 2020-04-10
url: https://arxiv.org/abs/2004.04906
tags: [retrieval, embeddings, question-answering, dpr, meta]
---

# Dense Passage Retrieval for Open-Domain Question Answering

> The **DPR** paper ([[vladimir-karpukhin]] et al., [[meta-ai]], EMNLP 2020) that
> showed learned dense [[embeddings]] beat classic sparse retrieval (BM25) for
> open-domain QA. Co-authored by [[patrick-lewis]], and a direct precursor to the
> retriever in [[retrieval-augmented-generation]].

## Idea
Train a dual-encoder: one BERT encoder for questions, one for passages, optimised
so a question vector lands near the vectors of passages that answer it
(contrastive learning with in-batch negatives). Retrieval is then a
[[approximate-nearest-neighbor|nearest-neighbour]] lookup in the shared embedding
space.

## Result
DPR improved top-20 passage retrieval accuracy by **9–19%** over BM25 on multiple
open-QA benchmarks, and lifted end-to-end answer accuracy. It established the
now-standard retriever architecture behind [[semantic-search]] and RAG pipelines.

## Relation to sparse retrieval
DPR captures **semantic** matches (synonyms, paraphrase) that lexical BM25 misses,
but BM25 still wins on exact keyword/rare-term matches — motivating the
[[hybrid-search]] combinations common today.

Original: https://arxiv.org/abs/2004.04906
