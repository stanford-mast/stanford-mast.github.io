---
title: 'The netflix challenge: Datacenter edition'
authors:
  - key: christinadelimitrou
  - key: christoskozyrakis
venue: archletters
year: 2012
date: 2012-06-01
doi: 10.1109/L-CA.2012.10
thumbnail: False
materials:
tags:
---
The hundreds of thousands of servers in modern warehouse-scale systems make performance and efficiency optimizations pressing design challenges. These systems are traditionally considered homogeneous. However, that is not typically the case. Multiple server generations compose a heterogeneous environment, whose performance opportunities have not been fully explored since techniques that account for platform heterogeneity typically do not scale to the tens of thousands of applications hosted in large-scale cloud providers. We present ADSM, a scalable and efficient recommendation system for application-to-server mapping in large-scale datacenters (DCs) that is QoS-aware. ADSM overcomes the drawbacks of previous techniques, by leveraging robust and computationally efficient analytical methods to scale to tens of thousands of applications with minimal overheads. It is also QoS-aware, mapping applications to platforms while enforcing strict QoS guarantees. ADSM is derived from validated analytical models, has low and bounded prediction errors, is simple to implement and scales to thousands of applications without significant changes to the system. Over 390 real DC workloads, ADSM improves performance by 16% on average and up to 2.5x and efficiency by 22% in a DC with 10 different server configurations.
