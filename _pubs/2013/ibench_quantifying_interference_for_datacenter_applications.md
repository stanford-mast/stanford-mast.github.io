---
title: 'iBench: Quantifying interference for datacenter applications'
authors:
  - key: christinadelimitrou
  - key: christoskozyrakis
venue: iiswc
year: 2013
date: 2013-09-01
doi: 10.1109/iiswc.2013.6704667
thumbnail: False
materials:
tags:
  - cloud
  - datacenter-systems
  - resource-management
---
Interference between co-scheduled applications is one of the major reasons that causes modern datacenters (DCs) to operate at low utilization. DC operators traditionally side-step interference either by disallowing colocation altogether and providing isolated server instances, or by requiring the users to express resource reservations, which are often exaggerated to counter-balance the unpredictability in the quality of allocated resources. Understanding, reducing and managing interference can significantly impact the manner in which these large-scale systems operate. We present iBench, a novel workload suite that helps quantify the pressure different applications put in various shared resources, and similarly the pressure they can tolerate in these resources. iBench consists of a set of carefully-crafted benchmarks that induce interference of increasing intensity in resources that span the CPU, cache hierarchy, memory, storage and networking subsystems. We first validate the effect that iBench workloads have on performance against a wide spectrum of DC applications. Then, we use iBench to demonstrate the importance of considering interference in a set of challenging problems that range from DC scheduling and server provisioning, to resource-efficient application development and scheduling for heterogeneous CMPs. In all cases quantifying interference with iBench results in significant performance and/or efficiency improvements. We plan to release iBench under a free software license.
