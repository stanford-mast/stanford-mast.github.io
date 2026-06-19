---
title: 'FARM: A Prototyping Environment for Tightly-Coupled, Heterogeneous Architectures'
authors:
  - name: Tayo Oguntebi
  - name: Sungpack Hong
  - name: Jared Casper
  - name: Nathan Bronson
  - key: christoskozyrakis
  - name: Kunle Olukotun
venue: fccm
year: 2010
date: 2010-05-01
doi: 10.1109/fccm.2010.41
thumbnail: False
materials:
tags:
  - architecture
  - accelerators
  - energy-efficiency
---
Computer architectures are increasingly turning to parallelism and heterogeneity as solutions for boosting performance in the face of power constraints. As this trend continues, the challenges of simulating and evaluating these architectures have grown. Hardware prototypes provide deeper insight into these systems when compared to simulators, but are traditionally more difficult and costly to build. We present the Flexible Architecture Research Machine (FARM), a hardware prototyping system based on an FPGA coherently connected to a multiprocessor system. FARM substantially reduces the difficulty and cost of building hardware prototypes by providing a ready-made framework for communicating with a custom design on the FPGA. FARM ensures efficient, low-latency communication with the FPGA via a variety of mechanisms, allowing a wide range of applications to effectively utilize the system. FARM's coherent FPGA includes a cache and participates in coherence activities with the processors. This tight coupling allows for realistic, innovative architecture prototypes that would otherwise be extremely difficult to simulate. We evaluate FARM by providing the reader with a profile of the overheads introduced across the full range of communication mechanisms. This will guide the potential FARM user towards an optimal configuration when designing his prototype.
