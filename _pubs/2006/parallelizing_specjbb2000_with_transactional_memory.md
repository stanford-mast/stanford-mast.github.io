---
title: 'Parallelizing specjbb2000 with transactional memory'
authors:
  - name: J Chung
  - name: C Cao Minh
  - name: Brian D Carlstrom
  - key: christoskozyrakis
venue: wtw
year: 2006
date: 2006-06-01
doi: 
thumbnail: False
materials:
tags:
---
As chip-multiprocessors become ubiquitous, it is critical to provide architectural support for practical parallel programming. Transactional Memory (TM)[4] has the potential to simplify concurrency management by supporting parallel tasks (transactions) that appear to execute atomically and in isolation. By virtue of optimistic concurrency, transactional memory promises good parallel performance with easy-to-write, coarse-grain transactions. Furthermore, transactions can address other challenges of lock-based parallel code such as deadlock avoidance and robustness to failures. In this paper, we use transactional memory to parallelize SPECjbb2000 [9], a popular benchmark for Java middleware. SPECjbb2000 combines in a single Java program many common features of 3-tier enterprise systems, hence it is significantly more complicated than the data structure microbenchmarks frequently used for TM research [3, 5, 8]. Since SPECjbb2000 models the operation of a wholesale company with multiple warehouses, the original code is already parallel, with a separate Java thread managing each warehouse. Different warehouses accesses mostly disjoint data structures, hence dependencies are rare. We focus on parallelism within a single warehouse, which is a more challenging case1. Conceptually, there are significant amounts of parallelism within a single warehouse as different customers order or pay for different objects. Nevertheless, all operations within a warehouse access the same data structures (B-trees), hence dependencies are possible and difficult to predict. Overall, single-warehouse SPECjbb2000 is an excellent candidate to explore the ease-of-use and performance potential of transactional memory with irregular code. We study multiple ways of defining transactions within the SPECjbb2000 code and explore their performance potential using an execution-driven simulator for a CMP system with TM support. We demonstrate that even the simplest, coarse-grain transactions (one transaction for a whole operation) lead to significant speedups. Nevertheless, performance is still limited by frequent dependency violations on shared data structures. To mitigate the violation overhead, we use nested transactions, both closed and open, to achieve up to a 75% speedup increase. Closed nesting reduces the penalty of violations and open nesting reduces the frequency of violations. While nested transactions, particularly open, require some additional effort by the programmer, they are still significantly easier to use than fine-grain locks. Overall, we conclude that for SPECjbb2000, transactional memory lives up to its promise of good performance with simple parallel code.
