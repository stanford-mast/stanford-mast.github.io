---
title: 'VIVA: An End-to-End System for Interactive Video Analytics'
authors:
  - name: Daniel Kang
  - name: Francisco Romero
  - name: Peter Bailis
  - key: christoskozyrakis
  - name: Matei Zaharia
venue: cidr
year: 2022
date: 2022-01-09
doi:
thumbnail: False
materials:
  - name: Paper
    url: https://vldb.org/cidrdb/papers/2022/p75-kang.pdf
    type: file-alt
tags:
  - databases
  - AI-systems
  - accelerators
  - video-analytics
---
The growth of video volumes and increased DNN capabilities has led to a growing desire for video analytics. In response, the data analytics community has proposed multiple systems that optimize specific query types (e.g., selection queries) or a particular step in query execution (e.g., video retrieval from storage).

However, none of these systems provide end-to-end, practical video analytics for users to iteratively and interactively engage with queries, as is the case with analytics systems for structured data. In response, we are building VIVA: an end-to-end system for interactive video analytics. VIVA contains five novel components.

First, VIVA uses relational hints, which allow users to express relationships between columns that are difficult to automatically infer (e.g., mentions of a person in a transcript can be used as a proxy for the person appearing in the video). Second, VIVA introduces a mixed-data query optimizer that optimizes queries across both structured and unstructured data. Third, VIVA features an embedding cache that decides which results/embeddings to store for future queries.

Finally, VIVA co-optimizes storage and query execution with its video file manager and accelerator-based execution engine. The former decides how to pre-fetch/manage video, while the latter selects and manages heterogeneous hardware backends spanning the growing number of DNN accelerators. We describe the challenges and design requirements for VIVA's development and outline ongoing and future work for realizing VIVA.
