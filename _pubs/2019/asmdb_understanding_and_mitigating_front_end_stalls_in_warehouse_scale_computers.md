---
title: 'AsmDB: understanding and mitigating front-end stalls in warehouse-scale computers'
authors:
  - key: grantayers
  - name: Nayana Prasad Nagendra
  - name: David I August
  - name: Hyoun Kyu Cho
  - name: Svilen Kanev
  - key: christoskozyrakis
  - name: Trivikram Krishnamurthy
  - key: heinerlitz
  - name: Tipp Moseley
  - name: Parthasarathy Ranganathan
    affiliation: Google
venue: isca
year: 2019
date: 2019-06-01
doi: 10.1145/3307650.3322234
thumbnail: True
materials:
tags:
  - architecture
  - cloud
  - datacenter-systems
---
It is well known that the datacenters hosting today's cloud services waste a significant number of cycles on front-end stalls. However, prior work has provided little insights about the source of these front-end stalls and how to address them. This work analyzes the cause of instruction cache misses at a fleet-wide scale and proposes a new compiler-driven software code prefetching strategy to reduce instruction caches misses by 90%.
