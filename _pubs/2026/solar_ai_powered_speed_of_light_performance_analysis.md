---
title: 'SOLAR: AI-Powered Speed-of-Light Performance Analysis'
authors:
  - name: Qijing Huang
  - name: Sana Damani
  - name: Zhifan Ye
  - key: athinagorasskiadopoulos
  - name: Siva Kumar Sastry Hari
  - name: Jason Clemons
  - name: Sahil Modi
  - name: Jingquan Wang
  - name: Aditya Kane
  - name: Edward C Lin
  - name: Humphrey Shi
  - key: christoskozyrakis
venue: preprint
year: 2026
date: 2026-06-24
doi: 10.48550/arXiv.2606.26383
thumbnail: True
materials:
  - name: paper
    url: /pubs/solar_ai_powered_speed_of_light_performance_analysis/paper.pdf
    type: file-pdf
  - name: arXiv
    url: https://doi.org/10.48550/arXiv.2606.26383
    type: file-alt
tags:
  - architecture
  - compilers
  - AI-systems
  - accelerators
  - gpu-systems
---
How fast could a deep-learning model run on target hardware, and how far is today's implementation from that limit? These questions are central to software, hardware, and algorithm optimizations. Speed-of-Light (SOL) analysis answers them by computing a workload's theoretical minimum execution time on a given architecture. Yet deriving SOL bounds remains manual, error-prone, and disconnected from rapid model development. To close this gap, we introduce SOLAR, a framework that automatically derives validated SOL bounds from PyTorch and JAX source code. SOLAR leverages both generative and deterministic components in its flow: an LLM frontend translates any source programs into an executable Affine Loop IR, validated by output comparison; a deterministic flow lifts the IR into an einsum graph; and an analytical backend computes unfused, fused, and cache-aware SOL bounds. SOLAR provides comprehensive operator and language coverage, produces validated bounds with zero observed SOL violations, and offers multi-fidelity analysis that tightens bounds and surfaces optimization insights. We evaluate SOLAR across KernelBench, JAX/Flax models, and robotics workloads. These experiments demonstrate four use cases: headroom analysis at multiple fidelity levels, identifying optimization opportunities, cross-platform exploration, and inverse-roofline hardware provisioning.
