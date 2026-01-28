---
title: 'Interstellar: Using Halides Scheduling Language to Analyze DNN Accelerators'
authors:
  - name: Xuan Yang
  - key: mingyugao
  - name: Qiaoyi Liu
  - name: Jeff Setter
  - name: Jing Pu
  - name: Ankita Nayak
  - name: Steven Bell
  - name: Kaidi Cao
  - name: Heonjae Ha
  - name: Priyanka Raina
  - key: christoskozyrakis
  - name: Mark Horowitz
    affiliation: Stanford
venue: asplos
year: 2020
date: 2020-03-01
doi: 10.1145/3373376.3378514
thumbnail: True
materials:
tags:
---
We show that DNN accelerator micro-architectures and their program mappings represent specific choices of loop order and hardware parallelism for computing the seven nested loops of DNNs, which enables us to create a formal taxonomy of all existing dense DNN accelerators. Surprisingly, the loop transformations needed to create these hardware variants can be precisely and concisely represented by Halide's scheduling language. By modifying the Halide compiler to generate hardware, we create a system that can fairly compare these prior accelerators. As long as proper loop blocking schemes are used, and the hardware can support mapping replicated loops, many different hardware dataflows yield similar energy efficiency with good performance. This is because the loop blocking can ensure that most data references stay on-chip with good locality and the processing units have high resource utilization …
