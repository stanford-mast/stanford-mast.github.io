---
title: 'Faa$t: A Transparent Auto-Scaling Cache for Serverless Applications'
authors:
  - key: frankyromero
  - name: Gohar Irfan Chaudhry
  - name: Íñigo Goiri
  - name: Pragna Gopa
  - name: Paul Batum
  - key: neerajadwadkar
  - name: Rodrigo Fonseca
  - key: christoskozyrakis
  - name: Ricardo Bianchini
venue: socc
year: 2021
date: 2021-11-01
doi: 10.1145/3472883.3486974
thumbnail: True
materials:
tags:
---
Function-as-a-Service (FaaS) has become an increasingly popular way for users to deploy their applications without the burden of managing the underlying infrastructure. However, existing FaaS platforms rely on remote storage to maintain state, limiting the set of applications that can be run efficiently. Recent caching work for FaaS platforms has tried to address this problem, but has fallen short: it disregards the widely different characteristics of FaaS applications, does not scale the cache based on data access patterns, or requires changes to applications. To address these limitations, we present Faa$T, a transparent auto-scaling distributed cache for serverless applications. Each application gets its own cache. After a function executes and the application becomes inactive, the cache is unloaded from memory with the application. Upon reloading for the next invocation, Faa$T pre-warms the cache with objects …
