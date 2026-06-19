---
title: 'The Common Case Transactional Behavior of Multithreaded Programs'
authors:
  - name: JaeWoong Chung
  - name: Hassan Chafi
  - name: Chi Cao Minh
  - key: austenmcdonald
  - name: Brian D. Carlstrom
  - key: christoskozyrakis
  - name: Kunle Olukotun
venue: hpca
year: 2006
date: 2006-02-01
doi: 10.1109/hpca.2006.1598135
thumbnail: False
materials:
tags:
  - architecture
  - parallel-compute
  - transactional-memory
---
Transactional memory (TM) provides an easy-to-use and high-performance parallel programming model for the upcoming chip-multiprocessor systems. Several researchers have proposed alternative hardware and software TM implementations. However, the lack of transaction-based programs makes it difficult to understand the merits of each proposal and to tune future TM implementations to the common case behavior of real application. This work addresses this problem by analyzing the common case transactional behavior for 35 multithreaded programs from a wide range of application domains. We identify transactions within the source code by mapping existing primitives for parallelism and synchronization management to transaction boundaries. The analysis covers basic characteristics such as transaction length, distribution of read-set and write-set size, and the frequency of nesting and I/O operations. The measured characteristics provide key insights into the design of efficient TM systems for both non-blocking synchronization and speculative parallelization.
