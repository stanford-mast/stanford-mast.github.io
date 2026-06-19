# Publication Manual Check Issues
Generated: 2026-06-19

This is an additional consistency pass over `_pubs/**/*.md` after the missing-paper and abstract cleanup work.

Resolved items were removed after Christos reviewed the checklist and provided notes. The remaining items below are not necessarily errors; they are still-open manual-review candidates.

Checks with no findings:
- Undefined venue keys: 0
- Undefined author keys: 0
- Duplicate normalized titles: 0
- Duplicate DOI values: 0
- Path year differs from publication year: resolved by moving pages to their publication-year directories
- Previously flagged accepted-venue arXiv DOI/material issues: resolved or confirmed okay

## Publisher Venue With Blank DOI

Most USENIX/ATC/PMLR cases were resolved by adding or confirming canonical venue pages under `materials`. IEEE/IEEE Micro cases with Crossref DOI matches were updated. These remaining entries still have blank DOI values and did not produce a trustworthy DOI match in the automated search.

- `_pubs/2009/energy_dumpster_diving.md` — venue `hotpower`
- `_pubs/2009/smart_memories_polymorphic_chip_multiprocessor.md` — venue `dac`
- `_pubs/2011/accurate_modeling_and_generation_of_storage_i_o_for_datacenter_workloads.md` — venue `tos`

## No DOI And No Material

These are pages without either a DOI value or a material link. Some may be acceptable, but they are worth checking for discoverability.

- `_pubs/2004/viram1_a_media_oriented_vector_processor_with_embedded_dram.md` — venue `dacontest`
- `_pubs/2005/smart_memories_a_configurable_processor_architecture_for_high_productivity_parallel_programming.md` — venue `preprint`
- `_pubs/2006/deconstructing_hardware_architectures_for_security.md` — venue `ddd`
- `_pubs/2006/library_based_prefetching_for_pointer_intensive_applications.md` — venue `report`
- `_pubs/2006/parallelizing_specjbb2000_with_transactional_memory.md` — venue `wtw`
- `_pubs/2006/the_software_stack_for_transactional_memory.md` — venue `stmcs`
- `_pubs/2014/high_performance_hardware_accelerated_flash_key_value_store.md` — venue `nvmw`
