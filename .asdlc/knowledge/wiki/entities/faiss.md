---
id: faiss
title: FAISS
type: entity
entity_type: system
status: draft
confidence: 0.6
sources: [faiss-johnson-2017, hnsw-malkov-2016]
created: 2026-07-24
updated: 2026-07-24
aliases: [facebook-ai-similarity-search]
tags: [library, ann, vector-search]
---

# FAISS

> **F**acebook **AI** **Si**milarity **S**earch — the open-source library from
> [[meta-ai]] for efficient similarity search over dense [[embeddings]]. The
> reference [[approximate-nearest-neighbor]] engine underneath many vector systems.

## What it is
Introduced in [[faiss-johnson-2017]], FAISS provides GPU/CPU implementations of
exact and approximate search: IVF, product quantization for compressed
billion-scale indexes, and an [[hnsw-malkov-2016|HNSW]] index. Many a
[[vector-database]] (Milvus, Qdrant, and research systems) builds on or benchmarks
against it, making it foundational infrastructure for [[semantic-search]] within
[[knowledge-management-for-llms]].
