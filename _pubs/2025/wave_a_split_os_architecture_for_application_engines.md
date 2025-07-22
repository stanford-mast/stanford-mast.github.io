---
title: 'Wave: A Split OS Architecture for Application Engines'
authors:
  - name: Jack Tigar Humphries
    affiliation: Stanford
  - name: Neel Natu
  - key: kostiskaffes
  - name: Stanko Novakovic
  - name: Paul Turner
  - name: Hank Levy
  - name: David E Culler
  - key: christoskozyrakis
venue: preprint
year: 2025
date: 2025-01-01
doi: 10.48550/arXiv.2408.17351
thumbnail: False
materials:
tags:
---
The end of Moore's Law is driving cloud providers to offload virtualization and the network data plane to SmartNICs to improve compute efficiency. Even though individual OS control plane tasks consume up to 5% of cycles across the fleet, they remain on the host CPU because they are tightly intertwined with OS mechanisms. Moreover, offloading puts the slow PCIe interconnect in the critical path of OS decisions. We propose Tide, a new split OS architecture that separates OS control plane policies from mechanisms and offloads the control plane policies onto a SmartNIC. Tide has a new host-SmartNIC communication API, state synchronization mechanism, and communication mechanisms that overcome the PCIe bottleneck, even fors-scale workloads. Tide frees up host compute for applications and unlocks new optimization opportunities, including machine learning-driven policies, scheduling on the network I/O …
