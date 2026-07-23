---
id: asdlc-knowledge-readme
title: "ASDLC Knowledge Base — README"
type: source
status: verified
confidence: 0.9
sources: [asdlc-knowledge-readme]
created: 2026-07-23
updated: 2026-07-23
last_verified: 2026-07-23
origin: raw/asdlc-knowledge-readme.md
media_type: text
ingested_with: plaintext
checksum: 967bcd91657735691201eb4779bf016df3bce0c80698473647f49e0882ed808d
tags: [meta, documentation, repo]
---

# ASDLC Knowledge Base — README

> The project README for [[asdlc-knowledge-base]]: a persistent, file-based
> knowledge base for AI-assisted software delivery that implements the
> [[llm-wiki-pattern]] — knowledge compiled once into an interlinked markdown
> wiki and kept current by an agent, rather than re-derived per query as in
> [[retrieval-augmented-generation]].

The canonical description of this repository. It states the thesis (bookkeeping,
not thinking, is the bottleneck a knowledge base faces — quoting
[[andrej-karpathy]]), the no-infrastructure constraint (plain files: no database,
no server), and the layout: `manifest.yaml` as the single source of truth,
`AGENTS.md` as the single agent entry point, and the `kb` CLI as the interaction
interface.

It documents the seven `kb` operations — **scaffold, ingest, index, lint, verify,
viz, purge** — and the confidence/fact-check policy: every page carries a
`confidence`, a `status`, and a `last_verified`, enforced deterministically by
`lint` and judged at the claim level by `verify`.

As a source this is authoritative for *what the system is and how it is used*; it
is not a source for the wider claims about the underlying pattern (those cite
[[karpathy-llm-wiki]]).

Original: README.md (repository root)
