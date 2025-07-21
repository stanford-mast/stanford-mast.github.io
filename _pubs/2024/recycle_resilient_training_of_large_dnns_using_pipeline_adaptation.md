---
title: 'Recycle: Resilient training of large dnns using pipeline adaptation'
authors:
  - key: swapnilgandhi
  - key: markzhao
  - key: athinagorasskiadopoulos
  - key: christoskozyrakis
venue: preprint
year: 2024
date: 2024-11-01
doi: 
thumbnail: False
materials:
tags:
---
Training large Deep Neural Network (DNN) models requires thousands of GPUs over the course of several days or weeks. At this scale, failures are frequent and can have a big impact on training throughput. Utilizing spare GPU servers to mitigate performance loss becomes increasingly costly as model sizes grow. ReCycle is a system designed for efficient DNN training in the presence of failures, without relying on spare servers. It exploits the inherentfunctional redundancyin distributed training systems - where servers across data-parallel groups store the same model parameters - andpipeline schedule bubbleswithin each data-parallel group. When servers fails, ReCycle dynamically re-routes microbatches to data-parallel peers, allowing for uninterrupted training despite multiple failures. However, this re-routing can create imbalances across pipeline stages, leading to reduced training throughput. To address …
