---
title: 'Characterization of TCC on chip-multiprocessors'
authors:
  - key: austenmcdonald
  - name: JaeWoong Chung
  - name: Hassan Chafi
  - name: Chi Cao Minh
  - name: Brian D. Carlstrom
  - name: Lance Hammond
  - key: christoskozyrakis
  - name: Kunle Olukotun
venue: pact
year: 2005
date: 2005-09-01
doi: 10.1109/pact.2005.11
thumbnail: False
materials:
tags:
  - architecture
  - memory-storage
  - transactional-memory
---
Transactional coherence and consistency (TCC) is a novel coherence scheme for shared memory multiprocessors that uses programmer-defined transactions as the fundamental unit of parallel work, synchronization, coherence, and consistency. TCC has the potential to simplify parallel program development and optimization by providing a smooth transition from sequential to parallel programs. In this paper, we study the implementation of TCC on chip-multiprocessors (CMPs). We explore design alternatives such as the granularity of state tracking, double-buffering, and write-update and write-invalidate protocols. Furthermore, we characterize the performance of TCC in comparison to conventional snoopy cache coherence (SCC) using parallel applications optimized for each scheme. We conclude that the two coherence schemes perform similarly, with each scheme having a slight advantage for some applications. The bandwidth requirements of TCC are slightly higher but well within the capabilities of CMP systems. Also, we find that overflow of speculative state can be effectively handled by a simple victim cache. Our results suggest TCC can provide its programming advantages without compromising the performance expected from well-tuned parallel applications.
