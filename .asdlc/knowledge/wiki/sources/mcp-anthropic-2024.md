---
id: mcp-anthropic-2024
title: "Introducing the Model Context Protocol"
type: source
status: verified
confidence: 0.75
sources: [mcp-anthropic-2024]
created: 2026-07-24
updated: 2026-07-24
last_verified: 2026-07-24
origin: https://www.anthropic.com/news/model-context-protocol
media_type: html
author: "Anthropic"
published: 2024-11-25
url: https://www.anthropic.com/news/model-context-protocol
tags: [mcp, protocol, tools, interoperability, anthropic]
---

# Introducing the Model Context Protocol

> Anthropic's announcement (25 Nov 2024) open-sourcing the **Model Context
> Protocol** ([[model-context-protocol]]) — an open standard that connects LLM
> applications to external tools and data sources through a single, uniform
> interface. Published by [[anthropic]].

## What it standardizes
MCP replaces bespoke, per-integration connectors with one protocol. A **host**
(an LLM app such as an IDE or chat client) speaks to **servers** that expose:
- **Resources** — readable context (files, database rows, wiki pages).
- **Tools** — callable functions the model can invoke.
- **Prompts** — reusable templates.

The transport is JSON-RPC 2.0; the initial spec revision was dated 2024-11-05.

## Why it matters
Before MCP, every application × every data source needed a custom integration —
an "M×N" problem. MCP turns it into "M+N": build one server per source, one
client per app. It is directly relevant to [[context-engineering]] and to
[[agentic-memory]] — a knowledge base like [[asdlc-knowledge-base]] could expose
its pages to any agent as an MCP resource server. Released under an open (MIT)
licence with SDKs and reference servers.

Original: https://www.anthropic.com/news/model-context-protocol
