---
title: 'Overcoming the limitations of conventional vector processors'
authors:
  - key: christoskozyrakis
  - name: David Patterson
venue: isca
year: 2003
date: 2003-06-01
doi: 10.1145/859618.859664
thumbnail: False
materials:
tags:
  - architecture
  - parallel-compute
  - datacenter-systems
---
Despite their superior performance for multimedia applications, vector processors have three limitations that hinder their widespread acceptance. First, the complexity and size of the centralized vector register file limits the number of functional units. Second, precise exceptions for vector instructions are difficult to implement. Third, vector processors require an expensive on-chip memory system that supports high bandwidth at low access latency. This paper introduces CODE, a scalable vector microarchitecture that addresses these three shortcomings. It is designed around a clustered vector register file and uses a separate network for operand transfers across functional units. With extensive use of decoupling, it can hide the latency of communication across functional units and provides 26% performance improvement over a centralized organization. CODE scales efficiently to 8 functional units without requiring wide instruction issue capabilities. A renaming table makes the clustered register file transparent at the instruction set level. Renaming also enables precise exceptions for vector instructions at a performance loss of less than 5%. Finally, decoupling allows CODE to tolerate large increases in memory latency at sub-linear performance degradation without using on-chip caches. Thus, CODE can use economical, off-chip, memory systems.
