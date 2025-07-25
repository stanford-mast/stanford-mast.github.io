---
title: 'Tainting is not pointless'
authors:
  - key: michaeldalton
  - key: harikannan
  - key: christoskozyrakis
venue: sigopsreview
year: 2010
date: 2010-04-01
doi: 10.1145/1773912.1773933
thumbnail: False
materials:
tags:
---
Pointer tainting is a form of Dynamic Information Flow Tracking used primarily to prevent software security attacks such as buffer overflows. Researchers have also applied pointer tainting to malware and virus analysis.
A recent paper by Slowinska and Bos has criticized pointer tainting as a security mechanism, arguing that it is has serious, inherent false positive and false negative defects. We present a rebuttal that addresses the confusion due to the two uses of pointer tainting in security literature. We clarify that many of the arguments against pointer tainting apply only to its use as a malware and virus analysis platform, but do not apply to the application of pointer tainting to memory corruption protection. Hence, we argue that pointer tainting remains a useful and promising technique for robust protection against memory corruption attacks.
