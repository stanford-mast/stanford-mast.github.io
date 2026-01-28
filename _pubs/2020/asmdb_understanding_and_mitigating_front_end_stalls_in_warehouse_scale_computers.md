---
title: 'Asmdb: Understanding and mitigating front-end stalls in warehouse-scale computers'
authors:
  - name: Nayana Prasad Nagendra
  - key: grantayers
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
year: 2020
date: 2020-04-01
doi: 10.1145/3307650.3322234
thumbnail: True
materials:
tags:
---
It is well known that the datacenters hosting today's cloud services waste a significant number of cycles on front-end stalls. However, prior work has provided little insights about the source of these front-end stalls and how to address them. This work analyzes the cause of instruction cache misses at a fleet-wide scale and proposes a new compiler-driven software code prefetching strategy to reduce instruction caches misses by 90%.
