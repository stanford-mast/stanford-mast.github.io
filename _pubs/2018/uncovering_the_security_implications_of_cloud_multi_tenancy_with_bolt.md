---
title: 'Uncovering the Security Implications of Cloud Multi-Tenancy with Bolt'
authors:
  - key: christinadelimitrou
  - key: christoskozyrakis
venue: micro
year: 2018
date: 2018-05-01
doi: 10.1109/MM.2018.032271065
thumbnail: False
materials:
tags:
---
Cloud providers routinely schedule multiple applications per physical host to increase efficiency. The resulting interference on shared resources often leads to performance degradation and, more importantly, security vulnerabilities. Interference can leak important information about an application, ranging from a services placement to confidential data, such as private keys. We present Bolt, a practical system that accurately detects the type and characteristics of applications sharing a cloud platform based on the interference an adversary sees on shared resources. Bolt leverages online data mining techniques that only require 2-5 seconds for detection. In a multi-user study on Amazon Elastic Compute Cloud (EC2), Bolt correctly identifies the characteristics of 385 out of a set of 436 diverse workloads. Extracting this information enables a wide spectrum of previously impractical cloud attacks, including denial of service (DoS) attacks that increase tail latency by 140X, as well as resource freeing attacks (RFAs), and co-residency attacks. Finally, we show that, while advanced isolation mechanisms such as cache partitioning lower detection accuracy, they are insufficient to eliminate these vulnerabilities altogether. To do so, one must either disallow core sharing or allow it only between threads of the same application, leading to significant inefficiencies and performance penalties.
