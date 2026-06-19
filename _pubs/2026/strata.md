---
title: 'Contextra: Hierarchical Context Caching for Long Context Language Model Serving'
authors:
  - key: zhiqiangxie
  - name: Ziyi Xu
  - key: markzhao
  - name: Yuwei An
  - name: Vikram Sharma Mailthody
  - name: Scott Mahlke
  - name: Michael Garland
  - key: christoskozyrakis
venue: osdi
year: 2026
date: 2026-07-13
doi:
thumbnail: True
materials:
  - name: PDF
    url: https://www.usenix.org/conference/osdi26/presentation/xie-zhiqiang
    type: file-pdf
tags:
  - OS
  - AI-systems
  - memory-storage
  - resource-management
  - low-latency
  - accelerators
  - gpu-systems
---
Large Language Models (LLMs) with expanding context windows face significant performance hurdles. While caching key-value (KV) states is critical for avoiding redundant computation, the storage footprint of long-context caches quickly exceeds GPU memory capacity, forcing production systems to adopt hierarchical caching across memory hierarchies. However, transferring large cached contexts back to the GPU introduces severe performance bottlenecks: fragmented I/O from paged layouts prevents full bandwidth utilization, and existing schedulers fail to account for cache-loading delays, leaving systems loading-bound rather than compute-bound. We present Contextra, a hierarchical context caching framework designed for efficient long context LLM serving. Contextra introduces GPU-assisted I/O to combat KV cache fragmentation, decoupling GPU and CPU memory layouts and employs cache-aware request scheduling to balance compute with I/O latency and overlapping unavoidable stalls with complementary tasks. Built on SGLang and deployed in production, Contextra achieves up to 5x lower Time-To-First-Token (TTFT) compared to vLLM + LMCache and 3.75x speedup over NVIDIA TensorRT-LLM on long-context benchmarks, without degrading short-context performance.
