---
title: 'Zelda: Video analytics using vision-language models'
authors:
  - key: frankyromero
  - key: calebwinston
  - name: Johann Hauswald
    affiliation: Stanford
  - name: Matei Zaharia
    affiliation: UC Berkeley
  - key: christoskozyrakis
venue: preprint
year: 2023
date: 2023-05-01
doi: 
thumbnail: False
materials:
tags:
---
Advances in ML have motivated the design of video analytics systems that allow for structured queries over video datasets. However, existing systems limit query expressivity, require users to specify an ML model per predicate, rely on complex optimizations that trade off accuracy for performance, and return large amounts of redundant and low-quality results. This paper focuses on the recently developed Vision-Language Models (VLMs) that allow users to query images using natural language like "cars during daytime at traffic intersections." Through an in-depth analysis, we show VLMs address three limitations of current video analytics systems: general expressivity, a single general purpose model to query many predicates, and are both simple and fast. However, VLMs still return large numbers of redundant and low-quality results that can overwhelm and burden users. In addition, VLMs often require manual prompt engineering to improve result relevance. We present Zelda: a video analytics system that uses VLMs to return both relevant and semantically diverse results for top-K queries on large video datasets. Zelda prompts the VLM with the user's query in natural language. Zelda then automatically adds discriminator and synonym terms to boost accuracy, and terms to identify low-quality frames. To improve result diversity, Zelda uses semantic-rich VLM embeddings in an algorithm that prunes similar frames while considering their relevance to the query and the number of top-K results requested. We evaluate Zelda across five datasets and 19 queries and quantitatively show it achieves higher mean average precision (up to 1.15x) and …
