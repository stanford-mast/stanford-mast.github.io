---
title: 'DBOS: A proposal for a data-centric operating system'
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
venue: vldb
year: 2020
date: 2020-07-01
doi: 10.14778/3485450.3485454
thumbnail: False
materials:
tags:
---
Current operating systems are complex systems that were designed before today's computing environments. This makes it difficult for them to meet the scalability, heterogeneity, availability, and security challenges in current cloud and parallel computing environments. To address these problems, we propose a radically new OS design based on data-centric architecture: all operating system state should be represented uniformly as database tables, and operations on this state should be made via queries from otherwise stateless tasks. This design makes it easy to scale and evolve the OS without whole-system refactoring, inspect and debug system state, upgrade components without downtime, manage decisions using machine learning, and implement sophisticated security features. We discuss how a database OS (DBOS) can improve the programmability and performance of many of today's most important applications and propose a plan for the development of a DBOS proof of concept.
