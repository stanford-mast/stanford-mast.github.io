---
title: 'ECHO: Recreating network traffic maps for datacenters with tens of thousands of servers'
authors:
  - key: christinadelimitrou
  - name: Sriram Sankar
    affiliation: Microsoft
  - name: Aman Kansal
    affiliation: Microsoft
  - key: christoskozyrakis
venue: iiswc
year: 2012
date: 2012-04-01
doi: 10.1109/IISWC.2012.6402896
thumbnail: False
materials:
tags:
---
Large-scale datacenters now host a large part of the world's data and computation, which makes their design a crucial architectural challenge. Datacenter (DC) applications, unlike traditional workloads, are dominated by user patterns that only emerge in the large-scale. This creates the need for concise, accurate and scalable analytical models that capture both their temporal and spatial features and can be used to create representative activity patterns. Unfortunately, previous work lacks the ability to track the complex patterns that are present in these applications, or scales poorly with the size of the system. In this work, we focus on the network aspect of datacenter workloads. We present ECHO, a scalable and accurate modeling scheme that uses hierarchical Markov Chains to capture the network activity of large-scale applications in time and space. ECHO can also use these models to re-create representative network traffic patterns. We validate the model against real DC-scale applications, such as Websearch and show marginal deviations between original and generated workloads. We verify that ECHO captures all the critical features of DC workloads, such as the locality of communication and burstiness and evaluate the granularity necessary for this. Finally we perform a detailed characterization of the network traffic for workloads in DCs of tens of thousands of servers over significant time frames.


