---
title: 'Wave: Offloading Resource Management to SmartNIC Cores'
authors:
  - key: jackhumphries
  - name: Neel Natu
    affiliation: Google
  - key: kostiskaffes
  - name: Stanko Novaković
    affiliation: Google
  - name: Paul Turner
    affiliation: Google
  - name: Henry M. Levy
    affiliation: Google
  - name: David Culler
    affiliation: Google
  - key: christoskozyrakis
venue: asplos
year: 2025
date: 2025-08-01
doi: 10.1145/3676642.3736113
thumbnail: True
materials:
tags:
  - OS
  - cloud
  - networking
  - datacenter-systems
  - resource-management
  - low-latency
  - accelerators
---
SmartNICs are increasingly deployed in datacenters to offload tasks from server CPUs, improving the efficiency and flexibility of datacenter security, networking and storage. Optimizing cloud server efficiency in this way is critically important to ensure that virtually all server resources are available to paying customers. Userspace system software, specifically, decision-making tasks performed by various operating system subsystems, is particularly well suited for execution on mid-tier SmartNIC ARM cores. To this end, we introduce Wave, a framework for offloading userspace system software to processes/agents running on the SmartNIC. Wave uses Linux userspace systems to better align system functionality with SmartNIC capabilities. It also introduces a new host-SmartNIC communication API that enables offloading of even μs-scale system software. To evaluate Wave, we offloaded preexisting userspace system software including kernel thread scheduling, memory management, and an RPC stack to SmartNIC ARM cores, which showed a performance degradation of 1.1%-7.4% in an apples-to-apples comparison with on-host implementations. Wave recovered host resources consumed by on-host system software for memory management (saving 16 host cores), RPCs (saving 8 host cores), and virtual machines (an 11.2% performance improvement). Wave highlights the potential for rethinking system software placement in modern datacenters, unlocking new opportunities for efficiency and scalability.
