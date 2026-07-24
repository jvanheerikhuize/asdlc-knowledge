---
id: context-engineering
title: Context Engineering
type: concept
status: draft
confidence: 0.55
sources: [llm-wiki-setup-guide-2026, mcp-anthropic-2024]
created: 2026-07-24
updated: 2026-07-24
category: knowledge-management
tags: [context-engineering, prompting, retrieval]
---

# Context Engineering

> The discipline of deciding **what information occupies a model's finite context
> window** at each step — which retrieved passages, memories, tools, and
> instructions to include, in what order, at what fidelity. The connective tissue
> between a knowledge store and the model in [[knowledge-management-for-llms]].

## Why it is more than prompting
Prompting is wording; context engineering is *selection and budgeting*. The window
is a scarce resource, and more context is not better — irrelevant or contradictory
material degrades output and invites [[hallucination]]. The job is to assemble the
minimal sufficient context.

## Core moves
- **Retrieve and rank** — pull candidates via [[semantic-search]] / [[hybrid-search]],
  trim with [[reranking]].
- **Compress** — summarise or [[chunking|chunk]] so the essential survives.
- **Structure** — order by relevance, mark provenance so the model can cite.
- **Route tools & memory** — surface the right [[model-context-protocol|MCP]]
  resources and [[agentic-memory|memories]] for the task.

## Link to curated knowledge
A well-organised [[llm-wiki-pattern|wiki]] makes context engineering easier: pages
are pre-summarised, pre-linked units, so assembling good context is closer to
graph traversal than to re-chunking raw documents.
