---
title: 'Understanding data storage and ingestion for large-scale deep recommendation model training: Industrial product'
authors:
  - key: markzhao
  - name: Niket Agarwal
  - name: Aarti Basant
  - name: Buğra Gedik
  - name: Satadru Pan
  - name: Mustafa Ozdal
  - name: Rakesh Komuravelli
  - name: Jerry Pan
  - name: Tianshu Bao
  - name: Haowei Lu
  - name: Sundaram Narayanan
  - name: Jack Langman
  - name: Kevin Wilfong
  - name: Harsha Rastogi
  - name: Carole-Jean Wu
  - key: christoskozyrakis
  - name: Parik Pol
venue: isca
year: 2022
date: 2022-06-01
doi: 10.1145/3470496.3533044
thumbnail: False
materials:
tags:
---
Datacenter-scale AI training clusters consisting of thousands of domain-specific accelerators (DSA) are used to train increasingly-complex deep learning models. These clusters rely on a data storage and ingestion (DSI) pipeline, responsible for storing exabytes of training data and serving it at tens of terabytes per second. As DSAs continue to push training efficiency and throughput, the DSI pipeline is becoming the dominating factor that constrains the overall training performance and capacity. Innovations that improve the efficiency and performance of DSI systems and hardware are urgent, demanding a deep understanding of DSI characteristics and infrastructure at scale.This paper presents Meta's end-to-end DSI pipeline, composed of a central data warehouse built on distributed storage and a Data PreProcessing Service that scales to eliminate data stalls. We characterize how hundreds of models are …
