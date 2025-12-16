---
title: 'Strata: Hierarchical Context Caching for Long Context Language Model Serving'
authors:
  - key: zhiqiangxie
  - name: Ziyi Xu
  - key: markzhao
  - name: Yuwei An
  - name: Vikram Mailthody
  - name: Scott Mahlke
  - name: Michael Garland
  - key: christoskozyrakis
venue: preprint
year: 2025
date: 2025-08-01
doi: 10.48550/arXiv.2508.18572
thumbnail: True
materials:
tags:
---
Large Language Models (LLMs) with expanding context windows face significant performance hurdles. While caching key-value (KV) states is critical for avoiding redundant computation, the storage footprint of long-context caches quickly exceeds GPU memory capacity, forcing production systems to adopt hierarchical caching across memory hierarchies. However, transferring large cached contexts back to the GPU introduces severe performance bottlenecks: fragmented I/O from paged layouts prevents full bandwidth utilization, and existing schedulers fail to account for cache-loading delays, leaving systems loading-bound rather than compute-bound. We present Strata, a hierarchical context caching framework designed for efficient long context LLM serving. Strata introduces GPU-assisted I/O to combat KV cache fragmentation, decoupling GPU and CPU memory layouts and employs cache-aware request scheduling to balance compute with I/O latency and overlapping unavoidable stalls with complementary tasks. Built on SGLang and deployed in production, Strata achieves up to 5x lower Time-To-First-Token (TTFT) compared to vLLM + LMCache and 3.75x speedup over NVIDIA TensorRT-LLM on long-context benchmarks, without degrading short-context performance.
