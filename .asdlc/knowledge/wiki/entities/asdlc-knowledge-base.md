---
id: asdlc-knowledge-base
title: "ASDLC Knowledge Base"
type: entity
status: verified
confidence: 0.9
sources: [asdlc-knowledge-readme]
created: 2026-07-23
updated: 2026-07-23
last_verified: 2026-07-23
entity_type: system
aliases: [asdlc-kb, this-repo]
tags: [meta, knowledge-management, tooling]
---

# ASDLC Knowledge Base

> This repository: a persistent, file-based knowledge base for AI-assisted
> software delivery that implements the [[llm-wiki-pattern]]. Described in full by
> its [[asdlc-knowledge-readme]].

A concrete implementation of [[andrej-karpathy]]'s LLM-wiki idea, positioned as an
alternative to [[retrieval-augmented-generation]]: knowledge is compiled once into
an interlinked markdown wiki and kept current by an agent, rather than re-retrieved
per query.

## Design
- **Single source of truth** — `manifest.yaml` defines page types, fields, the
  confidence policy, and ingestion/viz config; schema and templates are generated
  from it so they can't drift.
- **Single agent entry point** — a vendor-neutral `AGENTS.md` contract.
- **No infrastructure** — plain markdown files; the toolchain is stdlib + PyYAML.
- **Interaction interface** — the `kb` CLI, with operations scaffold, ingest,
  index, lint, verify, viz, and purge.

## Trustworthiness
Every page carries a confidence score, an editorial status, and a `last_verified`
date. `kb lint` enforces the structural rules deterministically (schema, broken
links, orphans, unsourced claims, staleness); `kb verify` assembles a page with
its cited sources for claim-level fact-checking. This page's own facts trace to
[[asdlc-knowledge-readme]].
