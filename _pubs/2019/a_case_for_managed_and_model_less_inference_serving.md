---
title: 'A case for managed and model-less inference serving'
authors:
  - key: neerajadwadkar
  - key: frankyromero
  - key: qianli
  - key: christoskozyrakis
venue: hotos
year: 2019
date: 2019-05-01
doi: 10.1145/3317550.3321443
thumbnail: True
materials:
tags:
---
The number of applications relying on inference from machine learning models, especially neural networks, is already large and expected to keep growing. For instance, Facebook applications issue tens-of-trillions of inference queries per day with varying performance, accuracy, and cost constraints. Unfortunately, today's inference serving systems are neither easy to use nor cost effective. Developers must manually match the performance, accuracy, and cost constraints of their applications to a large design space that includes decisions such as selecting the right model and model optimizations, selecting the right hardware architecture, selecting the right scale-out factor, and avoiding cold-start effects. These interacting decisions are difficult to make, especially when the application load varies over time, applications evolve over time, and the available resources vary over time.If we want an increasing number of …
