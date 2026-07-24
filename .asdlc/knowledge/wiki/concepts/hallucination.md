---
id: hallucination
title: Hallucination
type: concept
status: draft
confidence: 0.6
sources: [self-rag-asai-2023, llm-wiki-setup-guide-2026]
created: 2026-07-24
updated: 2026-07-24
category: reliability
tags: [hallucination, reliability, grounding, faithfulness]
---

# Hallucination

> When a language model generates fluent, confident output that is **not grounded
> in fact or in its provided evidence**. The central reliability problem that
> [[knowledge-management-for-llms]] exists to mitigate.

## Two flavours
- **Factuality** — the claim contradicts the real world.
- **Faithfulness** — the claim contradicts, or is unsupported by, the retrieved
  context, even if plausible. [[retrieval-augmented-generation]] targets this one.

## Why grounding helps (and doesn't fully solve it)
Supplying retrieved evidence reduces hallucination, but a model can still ignore or
misread it, or the retrieval itself can be wrong. Mitigations:
- **Grounded generation** — [[retrieval-augmented-generation]] with citations.
- **Self-checking** — [[self-rag-asai-2023|Self-RAG]] emits tokens judging whether
  each statement is supported by its source.
- **Better retrieval** — [[reranking]], [[hybrid-search]], and [[graph-rag]] raise
  the odds the right evidence is present.
- **Provenance discipline** — every claim tied to a dated source, exactly the
  confidence-and-verification policy the [[asdlc-knowledge-base]] enforces so that
  [[agentic-memory]] writes don't compound errors.

## Measuring it
Faithfulness/groundedness metrics and citation-precision scores (as in
[[self-rag-asai-2023]]) quantify how well output stays tied to evidence.
