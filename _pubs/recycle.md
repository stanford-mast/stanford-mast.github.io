---
title: 'ReCycle: Resilient Training of Large DNNs using Pipeline Adaptation'
authors:
  - key: swapnilgandhi
  - key: markzhao
  - key: athinagorasskiadopoulos
  - key: christoskozyrakis
venue: sosp
year: 2024
date: 2024-11-04
doi: 10.1145/3694715.3695960
materials:
  - name: PDF
    url: https://arxiv.org/pdf/2405.14009
    type: file-pdf
  - name: Slides
    url: https://swapnilgandhi.com/slides/recycle-sosp24.pdf
    type: file
tags:
  - distributed pre-training
  - fault-tolerance
---
Training large Deep Neural Network (DNN) models requires thousands of GPUs over the course of several days or weeks. At this scale, failures are frequent and can have a big impact on training throughput. Utilizing spare GPU servers to mitigate performance loss becomes increasingly costly as model sizes grow. ReCycle is a system designed for efficient DNN training in the presence of failures, without relying on spare servers. It exploits the inherent functional redundancy in distributed training systems - where servers across data-parallel groups store the same model parameters - and pipeline schedule bubbles within each data-parallel group. When servers fails, ReCycle dynamically re-routes microbatches to data-parallel peers, allowing for uninterrupted training despite multiple failures. However, this re-routing can create imbalances across pipeline stages, leading to reduced training throughput. To address this, ReCycle introduces two key optimizations that ensure re-routed microbatches are processed within the original pipeline schedule's bubbles. First, it decouples the backward pass into two phases: one for computing gradients for the input and another for calculating gradients for the parameters. Second, it avoids synchronization across pipeline stages by staggering the optimizer step. Together, these optimizations enable adaptive pipeline schedules that minimize or even eliminate training throughput degradation during failures. We describe a prototype for ReCycle and show that it achieves high training throughput under multiple failures, outperforming recent proposals for fault-tolerant training such as Oobleck and Bamboo by up to 1.46× and 1.64×, respectively.