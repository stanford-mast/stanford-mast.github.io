---
title: 'Apiary: A DBMS-Integrated Transactional Function-as-a-Service Framework'
authors:
  - name: Peter Kraft
    affiliation: Stanford
  - key: qianli
  - key: kostiskaffes
  - key: athinagorasskiadopoulos
  - name: Deeptaanshu Kumar
  - name: Danny Cho
  - name: Jason Li
  - name: Robert Redmond
  - name: Nathan Weckwerth
  - name: Brian Xia
  - name: Peter Bailis
  - name: Michael Cafarella
  - name: Goetz Graefe
  - name: Jeremy Kepner
  - key: christoskozyrakis
  - name: Michael Stonebraker
    affiliation: MIT
  - name: Lalith Suresh
  - name: Xiangyao Yu
  - name: Matei Zaharia
    affiliation: UC Berkeley
venue: preprint
year: 2022
date: 2022-08-01
doi: 10.48550/arXiv.2208.13068
thumbnail: False
materials:
tags:
---
Developers increasingly use function-as-a-service (FaaS) platforms for data-centric applications that perform low-latency and transactional operations on data, such as for microservices or web serving. Unfortunately, existing FaaS platforms support these applications poorly because they physically and logically separate application logic, executed in cloud functions, from data management, done in interactive transactions accessing remote storage. Physical separation harms performance while logical separation complicates efficiently providing transactional guarantees and fault tolerance. This paper introduces Apiary, a novel DBMS-integrated FaaS platform for deploying and composing fault-tolerant transactional functions. Apiary physically co-locates and logically integrates function execution and data management by wrapping a distributed DBMS engine and using it as a unified runtime for function execution, data management, and operational logging, thus providing similar or stronger transactional guarantees as comparable systems while greatly improving performance and observability. To allow developers to write complex stateful programs, we leverage this integration to enable efficient and fault-tolerant function composition, building a frontend for orchestrating workflows of functions with the guarantees that each workflow runs to completion and each function in a workflow executes exactly once. We evaluate Apiary against research and production FaaS platforms and show it outperforms them by 2--68x on microservice workloads by reducing communication overhead.
