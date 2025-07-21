---
title: 'Appswitch: Resolving the application identity crisis'
authors:
  - name: Dinesh Subhraveti
  - name: Sri Goli
  - name: Serge Hallyn
  - name: Ravi Chamarthy
  - key: christoskozyrakis
venue: preprint
year: 2017
date: 2017-11-01
doi: 
thumbnail: False
materials:
tags:
---
Networked applications traditionally derive their identity from the identity of the host on which they run. The default application identity acquired from the host results in subtle and substantial problems related to application deployment, discovery and access, especially for modern distributed applications. A number of mechanisms and workarounds, often quite elaborate, are used to address those problems but they only address them indirectly and incompletely. This paper presents AppSwitch, a novel transport layer network element that decouples applications from underlying network at the system call layer and enables them to be identified independently of the network. Without requiring changes to existing applications or infrastructure, it removes the cost and complexity associated with operating distributed applications while offering a number of benefits including an efficient implementation of common network functions such as application firewall and load balancer. Experiments with our implementation show that AppSwitch model also effectively removes the performance penalty associated with unnecessary data path processing that is typical in those application environments.
