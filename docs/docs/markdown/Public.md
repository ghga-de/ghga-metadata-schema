
# Subset: public


Subset of properties that are considered to be public.

URI: [GHGA:public](https://w3id.org/GHGA/public)


### Classes


### Mixins


### Slots

 * [abstract](abstract.md) - The study abstract that describes the goals.  Can also hold abstract from a publication related to this study
 * [affiliation](affiliation.md) - The Institution(s) associated with an entity.
 * [analysis➞description](analysis_description.md) - Describing how an Analysis was carried out. (e.g.: computational tools, settings, etc.).
 * [analysis➞has study](analysis_has_study.md) - The Study entity associated with this Analysis.
 * [analysis➞reference chromosome](analysis_reference_chromosome.md)
 * [analysis➞reference genome](analysis_reference_genome.md)
 * [analysis➞type](analysis_type.md) - The type of the Analysis. Either Reference Alignment (BAM) or Sequence Variation (VCF)
 * [biological replicates](biological_replicates.md) - A biological replicate is a replicate role that consists of independent biological replicates made from different individual biosamples.
 * [biospecimen➞has anatomical entity](biospecimen_has_anatomical_entity.md) - The Anatomical entity, that represents the site, from which the Biospecimen was retrieved. Typically, a concept from Uber-anatomy Ontology (UBERON). For example, 'UBERON:0008307' indicates that the Biospecimen was extracted from the 'Heart Endothelium' of an Individual.
 * [biospecimen➞has disease](biospecimen_has_disease.md) - The Disease entity that is associated with the Individual. Typically, a concept from Mondo Disease Ontology. For example, 'MONDO:0005267' indicates that the Individual suffers from 'Heart Disease'.
 * [biospecimen➞type](biospecimen_type.md) - The type of Biospecimen.
 * [case control status](case_control_status.md) - Whether the sample is to be treated as Case or Control in a Study.
 * [cell barcode offset](cell_barcode_offset.md) - The offset in sequence of the cell identifying barcode. (Eg. '0').
 * [cell barcode read](cell_barcode_read.md) - The type of read that contains the cell barcode (eg: index1/index2/read1/read2).
 * [cell barcode size](cell_barcode_size.md) - The size of the cell identifying barcode (E.g. '16').
 * [checksum](checksum.md) - A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data. The receiving system recomputes the checksum based upon the received data and compares this value with the one sent with the data. If the two values are the same, the receiver has some confidence that the data was received correctly.
 * [checksum type](checksum_type.md) - The type of algorithm used to generate the checksum of a file.
 * [data access committee➞description](data_access_committee_description.md) - A description for the Data Access Committee.
 * [data access committee➞name](data_access_committee_name.md) - The name for the Data Access Committee.
 * [data access policy➞description](data_access_policy_description.md) - A short description for the Data Access Policy.
 * [data access policy➞name](data_access_policy_name.md) - A name for the Data Access Policy.
 * [dataset➞description](dataset_description.md)
 * [dataset➞has publication](dataset_has_publication.md) - One or more Publication entities associated with this Dataset.
 * [dataset➞has study](dataset_has_study.md) - One or more Study entities that are referenced by this Dataset.
 * [dataset➞title](dataset_title.md) - A title for the submitted Dataset.
 * [dataset➞type](dataset_type.md) - The type of a dataset.
 * [description](description.md) - Description of an entity.
 * [end bias](end_bias.md) - The end of the cDNA molecule that is preferentially sequenced, e.g. 3/5 prime tag or end, or the full-length transcript.
 * [experiment process➞title](experiment_process_title.md) - A descriptive title that explains the step(s) involved in performing the experiment leading up to the sequencing of the sample and generation of raw data from the instrument. (eg: Sample extraction -> Target Enrichment)
 * [experiment process➞type](experiment_process_type.md) - The type of experiment process.
 * [experiment➞description](experiment_description.md) - A detailed description of the Experiment.
 * [experiment➞has study](experiment_has_study.md) - The Study entity associated with this Experiment.
 * [experiment➞title](experiment_title.md) - Name for the experiment (eg: GHGAE_PBMC_RNAseq).
 * [experiment➞type](experiment_type.md) - The type of Experiment.
 * [experimental replicates](experimental_replicates.md) - The replicate number of the assay, i.e. the numeric iteration for the assay that was repeated.
 * [file➞checksum](file_checksum.md)
 * [file➞checksum type](file_checksum_type.md)
 * [file➞format](file_format.md)
 * [file➞name](file_name.md) - The given filename.
 * [flow cell id](flow_cell_id.md) - Flow Cell ID (eg: Experiment ID_Cell 1_Lane_1). The barcode assigned to a flow cell used in nucleotide sequencing.
 * [flow cell type](flow_cell_type.md) - Type of flow cell used (e.g. S4, S2 for NovaSeq; PromethION, Flongle for Nanopore). Aparatus in the fluidic subsystem where the sheath and sample meet. Can be one of several types; jet-in-air, quartz cuvette, or a hybrid of the two. The sample flows through the center of a fluid column of sheath fluid in the flow cell.
 * [format](format.md) - The format of the file: BAM, SAM, CRAM, BAI, etc.
 * [has anatomical entity](has_anatomical_entity.md) - Anatomical site associated with an entity.
 * [has disease](has_disease.md) - Disease concept that the entity is associated with.
 * [has project](has_project.md) - The project associated with an entity.
 * [has publication](has_publication.md) - The Publication associated with an entity.
 * [has study](has_study.md) - The study associated with an entity.
 * [index sequence](index_sequence.md) - A unique nucleotide sequence that is added to a sample during library preparation to serve as a unique identifier for the sample.
 * [individual➞has disease](individual_has_disease.md) - The Disease entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Mondo Disease Ontology. For example, 'MONDO:0003742' indicates that the Individual - from which the Biospecimen was extracted from - suffers from 'Heart Fibrosarcoma'.
 * [instrument model](instrument_model.md) - The name and model of the technology platform used to perform sequencing.
 * [isolation](isolation.md) - Method or device employed for collecting/isolating a biospecimen or a sample.
 * [lane number](lane_number.md) - The numerical identifier for the lane or machine unit where a sample was located during nucleotide sequencing.
 * [library layout](library_layout.md) - Describe whether the library was sequenced in single-end (forward or reverse) or paired-end mode
 * [library name](library_name.md) - A short name identifying the library to potential users. The same name may refer to multiple versions of the same continually updated library.
 * [library preparation](library_preparation.md) - The general method for sequencing library preparation (e.g. KAPA PCR-free).
 * [library preparation kit manufacturer](library_preparation_kit_manufacturer.md) - Manufacturer of library preparation kit
 * [library preparation kit retail name](library_preparation_kit_retail_name.md) - A unique identifier for the kit used to construct a genomic library. This may include the vendor name, kit name and kit version  (e.g. Agilent sure select Human Exome V8, Twist RefSeq Exome, etc.)
 * [library preparation protocol➞description](library_preparation_protocol_description.md) - Description about how a sequencing library was prepared (eg: Library construction method).
 * [library preparation protocol➞library layout](library_preparation_protocol_library_layout.md)
 * [library preparation protocol➞library name](library_preparation_protocol_library_name.md)
 * [library preparation protocol➞library preparation](library_preparation_protocol_library_preparation.md)
 * [library preparation protocol➞library preparation kit manufacturer](library_preparation_protocol_library_preparation_kit_manufacturer.md)
 * [library preparation protocol➞library preparation kit retail name](library_preparation_protocol_library_preparation_kit_retail_name.md)
 * [library preparation protocol➞library selection](library_preparation_protocol_library_selection.md)
 * [library preparation protocol➞library type](library_preparation_protocol_library_type.md)
 * [library selection](library_selection.md) - Whether any method was used to select for or against, enrich, or screen the material being sequenced. Library Selection method (e.g. random, PCA, cDNA, etc )
 * [library type](library_type.md) - Describe the level of omics analysis (eg: Metagenome, transcriptome, etc)
 * [name](name.md) - The name for an entity.
 * [named thing➞xref](named_thing_xref.md) - Holds one or more database cross references for an entity.
 * [ontology class mixin➞description](ontology_class_mixin_description.md) - The description or definition of an ontology class.
 * [ontology class mixin➞name](ontology_class_mixin_name.md) - The name or label (rdfs:label) of an ontology class.
 * [paired or single end](paired_or_single_end.md) - Denotes whether a submitted FASTQ file contains forward (R1) or reverse (R2) reads for paired-end sequencing. The number that identifies each read direction in a paired-end nucleotide sequencing replications.
 * [primer](primer.md) - The type of primer used for reverse transcription, e.g. 'oligo-dT' or 'random' primer. This allows users to identify content of the cDNA library input e.g. enriched for mRNA.
 * [project➞description](project_description.md) - Short textual description of the project.
 * [project➞has publication](project_has_publication.md) - One or more Publication entities associated with this Project.
 * [project➞title](project_title.md) - Comprehensive title for the project.
 * [protocol➞description](protocol_description.md) - Detailed description of the Protocol.
 * [protocol➞name](protocol_name.md) - Name of the protocol (eg: Sample extraction_PCR amplification).
 * [protocol➞type](protocol_type.md) - Type of the protocol (eg: Target enrichment).
 * [protocol➞xref](protocol_xref.md) - One or more cross-references for this Protocol.  (Eg: manufacturer protocol, protocol from publication etc )
 * [publication➞abstract](publication_abstract.md) - The study abstract that describes the goals. Can also hold abstract from a publication related to this study.
 * [publication➞title](publication_title.md) - The title for the Publication.
 * [publication➞xref](publication_xref.md) - One or more cross-references for this Publication.
 * [reference chromosome](reference_chromosome.md) - The reference chromosome used for this Analysis.
 * [reference genome](reference_genome.md) - A published genetic sequence that is used as a reference sequence against which other sequences are compared. Reference genome(s) or annotation(s) used for prior analyses (eg: GRCh38.p13).
 * [rnaseq strandedness](rnaseq_strandedness.md) - The strandedness of the library, whether reads come from both strands of the cDNA or only from the first (antisense) or the second (sense) strand.
 * [sample barcode read](sample_barcode_read.md) - The type of read that contains the sample barcode (eg: index1/index2/read1/read2).
 * [sample➞description](sample_description.md) - Short textual description of the sample (How the sample was collected, sample source, protocol followed for processing the sample etc).
 * [sample➞has anatomical entity](sample_has_anatomical_entity.md)
 * [sample➞name](sample_name.md) - Name of the sample (eg:GHGAS_Blood_Sample1 or GHGAS_PBMC_RNAseq_S1).
 * [sample➞type](sample_type.md) - The type of sample.
 * [sample➞xref](sample_xref.md) - One or more cross-references for this Sample. For example, this Sample may have an EBI BioSamples accession or an EGA Sample accession.
 * [sequencing center](sequencing_center.md) - Center where sample was sequenced.
 * [sequencing protocol➞description](sequencing_protocol_description.md) - Description about the sequencing protocol (eg: mRNA-seq,Whole exome long-read sequencing etc).
 * [sequencing protocol➞instrument model](sequencing_protocol_instrument_model.md)
 * [sequencing protocol➞type](sequencing_protocol_type.md) - Name of the library preparation protocol (eg: mRNA-seq,Whole exome long-read sequencing etc).
 * [storage](storage.md) - Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).
 * [study➞affiliation](study_affiliation.md)
 * [study➞description](study_description.md) - A detailed description (abstract) that describes the goals of this Study.
 * [study➞has project](study_has_project.md) - The project associated with this Study.
 * [study➞has publication](study_has_publication.md) - One or more Publication entities associated with this Study.
 * [study➞title](study_title.md) - A comprehensive title for the study.
 * [study➞type](study_type.md) - The type of Study. For example, 'Cancer Genomics', 'Epigenetics', 'Exome Sequencing'.
 * [submission➞affiliation](submission_affiliation.md) - Institution/Center/Data Hub that is providing this submission.
 * [submission➞has project](submission_has_project.md) - Information about a Project entity associated with this submission.
 * [submission➞has publication](submission_has_publication.md) - One or more Publication entities associated with this Submission.
 * [submission➞has study](submission_has_study.md) - Information about a Study entities associated with this submission.
 * [target regions](target_regions.md) - Subset of genes or specific regions of the genome, which are most likely to be involved in the phenotype under study.
 * [technical replicates](technical_replicates.md) - A technical replicate is a replicate role where the same BioSample is use e.g. the same pool of RNA used to assess technical (as opposed to biological) variation within an experiment.
 * [tissue](tissue.md) - An anatomical structure consisting of similarly specialized cells and intercellular matrix, aggregated according to genetically determined spatial relationships, performing a specific function.
 * [title](title.md) - The title that describes an entity.
 * [type](type.md) - The type of an entity.
 * [umi barcode offset](umi_barcode_offset.md) - The offset in sequence of the UMI identifying barcode. (E.g. '16').
 * [umi barcode read](umi_barcode_read.md) - The type of read that contains the UMI barcode (Eg: index1/index2/read1/read2).
 * [umi barcode size](umi_barcode_size.md) - The size of the UMI identifying barcode (Eg. '10').
 * [vital status at sampling](vital_status_at_sampling.md) - Vital Status of an Individual at the point of sampling (eg:'Alive', 'Deceased').
 * [workflow➞name](workflow_name.md)
 * [xref](xref.md) - Database cross references for an entity.

### Types


### Enums

