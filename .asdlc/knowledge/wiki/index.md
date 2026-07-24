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
<script id="kb-graph-data" type="application/json">{"nodes":[{"id":"llm-wiki-pattern","name":"LLM Wiki Pattern","type":"concept","conf":0.8,"band":"high","color":"#2f9e44","val":7,"href":"concepts/llm-wiki-pattern/"},{"id":"retrieval-augmented-generation","name":"Retrieval-Augmented Generation (RAG)","type":"concept","conf":0.8,"band":"high","color":"#2f9e44","val":6,"href":"concepts/retrieval-augmented-generation/"},{"id":"andrej-karpathy","name":"Andrej Karpathy","type":"entity","conf":0.85,"band":"high","color":"#2f9e44","val":5,"href":"entities/andrej-karpathy/"},{"id":"asdlc-knowledge-base","name":"ASDLC Knowledge Base","type":"entity","conf":0.9,"band":"high","color":"#2f9e44","val":4,"href":"entities/asdlc-knowledge-base/"},{"id":"patrick-lewis","name":"Patrick Lewis","type":"entity","conf":0.7,"band":"medium","color":"#f08c00","val":2,"href":"entities/patrick-lewis/"},{"id":"asdlc-knowledge-readme","name":"ASDLC Knowledge Base \u2014 README","type":"source","conf":0.9,"band":"high","color":"#2f9e44","val":5,"href":"sources/asdlc-knowledge-readme/"},{"id":"karpathy-llm-wiki","name":"Karpathy \u2014 LLM Wiki gist","type":"source","conf":0.9,"band":"high","color":"#2f9e44","val":3,"href":"sources/karpathy-llm-wiki/"},{"id":"llm-wiki-setup-guide-2026","name":"LLM Wiki Setup: Karpathy's Knowledge Base (2026 Guide)","type":"source","conf":0.5,"band":"medium","color":"#f08c00","val":3,"href":"sources/llm-wiki-setup-guide-2026/"},{"id":"rag-lewis-2020","name":"Lewis et al. \u2014 Retrieval-Augmented Generation (2020)","type":"source","conf":0.85,"band":"high","color":"#2f9e44","val":3,"href":"sources/rag-lewis-2020/"}],"links":[{"source":"llm-wiki-pattern","target":"retrieval-augmented-generation"},{"source":"llm-wiki-pattern","target":"karpathy-llm-wiki"},{"source":"llm-wiki-pattern","target":"andrej-karpathy"},{"source":"llm-wiki-pattern","target":"asdlc-knowledge-base"},{"source":"llm-wiki-pattern","target":"llm-wiki-setup-guide-2026"},{"source":"retrieval-augmented-generation","target":"rag-lewis-2020"},{"source":"retrieval-augmented-generation","target":"llm-wiki-setup-guide-2026"},{"source":"andrej-karpathy","target":"karpathy-llm-wiki"},{"source":"andrej-karpathy","target":"llm-wiki-setup-guide-2026"},{"source":"asdlc-knowledge-base","target":"asdlc-knowledge-readme"},{"source":"asdlc-knowledge-base","target":"andrej-karpathy"},{"source":"asdlc-knowledge-base","target":"retrieval-augmented-generation"},{"source":"patrick-lewis","target":"rag-lewis-2020"},{"source":"patrick-lewis","target":"retrieval-augmented-generation"},{"source":"asdlc-knowledge-readme","target":"llm-wiki-pattern"},{"source":"asdlc-knowledge-readme","target":"retrieval-augmented-generation"},{"source":"asdlc-knowledge-readme","target":"andrej-karpathy"},{"source":"asdlc-knowledge-readme","target":"karpathy-llm-wiki"},{"source":"rag-lewis-2020","target":"llm-wiki-pattern"}]}</script>
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
  llm_wiki_pattern["LLM Wiki Pattern<br/>0.8 · high"]
  style llm_wiki_pattern fill:#2f9e4422,stroke:#2f9e44
  click llm_wiki_pattern "concepts/llm-wiki-pattern/" "Open page" _self
  retrieval_augmented_generation["Retrieval-Augmented Generation (RAG)<br/>0.8 · high"]
  style retrieval_augmented_generation fill:#2f9e4422,stroke:#2f9e44
  click retrieval_augmented_generation "concepts/retrieval-augmented-generation/" "Open page" _self
  andrej_karpathy["Andrej Karpathy<br/>0.85 · high"]
  style andrej_karpathy fill:#2f9e4422,stroke:#2f9e44
  click andrej_karpathy "entities/andrej-karpathy/" "Open page" _self
  asdlc_knowledge_base["ASDLC Knowledge Base<br/>0.9 · high"]
  style asdlc_knowledge_base fill:#2f9e4422,stroke:#2f9e44
  click asdlc_knowledge_base "entities/asdlc-knowledge-base/" "Open page" _self
  patrick_lewis["Patrick Lewis<br/>0.7 · medium"]
  style patrick_lewis fill:#f08c0022,stroke:#f08c00
  click patrick_lewis "entities/patrick-lewis/" "Open page" _self
  asdlc_knowledge_readme["ASDLC Knowledge Base — README<br/>0.9 · high"]
  style asdlc_knowledge_readme fill:#2f9e4422,stroke:#2f9e44
  click asdlc_knowledge_readme "sources/asdlc-knowledge-readme/" "Open page" _self
  karpathy_llm_wiki["Karpathy — LLM Wiki gist<br/>0.9 · high"]
  style karpathy_llm_wiki fill:#2f9e4422,stroke:#2f9e44
  click karpathy_llm_wiki "sources/karpathy-llm-wiki/" "Open page" _self
  llm_wiki_setup_guide_2026["LLM Wiki Setup: Karpathy's Knowledge Base (2026 Guide)<br/>0.5 · medium"]
  style llm_wiki_setup_guide_2026 fill:#f08c0022,stroke:#f08c00
  click llm_wiki_setup_guide_2026 "sources/llm-wiki-setup-guide-2026/" "Open page" _self
  rag_lewis_2020["Lewis et al. — Retrieval-Augmented Generation (2020)<br/>0.85 · high"]
  style rag_lewis_2020 fill:#2f9e4422,stroke:#2f9e44
  click rag_lewis_2020 "sources/rag-lewis-2020/" "Open page" _self
  llm_wiki_pattern --> retrieval_augmented_generation
  llm_wiki_pattern --> karpathy_llm_wiki
  llm_wiki_pattern --> andrej_karpathy
  llm_wiki_pattern --> asdlc_knowledge_base
  llm_wiki_pattern --> llm_wiki_setup_guide_2026
  retrieval_augmented_generation --> rag_lewis_2020
  retrieval_augmented_generation --> llm_wiki_pattern
  retrieval_augmented_generation --> llm_wiki_setup_guide_2026
  andrej_karpathy --> llm_wiki_pattern
  andrej_karpathy --> karpathy_llm_wiki
  andrej_karpathy --> llm_wiki_setup_guide_2026
  asdlc_knowledge_base --> llm_wiki_pattern
  asdlc_knowledge_base --> asdlc_knowledge_readme
  asdlc_knowledge_base --> andrej_karpathy
  asdlc_knowledge_base --> retrieval_augmented_generation
  patrick_lewis --> rag_lewis_2020
  patrick_lewis --> retrieval_augmented_generation
  asdlc_knowledge_readme --> asdlc_knowledge_base
  asdlc_knowledge_readme --> llm_wiki_pattern
  asdlc_knowledge_readme --> retrieval_augmented_generation
  asdlc_knowledge_readme --> andrej_karpathy
  asdlc_knowledge_readme --> karpathy_llm_wiki
  karpathy_llm_wiki --> andrej_karpathy
  karpathy_llm_wiki --> llm_wiki_pattern
  llm_wiki_setup_guide_2026 --> llm_wiki_pattern
  llm_wiki_setup_guide_2026 --> andrej_karpathy
  llm_wiki_setup_guide_2026 --> retrieval_augmented_generation
  rag_lewis_2020 --> retrieval_augmented_generation
  rag_lewis_2020 --> patrick_lewis
  rag_lewis_2020 --> llm_wiki_pattern
