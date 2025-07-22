---
title: 'Hermod: principled and practical scheduling for serverless functions'
authors:
  - key: kostiskaffes
  - key: neerajadwadkar
  - key: christoskozyrakis
venue: socc
year: 2022
date: 2022-11-01
doi: 10.1145/3542929.3563468
thumbnail: False
materials:
tags:
---
Serverless computing has seen rapid growth due to the ease-of-use and cost-efficiency it provides. However, function scheduling, a critical component of serverless systems, has been overlooked. In this paper, we take a fist-principles approach toward designing a scheduler that caters to the unique characteristics of serverless functions as seen in real-world deployments. We first create a taxonomy of scheduling policies along three dimensions. Next, we use simulation to explore the scheduling policy space and show that frequently used features such as late binding and random load balancing are sub-optimal for common execution time distributions and load ranges. We use these insights to design Hermod, a scheduler for serverless functions with two key characteristics. First, to avoid head-of-line blocking due to high function execution time variability, Hermod uses a combination of early binding and processor …
