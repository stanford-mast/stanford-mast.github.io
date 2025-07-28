---
title: 'Programming with transactional coherence and consistency (TCC)'
authors:
  - name: Lance Hammond
  - name: Brian D Carlstrom
  - name: Vicky Wong
  - name: Ben Hertzberg
  - name: Mike Chen
  - key: christoskozyrakis
  - name: Kunle Olukotun
    affiliation: Stanford
venue: asplos
year: 2004
date: 2004-10-01
doi: 10.1145/1037187.1024395
thumbnail: False
materials:
tags:
---
Transactional Coherence and Consistency (TCC) offers a way to simplify parallel programming by executing all code within transactions. In TCC systems, transactions serve as the fundamental unit of parallel work, communication and coherence. As each transaction completes, it writes all of its newly produced state to shared memory atomically, while restarting other processors that have speculatively read stale data. With this mechanism, a TCC-based system automatically handles data synchronization correctly, without programmer intervention. To gain the benefits of TCC, programs must be decomposed into transactions. We describe two basic programming language constructs for decomposing programs into transactions, a loop conversion syntax and a general transaction-forking mechanism. With these constructs, writing correct parallel programs requires only small, incremental changes to correct sequential programs. The performance of these programs may then easily be optimized, based on feedback from real program execution, using a few simple techniques.
