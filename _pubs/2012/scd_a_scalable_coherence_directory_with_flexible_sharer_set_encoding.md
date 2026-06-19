---
title: 'SCD: A scalable coherence directory with flexible sharer set encoding'
authors:
  - key: danielsanchez
  - key: christoskozyrakis
venue: hpca
year: 2012
date: 2012-02-01
doi: 10.1109/hpca.2012.6168950
thumbnail: False
materials:
tags:
  - architecture
  - memory-storage
  - energy-efficiency
---
Large-scale CMPs with hundreds of cores require a directory-based protocol to maintain cache coherence. However, previously proposed coherence directories are hard to scale beyond tens of cores, requiring either excessive area or energy, complex hierarchical protocols, or inexact representations of sharer sets that increase coherence traffic and degrade performance. We present SCD, a scalable coherence directory that relies on efficient highly-associative caches (such as zcaches) to implement a single-level directory that scales to thousands of cores, tracks sharer sets exactly, and incurs negligible directory-induced invalidations. SCD scales because, unlike conventional directories, it uses a variable number of directory tags to represent sharer sets: lines with one or few sharers use a single tag, while widely shared lines use additional tags, so tags remain small as the system scales up. We show that, thanks to the efficient highly-associative array it relies on, SCD can be fully characterized using analytical models, and can be sized to guarantee a negligible number of evictions independently of the workload. We evaluate SCD using simulations of a 1024-core CMP. For the same level of coverage, we find that SCD is 13× more area-efficient than full-map sparse directories, and 2× more area-efficient and faster than hierarchical directories, while requiring a simpler protocol. Furthermore, we show that SCD's analytical models are accurate in practice.
