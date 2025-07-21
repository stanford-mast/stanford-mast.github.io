---
title: 'RAIL: Predictable, low tail latency for NVMe flash'
authors:
  - key: heinerlitz
  - name: Javier Gonzalez
  - key: anaklimovic
  - key: christoskozyrakis
venue: preprint
year: 2022
date: 2022-01-01
doi: 
thumbnail: False
materials:
tags:
---
Flash-based storage is replacing disk for an increasing number of data center applications, providing orders of magnitude higher throughput and lower average latency. However, applications also require predictable storage latency. Existing Flash devices fail to provide low tail read latency in the presence of write operations. We propose two novel techniques to address SSD read tail latency, includingRedundant Array of Independent LUNs(RAIL) which avoids serialization of reads behind user writes as well aslatency-aware hot-cold separation(HC) which improves write throughput while maintaining low tail latency. RAIL leverages the internal parallelism of modern Flash devices and allocates data and parity pages to avoid reads getting stuck behind writes. We implement RAIL in the Linux Kernel as part of the LightNVM Flash translation layer and show that it can reduce read tail latency by 7× at the 99.99th …
