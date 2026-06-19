---
title: 'ProofWright: Towards Agentic Formal Verification of CUDA'
authors:
  - name: Bodhisatwa Chatterjee
  - name: Drew Zagieboylo
  - name: Sana Damani
  - name: Siva Hari
  - key: christoskozyrakis
venue: preprint
year: 2025
date: 2025-11-15
doi: 10.48550/arXiv.2511.12294
thumbnail: False
materials:
tags:
  - compilers
  - AI-systems
  - parallel-compute
  - accelerators
  - gpu-systems
---
Large Language Models (LLMs) are increasingly used to automatically generate optimized CUDA kernels, substantially improving developer productivity. However, despite rapid generation, these kernels often contain subtle correctness bugs and lack formal safety guarantees. Runtime testing is inherently unreliable - limited input coverage and reward hacking can mask incorrect behavior - while manual formal verification is reliable but cannot scale to match LLM output rates, creating a critical validation bottleneck. We present ProofWright, an agentic verification framework that bridges this gap by integrating automated formal verification with LLM-based code generation. ProofWright provides end-to-end guarantees of memory safety, thread safety, and semantic correctness for LLM-generated CUDA kernels. On KernelBench L1, ProofWright verifies safety properties for 74% of generated kernels, uncovers subtle correctness errors missed by conventional testing, and establishes semantic equivalence for a class of element-wise kernels. With a modest overhead of 3 minutes per kernel, ProofWright demonstrates that scalable, automated formal verification of LLM-generated GPU code is feasible - offering a path toward trustworthy high-performance code generation without sacrificing developer productivity.
