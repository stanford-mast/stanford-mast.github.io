---
title: 'Evaluating MapReduce for Multi-core and Multiprocessor Systems'
authors:
  - name: Colby Ranger
  - name: Ramanan Raghuraman
  - name: Arun Penmetsa
  - name: Gary Bradski
  - key: christoskozyrakis
venue: hpca
year: 2007
date: 2007-02-01
doi: 10.1109/hpca.2007.346181
thumbnail: False
materials:
tags:
  - architecture
  - parallel-compute
  - resource-management
---
This paper evaluates the suitability of the MapReduce model for multi-core and multi-processor systems. MapReduce was created by Google for application development on data-centers with thousands of servers. It allows programmers to write functional-style code that is automatically parallelized and scheduled in a distributed system. We describe Phoenix, an implementation of MapReduce for shared-memory systems that includes a programming API and an efficient runtime system. The Phoenix run-time automatically manages thread creation, dynamic task scheduling, data partitioning, and fault tolerance across processor nodes. We study Phoenix with multi-core and symmetric multiprocessor systems and evaluate its performance potential and error recovery features. We also compare MapReduce code to code written in lower-level APIs such as P-threads. Overall, we establish that, given a careful implementation, MapReduce is a promising model for scalable performance on shared-memory systems with simple parallel code.
