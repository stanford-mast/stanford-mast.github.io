---
title: 'Enhanced Concurrency Control with Transactional NACKs'
authors:
  - key: woongkibaek
  - name: Richard M Yoo
  - key: christoskozyrakis
venue: transact
year: 2013
date: 2013-03-01
doi:
thumbnail: False
materials:
  - name: paper
    url: /pubs/enhanced_concurrency_control_with_transactional_nacks/paper.pdf
    type: file-pdf
  - name: talk
    url: /pubs/enhanced_concurrency_control_with_transactional_nacks/talk.pdf
    type: file-pdf
  - name: TRANSACT
    url: https://transact2013.cse.lehigh.edu/
    type: file-alt
tags:
  - architecture
  - parallel-compute
  - transactional-memory
  - resource-management
---
Transactional-memory systems must dynamically adjust concurrency to provide robust performance and fairness, but obtaining accurate runtime information can be expensive. This paper identifies transactional NACKs as a low-cost source of dependency and utilization information and proposes three uses: accurate deadlock detection, dependency-tree construction, and carrier sensing. A prototype concurrency controller using these techniques improves the performance of hardware and hybrid transactional-memory systems.
