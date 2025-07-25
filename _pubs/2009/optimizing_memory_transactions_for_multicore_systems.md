---
title: 'Optimizing memory transactions for multicore systems'
authors:
  - name: Ali-Reza Adl-Tabatabai
  - key: christoskozyrakis
  - name: Bratin Saha
venue: mps
year: 2009
date: 2009-08-01
doi: 10.1007/978-1-4419-0263-4_5
thumbnail: False
materials:
tags:
---
The shift to multicore architectures will require new programming technologies that enable mainstream developers to write parallel programs that can safely take advantage of the parallelism offered by multicore processors. One challenging aspect of shared memory parallel programming is synchronization. Programmers have traditionally used locks for synchronization, but lock-based synchronization has well-known pitfalls that make it hard to use for building thread-safe and scalable software components. Memory transactions have emerged as a promising alternative to lock-based synchronization because they promise to eliminate many of the problems associated with locks. Transactional programming constructs, however, have overheads and require optimizations to make them practical. Transactions can also benefit significantly from hardware support, and multicore processors with their large transistor budgets and on-chip memory hierarchies have the opportunity to provide this support.

In this chapter, we discuss the design of transactional memory systems, focusing on software optimizations and hardware support to accelerate their performance. We show how programming languages, compilers, and language runtimes can support transactional memory. We describe optimization opportunities for reducing the overheads of transactional memory and show how the compiler and runtime can perform these optimizations. We describe a range of transactional memory hardware acceleration mechanisms spanning techniques that execute transactions completely in hardware to techniques that provide hardware acceleration for transactions executed mainly in software.
