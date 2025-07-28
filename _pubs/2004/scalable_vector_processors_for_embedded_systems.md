---
title: 'Scalable, vector processors for embedded systems'
authors:
  - key: christoskozyrakis
  - name: David A Patterson
    affiliation: UC Berkeley
venue: ieeemicro
year: 2004
date: 2004-01-01
doi: 10.1109/MM.2003.1261385
thumbnail: False
materials:
tags:
---
For embedded applications with data-level parallelism, a vector processor offers high performance at low power consumption and low design complexity. Unlike superscalar and VLIW designs, a vector processor is scalable and can optimally match specific application requirements.To demonstrate that vector architectures meet the requirements of embedded media processing, we evaluate the Vector IRAM, or VIRAM (pronounced "V-IRAM"), architecture developed at UC Berkeley, using benchmarks from the Embedded Microprocessor Benchmark Consortium (EEMBC). Our evaluation covers all three components of the VIRAM architecture: the instruction set, the vectorizing compiler, and the processor microarchitecture. We show that a compiler can vectorize embedded tasks automatically without compromising code density. We also describe a prototype vector processor that outperforms high-end superscalar and VLIW designs by 1.5x to 100x for media tasks, without compromising power consumption. Finally, we demonstrate that clustering and modular design techniques let a vector processor scale to tens of arithmetic data paths before wide instruction-issue capabilities become necessary.
