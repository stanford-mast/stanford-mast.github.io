---
title: 'Vector vs. superscalar and VLIW architectures for embedded multimedia benchmarks'
authors:
  - key: christoskozyrakis
  - name: David Patterson
venue: micro
year: 2002
date: 2002-11-01
doi: 10.1109/MICRO.2002.1176257
thumbnail: False
materials:
tags:
  - architecture
  - near-data-processing
  - energy-efficiency
---
Multimedia processing on embedded devices requires an architecture that leads to high performance, low power consumption, reduced design complexity, and small code size. In this paper, we use EEMBC, an industrial benchmark suite, to compare the VIRAM vector architecture to superscalar and VLIW processors for embedded multimedia applications. The comparison covers the VIRAM instruction set, vectorizing compiler and the prototype chip that integrates a vector processor with DRAM main memory. We demonstrate that executable code for VIRAM is up to 10 times smaller than VLIW code and comparable to x86 CISC code. The simple, cache-less VIRAM chip is 2 times faster than a 4-way superscalar RISC processor that uses a 5 times faster clock frequency and consumes 10 times more power. VIRAM is also 10 times faster than cache-based VLIW processors. Even after manual optimization of the VLIW code and insertion of SIMD and DSP instructions, the single-issue VIRAM processor is 60% faster than 5-way to 8-way VLIW designs.
