---
id: retrieval-augmented-generation
title: "Retrieval-Augmented Generation (RAG)"
type: concept
status: verified
confidence: 0.8
sources: [rag-lewis-2020, llm-wiki-setup-guide-2026]
created: 2026-07-23
updated: 2026-07-23
last_verified: 2026-07-23
category: knowledge-management
tags: [rag, retrieval, pattern]
---

# Retrieval-Augmented Generation (RAG)

> Give a language model differentiable access to an external, swappable knowledge
> store and retrieve relevant passages **at query time**, conditioning generation
> on them. Named and formalised in [[rag-lewis-2020]].

## How it works
- **Parametric memory** — a pre-trained seq2seq generator holds knowledge in its
  weights.
- **Non-parametric memory** — an external index (in the original paper, a dense
  vector index of Wikipedia) reached through a neural retriever.
- On each query, the retriever pulls the top passages and the generator conditions
  on them — either once for the whole output (*RAG-Sequence*) or per token
  (*RAG-Token*).

## Why it matters
RAG lets a model cite provenance and update its world knowledge by swapping the
index, without retraining — the three limitations of parametric-only models that
[[rag-lewis-2020]] set out to fix.

## Contrast with the LLM wiki pattern
RAG and the [[llm-wiki-pattern]] answer the same question — *how does a model use
knowledge it wasn't trained on?* — with opposite trade-offs:

- **RAG** re-derives the relevant knowledge **per query**. Always current with the
  underlying index, but pays retrieval + reasoning cost every time and leaves no
  durable, human-readable artifact.
- **LLM wiki** compiles knowledge **once** into a maintained, interlinked wiki.
  Cheap to read and auditable, but requires ongoing bookkeeping to stay current.

They are complementary: a wiki can be the curated, high-confidence layer over a
larger corpus that RAG still searches on demand. A practitioner report
([[llm-wiki-setup-guide-2026]]) puts the rule of thumb bluntly: reach for RAG to
search 100k support tickets, and for the [[llm-wiki-pattern]] to synthesise 50
research papers into one coherent understanding.
