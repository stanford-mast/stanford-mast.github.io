---
title: 'Towards energy proportionality for large-scale latency-critical workloads'
authors:
  - key: davidlo
  - name: Liqun Cheng
    affiliation: Google
  - name: Rama Govindaraju
    affiliation: Google
  - name: Luiz André Barroso
    affiliation: Google
  - key: christoskozyrakis
venue: isca
year: 2014
date: 2014-06-01
doi: 10.1109/ISCA.2014.6853237
thumbnail: False
materials:
tags:
---
Reducing the energy footprint of warehouse-scale computer (WSC) systems is key to their affordability, yet difficult to achieve in practice. The lack of energy proportionality of typical WSC hardware and the fact that important workloads (such as search) require all servers to remain up regardless of traffic intensity renders existing power management techniques ineffective at reducing WSC energy use. We present PEGASUS, a feedback-based controller that significantly improves the energy proportionality of WSC systems, as demonstrated by a real implementation in a Google search cluster. PEGASUS uses request latency statistics to dynamically adjust server power management limits in a fine-grain manner, running each server just fast enough to meet global service-level latency objectives. In large cluster experiments, PEGASUS reduces power consumption by up to 20%. We also estimate that a distributed version of PEGASUS can nearly double these savings.
