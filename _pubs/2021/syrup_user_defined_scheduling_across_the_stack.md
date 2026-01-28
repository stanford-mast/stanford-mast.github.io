---
title: 'Syrup: User-defined scheduling across the stack'
authors:
  - key: kostiskaffes
  - key: jackhumphries
  - name: David Mazières
    affiliation: Stanford
  - key: christoskozyrakis
venue: sosp
year: 2021
date: 2021-10-01
doi: 10.1145/3477132.3483548
thumbnail: True
materials:
tags:
---
Suboptimal scheduling decisions in operating systems, networking stacks, and application runtimes are often responsible for poor application performance, including higher latency and lower throughput. These poor decisions stem from a lack of insight into the applications and requests the scheduler is handling and a lack of coherence and coordination between the various layers of the stack, including NICs, kernels, and applications.We propose Syrup, a framework for user-defined scheduling. Syrup enables untrusted application developers to express application-specific scheduling policies across these system layers without being burdened with the low-level system mechanisms that implement them. Application developers write a scheduling policy with Syrup as a set of matching functions between inputs (threads, network packets, network connections) and executors (cores, network sockets, NIC queues) and …
