---
title: 'Over the Memory Wall, Into the Instruction Wall: The New Bottleneck in GPU Data Processing'
authors:
  - name: Sven Hepkema
  - name: Bowen Wu
  - key: christoskozyrakis
  - name: Yannis Chronis
  - name: Gustavo Alonso
venue: preprint
year: 2026
date: 2026-08-13
doi: 10.48550/arXiv.2608.13696
thumbnail: True
materials:
  - name: paper
    url: /pubs/over_the_memory_wall_into_the_instruction_wall_the_new_bottleneck_in_gpu_data_processing/paper.pdf
    type: file-pdf
  - name: arXiv
    url: https://doi.org/10.48550/arXiv.2608.13696
    type: file-alt
tags:
  - architecture
  - databases
  - memory-storage
  - datacenter-systems
  - accelerators
  - gpu-systems
---
Datacenter GPUs have seen an order-of-magnitude increase in memory bandwidth with the adoption of newer generations of HBM. Meanwhile, GPU database systems are gaining traction, many building on cuDF, an open-source library of GPU relational operators. Previously, query performance was bound by memory bandwidth, but the increase in memory bandwidth has not resulted in a proportional speedup of cuDF kernels. To investigate why performance has not kept up, we built Valk, a performance analysis tool that combines data from multiple profilers. We profile cuDF running TPC-H in-memory on two extremes of hardware capability, the L4 and GH200 GPUs. The GH200 has 13.4x the memory bandwidth and 2.5x the instruction throughput of the L4, yet is only 5.2x faster in running TPC-H. Our analysis shows that when memory bandwidth is increased, kernels become compute bound. From our analysis, we make three recommendations to fully utilize the GPUs' potential for relational workloads when the memory wall is removed: kernels need to (1) make more efficient use of caches, (2) increase occupancy and/or instruction level parallelism, and (3) execute fewer instructions per memory access.
