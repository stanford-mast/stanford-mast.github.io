---
title: 'Testing implementations of transactional memory'
authors:
  - name: Chaiyasit Manovit
  - name: Sudheendra Hangal
  - name: Hassan Chafi
  - key: austenmcdonald
  - key: christoskozyrakis
  - name: Kunle Olukotun
    affiliation: Stanford
venue: pact
year: 2006
date: 2006-09-01
doi: 10.1145/1152154.1152177
thumbnail: False
materials:
tags:
---
Transactional memory is an attractive design concept for scalable multiprocessors because it offers efficient lock-free synchronization and greatly simplifies parallel software. Given the subtle issues involved with concurrency and atomicity, however, it is important that transactional memory systems be carefully designed and aggressively tested to ensure their correctness. In this paper, we propose an axiomatic framework to model the formal specification of a realistic transactional memory system which may contain a mix of transactional and non-transactional operations. Using this framework and extensions to analysis algorithms originally developed for checking traditional memory consistency, we show that the widely practiced pseudo-random testing methodology can be effectively applied to transactional memory systems. Our testing methodology was successful in finding previously unknown bugs in the implementation of TCC, a transactional memory system. We study two flavors of the underlying analysis algorithm, one incomplete and the other complete, and show that the complete algorithm while being theoretically intractable is very efficient in practice.
