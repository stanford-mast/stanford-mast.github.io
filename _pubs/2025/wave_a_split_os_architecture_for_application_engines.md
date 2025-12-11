---
title: 'Wave: A Split OS Architecture for Application Engines'
authors:
  - key: jackhumphries
  - name: Neel Natu
    affiliation: Google
  - key: kostiskaffes
  - name: Stanko Novakovic
    affiliation: Google
  - name: Paul Turner
    affiliation: Google
  - name: Hank Levy
    affiliation: Google
  - name: David E Culler
    affiliation: Google
  - key: christoskozyrakis
venue: asplos
year: 2025
date: 2025-08-06
doi: https://doi.org/10.1145/3676642.3736113
thumbnail: True
materials:
tags:
---
SmartNICs are increasingly deployed in datacenters to offload tasks from server CPUs, improving the efficiency and flexibility of datacenter security, networking and storage. Optimizing cloud server efficiency in this way is critically important to ensure that virtually all server resources are available to paying customers. Userspace system software, specifically, decision-making tasks performed by various operating system subsystems, is particularly well suited for execution on mid-tier SmartNIC ARM cores. To this end, we introduce Wave, a framework for offloading userspace system software to processes/agents running on the SmartNIC. Wave uses Linux userspace systems to better align system functionality with SmartNIC capabilities. It also introduces a new host-SmartNIC communication API that enables offloading of even μs-scale system software. To evaluate Wave, we offloaded preexisting userspace system software including kernel thread scheduling, memory management, and an RPC stack to SmartNIC ARM cores, which showed a performance degradation of 1.1%-7.4% in an apples-to-apples comparison with on-host implementations. Wave recovered host resources consumed by on-host system software for memory management (saving 16 host cores), RPCs (saving 8 host cores), and virtual machines (an 11.2% performance improvement). Wave highlights the potential for rethinking system software placement in modern datacenters, unlocking new opportunities for efficiency and scalability.
