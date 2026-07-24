---
id: self-rag-asai-2023
title: "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection"
type: source
status: verified
confidence: 0.75
sources: [self-rag-asai-2023]
created: 2026-07-24
updated: 2026-07-24
last_verified: 2026-07-24
origin: https://arxiv.org/abs/2310.11511
media_type: pdf
author: "Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, Hannaneh Hajishirzi"
published: 2023-10-17
url: https://arxiv.org/abs/2310.11511
tags: [rag, self-reflection, hallucination, question-answering]
---

# Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

> **Self-RAG** ([[akari-asai]] et al., 2023) makes an LLM decide *when* to
> retrieve and *judge its own output* against the retrieved evidence, using
> special "reflection tokens." A concrete answer to
> [[retrieval-augmented-generation]]'s weakness of retrieving indiscriminately and
> still [[hallucination|hallucinating]].

## Idea
Standard RAG always retrieves a fixed number of passages and always uses them —
wasteful when unneeded, and it can be led astray by irrelevant hits. Self-RAG
trains a single model to emit **reflection tokens** that:
- decide **whether** retrieval is needed for the current span;
- assess whether each retrieved passage is **relevant**;
- check whether the generated statement is **supported** by that passage
  (an explicit grounding / faithfulness signal).

## Result
Self-RAG outperformed standard RAG and much larger models on open-domain QA,
reasoning, and fact-verification, with **better citation precision** and factual
grounding — reducing [[hallucination]]. It is a landmark in the "adaptive /
agentic RAG" line that also includes [[graph-rag|GraphRAG]].

Original: https://arxiv.org/abs/2310.11511
