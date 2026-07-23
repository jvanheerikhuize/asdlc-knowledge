---
title: Knowledge Graph
---

# Knowledge Graph

Every page in the wiki at a glance — no tangle of link lines. Each card reads as:

- **Shape = type** — `(concept)` rounded, `([entity])` stadium, `[/source/]` document.
- **Colour = confidence** — green `high` (≥0.75), orange `medium` (≥0.45), red `low`; the score sits under the title.
- **`N🔗` = connections** — how many other pages this one is linked to. Cards are ordered by that count, so the hubs come first.

The exact **who-links-to-whom** is in the table below the graph, so the relationships stay readable without drawing every edge.

Regenerate after any content change with `python tools/kb.py viz`.

```mermaid
graph LR
  llm_wiki_pattern("LLM Wiki Pattern<br/><small>concept · 0.8 high</small><br/><b>7🔗</b>")
  retrieval_augmented_generation("Retrieval-Augmented Generation (RAG)<br/><small>concept · 0.8 high</small><br/><b>6🔗</b>")
  andrej_karpathy(["Andrej Karpathy<br/><small>entity · 0.85 high</small><br/><b>5🔗</b>"])
  asdlc_knowledge_readme[/"ASDLC Knowledge Base — README<br/><small>source · 0.9 high</small><br/><b>5🔗</b>"/]
  asdlc_knowledge_base(["ASDLC Knowledge Base<br/><small>entity · 0.9 high</small><br/><b>4🔗</b>"])
  karpathy_llm_wiki[/"Karpathy — LLM Wiki gist<br/><small>source · 0.9 high</small><br/><b>3🔗</b>"/]
  llm_wiki_setup_guide_2026[/"LLM Wiki Setup: Karpathy's Knowledge Base (2026 Guide)<br/><small>source · 0.5 medium</small><br/><b>3🔗</b>"/]
  rag_lewis_2020[/"Lewis et al. — Retrieval-Augmented Generation (2020)<br/><small>source · 0.85 high</small><br/><b>3🔗</b>"/]
  patrick_lewis(["Patrick Lewis<br/><small>entity · 0.7 medium</small><br/><b>2🔗</b>"])
  style llm_wiki_pattern fill:#2f9e4422,stroke:#2f9e44,stroke-width:2px,color:#212529
  style retrieval_augmented_generation fill:#2f9e4422,stroke:#2f9e44,stroke-width:2px,color:#212529
  style andrej_karpathy fill:#2f9e4422,stroke:#2f9e44,stroke-width:2px,color:#212529
  style asdlc_knowledge_readme fill:#2f9e4422,stroke:#2f9e44,stroke-width:2px,color:#212529
  style asdlc_knowledge_base fill:#2f9e4422,stroke:#2f9e44,stroke-width:2px,color:#212529
  style karpathy_llm_wiki fill:#2f9e4422,stroke:#2f9e44,stroke-width:2px,color:#212529
  style llm_wiki_setup_guide_2026 fill:#f08c0022,stroke:#f08c00,stroke-width:2px,color:#212529
  style rag_lewis_2020 fill:#2f9e4422,stroke:#2f9e44,stroke-width:2px,color:#212529
  style patrick_lewis fill:#f08c0022,stroke:#f08c00,stroke-width:2px,color:#212529
```

## Connections

| Page | Type | Confidence | 🔗 | Connects to |
| --- | --- | --- | --- | --- |
| **LLM Wiki Pattern** | concept | 0.8 high | 7 | `andrej-karpathy`, `asdlc-knowledge-base`, `asdlc-knowledge-readme`, `karpathy-llm-wiki`, `llm-wiki-setup-guide-2026`, `rag-lewis-2020`, `retrieval-augmented-generation` |
| **Retrieval-Augmented Generation (RAG)** | concept | 0.8 high | 6 | `asdlc-knowledge-base`, `asdlc-knowledge-readme`, `llm-wiki-pattern`, `llm-wiki-setup-guide-2026`, `patrick-lewis`, `rag-lewis-2020` |
| **Andrej Karpathy** | entity | 0.85 high | 5 | `asdlc-knowledge-base`, `asdlc-knowledge-readme`, `karpathy-llm-wiki`, `llm-wiki-pattern`, `llm-wiki-setup-guide-2026` |
| **ASDLC Knowledge Base — README** | source | 0.9 high | 5 | `andrej-karpathy`, `asdlc-knowledge-base`, `karpathy-llm-wiki`, `llm-wiki-pattern`, `retrieval-augmented-generation` |
| **ASDLC Knowledge Base** | entity | 0.9 high | 4 | `andrej-karpathy`, `asdlc-knowledge-readme`, `llm-wiki-pattern`, `retrieval-augmented-generation` |
| **Karpathy — LLM Wiki gist** | source | 0.9 high | 3 | `andrej-karpathy`, `asdlc-knowledge-readme`, `llm-wiki-pattern` |
| **LLM Wiki Setup: Karpathy's Knowledge Base (2026 Guide)** | source | 0.5 medium | 3 | `andrej-karpathy`, `llm-wiki-pattern`, `retrieval-augmented-generation` |
| **Lewis et al. — Retrieval-Augmented Generation (2020)** | source | 0.85 high | 3 | `llm-wiki-pattern`, `patrick-lewis`, `retrieval-augmented-generation` |
| **Patrick Lewis** | entity | 0.7 medium | 2 | `rag-lewis-2020`, `retrieval-augmented-generation` |
