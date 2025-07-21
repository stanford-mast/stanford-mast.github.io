---
title: 'Towards μs tail latency and terabit ethernet: disaggregating the host network stack'
authors:
  - name: Qizhe Cai
  - name: Midhul Vuppalapati
  - name: Jaehyun Hwang
  - key: christoskozyrakis
  - name: Rachit Agarwal
    affiliation: Cornell
venue: preprint
year: 2022
date: 2022-08-01
doi: 
thumbnail: False
materials:
tags:
---
Dedicated, tightly integrated, and static packet processing pipelines in today's most widely deployed network stacks preclude them from fully exploiting capabilities of modern hardware.We present NetChannel, a disaggregated network stack architecture forμs-scale applications running atop Terabit Ethernet. NetChannel's disaggregated architecture enables independent scaling and scheduling of resources allocated to each layer in the packet processing pipeline. Using an end-to-end NetChannel realization within the Linux network stack, we demonstrate that NetChannel enables new operating points---(1) enabling a single application thread to saturate multi-hundred gigabit access link bandwidth; (2) enabling near-linear scalability for small message processing with number of cores, independent of number of application threads; and, (3) enabling isolation of latency-sensitive applications, allowing them to …
