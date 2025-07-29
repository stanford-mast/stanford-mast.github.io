---
title: 'Transactional memory: The hardware-software interface'
authors:
  - key: austenmcdonald
  - name: Brian D Carlstrom
  - key: jaewoongchung
  - key: chicaominh
  - name: Hassan Chafi
  - key: christoskozyrakis
  - name: Kunle Olukotun
    affiliation: Stanford
venue: ieeemicro
year: 2007
date: 2007-05-01
doi: 10.1109/MM.2007.26
thumbnail: False
materials:
tags:
---
As multicore chips become ubiquitous, the need to provide architectural support for practical parallel programming is reaching critical. Conventional lock-based concurrency control techniques are difficult to use, requiring the programmer to navigate through the minefield of coarse-versus fine-grained locks, deadlock, livelock, lock convoying, and priority inversion. This explicit management of concurrency is beyond the reach of the average programmer, threatening to waste the additional parallelism available with multicore architectures. This comprehensive architecture supports nested transactions, transactional handlers, and two-phase commit. The result is a seamless integration of transactional memory with modern programming languages and runtime environments
