---
title: 'Power management of datacenter workloads using per-core power gating'
authors:
  - key: jacobleverich
  - name: Matteo Monchiero
  - name: Vanish Talwar
  - name: Parthasarathy Ranganathan
    affiliation: Google
  - key: christoskozyrakis
venue: archletters
year: 2009
date: 2009-08-01
doi: 10.1109/L-CA.2009.46
thumbnail: False
materials:
tags:
---
While modern processors offer a wide spectrum of software-controlled power modes, most datacenters only rely on Dynamic Voltage and Frequency Scaling (DVFS, a.k.a. P-states) to achieve energy efficiency. This paper argues that, in the case of datacenter workloads, DVFS is not the only option for processor power management. We make the case for per-core power gating (PCPG) as an additional power management knob for multi-core processors. PCPG is the ability to cut the voltage supply to selected cores, thus reducing to almost zero the leakage power for the gated cores. Using a testbed based on a commercial 4-core chip and a set of real-world application traces from enterprise environments, we have evaluated the potential of PCPG. We show that PCPG can significantly reduce a processor's energy consumption (up to 40%) without significant performance overheads. When compared to DVFS, PCPG is highly effective saving up to 30% more energy than DVFS. When DVFS and PCPG operate together they can save up to almost 60%.
