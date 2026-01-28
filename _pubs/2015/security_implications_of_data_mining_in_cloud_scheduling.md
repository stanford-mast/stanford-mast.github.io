---
title: 'Security implications of data mining in cloud scheduling'
authors:
  - key: christinadelimitrou
  - key: christoskozyrakis
venue: archletters
year: 2015
date: 2015-07-01
doi: 10.1109/LCA.2015.2461215
thumbnail: True
materials:
tags:
---
Cloud providers host an increasing number of popular applications, on the premise of resource flexibility and cost efficiency. Most of these systems expose virtualized resources of different types and sizes. As instances share the same physical host to increase utilization, they contend on hardware resources, e.g., last-level cache, making them vulnerable to side-channel attacks from co-scheduled applications. In this work we show that using data mining techniques can help an adversarial user of the cloud determine the nature and characteristics of co-scheduled applications and negatively impact their performance through targeted contention injections. We design Bolt, a simple runtime that extracts the sensitivity of co-scheduled applications to various types of interference and uses this signal to determine the type of these applications by applying a set of data mining techniques. We validate the accuracy of Bolt on a 39-server cluster. Bolt correctly identifies the type and characteristics of 81 percent out of 108 victim applications, and constructs specialized contention signals that degrade their performance. We also use Bolt to find the most commonly-run applications on EC2. We hope that underlining such security vulnerabilities in modern cloud facilities will encourage cloud providers to introduce stronger resource isolation primitives in their systems.
