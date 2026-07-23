# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

Source: Lewis et al., NeurIPS 2020. arXiv:2005.11401
URL: https://arxiv.org/abs/2005.11401

Authors: Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir
Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim
Rocktäschel, Sebastian Riedel, Douwe Kiela.

## Abstract (verbatim)

Large pre-trained language models have been shown to store factual knowledge in
their parameters, and achieve state-of-the-art results when fine-tuned on
downstream NLP tasks. However, their ability to access and precisely manipulate
knowledge is still limited, and hence on knowledge-intensive tasks, their
performance lags behind task-specific architectures. Additionally, providing
provenance for their decisions and updating their world knowledge remain open
research problems. Pre-trained models with a differentiable access mechanism to
explicit non-parametric memory can overcome this issue, but have so far been
only investigated for extractive downstream tasks. We explore a general-purpose
fine-tuning recipe for retrieval-augmented generation (RAG) — models which
combine pre-trained parametric and non-parametric memory for language
generation. We introduce RAG models where the parametric memory is a pre-trained
seq2seq model and the non-parametric memory is a dense vector index of
Wikipedia, accessed with a pre-trained neural retriever. We compare two RAG
formulations, one which conditions on the same retrieved passages across the
whole generated sequence, the other can use different passages per token. We
fine-tune and evaluate our models on a wide range of knowledge-intensive NLP
tasks and set the state-of-the-art on three open domain QA tasks, outperforming
parametric seq2seq models and task-specific retrieve-and-extract architectures.
For language generation tasks, we find that RAG models generate more specific,
diverse and factual language than a state-of-the-art parametric-only seq2seq
baseline.

## Key points

- **Problem.** LLMs store facts in their weights (parametric memory) but cannot
  reliably access or precisely manipulate that knowledge; provenance and
  knowledge updates are open problems.
- **Architecture.** RAG couples a parametric memory (a pre-trained seq2seq
  generator) with a non-parametric memory (a dense vector index of Wikipedia)
  reached through a pre-trained neural retriever (Dense Passage Retrieval).
- **Two formulations.** RAG-Sequence conditions on the same retrieved passages
  for the whole output; RAG-Token may use a different passage per generated
  token.
- **Results.** Sets state-of-the-art on three open-domain QA tasks, beating both
  parametric-only seq2seq models and task-specific retrieve-and-extract systems;
  generates more specific, diverse, and factual text than a parametric-only
  baseline.
- **Relevance here.** RAG re-retrieves knowledge per query at inference time.
  This is the approach the persistent LLM-wiki pattern positions itself against:
  compile knowledge once into a maintained wiki instead of re-deriving it on
  every query.
