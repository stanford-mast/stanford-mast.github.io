---
title: 'Sglang: Efficient execution of structured language model programs'
authors:
  - name: Lianmin Zheng
    affiliation: UC Berkeley
  - name: Liangsheng Yin
  - key: zhiqiangxie
  - name: Chuyue Livia Sun
    affiliation: Stanford
  - name: Jeff Huang
  - name: Cody Hao Yu
  - name: Shiyi Cao
    affiliation: UC Berkeley
  - key: christoskozyrakis
  - name: Ion Stoica
    affiliation: UC Berkeley
  - name: Joseph E Gonzalez
    affiliation: UC Berkeley
  - name: Clark Barrett
    affiliation: Stanford
  - name: Ying Sheng
    affiliation: Stanford
venue: neurips
year: 2024
date: 2024-12-01
doi: 10.48550/arXiv.2312.07104
thumbnail: False
materials:
tags:
---
Large language models (LLMs) are increasingly used for complex tasks that require multiple generation calls, advanced prompting techniques, control flow, and structured inputs/outputs. However, efficient systems are lacking for programming and executing these applications. We introduce SGLang, a system for efficient execution of complex language model programs. SGLang consists of a frontend language and a runtime. The frontend simplifies programming with primitives for generation and parallelism control. The runtime accelerates execution with novel optimizations like RadixAttention for KV cache reuse and compressed finite state machines for faster structured output decoding. Experiments show that SGLang achieves up tohigher throughput compared to state-of-the-art inference systems on various large language and multi-modal models on tasks including agent control, logical reasoning, few-shot learning benchmarks, JSON decoding, retrieval-augmented generation pipelines, and multi-turn chat. The code is publicly available at https://github. com/sgl-project/sglang.
