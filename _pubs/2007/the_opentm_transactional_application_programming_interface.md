---
title: 'The OpenTM Transactional Application Programming Interface'
authors:
  - key: woongkibaek
  - name: Chi Cao Minh
  - name: Martin Trautmann
  - key: christoskozyrakis
  - name: Kunle Olukotun
venue: pact
year: 2007
date: 2007-09-01
doi: 10.1109/pact.2007.4336227
thumbnail: False
materials:
tags:
  - compilers
  - parallel-compute
  - transactional-memory
  - resource-management
---
Transactional Memory (TM) simplifies parallel programming by supporting atomic and isolated execution of user-identified tasks. To date, TM programming has required the use of libraries that make it difficult to achieve scalable performance with code that is easy to develop and maintain. For TM programming to become practical, it is important to integrate TM into familiar, high-level environments for parallel programming. This paper presents OpenTM, an application programming interface (API) for parallel programming with transactions. OpenTM extends OpenMP, a widely used API for shared-memory parallel programming, with a set of compiler directives to express non-blocking synchronization and speculative parallelization based on memory transactions. We also present a portable OpenTM implementation that produces code for hardware, software, and hybrid TM systems. The implementation builds upon the OpenMP support in the GCC compiler and includes a runtime for the C programming language. We evaluate the performance and programmability features of OpenTM. We show that it delivers the performance of fine-grain locks at the programming simplicity of coarse-grain locks. Compared to transactional programming with lower-level interfaces, it removes the burden of manual annotations for accesses to shared variables and enables easy changes of the scheduling and contention management policies. Overall, OpenTM provides a practical and efficient TM programming environment within the familiar scope of OpenMP.
