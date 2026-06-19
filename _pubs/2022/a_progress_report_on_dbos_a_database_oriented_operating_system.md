---
title: 'A Progress Report on DBOS: A Database-oriented Operating System'
authors:
  - key: qianli
  - name: Peter Kraft
  - key: kostiskaffes
  - key: athinagorasskiadopoulos
  - name: Deeptaanshu Kumar
  - name: Jason Li
  - name: Michael Cafarella
  - name: Goetz Graefe
  - name: Jeremy Kepner
  - key: christoskozyrakis
  - name: Michael Stonebraker
  - name: Lalith Suresh
  - name: Matei Zaharia
venue: cidr
year: 2022
date: 2022-01-09
doi:
thumbnail: False
materials:
  - name: Paper
    url: https://vldb.org/cidrdb/papers/2022/p26-li.pdf
    type: file-alt
tags:
  - OS
  - databases
  - datacenter-systems
---
Over the last year, a group of us at MIT, Stanford, CMU, Google, and VMware have been designing and implementing a new Operating System (OS) stack for modern hyperscale datacenter environments. This new stack leverages a set of multi-core, multi-node distributed DBMSs near the bottom of the stack to manage a cluster of machines on a public or private cloud. In this paper, we briefly review the rationale for a new OS, present our resulting architecture, and review our progress to date.

The meat of our paper is a presentation of the main lessons thus far from this project. Many of these have to do with missing capabilities in multi-node DBMSs that form the guts of our proposal. Finally, we present future research directions in database-oriented operating systems.
