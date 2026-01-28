---
title: 'Leveraging application classes to save power in highly-utilized data centers'
authors:
  - key: kostiskaffes
  - name: Dragos Sbirlea
  - name: Yiyan Lin
  - key: davidlo
  - key: christoskozyrakis
venue: socc
year: 2020
date: 2020-10-01
doi: 10.1145/3419111.3421274
thumbnail: True
materials:
tags:
---
Data center energy consumption has become an increasingly significant contributor both to greenhouse emissions and costs. To increase utilization of individual hosts and improve efficiency, most modern data centers co-locate workloads belonging to different application classes, some being latency-sensitive (LS) and others best-effort (BE) which are more tolerant to performance variation. It is therefore necessary to design mechanisms that reduce power consumption even in the resulting high-utilization environment, while preserving LS task performance. Moreover, the abundance of different workloads and the security implications of public cloud make mechanisms that rely on extensive knowledge of workload characteristics or on application-exported metrics challenging to deploy.We present PACT, Per Application Class Turbo Controller, a system that leverages two novel mechanisms to reduce power …
