---
title: 'A low power front-end for embedded processors using a block-aware instruction set'
authors:
  - key: ahmadzmily
  - key: christoskozyrakis
venue: cases
year: 2007
date: 2007-09-01
doi: 10.1145/1289881.1289926
thumbnail: False
materials:
tags:
---
Energy, power, and area efficiency are critical design concerns for embedded processors. Much of the energy of a typical embedded processor is consumed in the front-end since instruction fetching happens on nearly every cycle and involves accesses to large memory arrays such as instruction and branch target caches. The use of small front-end arrays leads to significant power and area savings, but typically results in significant performance degradation. This paper evaluates and compares optimizations that improve the performance of embedded processors with small front-end caches. We examine both software techniques, such as instruction re-ordering and selective caching, and hardware techniques, such as instruction prefetching, tagless instruction cache, and unified caches for instruction and branch targets. We demonstrate that, building on top of a block-aware instruction set, these optimizations can eliminate the performance degradation due to small front-end caches. Moreover, selective combinations of these optimizations lead to an embedded processor that performs significantly better than the large cache design while maintaining the area and energy efficiency of the small cache design.
