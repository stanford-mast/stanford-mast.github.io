---
title: 'Dynamic Fine-Grain Scheduling of Pipeline Parallelism'
authors:
  - key: danielsanchez
  - key: davidlo
  - key: richardyoo
  - name: Jeremy Sugerman
  - key: christoskozyrakis
venue: pact
year: 2011
date: 2011-10-01
doi: 10.1109/pact.2011.9
thumbnail: False
materials:
tags:
  - cloud
  - parallel-compute
  - resource-management
  - accelerators
---
Scheduling pipeline-parallel programs, defined as a graph of stages that communicate explicitly through queues, is challenging. When the application is regular and the underlying architecture can guarantee predictable execution times, several techniques exist to compute highly optimized static schedules. However, these schedules do not admit run-time load balancing, so variability introduced by the application or the underlying hardware causes load imbalance, hindering performance. On the other hand, existing schemes for dynamic fine-grain load balancing (such as task-stealing) do not work well on pipeline-parallel programs: they cannot guarantee memory footprint bounds, and do not adequately schedule complex graphs or graphs with ordered queues. We present a scheduler implementation for pipeline-parallel programs that performs fine-grain dynamic load balancing efficiently. Specifically, we implement the first real runtime for GRAMPS, a recently proposed programming model that focuses on supporting irregular pipeline and data-parallel applications (in contrast to classical stream programming models and schedulers, which require programs to be regular). Task-stealing with per-stage queues and queuing policies, coupled with a backpressure mechanism, allow us to maintain strict footprint bounds, and a buffer management scheme based on packet-stealing allows low-overhead and locality-aware dynamic allocation of queue data. We evaluate our runtime on a multi-core SMP and find that it provides low-overhead scheduling of irregular workloads while maintaining locality. We also show that the GRAMPS scheduler outperforms several other commonly used scheduling approaches. Specifically, while a typical task-stealing scheduler performs on par with GRAMPS on simple graphs, it does significantly worse on complex ones, a canonical GPGPU scheduler cannot exploit pipeline parallelism and suffers from large memory footprints, and a typical static, streaming scheduler achieves somewhat better locality, but suffers significant load imbalance on a general-purpose multi-core due to fine-grain architecture variability (e.g., cache misses and SMT).
