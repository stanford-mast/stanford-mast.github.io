---
title: 'INFaaS: A model-less and managed inference serving system'
authors:
  - key: frankyromero
  - key: qianli
  - name: Neeraja J Yadwadkar
    affiliation: Stanford
  - key: christoskozyrakis
venue: atc
year: 2019
date: 2019-05-01
doi: 10.48550/arXiv.1905.13348
thumbnail: False
materials:
tags:
---
Despite existing work in machine learning inference serving, ease-of-use and cost efficiency remain challenges at large scales. Developers must manually search through thousands of model-variants -- versions of already-trained models that differ in hardware, resource footprints, latencies, costs, and accuracies -- to meet the diverse application requirements. Since requirements, query load, and applications themselves evolve over time, these decisions need to be made dynamically for each inference query to avoid excessive costs through naive autoscaling. To avoid navigating through the large and complex trade-off space of model-variants, developers often fix a variant across queries, and replicate it when load increases. However, given the diversity across variants and hardware platforms in the cloud, a lack of understanding of the trade-off space can incur significant costs to developers. This paper introduces INFaaS, a managed and model-less system for distributed inference serving, where developers simply specify the performance and accuracy requirements for their applications without needing to specify a specific model-variant for each query. INFaaS generates model-variants, and efficiently navigates the large trade-off space of model-variants on behalf of developers to meet application-specific objectives: (a) for each query, it selects a model, hardware architecture, and model optimizations, (b) it combines VM-level horizontal autoscaling with model-level autoscaling, where multiple, different model-variants are used to serve queries within each machine. By leveraging diverse variants and sharing hardware resources across models …
