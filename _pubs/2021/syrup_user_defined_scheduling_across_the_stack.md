---
title: 'Syrup: User-defined scheduling across the stack'
authors:
  - key: kostiskaffes
  - name: Jack Tigar Humphries
    affiliation: Stanford
  - name: David Mazières
    affiliation: Stanford
  - key: christoskozyrakis
venue: preprint
year: 2021
date: 2021-10-01
doi: 
thumbnail: False
materials:
tags:
---
Suboptimal scheduling decisions in operating systems, networking stacks, and application runtimes are often responsible for poor application performance, including higher latency and lower throughput. These poor decisions stem from a lack of insight into the applications and requests the scheduler is handling and a lack of coherence and coordination between the various layers of the stack, including NICs, kernels, and applications.We propose Syrup, a framework for user-defined scheduling. Syrup enables untrusted application developers to express application-specific scheduling policies across these system layers without being burdened with the low-level system mechanisms that implement them. Application developers write a scheduling policy with Syrup as a set of matching functions between inputs (threads, network packets, network connections) and executors (cores, network sockets, NIC queues) and …
