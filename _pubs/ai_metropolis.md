---
title: 'AI Metropolis: Scaling Large Language Model-based Multi-Agent Simulation with Out-of-order Execution'
authors:
  - key: zhiqiangxie
  - name: Hao Kang
    affiliation: Georgia Institute of Technology
  - name: Ying Sheng
    affiliation: Stanford
  - name: Tushar Krishna
    affiliation: Georgia Institute of Technology
  - name: Kayvon Fatahalian
    affiliation: Stanford
  - key: christoskozyrakis
venue: mlsys
year: 2025
date: 2025-05-12
doi: 10.48550/arXiv.2411.03519
teaser: False
thumbnail: True
materials:
  - name: PDF
    url: https://arxiv.org/pdf/2411.03519
    type: file-pdf
tags:
  - AI efficiency
---
With more advanced natural language understanding and reasoning capabilities, large language model (LLM)-powered agents are increasingly developed in simulated environments to perform complex tasks, interact with other agents, and exhibit emergent behaviors relevant to social science and gaming. However, current multi-agent simulations frequently suffer from inefficiencies due to the limited parallelism caused by false dependencies, resulting in performance bottlenecks. In this paper, we introduce AI Metropolis, a simulation engine that improves the efficiency of LLM agent simulations by incorporating out-of-order execution scheduling. By dynamically tracking real dependencies between agents, AI Metropolis minimizes false dependencies, enhancing parallelism and enabling efficient hardware utilization. Our evaluations demonstrate that AI Metropolis achieves speedups from 1.3x to 4.15x over standard parallel simulation with global synchronization, approaching optimal performance as the number of agents increases.