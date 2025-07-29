---
title: 'ATLAS: A Scalable Emulator for Transactional Parallel Systems'
authors:
  - key: christoskozyrakis
  - name: Kunle Olukotun
    affiliation: Stanford
venue: warfp
year: 2005
date: 2005-02-01
doi: 
thumbnail: False
materials:
tags:
---
With uniprocessor systems running into instruction-level parallelism (ILP) limits and fundamental VLSI constraints, multiprocessor architectures provide a realistic path towards scalable performance. Nevertheless, the key factors limiting the potential of multiprocessor systems are the difficulty of parallel application development and the hardware complexity of large-scale systems. Several groups have recently proposed parallel software and hardware based on the concept of transactions as a novel approach for addressing the problems of multiprocessor systems [1-6]. Transactions have the potential to simplify parallel programming by eliminating the need for manual orchestration of parallel tasks using locks and messages [5]. Transactions have the potential to improve parallel hardware by allowing for speculative parallelism and increasing the granularity of the coherence and consistency protocols [4].To realize the potential of transactional systems, researchers must address challenges that span across the fields of architecture, programming models, compilers, and operating systems. It is particularly important to prove that transactional software and hardware work well with large enterprise, scientific, and cognitive workloads, which rely on the performance potential of multiprocessor chips. While architectural studies of small-scale systems with reduced datasets are certainly possible through simulation, slowdowns of 5 orders of magnitude are typical when simulating large-scale parallel systems with large enterprise or scientific applications and modern operating systems [7]. The prohibitive slowdowns deter aggressive experiments and …
