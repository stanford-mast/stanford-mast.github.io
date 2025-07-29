---
title: 'Executing Java programs with transactional memory'
authors:
  - name: Brian D Carlstrom
  - key: jaewoongchung
  - name: Hassan Chafi
  - key: austenmcdonald
  - key: chicaominh
  - name: Lance Hammond
  - key: christoskozyrakis
  - name: Kunle Olukotun
    affiliation: Stanford
venue: compprogramming
year: 2006
date: 2006-12-01
doi: 10.1016/j.scico.2006.05.006
thumbnail: False
materials:
tags:
---
Parallel programming is difficult due to the complexity of dealing with conventional lock-based synchronization. To simplify parallel programming, there have been a number of proposals to support transactions directly in hardware and eliminate locks completely. Although hardware support for transactions has the potential to completely change the way parallel programs are written, initially transactions will be used to execute existing parallel programs. In this paper we investigate the implications of using transactions to execute existing parallel Java programs. Our results show that transactions can be used to support all aspects of Java multithreaded programs, and once Java virtual machine issues have been addressed, the conversion of a lock-based application into transactions is largely straightforward. The performance that these converted applications achieve is equal to or sometimes better than the original lock-based implementation.
