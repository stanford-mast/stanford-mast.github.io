---
title: 'Locality-aware task management for unstructured parallelism: A quantitative limit study'
authors:
  - name: Richard M Yoo
    affiliation: Intel
  - name: Christopher J Hughes
    affiliation: Intel
  - name: Changkyu Kim
    affiliation: Intel
  - name: Yen-Kuang Chen
    affiliation: Intel
  - key: christoskozyrakis
venue: spaa
year: 2013
date: 2013-07-01
doi: 10.1145/2486159.2486175
thumbnail: False
materials:
tags:
---
As we increase the number of cores on a processor die, the on-chip cache hierarchies that support these cores are getting larger, deeper, and more complex. As a result, non-uniform memory access effects are now prevalent even on a single chip. To reduce execution time and energy consumption, data access locality should be exploited. This is especially important for task-based programming systems, where a scheduler decides when and where on the chip the code segments, i.e., tasks, should execute. Capturing locality for structured task parallelism has been done effectively, but the more difficult case, unstructured parallelism, remains largely unsolved - little quantitative analysis exists to demonstrate the potential of locality-aware scheduling, and to guide future scheduler implementations in the most fruitful direction.
This paper quantifies the potential of locality-aware scheduling for unstructured parallelism on three different many-core processors. Our simulation results of 32-core systems show that locality-aware scheduling can bring up to 2.39x speedup over a randomized schedule, and 2.05x speedup over a state-of-the-art baseline scheduling scheme. At the same time, a locality-aware schedule reduces average energy consumption by 55% and 47%, relative to the random and the baseline schedule, respectively. In addition, our 1024-core simulation results project that these benefits will only increase: Compared to 32-core executions, we see up to 1.83x additional locality benefits. To capture such potentials in a practical setting, we also perform a detailed scheduler design space exploration to quantify the impact of different scheduling decisions. We also highlight the importance of locality-aware stealing, and demonstrate that a stealing scheme can exploit significant locality while performing load balancing. Over randomized stealing, our proposed scheme shows up to 2.0x speedup for stolen tasks.
