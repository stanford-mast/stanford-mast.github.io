---
title: 'TAPE: A transactional application profiling environment'
authors:
  - name: Hassan Chafi
  - key: chicaominh
  - key: austenmcdonald
  - name: Brian D Carlstrom
  - key: jaewoongchung
  - name: Lance Hammond
  - key: christoskozyrakis
  - name: Kunle Olukotun
    affiliation: Stanford
venue: ics
year: 2005
date: 2005-06-01
doi: 10.1145/1088149.1088176
thumbnail: False
materials:
tags:
---
Transactional Coherence and Consistency (TCC) provides a new parallel programming model that uses transactions as the basic unit of parallel work and communication. TCC simplifies the development of correct parallel code because hardware provides transaction atomicity and ordering. Nevertheless, the programmer or a dynamic compiler must still optimize the parallel code for performance.This paper presents TAPE, a hardware and software infrastructure for profiling in TCC systems. TAPE extends the hardware for transactional execution to identify performance impediments such as dependence violations, buffer overflows, and work imbalance. It filters infrequent events to reduce resource requirements and allows the programmer to focus on the most important bottlenecks. We demonstrate that TAPE introduces minimal die area and performance overhead and can be used continuously, even for production runs. Moreover, we demonstrate how to leverage the profiling information to guide optimization for a set of parallel applications. TAPE accurately identifies the source code location and type of the most important bottlenecks, allowing a programmer to achieve maximum parallel speedup with a few profiling steps.
