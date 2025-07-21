---
title: 'Shef: Shielded enclaves for cloud fpgas'
authors:
  - key: markzhao
  - key: mingyugao
  - key: christoskozyrakis
venue: preprint
year: 2022
date: 2022-02-01
doi: 
thumbnail: False
materials:
tags:
---
FPGAs are now used in public clouds to accelerate a wide range of applications, including many that operate on sensitive data such as financial and medical records. We present ShEF, a trusted execution environment (TEE) for cloud-based reconfigurable accelerators. ShEF is independent from CPU-based TEEs and allows secure execution under a threat model where the adversary can control all software running on the CPU connected to the FPGA, has physical access to the FPGA, and can compromise the FPGA interface logic of the cloud provider. ShEF provides a secure boot and remote attestation process that relies solely on existing FPGA mechanisms for root of trust. It also includes a Shield component that provides secure access to data while the accelerator is in use. The Shield is highly customizable and extensible, allowing users to craft a bespoke security solution that fits their accelerator's memory …
