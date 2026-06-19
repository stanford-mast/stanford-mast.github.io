---
title: 'SOL-ExecBench: Speed-of-Light Benchmarking for Real-World GPU Kernels Against Hardware Limits'
authors:
  - name: Edward Lin
  - name: Sahil Modi
  - name: Siva Kumar Sastry Hari
  - name: Qijing Huang
  - name: Zhifan Ye
  - name: Nestor Qin
  - name: Fengzhe Zhou
  - name: Yuan Zhang
  - name: Jingquan Wang
  - name: Sana Damani
  - name: Dheeraj Peri
  - name: Ouye Xie
  - name: Aditya Kane
  - name: Moshe Maor
  - name: Michael Behar
  - name: Triston Cao
  - name: Rishabh Mehta
  - name: Vartika Singh
  - name: Vikram Sharma Mailthody
  - name: Terry Chen
  - name: Zihao Ye
  - name: Hanfeng Chen
  - name: Tianqi Chen
  - name: Vinod Grover
  - name: Wei Chen
  - name: Wei Liu
  - name: Eric Chung
  - name: Luis Ceze
  - name: Roger Bringmann
  - name: Cyril Zeller
  - name: Michael Lightstone
  - key: christoskozyrakis
  - name: Humphrey Shi
venue: preprint
year: 2026
date: 2026-03-19
doi: 10.48550/arXiv.2603.19173
thumbnail: False
materials:
tags:
  - architecture
  - OS
  - AI-systems
  - parallel-compute
  - accelerators
  - gpu-systems
---
As agentic AI systems become increasingly capable of generating and optimizing GPU kernels, progress is constrained by benchmarks that reward speedup over software baselines rather than proximity to hardware-efficient execution. We present SOL-ExecBench, a benchmark of 235 CUDA kernel optimization problems extracted from 124 production and emerging AI models spanning language, diffusion, vision, audio, video, and hybrid architectures, targeting NVIDIA Blackwell GPUs. The benchmark covers forward and backward workloads across BF16, FP8, and NVFP4, including kernels whose best performance is expected to rely on Blackwell-specific capabilities. Unlike prior benchmarks that evaluate kernels primarily relative to software implementations, SOL-ExecBench measures performance against analytically derived Speed-of-Light (SOL) bounds computed by SOLAR, our pipeline for deriving hardware-grounded SOL bounds, yielding a fixed target for hardware-efficient optimization. We report a SOL Score that quantifies how much of the gap between a release-defined scoring baseline and the hardware SOL bound a candidate kernel closes. To support robust evaluation of agentic optimizers, we additionally provide a sandboxed harness with GPU clock locking, L2 cache clearing, isolated subprocess execution, and static analysis based checks against common reward-hacking strategies. SOL-ExecBench reframes GPU kernel benchmarking from beating a mutable software baseline to closing the remaining gap to hardware Speed-of-Light.
