---
title: 'ATLAS: A Chip-Multiprocessor with Transactional Memory Support'
authors:
  - name: Njuguna Njoroge
  - name: Jared Casper
  - key: sewookwee
  - name: Yuriy Teslyar
  - name: Daxia Ge
  - key: christoskozyrakis
  - name: Kunle Olukotun
venue: date
year: 2007
date: 2007-04-01
doi: 10.1109/date.2007.364558
thumbnail: False
materials:
tags:
  - architecture
  - parallel-compute
  - memory-storage
  - transactional-memory
  - accelerators
  - energy-efficiency
---
Chip-multiprocessors are quickly becoming popular in embedded systems. However, the practical success of CMPs strongly depends on addressing the difficulty of multithreaded application development for such systems. Transactional memory (TM) promises to simplify concurrency management in multithreaded applications by allowing programmers to specify coarse-grain parallel tasks, while achieving performance comparable to fine-grain lock-based applications. This paper presents ATLAS, the first prototype of a CMP with hardware support for transactional memory. ATLAS includes 8 embedded PowerPC cores that access coherent shared memory in a transactional manner. The data cache for each core is modified to support the speculative buffering and conflict detection necessary for transactional execution. The authors have mapped ATLAS to the BEE2 multi-FPGA board to create a full-system prototype that operates at 100MHz, boots Linux, and provides significant performance and ease-of-use benefits for a range of parallel applications. Overall, the ATLAS prototype provides an excellent framework for further research on the software and hardware techniques necessary to deliver on the potential of transactional memory.
