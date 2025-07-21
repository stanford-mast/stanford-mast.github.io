---
title: 'Accelerating Mixture-of-Experts Training with Adaptive Expert Replication'
authors:
  - key: athinagorasskiadopoulos
  - key: markzhao
  - key: swapnilgandhi
  - name: Thomas Norrie
    affiliation: OpenAI
  - name: Shrijeet Mukherjee
    affiliation: Enfabrica
  - key: christoskozyrakis
venue: preprint
year: 2025
date: 2025-04-01
doi: 
thumbnail: False
materials:
tags:
---
Mixture-of-Experts (MoE) models have become a widely adopted solution to continue scaling model sizes without a corresponding linear increase in compute. During MoE model training, each input token is dynamically routed to a subset of experts -- sparsely-activated feed-forward networks -- within each transformer layer. The distribution of tokens assigned to each expert varies widely and rapidly over the course of training. To handle the wide load imbalance across experts, current systems are forced to either drop tokens assigned to popular experts, degrading convergence, or frequently rebalance resources allocated to each expert based on popularity, incurring high state migration overheads. To break this performance-accuracy tradeoff, we introduce SwiftMoE, an adaptive MoE training system. The key insight of SwiftMoE is to decouple the placement of expert parameters from their large optimizer state. SwiftMoE statically partitions the optimizer of each expert across all training nodes. Meanwhile, SwiftMoE dynamically adjusts the placement of expert parameters by repurposing existing weight updates, avoiding migration overheads. In doing so, SwiftMoE right-sizes the GPU resources allocated to each expert, on a per-iteration basis, with minimal overheads. Compared to state-of-the-art MoE training systems, DeepSpeed and FlexMoE, SwiftMoE is able to achieve a 30.5% and 25.9% faster time-to-convergence, respectively.
