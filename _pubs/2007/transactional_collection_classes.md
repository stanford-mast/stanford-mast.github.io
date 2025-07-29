---
title: 'Transactional collection classes'
authors:
  - name: Brian D Carlstrom
  - key: austenmcdonald
  - name: Michael Carbin
  - key: christoskozyrakis
  - name: Kunle Olukotun
    affiliation: Stanford
venue: ppopp
year: 2007
date: 2007-03-01
doi: 10.1145/1229428.1229441
thumbnail: False
materials:
tags:
---
While parallel programmers find it easier to reason about large atomic regions, the conventional mutual exclusion-based primitives for synchronization force them to interleave many small operations to achieve performance. Transactional memory promises that programmer scan use large atomic regions while achieving similar performance. However, these large transactions can conflict when operating on shared data structures, even for logically independent operations. Transactional collection classes address this problem by allowing long-running transactions to operate on shared data while eliminating unnecessary conflicts. Transactional collection classes wrap existing data structures, without the need for custom implementations or knowledge of data structure internals.Without transactional collection classes, access to shared datafrom within long-running transactions can suffer from data dependency conflicts that are logically unnecessary, but are artifacts of the data structure implementation such as hash table collisions or tree-balancing rotations. Our transactional collection classes use the concept of semantic concurrency control to eliminate these unnecessary data dependencies, replacing them with conflict detection based on the operations of the abstract data type.The design and behavior of these transactional collection classes is discussed with reference to the related work from the database community such as multi-level transactions and semantic concurrency control, as well as other concurrent data structures such as java.util.concurrent. The required transactional semantics needed for implementing transactional collection are enumerated, including open-nested transactions and commit and abort handlers. We also discuss how isolation can be reduced for greater concurrency. Finally, we provide guidelines on the construction of classes that preserve isolation and serializability.The performance of these classes is evaluated with a number of benchmarks including targeted micro-benchmarks and a version of SPECjbb2000 with increased contention. The results show that easier-to-use long transactions can still allow programs to deliver scalable performance by simply wrapping existing data structures with transactional collection classes.
