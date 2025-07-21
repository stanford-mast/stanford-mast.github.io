---
title: 'The IX operating system: Combining low latency, high throughput, and efficiency in a protected dataplane'
authors:
  - key: adambelay
  - name: George Prekas
  - name: Mia Primorac
  - key: anaklimovic
  - key: samgrossman
  - key: christoskozyrakis
  - name: Edouard Bugnion
venue: preprint
year: 2016
date: 2016-12-01
doi: 
thumbnail: False
materials:
tags:
---
The conventional wisdom is that aggressive networking requirements, such as high packet rates for small messages and μs-scale tail latency, are best addressed outside the kernel, in a user-level networking stack. We presentix, a dataplane operating system that provides high I/O performance and high resource efficiency while maintaining the protection and isolation benefits of existing kernels.ixuses hardware virtualization to separate management and scheduling functions of the kernel (control plane) from network processing (dataplane). The dataplane architecture builds upon a native, zero-copy API and optimizes for both bandwidth and latency by dedicating hardware threads and networking queues to dataplane instances, processing bounded batches of packets to completion, and eliminating coherence traffic and multicore synchronization. The control plane dynamically adjusts core allocations and voltage …
