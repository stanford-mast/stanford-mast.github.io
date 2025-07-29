---
title: 'From chaos to QoS: case studies in CMP resource management'
authors:
  - name: Fei Guo
  - key: harikannan
  - name: Li Zhao
  - name: Ramesh Illikkal
  - name: Ravi Iyer
  - name: Don Newell
  - name: Yan Solihin
  - key: christoskozyrakis
venue: sigarchnews
year: 2007
date: 2007-03-01
doi: 10.1145/1241601.1241608
thumbnail: False
materials:
tags:
---
As more and more cores are enabled on the die of future CMP platforms, we expect that several diverse workloads will run simultaneously on the platform. A key example of this trend is the growth of virtualization usage models. When multiple virtual machines or applications or threads run simultaneously, the quality of service (QoS) that the platform provides to each individual thread is non-deterministic today. This occurs because the simultaneously running threads place very different demands on the shared resources (cache space, memory bandwidth, etc) in the platform and in most cases contend with each other. In this paper, we first present case studies that show how this results in non-deterministic performance. Unlike the compute resources managed through scheduling, platform resource allocation to individual threads cannot be controlled today. In order to provide better determinism and QoS, we then examine resource management mechanisms and present QoS-aware architectures and execution environments. The main contribution of this paper is the architecture feasibility analysis through prototypes that allow experimentation with QoS-Aware execution environments and architectural resources. We describe these QoS prototypes and then present preliminary case studies of multi-tasking and virtualization usage models sharing one critical CMP resource (last-level cache). We then demonstrate how proper management of the cache resource can provide service differentiation and deterministic performance behavior when running disparate workloads in future CMP platforms.
