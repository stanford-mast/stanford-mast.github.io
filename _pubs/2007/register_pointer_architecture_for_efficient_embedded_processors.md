---
title: 'Register pointer architecture for efficient embedded processors'
authors:
  - name: Jason S. Park
  - name: Sang Bum Park
  - name: James D. Balfour
  - name: David Black-Schaffer
  - key: christoskozyrakis
  - name: William J. Dally
venue: date
year: 2007
date: 2007-04-16
doi: 10.1109/date.2007.364659
thumbnail: False
materials:
  - name: IEEE Xplore
    url: https://ieeexplore.ieee.org/document/4211864
    type: file-alt
tags:
  - architecture
  - energy-efficiency
---
Conventional register file architectures cannot optimally exploit temporal locality in data references due to their limited capacity and static encoding of register addresses in instructions. In conventional embedded architectures, the register file capacity cannot be increased without resorting to longer instruction words. Similarly, loop unrolling is often required to exploit locality in the register file accesses across iterations because naming registers statically is inflexible. Both optimizations lead to significant code size increases, which is undesirable in embedded systems. In this paper, the authors introduce the register pointer architecture (RPA), which allows registers to be accessed indirectly through register pointers. Indirection allows a larger register file to be used without increasing the length of instruction words. Additional register file capacity allows many loads and stores, such as those introduced by spill code, to be eliminated, which improves performance and reduces energy consumption. Moreover, indirection affords additional flexibility in naming registers, which reduces the need to apply loop unrolling in order to maximize reuse of register allocated variables.
