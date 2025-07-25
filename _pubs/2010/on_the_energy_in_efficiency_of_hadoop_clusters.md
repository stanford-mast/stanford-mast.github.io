---
title: 'On the energy (in) efficiency of hadoop clusters'
authors:
  - key: jacobleverich
  - key: christoskozyrakis
venue: sigopsreview
year: 2010
date: 2010-03-01
doi: 10.1145/1740390.1740405
thumbnail: False
materials:
tags:
---
Distributed processing frameworks, such as Yahoo!'s Hadoop and Google's MapReduce, have been successful at harnessing expansive datacenter resources for large-scale data analysis. However, their effect on datacenter energy efficiency has not been scrutinized. Moreover, the filesystem component of these frameworks effectively precludes scale-down of clusters deploying these frameworks (i.e. operating at reduced capacity). This paper presents our early work on modifying Hadoop to allow scale-down of operational clusters. We find that running Hadoop clusters in fractional configurations can save between 9% and 50% of energy consumption, and that there is a tradeoff between performance energy consumption. We also outline further research into the energy-efficiency of these frameworks.
