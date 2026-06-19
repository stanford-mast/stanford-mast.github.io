---
title: 'LIMINAL: Exploring The Frontiers of LLM Decode Performance'
authors:
  - name: Michael Davies
  - name: Neal Crago
  - name: Karthikeyan Sankaralingam
  - key: christoskozyrakis
venue: preprint
year: 2025
date: 2025-07-18
doi: 10.48550/arXiv.2507.14397
thumbnail: False
materials:
tags:
  - AI-systems
  - accelerators
  - gpu-systems
---
The rapid advancement of Large Language Models (LLMs) necessitates a deep understanding of their fundamental performance limits. This paper investigates the limits of LLM inference, focusing on hardware-imposed bottlenecks in auto-regressive decoding. We develop LIMINAL, an analytical performance model that abstracts application requirements and hardware capabilities to systematically explore performance and efficiency across a wide range of current, near-future, and hypothetical hardware. We find LIMINAL is accurate when comparing to LLMs executing on existing hardware, achieving a mean absolute error of $7.6\%$. Our analysis spans from current HBM3 memory technology used in AI accelerators like GPUs and TPUs to systems based on advanced HBM4 and advanced 3D-stacked DRAM technology. We identify five non-negotiable challenges for LLM inference hardware, establishing compute, memory capacity, bandwidth and collective communication as primary barriers to performance. These findings suggest that achieving significant performance gains beyond 10,000 tokens-per-second will require not just hardware evolution but also fundamental algorithmic advances.
