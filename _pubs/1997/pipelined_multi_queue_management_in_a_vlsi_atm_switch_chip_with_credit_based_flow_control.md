---
title: 'Pipelined multi-queue management in a VLSI ATM switch chip with credit-based flow-control'
authors:
  - name: Georgios Kornaros
  - key: christoskozyrakis
  - name: Popi Vatsolaki
  - name: Manolis Katevenis
venue: arvlsi
year: 1997
date: 1997-01-01
doi: 10.5555/786452.786683
thumbnail: False
materials:
  - name: ACM DL
    url: https://dl.acm.org/doi/10.5555/786452.786683
    type: file-alt
tags:
  - architecture
  - networking
  - low-latency
---
We describe the queue management block of ATLAS I, a single-chip ATM switch (router) with optional credit-based (backpressure) flow control. ATLAS I is a 4-million-transistor 0.35-micron CMOS chip, currently under development, offering 20 Gbit/s aggregate I/O throughput, sub-microsecond cut-through latency, 256-cell shared buffer containing multiple logical output queues, priorities, multicasting, and load monitoring. The queue management block of ATLAS I is a dual parallel pipeline that manages the multiple queues of ready cells, the per-flow-group credits, and the cells that are waiting for credits. All cells, in all queues, share one, common buffer space. These 3- and 4-stage pipelines handle events at the rate of one cell arrival or departure per clock cycle, and one credit arrival per clock cycle. The queue management block consists of two compiled SRAM's, pipeline bypass logic, and multi-port CAM and SRAM blocks that are laid out in full-custom and support special access operations. The full-custom part of queue management contains approximately 65 thousand transistors in logic and 14 Kbits in various special memories, it occupies 2.3 mm2, it consumes 270 mW (worst case), and it operates at 80 MHz (worst case) versus 50 MHz which is the required clock frequency to support the 622 Mb/s switch link rate.
