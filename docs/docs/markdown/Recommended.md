
# Subset: recommended


Subset of properties that are considered to be of importance for FAIR data sharing.

URI: [GHGA:recommended](https://w3id.org/GHGA/recommended)


### Classes


### Mixins


### Slots

 * [biospecimen➞has anatomical entity](biospecimen_has_anatomical_entity.md) - The Anatomical entity, that represents the site, from which the Biospecimen was retrieved. Typically, a concept from Uber-anatomy Ontology (UBERON). For example, 'UBERON:0008307' indicates that the Biospecimen was extracted from the 'Heart Endothelium' of an Individual.
 * [case control status](case_control_status.md) - Whether the sample is to be treated as Case or Control in a Study.
 * [cell barcode offset](cell_barcode_offset.md) - The offset in sequence of the cell identifying barcode. (Eg. '0').
 * [cell barcode read](cell_barcode_read.md) - The type of read that contains the cell barcode (eg: index1/index2/read1/read2).
 * [cell barcode size](cell_barcode_size.md) - The size of the cell identifying barcode (E.g. '16').
 * [data access policy➞has data use condition](data_access_policy_has_data_use_condition.md) - Data Use Condition entities that are associated with the Data Access Policy.
 * [data access policy➞policy url](data_access_policy_policy_url.md) - URL for the policy, if available. This is useful if the terms of the policy is made available online at a resolvable URL.
 * [data use condition➞has data use modifier](data_use_condition_has_data_use_modifier.md) - Modifier for Data use permission associated with a policy. Should be descendants of 'DUO:0000017 data use modifier'
 * [data use condition➞has data use permission](data_use_condition_has_data_use_permission.md) - Data use permission associated with a policy. Typically one or more terms from DUO and should be descendants of 'DUO:0000001 data use permission'.
 * [end bias](end_bias.md) - The end of the cDNA molecule that is preferentially sequenced, e.g. 3/5 prime tag or end, or the full-length transcript.
 * [flow cell id](flow_cell_id.md) - Flow Cell ID (eg: Experiment ID_Cell 1_Lane_1). The barcode assigned to a flow cell used in nucleotide sequencing.
 * [flow cell type](flow_cell_type.md) - Type of flow cell used (e.g. S4, S2 for NovaSeq; PromethION, Flongle for Nanopore). Aparatus in the fluidic subsystem where the sheath and sample meet. Can be one of several types; jet-in-air, quartz cuvette, or a hybrid of the two. The sample flows through the center of a fluid column of sheath fluid in the flow cell.
 * [forward or reverse](forward_or_reverse.md) - Denotes whether a submitted FASTQ file contains forward (R1) or reverse (R2) reads for paired-end sequencing. The number that identifies each read direction in a paired-end nucleotide sequencing reaction.
 * [has anatomical entity](has_anatomical_entity.md) - Anatomical site associated with an entity.
 * [has data use condition](has_data_use_condition.md) - Data Use Condition entities that are associated with an entity.
 * [has data use modifier](has_data_use_modifier.md) - Modifier for Data use permission associated with an entity. Should be descendants of 'DUO:0000017 data use modifier'
 * [has data use permission](has_data_use_permission.md) - Data use permission associated with an entity. Typically one or more terms from DUO. Should be descendants of 'DUO:0000001 data use permission'.
 * [index sequence](index_sequence.md) - A unique nucleotide sequence that is added to a sample during library preparation to serve as a unique identifier for the sample.
 * [isolation](isolation.md) - Method or device employed for collecting/isolating a biospecimen or a sample.
 * [lane number](lane_number.md) - The numerical identifier for the lane or machine unit where a sample was located during nucleotide sequencing.
 * [library preparation kit manufacturer](library_preparation_kit_manufacturer.md) - Manufacturer of library preparation kit
 * [library preparation kit retail name](library_preparation_kit_retail_name.md) - A unique identifier for the kit used to construct a genomic library. This may include the vendor name, kit name and kit version  (e.g. Agilent sure select Human Exome V8, Twist RefSeq Exome, etc.)
 * [library preparation protocol➞library preparation kit manufacturer](library_preparation_protocol_library_preparation_kit_manufacturer.md)
 * [library preparation protocol➞library preparation kit retail name](library_preparation_protocol_library_preparation_kit_retail_name.md)
 * [paired or single end](paired_or_single_end.md) - Denotes whether a submitted FASTQ file contains forward (R1) or reverse (R2) reads for paired-end sequencing. The number that identifies each read direction in a paired-end nucleotide sequencing replications.
 * [policy url](policy_url.md) - Alternative to pasting the Data Access Policy text.
 * [primer](primer.md) - The type of primer used for reverse transcription, e.g. 'oligo-dT' or 'random' primer. This allows users to identify content of the cDNA library input e.g. enriched for mRNA.
 * [rnaseq strandedness](rnaseq_strandedness.md) - The strandedness of the library, whether reads come from both strands of the cDNA or only from the first (antisense) or the second (sense) strand.
 * [sample barcode read](sample_barcode_read.md) - The type of read that contains the sample barcode (eg: index1/index2/read1/read2).
 * [sample➞has anatomical entity](sample_has_anatomical_entity.md)
 * [sequencing center](sequencing_center.md) - Center where sample was sequenced.
 * [storage](storage.md) - Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).
 * [umi barcode offset](umi_barcode_offset.md) - The offset in sequence of the UMI identifying barcode. (E.g. '16').
 * [umi barcode read](umi_barcode_read.md) - The type of read that contains the UMI barcode (Eg: index1/index2/read1/read2).
 * [umi barcode size](umi_barcode_size.md) - The size of the UMI identifying barcode (Eg. '10').
 * [vital status at sampling](vital_status_at_sampling.md) - Vital Status of an Individual at the point of sampling (eg:'Alive', 'Deceased').

### Types


### Enums

