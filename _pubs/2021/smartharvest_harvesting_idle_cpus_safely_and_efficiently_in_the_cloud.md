---
title: 'Smartharvest: Harvesting idle cpus safely and efficiently in the cloud'
authors:
  - key: yawenwang
  - name: Kapil Arya
  - name: Marios Kogias
  - name: Manohar Vanga
  - name: Aditya Bhandari
  - name: Neeraja J Yadwadkar
    affiliation: Stanford
  - name: Siddhartha Sen
  - name: Sameh Elnikety
  - key: christoskozyrakis
  - name: Ricardo Bianchini
venue: eurosys
year: 2021
date: 2021-04-01
doi: 10.1145/3447786.3456225
thumbnail: False
materials:
tags:
---
We can increase the efficiency of public cloud datacenters by harvesting allocated but temporarily idling CPU cores from customer virtual machines (VMs) to run batch or analytics workloads. Even small efficiency gains translate into substantial savings, since provisioning and operating a datacenter costs hundreds of millions of dollars per year. The main challenge is to harvest idle cores with little or no impact on customer VMs, which could be running latency-sensitive services and are essentially black-boxes to the cloud provider.We introduce ElasticVM, a new VM type that can run batch workloads cheaply using mainly harvested cores. We also propose SmartHarvest, a system that dynamically manages the number of cores available to ElasticVMs in each fine-grained time window. SmartHarvest uses online learning to predict the core demand of primary, customer VMs and compute the number of cores that can …
