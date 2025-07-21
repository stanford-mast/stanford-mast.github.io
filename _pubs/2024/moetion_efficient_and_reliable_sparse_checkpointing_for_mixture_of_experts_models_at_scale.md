---
title: 'MoEtion: Efficient and Reliable Sparse Checkpointing for Mixture-of-Experts Models at Scale'
authors:
  - key: swapnilgandhi
  - key: christoskozyrakis
venue: preprint
year: 2024
date: 2024-12-01
doi: 
thumbnail: False
materials:
tags:
---
As large language models continue to scale, training them requires thousands of GPUs over prolonged durations--making frequent failures an inevitable reality. While checkpointing remains the primary fault-tolerance mechanism, existing methods struggle to efficiently support Mixture-of-Experts (MoE) models. Due to the substantially larger training state of MoE models, traditional checkpointing techniques incur prohibitive overheads, resulting in frequent stalls or prolonged recovery periods that severely degrade training efficiency. We introduce MoEtion, a distributed, in-memory checkpointing system designed explicitly for MoE models. MoEtion builds on three key ideas: (1) sparse checkpointing, which incrementally checkpoints subsets of experts over multiple iterations, significantly reducing snapshot overhead; (2) a sparse-to-dense checkpoint conversion technique that incrementally reconstructs temporally consistent checkpoints from sparse snapshots; and (3) lightweight upstream logging activations and gradients at pipeline-stage boundaries to localize recovery of failed workers without redundant recomputation of unaffected workers. Evaluations across diverse MoE models with up to 64 experts demonstrate that MoEtion reduces checkpointing overhead by up toand recovery overhead by up tocompared to state-of-the-art approaches, achieving consistently high Effective Training Time Ratios (ETTR) of up to, even under frequent failures (MTBF as low as 20 minutes) without compromising synchronous training semantics. Overall, MoEtion offers a practical, scalable, and robust fault-tolerance solution for the next generation of …
