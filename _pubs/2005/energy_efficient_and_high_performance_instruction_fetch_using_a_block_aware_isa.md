---
title: 'Energy-efficient and high-performance instruction fetch using a block-aware ISA'
authors:
  - key: ahmadzmily
  - key: christoskozyrakis
venue: ispld
year: 2005
date: 2005-08-01
doi: 10.1145/1077603.1077614
thumbnail: False
materials:
tags:
---
The front-end in superscalar processors must deliver high application performance in an energy-effective manner. Impediments such as multi-cycle instruction accesses, instruction-cache misses, and mispredictions reduce performance by 48% and increase energy consumption by 21%. This paper presents a block-aware instruction set architecture (BLISS) that defines basic block descriptors in addition to the actual instructions in a program. BLISS allows for a decoupled front-end that reduces the time and energy spent on misspeculated instructions. It also allows for accurate instruction prefetching and energy efficient instruction access. A BLISS-based front-end leads to 14% IPC, 16% total energy, and 83% energy-delay-squared product improvements for wide-issue processors.
