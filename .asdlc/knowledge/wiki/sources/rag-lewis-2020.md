---
id: rag-lewis-2020
title: "Lewis et al. — Retrieval-Augmented Generation (2020)"
type: source
status: verified
confidence: 0.85
sources: [rag-lewis-2020]
created: 2026-07-23
updated: 2026-07-23
last_verified: 2026-07-23
origin: raw/rag-lewis-2020.md
media_type: text
ingested_with: plaintext
checksum: c356de74235bc52d0d9d498744a6ea65394acfc959f1c663ba256f93ddbd7490
tags: [rag, retrieval, nlp, paper]
---

# Lewis et al. — Retrieval-Augmented Generation (2020)

> The paper that named and formalised [[retrieval-augmented-generation]]: a
> general-purpose recipe coupling a pre-trained seq2seq generator (parametric
> memory) with a dense vector index of Wikipedia (non-parametric memory) reached
> through a neural retriever. NeurIPS 2020, arXiv:2005.11401.

Lead author [[patrick-lewis]] and colleagues introduce **RAG**. They motivate it
by three limitations of parametric-only language models: they cannot precisely
manipulate the knowledge stored in their weights, cannot easily provide
provenance for a decision, and cannot cheaply update their world knowledge. RAG
addresses all three by giving the generator differentiable access to an explicit,
swappable knowledge store.

The paper compares two formulations — *RAG-Sequence* (one retrieved passage set
conditions the whole output) and *RAG-Token* (a different passage may inform each
generated token). It set the state of the art on three open-domain QA tasks,
beating both parametric-only seq2seq models and task-specific retrieve-and-extract
architectures, and produced more specific, diverse, and factual generation than a
parametric-only baseline.

> "models which combine pre-trained parametric and non-parametric memory for
> language generation."

RAG re-retrieves knowledge on **every query** at inference time. That is exactly
the cost the [[llm-wiki-pattern]] positions itself against: compile knowledge once
into a maintained, interlinked wiki instead of re-deriving it per query.

Original: https://arxiv.org/abs/2005.11401
