---
title: 'Optimizing video analytics with declarative model relationships'
authors:
  - key: frankyromero
  - name: Johann Hauswald
    affiliation: Stanford
  - name: Aditi Partap
    affiliation: Stanford
  - name: Daniel Kang
    affiliation: Stanford
  - name: Matei Zaharia
    affiliation: UC Berkeley
  - key: christoskozyrakis
venue: vldb
year: 2022
date: 2022-11-01
doi: 10.14778/3570690.3570695
thumbnail: True
materials:
tags:
---
The availability of vast video collections and the accuracy of ML models has generated significant interest in video analytics systems. Since naively processing all frames using expensive models is impractical, researchers have proposed optimizations such as selectively using faster but less accurate models to replace or filter frames for expensive models. However, these optimizations are difficult to apply on queries with multiple predicates and models, as users must manually explore a large optimization space. Without significant systems expertise or time investment, an analyst may manually create an execution plan that is unnecessarily expensive and/or terribly inaccurate.We proposeRelational Hints, a declarative interface that allows users to suggest ML model relationships based on domain knowledge. Users can express two key relationships: when a model can replace another (CAN REPLACE) and when a …
