---
title: 'RecD: Deduplication for end-to-end deep learning recommendation model training infrastructure'
authors:
  - key: markzhao
  - name: Dhruv Choudhary
  - name: Devashish Tyagi
  - name: Ajay Somani
  - name: Max Kaplan
  - name: Sung-Han Lin
  - name: Sarunya Pumma
  - name: Jongsoo Park
  - name: Aarti Basant
  - name: Niket Agarwal
  - name: Carole-Jean Wu
  - key: christoskozyrakis
venue: mlsys
year: 2023
date: 2023-03-01
doi: 10.48550/arXiv.2211.05239
thumbnail: False
materials:
tags:
---
We present RecD (Recommendation Deduplication), a suite of end-to-end infrastructure optimizations across the Deep Learning Recommendation Model (DLRM) training pipeline. RecD addresses immense storage, preprocessing, and training overheads caused by feature duplication inherent in industry-scale DLRM training datasets. Feature duplication arises because DLRM datasets are generated from interactions. While each user session can generate multiple training samples, many features’ values do not change across these samples. We demonstrate how RecD exploits this property, end-to-end, across a deployed training pipeline. RecD optimizes data generation pipelines to decrease dataset storage and preprocessing resource demands and to maximize duplication within a training batch. RecD introduces a new tensor format, InverseKeyedJaggedTensors (IKJTs), to deduplicate feature values in each batch. We show how DLRM model architectures can leverage IKJTs to drastically increase training throughput. RecD improves the training and preprocessing throughput and storage efficiency by up to 2.48×, 1.79×, and 3.71×, respectively, in an industry-scale DLRM training system.
