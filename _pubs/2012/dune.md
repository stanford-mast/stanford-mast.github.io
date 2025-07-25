---
title: 'Dune: Safe User-level Access to Privileged CPU Features'
authors:
  - key: adambelay
  - name: Andrea Bittau
    affiliation: Stanford
  - name: Ali Mashtizadeh
    affiliation: Stanford
  - name: David Terei
    affiliation: Stanford
  - name: David Mazières
    affiliation: Stanford
  - key: christoskozyrakis
venue: osdi
year: 2012
date: 2012-04-01
doi: 
thumbnail: False
materials:
tags:
---
Dune is a system that provides applications with direct but safe access to hardware features such as ring protection, page tables, and tagged TLBs, while preserving the existing OS interfaces for processes. Dune uses the virtualization hardware in modern processors to provide a process, rather than a machine abstraction. It consists of a small kernel module that initializes virtualization hardware and mediates interactions with the kernel, and a user-level library that helps applications manage privileged hardware features. We present the implementation of Dune for 64bit x86 Linux. We use Dune to implement three userlevel applications that can benefit from access to privileged hardware: a sandbox for untrusted code, a privilege separation facility, and a garbage collector. The use of Dune greatly simplifies the implementation of these applications and provides significant performance advantages.


