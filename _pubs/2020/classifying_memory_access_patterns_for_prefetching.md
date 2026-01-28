---
title: 'Classifying memory access patterns for prefetching'
authors:
  - key: grantayers
  - key: heinerlitz
  - key: christoskozyrakis
  - name: Parthasarathy Ranganathan
    affiliation: Google
venue: asplos
year: 2020
date: 2020-03-01
doi: 10.1145/3373376.3378498
thumbnail: True
materials:
tags:
---
Prefetching is a well-studied technique for addressing the memory access stall time of contemporary microprocessors. However, despite a large body of related work, the memory access behavior of applications is not well understood, and it remains difficult to predict whether a particular application will benefit from a given prefetcher technique. In this work we propose a novel methodology to classify the memory access patterns of applications, enabling well-informed reasoning about the applicability of a certain prefetcher. Our approach leverages instruction dataflow information to uncover a wide range of access patterns, including arbitrary combinations of offsets and indirection. These combinations or prefetch kernels represent reuse, strides, reference locality, and complex address generation. By determining the complexity and frequency of these access patterns, we enable reasoning about prefetcher timeliness …
