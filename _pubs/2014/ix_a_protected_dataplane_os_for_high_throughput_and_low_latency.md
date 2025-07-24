---
title: 'IX: A Protected Dataplane Operating System for High Throughput and Low Latency'
authors:
  - key: adambelay
  - name: George Prekas
    affiliation: EPFL
  - key: anaklimovic
  - key: samgrossman
  - key: christoskozyrakis
  - name: Edouard Bugnion
    affiliation: EPFL
venue: osdi
year: 2014
date: 2014-10-01
doi: 10.5555/2685048.2685053
thumbnail: False
materials:
tags:
---
The conventional wisdom is that aggressive networking requirements, such as high packet rates for small messages and microsecond-scale tail latency, are best addressed outside the kernel, in a user-level networking stack. We present IX, a dataplane operating system that provides high I/O performance, while maintaining the key advantage of strong protection offered by existing kernels. IX uses hardware virtualization to separate management and scheduling functions of the kernel (control plane) from network processing (dataplane). The data-plane architecture builds upon a native, zero-copy API and optimizes for both bandwidth and latency by dedicating hardware threads and networking queues to data-plane instances, processing bounded batches of packets to completion, and by eliminating coherence traffic and multi-core synchronization. We demonstrate that IX outperforms Linux and state-of-the-art, user-space network stacks significantly in both throughput and end-to-end latency. Moreover, IX improves the throughput of a widely deployed, key-value store by up to 3.6x and reduces tail latency by more than 2x.
