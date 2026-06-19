---
title: 'ARGUS: Agentic GPU Optimization Guided by Data-Flow Invariants'
authors:
  - name: Haohui Mai
  - name: Xiaoyan Guo
  - name: Xiangyun Ding
  - name: Daifeng Li
  - name: Qiuchu Yu
  - name: Chenzhun Guo
  - name: Cong Wang
  - name: Jiacheng Zhao
  - key: christoskozyrakis
  - name: Binhang Yuan
venue: preprint
year: 2026
date: 2026-04-16
doi: 10.48550/arXiv.2604.18616
thumbnail: False
materials:
tags:
  - AI-systems
  - parallel-compute
  - resource-management
  - accelerators
  - gpu-systems
---
LLM-based coding agents can generate functionally correct GPU kernels, yet their performance remains far below hand-optimized libraries on critical computations such as matrix multiplication, attention, and Mixture-of-Experts (MoE). Peak GPU performance requires coordinated reasoning over tightly coupled optimizations, including tiling, shared-memory staging, software pipelining, and instruction scheduling, while existing agents rely on sparse pass/fail feedback, leaving them unable to diagnose global constraint violations. We present Argus, an agentic framework that addresses this through data-flow invariants: compile-time specifications encoding how data must be choreographed throughout kernel execution. Argus introduces a tile-based, Pythonic DSL exposing hardware instructions and compiler policies while hiding low-level representations. The DSL provides tag functions to propagate symbolic annotations through data and control flow, and tag assertions to enforce relational constraints at use sites. When violations occur, the compiler returns concrete counterexamples identifying the thread, data element, and program point, enabling dense, structured feedback for targeted fixes. Invariants are verified at compile time via abstract interpretation over a layout algebra and SMT solving, with zero runtime overhead. An in-context reinforcement learning planner learns to select optimizations and synthesize effective invariants, supported by a curated knowledge base of GPU optimization techniques. We evaluate Argus on the AMD MI300X GPU across GEMM, flash attention, and MoE kernels accounting for over 90% of GPU time in LLM inference. Generated kernels achieve 99-104% of state-of-the-art hand-optimized assembly throughput and are 2-1543x faster than existing agentic systems. Argus further generalizes to 200 KernelBench tasks, solving 100% of Level 1 and 90% of Level 2 problems.
