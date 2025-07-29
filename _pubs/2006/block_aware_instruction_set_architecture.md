---
title: 'Block-aware instruction set architecture'
authors:
  - key: ahmadzmily
  - key: christoskozyrakis
venue: taco
year: 2006
date: 2006-09-01
doi: 10.1145/1162690.1162694
thumbnail: False
materials:
tags:
---
Instruction delivery is a critical component for wide-issue, high-frequency processors since its bandwidth and accuracy place an upper limit on performance. The processor front-end accuracy and bandwidth are limited by instruction-cache misses, multicycle instruction-cache accesses, and target or direction mispredictions for control-flow operations. This paper presents a block-aware instruction set (BLISS) that allows software to assist with front-end challenges. BLISS defines basic block descriptors that are stored separately from the actual instructions in a program. We show that BLISS allows for a decoupled front-end that tolerates instruction-cache latency, facilitates instruction prefetching, and leads to higher prediction accuracy.
