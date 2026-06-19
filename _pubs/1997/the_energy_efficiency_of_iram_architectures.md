---
title: 'The energy efficiency of IRAM architectures'
authors:
  - name: Richard Fromm
  - name: Stylianos Perissakis
  - name: Neal Cardwell
  - key: christoskozyrakis
  - name: Benjamin McGaughy
  - name: David Patterson
  - name: Thomas Anderson
  - name: Katherine Yelick
venue: isca
year: 1997
date: 1997-06-01
doi: 10.1145/264107.264214
thumbnail: False
materials:
tags:
  - architecture
  - near-data-processing
  - energy-efficiency
---
Portable systems demand energy efficiency in order to maximize battery life. IRAM architectures, which combine DRAM and a processor on the same chip in a DRAM process, are more energy efficient than conventional systems. The high density of DRAM permits a much larger amount of memory on-chip than a traditional SRAM cache design in a logic process. This allows most or all IRAM memory accesses to be satisfied on-chip. Thus there is much less need to drive high-capacitance off-chip buses, which contribute significantly to the energy consumption of a system. To quantify this advantage we apply models of energy consumption in DRAM and SRAM memories to results from cache simulations of applications reflective of personal productivity tasks on low power systems. We find that IRAM memory hierarchies consume as little as 22% of the energy consumed by a conventional memory hierarchy for memory-intensive applications, while delivering comparable performance. Furthermore, the energy consumed by a system consisting of an IRAM memory hierarchy combined with an energy efficient CPU core is as little as 40% of that of the same CPU core with a traditional memory hierarchy.
