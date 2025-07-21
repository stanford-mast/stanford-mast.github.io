---
title: 'Uncovering the Security Implications of Cloud Multi-Tenancy with Bolt'
authors:
  - key: christinadelimitrou
  - key: christoskozyrakis
venue: preprint
year: 2018
date: 2018-05-01
doi: 
thumbnail: False
materials:
tags:
---
Cloud providers routinely schedule multiple applications per physical host to increase efficiency. The resulting interference on shared resources often leads to performance degradation and, more importantly, security vulnerabilities. Interference can leak important information about an application, ranging from a services placement to confidential data, such as private keys. We present Bolt, a practical system that accurately detects the type and characteristics of applications sharing a cloud platform based on the interference an adversary sees on shared resources. Bolt leverages online data mining techniques that only require 2-5 seconds for detection. In a multi-user study on Amazon Elastic Compute Cloud (EC2), Bolt correctly identifies the characteristics of 385 out of a set of 436 diverse workloads. Extracting this information enables a wide spectrum of previously impractical cloud attacks, including denial of …
