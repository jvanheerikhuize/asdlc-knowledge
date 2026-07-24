---
id: vector-database
title: Vector Database
type: concept
status: draft
confidence: 0.6
sources: [faiss-johnson-2017, hnsw-malkov-2016]
created: 2026-07-24
updated: 2026-07-24
category: infrastructure
tags: [vector-database, ann, infrastructure, retrieval]
---

# Vector Database

> A datastore specialised for indexing and querying [[embeddings]] by similarity
> rather than exact match. It is the retrieval engine of most
> [[retrieval-augmented-generation]] systems and the home of
> [[approximate-nearest-neighbor]] indexes.

## What it provides
- **ANN indexing** — [[hnsw-malkov-2016|HNSW]] graphs, or IVF + product
  quantization from [[faiss-johnson-2017|FAISS]], to search millions–billions of
  vectors in milliseconds.
- **Metadata filtering** — combine vector similarity with structured predicates
  (date, tag, source), enabling [[hybrid-search]].
- **CRUD + persistence** — insert, update, and delete vectors without full
  reindexing, plus durability and sharding.

## Landscape
Dedicated engines (Qdrant, Milvus, Weaviate, Pinecone) and extensions to existing
databases (pgvector for Postgres, vector search in Elasticsearch/OpenSearch). Most
build on [[faiss]] or an HNSW implementation under the hood.

## When you don't need one
For small or highly structured corpora, a [[knowledge-graph]] or a curated
[[llm-wiki-pattern|wiki]] with explicit links can outperform vector retrieval —
a recurring theme in [[knowledge-management-for-llms]].
