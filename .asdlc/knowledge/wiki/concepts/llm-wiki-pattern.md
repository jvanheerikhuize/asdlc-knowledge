---
id: llm-wiki-pattern
title: "LLM Wiki Pattern"
type: concept
status: verified
confidence: 0.8
sources: [karpathy-llm-wiki]
created: 2026-07-23
updated: 2026-07-23
last_verified: 2026-07-23
category: knowledge-management
tags: [pattern, rag-alternative]
---

# LLM Wiki Pattern

> Compile knowledge once into a persistent, interlinked markdown wiki and keep
> it current — instead of re-deriving it on every query as
> [[retrieval-augmented-generation]] does.
> Introduced in [[karpathy-llm-wiki]] by [[andrej-karpathy]].

## Layers
- **Raw** — immutable source documents. Never edited by the agent.
- **Wiki** — LLM-maintained markdown: source, entity, and concept pages.
- **Schema** — the config (here `manifest.yaml` + `AGENTS.md`) encoding conventions.

## Operations
- **Ingest** — read a new source, write a summary page, update ~10–15 pages, log it.
- **Query** — search pages, answer with citations, file durable analyses back.
- **Lint** — health-check for contradictions, staleness, orphans, gaps.

## Why it works
The bottleneck in knowledge bases is *bookkeeping*, not thinking — precisely the
maintenance work an agent can do tirelessly. This KB extends the pattern with an
explicit confidence/fact-check policy and a binary ingestion layer so the wiki
stays both broad and trustworthy.
