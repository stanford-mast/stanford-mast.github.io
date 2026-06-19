---
title: 'Understanding Ephemeral Storage for Serverless Analytics'
authors:
  - key: anaklimovic
  - key: yawenwang
  - key: christoskozyrakis
  - name: Patrick Stuedi
  - name: Jonas Pfefferle
  - name: Animesh Trivedi
venue: atc
year: 2018
date: 2018-07-01
doi:
thumbnail: True
materials:
  - name: USENIX
    url: https://www.usenix.org/conference/atc18/presentation/klimovic-serverless
    type: file-alt
tags:
  - cloud
  - memory-storage
  - datacenter-systems
  - serverless
---
Serverless computing frameworks allow users to launch thousands of concurrent tasks with high elasticity and fine-grain resource billing without explicitly managing computing resources. While already successful for IoT and web microservices, there is increasing interest in leveraging serverless computing to run data-intensive jobs, such as interactive analytics. A key challenge in running analytics workloads on serverless platforms is enabling tasks in different execution stages to efficiently communicate data between each other via a shared data store. In this paper, we explore the suitability of different cloud storage services (e.g., object stores and distributed caches) as remote storage for serverless analytics. Our analysis leads to key insights to guide the design of an ephemeral cloud storage system, including the performance and cost efficiency of Flash storage for serverless application requirements and the need for a pay-what-you-use storage service that can support the high throughput demands of highly parallel applications.
