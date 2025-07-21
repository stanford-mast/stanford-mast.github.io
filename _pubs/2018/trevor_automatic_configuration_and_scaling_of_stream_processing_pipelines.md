---
title: 'Trevor: Automatic configuration and scaling of stream processing pipelines'
authors:
  - name: Manu Bansal
  - name: Eyal Cidon
  - name: Arjun Balasingam
  - name: Aditya Gudipati
  - key: christoskozyrakis
  - name: Sachin Katti
venue: preprint
year: 2018
date: 2018-12-01
doi: 
thumbnail: False
materials:
tags:
---
Operating a distributed data stream processing workload efficiently at scale is hard. The operator of the workload must parallelize and lay out tasks of the workload with resources that match the requirement of target data rate. The challenge is that neither the operator nor the programmer is typically aware of the scaling behavior of the workload as a function of resources. An operator manually searches for a safe operating point that can handle predicted peak load and deploys with ample headroom for absorbing unpredictable spikes. Such empirical, static over-provisioning is wasteful of both compute and human resources. We show that precise performance models can be automatically learned for distributed stream processing systems that can predict the execution performance of a job even before deployment. Further, those models can be used to optimally schedule logically specified jobs onto available physical hardware. Finally, those models and the derived execution schedules can be refined online to dynamically adapt to unpredictable changes in the runtime environment or auto-scale with variations in job load.
