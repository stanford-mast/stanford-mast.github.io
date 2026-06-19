---
title: 'Thread-safe dynamic binary translation using transactional memory'
authors:
  - name: JaeWoong Chung
  - key: michaeldalton
  - key: harikannan
  - key: christoskozyrakis
venue: hpca
year: 2008
date: 2008-02-01
doi: 10.1109/hpca.2008.4658646
thumbnail: False
materials:
tags:
  - architecture
  - compilers
  - parallel-compute
  - memory-storage
  - transactional-memory
---
Dynamic binary translation (DBT) is a runtime instrumentation technique commonly used to support profiling, optimization, secure execution, and bug detection tools for application binaries. However, DBT frameworks may incorrectly handle multithreaded programs due to races involving updates to the application data and the corresponding metadata maintained by the DBT. Existing DBT frameworks handle this issue by serializing threads, disallowing multithreaded programs, or requiring explicit use of locks. This paper presents a practical solution for correct execution of multithreaded programs within DBT frameworks. To eliminate races involving metadata, we propose the use of transactional memory (TM). The DBT uses memory transactions to encapsulate the data and metadata accesses in a trace, within one atomic block. This approach guarantees correct execution of concurrent threads of the translated program, as TM mechanisms detect and correct races. To demonstrate this approach, we implemented a DBT-based tool for secure execution of x86 binaries using dynamic information flow tracking. This is the first such framework that correctly handles multithreaded binaries without serialization. We show that the use of software transactions in the DBT leads to a runtime overhead of 40%. We also show that software optimizations in the DBT and hardware support for transactions can reduce the runtime overhead to 6%.
