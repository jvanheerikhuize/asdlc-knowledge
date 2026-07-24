---
id: model-context-protocol
title: Model Context Protocol (MCP)
type: concept
status: draft
confidence: 0.65
sources: [mcp-anthropic-2024]
created: 2026-07-24
updated: 2026-07-24
category: agents
tags: [mcp, protocol, tools, interoperability]
---

# Model Context Protocol (MCP)

> An open standard ([[anthropic]], Nov 2024 — see [[mcp-anthropic-2024]]) that
> gives LLM applications **one uniform interface** to external tools and data. The
> plumbing that lets [[agentic-memory]] and knowledge stores plug into any model.

## The shape
A **host** app connects to **servers** over JSON-RPC. Each server exposes:
- **Resources** — readable context (files, records, [[llm-wiki-pattern|wiki]]
  pages).
- **Tools** — functions the model may call.
- **Prompts** — reusable templates.

## Why it matters for knowledge management
Without a standard, connecting *M* apps to *N* data sources is an M×N tangle of
bespoke integrations. MCP makes it M+N: one server per source, reused by every
client. So a store like the [[asdlc-knowledge-base]] could expose its curated
pages as MCP resources, and any agent could read them through
[[context-engineering]] — without a custom connector.

## Relation to RAG
MCP is transport and interface, not retrieval strategy; a
[[retrieval-augmented-generation]] pipeline or [[vector-database]] can sit *behind*
an MCP server. It standardises *access*, leaving *what to retrieve* to the tools
this cluster describes. A cornerstone of the agent side of
[[knowledge-management-for-llms]].
