---
title: 'Llama: A heterogeneous & serverless framework for auto-tuning video analytics pipelines'
authors:
  - key: frankyromero
  - key: markzhao
  - name: Neeraja J Yadwadkar
    affiliation: Stanford
  - key: christoskozyrakis
venue: preprint
year: 2021
date: 2021-11-01
doi: 
thumbnail: False
materials:
tags:
---
The proliferation of camera-enabled devices and large video repositories has led to a diverse set of video analytics applications. These applications rely on video pipelines, represented as DAGs of operations, to transform videos, process extracted metadata, and answer questions like, "Is this intersection congested?" The latency and resource efficiency of pipelines can be optimized using configurable knobs for each operation (e.g., sampling rate, batch size, or type of hardware used). However, determining efficient configurations is challenging because (a) the configuration search space is exponentially large, and (b) the optimal configuration depends on users' desired latency and cost targets, (c) input video contents may exercise different paths in the DAG and produce a variable amount intermediate results. Existing video analytics and processing systems leave it to the users to manually configure operations and …
