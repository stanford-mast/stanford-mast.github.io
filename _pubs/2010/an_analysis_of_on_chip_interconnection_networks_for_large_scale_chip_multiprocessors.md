---
title: 'An analysis of on-chip interconnection networks for large-scale chip multiprocessors'
authors:
  - key: danielsanchez
  - name: George Michelogiannakis
    affiliation: Stanford
  - key: christoskozyrakis
venue: taco
year: 2010
date: 2010-05-01
doi: 10.1145/1736065.1736069
thumbnail: False
materials:
tags:
---
With the number of cores of chip multiprocessors (CMPs) rapidly growing as technology scales down, connecting the different components of a CMP in a scalable and efficient way becomes increasingly challenging. In this article, we explore the architectural-level implications of interconnection network design for CMPs with up to 128 fine-grain multithreaded cores. We evaluate and compare different network topologies using accurate simulation of the full chip, including the memory hierarchy and interconnect, and using a diverse set of scientific and engineering workloads.
We find that the interconnect has a large impact on performance, as it is responsible for 60% to 75% of the miss latency. Latency, and not bandwidth, is the primary performance constraint, since, even with many threads per core and workloads with high miss rates, networks with enough bandwidth can be efficiently implemented for the system scales we consider. From the topologies we study, the flattened butterfly consistently outperforms the mesh and fat tree on all workloads, leading to performance advantages of up to 22%. We also show that considering interconnect and memory hierarchy together when designing large-scale CMPs is crucial, and neglecting either of the two can lead to incorrect conclusions. Finally, the effect of the interconnect on overall performance becomes more important as the number of cores increases, making interconnection choices especially critical when scaling up.
