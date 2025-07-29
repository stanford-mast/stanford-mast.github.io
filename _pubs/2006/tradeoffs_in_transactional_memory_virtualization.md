---
title: 'Tradeoffs in transactional memory virtualization'
authors:
  - key: jaewoongchung
  - key: chicaominh
  - key: austenmcdonald
  - key: travisskare
  - name: Hassan Chafi
  - name: Brian D Carlstrom
  - key: christoskozyrakis
  - name: Kunle Olukotun
    affiliation: Stanford
venue: asplos
year: 2006
date: 2006-10-01
doi: 10.1145/1168919.1168903
thumbnail: False
materials:
tags:
---
For transactional memory (TM) to achieve widespread acceptance, transactions should not be limited to the physical resources of any specific hardware implementation. TM systems should guarantee correct execution even when transactions exceed scheduling quanta, overflow the capacity of hardware caches and physical memory, or include more independent nesting levels than what is supported in hardware. Existing proposals for TM virtualization are either incomplete or rely on complex hardware implementations, which are an overkill if virtualization is invoked infrequently in the common case.We present eXtended Transactional Memory (XTM), the first TM virtualization system that virtualizes all aspects of transactional execution (time, space, and nesting depth). XTM is implemented in software using virtual memory support. It operates at page granularity, using private copies of overflowed pages to buffer memory updates until the transaction commits and snapshots of pages to detect interference between transactions. We also describe two enhancements to XTM that use limited hardware support to address key performance bottlenecks.We compare XTM to hardwarebased virtualization using both real applications and synthetic microbenchmarks. We show that despite being software-based, XTM and its enhancements are competitive with hardware-based alternatives. Overall, we demonstrate that XTM provides a complete, flexible, and low-cost mechanism for practical TM virtualization.
