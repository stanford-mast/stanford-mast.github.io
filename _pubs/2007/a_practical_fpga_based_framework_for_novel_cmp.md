---
title: 'A Practical FPGA-based Framework for Novel CMP'
authors:
  - key: sewookwee
  - name: Jared Casper
  - name: Njuguna Njoroge
  - name: Yuriy Tesylar
  - name: Daxia Ge
  - key: christoskozyrakis
  - name: Kunle Olukotun
    affiliation: Stanford
venue: fpga
year: 2007
date: 2007-01-01
doi: 10.1145/1216919.1216936
thumbnail: False
materials:
tags:
---
Chip-multiprocessors are quickly gaining momentum in all segments of computing. However, the practical success of CMPs strongly depends on addressing the difficulty of multithreaded application development. To address this challenge, it is necessary to co-develop new CMP architecture with novel programming models. Currently, architecture research relies on software simulators which are too slow to facilitate interesting experiments with CMP software without using small datasets or significantly reducing the level of detail in the simulated models. An alternative to simulation is to exploit the rich capabilities of modern FPGAs to create FPGA-based platforms for novel CMP research. This paper presents ATLAS, the first prototype for CMPs with hardware support for Transactional Memory (TM), a technology aiming to simplify parallel programming. ATLAS uses the BEE2 multi-FPGA board to provide a system with 8 PowerPC cores that run at 100MHz and runs Linux. ATLAS provides significant benefits for CMP research such as 100x performance improvement over a software simulator and good visibility that helps with software tuning and architectural improvements. In addition to presenting and evaluating ATLAS, we share our observations about building a FPGA-based framework for CMP research. Specifically, we address issues such as overall performance, challenges of mapping ASIC-style CMP RTL on to FPGAs, software support, the selection criteria for the base processor, and the challenges of using pre-designed IP libraries.
