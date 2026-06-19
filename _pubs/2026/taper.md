---
title: 'Regulating Branch Parallelism in LLM Serving'
authors:
  - key: swapnilgandhi
  - name: Siva Hari
  - name: Bill Dally
  - key: christoskozyrakis
venue: preprint
year: 2026
date: 2026-06-01
doi: 10.48550/arXiv.2605.06914
thumbnail: True
materials:
tags:
  - AI-systems
  - parallel-compute
  - resource-management
---
Recent methods expose intra-request parallelism in LLM outputs, allowing independent branches to decode concurrently. Existing serving systems execute these branches eagerly or under fixed caps. We show that both are brittle: eager admission inflates the shared decode step, degrading co-batched requests in serial stages, while conservative fixed caps forgo the throughput that motivated exposing branches in the first place. We call the excess step latency caused by admitted branches the branch externality and show that the safe width depends on batch composition, context lengths, and accumulated slack, all of which change continuously over a workload trace.

We introduce TAPER, a per-step admission controller that treats extra branches as opportunistic work, admitted only when the predicted branch externality fits within the batch's current slack budget. Per-step regulation is practical because branch-level scheduling decouples compute from memory: branches share the request's prefix KV, so expanding or contracting width requires no memory reclamation. On Qwen3-32B, TAPER improves goodput by 1.77× over IRP-Off and by 1.48× over IRP-Eager, while maintaining over 95% SLO attainment.