---
title: 'Hardware/compiler codevelopment for an embedded media processor'
authors:
  - key: christoskozyrakis
  - name: David Judd
  - name: Jeremy Gebis
  - name: Sam Williams
  - name: David Patterson
  - name: Katherine Yelick
venue: pieee
year: 2001
date: 2001-11-01
doi: 10.1109/5.964446
thumbnail: False
materials:
tags:
  - architecture
  - compilers
  - near-data-processing
  - energy-efficiency
---
Embedded and portable systems running multimedia applications create a new challenge for hardware architects. A microprocessor for such applications needs to be easy to program like a general-purpose processor and have the performance and power efficiency of a digital signal processor. This paper presents the codevelopment of the instruction set, the hardware, and the compiler for the Vector IRAM media processor. A vector architecture is used to exploit the data parallelism of multimedia programs, which allows the use of highly modular hardware and enables implementations that combine high performance, low power consumption, and reduced design complexity. It also leads to a compiler model that is efficient both in terms of performance and executable code size. The memory system for the vector processor is implemented using embedded DRAM technology, which provides high bandwidth in an integrated, cost-effective manner. The hardware and the compiler for this architecture make complementary contributions to the efficiency of the overall system. This paper explores the interactions and tradeoffs between them, as well as the enhancements to a vector architecture necessary for multimedia processing. We also describe how the architecture, design, and compiler features come together in a prototype system-on-a-chip, able to execute 3.2 billion operations per second per watt.
