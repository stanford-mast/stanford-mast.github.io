---
title: 'The software stack for transactional memory'
authors:
  - name: Brian D Carlstrom
  - key: jaewoongchung
  - name: Christos Kozyrakis Kunle Olukotun
venue: stmcs
year: 2006
date: 2006-03-01
doi: 
thumbnail: False
materials:
tags:
---
Transactional memory systems apply the experience of the database community to the general problem of parallel programming with the goal of providing a simple parallel programing model that delivers on the performance potential of multi-processor systems. Although initial research into both software-only and hardwaresupported transactional memory has shown promising results, there are many challenges to creating a fully transactional software stack. Although today’s software stack has some limited use of transactional programming, many parts of the stack from basic data structures to the operating system and program runtimes contain at least some lock-based code. In code with coarse-grained locking, transactions provide an opportunity to improve performance. In code with fine-grained lock, transactions provide an opportunity to simplify code while reducing overhead.
