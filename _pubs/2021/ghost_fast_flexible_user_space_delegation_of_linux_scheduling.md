---
title: 'ghOSt: Fast & Flexible User-Space Delegation of Linux Scheduling'
authors:
  - name: Jack Tigar Humphries
    affiliation: Stanford
  - name: Neel Natu
  - name: Ashwin Chaugule
  - name: Ofir Weisse
  - name: Barret Rhoden
  - name: Josh Don
  - name: Luigi Rizzo
  - name: Oleg Rombakh
  - name: Paul Turner
  - key: christoskozyrakis
venue: sosp
year: 2021
date: 2021-10-01
doi: 10.1145/3477132.3483542
thumbnail: False
materials:
tags:
---
We present ghOSt, our infrastructure for delegating kernel scheduling decisions to userspace code. ghOSt is designed to support the rapidly evolving needs of our data center workloads and platforms.Improving scheduling decisions can drastically improve the throughput, tail latency, scalability, and security of important workloads. However, kernel schedulers are difficult to implement, test, and deploy efficiently across a large fleet. Recent research suggests bespoke scheduling policies, within custom data plane operating systems, can provide compelling performance results in a data center setting. However, these gains have proved difficult to realize as it is impractical to deploy a custom OS image(s) at an application granularity, particularly in a multi-tenant environment, limiting the practical applications of these new techniques.ghOSt provides general-purpose delegation of scheduling policies to userspace …
