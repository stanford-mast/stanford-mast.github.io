---
title: 'A case against (most) context switches'
authors:
  - key: jackhumphries
    equal: True
  - key: kostiskaffes
    equal: True
  - name: David Mazières
    affiliation: Stanford
  - key: christoskozyrakis
venue: hotos
year: 2021
date: 2021-06-01
doi: 10.1145/3458336.3465274
thumbnail: True
materials:
tags:
---
Multiplexing software threads onto hardware threads and serving interrupts, VM-exits, and system calls require frequent context switches, causing high overheads and significant kernel and application complexity. We argue that context switching is an idea whose time has come and gone, and propose eliminating it through a radically different hardware threading model targeted to solve software rather than hardware problems. The new model adds a large number of hardware threads to each physical core - making thread multiplexing unnecessary - and lets software manage them. The only state change directly triggered in hardware by system calls, exceptions, and asynchronous hardware events will be blocking and unblocking hardware threads. We also present ISA extensions to allow kernel and user software to exploit this new threading model. Developers can use these extensions to eliminate interrupts and …
