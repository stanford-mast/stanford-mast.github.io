---
title: 'Transactions Make Debugging Easy'
authors:
  - key: qianli
  - name: Peter Kraft
    affiliation: Stanford
  - name: Michael Cafarella
  - name: Çağatay Demiralp
  - name: Goetz Graefe
  - key: christoskozyrakis
  - name: Michael Stonebraker
    affiliation: MIT
  - name: Lalith Suresh
  - name: Matei Zaharia
    affiliation: UC Berkeley
venue: preprint
year: 2022
date: 2022-12-01
doi: 
thumbnail: False
materials:
tags:
---
We propose TROD, a novel transaction-oriented framework for debugging modern distributed web applications and online services. Our critical insight is that if applications store all state in databases and only access state transactionally, TROD can use lightweight always-on tracing to track the history of application state changes and data provenance, and then leverage the captured traces and transaction logs to faithfully replay or even test modified code retroactively on any past event. We demonstrate how TROD can simplify programming and debugging in production applications, list several research challenges and directions, and encourage the database and systems communities to drastically rethink the synergy between the way people develop and debug applications.
