---
title: 'A polystore based database operating system (DBOS)'
authors:
  - name: Michael Cafarella
  - name: David DeWitt
  - name: Vijay Gadepally
  - name: Jeremy Kepner
  - key: christoskozyrakis
  - name: Tim Kraska
    affiliation: MIT
  - name: Michael Stonebraker
    affiliation: MIT
  - name: Matei Zaharia
    affiliation: UC Berkeley
venue: vldbworkshop
year: 2020
date: 2020-08-01
doi: 10.1007/978-3-030-71055-2_1
thumbnail: True
materials:
tags:
---
Current operating systems are complex systems that were designed before today’s computing environments. This makes it difficult for them to meet the scalability, heterogeneity, availability, and security challenges in current cloud and parallel computing environments. To address these problems, we propose a radically new OS design based ondata-centric architecture: all operating system state should be represented uniformly as database tables, and operations on this state should be made via queries from otherwise stateless tasks. This design makes it easy to scale and evolve the OS without whole-system refactoring, inspect and debug system state, upgrade components without downtime, manage decisions using machine learning, and implement sophisticated security features. We discuss how a database OS (DBOS) can improve the programmability and performance of many of today’s most important …
