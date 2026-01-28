---
title: 'RAMBO: Resource allocation for microservices using Bayesian optimization'
authors:
  - key: qianli
  - name: Bin Li
  - name: Pietro Mercati
  - name: Ramesh Illikkal
  - name: Charlie Tai
  - name: Michael Kishinevsky
  - key: christoskozyrakis
venue: archletters
year: 2021
date: 2021-03-01
doi: 10.1109/LCA.2021.3066142
thumbnail: True
materials:
tags:
---
Microservices are becoming the defining paradigm of cloud applications, which raises urgent challenges for efficient datacenter management. Guaranteeing end-to-end Service Level Agreement (SLA) while optimizing resource allocation is critical to both cloud service providers and users. However, one application may contain hundreds of microservices, which constitute an enormous search space that is unfeasible to explore exhaustively. Thus, we propose RAMBO, an SLA-aware framework for microservices that leverages multi-objective Bayesian Optimization (BO) to allocate resources and meet performance/cost goals. Experiments conducted on a real microservice workload demonstrate that RAMBO can correctly characterize each microservice and efficiently discover Pareto-optimal solutions. We envision that the proposed methodology and results will benefit future resource planning, cluster orchestration …
