---
title: 'Tarcil: High quality and low latency scheduling in large, shared clusters'
authors:
  - key: christinadelimitrou
  - key: danielsanchez
  - key: christoskozyrakis
venue: socc
year: 2015
date: 2015-01-01
doi: 10.1145/2806777.2806779
thumbnail: False
materials:
tags:
---
Scheduling diverse applications in large, shared clusters is particularly challenging. Recent research on cluster management focuses either on scheduling speed, using sampling techniques to quickly assign tasks to resources, or on scheduling quality, using centralized algorithms that examine the cluster state to find the most suitable resources that improve both task performance and cluster utilization. We present Tarcil, a distributed scheduler that targets both scheduling speed and quality, making it appropriate for large, highly-loaded clusters running both short and long jobs. Tarcil uses an analytically derived sampling framework that dynamically adjusts the sample size based on load and provides guarantees on the quality of scheduling decisions with respect to resource heterogeneity and workload interference. It also implements admission control when sampling is unlikely to find suitable resources for a task. We evaluate Tarcil on clusters with hundreds of servers on EC2. For highly-loaded clusters running short jobs, Tarcil improves task execution time by 41% over a distributed, sampling-based scheduler. For more general workload scenarios, Tarcil increases the fraction of tasks that achieve near ideal performance by 4x and 2x compared to sampling-based and centralized scheduling respectively.
