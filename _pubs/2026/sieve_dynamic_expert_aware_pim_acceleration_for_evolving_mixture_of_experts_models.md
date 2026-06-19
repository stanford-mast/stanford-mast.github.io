---
title: 'Sieve: Dynamic Expert-Aware PIM Acceleration for Evolving Mixture-of-Experts Models'
authors:
  - name: Jungwoo Kim
  - name: Rubens Lacouture
  - name: Genghan Zhang
  - name: Gina Sohn
  - name: Qizheng Zhang
  - key: swapnilgandhi
  - key: christoskozyrakis
  - name: Kunle Olukotun
venue: preprint
year: 2026
date: 2026-05-11
doi: 10.48550/arXiv.2605.11277
thumbnail: False
materials:
tags:
  - architecture
  - AI-systems
  - memory-storage
  - resource-management
  - near-data-processing
  - accelerators
  - gpu-systems
---
Mixture-of-Experts (MoE) has become a dominant architecture for scaling large language models (LLMs). However, the execution characteristics of MoE inference are changing rapidly and increasingly mismatch the assumptions underlying existing Processing-in-Memory (PIM) systems. Prior PIM systems for LLMs rely on static rules to offload memory-bound operations to PIM, without accounting for the combined effects of load imbalance and inter-GPU communication. Meanwhile, modern MoE models activate fewer experts out of increasingly many, creating a bimodal expert distribution: a small set of experts receives many tokens, while a long tail of experts receives only one or a few. We identify a trend in modern MoE models toward increasingly bimodal token-to-expert distributions, quantify the resulting disparity in arithmetic intensity across experts, and show that this disparity dramatically reduces the efficiency of state-of-the-art PIM systems for LLMs. To address this problem, we propose a scheduler for serving MoE models on multi-GPU systems with attached HBM-PIM stacks. Our scheduler partitions expert execution between GPU and PIM based on runtime token-to-expert distributions, while jointly considering interconnect overhead, memory bandwidth, GPU throughput, and PIM throughput. Moreover, we propose Sieve, a runtime framework that employs the scheduler to coordinate execution across GPUs and their attached HBM-PIM stacks. Sieve overlaps GPU computation, PIM computation, and intra- and inter-device communication while preserving cross-device dependencies induced by expert parallelism. Sieve is evaluated on our cycle-accurate simulator based on Ramulator 2.0. Compared to state-of-the-art PIM systems for MoE, Sieve improves both throughput and interactivity by 1.3x, 1.3x, and 1.6x on Qwen3.5-397B-A17B, GPT-OSS-120B, and Qwen3-30B-A3B, respectively.
