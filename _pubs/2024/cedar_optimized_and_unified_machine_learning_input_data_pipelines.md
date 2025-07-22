---
title: 'cedar: Optimized and Unified Machine Learning Input Data Pipelines'
authors:
  - key: markzhao
  - name: Emanuel Adamiak
    affiliation: Stanford
  - key: christoskozyrakis
venue: vldb
year: 2024
date: 2024-10-01
doi: 10.14778/3705829.3705861
thumbnail: False
materials:
tags:
---
The input data pipeline is an essential component of each machine learning (ML) training job. It is responsible for reading massive amounts of training data, processing batches of samples using complex transformations, and loading them onto training nodes at low latency and high throughput. Performant input data systems are becoming increasingly critical, driven by skyrocketing data volumes and training throughput demands. Unfortunately, current input data systems cannot fully leverage key performance optimizations, resulting in hugely inefficient infrastructures that require significant resources - or worse - underutilize expensive accelerators. To address these demands, we present cedar, an optimized and unified programming framework for ML input data pipelines. cedar allows users to define input data pipelines using composable operators that support arbitrary ML frameworks and libraries. cedar introduces an extensible optimizer that systematically applies a complex combination of optimizations (e.g., offloading, caching, prefetching, fusion, and reordering). It orchestrates processing across a customizable set of local and distributed compute resources in order to improve processing performance and efficiency, all without user input. Across eight pipelines, cedar improves performance by up to 1.87x to 10.65x compared to state-of-the-art input data systems.
