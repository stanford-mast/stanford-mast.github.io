---
title: 'Decoupling datacenter studies from access to large-scale applications: A modeling approach for storage workloads'
authors:
  - key: christinadelimitrou
  - name: Sriram Sankar
    affiliation: Microsoft
  - name: Kushagra Vaid
    affiliation: Microsoft
  - key: christoskozyrakis
venue: iiswc
year: 2012
date: 2012-04-01
doi: 10.1109/IISWC.2011.6114196
thumbnail: False
materials:
tags:
---
The cost and power impact of suboptimal storage configurations is significant in datacenters (DCs) as inefficiencies are aggregated over several thousand servers and represent considerable losses in capital and operating costs. Designing performance, power and cost-optimized systems requires a deep understanding of target workloads, and mechanisms to effectively model different storage design choices. Traditional benchmarking is invalid in cloud data-stores, representative storage profiles are hard to obtain, while replaying the entire application in all storage configurations is impractical both from a cost and time perspective. Despite these issues, current workload generators are not able to accurately reproduce key aspects of real application patterns. Some of these features include spatial and temporal locality, as well as tuning the intensity of the workload to emulate different storage system configurations. To address these limitations, we propose a modeling and characterization framework for large-scale storage applications. As part of this framework we use a state diagram-based storage model, extend it to a hierarchical representation and implement a tool that consistently recreates I/O loads of DC applications. We present the principal features of the framework that allow accurate modeling and generation of storage workloads and the validation process performed against ten original DC applications traces. Furthermore, using our framework, we perform an in-depth, per-thread characterization of these applications and provide insights on their behavior. Finally, we explore two practical applications of this methodology: SSD caching and defragmentation benefits on enterprise storage. In both cases we observe significant speedup for most of the examined applications. Since knowledge of the workload's spatial and temporal locality is necessary to model these use cases, our framework was instrumental in quantifying their performance benefits. The proposed methodology provides a detailed understanding on the storage activity of large-scale applications and enables a wide spectrum of storage studies without the requirement for access to real applications and full application deployment.