```

## Connections

| Page | Type | Confidence | 🔗 | Connects to |
| --- | --- | --- | --- | --- |
| **[[llm-wiki-pattern]]** | concept | 0.8 high | 7 | [[andrej-karpathy|andrej-karpathy]], [[asdlc-knowledge-base|asdlc-knowledge-base]], [[asdlc-knowledge-readme|asdlc-knowledge-readme]], [[karpathy-llm-wiki|karpathy-llm-wiki]], [[llm-wiki-setup-guide-2026|llm-wiki-setup-guide-2026]], [[rag-lewis-2020|rag-lewis-2020]], [[retrieval-augmented-generation|retrieval-augmented-generation]] |
| **[[retrieval-augmented-generation]]** | concept | 0.8 high | 6 | [[asdlc-knowledge-base|asdlc-knowledge-base]], [[asdlc-knowledge-readme|asdlc-knowledge-readme]], [[llm-wiki-pattern|llm-wiki-pattern]], [[llm-wiki-setup-guide-2026|llm-wiki-setup-guide-2026]], [[patrick-lewis|patrick-lewis]], [[rag-lewis-2020|rag-lewis-2020]] |
| **[[andrej-karpathy]]** | entity | 0.85 high | 5 | [[asdlc-knowledge-base|asdlc-knowledge-base]], [[asdlc-knowledge-readme|asdlc-knowledge-readme]], [[karpathy-llm-wiki|karpathy-llm-wiki]], [[llm-wiki-pattern|llm-wiki-pattern]], [[llm-wiki-setup-guide-2026|llm-wiki-setup-guide-2026]] |
| **[[asdlc-knowledge-readme]]** | source | 0.9 high | 5 | [[andrej-karpathy|andrej-karpathy]], [[asdlc-knowledge-base|asdlc-knowledge-base]], [[karpathy-llm-wiki|karpathy-llm-wiki]], [[llm-wiki-pattern|llm-wiki-pattern]], [[retrieval-augmented-generation|retrieval-augmented-generation]] |
| **[[asdlc-knowledge-base]]** | entity | 0.9 high | 4 | [[andrej-karpathy|andrej-karpathy]], [[asdlc-knowledge-readme|asdlc-knowledge-readme]], [[llm-wiki-pattern|llm-wiki-pattern]], [[retrieval-augmented-generation|retrieval-augmented-generation]] |
| **[[karpathy-llm-wiki]]** | source | 0.9 high | 3 | [[andrej-karpathy|andrej-karpathy]], [[asdlc-knowledge-readme|asdlc-knowledge-readme]], [[llm-wiki-pattern|llm-wiki-pattern]] |
| **[[llm-wiki-setup-guide-2026]]** | source | 0.5 medium | 3 | [[andrej-karpathy|andrej-karpathy]], [[llm-wiki-pattern|llm-wiki-pattern]], [[retrieval-augmented-generation|retrieval-augmented-generation]] |
| **[[rag-lewis-2020]]** | source | 0.85 high | 3 | [[llm-wiki-pattern|llm-wiki-pattern]], [[patrick-lewis|patrick-lewis]], [[retrieval-augmented-generation|retrieval-augmented-generation]] |
| **[[patrick-lewis]]** | entity | 0.7 medium | 2 | [[rag-lewis-2020|rag-lewis-2020]], [[retrieval-augmented-generation|retrieval-augmented-generation]] |
