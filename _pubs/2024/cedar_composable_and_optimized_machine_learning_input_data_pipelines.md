---
title: 'cedar: Composable and optimized machine learning input data pipelines'
authors:
  - key: markzhao
  - name: Emanuel Adamiak
  - key: christoskozyrakis
venue: preprint
year: 2024
date: 2024-01-01
doi: 
thumbnail: False
materials:
tags:
---
The input data pipeline is an essential component of each machine learning (ML) training job. It is responsible for reading massive amounts of training data, processing batches of samples using complex transformations, and loading them onto training nodes at low latency and high throughput. Performant input data systems are becoming increasingly critical, driven by skyrocketing data volumes and training throughput demands. Unfortunately, current input data systems cannot fully leverage key performance optimizations, resulting in hugely inefficient infrastructures that require significant resources -- or worse -- underutilize expensive accelerators. To address these demands, we present cedar, a programming model and framework that allows users to easily build, optimize, and execute input data pipelines. cedar presents an easy-to-use programming interface, allowing users to define input data pipelines using …
