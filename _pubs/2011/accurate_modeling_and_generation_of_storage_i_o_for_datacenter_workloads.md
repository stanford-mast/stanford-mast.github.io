---
title: 'Accurate modeling and generation of storage i/o for datacenter workloads'
authors:
  - key: christinadelimitrou
  - name: Sriram Sankar
  - name: Kushagra Vaid
  - key: christoskozyrakis
venue: tos
year: 2011
date: 2011-03-01
doi: 10.1145/2818716
thumbnail: False
materials:
tags:
---
Tools that confidently recreate I/O workloads have become a critical requirement in designing efficient storage systems for datacenters (DCs), since potential inefficiencies get aggregated over several thousand servers. Designing performance, power and cost optimized systems requires a deep understanding of target workloads, and mechanisms to effectively model different design choices. Traditional benchmarking is invalid in cloud data-stores, representative storage profiles are hard to obtain, while replaying the entire application in all storage configurations is impractical. Despite these issues, current workload generators are not comprehensive enough to accurately reproduce key aspects of real application patterns. Some of these features include spatial and temporal locality, as well as tuning the intensity of the workload to emulate different storage system behaviors. To address these limitations, we use a state diagram-based storage model, extend it to a hierarchical representation and implement a tool that consistently recreates I/O loads of DC applications. We present the design of the tool and the validation process performed against six original DC applications traces. We explore the practical applications of this methodology in two important storage challenges-1) SSD caching and 2) defragmentation benefits on enterprise storage. In both cases we observe significant storage speedup for most of the DC applications. Since knowledge of the workload’s spatial locality is necessary to model these use cases, our tool was instrumental in quantifying their performance benefits.
