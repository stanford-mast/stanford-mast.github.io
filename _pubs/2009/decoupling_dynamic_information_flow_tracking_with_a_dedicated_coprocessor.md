---
title: 'Decoupling Dynamic Information Flow Tracking with a dedicated coprocessor'
authors:
  - key: harikannan
  - key: michaeldalton
  - key: christoskozyrakis
venue: dsn
year: 2009
date: 2009-06-01
doi: 10.1109/dsn.2009.5270347
thumbnail: False
materials:
tags:
  - architecture
  - cloud
  - security
---
Dynamic information flow tracking (DIFT) is a promising security technique. With hardware support, DIFT prevents a wide range of attacks on vulnerable software with minimal performance impact. DIFT architectures, however, require significant changes in the processor pipeline that increase design and verification complexity and may affect clock frequency. These complications deter hardware vendors from supporting DIFT. This paper makes hardware support for DIFT cost effective by decoupling DIFT functionality onto a simple, separate coprocessor. Decoupling is possible because DIFT operations and regular computation need only synchronize on system calls. The coprocessor is a small hardware engine that performs logical operations and caches 4-bit tags. It introduces no changes to the design or layout of the main processor's logic, pipeline, or caches, and can be combined with various processors. Using a full-system hardware prototype and realistic Linux workloads, we show that the DIFT coprocessor provides the same security guarantees as current DIFT architectures with low runtime overheads.
