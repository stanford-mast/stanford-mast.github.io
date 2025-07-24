---
title: 'Convolution engine: balancing efficiency & flexibility in specialized computing'
authors:
  - name: Wajahat Qadeer
  - key: rehanhameed
  - name: Ofer Shacham
  - name: Preethi Venkatesan
  - key: christoskozyrakis
  - name: Mark A Horowitz
venue: cacm
year: 2013
date: 2013-06-01
doi: 10.1145/2735841
thumbnail: False
materials:
tags:
---
General-purpose processors, while tremendously versatile, pay a huge cost for their flexibility by wasting over 99% of the energy in programmability overheads. We observe that reducing this waste requires tuning data storage and compute structures and their connectivity to the data-flow and data-locality patterns in the algorithms. Hence, by backing off from full programmability and instead targeting key data-flow patterns used in a domain, we can create efficient engines that can be programmed and reused across a wide range of applications within that domain.
We present the Convolution Engine (CE)---a programmable processor specialized for the convolution-like data-flow prevalent in computational photography, computer vision, and video processing. The CE achieves energy efficiency by capturing data-reuse patterns, eliminating data transfer overheads, and enabling a large number of operations per memory access. We demonstrate that the CE is within a factor of 2--3× of the energy and area efficiency of custom units optimized for a single kernel. The CE improves energy and area efficiency by 8--15× over data-parallel Single Instruction Multiple Data (SIMD) engines for most image processing applications.
