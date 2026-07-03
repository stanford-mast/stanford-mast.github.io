---
title: 'Convolution Engine: Balancing Efficiency and Flexibility in Specialized Computing'
authors:
  - name: Wajahat Qadeer
  - key: rehanhameed
  - name: Ofer Shacham
  - name: Preethi Venkatesan
  - key: christoskozyrakis
  - name: Mark Horowitz
venue: cacm
year: 2015
date: 2015-04-01
doi: 10.1145/2735841
thumbnail: True
materials:
  - name: paper
    url: /pubs/convolution_engine_balancing_efficiency_and_flexibility_in_specialized_computing_cacm/paper.pdf
    type: file-pdf
  - name: CACM
    url: https://cacm.acm.org/research/convolution-engine/
    type: file-alt
tags:
  - memory-storage
  - accelerators
  - energy-efficiency
---
General-purpose processors, while tremendously versatile, pay a huge cost for their flexibility by wasting over 99% of the energy in programmability overheads. Reducing this waste requires tuning data storage and compute structures and their connectivity to the data-flow and data-locality patterns in the algorithms.

The Convolution Engine (CE) is a programmable processor specialized for the convolution-like data-flow prevalent in computational photography, computer vision, and video processing. CE achieves energy efficiency by capturing data-reuse patterns, eliminating data transfer overheads, and enabling a large number of operations per memory access.
