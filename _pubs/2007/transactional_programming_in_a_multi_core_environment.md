---
title: 'Transactional programming in a multi-core environment'
authors:
  - name: Ali-Reza Adl-Tabatabai
  - key: christoskozyrakis
  - name: Bratin Saha
venue: ppopp
year: 2007
date: 2007-03-01
doi: 10.1145/1229428.1229484
thumbnail: False
materials:
tags:
---
With single thread performance starting to plateau, HW architects have turned to chip level multiprocessing (CMP) to increase processing power. All major microprocessor companies are aggressively shipping multi-core products in the mainstream computing market. Moore's law will largely be used to increase HW thread-level parallelism through higher core counts in a CMP environment. CMPs bring new challenges into the design of the software system stack.
In this tutorial, we talk about the shift to multi-core processors and the programming implications. In particular, we focus on transactional programming. Transactions have emerged as a promising alternative to lock-based synchronization that eliminates many of the problems associated with lock-based synchronization. We discuss the design of both hardware and software transactional memory and quantify the tradeoffs between the different design points. We show how to extend the Java and C languages with transactional constructs, and how to integrate transactions with compiler optimizations and the language runtime (e.g., memory manager and garbage collection).
