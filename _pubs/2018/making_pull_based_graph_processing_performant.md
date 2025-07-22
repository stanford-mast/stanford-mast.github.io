---
title: 'Making pull-based graph processing performant'
authors:
  - key: samgrossman
  - key: heinerlitz
  - key: christoskozyrakis
venue: ppopp
year: 2018
date: 2018-02-01
doi: 10.1145/3178487.3178506
thumbnail: False
materials:
tags:
---
Graph processing engines following either the push-based or pull-based pattern conceptually consist of a two-level nested loop structure. Parallelizing and vectorizing these loops is critical for high overall performance and memory bandwidth utilization. Outer loop parallelization is simple for both engine types but suffers from high load imbalance. This work focuses on inner loop parallelization for pull engines, which when performed naively leads to a significant increase in conflicting memory writes that must be synchronized.
Our first contribution is a scheduler-aware interface for parallel loops that allows us to optimize for the common case in which each thread executes several consecutive iterations. This eliminates most write traffic and avoids all synchronization, leading to speedups of up to 50X.
Our second contribution is the Vector-Sparse format, which addresses the obstacles to vectorization that stem from the commonly-used Compressed-Sparse data structure. Our new format eliminates unaligned memory accesses and bounds checks within vector operations, two common problems when processing low-degree vertices. Vectorization with Vector-Sparse leads to speedups of up to 2.5X.
Our contributions are embodied in Grazelle, a hybrid graph processing framework. On a server equipped with four Intel Xeon E7-4850 v3 processors, Grazelle respectively outperforms Ligra, Polymer, GraphMat, and X-Stream by up to 15.2X, 4.6X, 4.7X, and 66.8X.
