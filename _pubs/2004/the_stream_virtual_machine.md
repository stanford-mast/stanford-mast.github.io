---
title: 'The stream virtual machine'
authors:
  - name: Francois Labonte
  - name: Peter Mattson
  - name: William Thies
  - name: Ian Buck
  - key: christoskozyrakis
  - name: Mark Horowitz
venue: pact
year: 2004
date: 2004-09-01
doi: 10.1109/pact.2004.1342560
thumbnail: False
materials:
tags:
  - architecture
---
Stream programming is currently being pushed as a way to expose concurrency and separate communication from computation. Since there are many stream languages and potential stream execution engines, we propose an abstract machine model that captures the essential characteristics of stream architectures, the stream virtual machine (SVM). The goal of the SVM is to improve interoperability, allow development of common compilation tools and reason about stream program performance. The SVM contains control processors, slave kernel processors, and slave DMA units. The compilation process takes a stream program down to the SVM and finally down to machine binary. To extract the parameters for our SVM model, we use micro-kernels to characterize two graphics processors and a stream engine, Imagine. The results are encouraging; the model estimates the performance of the target machines with high accuracy.
