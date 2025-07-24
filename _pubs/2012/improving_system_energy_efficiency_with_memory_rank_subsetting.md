---
title: 'Improving system energy efficiency with memory rank subsetting'
authors:
  - name: Jung Ho Ahn
  - name: Norman P Jouppi
  - key: christoskozyrakis
  - key: jacobleverich
  - name: Robert S Schreiber
venue: taco
year: 2012
date: 2012-03-01
doi: 10.1145/2133382.2133386
thumbnail: False
materials:
tags:
---
VLSI process technology scaling has enabled dramatic improvements in the capacity and peak bandwidth of DRAM devices. However, current standard DDRx DIMM memory interfaces are not well tailored to achieve high energy efficiency and performance in modern chip-multiprocessor-based computer systems. Their suboptimal performance and energy inefficiency can have a significant impact on system-wide efficiency since much of the system power dissipation is due to memory power. New memory interfaces, better suited for future many-core systems, are needed. In response, there are recent proposals to enhance the energy efficiency of main-memory systems by dividing a memory rank into subsets, and making a subset rather than a whole rank serve a memory request.
We holistically assess the effectiveness of rank subsetting from system-wide performance, energy-efficiency, and reliability perspectives. We identify the impact of rank subsetting on memory power and processor performance analytically, compare two promising rank-subsetting proposals, Multicore DIMM and mini-rank, and verify our analysis by simulating a chip-multiprocessor system using multithreaded and consolidated workloads. We extend the design of Multicore DIMM for high-reliability systems and show that compared with conventional chipkill approaches, rank subsetting can lead to much higher system-level energy efficiency and performance at the cost of additional DRAM devices. This holistic assessment shows that rank subsetting offers compelling alternatives to existing processor-memory interfaces for future DDR systems.
