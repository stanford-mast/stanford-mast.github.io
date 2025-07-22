---
title: 'Centralized core-granular scheduling for serverless functions'
authors:
  - key: kostiskaffes
  - key: neerajadwadkar
  - key: christoskozyrakis
venue: socc
year: 2019
date: 2019-11-01
doi: 10.1145/3357223.3362709
thumbnail: False
materials:
tags:
---
In recent years, many applications have started using serverless computing platforms primarily due to the ease of deployment and cost efficiency they offer. However, the existing scheduling mechanisms of serverless platforms fall short in catering to the unique characteristics of such applications: burstiness, short and variable execution times, statelessness and use of a single core. Specifically, the existing mechanisms fall short in meeting the requirements generated due to the combined effect of these characteristics: scheduling at a scale of millions of function invocations per second while achieving predictable performance.In this paper, we argue for a cluster-level centralized and core-granular scheduler for serverless functions. By maintaining a global view of the cluster resources, the centralized approach eliminates queue imbalances while the core granularity reduces interference; together these properties …
