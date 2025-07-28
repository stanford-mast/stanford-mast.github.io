---
title: 'Comparative evaluation of memory models for chip multiprocessors'
authors:
  - key: jacobleverich
  - name: Hideho Arakida
  - name: Alex Solomatnikov
  - name: Amin Firoozshahian
  - name: Mark Horowitz
    affiliation: Stanford
  - key: christoskozyrakis
venue: taco
year: 2008
date: 2008-12-01
doi: 10.1145/1455650.1455651
thumbnail: False
materials:
tags:
---
There are two competing models for the on-chip memory in Chip Multiprocessor (CMP) systems: hardware-managed coherent caches and software-managed streaming memory. This paper performs a direct comparison of the two models under the same set of assumptions about technology, area, and computational capabilities. The goal is to quantify how and when they differ in terms of performance, energy consumption, bandwidth requirements, and latency tolerance for general-purpose CMPs. We demonstrate that for data-parallel applications on systems with up to 16 cores, the cache-based and streaming models perform and scale equally well. For certain applications with little data reuse, streaming scales better due to better bandwidth use and macroscopic software prefetching. However, the introduction of techniques such as hardware prefetching and nonallocating stores to the cache-based model eliminates the streaming advantage. Overall, our results indicate that there is not sufficient advantage in building streaming memory systems where all on-chip memory structures are explicitly managed. On the other hand, we show that streaming at the programming model level is particularly beneficial, even with the cache-based model, as it enhances locality and creates opportunities for bandwidth optimizations. Moreover, we observe that stream programming is actually easier with the cache-based model because the hardware guarantees correct, best-effort execution even when the programmer cannot fully regularize an application's code.
