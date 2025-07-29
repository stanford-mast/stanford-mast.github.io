---
title: 'Library-based prefetching for pointer-intensive applications'
authors:
  - name: Varun Malhotra
  - key: christoskozyrakis
venue: report
year: 2006
date: 2006-02-01
doi: 
thumbnail: False
materials:
tags:
---
Processor speed has been improving faster than memory latency for over two decades. Thus, an increased portion of execution time is spent stalling on loads, waiting for data from the memory hierarchy. Prefetching is an effective mechanism to hide memory latency for applications with low temporal locality. However, existing hardware prefetching techniques work well for array-based programs but not effective effective for pointer-intensive applications. Existing software prefetching techniques require recompilation or even modifications to application code before running on a new system with different hardware parameters. In this paper, we exploit two opportunities to address this challenge. First, chip-multiprocessors (CMPs) are quickly becoming the norm, providing spare processors for prefetching tasks. Second, productivity reasons encourage programmers to make frequent use of standard or popular data-structure libraries. Hence, we propose a novel software prefetching scheme for pointer-based data-structures in which prefetching is performed by a helper thread included in the data-structure library code. The prefetch thread runs on a spare processor and relies on the library’s knowledge of the data-structure type and access pattern to perform effective prefetching. All the development effort for prefetching is concentrated in the library code and is done once. The user application is not modified at all, as the library API remains the same. We implement and evaluate the library-based prefetch scheme. We demonstrate that it performs accurate prefetching and leads to an average reduction in execution time of 26% for pointer-intensive benchmarks with appreciable memory stall time. Furthermore, we show that, using dynamic adaptation, the benefits from library-based prefetching are robust across a range of memory system and application parameters without the need for recompilation.
