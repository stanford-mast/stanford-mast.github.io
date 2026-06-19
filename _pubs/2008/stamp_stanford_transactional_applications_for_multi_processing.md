---
title: 'STAMP: Stanford Transactional Applications for Multi-Processing'
authors:
  - name: Chi Cao Minh
  - name: JaeWoong Chung
  - key: christoskozyrakis
  - name: Kunle Olukotun
venue: iiswc
year: 2008
date: 2008-10-01
doi: 10.1109/iiswc.2008.4636089
thumbnail: False
materials:
tags:
  - parallel-compute
  - transactional-memory
---
Transactional Memory (TM) is emerging as a promising technology to simplify parallel programming. While several TM systems have been proposed in the research literature, we are still missing the tools and workloads necessary to analyze and compare the proposals. Most TM systems have been evaluated using microbenchmarks, which may not be representative of any real-world behavior, or individual applications, which do not stress a wide range of execution scenarios. We introduce the Stanford Transactional Application for Multi-Processing (STAMP), a comprehensive benchmark suite for evaluating TM systems. STAMP includes eight applications and thirty variants of input parameters and data sets in order to represent several application domains and cover a wide range of transactional execution cases (frequent or rare use of transactions, large or small transactions, high or low contention, etc.). Moreover, STAMP is portable across many types of TM systems, including hardware, software, and hybrid systems. In this paper, we provide descriptions and a detailed characterization of the applications in STAMP. We also use the suite to evaluate six different TM systems, identify their shortcomings, and motivate further research on their performance characteristics.
