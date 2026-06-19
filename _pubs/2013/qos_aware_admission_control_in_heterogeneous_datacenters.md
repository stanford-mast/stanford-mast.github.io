---
title: 'QoS-Aware Admission Control in Heterogeneous Datacenters'
authors:
  - key: christinadelimitrou
  - name: Nick Bambos
  - key: christoskozyrakis
venue: icac
year: 2013
date: 2013-06-01
doi:
thumbnail: False
materials:
  - name: USENIX
    url: https://www.usenix.org/conference/icac13/technical-sessions/presentation/delimitrou
    type: file-alt
tags:
  - cloud
  - datacenter-systems
  - resource-management
---
Large-scale datacenters (DCs) host tens of thousands of diverse applications each day. Apart from determining where to schedule workloads, the cluster manager should also decide when to constrain application admission to prevent system oversubscription. At the same time datacenter users care not only for fast execution time but for low waiting time (fast scheduling) as well. Recent work has addressed the first challenge in the presence of unknown workloads, but not the second one.

We present ARQ, a multi-class admission control protocol that leverages Paragon, a heterogeneity and interference-aware DC scheduler. ARQ divides applications in classes based on the quality of resources they need and queues them separately. This improves utilization and system throughput, while maintaining per-application QoS. To enforce timely scheduling, ARQ diverges workloads to a queue of lower resource quality, if no suitable server becomes available within the time window specified by its QoS.

In an oversubscribed scenario with 8,500 applications on 1,000 EC2 servers, ARQ bounds performance degradation to less than 10% for 99% of workloads, while significantly improving utilization.
