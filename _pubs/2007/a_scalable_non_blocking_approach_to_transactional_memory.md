---
title: 'A Scalable, Non-blocking Approach to Transactional Memory'
authors:
  - name: Hassan Chafi
  - name: Jared Casper
  - name: Brian D. Carlstrom
  - key: austenmcdonald
  - name: Chi Cao Minh
  - key: woongkibaek
  - key: christoskozyrakis
  - name: Kunle Olukotun
venue: hpca
year: 2007
date: 2007-02-01
doi: 10.1109/hpca.2007.346189
thumbnail: False
materials:
tags:
  - architecture
  - parallel-compute
  - memory-storage
  - transactional-memory
---
Transactional memory (TM) provides mechanisms that promise to simplify parallel programming by eliminating the need for locks and their associated problems (deadlock, livelock, priority inversion, convoying). For TM to be adopted in the long term, not only does it need to deliver on these promises, but it needs to scale to a high number of processors. To date, proposals for scalable TM have relegated livelock issues to user-level contention managers. This paper presents the first scalable TM implementation for directory-based distributed shared memory systems that is livelock free without the need for user-level intervention. The design is a scalable implementation of optimistic concurrency control that supports parallel commits with a two-phase commit protocol, uses write-back caches, and filters coherence messages. The scalable design is based on transactional coherence and consistency (TCC), which supports continuous transactions and fault isolation. A performance evaluation of the design using both scientific and enterprise benchmarks demonstrates that the directory-based TCC design scales efficiently for NUMA systems up to 64 processors.
