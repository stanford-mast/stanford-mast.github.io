---
title: 'Vector Lane Threading'
authors:
  - name: Suzanne Rivoire
  - name: Rebecca Schultz
  - name: Tomofumi Okuda
  - key: christoskozyrakis
venue: icpp
year: 2006
date: 2006-08-01
doi: 10.1109/icpp.2006.74
thumbnail: False
materials:
tags:
  - architecture
  - parallel-compute
---
Multi-lane vector processors achieve excellent computational throughput for programs with high data-level parallelism (DLP). However, application phases without significant DLP are unable to fully utilize the datapaths in the vector lanes. In this paper, we propose vector lane threading (VLT), an architectural enhancement that allows idle vector lanes to run short-vector or scalar threads. VLT-enhanced vector hardware can exploit both data-level and thread-level parallelism to achieve higher performance. We investigate implementation alternatives for VLT, focusing mostly on the instruction issue bandwidth requirements. We demonstrate that VLT's area overhead is small. For applications with short vectors, VLT leads to additional speedup of 1.4 to 2.3 over the base vector design. For scalar threads, VLT outperforms a 2-way CMP design by a factor of two. Overall, VLT allows vector processors to reach high computational throughput for a wider range of parallel programs and become a competitive alternative to CMP systems.
