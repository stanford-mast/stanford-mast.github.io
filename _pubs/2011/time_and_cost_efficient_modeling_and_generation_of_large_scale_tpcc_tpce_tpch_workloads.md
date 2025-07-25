---
title: 'Time and cost-efficient modeling and generation of large-scale tpcc/tpce/tpch workloads'
authors:
  - key: christinadelimitrou
  - name: Sriram Sankar
  - name: Badriddine Khessib
  - name: Kushagra Vaid
  - key: christoskozyrakis
venue: tpctc
year: 2011
date: 2011-08-01
doi: 10.1007/978-3-642-32627-1_11
thumbnail: False
materials:
tags:
---
Large-scale TPC workloads are critical for the evaluation of datacenter-scale storage systems. However, these workloads have not been previously characterized, in-depth, and modeled in a DC environment. In this work, we categorize the TPC workloads into storage threads that have unique features and characterize the storage activity of TPCC, TPCE and TPCH based on I/O traces from real server installations. We also propose a framework for modeling and generation of large-scale TPC workloads, which allows us to conduct a wide spectrum of storage experiments without requiring knowledge on the structure of the application or the overhead of fully deploying it in different storage configurations. Using our framework, we eliminate the time for TPC setup and reduce the time for experiments by two orders of magnitude, due to the compression in storage activity enforced by the model. We demonstrate the accuracy of the model and the applicability of our method to significant datacenter storage challenges, including identification of early disk errors, and SSD caching.
