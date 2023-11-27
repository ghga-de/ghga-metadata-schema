
# GHGA-Submission-Metadata-Schema


**metamodel version:** 1.7.0

**version:** 1.1.1


The submission centric metadata schema for the German Human Genome-Phenome Archive (GHGA).


### Classes

 * [Analysis](Analysis.md) - An Analysis is a data transformation that transforms input data to output data.
 * [AnalysisProcess](AnalysisProcess.md) - An Analysis Process captures the workflow steps that were performed to analyze data obtained from a Sequencing Experiment.
 * [Attribute](Attribute.md) - A key/value pair that further characterizes an entity.
 * [Biospecimen](Biospecimen.md) - A Biospecimen is any natural material taken from a biological entity for testing, diagnostics, treatment, or research purposes.  It is linked to the Individual from which the Biospecimen is derived.
 * [Condition](Condition.md) - A Condition specifies which special characteristics and treatments apply to a Sample. It is used to link comparable Samples (e.g., healthy Samples, wildtype Samples).
 * [DataAccessCommittee](DataAccessCommittee.md) - A group of members that are delegated to grant access to one or more datasets after ensuring the criteria for data sharing has been met,  and request for data use does not raise ethical and/or legal concerns.
 * [DataAccessPolicy](DataAccessPolicy.md) - A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.
 * [Dataset](Dataset.md) - A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
 * [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.
     * [AnalysisProcessOutputFile](AnalysisProcessOutputFile.md) - A Analysis Process OutputFile is a File that is associated as an output file with an Analysis Process.
     * [SampleFile](SampleFile.md) - A Sample File is a File that is associated with a Sample.
     * [SequencingProcessFile](SequencingProcessFile.md) - A Sequencing Process File is a File that is associated with a Sequencing Process.
     * [StudyFile](StudyFile.md) - A Study File is a File that is associated with a Study.
 * [Individual](Individual.md) - An Individual is a Person who is participating in a Study.
 * [LibraryPreparationProtocol](LibraryPreparationProtocol.md) - The Library Preparation Protocol captures information about the library preparation of a Sequencing Experiment.
 * [Publication](Publication.md) - A Publication represents an article that is published. The minimum expectation is that the publication has a valid DOI.
 * [Sample](Sample.md) - A Sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use.  It is prepared from a Biospecimen.
 * [SequencingExperiment](SequencingExperiment.md) - A Sequencing Experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
 * [SequencingProcess](SequencingProcess.md) - The Sequencing Process captures the technical parameters that were used to produce sequencing output from the Sample. It links the Sample to sequencing output.
 * [SequencingProtocol](SequencingProtocol.md) - The Sequencing Protocol captures information about parameters and metadata associated with a Sequencing Experiment.
 * [Study](Study.md) - A Study is an experimental investigation of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.
 * [Submission](Submission.md) - A grouping entity that represents information about one or more entities. A submission can be considered as a set of inter-related (and inter-connected) entities that represent a data submission to GHGA.
 * [Trio](Trio.md) - A Trio is a study design in which the genetic information of three individuals within a family unit is analyzed. It consists of a child and their biological parents.

### Mixins

 * [AliasMixin](AliasMixin.md) - Mixin for entities that can be assigned an alias at the time of metadata submission.
     * [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 * [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.
 * [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

### Slots

 * [abstract](abstract.md) - The study abstract that describes the goals. Can also hold abstract from a publication related to this Study
     * [Publication➞abstract](Publication_abstract.md) - The study abstract that describes the goals. Can also hold abstract from a Publication related to this Study.
 * [affiliations](affiliations.md) - The Institution(s) associated with an entity.
     * [Study➞affiliations](Study_affiliations.md) - The affiliations associated with this Study.
 * [age_at_sampling](age_at_sampling.md) - The age of the Individual.
     * [Biospecimen➞age_at_sampling](Biospecimen_age_at_sampling.md)
 * [alias](alias.md) - The alias for an entity at the time of submission.
     * [AliasMixin➞alias](AliasMixin_alias.md)
         * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)
 * [analyses](analyses.md) - The Analyses associated with an entity.
     * [Submission➞analyses](Submission_analyses.md) - One or more Analysis entities associated with this Submission.
 * [analysis](analysis.md) - The Analysis associated with an entity
     * [AnalysisProcess➞analysis](AnalysisProcess_analysis.md) - The Analysis that this Analysis Process is part of.
 * [analysis_process](analysis_process.md) - The Analysis Process associated with an entity.
     * [AnalysisProcessOutputFile➞analysis_process](AnalysisProcessOutputFile_analysis_process.md) - The Analysis Process this Analysis Process Output File is associated with.
 * [analysis_process_output_files](analysis_process_output_files.md) - The Analysis Process Output Files associated with an entity.
     * [Submission➞analysis_process_output_files](Submission_analysis_process_output_files.md) - The Analysis Process Output Files that are part of this Submission.
 * [analysis_processes](analysis_processes.md) - The Analysis Processes associated with an entity.
     * [Submission➞analysis_processes](Submission_analysis_processes.md) - The Analysis Processes that are part of this Submission.
 * [ancestries](ancestries.md) - A person's descent or lineage from a population.
     * [Individual➞ancestries](Individual_ancestries.md)
 * [attributes](attributes.md) - Key/value pairs corresponding to an entity.
     * [AttributeMixin➞attributes](AttributeMixin_attributes.md)
         * [LibraryPreparationProtocol➞attributes](LibraryPreparationProtocol_attributes.md) - One or more attributes that further characterize this Library Preparation Protocol.
         * [SequencingProtocol➞attributes](SequencingProtocol_attributes.md) - One or more attributes that further characterize this Sequencing Protocol.
         * [Study➞attributes](Study_attributes.md) - One or more attributes that further characterize this Study.
 * [author](author.md) - The individual who is responsible for the content of the Publication.
     * [Publication➞author](Publication_author.md) - Author(s) of this Publication.
 * [biospecimen](biospecimen.md) - The Biospecimen associated with an entity.
     * [Sample➞biospecimen](Sample_biospecimen.md) - The Biospecimen which this Sample was prepared from.
 * [biospecimens](biospecimens.md) - The Biospecimens associated with an entity.
     * [Submission➞biospecimens](Submission_biospecimens.md) - One or more Biospecimen entities associated with this Submission.
 * [case_control_status](case_control_status.md) - Whether a Condition corresponds to a treatment or a control.
     * [Condition➞case_control_status](Condition_case_control_status.md)
 * [cell_barcode_offset](cell_barcode_offset.md) - The offset in sequence of the cell identifying barcode (e.g., 0).
     * [SequencingProtocol➞cell_barcode_offset](SequencingProtocol_cell_barcode_offset.md)
 * [cell_barcode_read](cell_barcode_read.md) - The type of read that contains the cell barcode (e.g., index1, index2, read1, read2).
     * [SequencingProtocol➞cell_barcode_read](SequencingProtocol_cell_barcode_read.md)
 * [cell_barcode_size](cell_barcode_size.md) - The size of the cell identifying barcode (e.g., 16).
     * [SequencingProtocol➞cell_barcode_size](SequencingProtocol_cell_barcode_size.md)
 * [checksum](checksum.md) - The checksum of the File.
     * [File➞checksum](File_checksum.md)
 * [checksum_type](checksum_type.md) - The type of algorithm used to generate the checksum of the File.
     * [File➞checksum_type](File_checksum_type.md)
 * [child](child.md) - The Child of two individuals.
     * [Trio➞child](Trio_child.md)
 * [condition](condition.md) - The Condition associated with an entity.
     * [Sample➞condition](Sample_condition.md)
 * [conditions](conditions.md) - The Conditions associated with an entity.
     * [Submission➞conditions](Submission_conditions.md) - One or more Condition entities associated with this Submission.
 * [data_access_committee](data_access_committee.md) - Data Access Committee associated with an entity.
     * [DataAccessPolicy➞data_access_committee](DataAccessPolicy_data_access_committee.md) - The Data Access Committee linked to this Data Use Policy.
 * [data_access_committees](data_access_committees.md) - Data Access Committees associated with an entity.
     * [Submission➞data_access_committees](Submission_data_access_committees.md) - The Data Access Committees that apply to the Data Access Policies in this Submission.
 * [data_access_policies](data_access_policies.md) - Data Access Policies associated with an entity.
     * [Submission➞data_access_policies](Submission_data_access_policies.md) - The Data Access Policies that apply to the Datasets in this Submission.
 * [data_access_policy](data_access_policy.md) - Data Access Policy associated with an entity.
     * [Dataset➞data_access_policy](Dataset_data_access_policy.md) - The Data Access Policy that applies to this Dataset.
 * [data_use_modifiers](data_use_modifiers.md) - Data Use Modifiers for the Data Use Permission associated with an entity. The used terms should be descendants of 'DUO:0000017: data use modifier'. Please use 'user specific restriction' if no other modifier applies.
     * [DataAccessPolicy➞data_use_modifiers](DataAccessPolicy_data_use_modifiers.md) - One or more Data Use Modifiers for the Data Use Permission associated with this Data Use Policy. The used terms should be descendants of 'DUO:0000017: data use modifier'. Please use 'user specific restriction' if no other modifier applies.
 * [data_use_permission](data_use_permission.md) - Data Use Permission associated with an entity. The used term should be a descendant of 'DUO:0000001: data use permission'.
     * [DataAccessPolicy➞data_use_permission](DataAccessPolicy_data_use_permission.md) - The Data Use Permission associated with this Data Use Policy. The used term should be a descendant of 'DUO:0000001: data use permission'.
 * [dataset](dataset.md) - The Dataset associated with an entity.
     * [File➞dataset](File_dataset.md) - The Dataset associated with this File.
 * [datasets](datasets.md) - The Datasets associated with an entity.
     * [Submission➞datasets](Submission_datasets.md) - One or more Dataset entities that are part of this Submission.
 * [description](description.md) - Description of an entity.
     * [Analysis➞description](Analysis_description.md) - A description summarizing how this Analysis was carried out (e.g., computational tools, pipelines, workflows).
     * [Biospecimen➞description](Biospecimen_description.md) - A concise description about the Biospecimen source, the collection method, and the protocol which was followed to process this Biospecimen.
     * [Condition➞description](Condition_description.md) - A concise description of the applied Condition.
     * [DataAccessPolicy➞description](DataAccessPolicy_description.md) - A short description for this Data Access Policy.
     * [Dataset➞description](Dataset_description.md) - A description summarizing this Dataset.
     * [LibraryPreparationProtocol➞description](LibraryPreparationProtocol_description.md) - Description summarizing how a sequencing library was prepared.
     * [Sample➞description](Sample_description.md) - A concise description about the Sample source, the collection method, and the protocol which was followed to process this Sample.
     * [SequencingExperiment➞description](SequencingExperiment_description.md) - A detailed description of this Sequencing Experiment.
     * [SequencingProcess➞description](SequencingProcess_description.md) - A short description of this Sequencing Process.
     * [SequencingProtocol➞description](SequencingProtocol_description.md) - A description summarizing the Sequencing Protocol.
     * [Study➞description](Study_description.md) - A detailed description (abstract) that describes the goals of this Study.
 * [disease_or_healthy](disease_or_healthy.md) - Whether a Condition corresponds to a disease or a healthy state.
     * [Condition➞disease_or_healthy](Condition_disease_or_healthy.md)
 * [doi](doi.md) - DOI identifier of a publication.
     * [Publication➞doi](Publication_doi.md)
 * [email](email.md) - Email of a Data Access Committee (e.g., DAC[at]email.com). This property must not include any personally identifiable information.
     * [DataAccessCommittee➞email](DataAccessCommittee_email.md) - The email of the Data Access Committee (e.g., DAC[at]email.com). This property must not include any personally identifiable data.
 * [end_bias](end_bias.md) - The end of the cDNA molecule that is preferentially sequenced (e.g., 3/5 prime end, full-length).
     * [LibraryPreparationProtocol➞end_bias](LibraryPreparationProtocol_end_bias.md)
 * [father](father.md) - The Father of an individual.
     * [Trio➞father](Trio_father.md)
 * [flow_cell_id](flow_cell_id.md) - Flow cell ID (e.g., Experiment ID_Cell 1_Lane_1).
     * [SequencingProtocol➞flow_cell_id](SequencingProtocol_flow_cell_id.md)
 * [flow_cell_type](flow_cell_type.md) - Type of flow cell used (e.g., S4, S2 for NovaSeq; PromethION, Flongle for Nanopore).
     * [SequencingProtocol➞flow_cell_type](SequencingProtocol_flow_cell_type.md)
 * [format](format.md) - The format of the File (e.g., BAM, SAM, CRAM, BAI).
     * [File➞format](File_format.md)
 * [forward_or_reverse](forward_or_reverse.md) - Denotes whether a submitted FASTQ file contains forward (R1) or reverse (R2) reads for paired-end sequencing.
     * [File➞forward_or_reverse](File_forward_or_reverse.md)
 * [geographical_region](geographical_region.md) - The geographical region where the Individual is located.
     * [Individual➞geographical_region](Individual_geographical_region.md)
 * [index_sequence](index_sequence.md) - A unique nucleotide sequence that is added to a sample during library preparation to serve as a unique identifier for the Sample.
     * [SequencingProcess➞index_sequence](SequencingProcess_index_sequence.md)
 * [individual](individual.md) - The Individual associated with an entity.
     * [Biospecimen➞individual](Biospecimen_individual.md) - The Individual entity from which this Biospecimen was derived.
 * [individuals](individuals.md) - The Individuals associated with an entity.
     * [Submission➞individuals](Submission_individuals.md) - One or more Individual entities associated with this Submission.
 * [institute](institute.md) - The Institute a person is affiliated with.
     * [DataAccessCommittee➞institute](DataAccessCommittee_institute.md)
 * [instrument_model](instrument_model.md) - The name and model of the technology platform used to perform sequencing.
     * [SequencingProtocol➞instrument_model](SequencingProtocol_instrument_model.md)
 * [isolation](isolation.md) - Method or device employed for collecting/isolating a Biospecimen or a Sample.
     * [Biospecimen➞isolation](Biospecimen_isolation.md) - Method or device employed for collecting/isolating this Biospecimen.
     * [Sample➞isolation](Sample_isolation.md) - Method or device employed for collecting/isolating this Sample.
 * [journal](journal.md) - The name of the journal.
     * [Publication➞journal](Publication_journal.md)
 * [karyotype](karyotype.md) - The karyotype of the Individual.
     * [Individual➞karyotype](Individual_karyotype.md)
 * [key](key.md) - The key of an attribute.
     * [Attribute➞key](Attribute_key.md)
 * [key_type](key_type.md) - A semantic type that characterizes the attribute key (e.g., oxygen saturation measurement (MAXO:0000616)).
     * [Attribute➞key_type](Attribute_key_type.md)
 * [library_layout](library_layout.md) - Describe whether the library was sequenced in single-end (forward or reverse) or paired-end mode.
     * [LibraryPreparationProtocol➞library_layout](LibraryPreparationProtocol_library_layout.md)
 * [library_name](library_name.md) - A short name identifying the library. The same name may refer to multiple versions of the same continually updated library.
     * [LibraryPreparationProtocol➞library_name](LibraryPreparationProtocol_library_name.md)
 * [library_preparation](library_preparation.md) - The general method for preparation of the sequencing library (e.g., KAPA PCR-free).
     * [LibraryPreparationProtocol➞library_preparation](LibraryPreparationProtocol_library_preparation.md)
 * [library_preparation_kit_manufacturer](library_preparation_kit_manufacturer.md) - The manufacturer of the kit used for library preparation.
     * [LibraryPreparationProtocol➞library_preparation_kit_manufacturer](LibraryPreparationProtocol_library_preparation_kit_manufacturer.md)
 * [library_preparation_kit_retail_name](library_preparation_kit_retail_name.md) - The retail name for the kit used to construct a genomic library. This may include the vendor name, kit name and kit version (e.g., Agilent sure select Human Exome V8, Twist RefSeq Exome).
     * [LibraryPreparationProtocol➞library_preparation_kit_retail_name](LibraryPreparationProtocol_library_preparation_kit_retail_name.md)
 * [library_preparation_protocol](library_preparation_protocol.md) - The Library Preparation Protocol associated with an entity.
     * [SequencingExperiment➞library_preparation_protocol](SequencingExperiment_library_preparation_protocol.md) - The Library Preparation Protocol associated with this Sequencing Experiment.
 * [library_preparation_protocols](library_preparation_protocols.md) - The Library Preparation Protocol associated with an entity.
     * [Submission➞library_preparation_protocols](Submission_library_preparation_protocols.md) - One or more Library Preparation Protocol entities associated with this Submission.
 * [library_selection](library_selection.md) - The method used to select for or against, enrich, or screen the material being sequenced (e.g., random, PCA, cDNA).
     * [LibraryPreparationProtocol➞library_selection](LibraryPreparationProtocol_library_selection.md)
 * [library_type](library_type.md) - Describe the level of omics analysis (e.g., metagenome, transcriptome)
     * [LibraryPreparationProtocol➞library_type](LibraryPreparationProtocol_library_type.md)
 * [mother](mother.md) - The Mother of an individual.
     * [Trio➞mother](Trio_mother.md)
 * [mutant_or_wildtype](mutant_or_wildtype.md) - Whether a Condition corresponds to a mutant or a wildtype.
     * [Condition➞mutant_or_wildtype](Condition_mutant_or_wildtype.md)
 * [name](name.md) - The name for an entity.
     * [AnalysisProcess➞name](AnalysisProcess_name.md)
     * [Biospecimen➞name](Biospecimen_name.md) - A descriptive name of this Biospecimen (e.g., GHGAB_caudate_nucleus_biospecimen). This property must not include any personally identifiable data.
     * [Condition➞name](Condition_name.md) - The name of this Condition.
     * [DataAccessPolicy➞name](DataAccessPolicy_name.md) - A name for this Data Access Policy.
     * [File➞name](File_name.md) - The given filename.
     * [Sample➞name](Sample_name.md) - A descriptive name of this Sample (e.g., GHGAS_Blood_Sample1 or GHGAS_PBMC_RNAseq_S1). This property must not include any personally identifiable data.
     * [SequencingProcess➞name](SequencingProcess_name.md) - A short name identifying this Sequencing Process.
     * [SequencingProtocol➞name](SequencingProtocol_name.md) - A short name identifying this Sequencing Protocol.
 * [phenotypic_features](phenotypic_features.md) - The phenotypic feature concepts that the entity is associated with at the time of retrieval from the organism. The Phenotypic Feature is captured using a concept from the Human Phenotype Ontology.
     * [Individual➞phenotypic_features](Individual_phenotypic_features.md)
 * [policy_text](policy_text.md) - The complete text for the Data Access Policy.
     * [DataAccessPolicy➞policy_text](DataAccessPolicy_policy_text.md)
 * [policy_url](policy_url.md) - An alternative to the Data Access Policy text is to provide the URL for the policy. This is useful if the terms of the policy are available online at a resolvable URL.
     * [DataAccessPolicy➞policy_url](DataAccessPolicy_policy_url.md)
 * [primer](primer.md) - The type of primer used for reverse transcription (e.g., oligo-dT or random).
     * [LibraryPreparationProtocol➞primer](LibraryPreparationProtocol_primer.md)
 * [publications](publications.md) - The Publication associated with an entity.
     * [Submission➞publications](Submission_publications.md) - One or more Publication entities associated with this Submission.
 * [reference_chromosome](reference_chromosome.md) - The reference chromosome used for this Analysis.
     * [Analysis➞reference_chromosome](Analysis_reference_chromosome.md)
 * [reference_genome](reference_genome.md) - The reference genome or annotation used for prior analyses (e.g., GRCh38.p13).
     * [Analysis➞reference_genome](Analysis_reference_genome.md)
 * [rnaseq_strandedness](rnaseq_strandedness.md) - The strandedness of the library, whether reads come from both strands of the cDNA or only from the first (antisense) or the second (sense) strand.
     * [LibraryPreparationProtocol➞rnaseq_strandedness](LibraryPreparationProtocol_rnaseq_strandedness.md)
 * [sample](sample.md) - The Sample associated with an entity.
     * [SampleFile➞sample](SampleFile_sample.md) - The Sample that is associated with this Sample File.
     * [SequencingProcess➞sample](SequencingProcess_sample.md) - The Sample associated with this Sequencing Process.
 * [sample_barcode_read](sample_barcode_read.md) - The type of read that contains the sample barcode (e.g., index1, index2, read1, read2).
     * [SequencingProtocol➞sample_barcode_read](SequencingProtocol_sample_barcode_read.md)
 * [sample_files](sample_files.md) - The Sample Files associated with an entity.
     * [Submission➞sample_files](Submission_sample_files.md) - The Sample Files that are part of this submission.
 * [sample_input_files](sample_input_files.md) - The Sample File associated used as an input for an entity.
     * [AnalysisProcess➞sample_input_files](AnalysisProcess_sample_input_files.md) - The associated Sample File used as an input for this Analysis Process.
 * [samples](samples.md) - The Samples associated with an entity.
     * [Submission➞samples](Submission_samples.md) - One or more Sample entities associated with this Submission.
 * [sequencing_center](sequencing_center.md) - Center where sample was sequenced.
     * [SequencingProtocol➞sequencing_center](SequencingProtocol_sequencing_center.md)
 * [sequencing_experiment](sequencing_experiment.md) - The Sequencing Experiment associated with an entity.
     * [SequencingProcess➞sequencing_experiment](SequencingProcess_sequencing_experiment.md) - The Sequencing Experiment associated with this Sequencing Process.
 * [sequencing_experiments](sequencing_experiments.md) - The Sequencing Experiments associated with an entity.
     * [Submission➞sequencing_experiments](Submission_sequencing_experiments.md) - One or more Sequencing Experiment entities associated with this Submission.
 * [sequencing_lane_id](sequencing_lane_id.md) - The identifier of a sequencing lane.
     * [SequencingProcess➞sequencing_lane_id](SequencingProcess_sequencing_lane_id.md)
 * [sequencing_machine_id](sequencing_machine_id.md) - The identifier of a sequencing machine.
     * [SequencingProcess➞sequencing_machine_id](SequencingProcess_sequencing_machine_id.md)
 * [sequencing_process](sequencing_process.md) - The Sequencing Process associated with an entity.
     * [SequencingProcessFile➞sequencing_process](SequencingProcessFile_sequencing_process.md) - The Sequencing Process associated with this Sequencing Process File.
 * [sequencing_process_files](sequencing_process_files.md) - The Sequencing Process Files associated with an entity.
     * [Submission➞sequencing_process_files](Submission_sequencing_process_files.md) - The Sequencing Process Files that are part of this Submission.
 * [sequencing_process_input_files](sequencing_process_input_files.md) - The Sequencing Process File associated used as an input for an entity.
     * [AnalysisProcess➞sequencing_process_input_files](AnalysisProcess_sequencing_process_input_files.md) - The associated Sequencing Process File used as an input for this Analysis Process.
 * [sequencing_processes](sequencing_processes.md) - The Sequencing Processes associated with an entity.
     * [Submission➞sequencing_processes](Submission_sequencing_processes.md) - The Sequencing Processes that are part of this Submission.
 * [sequencing_protocol](sequencing_protocol.md) - The Sequencing Protocol associated with an entity.
     * [SequencingExperiment➞sequencing_protocol](SequencingExperiment_sequencing_protocol.md) - The Sequencing Protocol associated with this Sequencing Experiment.
 * [sequencing_protocols](sequencing_protocols.md) - The Sequencing Protocol associated with an entity.
     * [Submission➞sequencing_protocols](Submission_sequencing_protocols.md) - One or more Sequencing Protocol entities associated with this Submission.
 * [sequencing_read_length](sequencing_read_length.md) - Length of sequencing reads (e.g., long or short or actual number of the read length).
     * [SequencingProtocol➞sequencing_read_length](SequencingProtocol_sequencing_read_length.md)
 * [sequencing_run_id](sequencing_run_id.md) - The identifier of a sequencing run.
     * [SequencingProcess➞sequencing_run_id](SequencingProcess_sequencing_run_id.md)
 * [sex](sex.md) - The genotypic sex of the Individual (e.g., female).
     * [Individual➞sex](Individual_sex.md)
 * [size](size.md) - The size of the File in bytes.
     * [File➞size](File_size.md)
 * [storage](storage.md) - Methods by which a Biospecimen or a Sample is stored.
     * [Biospecimen➞storage](Biospecimen_storage.md) - Methods by which this Biospecimen is stored.
     * [Sample➞storage](Sample_storage.md) - Methods by which this Sample is stored.
 * [studies](studies.md) - The Study associated with an entity.
     * [Submission➞studies](Submission_studies.md) - Study entities associated with this Submission.
 * [study](study.md) - The Study associated with an entity.
     * [Condition➞study](Condition_study.md) - The Study associated with this Condition.
     * [Publication➞study](Publication_study.md) - The Study entity associated with this Publication.
     * [StudyFile➞study](StudyFile_study.md) - The Study that is associated with this Study File.
 * [study_files](study_files.md) - The Study Files associated with an entity.
     * [Submission➞study_files](Submission_study_files.md) - The Study Files that are part of this Submission.
 * [study_input_files](study_input_files.md) - The Study File associated used as an input for an entity.
     * [AnalysisProcess➞study_input_files](AnalysisProcess_study_input_files.md) - The associated Study File used as an input for this Analysis Process.
 * [target_coverage](target_coverage.md) - Mean coverage for whole genome sequencing, or mean target coverage for whole exome and targeted sequencing, (i.e. the number of times a particular locus was sequenced).
     * [SequencingProtocol➞target_coverage](SequencingProtocol_target_coverage.md)
 * [target_regions](target_regions.md) - Subset of genes or specific regions of the genome, which are most likely to be involved in the phenotype under study.
     * [LibraryPreparationProtocol➞target_regions](LibraryPreparationProtocol_target_regions.md)
 * [tissue](tissue.md)
     * [Biospecimen➞tissue](Biospecimen_tissue.md) - The tissue this Biospecimen originated from.
 * [title](title.md) - The title that describes an entity.
     * [Analysis➞title](Analysis_title.md)
     * [Dataset➞title](Dataset_title.md) - A title for this Dataset.
     * [Publication➞title](Publication_title.md) - The title for this Publication.
     * [SequencingExperiment➞title](SequencingExperiment_title.md) - The title for this Sequencing Experiment (e.g., GHGAE_PBMC_RNAseq).
     * [Study➞title](Study_title.md) - A comprehensive title for this Study.
 * [trios](trios.md) - The Trios associated with an entity.
     * [Submission➞trios](Submission_trios.md) - One or more Trio entities associated with this Submission.
 * [type](type.md) - The type of an entity. Note: Not to be confused with rdf:type
     * [Analysis➞type](Analysis_type.md) - The type of this Analysis.
     * [Biospecimen➞type](Biospecimen_type.md) - The type of Biospecimen.
     * [Sample➞type](Sample_type.md) - The type of the Sample.
     * [SequencingExperiment➞type](SequencingExperiment_type.md) - The type of this Sequencing Experiment.
     * [SequencingProtocol➞type](SequencingProtocol_type.md) - Type of the Sequencing Protocol (e.g., mRNA-seq, Whole exome long-read sequencing).
     * [Study➞type](Study_type.md) - The type of this Study (e.g., Cancer Genomics, Epigenetics, Exome Sequencing).
 * [types](types.md) - The types of an entity. Note: Not to be confused with rdf:type
     * [Dataset➞types](Dataset_types.md) - The type of this Dataset.
 * [umi_barcode_offset](umi_barcode_offset.md) - The offset in sequence of the UMI identifying barcode (e.g., 16).
     * [SequencingProtocol➞umi_barcode_offset](SequencingProtocol_umi_barcode_offset.md)
 * [umi_barcode_read](umi_barcode_read.md) - The type of read that contains the UMI barcode (e.g., index1, index2, read1, read2).
     * [SequencingProtocol➞umi_barcode_read](SequencingProtocol_umi_barcode_read.md)
 * [umi_barcode_size](umi_barcode_size.md) - The size of the UMI identifying barcode (e.g., 10).
     * [SequencingProtocol➞umi_barcode_size](SequencingProtocol_umi_barcode_size.md)
 * [value](value.md) - The value for an attribute (e.g., a numerical value without the units).
     * [Attribute➞value](Attribute_value.md)
 * [value_type](value_type.md) - The value_type that characterizes the attribute value (e.g., percentage (SIO:001413)).
     * [Attribute➞value_type](Attribute_value_type.md)
 * [vital_status_at_sampling](vital_status_at_sampling.md) - Vital Status of the Individual at the point of sampling (e.g., alive).
     * [Biospecimen➞vital_status_at_sampling](Biospecimen_vital_status_at_sampling.md)
 * [xref](xref.md) - Database cross references for an entity.
     * [Publication➞xref](Publication_xref.md) - One or more cross-references for this Publication.
     * [Sample➞xref](Sample_xref.md) - One or more cross-references for this Sample (e.g., this Sample may have an EBI BioSamples accession ID).
 * [year](year.md) - The year in which the paper was published.
     * [Publication➞year](Publication_year.md)

### Enums

 * [AgeRangeEnum](AgeRangeEnum.md) - Enum to capture the age range that an Indiviudal belongs to.
 * [AncestryEnum](AncestryEnum.md) - Permitted values for ancestry
 * [CaseControlStatusEnum](CaseControlStatusEnum.md) - Enum to capture whether a condition corresponds to a case or a control condition.
 * [DataUseModifierEnum](DataUseModifierEnum.md) - Permitted values for data use modifier
 * [DataUsePermissionEnum](DataUsePermissionEnum.md) - Permitted values for data use permission
 * [DiseaseOrHealthyEnum](DiseaseOrHealthyEnum.md) - Enum to capture whether a condition corresponds to a disease or a healthy state.
 * [EndBiasEnum](EndBiasEnum.md) - Permitted values for end bias
 * [FileFormatEnum](FileFormatEnum.md) - Enum to capture file types.
 * [FlowCellTypeEnum](FlowCellTypeEnum.md) - Permitted values for flow cell type
 * [ForwardOrReverseEnum](ForwardOrReverseEnum.md) - Enum to capture whether the reads from paired-end sequencing are forward (R1) or reverse (R2).
 * [GeographicalRegionEnum](GeographicalRegionEnum.md) - Permitted values for geographical region
 * [IndexReadEnum](IndexReadEnum.md) - Permitted Values to indicate the location of a sequence component in a read or index
 * [IndividualSexEnum](IndividualSexEnum.md) - The sex of an Individual as as defined in a specific medical and clinical context.
 * [InstrumentModelEnum](InstrumentModelEnum.md) - Permitted values for the instrument model
 * [IsolationEnum](IsolationEnum.md) - Describes how biomaterial was isolated.
 * [KaryotypeEnum](KaryotypeEnum.md) - Permitted values for karyotype
 * [LibraryPreparationKitRetailNameEnum](LibraryPreparationKitRetailNameEnum.md) - Permitted values for library preparation kit retail name
 * [LibraryPreparationLibraryLayoutEnum](LibraryPreparationLibraryLayoutEnum.md) - Single-end vs paired-end library
 * [LibraryPreparationLibrarySelectionEnum](LibraryPreparationLibrarySelectionEnum.md) - Permitted vocabulary for library selections
 * [LibraryPreparationLibraryTypeEnum](LibraryPreparationLibraryTypeEnum.md) - The type of the library
 * [LibraryPreparationRNASeqStrandednessEnum](LibraryPreparationRNASeqStrandednessEnum.md) - Permitted values for library preparation RNASeq strandedness
 * [MutantOrWildtypeEnum](MutantOrWildtypeEnum.md) - Enum to capture whether a condition corresponds to a mutant or a wildtype.
 * [PhenotypicFeaturesEnum](PhenotypicFeaturesEnum.md) - An enum describing permissible phenotype descriptors
 * [PrimerEnum](PrimerEnum.md) - Permitted values for primer
 * [SampleBarcodeReadEnum](SampleBarcodeReadEnum.md) - Permitted values for sample barcode read
 * [SampleTypeEnum](SampleTypeEnum.md) - The type of a sample
 * [StorageEnum](StorageEnum.md) - Enum to capture how a Sample or Biospecimen was stored.
 * [StudyTypeEnum](StudyTypeEnum.md) - Enum to capture the type of a study.
 * [TissueEnum](TissueEnum.md) - A tissue as described in the BRENDA ontology.
 * [VitalStatusEnum](VitalStatusEnum.md) - Enum to capture the vital status of an individual.

### Subsets

 * [Ontology](Ontology.md) - This slot is part of an ontology which is currently not otherwise encoded in the schema.

### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
