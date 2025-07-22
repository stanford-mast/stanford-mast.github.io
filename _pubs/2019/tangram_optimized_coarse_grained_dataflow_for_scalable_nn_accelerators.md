---
title: 'Tangram: Optimized coarse-grained dataflow for scalable nn accelerators'
authors:
  - key: mingyugao
  - name: Xuan Yang
  - name: Jing Pu
  - name: Mark Horowitz
    affiliation: Stanford
  - key: christoskozyrakis
venue: asplos
year: 2019
date: 2019-04-01
doi: 10.1145/3297858.3304014
thumbnail: False
materials:
tags:
---
The use of increasingly larger and more complex neural networks (NNs) makes it critical to scale the capabilities and efficiency of NN accelerators. Tiled architectures provide an intuitive scaling solution that supports both coarse-grained parallelism in NNs: intra-layer parallelism, where all tiles process a single layer, and inter-layer pipelining, where multiple layers execute across tiles in a pipelined manner. This work proposes dataflow optimizations to address the shortcomings of existing parallel dataflow techniques for tiled NN accelerators. For intra-layer parallelism, we develop buffer sharing dataflow that turns the distributed buffers into an idealized shared buffer, eliminating excessive data duplication and the memory access overheads. For inter-layer pipelining, we develop alternate layer loop ordering that forwards the intermediate data in a more fine-grained and timely manner, reducing the buffer …
