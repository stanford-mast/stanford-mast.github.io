---
title: 'Practical scheduling for real-world serverless computing'
authors:
  - key: kostiskaffes
  - name: Neeraja J Yadwadkar
    affiliation: Stanford
  - key: christoskozyrakis
venue: preprint
year: 2021
date: 2021-11-01
doi: 
thumbnail: False
materials:
tags:
---
Serverless computing has seen rapid growth due to the ease-of-use and cost-efficiency it provides. However, function scheduling, a critical component of serverless systems, has been overlooked. In this paper, we take a first-principles approach toward designing a scheduler that caters to the unique characteristics of serverless functions as seen in real-world deployments. We first create a taxonomy of scheduling policies along three dimensions. Next, we use simulation to explore the scheduling policy space for the function characteristics in a 14-day trace of Azure functions and conclude that frequently used features such as late binding and random load balancing are sub-optimal for common execution time distributions and load ranges. We use these insights to design Hermes, a scheduler for serverless functions with three key characteristics. First, to avoid head-of-line blocking due to high function execution time variability, Hermes uses a combination of early binding and processor sharing for scheduling at individual worker machines. Second, Hermes uses a hybrid load balancing approach that improves consolidation at low load while employing least-loaded balancing at high load to retain high performance. Third, Hermes is both load and locality-aware, reducing the number of cold starts compared to pure load-based policies. We implement Hermes for Apache OpenWhisk and demonstrate that, for the case of the function patterns observed both in the Azure and in other real-world traces, it achieves up to 85% lower function slowdown and 60% higher throughput compared to existing policies.
