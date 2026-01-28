---
title: 'Bolt: I know what you did last summer... in the cloud'
authors:
  - key: christinadelimitrou
  - key: christoskozyrakis
venue: asplos
year: 2017
date: 2017-04-01
doi: 10.1145/3093337.3037703
thumbnail: True
materials:
tags:
---
Cloud providers routinely schedule multiple applications per physical host to increase efficiency. The resulting interference on shared resources often leads to performance degradation and, more importantly, security vulnerabilities. Interference can leak important information ranging from a service's placement to confidential data, like private keys. We present Bolt, a practical system that accurately detects the type and characteristics of applications sharing a cloud platform based on the interference an adversary sees on shared resources. Bolt leverages online data mining techniques that only require 2-5 seconds for detection. In a multi-user study on EC2, Bolt correctly identifies the characteristics of 385 out of 436 diverse workloads. Extracting this information enables a wide spectrum of previously-impractical cloud attacks, including denial of service attacks (DoS) that increase tail latency by 140x, as well as …
