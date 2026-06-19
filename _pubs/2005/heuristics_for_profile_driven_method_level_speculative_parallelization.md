---
title: 'Heuristics for Profile-Driven Method-Level Speculative Parallelization'
authors:
  - name: John Whaley
  - key: christoskozyrakis
venue: icpp
year: 2005
date: 2005-06-01
doi: 10.1109/icpp.2005.44
thumbnail: False
materials:
tags:
  - compilers
  - parallel-compute
---
Thread level speculation (TLS) is an effective technique for extracting parallelism from sequential code. Method calls provide good templates for the boundaries of speculative threads as they often describe independent tasks. However, selecting the most profitable methods to speculate on is difficult as it involves complicated trade-offs between speculation violations, thread overheads, and resource utilization. This paper presents a first analysis of heuristics for automatic selection of speculative threads across method boundaries using a dynamic or profile-driven compiler. We study the potential of three classes of heuristics that involve increasing amounts of profiling information and runtime complexity. Several of the heuristics allow for speculation to start at internal method points, nested speculation, and speculative thread preemption. Using a set of Java benchmarks, we demonstrate that careful thread selection at method boundaries leads to speedups of 1.4 to 1.8 on practical TLS hardware. Single-pass heuristics that filter out less profitable methods using simple speedup estimates lead to the best average performance by consistently providing a good balance between over- and under-speculation. On the other hand, multi-pass heuristics that perform additional filtering by taking into account interactions between nested method calls often lead to significant under-speculation and perform poorly.
