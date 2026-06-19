---
title: 'A media-enhanced vector architecture for embedded memory systems'
authors:
  - key: christoskozyrakis
venue: techreport
year: 1999
date: 1999-07-01
doi:
thumbnail: False
materials:
  - name: Report
    url: https://www2.eecs.berkeley.edu/Pubs/TechRpts/1999/Archive/CSD-99-1059.pdf
    type: file-alt
tags:
  - architecture
  - parallel-compute
  - memory-storage
  - datacenter-systems
  - near-data-processing
  - energy-efficiency
---
Next generation portable devices will require processors with both low energy consumption and high performance for media functions. At the same time, modern CMOS technology creates the need for highly scalable VLSI architectures. Conventional processor architectures fail to meet these requirements. This paper presents the architecture of Vector IRAM (VIRAM), a processor that combines vector processing with embedded DRAM technology.

Vector processing achieves high multimedia performance with simple hardware, while embedded DRAM provides high memory bandwidth at low energy consumption. VIRAM provides flexible support for media data types, short vectors, and DSP features. The vector pipeline is enhanced to hide DRAM latency without using caches. The peak performance is 3.2 GFLOPS (single precision) and maximum memory bandwidth is 25.6 GBytes/s. With a target power consumption of 2 Watts for the vector pipeline and the memory system, VIRAM supports 1.6 GFLOPS/Watt. For a set of representative media kernels, VIRAM sustains on average 88% of its peak performance, outperforming conventional SIMD media extensions and DSP processors by factors of 4.5 to 17. Using a clustered implementation approach, the modular design can be scaled without complicating control logic. We demonstrate that scaling the architecture leads to near linear application speedup. We also evaluate the effect of scaling the capacity and parallelism of the on-chip memory system to die area and sustained performance.
