---
title: 'Dynamic management of TurboMode in modern multi-core chips'
authors:
  - key: davidlo
  - key: christoskozyrakis
venue: hpca
year: 2014
date: 2014-06-01
doi: 10.1109/HPCA.2014.6835969
thumbnail: True
materials:
tags:
---
Dynamic overclocking of CPUs, or TurboMode, is a feature recently introduced on all x86 multi-core chips. It leverages thermal and power headroom from idle execution resources to overclock active cores to increase performance. TurboMode can accelerate CPU-bound applications at the cost of additional power consumption. Nevertheless, naive use of TurboMode can significantly increase power consumption without increasing performance. Thus far, there is no strategy for managing TurboMode to optimize its use across all workloads and efficiency metrics. This paper analyzes the impact of TurboMode on a wide range of efficiency metrics (performance, power, cost, and combined metrics such as QPS/W and ED2) for representative server workloads on various hardware configurations. We determine that TurboMode is generally beneficial for performance (up to +24%), cost efficiency (QPS/upto+8, ED, and ED2 by 8%, 47%, and 68% respectively over not using TurboMode. At the same time, autoturbo virtually eliminates all the large drops in those same metrics (-12%, -25%, -25% for QPS/$, ED, and ED2) that occur when TurboMode is used naively (always on).
