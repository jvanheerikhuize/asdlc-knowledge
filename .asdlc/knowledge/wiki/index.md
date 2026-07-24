---
title: Knowledge Graph
---

# Knowledge Graph

Nodes colored by confidence band, and every node is a link. Use the **2D / 3D** toggle to switch between the Mermaid diagram and an interactive force-directed graph. In **2D**, click a node to open its page. In **3D**, drag to rotate and scroll to zoom; click a node to focus the camera, or ⌘/Ctrl/Shift-click to open its page. Regenerate with `python tools/kb.py viz`.

<div class="kb-graph">
<style>
.kb-view-toggle{display:flex;gap:.4rem;margin:.2rem 0 .8rem}
.kb-view-toggle button{font:inherit;cursor:pointer;padding:.35rem .8rem;border-radius:.4rem;border:1px solid var(--md-default-fg-color--lighter,#8888);background:transparent;color:inherit}
.kb-view-toggle button.kb-active{background:var(--md-accent-fg-color,#3b82f6);color:#fff;border-color:transparent}
#kb-graph-3d{width:100%;height:560px;border:1px solid var(--md-default-fg-color--lightest,#8883);border-radius:.5rem;overflow:hidden}
#kb-graph-3d .kb-msg{padding:1rem;opacity:.8}
</style>
<div class="kb-view-toggle" role="tablist">
<button id="kb-btn-2d" class="kb-active" type="button" onclick="kbShowView('2d')">2D · Mermaid</button>
<button id="kb-btn-3d" type="button" onclick="kbShowView('3d')">3D · Force graph</button>
</div>
<div id="kb-graph-3d" style="display:none"></div>
<script id="kb-graph-data" type="application/json">{"nodes":[{"id":"agentic-memory","name":"Agentic Memory","type":"concept","conf":0.55,"band":"medium","color":"#f08c00","val":13,"href":"concepts/agentic-memory/"},{"id":"approximate-nearest-neighbor","name":"Approximate Nearest Neighbor Search","type":"concept","conf":0.65,"band":"medium","color":"#f08c00","val":12,"href":"concepts/approximate-nearest-neighbor/"},{"id":"chunking","name":"Chunking","type":"concept","conf":0.55,"band":"medium","color":"#f08c00","val":10,"href":"concepts/chunking/"},{"id":"context-engineering","name":"Context Engineering","type":"concept","conf":0.55,"band":"medium","color":"#f08c00","val":13,"href":"concepts/context-engineering/"},{"id":"embeddings","name":"Embeddings","type":"concept","conf":0.65,"band":"medium","color":"#f08c00","val":20,"href":"concepts/embeddings/"},{"id":"graph-rag","name":"GraphRAG","type":"concept","conf":0.6,"band":"medium","color":"#f08c00","val":10,"href":"concepts/graph-rag/"},{"id":"hallucination","name":"Hallucination","type":"concept","conf":0.6,"band":"medium","color":"#f08c00","val":11,"href":"concepts/hallucination/"},{"id":"hybrid-search","name":"Hybrid Search","type":"concept","conf":0.6,"band":"medium","color":"#f08c00","val":9,"href":"concepts/hybrid-search/"},{"id":"knowledge-graph","name":"Knowledge Graph","type":"concept","conf":0.6,"band":"medium","color":"#f08c00","val":14,"href":"concepts/knowledge-graph/"},{"id":"knowledge-management-for-llms","name":"Knowledge Management for LLMs","type":"concept","conf":0.6,"band":"medium","color":"#f08c00","val":26,"href":"concepts/knowledge-management-for-llms/"},{"id":"llm-wiki-pattern","name":"LLM Wiki Pattern","type":"concept","conf":0.8,"band":"high","color":"#2f9e44","val":20,"href":"concepts/llm-wiki-pattern/"},{"id":"model-context-protocol","name":"Model Context Protocol (MCP)","type":"concept","conf":0.65,"band":"medium","color":"#f08c00","val":9,"href":"concepts/model-context-protocol/"},{"id":"reranking","name":"Reranking","type":"concept","conf":0.6,"band":"medium","color":"#f08c00","val":8,"href":"concepts/reranking/"},{"id":"retrieval-augmented-generation","name":"Retrieval-Augmented Generation (RAG)","type":"concept","conf":0.8,"band":"high","color":"#2f9e44","val":28,"href":"concepts/retrieval-augmented-generation/"},{"id":"semantic-search","name":"Semantic Search","type":"concept","conf":0.65,"band":"medium","color":"#f08c00","val":20,"href":"concepts/semantic-search/"},{"id":"vector-database","name":"Vector Database","type":"concept","conf":0.6,"band":"medium","color":"#f08c00","val":15,"href":"concepts/vector-database/"},{"id":"zettelkasten","name":"Zettelkasten","type":"concept","conf":0.55,"band":"medium","color":"#f08c00","val":6,"href":"concepts/zettelkasten/"},{"id":"akari-asai","name":"Akari Asai","type":"entity","conf":0.6,"band":"medium","color":"#f08c00","val":3,"href":"entities/akari-asai/"},{"id":"andrej-karpathy","name":"Andrej Karpathy","type":"entity","conf":0.85,"band":"high","color":"#2f9e44","val":5,"href":"entities/andrej-karpathy/"},{"id":"anthropic","name":"Anthropic","type":"entity","conf":0.65,"band":"medium","color":"#f08c00","val":6,"href":"entities/anthropic/"},{"id":"asdlc-knowledge-base","name":"ASDLC Knowledge Base","type":"entity","conf":0.9,"band":"high","color":"#2f9e44","val":13,"href":"entities/asdlc-knowledge-base/"},{"id":"darren-edge","name":"Darren Edge","type":"entity","conf":0.6,"band":"medium","color":"#f08c00","val":5,"href":"entities/darren-edge/"},{"id":"docling","name":"Docling","type":"entity","conf":0.55,"band":"medium","color":"#f08c00","val":6,"href":"entities/docling/"},{"id":"faiss","name":"FAISS","type":"entity","conf":0.6,"band":"medium","color":"#f08c00","val":9,"href":"entities/faiss/"},{"id":"markitdown","name":"MarkItDown","type":"entity","conf":0.55,"band":"medium","color":"#f08c00","val":5,"href":"entities/markitdown/"},{"id":"meta-ai","name":"Meta AI (FAIR)","type":"entity","conf":0.6,"band":"medium","color":"#f08c00","val":8,"href":"entities/meta-ai/"},{"id":"microsoft-research","name":"Microsoft Research","type":"entity","conf":0.6,"band":"medium","color":"#f08c00","val":6,"href":"entities/microsoft-research/"},{"id":"mkdocs","name":"MkDocs","type":"entity","conf":0.55,"band":"medium","color":"#f08c00","val":4,"href":"entities/mkdocs/"},{"id":"nils-reimers","name":"Nils Reimers","type":"entity","conf":0.6,"band":"medium","color":"#f08c00","val":4,"href":"entities/nils-reimers/"},{"id":"obsidian","name":"Obsidian","type":"entity","conf":0.55,"band":"medium","color":"#f08c00","val":5,"href":"entities/obsidian/"},{"id":"patrick-lewis","name":"Patrick Lewis","type":"entity","conf":0.7,"band":"medium","color":"#f08c00","val":4,"href":"entities/patrick-lewis/"},{"id":"vladimir-karpukhin","name":"Vladimir Karpukhin","type":"entity","conf":0.6,"band":"medium","color":"#f08c00","val":5,"href":"entities/vladimir-karpukhin/"},{"id":"yury-malkov","name":"Yury Malkov","type":"entity","conf":0.6,"band":"medium","color":"#f08c00","val":6,"href":"entities/yury-malkov/"},{"id":"asdlc-knowledge-readme","name":"ASDLC Knowledge Base \u2014 README","type":"source","conf":0.9,"band":"high","color":"#2f9e44","val":5,"href":"sources/asdlc-knowledge-readme/"},{"id":"dpr-karpukhin-2020","name":"Dense Passage Retrieval for Open-Domain Question Answering","type":"source","conf":0.75,"band":"high","color":"#2f9e44","val":8,"href":"sources/dpr-karpukhin-2020/"},{"id":"faiss-johnson-2017","name":"Billion-scale Similarity Search with GPUs","type":"source","conf":0.75,"band":"high","color":"#2f9e44","val":7,"href":"sources/faiss-johnson-2017/"},{"id":"graphrag-edge-2024","name":"From Local to Global: A Graph RAG Approach to Query-Focused Summarization","type":"source","conf":0.75,"band":"high","color":"#2f9e44","val":5,"href":"sources/graphrag-edge-2024/"},{"id":"hnsw-malkov-2016","name":"Efficient and Robust ANN Search Using Hierarchical Navigable Small World Graphs","type":"source","conf":0.75,"band":"high","color":"#2f9e44","val":7,"href":"sources/hnsw-malkov-2016/"},{"id":"karpathy-llm-wiki","name":"Karpathy \u2014 LLM Wiki gist","type":"source","conf":0.9,"band":"high","color":"#2f9e44","val":3,"href":"sources/karpathy-llm-wiki/"},{"id":"llm-wiki-setup-guide-2026","name":"LLM Wiki Setup: Karpathy's Knowledge Base (2026 Guide)","type":"source","conf":0.5,"band":"medium","color":"#f08c00","val":5,"href":"sources/llm-wiki-setup-guide-2026/"},{"id":"mcp-anthropic-2024","name":"Introducing the Model Context Protocol","type":"source","conf":0.75,"band":"high","color":"#2f9e44","val":5,"href":"sources/mcp-anthropic-2024/"},{"id":"rag-lewis-2020","name":"Lewis et al. \u2014 Retrieval-Augmented Generation (2020)","type":"source","conf":0.85,"band":"high","color":"#2f9e44","val":3,"href":"sources/rag-lewis-2020/"},{"id":"self-rag-asai-2023","name":"Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection","type":"source","conf":0.75,"band":"high","color":"#2f9e44","val":7,"href":"sources/self-rag-asai-2023/"},{"id":"sentence-bert-2019","name":"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks","type":"source","conf":0.75,"band":"high","color":"#2f9e44","val":5,"href":"sources/sentence-bert-2019/"}],"links":[{"source":"agentic-memory","target":"knowledge-management-for-llms"},{"source":"agentic-memory","target":"semantic-search"},{"source":"agentic-memory","target":"embeddings"},{"source":"agentic-memory","target":"knowledge-graph"},{"source":"agentic-memory","target":"llm-wiki-pattern"},{"source":"agentic-memory","target":"retrieval-augmented-generation"},{"source":"agentic-memory","target":"context-engineering"},{"source":"agentic-memory","target":"asdlc-knowledge-base"},{"source":"agentic-memory","target":"hallucination"},{"source":"agentic-memory","target":"self-rag-asai-2023"},{"source":"agentic-memory","target":"model-context-protocol"},{"source":"approximate-nearest-neighbor","target":"embeddings"},{"source":"approximate-nearest-neighbor","target":"vector-database"},{"source":"approximate-nearest-neighbor","target":"semantic-search"},{"source":"approximate-nearest-neighbor","target":"hnsw-malkov-2016"},{"source":"approximate-nearest-neighbor","target":"faiss-johnson-2017"},{"source":"approximate-nearest-neighbor","target":"knowledge-management-for-llms"},{"source":"chunking","target":"embeddings"},{"source":"chunking","target":"semantic-search"},{"source":"chunking","target":"retrieval-augmented-generation"},{"source":"chunking","target":"llm-wiki-pattern"},{"source":"chunking","target":"context-engineering"},{"source":"chunking","target":"knowledge-graph"},{"source":"context-engineering","target":"knowledge-management-for-llms"},{"source":"context-engineering","target":"hallucination"},{"source":"context-engineering","target":"semantic-search"},{"source":"context-engineering","target":"hybrid-search"},{"source":"context-engineering","target":"reranking"},{"source":"context-engineering","target":"model-context-protocol"},{"source":"context-engineering","target":"llm-wiki-pattern"},{"source":"embeddings","target":"semantic-search"},{"source":"embeddings","target":"vector-database"},{"source":"embeddings","target":"retrieval-augmented-generation"},{"source":"embeddings","target":"sentence-bert-2019"},{"source":"embeddings","target":"dpr-karpukhin-2020"},{"source":"embeddings","target":"llm-wiki-pattern"},{"source":"embeddings","target":"knowledge-management-for-llms"},{"source":"graph-rag","target":"retrieval-augmented-generation"},{"source":"graph-rag","target":"knowledge-graph"},{"source":"graph-rag","target":"microsoft-research"},{"source":"graph-rag","target":"graphrag-edge-2024"},{"source":"graph-rag","target":"chunking"},{"source":"graph-rag","target":"semantic-search"},{"source":"graph-rag","target":"knowledge-management-for-llms"},{"source":"graph-rag","target":"self-rag-asai-2023"},{"source":"hallucination","target":"knowledge-management-for-llms"},{"source":"hallucination","target":"retrieval-augmented-generation"},{"source":"hallucination","target":"self-rag-asai-2023"},{"source":"hallucination","target":"reranking"},{"source":"hallucination","target":"hybrid-search"},{"source":"hallucination","target":"graph-rag"},{"source":"hallucination","target":"asdlc-knowledge-base"},{"source":"hybrid-search","target":"embeddings"},{"source":"hybrid-search","target":"semantic-search"},{"source":"hybrid-search","target":"retrieval-augmented-generation"},{"source":"hybrid-search","target":"dpr-karpukhin-2020"},{"source":"hybrid-search","target":"reranking"},{"source":"hybrid-search","target":"vector-database"},{"source":"hybrid-search","target":"knowledge-management-for-llms"},{"source":"knowledge-graph","target":"embeddings"},{"source":"knowledge-graph","target":"retrieval-augmented-generation"},{"source":"knowledge-graph","target":"llm-wiki-pattern"},{"source":"knowledge-graph","target":"knowledge-management-for-llms"},{"source":"knowledge-graph","target":"zettelkasten"},{"source":"knowledge-management-for-llms","target":"retrieval-augmented-generation"},{"source":"knowledge-management-for-llms","target":"vector-database"},{"source":"knowledge-management-for-llms","target":"semantic-search"},{"source":"knowledge-management-for-llms","target":"zettelkasten"},{"source":"knowledge-management-for-llms","target":"llm-wiki-pattern"},{"source":"knowledge-management-for-llms","target":"model-context-protocol"},{"source":"knowledge-management-for-llms","target":"reranking"},{"source":"knowledge-management-for-llms","target":"chunking"},{"source":"knowledge-management-for-llms","target":"self-rag-asai-2023"},{"source":"knowledge-management-for-llms","target":"asdlc-knowledge-base"},{"source":"llm-wiki-pattern","target":"retrieval-augmented-generation"},{"source":"llm-wiki-pattern","target":"karpathy-llm-wiki"},{"source":"llm-wiki-pattern","target":"andrej-karpathy"},{"source":"llm-wiki-pattern","target":"asdlc-knowledge-base"},{"source":"llm-wiki-pattern","target":"llm-wiki-setup-guide-2026"},{"source":"llm-wiki-pattern","target":"zettelkasten"},{"source":"llm-wiki-pattern","target":"obsidian"},{"source":"llm-wiki-pattern","target":"vector-database"},{"source":"llm-wiki-pattern","target":"mkdocs"},{"source":"model-context-protocol","target":"anthropic"},{"source":"model-context-protocol","target":"mcp-anthropic-2024"},{"source":"model-context-protocol","target":"llm-wiki-pattern"},{"source":"model-context-protocol","target":"asdlc-knowledge-base"},{"source":"model-context-protocol","target":"retrieval-augmented-generation"},{"source":"model-context-protocol","target":"vector-database"},{"source":"reranking","target":"retrieval-augmented-generation"},{"source":"reranking","target":"sentence-bert-2019"},{"source":"reranking","target":"approximate-nearest-neighbor"},{"source":"retrieval-augmented-generation","target":"rag-lewis-2020"},{"source":"retrieval-augmented-generation","target":"vector-database"},{"source":"retrieval-augmented-generation","target":"approximate-nearest-neighbor"},{"source":"retrieval-augmented-generation","target":"semantic-search"},{"source":"retrieval-augmented-generation","target":"context-engineering"},{"source":"retrieval-augmented-generation","target":"self-rag-asai-2023"},{"source":"retrieval-augmented-generation","target":"llm-wiki-setup-guide-2026"},{"source":"semantic-search","target":"vector-database"},{"source":"semantic-search","target":"reranking"},{"source":"semantic-search","target":"dpr-karpukhin-2020"},{"source":"semantic-search","target":"self-rag-asai-2023"},{"source":"semantic-search","target":"hallucination"},{"source":"vector-database","target":"hnsw-malkov-2016"},{"source":"vector-database","target":"faiss-johnson-2017"},{"source":"vector-database","target":"faiss"},{"source":"vector-database","target":"knowledge-graph"},{"source":"zettelkasten","target":"obsidian"},{"source":"zettelkasten","target":"context-engineering"},{"source":"zettelkasten","target":"chunking"},{"source":"akari-asai","target":"retrieval-augmented-generation"},{"source":"akari-asai","target":"self-rag-asai-2023"},{"source":"akari-asai","target":"hallucination"},{"source":"andrej-karpathy","target":"karpathy-llm-wiki"},{"source":"andrej-karpathy","target":"llm-wiki-setup-guide-2026"},{"source":"anthropic","target":"mcp-anthropic-2024"},{"source":"anthropic","target":"agentic-memory"},{"source":"anthropic","target":"context-engineering"},{"source":"anthropic","target":"knowledge-management-for-llms"},{"source":"anthropic","target":"asdlc-knowledge-base"},{"source":"asdlc-knowledge-base","target":"asdlc-knowledge-readme"},{"source":"asdlc-knowledge-base","target":"andrej-karpathy"},{"source":"asdlc-knowledge-base","target":"retrieval-augmented-generation"},{"source":"darren-edge","target":"microsoft-research"},{"source":"darren-edge","target":"graphrag-edge-2024"},{"source":"darren-edge","target":"graph-rag"},{"source":"darren-edge","target":"retrieval-augmented-generation"},{"source":"darren-edge","target":"knowledge-graph"},{"source":"docling","target":"asdlc-knowledge-base"},{"source":"docling","target":"markitdown"},{"source":"docling","target":"chunking"},{"source":"docling","target":"embeddings"},{"source":"docling","target":"llm-wiki-pattern"},{"source":"docling","target":"knowledge-management-for-llms"},{"source":"faiss","target":"meta-ai"},{"source":"faiss","target":"embeddings"},{"source":"faiss","target":"approximate-nearest-neighbor"},{"source":"faiss","target":"faiss-johnson-2017"},{"source":"faiss","target":"hnsw-malkov-2016"},{"source":"faiss","target":"semantic-search"},{"source":"faiss","target":"knowledge-management-for-llms"},{"source":"markitdown","target":"asdlc-knowledge-base"},{"source":"markitdown","target":"knowledge-management-for-llms"},{"source":"markitdown","target":"llm-wiki-pattern"},{"source":"markitdown","target":"llm-wiki-setup-guide-2026"},{"source":"meta-ai","target":"dpr-karpukhin-2020"},{"source":"meta-ai","target":"faiss-johnson-2017"},{"source":"meta-ai","target":"approximate-nearest-neighbor"},{"source":"meta-ai","target":"vector-database"},{"source":"meta-ai","target":"embeddings"},{"source":"meta-ai","target":"knowledge-management-for-llms"},{"source":"microsoft-research","target":"graphrag-edge-2024"},{"source":"microsoft-research","target":"retrieval-augmented-generation"},{"source":"microsoft-research","target":"knowledge-graph"},{"source":"microsoft-research","target":"knowledge-management-for-llms"},{"source":"mkdocs","target":"asdlc-knowledge-base"},{"source":"mkdocs","target":"knowledge-graph"},{"source":"mkdocs","target":"knowledge-management-for-llms"},{"source":"nils-reimers","target":"embeddings"},{"source":"nils-reimers","target":"semantic-search"},{"source":"nils-reimers","target":"sentence-bert-2019"},{"source":"nils-reimers","target":"retrieval-augmented-generation"},{"source":"obsidian","target":"llm-wiki-setup-guide-2026"},{"source":"obsidian","target":"knowledge-graph"},{"source":"obsidian","target":"knowledge-management-for-llms"},{"source":"patrick-lewis","target":"rag-lewis-2020"},{"source":"patrick-lewis","target":"retrieval-augmented-generation"},{"source":"vladimir-karpukhin","target":"embeddings"},{"source":"vladimir-karpukhin","target":"dpr-karpukhin-2020"},{"source":"vladimir-karpukhin","target":"meta-ai"},{"source":"vladimir-karpukhin","target":"retrieval-augmented-generation"},{"source":"vladimir-karpukhin","target":"patrick-lewis"},{"source":"yury-malkov","target":"approximate-nearest-neighbor"},{"source":"yury-malkov","target":"vector-database"},{"source":"yury-malkov","target":"hnsw-malkov-2016"},{"source":"yury-malkov","target":"semantic-search"},{"source":"yury-malkov","target":"embeddings"},{"source":"yury-malkov","target":"faiss"},{"source":"asdlc-knowledge-readme","target":"llm-wiki-pattern"},{"source":"asdlc-knowledge-readme","target":"retrieval-augmented-generation"},{"source":"asdlc-knowledge-readme","target":"andrej-karpathy"},{"source":"asdlc-knowledge-readme","target":"karpathy-llm-wiki"},{"source":"dpr-karpukhin-2020","target":"patrick-lewis"},{"source":"dpr-karpukhin-2020","target":"retrieval-augmented-generation"},{"source":"dpr-karpukhin-2020","target":"approximate-nearest-neighbor"},{"source":"faiss-johnson-2017","target":"embeddings"},{"source":"faiss-johnson-2017","target":"semantic-search"},{"source":"faiss-johnson-2017","target":"hnsw-malkov-2016"},{"source":"graphrag-edge-2024","target":"knowledge-graph"},{"source":"graphrag-edge-2024","target":"retrieval-augmented-generation"},{"source":"hnsw-malkov-2016","target":"semantic-search"},{"source":"hnsw-malkov-2016","target":"embeddings"},{"source":"mcp-anthropic-2024","target":"context-engineering"},{"source":"mcp-anthropic-2024","target":"agentic-memory"},{"source":"mcp-anthropic-2024","target":"asdlc-knowledge-base"},{"source":"rag-lewis-2020","target":"llm-wiki-pattern"},{"source":"sentence-bert-2019","target":"semantic-search"},{"source":"sentence-bert-2019","target":"vector-database"}]}</script>
<script>
(function(){
 var g=null;
 window.kbShowView=function(v){
  var pre=document.querySelector('pre.mermaid');
  var box=document.getElementById('kb-graph-3d');
  var b2=document.getElementById('kb-btn-2d'),b3=document.getElementById('kb-btn-3d');
  if(v==='3d'){ if(pre)pre.style.display='none'; box.style.display='block'; b3.classList.add('kb-active'); b2.classList.remove('kb-active'); kbInit(box); }
  else { if(pre)pre.style.display=''; box.style.display='none'; b2.classList.add('kb-active'); b3.classList.remove('kb-active'); }
 };
 function kbInit(box){
  if(g){ g.width(box.clientWidth); return; }
  if(typeof ForceGraph3D==='undefined'){ box.innerHTML='<div class="kb-msg">The 3D force-graph library did not load (offline?). The 2D view above has the full graph.</div>'; return; }
  var data=JSON.parse(document.getElementById('kb-graph-data').textContent);
  g=ForceGraph3D()(box).graphData(data)
    .backgroundColor('rgba(0,0,0,0)')
    .nodeColor(function(n){return n.color;})
    .nodeVal(function(n){return n.val;})
    .nodeRelSize(4)
    .nodeLabel(function(n){return '<b>'+n.name+'</b><br>'+n.type+' · '+n.conf+' '+n.band+'<br><small>click to focus · '+(navigator.platform.indexOf('Mac')>-1?'⌘':'Ctrl')+'/Shift-click to open</small>';})
    .linkColor(function(){return 'rgba(136,136,136,0.4)';})
    .linkWidth(0.5)
    .width(box.clientWidth).height(560);
  g.onNodeClick(function(n,e){
    // Modifier-click opens the page; a plain click focuses the camera on it.
    if(e&&(e.shiftKey||e.ctrlKey||e.metaKey)){ if(n.href)window.location.href=n.href; return; }
    var r=1+90/Math.hypot(n.x||1,n.y||1,n.z||1);
    g.cameraPosition({x:(n.x||0)*r,y:(n.y||0)*r,z:(n.z||0)*r},n,1200);
  });
  window.addEventListener('resize',function(){ if(g)g.width(box.clientWidth); });
 }
})();
</script>
</div>

```mermaid
graph LR
  agentic_memory["Agentic Memory<br/>0.55 · medium"]
  style agentic_memory fill:#f08c0022,stroke:#f08c00
  click agentic_memory "concepts/agentic-memory/" "Open page" _self
  approximate_nearest_neighbor["Approximate Nearest Neighbor Search<br/>0.65 · medium"]
  style approximate_nearest_neighbor fill:#f08c0022,stroke:#f08c00
  click approximate_nearest_neighbor "concepts/approximate-nearest-neighbor/" "Open page" _self
  chunking["Chunking<br/>0.55 · medium"]
  style chunking fill:#f08c0022,stroke:#f08c00
  click chunking "concepts/chunking/" "Open page" _self
  context_engineering["Context Engineering<br/>0.55 · medium"]
  style context_engineering fill:#f08c0022,stroke:#f08c00
  click context_engineering "concepts/context-engineering/" "Open page" _self
  embeddings["Embeddings<br/>0.65 · medium"]
  style embeddings fill:#f08c0022,stroke:#f08c00
  click embeddings "concepts/embeddings/" "Open page" _self
  graph_rag["GraphRAG<br/>0.6 · medium"]
  style graph_rag fill:#f08c0022,stroke:#f08c00
  click graph_rag "concepts/graph-rag/" "Open page" _self
  hallucination["Hallucination<br/>0.6 · medium"]
  style hallucination fill:#f08c0022,stroke:#f08c00
  click hallucination "concepts/hallucination/" "Open page" _self
  hybrid_search["Hybrid Search<br/>0.6 · medium"]
  style hybrid_search fill:#f08c0022,stroke:#f08c00
  click hybrid_search "concepts/hybrid-search/" "Open page" _self
  knowledge_graph["Knowledge Graph<br/>0.6 · medium"]
  style knowledge_graph fill:#f08c0022,stroke:#f08c00
  click knowledge_graph "concepts/knowledge-graph/" "Open page" _self
  knowledge_management_for_llms["Knowledge Management for LLMs<br/>0.6 · medium"]
  style knowledge_management_for_llms fill:#f08c0022,stroke:#f08c00
  click knowledge_management_for_llms "concepts/knowledge-management-for-llms/" "Open page" _self
  llm_wiki_pattern["LLM Wiki Pattern<br/>0.8 · high"]
  style llm_wiki_pattern fill:#2f9e4422,stroke:#2f9e44
  click llm_wiki_pattern "concepts/llm-wiki-pattern/" "Open page" _self
  model_context_protocol["Model Context Protocol (MCP)<br/>0.65 · medium"]
  style model_context_protocol fill:#f08c0022,stroke:#f08c00
  click model_context_protocol "concepts/model-context-protocol/" "Open page" _self
  reranking["Reranking<br/>0.6 · medium"]
  style reranking fill:#f08c0022,stroke:#f08c00
  click reranking "concepts/reranking/" "Open page" _self
  retrieval_augmented_generation["Retrieval-Augmented Generation (RAG)<br/>0.8 · high"]
  style retrieval_augmented_generation fill:#2f9e4422,stroke:#2f9e44
  click retrieval_augmented_generation "concepts/retrieval-augmented-generation/" "Open page" _self
  semantic_search["Semantic Search<br/>0.65 · medium"]
  style semantic_search fill:#f08c0022,stroke:#f08c00
  click semantic_search "concepts/semantic-search/" "Open page" _self
  vector_database["Vector Database<br/>0.6 · medium"]
  style vector_database fill:#f08c0022,stroke:#f08c00
  click vector_database "concepts/vector-database/" "Open page" _self
  zettelkasten["Zettelkasten<br/>0.55 · medium"]
  style zettelkasten fill:#f08c0022,stroke:#f08c00
  click zettelkasten "concepts/zettelkasten/" "Open page" _self
  akari_asai["Akari Asai<br/>0.6 · medium"]
  style akari_asai fill:#f08c0022,stroke:#f08c00
  click akari_asai "entities/akari-asai/" "Open page" _self
  andrej_karpathy["Andrej Karpathy<br/>0.85 · high"]
  style andrej_karpathy fill:#2f9e4422,stroke:#2f9e44
  click andrej_karpathy "entities/andrej-karpathy/" "Open page" _self
  anthropic["Anthropic<br/>0.65 · medium"]
  style anthropic fill:#f08c0022,stroke:#f08c00
  click anthropic "entities/anthropic/" "Open page" _self
  asdlc_knowledge_base["ASDLC Knowledge Base<br/>0.9 · high"]
  style asdlc_knowledge_base fill:#2f9e4422,stroke:#2f9e44
  click asdlc_knowledge_base "entities/asdlc-knowledge-base/" "Open page" _self
  darren_edge["Darren Edge<br/>0.6 · medium"]
  style darren_edge fill:#f08c0022,stroke:#f08c00
  click darren_edge "entities/darren-edge/" "Open page" _self
  docling["Docling<br/>0.55 · medium"]
  style docling fill:#f08c0022,stroke:#f08c00
  click docling "entities/docling/" "Open page" _self
  faiss["FAISS<br/>0.6 · medium"]
  style faiss fill:#f08c0022,stroke:#f08c00
  click faiss "entities/faiss/" "Open page" _self
  markitdown["MarkItDown<br/>0.55 · medium"]
  style markitdown fill:#f08c0022,stroke:#f08c00
  click markitdown "entities/markitdown/" "Open page" _self
  meta_ai["Meta AI (FAIR)<br/>0.6 · medium"]
  style meta_ai fill:#f08c0022,stroke:#f08c00
  click meta_ai "entities/meta-ai/" "Open page" _self
  microsoft_research["Microsoft Research<br/>0.6 · medium"]
  style microsoft_research fill:#f08c0022,stroke:#f08c00
  click microsoft_research "entities/microsoft-research/" "Open page" _self
  mkdocs["MkDocs<br/>0.55 · medium"]
  style mkdocs fill:#f08c0022,stroke:#f08c00
  click mkdocs "entities/mkdocs/" "Open page" _self
  nils_reimers["Nils Reimers<br/>0.6 · medium"]
  style nils_reimers fill:#f08c0022,stroke:#f08c00
  click nils_reimers "entities/nils-reimers/" "Open page" _self
  obsidian["Obsidian<br/>0.55 · medium"]
  style obsidian fill:#f08c0022,stroke:#f08c00
  click obsidian "entities/obsidian/" "Open page" _self
  patrick_lewis["Patrick Lewis<br/>0.7 · medium"]
  style patrick_lewis fill:#f08c0022,stroke:#f08c00
  click patrick_lewis "entities/patrick-lewis/" "Open page" _self
  vladimir_karpukhin["Vladimir Karpukhin<br/>0.6 · medium"]
  style vladimir_karpukhin fill:#f08c0022,stroke:#f08c00
  click vladimir_karpukhin "entities/vladimir-karpukhin/" "Open page" _self
  yury_malkov["Yury Malkov<br/>0.6 · medium"]
  style yury_malkov fill:#f08c0022,stroke:#f08c00
  click yury_malkov "entities/yury-malkov/" "Open page" _self
  asdlc_knowledge_readme["ASDLC Knowledge Base — README<br/>0.9 · high"]
  style asdlc_knowledge_readme fill:#2f9e4422,stroke:#2f9e44
  click asdlc_knowledge_readme "sources/asdlc-knowledge-readme/" "Open page" _self
  dpr_karpukhin_2020["Dense Passage Retrieval for Open-Domain Question Answering<br/>0.75 · high"]
  style dpr_karpukhin_2020 fill:#2f9e4422,stroke:#2f9e44
  click dpr_karpukhin_2020 "sources/dpr-karpukhin-2020/" "Open page" _self
  faiss_johnson_2017["Billion-scale Similarity Search with GPUs<br/>0.75 · high"]
  style faiss_johnson_2017 fill:#2f9e4422,stroke:#2f9e44
  click faiss_johnson_2017 "sources/faiss-johnson-2017/" "Open page" _self
  graphrag_edge_2024["From Local to Global: A Graph RAG Approach to Query-Focused Summarization<br/>0.75 · high"]
  style graphrag_edge_2024 fill:#2f9e4422,stroke:#2f9e44
  click graphrag_edge_2024 "sources/graphrag-edge-2024/" "Open page" _self
  hnsw_malkov_2016["Efficient and Robust ANN Search Using Hierarchical Navigable Small World Graphs<br/>0.75 · high"]
  style hnsw_malkov_2016 fill:#2f9e4422,stroke:#2f9e44
  click hnsw_malkov_2016 "sources/hnsw-malkov-2016/" "Open page" _self
  karpathy_llm_wiki["Karpathy — LLM Wiki gist<br/>0.9 · high"]
  style karpathy_llm_wiki fill:#2f9e4422,stroke:#2f9e44
  click karpathy_llm_wiki "sources/karpathy-llm-wiki/" "Open page" _self
  llm_wiki_setup_guide_2026["LLM Wiki Setup: Karpathy's Knowledge Base (2026 Guide)<br/>0.5 · medium"]
  style llm_wiki_setup_guide_2026 fill:#f08c0022,stroke:#f08c00
  click llm_wiki_setup_guide_2026 "sources/llm-wiki-setup-guide-2026/" "Open page" _self
  mcp_anthropic_2024["Introducing the Model Context Protocol<br/>0.75 · high"]
  style mcp_anthropic_2024 fill:#2f9e4422,stroke:#2f9e44
  click mcp_anthropic_2024 "sources/mcp-anthropic-2024/" "Open page" _self
  rag_lewis_2020["Lewis et al. — Retrieval-Augmented Generation (2020)<br/>0.85 · high"]
  style rag_lewis_2020 fill:#2f9e4422,stroke:#2f9e44
  click rag_lewis_2020 "sources/rag-lewis-2020/" "Open page" _self
  self_rag_asai_2023["Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection<br/>0.75 · high"]
  style self_rag_asai_2023 fill:#2f9e4422,stroke:#2f9e44
  click self_rag_asai_2023 "sources/self-rag-asai-2023/" "Open page" _self
  sentence_bert_2019["Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks<br/>0.75 · high"]
  style sentence_bert_2019 fill:#2f9e4422,stroke:#2f9e44
  click sentence_bert_2019 "sources/sentence-bert-2019/" "Open page" _self
  agentic_memory --> knowledge_management_for_llms
  agentic_memory --> semantic_search
  agentic_memory --> embeddings
  agentic_memory --> knowledge_graph
  agentic_memory --> llm_wiki_pattern
  agentic_memory --> retrieval_augmented_generation
  agentic_memory --> context_engineering
  agentic_memory --> asdlc_knowledge_base
  agentic_memory --> hallucination
  agentic_memory --> self_rag_asai_2023
  agentic_memory --> model_context_protocol
  approximate_nearest_neighbor --> embeddings
  approximate_nearest_neighbor --> vector_database
  approximate_nearest_neighbor --> semantic_search
  approximate_nearest_neighbor --> hnsw_malkov_2016
  approximate_nearest_neighbor --> faiss_johnson_2017
  approximate_nearest_neighbor --> knowledge_management_for_llms
  chunking --> embeddings
  chunking --> semantic_search
  chunking --> retrieval_augmented_generation
  chunking --> llm_wiki_pattern
  chunking --> context_engineering
  chunking --> knowledge_graph
  context_engineering --> knowledge_management_for_llms
  context_engineering --> hallucination
  context_engineering --> semantic_search
  context_engineering --> hybrid_search
  context_engineering --> reranking
  context_engineering --> chunking
  context_engineering --> model_context_protocol
  context_engineering --> agentic_memory
  context_engineering --> llm_wiki_pattern
  embeddings --> semantic_search
  embeddings --> vector_database
  embeddings --> retrieval_augmented_generation
  embeddings --> sentence_bert_2019
  embeddings --> dpr_karpukhin_2020
  embeddings --> approximate_nearest_neighbor
  embeddings --> llm_wiki_pattern
  embeddings --> knowledge_management_for_llms
  graph_rag --> retrieval_augmented_generation
  graph_rag --> knowledge_graph
  graph_rag --> microsoft_research
  graph_rag --> graphrag_edge_2024
  graph_rag --> chunking
  graph_rag --> semantic_search
  graph_rag --> knowledge_management_for_llms
  graph_rag --> self_rag_asai_2023
  hallucination --> knowledge_management_for_llms
  hallucination --> retrieval_augmented_generation
  hallucination --> self_rag_asai_2023
  hallucination --> reranking
  hallucination --> hybrid_search
  hallucination --> graph_rag
  hallucination --> asdlc_knowledge_base
  hallucination --> agentic_memory
  hybrid_search --> embeddings
  hybrid_search --> semantic_search
  hybrid_search --> retrieval_augmented_generation
  hybrid_search --> dpr_karpukhin_2020
  hybrid_search --> reranking
  hybrid_search --> vector_database
  hybrid_search --> knowledge_management_for_llms
  knowledge_graph --> embeddings
  knowledge_graph --> graph_rag
  knowledge_graph --> retrieval_augmented_generation
  knowledge_graph --> llm_wiki_pattern
  knowledge_graph --> knowledge_management_for_llms
  knowledge_graph --> zettelkasten
  knowledge_management_for_llms --> retrieval_augmented_generation
  knowledge_management_for_llms --> embeddings
  knowledge_management_for_llms --> vector_database
  knowledge_management_for_llms --> semantic_search
  knowledge_management_for_llms --> knowledge_graph
  knowledge_management_for_llms --> graph_rag
  knowledge_management_for_llms --> zettelkasten
  knowledge_management_for_llms --> llm_wiki_pattern
  knowledge_management_for_llms --> context_engineering
  knowledge_management_for_llms --> agentic_memory
  knowledge_management_for_llms --> model_context_protocol
  knowledge_management_for_llms --> reranking
  knowledge_management_for_llms --> hybrid_search
  knowledge_management_for_llms --> chunking
  knowledge_management_for_llms --> hallucination
  knowledge_management_for_llms --> self_rag_asai_2023
  knowledge_management_for_llms --> approximate_nearest_neighbor
  knowledge_management_for_llms --> asdlc_knowledge_base
  llm_wiki_pattern --> retrieval_augmented_generation
  llm_wiki_pattern --> karpathy_llm_wiki
  llm_wiki_pattern --> andrej_karpathy
  llm_wiki_pattern --> asdlc_knowledge_base
  llm_wiki_pattern --> llm_wiki_setup_guide_2026
  llm_wiki_pattern --> knowledge_management_for_llms
  llm_wiki_pattern --> knowledge_graph
  llm_wiki_pattern --> zettelkasten
  llm_wiki_pattern --> obsidian
  llm_wiki_pattern --> embeddings
  llm_wiki_pattern --> vector_database
  llm_wiki_pattern --> mkdocs
  model_context_protocol --> anthropic
  model_context_protocol --> mcp_anthropic_2024
  model_context_protocol --> agentic_memory
  model_context_protocol --> llm_wiki_pattern
  model_context_protocol --> asdlc_knowledge_base
  model_context_protocol --> context_engineering
  model_context_protocol --> retrieval_augmented_generation
  model_context_protocol --> vector_database
  model_context_protocol --> knowledge_management_for_llms
  reranking --> retrieval_augmented_generation
  reranking --> sentence_bert_2019
  reranking --> approximate_nearest_neighbor
  reranking --> hallucination
  reranking --> context_engineering
  reranking --> hybrid_search
  retrieval_augmented_generation --> rag_lewis_2020
  retrieval_augmented_generation --> knowledge_management_for_llms
  retrieval_augmented_generation --> chunking
  retrieval_augmented_generation --> embeddings
  retrieval_augmented_generation --> vector_database
  retrieval_augmented_generation --> approximate_nearest_neighbor
  retrieval_augmented_generation --> semantic_search
  retrieval_augmented_generation --> hybrid_search
  retrieval_augmented_generation --> reranking
  retrieval_augmented_generation --> context_engineering
  retrieval_augmented_generation --> graph_rag
  retrieval_augmented_generation --> knowledge_graph
  retrieval_augmented_generation --> self_rag_asai_2023
  retrieval_augmented_generation --> hallucination
  retrieval_augmented_generation --> llm_wiki_pattern
  retrieval_augmented_generation --> llm_wiki_setup_guide_2026
  semantic_search --> embeddings
  semantic_search --> retrieval_augmented_generation
  semantic_search --> chunking
  semantic_search --> vector_database
  semantic_search --> approximate_nearest_neighbor
  semantic_search --> reranking
  semantic_search --> dpr_karpukhin_2020
  semantic_search --> hybrid_search
  semantic_search --> self_rag_asai_2023
  semantic_search --> hallucination
  vector_database --> embeddings
  vector_database --> retrieval_augmented_generation
  vector_database --> approximate_nearest_neighbor
  vector_database --> hnsw_malkov_2016
  vector_database --> faiss_johnson_2017
  vector_database --> hybrid_search
  vector_database --> faiss
  vector_database --> knowledge_graph
  vector_database --> llm_wiki_pattern
  vector_database --> knowledge_management_for_llms
  zettelkasten --> llm_wiki_pattern
  zettelkasten --> obsidian
  zettelkasten --> knowledge_graph
  zettelkasten --> context_engineering
  zettelkasten --> chunking
  zettelkasten --> knowledge_management_for_llms
  akari_asai --> retrieval_augmented_generation
  akari_asai --> self_rag_asai_2023
  akari_asai --> hallucination
  andrej_karpathy --> llm_wiki_pattern
  andrej_karpathy --> karpathy_llm_wiki
  andrej_karpathy --> llm_wiki_setup_guide_2026
  anthropic --> model_context_protocol
  anthropic --> mcp_anthropic_2024
  anthropic --> agentic_memory
  anthropic --> context_engineering
  anthropic --> knowledge_management_for_llms
  anthropic --> asdlc_knowledge_base
  asdlc_knowledge_base --> llm_wiki_pattern
  asdlc_knowledge_base --> asdlc_knowledge_readme
  asdlc_knowledge_base --> andrej_karpathy
  asdlc_knowledge_base --> retrieval_augmented_generation
  darren_edge --> microsoft_research
  darren_edge --> graphrag_edge_2024
  darren_edge --> graph_rag
  darren_edge --> retrieval_augmented_generation
  darren_edge --> knowledge_graph
  docling --> asdlc_knowledge_base
  docling --> markitdown
  docling --> chunking
  docling --> embeddings
  docling --> llm_wiki_pattern
  docling --> knowledge_management_for_llms
  faiss --> meta_ai
  faiss --> embeddings
  faiss --> approximate_nearest_neighbor
  faiss --> faiss_johnson_2017
  faiss --> hnsw_malkov_2016
  faiss --> vector_database
  faiss --> semantic_search
  faiss --> knowledge_management_for_llms
  markitdown --> asdlc_knowledge_base
  markitdown --> knowledge_management_for_llms
  markitdown --> llm_wiki_pattern
  markitdown --> docling
  markitdown --> llm_wiki_setup_guide_2026
  meta_ai --> dpr_karpukhin_2020
  meta_ai --> faiss_johnson_2017
  meta_ai --> approximate_nearest_neighbor
  meta_ai --> faiss
  meta_ai --> vector_database
  meta_ai --> embeddings
  meta_ai --> knowledge_management_for_llms
  microsoft_research --> darren_edge
  microsoft_research --> graphrag_edge_2024
  microsoft_research --> graph_rag
  microsoft_research --> retrieval_augmented_generation
  microsoft_research --> knowledge_graph
  microsoft_research --> knowledge_management_for_llms
  mkdocs --> llm_wiki_pattern
  mkdocs --> asdlc_knowledge_base
  mkdocs --> knowledge_graph
  mkdocs --> knowledge_management_for_llms
  nils_reimers --> embeddings
  nils_reimers --> semantic_search
  nils_reimers --> sentence_bert_2019
  nils_reimers --> retrieval_augmented_generation
  obsidian --> zettelkasten
  obsidian --> llm_wiki_setup_guide_2026
  obsidian --> llm_wiki_pattern
  obsidian --> knowledge_graph
  obsidian --> knowledge_management_for_llms
  patrick_lewis --> rag_lewis_2020
  patrick_lewis --> retrieval_augmented_generation
  vladimir_karpukhin --> embeddings
  vladimir_karpukhin --> dpr_karpukhin_2020
  vladimir_karpukhin --> meta_ai
  vladimir_karpukhin --> retrieval_augmented_generation
  vladimir_karpukhin --> patrick_lewis
  yury_malkov --> approximate_nearest_neighbor
  yury_malkov --> vector_database
  yury_malkov --> hnsw_malkov_2016
  yury_malkov --> semantic_search
  yury_malkov --> embeddings
  yury_malkov --> faiss
  asdlc_knowledge_readme --> asdlc_knowledge_base
  asdlc_knowledge_readme --> llm_wiki_pattern
  asdlc_knowledge_readme --> retrieval_augmented_generation
  asdlc_knowledge_readme --> andrej_karpathy
  asdlc_knowledge_readme --> karpathy_llm_wiki
  dpr_karpukhin_2020 --> vladimir_karpukhin
  dpr_karpukhin_2020 --> meta_ai
  dpr_karpukhin_2020 --> embeddings
  dpr_karpukhin_2020 --> patrick_lewis
  dpr_karpukhin_2020 --> retrieval_augmented_generation
  dpr_karpukhin_2020 --> approximate_nearest_neighbor
  dpr_karpukhin_2020 --> semantic_search
  dpr_karpukhin_2020 --> hybrid_search
  faiss_johnson_2017 --> meta_ai
  faiss_johnson_2017 --> approximate_nearest_neighbor
  faiss_johnson_2017 --> embeddings
  faiss_johnson_2017 --> vector_database
  faiss_johnson_2017 --> faiss
  faiss_johnson_2017 --> semantic_search
  faiss_johnson_2017 --> hnsw_malkov_2016
  graphrag_edge_2024 --> graph_rag
  graphrag_edge_2024 --> darren_edge
  graphrag_edge_2024 --> microsoft_research
  graphrag_edge_2024 --> knowledge_graph
  graphrag_edge_2024 --> retrieval_augmented_generation
  hnsw_malkov_2016 --> yury_malkov
  hnsw_malkov_2016 --> approximate_nearest_neighbor
  hnsw_malkov_2016 --> vector_database
  hnsw_malkov_2016 --> faiss
  hnsw_malkov_2016 --> semantic_search
  hnsw_malkov_2016 --> embeddings
  karpathy_llm_wiki --> andrej_karpathy
  karpathy_llm_wiki --> llm_wiki_pattern
  llm_wiki_setup_guide_2026 --> llm_wiki_pattern
  llm_wiki_setup_guide_2026 --> andrej_karpathy
  llm_wiki_setup_guide_2026 --> retrieval_augmented_generation
  mcp_anthropic_2024 --> model_context_protocol
  mcp_anthropic_2024 --> anthropic
  mcp_anthropic_2024 --> context_engineering
  mcp_anthropic_2024 --> agentic_memory
  mcp_anthropic_2024 --> asdlc_knowledge_base
  rag_lewis_2020 --> retrieval_augmented_generation
  rag_lewis_2020 --> patrick_lewis
  rag_lewis_2020 --> llm_wiki_pattern
  self_rag_asai_2023 --> akari_asai
  self_rag_asai_2023 --> retrieval_augmented_generation
  self_rag_asai_2023 --> hallucination
  self_rag_asai_2023 --> graph_rag
  sentence_bert_2019 --> nils_reimers
  sentence_bert_2019 --> embeddings
  sentence_bert_2019 --> semantic_search
  sentence_bert_2019 --> reranking
  sentence_bert_2019 --> vector_database
```

## Connections

| Page | Type | Confidence | 🔗 | Connects to |
| --- | --- | --- | --- | --- |
| **[[retrieval-augmented-generation]]** | concept | 0.8 high | 28 | [[agentic-memory|agentic-memory]], [[akari-asai|akari-asai]], [[approximate-nearest-neighbor|approximate-nearest-neighbor]], [[asdlc-knowledge-base|asdlc-knowledge-base]], [[asdlc-knowledge-readme|asdlc-knowledge-readme]], [[chunking|chunking]], [[context-engineering|context-engineering]], [[darren-edge|darren-edge]], [[dpr-karpukhin-2020|dpr-karpukhin-2020]], [[embeddings|embeddings]], [[graph-rag|graph-rag]], [[graphrag-edge-2024|graphrag-edge-2024]], [[hallucination|hallucination]], [[hybrid-search|hybrid-search]], [[knowledge-graph|knowledge-graph]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[llm-wiki-pattern|llm-wiki-pattern]], [[llm-wiki-setup-guide-2026|llm-wiki-setup-guide-2026]], [[microsoft-research|microsoft-research]], [[model-context-protocol|model-context-protocol]], [[nils-reimers|nils-reimers]], [[patrick-lewis|patrick-lewis]], [[rag-lewis-2020|rag-lewis-2020]], [[reranking|reranking]], [[self-rag-asai-2023|self-rag-asai-2023]], [[semantic-search|semantic-search]], [[vector-database|vector-database]], [[vladimir-karpukhin|vladimir-karpukhin]] |
| **[[knowledge-management-for-llms]]** | concept | 0.6 medium | 26 | [[agentic-memory|agentic-memory]], [[anthropic|anthropic]], [[approximate-nearest-neighbor|approximate-nearest-neighbor]], [[asdlc-knowledge-base|asdlc-knowledge-base]], [[chunking|chunking]], [[context-engineering|context-engineering]], [[docling|docling]], [[embeddings|embeddings]], [[faiss|faiss]], [[graph-rag|graph-rag]], [[hallucination|hallucination]], [[hybrid-search|hybrid-search]], [[knowledge-graph|knowledge-graph]], [[llm-wiki-pattern|llm-wiki-pattern]], [[markitdown|markitdown]], [[meta-ai|meta-ai]], [[microsoft-research|microsoft-research]], [[mkdocs|mkdocs]], [[model-context-protocol|model-context-protocol]], [[obsidian|obsidian]], [[reranking|reranking]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[self-rag-asai-2023|self-rag-asai-2023]], [[semantic-search|semantic-search]], [[vector-database|vector-database]], [[zettelkasten|zettelkasten]] |
| **[[embeddings]]** | concept | 0.65 medium | 20 | [[agentic-memory|agentic-memory]], [[approximate-nearest-neighbor|approximate-nearest-neighbor]], [[chunking|chunking]], [[docling|docling]], [[dpr-karpukhin-2020|dpr-karpukhin-2020]], [[faiss|faiss]], [[faiss-johnson-2017|faiss-johnson-2017]], [[hnsw-malkov-2016|hnsw-malkov-2016]], [[hybrid-search|hybrid-search]], [[knowledge-graph|knowledge-graph]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[llm-wiki-pattern|llm-wiki-pattern]], [[meta-ai|meta-ai]], [[nils-reimers|nils-reimers]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[semantic-search|semantic-search]], [[sentence-bert-2019|sentence-bert-2019]], [[vector-database|vector-database]], [[vladimir-karpukhin|vladimir-karpukhin]], [[yury-malkov|yury-malkov]] |
| **[[llm-wiki-pattern]]** | concept | 0.8 high | 20 | [[agentic-memory|agentic-memory]], [[andrej-karpathy|andrej-karpathy]], [[asdlc-knowledge-base|asdlc-knowledge-base]], [[asdlc-knowledge-readme|asdlc-knowledge-readme]], [[chunking|chunking]], [[context-engineering|context-engineering]], [[docling|docling]], [[embeddings|embeddings]], [[karpathy-llm-wiki|karpathy-llm-wiki]], [[knowledge-graph|knowledge-graph]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[llm-wiki-setup-guide-2026|llm-wiki-setup-guide-2026]], [[markitdown|markitdown]], [[mkdocs|mkdocs]], [[model-context-protocol|model-context-protocol]], [[obsidian|obsidian]], [[rag-lewis-2020|rag-lewis-2020]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[vector-database|vector-database]], [[zettelkasten|zettelkasten]] |
| **[[semantic-search]]** | concept | 0.65 medium | 20 | [[agentic-memory|agentic-memory]], [[approximate-nearest-neighbor|approximate-nearest-neighbor]], [[chunking|chunking]], [[context-engineering|context-engineering]], [[dpr-karpukhin-2020|dpr-karpukhin-2020]], [[embeddings|embeddings]], [[faiss|faiss]], [[faiss-johnson-2017|faiss-johnson-2017]], [[graph-rag|graph-rag]], [[hallucination|hallucination]], [[hnsw-malkov-2016|hnsw-malkov-2016]], [[hybrid-search|hybrid-search]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[nils-reimers|nils-reimers]], [[reranking|reranking]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[self-rag-asai-2023|self-rag-asai-2023]], [[sentence-bert-2019|sentence-bert-2019]], [[vector-database|vector-database]], [[yury-malkov|yury-malkov]] |
| **[[vector-database]]** | concept | 0.6 medium | 15 | [[approximate-nearest-neighbor|approximate-nearest-neighbor]], [[embeddings|embeddings]], [[faiss|faiss]], [[faiss-johnson-2017|faiss-johnson-2017]], [[hnsw-malkov-2016|hnsw-malkov-2016]], [[hybrid-search|hybrid-search]], [[knowledge-graph|knowledge-graph]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[llm-wiki-pattern|llm-wiki-pattern]], [[meta-ai|meta-ai]], [[model-context-protocol|model-context-protocol]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[semantic-search|semantic-search]], [[sentence-bert-2019|sentence-bert-2019]], [[yury-malkov|yury-malkov]] |
| **[[knowledge-graph]]** | concept | 0.6 medium | 14 | [[agentic-memory|agentic-memory]], [[chunking|chunking]], [[darren-edge|darren-edge]], [[embeddings|embeddings]], [[graph-rag|graph-rag]], [[graphrag-edge-2024|graphrag-edge-2024]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[llm-wiki-pattern|llm-wiki-pattern]], [[microsoft-research|microsoft-research]], [[mkdocs|mkdocs]], [[obsidian|obsidian]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[vector-database|vector-database]], [[zettelkasten|zettelkasten]] |
| **[[agentic-memory]]** | concept | 0.55 medium | 13 | [[anthropic|anthropic]], [[asdlc-knowledge-base|asdlc-knowledge-base]], [[context-engineering|context-engineering]], [[embeddings|embeddings]], [[hallucination|hallucination]], [[knowledge-graph|knowledge-graph]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[llm-wiki-pattern|llm-wiki-pattern]], [[mcp-anthropic-2024|mcp-anthropic-2024]], [[model-context-protocol|model-context-protocol]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[self-rag-asai-2023|self-rag-asai-2023]], [[semantic-search|semantic-search]] |
| **[[asdlc-knowledge-base]]** | entity | 0.9 high | 13 | [[agentic-memory|agentic-memory]], [[andrej-karpathy|andrej-karpathy]], [[anthropic|anthropic]], [[asdlc-knowledge-readme|asdlc-knowledge-readme]], [[docling|docling]], [[hallucination|hallucination]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[llm-wiki-pattern|llm-wiki-pattern]], [[markitdown|markitdown]], [[mcp-anthropic-2024|mcp-anthropic-2024]], [[mkdocs|mkdocs]], [[model-context-protocol|model-context-protocol]], [[retrieval-augmented-generation|retrieval-augmented-generation]] |
| **[[context-engineering]]** | concept | 0.55 medium | 13 | [[agentic-memory|agentic-memory]], [[anthropic|anthropic]], [[chunking|chunking]], [[hallucination|hallucination]], [[hybrid-search|hybrid-search]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[llm-wiki-pattern|llm-wiki-pattern]], [[mcp-anthropic-2024|mcp-anthropic-2024]], [[model-context-protocol|model-context-protocol]], [[reranking|reranking]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[semantic-search|semantic-search]], [[zettelkasten|zettelkasten]] |
| **[[approximate-nearest-neighbor]]** | concept | 0.65 medium | 12 | [[dpr-karpukhin-2020|dpr-karpukhin-2020]], [[embeddings|embeddings]], [[faiss|faiss]], [[faiss-johnson-2017|faiss-johnson-2017]], [[hnsw-malkov-2016|hnsw-malkov-2016]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[meta-ai|meta-ai]], [[reranking|reranking]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[semantic-search|semantic-search]], [[vector-database|vector-database]], [[yury-malkov|yury-malkov]] |
| **[[hallucination]]** | concept | 0.6 medium | 11 | [[agentic-memory|agentic-memory]], [[akari-asai|akari-asai]], [[asdlc-knowledge-base|asdlc-knowledge-base]], [[context-engineering|context-engineering]], [[graph-rag|graph-rag]], [[hybrid-search|hybrid-search]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[reranking|reranking]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[self-rag-asai-2023|self-rag-asai-2023]], [[semantic-search|semantic-search]] |
| **[[chunking]]** | concept | 0.55 medium | 10 | [[context-engineering|context-engineering]], [[docling|docling]], [[embeddings|embeddings]], [[graph-rag|graph-rag]], [[knowledge-graph|knowledge-graph]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[llm-wiki-pattern|llm-wiki-pattern]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[semantic-search|semantic-search]], [[zettelkasten|zettelkasten]] |
| **[[graph-rag]]** | concept | 0.6 medium | 10 | [[chunking|chunking]], [[darren-edge|darren-edge]], [[graphrag-edge-2024|graphrag-edge-2024]], [[hallucination|hallucination]], [[knowledge-graph|knowledge-graph]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[microsoft-research|microsoft-research]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[self-rag-asai-2023|self-rag-asai-2023]], [[semantic-search|semantic-search]] |
| **[[faiss]]** | entity | 0.6 medium | 9 | [[approximate-nearest-neighbor|approximate-nearest-neighbor]], [[embeddings|embeddings]], [[faiss-johnson-2017|faiss-johnson-2017]], [[hnsw-malkov-2016|hnsw-malkov-2016]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[meta-ai|meta-ai]], [[semantic-search|semantic-search]], [[vector-database|vector-database]], [[yury-malkov|yury-malkov]] |
| **[[hybrid-search]]** | concept | 0.6 medium | 9 | [[context-engineering|context-engineering]], [[dpr-karpukhin-2020|dpr-karpukhin-2020]], [[embeddings|embeddings]], [[hallucination|hallucination]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[reranking|reranking]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[semantic-search|semantic-search]], [[vector-database|vector-database]] |
| **[[model-context-protocol]]** | concept | 0.65 medium | 9 | [[agentic-memory|agentic-memory]], [[anthropic|anthropic]], [[asdlc-knowledge-base|asdlc-knowledge-base]], [[context-engineering|context-engineering]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[llm-wiki-pattern|llm-wiki-pattern]], [[mcp-anthropic-2024|mcp-anthropic-2024]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[vector-database|vector-database]] |
| **[[dpr-karpukhin-2020]]** | source | 0.75 high | 8 | [[approximate-nearest-neighbor|approximate-nearest-neighbor]], [[embeddings|embeddings]], [[hybrid-search|hybrid-search]], [[meta-ai|meta-ai]], [[patrick-lewis|patrick-lewis]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[semantic-search|semantic-search]], [[vladimir-karpukhin|vladimir-karpukhin]] |
| **[[meta-ai]]** | entity | 0.6 medium | 8 | [[approximate-nearest-neighbor|approximate-nearest-neighbor]], [[dpr-karpukhin-2020|dpr-karpukhin-2020]], [[embeddings|embeddings]], [[faiss|faiss]], [[faiss-johnson-2017|faiss-johnson-2017]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[vector-database|vector-database]], [[vladimir-karpukhin|vladimir-karpukhin]] |
| **[[reranking]]** | concept | 0.6 medium | 8 | [[approximate-nearest-neighbor|approximate-nearest-neighbor]], [[context-engineering|context-engineering]], [[hallucination|hallucination]], [[hybrid-search|hybrid-search]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[semantic-search|semantic-search]], [[sentence-bert-2019|sentence-bert-2019]] |
| **[[faiss-johnson-2017]]** | source | 0.75 high | 7 | [[approximate-nearest-neighbor|approximate-nearest-neighbor]], [[embeddings|embeddings]], [[faiss|faiss]], [[hnsw-malkov-2016|hnsw-malkov-2016]], [[meta-ai|meta-ai]], [[semantic-search|semantic-search]], [[vector-database|vector-database]] |
| **[[hnsw-malkov-2016]]** | source | 0.75 high | 7 | [[approximate-nearest-neighbor|approximate-nearest-neighbor]], [[embeddings|embeddings]], [[faiss|faiss]], [[faiss-johnson-2017|faiss-johnson-2017]], [[semantic-search|semantic-search]], [[vector-database|vector-database]], [[yury-malkov|yury-malkov]] |
| **[[self-rag-asai-2023]]** | source | 0.75 high | 7 | [[agentic-memory|agentic-memory]], [[akari-asai|akari-asai]], [[graph-rag|graph-rag]], [[hallucination|hallucination]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[semantic-search|semantic-search]] |
| **[[anthropic]]** | entity | 0.65 medium | 6 | [[agentic-memory|agentic-memory]], [[asdlc-knowledge-base|asdlc-knowledge-base]], [[context-engineering|context-engineering]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[mcp-anthropic-2024|mcp-anthropic-2024]], [[model-context-protocol|model-context-protocol]] |
| **[[docling]]** | entity | 0.55 medium | 6 | [[asdlc-knowledge-base|asdlc-knowledge-base]], [[chunking|chunking]], [[embeddings|embeddings]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[llm-wiki-pattern|llm-wiki-pattern]], [[markitdown|markitdown]] |
| **[[microsoft-research]]** | entity | 0.6 medium | 6 | [[darren-edge|darren-edge]], [[graph-rag|graph-rag]], [[graphrag-edge-2024|graphrag-edge-2024]], [[knowledge-graph|knowledge-graph]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[retrieval-augmented-generation|retrieval-augmented-generation]] |
| **[[yury-malkov]]** | entity | 0.6 medium | 6 | [[approximate-nearest-neighbor|approximate-nearest-neighbor]], [[embeddings|embeddings]], [[faiss|faiss]], [[hnsw-malkov-2016|hnsw-malkov-2016]], [[semantic-search|semantic-search]], [[vector-database|vector-database]] |
| **[[zettelkasten]]** | concept | 0.55 medium | 6 | [[chunking|chunking]], [[context-engineering|context-engineering]], [[knowledge-graph|knowledge-graph]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[llm-wiki-pattern|llm-wiki-pattern]], [[obsidian|obsidian]] |
| **[[andrej-karpathy]]** | entity | 0.85 high | 5 | [[asdlc-knowledge-base|asdlc-knowledge-base]], [[asdlc-knowledge-readme|asdlc-knowledge-readme]], [[karpathy-llm-wiki|karpathy-llm-wiki]], [[llm-wiki-pattern|llm-wiki-pattern]], [[llm-wiki-setup-guide-2026|llm-wiki-setup-guide-2026]] |
| **[[asdlc-knowledge-readme]]** | source | 0.9 high | 5 | [[andrej-karpathy|andrej-karpathy]], [[asdlc-knowledge-base|asdlc-knowledge-base]], [[karpathy-llm-wiki|karpathy-llm-wiki]], [[llm-wiki-pattern|llm-wiki-pattern]], [[retrieval-augmented-generation|retrieval-augmented-generation]] |
| **[[darren-edge]]** | entity | 0.6 medium | 5 | [[graph-rag|graph-rag]], [[graphrag-edge-2024|graphrag-edge-2024]], [[knowledge-graph|knowledge-graph]], [[microsoft-research|microsoft-research]], [[retrieval-augmented-generation|retrieval-augmented-generation]] |
| **[[graphrag-edge-2024]]** | source | 0.75 high | 5 | [[darren-edge|darren-edge]], [[graph-rag|graph-rag]], [[knowledge-graph|knowledge-graph]], [[microsoft-research|microsoft-research]], [[retrieval-augmented-generation|retrieval-augmented-generation]] |
| **[[llm-wiki-setup-guide-2026]]** | source | 0.5 medium | 5 | [[andrej-karpathy|andrej-karpathy]], [[llm-wiki-pattern|llm-wiki-pattern]], [[markitdown|markitdown]], [[obsidian|obsidian]], [[retrieval-augmented-generation|retrieval-augmented-generation]] |
| **[[markitdown]]** | entity | 0.55 medium | 5 | [[asdlc-knowledge-base|asdlc-knowledge-base]], [[docling|docling]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[llm-wiki-pattern|llm-wiki-pattern]], [[llm-wiki-setup-guide-2026|llm-wiki-setup-guide-2026]] |
| **[[mcp-anthropic-2024]]** | source | 0.75 high | 5 | [[agentic-memory|agentic-memory]], [[anthropic|anthropic]], [[asdlc-knowledge-base|asdlc-knowledge-base]], [[context-engineering|context-engineering]], [[model-context-protocol|model-context-protocol]] |
| **[[obsidian]]** | entity | 0.55 medium | 5 | [[knowledge-graph|knowledge-graph]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[llm-wiki-pattern|llm-wiki-pattern]], [[llm-wiki-setup-guide-2026|llm-wiki-setup-guide-2026]], [[zettelkasten|zettelkasten]] |
| **[[sentence-bert-2019]]** | source | 0.75 high | 5 | [[embeddings|embeddings]], [[nils-reimers|nils-reimers]], [[reranking|reranking]], [[semantic-search|semantic-search]], [[vector-database|vector-database]] |
| **[[vladimir-karpukhin]]** | entity | 0.6 medium | 5 | [[dpr-karpukhin-2020|dpr-karpukhin-2020]], [[embeddings|embeddings]], [[meta-ai|meta-ai]], [[patrick-lewis|patrick-lewis]], [[retrieval-augmented-generation|retrieval-augmented-generation]] |
| **[[mkdocs]]** | entity | 0.55 medium | 4 | [[asdlc-knowledge-base|asdlc-knowledge-base]], [[knowledge-graph|knowledge-graph]], [[knowledge-management-for-llms|knowledge-management-for-llms]], [[llm-wiki-pattern|llm-wiki-pattern]] |
| **[[nils-reimers]]** | entity | 0.6 medium | 4 | [[embeddings|embeddings]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[semantic-search|semantic-search]], [[sentence-bert-2019|sentence-bert-2019]] |
| **[[patrick-lewis]]** | entity | 0.7 medium | 4 | [[dpr-karpukhin-2020|dpr-karpukhin-2020]], [[rag-lewis-2020|rag-lewis-2020]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[vladimir-karpukhin|vladimir-karpukhin]] |
| **[[akari-asai]]** | entity | 0.6 medium | 3 | [[hallucination|hallucination]], [[retrieval-augmented-generation|retrieval-augmented-generation]], [[self-rag-asai-2023|self-rag-asai-2023]] |
| **[[karpathy-llm-wiki]]** | source | 0.9 high | 3 | [[andrej-karpathy|andrej-karpathy]], [[asdlc-knowledge-readme|asdlc-knowledge-readme]], [[llm-wiki-pattern|llm-wiki-pattern]] |
| **[[rag-lewis-2020]]** | source | 0.85 high | 3 | [[llm-wiki-pattern|llm-wiki-pattern]], [[patrick-lewis|patrick-lewis]], [[retrieval-augmented-generation|retrieval-augmented-generation]] |
