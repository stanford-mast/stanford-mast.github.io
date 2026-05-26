---
title: 'RaidServe: High-performance Resilient Serving'
authors:
  - name: Ziyi Xu
  - key: zhiqiangxie
  - key: swapnilgandhi
  - key: christoskozyrakis
venue: mlsys
year: 2026
date: 2026-05-18
doi: 10.48550/arXiv.2511.14116
thumbnail: True
materials:
tags:
---
Tensor parallelism (TP) enables large language models (LLMs) to scale inference efficiently across multiple GPUs, but its tight coupling makes systems fragile: a single GPU failure can halt execution, trigger costly KVCache recomputation, and introduce long-term compute and memory imbalance. We present RaidServe , a fault-tolerant TP serving system that sustains high performance under irregular GPU availability. RaidServe introduces three techniques to balance computation and memory across GPUs: (1) Cyclic KVCache Placement for even memory utilization, (2) Hybrid Attention combining tensor- and data-parallel attention to eliminate stragglers, and (3) Fine-Grained Load-Aware Routing to dynamically balance requests. It further employs proactive KVCache backup and on-demand weight recovery to avoid expensive recomputation and redundant data transfers. Implemented in a lightweight serving engine compatible with existing infrastructures, RaidServe achieves up to 2× higher throughput and two orders of magnitude faster recovery than standard fault-handling methods on an 8×H100 DGX system, maintaining strong performance even with multiple GPU failures.