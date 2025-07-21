---
title: 'Apiary: A dbms-backed transactional function-as-a-service framework'
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
  - name: Nathan W Weckwerth
  - name: Brian S Xia
  - name: Peter Bailis
  - name: Michael J Cafarella
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
date: 2022-01-01
doi: 
thumbnail: False
materials:
tags:
---
Developers increasingly use function-as-a-service (FaaS) platforms for data-centric applications that perform low-latency and transactional operations on data, such as for microservices or web serving. Unfortunately, existing FaaS platforms support these applications poorly because they physically and logically separate application logic, executed in cloud functions, from data management, done in interactive transactions accessing remote storage. Physical separation harms performance while logical separation complicates efficiently providing transactional guarantees and fault tolerance. This paper introduces Apiary, a novel DBMS-integrated FaaS platform for deploying and composing fault-tolerant transactional functions. Apiary physically co-locates and logically integrates function execution and data management by wrapping a distributed DBMS engine and using it as a unified runtime for function execution …
