---
title: 'Phoenix rebirth: Scalable MapReduce on a large-scale shared-memory system'
authors:
  - key: richardyoo
  - name: Anthony Romano
  - key: christoskozyrakis
venue: iiswc
year: 2009
date: 2009-10-01
doi: 10.1109/iiswc.2009.5306783
thumbnail: False
materials:
tags:
  - parallel-compute
  - memory-storage
---
Dynamic runtimes can simplify parallel programming by automatically managing concurrency and locality without further burdening the programmer. Nevertheless, implementing such runtime systems for large-scale, shared-memory systems can be challenging. This work optimizes Phoenix, a MapReduce runtime for shared-memory multi-cores and multiprocessors, on a quad-chip, 32-core, 256-thread UltraSPARC T2+ system with NUMA characteristics. We show how a multi-layered approach that comprises optimizations on the algorithm, implementation, and OS interaction leads to significant speedup improvements with 256 threads (average of 2.5 times higher speedup, maximum of 19 times). We also identify the roadblocks that limit the scalability of parallel runtimes on shared-memory systems, which are inherently tied to the OS scalability on large-scale systems.
