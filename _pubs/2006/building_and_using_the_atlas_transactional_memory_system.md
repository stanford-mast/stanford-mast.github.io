---
title: 'Building and using the atlas transactional memory system'
authors:
  - name: Njuguna Njoroge
  - key: sewookwee
  - name: Jared Casper
  - name: Justin Burdick
  - name: Yuriy Teslyar
  - key: christoskozyrakis
  - name: Kunle Olukotun
    affiliation: Stanford
venue: warfp
year: 2006
date: 2006-02-01
doi: 
thumbnail: False
materials:
tags:
---
At WARFP 2005, we proposed ATLAS as a scalable implementation for transactional parallel systems [5]. The impetus for the development of ATLAS is to address the significant hurdles that software simulators face in multiprocessor architectural research. In particular, ATLAS is an FPGA-based system that primarily serves as a rapid software development platform for our transactional memory model, TCC [4]. Leveraging commodity hardware and software tools, ATLAS is poised to support research exploring the impact of transactional memory on architecture, operating systems, compilers and programming models.To date, we have implemented a fully functional 2-processor ATLAS system on Xilinx’s XUP board [8], employing the two embedded PowerPC cores in the Virtex II Pro FPGA. To interface with the TCC caches in the FPGA fabric, we have also implemented the TCC API [3]. Additionally, we have developed infrastructure to support debugging and profiling with the aim of increasing visibility and ease of performance tuning of applications.
