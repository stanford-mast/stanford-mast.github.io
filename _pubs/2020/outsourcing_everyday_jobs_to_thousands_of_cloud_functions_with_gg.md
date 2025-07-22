---
title: 'From laptop to lambda: outsourcing everyday jobs to thousands of transient functional containers'
authors:
  - name: Sadjad Fouladi
  - key: frankyromero
  - name: Dan Iter
  - key: qianli
  - name: Shuvo Chatterjee
  - key: christoskozyrakis
  - name: Matei Zaharia
    affiliation: UC Berkeley
  - name: Keith Winstein
    affiliation: Stanford
venue: atc
year: 2020
date: 2020-01-01
doi: 10.5555/3358807.3358848
thumbnail: False
materials:
tags:
---
We present gg, a framework and a set of command-line tools that helps people execute everyday applications--e.g., software compilation, unit tests, video encoding, or object recognition--using thousands of parallel threads on a cloud-functions service to achieve near-interactive completion times. In the future, instead of running these tasks on a laptop, or keeping a warm cluster running in the cloud, users might push a button that spawns 10,000 parallel cloud functions to execute a large job in a few seconds from start. gg is designed to make this practical and easy.

With gg, applications express a job as a composition of lightweight OS containers that are individually transient (lifetimes of 1-60 seconds) and functional (each container is hermetically sealed and deterministic). gg takes care of instantiating these containers on cloud functions, loading dependencies, minimizing data movement, moving data between containers, and dealing with failure and stragglers.

We ported several latency-sensitive applications to run on gg and evaluated its performance. In the best case, a distributed compiler built on gg outperformed a conventional tool (icecc) by 2-5×, without requiring a warm cluster running continuously. In the worst case, gg was within 20% of the hand-tuned performance of an existing tool for video encoding (ExCamera).
