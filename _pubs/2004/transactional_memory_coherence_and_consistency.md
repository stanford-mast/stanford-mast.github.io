---
title: 'Transactional memory coherence and consistency'
authors:
  - name: Lance Hammond
  - name: Vicky Wong
  - name: Mike Chen
  - name: Brian D Carlstrom
  - name: John D Davis
  - name: Ben Hertzberg
  - name: Manohar K Prabhu
  - name: Honggo Wijaya
  - key: christoskozyrakis
  - name: Kunle Olukotun
    affiliation: Stanford
venue: isca
year: 2004
date: 2004-03-01
doi: 10.1145/1028176.1006711
thumbnail: False
materials:
tags:
---
In this paper, we propos a new shared memory model: Transactionalmemory Coherence and Consistency (TCC).TCC providesa model in which atomic transactions are always the basicunit of parallel work, communication, memory coherence, andmemory reference consistency.TCC greatly simplifies parallelsoftware by eliminating the need for synchronization using conventionallocks and semaphores, along with their complexities.TCC hardware must combine all writes from each transaction regionin a program into a single packet and broadcast this packetto the permanent shared memory state atomically as a large block.This simplifies the coherence hardware because it reduces theneed for small, low-latency messages and completely eliminatesthe need for conventional snoopy cache coherence protocols, asmultiple speculatively written versions of a cache line may safelycoexist within the system.Meanwhile, automatic, hardware-controlledrollback of speculative transactions resolves any correctnessviolations that may occur when several processors attemptto read and write the same data simultaneously.The cost of thissimplified scheme is higher interprocessor bandwidth.To explore the costs and benefits of TCC, we study the characterisitcsof an optimal transaction-based memory system, and examinehow different design parameters could affect the performanceof real systems.Across a spectrum of applications, the TCC modelitself did not limit available parallelism.Most applications areeasily divided into transactions requiring only small write buffers,on the order of 4-8 KB.The broadcast requirements of TCCare high, but are well within the capabilities of CMPs and small-scaleSMPs with high-speed interconnects.
