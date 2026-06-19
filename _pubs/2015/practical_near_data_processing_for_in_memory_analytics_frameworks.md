---
title: 'Practical Near-Data Processing for In-Memory Analytics Frameworks'
authors:
  - key: mingyugao
  - key: grantayers
  - key: christoskozyrakis
venue: pact
year: 2015
date: 2015-10-01
doi: 10.1109/pact.2015.22
thumbnail: False
materials:
tags:
  - architecture
  - memory-storage
  - near-data-processing
  - accelerators
  - energy-efficiency
---
The end of Dennard scaling has made all systems energy-constrained. For data-intensive applications with limited temporal locality, the major energy bottleneck is data movement between processor chips and main memory modules. For such workloads, the best way to optimize energy is to place processing near the data in main memory. Advances in 3D integration provide an opportunity to implement near-data processing (NDP) without the technology problems that similar efforts had in the past. This paper develops the hardware and software of an NDP architecture for in-memory analytics frameworks, including MapReduce, graph processing, and deep neural networks. We develop simple but scalable hardware support for coherence, communication, and synchronization, and a runtime system that is sufficient to support analytics frameworks with complex data patterns while hiding all the details of the NDP hardware. Our NDP architecture provides up to 16x performance and energy advantage over conventional approaches, and 2.5x over recently-proposed NDP systems. We also investigate the balance between processing and memory throughput, as well as the scalability and physical and logical organization of the memory system. Finally, we show that it is critical to optimize software frameworks for spatial locality as it leads to 2.9x efficiency improvements for NDP.
