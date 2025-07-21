---
title: 'R3: Record-Replay-Retroaction for Database-Backed Applications'
authors:
  - key: qianli
  - name: Peter Kraft
    affiliation: Stanford
  - name: Michael Cafarella
  - name: Çağatay Demiralp
  - name: Goetz Graefe
  - key: christoskozyrakis
  - name: Michael Stonebraker
    affiliation: MIT
  - name: Lalith Suresh
  - name: Xiangyao Yu
  - name: Matei Zaharia
    affiliation: UC Berkeley
venue: preprint
year: 2023
date: 2023-07-01
doi: 
thumbnail: False
materials:
tags:
---
Developers would benefit greatly from time travel: being able tofaithfully replaypast executions andretroactively executemodified code on past events. Currently, replay and retroaction are impractical because they require expensively capturing fine-grained timing information to reproduce concurrent accesses to shared state. In this paper, we propose practical time travel fordatabase-backed applications, an important class of distributed applications that access shared state through transactions.We present R3, a novel Record-Replay-Retroaction tool. R3implements a lightweight interceptor to record concurrency information for applications at transaction-level granularity, enabling replay and retroaction with minimal overhead. We address key challenges in both replay and retroaction. First, we design a novel algorithm for faithfully reproducing application requests running with snapshot isolation, allowing R3to …
