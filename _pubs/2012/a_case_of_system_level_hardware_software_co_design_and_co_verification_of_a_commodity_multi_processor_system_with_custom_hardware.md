---
title: 'A case of system-level hardware/software co-design and co-verification of a commodity multi-processor system with custom hardware'
authors:
  - name: Sungpack Hong
  - name: Tayo Oguntebi
  - name: Jared Casper
  - name: Nathan Bronson
  - key: christoskozyrakis
  - name: Kunle Olukotun
    affiliation: Stanford
venue: codes
year: 2012
date: 2012-10-01
doi: 10.1145/2380445.2380524
thumbnail: False
materials:
tags:
---
This paper presents an interesting system-level co-design and co-verification case study for a non-trivial design where multiple high-performing x86 processors and custom hardware were connected through a coherent interconnection fabric. In functional verification of such a system, we used a processor bus functional model (BFM) to combine native software execution with a cycle-accurate interconnect simulator and an HDL simulator. However, we found that significant extensions need to be made to the conventional BFM methodology in order to capture various data-race cases in simulation, which eventually happen in modern multi-processor systems. Especially essential were faithful implementations of the memory consistency model and cache coherence protocol, as well as timing randomization. We demonstrate how such a co-simulation environment can be constructed from existing tools and software. Lessons from our study can similarly be applied to design and verification of other tightly-coupled systems.
