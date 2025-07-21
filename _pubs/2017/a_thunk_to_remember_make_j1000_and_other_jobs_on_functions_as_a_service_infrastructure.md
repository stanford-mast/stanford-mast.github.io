---
title: 'A thunk to remember: make-j1000 (and other jobs) on functions-as-a-service infrastructure'
authors:
  - name: Sadjad Fouladi
  - name: Dan Iter
  - name: Shuvo Chatterjee
  - key: christoskozyrakis
  - name: Matei Zaharia
    affiliation: UC Berkeley
  - name: Keith Winstein
    affiliation: Stanford
venue: preprint
year: 2017
date: 2017-09-01
doi: 
thumbnail: False
materials:
tags:
---
We present gg: a system for executing interdependent software workflows across thousands of short-lived “lambdas” that run in parallel on public cloud infrastructure. The system includes three major contributions:(a) an interchange format for representing “thunks”—programs and their complete data dependencies—that can be executed anywhere;(b) a system to automatically infer the dependency tree of a software build system and synthesize it as a directed acyclic graph of thunks, by replacing stages of the system with “models” that capture dependencies with fine granularity; and (c) an execution engine that resolves thunks recursively on public functions-as-a-service infrastructure with thousand-way parallelism. We found that gg outperforms existing schemes for accelerating compilation—with large projects such as inkscape and LLVM, gg was 3.7× to 4× as fast as outsourcing compilation to a remote 64-core machine, and 1.2× to 2.2× as fast as running make-j64 locally on the 64-core machine itself—and that the thunk abstraction is applicable to a broad range of tasks.
