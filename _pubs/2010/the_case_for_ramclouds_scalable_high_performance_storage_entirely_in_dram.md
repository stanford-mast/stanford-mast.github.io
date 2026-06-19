---
title: 'The case for RAMClouds: scalable high-performance storage entirely in DRAM'
authors:
  - name: John Ousterhout
  - name: Parag Agrawal
  - name: David Erickson
  - key: christoskozyrakis
  - key: jacobleverich
  - name: David Mazières
  - name: Subhasish Mitra
  - name: Aravind Narayanan
  - name: Guru Parulkar
  - name: Mendel Rosenblum
  - name: Stephen M. Rumble
  - name: Eric Stratmann
  - name: Ryan Stutsman
venue: sigopsreview
year: 2010
date: 2010-01-01
doi: 10.1145/1713254.1713276
thumbnail: False
materials:
tags:
  - OS
  - cloud
  - databases
  - memory-storage
  - datacenter-systems
  - low-latency
---
Disk-oriented approaches to online storage are becoming increasingly problematic: they do not scale gracefully to meet the needs of large-scale Web applications, and improvements in disk capacity have far outstripped improvements in access latency and bandwidth. This paper argues for a new approach to datacenter storage called RAMCloud, where information is kept entirely in DRAM and large-scale systems are created by aggregating the main memories of thousands of commodity servers. We believe that RAMClouds can provide durable and available storage with 100-1000x the throughput of disk-based systems and 100-1000x lower access latency. The combination of low latency and large scale will enable a new breed of dataintensive applications.
