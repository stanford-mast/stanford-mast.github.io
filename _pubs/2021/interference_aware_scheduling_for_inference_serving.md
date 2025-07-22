---
title: 'Interference-aware scheduling for inference serving'
authors:
  - key: danielmendoza
  - key: frankyromero
  - key: qianli
  - key: neerajadwadkar
  - key: christoskozyrakis
venue: euromlsys
year: 2021
date: 2021-04-01
doi: 10.1145/3437984.3458837
thumbnail: False
materials:
tags:
---
Machine learning inference applications have proliferated through diverse domains such as healthcare, security, and analytics. Recent work has proposed inference serving systems for improving the deployment and scalability of models. To improve resource utilization, multiple models can be co-located on the same backend machine. However, co-location can cause latency degradation due to interference and can subsequently violate latency requirements. Although interference-aware schedulers for general workloads have been introduced, they do not scale appropriately to heterogeneous inference serving systems where the number of co-location configurations grows exponentially with the number of models and machine types.This paper proposes an interference-aware scheduler for heterogeneous inference serving systems, reducing the latency degradation from co-location interference. We characterize …
