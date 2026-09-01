---
title: 'HiSparse: Scaling Sparse-Attention Decoding with Hierarchical KV Cache Management'
authors:
  - key: zhiqiangxie
  - name: Zhangheng Huang
  - name: Tingwei Huang
  - name: Ziyi Xu
  - name: Ruiyang Ma
  - key: christoskozyrakis
venue: preprint
year: 2026
date: 2026-08-07
doi: 10.48550/arXiv.2608.07009
thumbnail: True
materials:
  - name: paper
    url: /pubs/hisparse_scaling_sparse_attention_decoding_with_hierarchical_kv_cache_management/paper.pdf
    type: file-pdf
  - name: arXiv
    url: https://doi.org/10.48550/arXiv.2608.07009
    type: file-alt
tags:
  - AI-systems
  - memory-storage
  - datacenter-systems
  - resource-management
  - low-latency
  - gpu-systems
---
Top-k sparse attention makes long-context LLM decoding cheap to compute: each step reads only a few thousand selected KV entries rather than the full context. Serving systems, however, typically keep the entire KV cache in GPU HBM so that every position stays selectable, so a request's memory bill still grows with its full context length--decoding hits a capacity wall long before it runs out of compute, and a context whose KV cache exceeds HBM cannot be served at all. We present HiSparse, an exact, indexer-agnostic hierarchical KV cache for sparse-attention serving. HiSparse keeps each request's full KV history in host memory and bounds its decode footprint with a small, fixed-size GPU cache; a fused CUDA kernel resolves each layer's selections--hit detection, LRU replacement, and host-to-device fetches--inside the decode CUDA graph; and, for models that share selections across layers, exact layer-wise prefetching hides roughly half of the remaining miss overhead. Because only KV placement changes, model outputs are unchanged. HiSparse is merged into upstream SGLang and evaluated across three sparse-attention families (DSA, NSA, and Quest) on H200, B200, and GH200 platforms: it improves peak generation throughput by up to 4.7x on long-context workloads while preserving comparable per-token latency and reducing time-to-first-token at high load--and a no-IO oracle shows the resolution mechanism itself adds no measurable per-token cost, leaving host-device IO as the only price of bounded residency.
