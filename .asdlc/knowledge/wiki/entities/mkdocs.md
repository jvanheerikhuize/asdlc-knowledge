---
id: mkdocs
title: MkDocs
type: entity
entity_type: product
status: draft
confidence: 0.55
sources: [asdlc-knowledge-readme]
created: 2026-07-24
updated: 2026-07-24
aliases: [mkdocs-material]
tags: [tool, static-site, documentation]
---

# MkDocs

> A static-site generator that turns Markdown into a browsable documentation site —
> the publishing layer that renders this [[llm-wiki-pattern|wiki]] as a
> GitHub Pages site.

## Relevance to this cluster
MkDocs (with the Material theme) is how the [[asdlc-knowledge-base]] becomes a real,
navigable wiki for human readers. Making that published site behave like a true
wiki — resolving wiki-links, backlinks, and the [[knowledge-graph]] view — is
the "wiki-grade distribution" goal for
[[knowledge-management-for-llms|this knowledge base]]. It renders content authored
under the wiki layer without touching the immutable `raw/` sources.
