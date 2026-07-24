---
id: agentic-memory
title: Agentic Memory
type: concept
status: draft
confidence: 0.55
sources: [llm-wiki-setup-guide-2026, mcp-anthropic-2024]
created: 2026-07-24
updated: 2026-07-24
category: agents
tags: [agentic-memory, agents, memory, state]
---

# Agentic Memory

> The mechanisms by which an autonomous LLM agent **remembers across time** — past
> observations, decisions, and learned facts that outlive a single context window.
> The agent-facing branch of [[knowledge-management-for-llms]].

## Types of memory
- **Short-term / working** — the current context window; volatile.
- **Episodic** — a log of what happened, retrievable later (often via
  [[semantic-search]] over stored [[embeddings]]).
- **Semantic** — distilled facts and concepts, ideally a curated store like a
  [[knowledge-graph]] or [[llm-wiki-pattern|wiki]].
- **Procedural** — learned skills and routines.

## The read/write loop
Unlike read-only [[retrieval-augmented-generation]], an agent both **reads** memory
into context ([[context-engineering]]) and **writes** new memory back — which is
exactly the LLM-maintained-wiki operation Karpathy describes, and what the
[[asdlc-knowledge-base]] formalises with lint gates so writes stay trustworthy.

## Open problems
Deciding what is worth remembering, forgetting stale or wrong memories, and
avoiding compounding [[hallucination]] when the agent reads back its own unverified
writes. [[self-rag-asai-2023|Self-reflection]] and provenance discipline are
partial answers. [[model-context-protocol|MCP]] gives agents a uniform way to
reach an external memory store.
