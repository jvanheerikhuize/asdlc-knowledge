---
title: Knowledge Graph
---

# Knowledge Graph

Every page in the wiki and how it links to the others. Read it as:

- **Shape = layer** — `(concept)` rounded, `([entity])` stadium, `[/source/]` document. Pages are grouped into their layer.
- **Colour = confidence** — green `high` (≥0.75), orange `medium` (≥0.45), red `low`. The `0.0 · band` under each title is the score.
- **Line = relationship** — solid `↔` is a concept/entity cross-link; dotted `⋯▸` is a **citation** to a source. Double-headed means both pages link back to each other.

Regenerate after any content change with `python tools/kb.py viz`.

```mermaid
graph LR
  subgraph concept_layer["Concepts"]
    direction LR
    llm_wiki_pattern("LLM Wiki Pattern<br/><small>0.8 · high</small>")
    retrieval_augmented_generation("Retrieval-Augmented Generation (RAG)<br/><small>0.8 · high</small>")
  end
  subgraph entity_layer["Entities"]
    direction LR
    andrej_karpathy(["Andrej Karpathy<br/><small>0.85 · high</small>"])
    asdlc_knowledge_base(["ASDLC Knowledge Base<br/><small>0.9 · high</small>"])
    patrick_lewis(["Patrick Lewis<br/><small>0.7 · medium</small>"])
  end
  subgraph source_layer["Sources"]
    direction LR
    asdlc_knowledge_readme[/"ASDLC Knowledge Base — README<br/><small>0.9 · high</small>"/]
    karpathy_llm_wiki[/"Karpathy — LLM Wiki gist<br/><small>0.9 · high</small>"/]
    llm_wiki_setup_guide_2026[/"LLM Wiki Setup: Karpathy's Knowledge Base (2026 Guide)<br/><small>0.5 · medium</small>"/]
    rag_lewis_2020[/"Lewis et al. — Retrieval-Augmented Generation (2020)<br/><small>0.85 · high</small>"/]
  end
  asdlc_knowledge_base --> andrej_karpathy
  asdlc_knowledge_readme -.-> andrej_karpathy
  andrej_karpathy <-.-> karpathy_llm_wiki
  andrej_karpathy <--> llm_wiki_pattern
  andrej_karpathy <-.-> llm_wiki_setup_guide_2026
  asdlc_knowledge_base <-.-> asdlc_knowledge_readme
  asdlc_knowledge_base <--> llm_wiki_pattern
  asdlc_knowledge_base --> retrieval_augmented_generation
  asdlc_knowledge_readme -.-> karpathy_llm_wiki
  asdlc_knowledge_readme -.-> llm_wiki_pattern
  asdlc_knowledge_readme -.-> retrieval_augmented_generation
  karpathy_llm_wiki <-.-> llm_wiki_pattern
  llm_wiki_pattern <-.-> llm_wiki_setup_guide_2026
  rag_lewis_2020 -.-> llm_wiki_pattern
  llm_wiki_pattern <--> retrieval_augmented_generation
  llm_wiki_setup_guide_2026 <-.-> retrieval_augmented_generation
  patrick_lewis <-.-> rag_lewis_2020
  patrick_lewis --> retrieval_augmented_generation
  rag_lewis_2020 <-.-> retrieval_augmented_generation
  style llm_wiki_pattern fill:#2f9e4418,stroke:#2f9e44,stroke-width:1px
  style retrieval_augmented_generation fill:#2f9e4418,stroke:#2f9e44,stroke-width:1px
  style andrej_karpathy fill:#2f9e4418,stroke:#2f9e44,stroke-width:1px
  style asdlc_knowledge_base fill:#2f9e4418,stroke:#2f9e44,stroke-width:1px
  style patrick_lewis fill:#f08c0018,stroke:#f08c00,stroke-width:1px
  style asdlc_knowledge_readme fill:#2f9e4418,stroke:#2f9e44,stroke-width:1px
  style karpathy_llm_wiki fill:#2f9e4418,stroke:#2f9e44,stroke-width:1px
  style llm_wiki_setup_guide_2026 fill:#f08c0018,stroke:#f08c00,stroke-width:1px
  style rag_lewis_2020 fill:#2f9e4418,stroke:#2f9e44,stroke-width:1px
  subgraph legend["Legend"]
    direction LR
    lg_c("Concept")
    lg_e(["Entity"])
    lg_s[/"Source"/]
    lg_c -.->|cites| lg_s
    lg_c <--> lg_e
  end
  style legend fill:none,stroke:#adb5bd,stroke-dasharray:3 3
  style lg_c fill:#f1f3f5,stroke:#adb5bd
  style lg_e fill:#f1f3f5,stroke:#adb5bd
  style lg_s fill:#f1f3f5,stroke:#adb5bd
```
