---
title: 'Phoenix++ modular mapreduce for shared-memory systems'
authors:
  - name: Justin Talbot
    affiliation: Stanford
  - name: Richard M Yoo
    affiliation: Stanford
  - key: christoskozyrakis
venue: mapreduce
year: 2011
date: 2011-06-01
doi: 10.1145/1996092.1996095
thumbnail: False
materials:
tags:
---
This paper describes our rewrite of Phoenix, a MapReduce framework for shared-memory CMPs and SMPs. Despite successfully demonstrating the applicability of a MapReduce-style pipeline to shared-memory machines, Phoenix has a number of limitations; its uniform intermediate storage of key-value pairs, inefficient combiner implementation, and poor task overhead amortization fail to efficiently support a wide range of MapReduce applications, encouraging users to manually circumvent the framework. We describe an alternative implementation, Phoenix++, that provides a modular, flexible pipeline that can be easily adapted by the user to the characteristics of a particular workload. Compared to Phoenix, this new approach achieves a 4.7-fold performance improvement and increased scalability, while allowing users to write simple, strict MapReduce code.
