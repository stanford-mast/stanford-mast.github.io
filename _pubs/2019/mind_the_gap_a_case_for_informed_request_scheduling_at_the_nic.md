---
title: 'Mind the gap: A case for informed request scheduling at the nic'
authors:
  - name: Jack Tigar Humphries
    affiliation: Stanford
  - key: kostiskaffes
  - name: David Mazières
    affiliation: Stanford
  - key: christoskozyrakis
venue: preprint
year: 2019
date: 2019-11-01
doi: 
thumbnail: False
materials:
tags:
---
Recent research in high-throughput networked systems has established the need for centralized and preemptive request scheduling in order to achieve good hardware utilization and low tail latency for a wide variety of workloads. However, this approach is expensive to scale as it requires an increasing number of CPU cores dedicated to scheduling. Moreover, passing every request through a scheduling core introduces latency for inter-core communication and reduces the effectiveness of data preloading and caching optimizations.In this paper, we advocate in favor of pushing request-to-core scheduling back into the NIC. Instead of the simple request distribution of receive-side-scaling (RSS) in current NICs, we suggest implementing preemptive request scheduling by passing to the NIC up-to-date information about core availability and execution status of active requests. We present a prototype implementation on …
