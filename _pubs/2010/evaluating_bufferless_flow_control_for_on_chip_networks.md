---
title: 'Evaluating Bufferless Flow Control for On-chip Networks'
authors:
  - name: George Michelogiannakis
  - key: danielsanchez
  - name: William J. Dally
  - key: christoskozyrakis
venue: nocs
year: 2010
date: 2010-05-01
doi: 10.1109/nocs.2010.10
thumbnail: False
materials:
tags:
  - architecture
  - networking
  - energy-efficiency
---
With the emergence of on-chip networks, the power consumed by router buffers has become a primary concern. Bufferless flow control addresses this issue by removing router buffers, and handles contention by dropping or deflecting flits. This work compares virtual-channel (buffered) and deflection (packet-switched bufferless) flow control. Our evaluation includes optimizations for both schemes: buffered networks use custom SRAM-based buffers and empty buffer bypassing for energy efficiency, while bufferless networks feature a novel routing scheme that reduces average latency by 5%. Results show that unless process constraints lead to excessively costly buffers, the performance, cost and increased complexity of deflection flow control outweigh its potential gains: bufferless designs are only marginally (up to 1.5%) more energy efficient at very light loads, and buffered networks provide lower latency and higher throughput per unit power under most conditions.
