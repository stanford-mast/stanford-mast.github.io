---
title: 'Quality-of-service-aware scheduling in heterogeneous data centers with paragon'
authors:
  - key: christinadelimitrou
  - key: christoskozyrakis
venue: tocs
year: 2014
date: 2013-12-20
doi: 10.1145/2556583
thumbnail: False
materials:
tags:
---
Large-scale datacenters (DCs) host tens of thousands of diverse applications each day. However, interference between colocated workloads and the difficulty of matching applications to one of the many hardware platforms available can degrade performance, violating the quality of service (QoS) guarantees that many cloud workloads require. While previous work has identified the impact of heterogeneity and interference, existing solutions are computationally intensive, cannot be applied online, and do not scale beyond a few applications.
We present Paragon, an online and scalable DC scheduler that is heterogeneity- and interference-aware. Paragon is derived from robust analytical methods, and instead of profiling each application in detail, it leverages information the system already has about applications it has previously seen. It uses collaborative filtering techniques to quickly and accurately classify an unknown incoming workload with respect to heterogeneity and interference in multiple shared resources. It does so by identifying similarities to previously scheduled applications. The classification allows Paragon to greedily schedule applications in a manner that minimizes interference and maximizes server utilization. After the initial application placement, Paragon monitors application behavior and adjusts the scheduling decisions at runtime to avoid performance degradations. Additionally, we design ARQ, a multiclass admission control protocol that constrains application waiting time. ARQ queues applications in separate classes based on the type of resources they need and avoids long queueing delays for easy-to-satisfy workloads in highly-loaded scenarios. Paragon scales to tens of thousands of servers and applications with marginal scheduling overheads in terms of time or state.
We evaluate Paragon with a wide range of workload scenarios, on both small and large-scale systems, including 1,000 servers on EC2. For a 2,500-workload scenario, Paragon enforces performance guarantees for 91% of applications, while significantly improving utilization. In comparison, heterogeneity-oblivious, interference-oblivious, and least-loaded schedulers only provide similar guarantees for 14%, 11%, and 3% of workloads. The differences are more striking in oversubscribed scenarios where resource efficiency is more critical.
