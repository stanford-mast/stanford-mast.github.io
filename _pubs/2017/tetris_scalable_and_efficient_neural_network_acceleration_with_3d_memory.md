---
title: 'Tetris: Scalable and efficient neural network acceleration with 3d memory'
authors:
  - key: mingyugao
  - name: Jing Pu
  - name: Xuan Yang
  - name: Mark Horowitz
    affiliation: Stanford
  - key: christoskozyrakis
venue: preprint
year: 2017
date: 2017-04-01
doi: 
thumbnail: False
materials:
tags:
---
The high accuracy of deep neural networks (NNs) has led to the development of NN accelerators that improve performance by two orders of magnitude. However, scaling these accelerators for higher performance with increasingly larger NNs exacerbates the cost and energy overheads of their memory systems, including the on-chip SRAM buffers and the off-chip DRAM channels.This paper presents the hardware architecture and software scheduling and partitioning techniques for TETRIS, a scalable NN accelerator using 3D memory. First, we show that the high throughput and low energy characteristics of 3D memory allow us to rebalance the NN accelerator design, using more area for processing elements and less area for SRAM buffers. Second, we move portions of the NN computations close to the DRAM banks to decrease bandwidth pressure and increase performance and energy efficiency. Third, we show …
