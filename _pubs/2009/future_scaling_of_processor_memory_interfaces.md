---
title: 'Future scaling of processor-memory interfaces'
authors:
  - name: Jung Ho Ahn
  - name: Norman P Jouppi
  - key: christoskozyrakis
  - key: jacobleverich
  - name: Robert S Schreiber
venue: sc
year: 2009
date: 2009-11-01
doi: 10.1145/1654059.1654102
thumbnail: False
materials:
tags:
---
Continuous evolution in process technology brings energy-efficiency and reliability challenges, which are harder for memory system designs since chip multiprocessors demand high bandwidth and capacity, global wires improve slowly, and more cells are susceptible to hard and soft errors. Recently, there are proposals aiming at better main-memory energy efficiency by dividing a memory rank into subsets.
We holistically assess the effectiveness of rank subsetting in the context of system-wide performance, energy-efficiency, and reliability perspectives. We identify the impact of rank subsetting on memory power and processor performance analytically, then verify the analyses by simulating a chipmultiprocessor system using multithreaded and consolidated workloads. We extend the design of Multicore DIMM, one proposal embodying rank subsetting, for high-reliability systems and show that compared with conventional chipkill approaches, it can lead to much higher system-level energy efficiency and performance at the cost of additional DRAM devices.
