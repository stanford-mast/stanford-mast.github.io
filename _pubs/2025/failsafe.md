---
title: 'FailSafe: High-performance Resilient Serving'
authors:
  - name: Ziyi Xu
  - key: zhiqiangxie
  - key: swapnilgandhi
  - key: christoskozyrakis
venue: preprint
year: 2025
date: 2025-11-18
doi: 10.48550/arXiv.2511.14116
thumbnail: True
materials:
tags:
---
Tensor parallelism (TP) enables large language models (LLMs) to scale inference efficiently across multiple GPUs, but its tight coupling makes systems fragile: a single GPU failure can halt execution, trigger costly KVCache recomputation, and introduce long-term compute and memory imbalance. We present FailSafe, a fault-tolerant TP serving system that sustains high performance under irregular GPU availability. FailSafe introduces three techniques to balance computation and memory across GPUs: (1) Cyclic KVCache Placement for uniform memory utilization, (2) Hybrid Attention combining tensor- and data-parallel attention to eliminate stragglers, and (3) Fine-Grained Load-Aware Routing to dynamically balance requests. It further employs proactive KVCache backup and on-demand weight recovery to avoid expensive recomputation and redundant data transfers. We implement these techniques in a lightweight serving engine compatible with existing LLM infrastructures. Evaluated on an 8xH100 DGX system with real-world fault traces and representative workloads, FailSafe achieves up to 2x higher throughput and two orders of magnitude lower recovery latency compared to standard fault handling approaches. Even with up to three GPU failures, FailSafe sustains high throughput and balanced utilization, demonstrating robust and efficient LLM serving under dynamic and unreliable hardware conditions.
