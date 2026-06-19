---
title: 'Implementing and Evaluating a Model Checker for Transactional Memory Systems'
authors:
  - key: woongkibaek
  - name: Nathan Bronson
  - key: christoskozyrakis
  - name: Kunle Olukotun
venue: iceccs
year: 2010
date: 2010-03-01
doi: 10.1109/iceccs.2010.30
thumbnail: False
materials:
tags:
  - compilers
  - parallel-compute
  - memory-storage
  - transactional-memory
---
Transactional Memory (TM) is a promising technique that addresses the difficulty of parallel programming. Since TM takes responsibility for all concurrency control, TM systems are highly vulnerable to subtle correctness errors. Due to the difficulty of fully proving the correctness of TM systems, many of them are used without any formal correctness guarantees. This paper presents ChkTM, a flexible model checking environment to verify the correctness of various TM systems. ChkTM aims to model TM systems close to the implementation level to reveal as many potential bugs as possible. For example, ChkTM accurately models the version control mechanism in timestamp-based software TMs (STMs). In addition, ChkTM can flexibly model TM systems that use additional hardware components or support nested parallelism. Using ChkTM, we model several TM systems including a widely-used industrial STM (TL2), a hybrid TM (SigTM) that uses hardware signatures, and an STM (NesTM) that supports nested parallel transactions. We then demonstrate how ChkTM can be used to find a previously unreported correctness bug in the current implementation of eager-versioning TL2. We also verify the serializability of TL2 and SigTM and strong isolation guarantees of SigTM. Finally, we quantitatively analyze ChkTM to understand the practical issues and motivate further research in model checking TM systems.
