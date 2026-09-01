---
title: 'ROSA: A Robotics Foundation Model Serving System for Robot Factories'
authors:
  - name: Wenqi Jiang
  - name: Jason Clemons
  - name: Rowland O'Flaherty
  - name: Hugo Hadfield
  - name: Alperen Degirmenci
  - name: Shuran Song
  - name: Yashraj Narang
  - key: christoskozyrakis
venue: preprint
year: 2026
date: 2026-07-01
doi: 10.48550/arXiv.2607.01088
thumbnail: True
materials:
  - name: paper
    url: /pubs/rosa_a_robotics_foundation_model_serving_system_for_robot_factories/paper.pdf
    type: file-pdf
  - name: arXiv
    url: https://doi.org/10.48550/arXiv.2607.01088
    type: file-alt
tags:
  - cloud
  - AI-systems
  - datacenter-systems
  - resource-management
  - low-latency
  - gpu-systems
---
Robotics foundation models (RFMs) are making general-purpose robots increasingly practical for factory deployments. While RFM serving systems are central to this vision, existing systems are largely shaped by a single-robot, single-model assumption: inference is treated as an edge-computing problem handled by an on-robot or dedicated nearby GPU, and the serving objective is to minimize the latency of a single action model. In this paper, we propose ROSA, an RFM serving system for robot factories designed around three key principles. First, ROSA adopts shared GPU-pool serving, allowing a fleet of robots to access powerful server-class GPUs over the network in order to improve inference performance, battery duration, and GPU utilization. Second, ROSA provides a robotics-aware programming abstraction and system design that supports multi-model pipelines, per-task performance requirements, and failure handling. Third, ROSA uses factory-objective-driven scheduling to maximize SLO-qualified factory productivity rather than minimizing individual request latency. We implement ROSA on top of Ray Serve for distributed orchestration, with vLLM, PyTorch, and JAX as model-serving backends, and evaluate it on both real robots and synthetic large-scale workloads. The results show that ROSA improves factory productivity by up to 12.06x over conventional dedicated serving systems.
