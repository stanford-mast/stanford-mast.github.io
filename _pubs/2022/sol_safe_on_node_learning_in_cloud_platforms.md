---
title: 'SOL: Safe on-node learning in cloud platforms'
authors:
  - key: yawenwang
  - name: Daniel Crankshaw
  - name: Neeraja J Yadwadkar
    affiliation: Stanford
  - name: Daniel Berger
  - key: christoskozyrakis
  - name: Ricardo Bianchini
venue: preprint
year: 2022
date: 2022-02-01
doi: 
thumbnail: False
materials:
tags:
---
Cloud platforms run many software agents on each server node. These agents manage all aspects of node operation, and in some cases frequently collect data and make decisions. Unfortunately, their behavior is typically based on pre-defined static heuristics or offline analysis; they do not leverage on-node machine learning (ML). In this paper, we first characterize the spectrum of node agents in Azure, and identify the classes of agents that are most likely to benefit from on-node ML. We then propose SOL, an extensible framework for designing ML-based agents that are safe and robust to the range of failure conditions that occur in production. SOL provides a simple API to agent developers and manages the scheduling and running of the agent-specific functions they write. We illustrate the use of SOL by implementing three ML-based agents that manage CPU cores, node power, and memory placement. Our …
