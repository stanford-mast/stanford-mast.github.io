---
title: 'Making pull-based graph processing performant'
authors:
  - key: samgrossman
  - key: heinerlitz
  - key: christoskozyrakis
venue: preprint
year: 2018
date: 2018-02-01
doi: 
thumbnail: False
materials:
tags:
---
Graph processing engines following either the push-based or pull-based pattern conceptually consist of a two-level nested loop structure. Parallelizing and vectorizing these loops is critical for high overall performance and memory bandwidth utilization. Outer loop parallelization is simple for both engine types but suffers from high load imbalance. This work focuses on inner loop parallelization for pull engines, which when performed naively leads to a significant increase in conflicting memory writes that must be synchronized.Our first contribution is ascheduler-awareinterface for parallel loops that allows us to optimize for the common case in which each thread executes several consecutive iterations. This eliminates most write traffic and avoids all synchronization, leading to speedups of up to 50X.Our second contribution is theVector-Sparseformat, which addresses the obstacles to vectorization that stem from the …
