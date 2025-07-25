---
title: 'Implementing and evaluating nested parallel transactions in software transactional memory'
authors:
  - key: woongkibaek
  - name: Nathan Bronson
  - key: christoskozyrakis
  - name: Kunle Olukotun
    affiliation: Stanford
venue: spaa
year: 2010
date: 2010-06-01
doi: 10.1145/1810479.1810528
thumbnail: False
materials:
tags:
---
Transactional Memory (TM) is a promising technique that simplifies parallel programming for shared-memory applications. To date, most TM systems have been designed to efficiently support single-level parallelism. To achieve widespread use and maximize performance gains, TM must support nested parallelism available in many applications and supported by several programming models.
We present NesTM, a software TM (STM) system that supports closed-nested parallel transactions. NesTM is based on a high-performance, blocking STM that uses eager version management and word-granularity conflict detection. Its algorithm targets the state and runtime overheads of nested parallel transactions. We also describe several subtle correctness issues in supporting nested parallel transactions in NesTM and discuss their performance impact.
Through our evaluation, we quantitatively analyze the performance of NesTM using STAMP applications and microbenchmarks based on concurrent data structures. First, we show that the performance overhead of NesTM is reasonable when single-level parallelism is used. Second, we quantify the incremental overhead of NesTM when the parallelism is exploited in deeper nesting levels and draw conclusions that can be useful in designing a nesting-aware TM runtime environment. Finally, we demonstrate a use-case where nested parallelism improves the performance of a transactional microbenchmark.
