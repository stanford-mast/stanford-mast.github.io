---
title: 'How Fast Can I Run My VLA? Demystifying VLA Inference Performance with VLA-Perf'
authors:
  - name: Wenqi Jiang
  - name: Jason Clemons
  - name: Karu Sankaralingam
  - key: christoskozyrakis
venue: preprint
year: 2026
date: 2026-02-20
doi: 10.48550/arXiv.2602.18397
thumbnail: False
materials:
tags:
  - AI-systems
  - datacenter-systems
  - gpu-systems
  - video-analytics
---
Vision-Language-Action (VLA) models have recently demonstrated impressive capabilities across various embodied AI tasks. While deploying VLA models on real-world robots imposes strict real-time inference constraints, the inference performance landscape of VLA remains poorly understood due to the large combinatorial space of model architectures and inference systems. In this paper, we ask a fundamental research question: How should we design future VLA models and systems to support real-time inference? To address this question, we first introduce VLA-Perf, an analytical performance model that can analyze inference performance for arbitrary combinations of VLA models and inference systems. Using VLA-Perf, we conduct the first systematic study of the VLA inference performance landscape. From a model-design perspective, we examine how inference performance is affected by model scaling, model architectural choices, long-context video inputs, asynchronous inference, and dual-system model pipelines. From the deployment perspective, we analyze where VLA inference should be executed -- on-device, on edge servers, or in the cloud -- and how hardware capability and network performance jointly determine end-to-end latency. By distilling 15 key takeaways from our comprehensive evaluation, we hope this work can provide practical guidance for the design of future VLA models and inference systems.
