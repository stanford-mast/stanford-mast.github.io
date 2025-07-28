---
title: 'Improving instruction delivery with a block-aware ISA'
authors:
  - key: ahmadzmily
  - name: Earl Killian
  - key: christoskozyrakis
venue: europar
year: 2005
date: 2005-08-01
doi: 10.1007/11549468_60
thumbnail: False
materials:
tags:
---
Instruction delivery is a critical component for wide-issue processors since its bandwidth and accuracy place an upper limit on performance. The processor front-end accuracy and bandwidth are limited by instruction cache misses, multi-cycle instruction cache accesses, and target or direction mispredictions for control-flow operations. This paper introduces a block-aware ISA (BLISS) that helps accurate instruction delivery by defining basic block descriptors in addition to and separate from the actual instructions in a program. We show that BLISS allows for a decoupled front-end that tolerates cache latency and allows for higher speculation accuracy. This translates to a 20% IPC and 14% energy improvements over conventional front-ends. We also demonstrate that a BLISS-based front-end outperforms by 13% decoupled front-ends that detect fetched blocks dynamically in hardware, without any information from the ISA.
