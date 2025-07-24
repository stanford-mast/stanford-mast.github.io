---
title: 'Towards energy-proportional datacenter memory with mobile DRAM'
authors:
  - name: Krishna T Malladi
    affiliation: Stanford
  - name: Frank A Nothaft
    affiliation: Stanford
  - name: Karthika Periyathambi
    affiliation: Stanford
  - name: Benjamin C Lee
    affiliation: Duke
  - key: christoskozyrakis
  - name: Mark Horowitz
    affiliation: Stanford
venue: isca
year: 2012
date: 2012-06-01
doi: 10.1145/2366231.2337164
thumbnail: False
materials:
tags:
---
To increase datacenter energy efficiency, we need memory systems that keep pace with processor efficiency gains. Currently, servers use DDR3 memory, which is designed for high bandwidth but not for energy proportionality. A system using 20% of the peak DDR3 bandwidth consumes 2.3x the energy per bit compared to the energy consumed by a system with fully utilized memory bandwidth. Nevertheless, many datacenter applications stress memory capacity and latency but not memory bandwidth. In response, we architect server memory systems using mobile DRAM devices, trading peak bandwidth for lower energy consumption per bit and more efficient idle modes. We demonstrate 3-5x lower memory power, better proportionality, and negligible performance penalties for datacenter workloads.
