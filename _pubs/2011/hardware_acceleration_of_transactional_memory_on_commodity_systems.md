---
title: 'Hardware acceleration of transactional memory on commodity systems'
authors:
  - name: Jared Casper
    affiliation: Stanford
  - name: Tayo Oguntebi
    affiliation: Stanford
  - name: Sungpack Hong
    affiliation: Stanford
  - name: Nathan G Bronson
    affiliation: Stanford
  - key: christoskozyrakis
  - name: Kunle Olukotun
    affiliation: Stanford
venue: asplos
year: 2011
date: 2011-03-01
doi: 10.1145/1950365.1950372
thumbnail: False
materials:
tags:
---
The adoption of transactional memory is hindered by the high overhead of software transactional memory and the intrusive design changes required by previously proposed TM hardware. We propose that hardware to accelerate software transactional memory (STM) can reside outside an unmodified commodity processor core, thereby substantially reducing implementation costs. This paper introduces Transactional Memory Acceleration using Commodity Cores (TMACC), a hardware-accelerated TM system that does not modify the processor, caches, or coherence protocol.
We present a complete hardware implementation of TMACC using a rapid prototyping platform. Using this hardware, we implement two unique conflict detection schemes which are accelerated using Bloom filters on an FPGA. These schemes employ novel techniques for tolerating the latency of fine-grained asynchronous communication with an out-of-core accelerator. We then conduct experiments to explore the feasibility of accelerating TM without modifying existing system hardware. We show that, for all but short transactions, it is not necessary to modify the processor to obtain substantial improvement in TM performance. In these cases, TMACC outperforms an STM by an average of 69% in applications using moderate-length transactions, showing maximum speedup within 8% of an upper bound on TM acceleration. Overall, we demonstrate that hardware can substantially accelerate the performance of an STM on unmodified commodity processors.
