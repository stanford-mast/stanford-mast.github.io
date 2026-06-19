---
title: 'AI Metropolis: Scaling Large Language Model-based Multi-Agent Simulation with Out-of-order Execution'
authors:
  - key: zhiqiangxie
  - name: Hao Kang
    affiliation: Georgia Tech
  - name: Ying Sheng
    affiliation: Stanford
  - name: Tushar Krishna
    affiliation: Georgia Tech
  - name: Kayvon Fatahalian
    affiliation: Stanford
  - key: christoskozyrakis
venue: mlsys
year: 2025
date: 2025-05-17
doi:
thumbnail: True
materials:
  - name: OpenReview
    url: https://openreview.net/forum?id=fsMImmI1TE
    type: file-alt
  - name: PDF
    url: https://openreview.net/pdf?id=fsMImmI1TE
    type: file-pdf
tags:
  - AI-systems
  - resource-management
  - energy-efficiency
---
With more advanced natural language understanding and reasoning capabilities, agents powered by large language models (LLMs) are increasingly developed in simulated environments to perform complex tasks, interact with other agents, and exhibit emerging behaviors relevant to social science research and innovative gameplay development. However, current multi-agent simulations frequently suffer from inefficiencies due to the limited parallelism caused by false dependencies, resulting in a performance bottleneck. In this paper, we introduce AI Metropolis, a simulation engine that improves the efficiency of LLM agent simulations by incorporating out-of-order execution scheduling. By dynamically tracking real dependencies between agents, AI Metropolis minimizes false dependencies, enhances parallelism, and maximizes hardware utilization. Our evaluations demonstrate that AI Metropolis achieves speedups from 1.3x to 4.15x over standard parallel simulation with global synchronization, approaching optimal performance as the number of agents increases.
