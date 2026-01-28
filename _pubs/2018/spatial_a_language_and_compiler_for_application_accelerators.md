---
title: 'Spatial: A language and compiler for application accelerators'
authors:
  - name: David Koeplinger
  - name: Matthew Feldman
  - key: raghuprabhakar
  - name: Yaqi Zhang
  - name: Stefan Hadjis
  - name: Ruben Fiszel
  - name: Tian Zhao
  - name: Luigi Nardi
  - name: Ardavan Pedram
  - key: christoskozyrakis
  - name: Kunle Olukotun
    affiliation: Stanford
venue: pldi
year: 2018
date: 2018-06-01
doi: 10.1145/3192366.3192379
thumbnail: True
materials:
tags:
---
Industry is increasingly turning to reconfigurable architectures like FPGAs and CGRAs for improved performance and energy efficiency. Unfortunately, adoption of these architectures has been limited by their programming models. HDLs lack abstractions for productivity and are difficult to target from higher level languages. HLS tools are more productive, but offer an ad-hoc mix of software and hardware abstractions which make performance optimizations difficult.In this work, we describe a new domain-specific language and compiler called Spatial for higher level descriptions of application accelerators. We describe Spatial's hardware-centric abstractions for both programmer productivity and design performance, and summarize the compiler passes required to support these abstractions, including pipeline scheduling, automatic memory banking, and automated design tuning driven by active machine learning. We …
