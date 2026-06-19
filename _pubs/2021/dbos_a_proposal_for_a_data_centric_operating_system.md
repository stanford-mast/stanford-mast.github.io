---
title: 'DBOS: a DBMS-oriented operating system'
authors:
  - key: athinagorasskiadopoulos
  - key: qianli
  - name: Peter Kraft
    affiliation: Stanford
  - key: kostiskaffes
  - name: Daniel Hong
    affiliation: MIT
  - name: Shana Mathew
    affiliation: MIT
  - name: David Bestor
    affiliation: MIT
  - name: Michael Cafarella
    affiliation: MIT
  - name: Vijay Gadepally
    affiliation: MIT
  - name: Goetz Graefe
    affiliation: Google
  - name: Jeremy Kepner
    affiliation: MIT
  - key: christoskozyrakis
  - name: Tim Kraska
    affiliation: MIT
  - name: Michael Stonebraker
    affiliation: MIT
  - name: Lalith Suresh
    affiliation: VMware
  - name: Matei Zaharia
    affiliation: Stanford
venue: vldb
year: 2021
date: 2021-09-01
doi: 10.14778/3485450.3485454
thumbnail: True
materials:
tags:
  - OS
  - databases
  - datacenter-systems
  - resource-management
---
This paper presents the rationale and initial implementation results for DBOS, a database-oriented operating system architecture for scalable cluster computing. Instead of combining a traditional single-node OS with separate cluster schedulers, distributed file systems, and network managers, DBOS uses a distributed transactional DBMS as the foundation for scheduling, file management, inter-process communication, analytics, and high availability.
