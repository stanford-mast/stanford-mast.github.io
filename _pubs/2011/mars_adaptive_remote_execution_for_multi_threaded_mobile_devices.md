---
title: 'MARS: adaptive remote execution for multi-threaded mobile devices'
authors:
  - name: Asaf Cidon
    affiliation: Stanford
  - name: Tomer M London
    affiliation: Stanford
  - name: Sachin Katti
    affiliation: Stanford
  - key: christoskozyrakis
  - name: Mendel Rosenblum
    affiliation: Stanford
venue: mobiheld
year: 2011
date: 2011-10-01
doi: 10.1145/2043106.2043107
thumbnail: False
materials:
tags:
---
Mobile devices face a growing demand to support computationally intensive applications like 3D graphics and computer vision. However, these devices are inherently limited by processor power density and device battery life. Dynamic remote execution addresses this problem, by enabling mobile devices to opportunistically offload computations to a remote server. We envision remote execution as a new type of cloud-based heterogeneous computing resource, or a "Cloud-on-Chip", which would be managed as a system resource as if it were a local CPU, with a highly variable wireless interconnect. To realize this vision, we introduce MARS, the first adaptive, online and lightweight RPC-based remote execution scheduler supporting multi-threaded and multi-core systems. MARS uses a novel efficient offloading decision algorithm that takes into account the inherent trade-offs between communication and computation delays and power consumption. Due to its lightweight design, MARS runs on the device itself, instantly adapts its decisions to changing wireless resources, and supports any number of threads and cores. We evaluated MARS using a trace-based simulator driven by real world measurements on augmented reality, face recognition and video game applications. MARS achieves an average speedup of 57% and 33% higher energy savings over the best static client-server partitions.
