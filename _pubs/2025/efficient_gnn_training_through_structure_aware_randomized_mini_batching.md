---
title: 'Efficient GNN Training Through Structure-Aware Randomized Mini-Batching'
authors:
  - name: Vignesh Balaji
  - key: christoskozyrakis
  - name: Gal Chechik
  - name: Haggai Maron
venue: preprint
year: 2025
date: 2025-04-25
doi: 10.48550/arXiv.2504.18082
thumbnail: False
materials:
tags:
  - AI-systems
  - accelerators
  - gpu-systems
---
Graph Neural Networks (GNNs) enable learning on realworld graphs and mini-batch training has emerged as the de facto standard for training GNNs because it can scale to very large graphs and improve convergence. Current mini-batch construction policies largely ignore efficiency considerations of GNN training. Specifically, existing mini-batching techniques employ randomization schemes to improve accuracy and convergence. However, these randomization schemes are often agnostic to the structural properties of the graph (for eg. community structure), resulting in highly irregular memory access patterns during GNN training that make suboptimal use of on-chip GPU caches. On the other hand, while deterministic mini-batching based solely on graph structure delivers fast runtime performance, the lack of randomness compromises both the final model accuracy and training convergence speed. In this paper, we present Community-structure-aware Randomized Mini-batching (COMM-RAND), a novel methodology that bridges the gap between the above extremes. COMM-RAND allows practitioners to explore the space between pure randomness and pure graph structural awareness during mini-batch construction, leading to significantly more efficient GNN training with similar accuracy. We evaluated COMM-RAND across four popular graph learning benchmarks. COMM-RAND cuts down GNN training time by up to 2.76x (1.8x on average) while achieving an accuracy that is within 1.79% points (0.42% on average) compared to popular random mini-batching approaches.
