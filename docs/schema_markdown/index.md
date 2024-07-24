
# GHGA-Submission-Metadata-Schema


**metamodel version:** 1.7.0

**version:** 2.0.0


The submission centric metadata schema for the German Human Genome-Phenome Archive (GHGA).


### Classes

 * [Analysis](Analysis.md) - An Analysis is a data transformation that transforms input data to output data.
 * [AnalysisMethod](AnalysisMethod.md) - An Analysis Method captures the workflow steps that were performed to analyze data obtained from an Experiment.
 * [Attribute](Attribute.md) - A key/value pair that further characterizes an entity.
 * [DataAccessCommittee](DataAccessCommittee.md) - A group of members that are delegated to grant access to one or more datasets after ensuring the criteria for data sharing has been met,  and request for data use does not raise ethical and/or legal concerns.
 * [DataAccessPolicy](DataAccessPolicy.md) - A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.
 * [Dataset](Dataset.md) - A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
 * [Experiment](Experiment.md) - An Experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
 * [ExperimentMethod](ExperimentMethod.md) - The Experiment Method captures technical metadata describing the parameters used to generate output from the Sample.
 * [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.
     * [AnalysisMethodSupportingFile](AnalysisMethodSupportingFile.md) - An Analysis Method Supporting File is a File that contains additional information relevant for the Analysis Method, such as (unstructured) protocols or task descriptions.
     * [ExperimentMethodSupportingFile](ExperimentMethodSupportingFile.md) - An Experiment Method Supporting File is a File that contains additional information relevant for the Experiment Method, such as (unstructured) protocols.
     * [IndividualSupportingFile](IndividualSupportingFile.md) - An Individual Supporting File is a File that contains additional information relevant for the Individual, such as ped-files, phenopackets or imaging data.
     * [ProcessDataFile](ProcessDataFile.md) - A Process Data File is a File that contains data produced by an Analysis or workflow.
     * [ResearchDataFile](ResearchDataFile.md) - A Research Data File is a File that contains raw data originating from an Experiment.
 * [Individual](Individual.md) - An Individual is a Person who is participating in a Study.
 * [Publication](Publication.md) - A Publication represents an article that is published. The minimum expectation is that the publication has a valid DOI.
 * [Sample](Sample.md) - A Sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use.  It is prepared from a Biospecimen.
 * [Study](Study.md) - A Study is an experimental investigation of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.
 * [Submission](Submission.md) - A grouping entity that represents information about one or more entities. A submission can be considered as a set of inter-related (and inter-connected) entities that represent a data submission to GHGA.

### Mixins

 * [AliasMixin](AliasMixin.md) - Mixin for entities that can be assigned an alias at the time of metadata submission.
     * [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 * [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.
 * [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

### Slots

 * [abstract](abstract.md) - The study abstract that describes the goals. Can also hold abstract from a publication related to this Study.
     * [Publication➞abstract](Publication_abstract.md)
 * [affiliations](affiliations.md) - The Institution(s) associated with an entity.
     * [Study➞affiliations](Study_affiliations.md) - The affiliations associated with this Study.
 * [alias](alias.md) - The alias for an entity at the time of submission.
     * [AliasMixin➞alias](AliasMixin_alias.md)
         * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)
 * [analyses](analyses.md) - The Analyses associated with an entity.
     * [Submission➞analyses](Submission_analyses.md) - One or more Analysis entities associated with this Submission.
 * [analysis](analysis.md) - The Analysis associated with an entity.
     * [ProcessDataFile➞analysis](ProcessDataFile_analysis.md) - The alias of the Analysis that produced this Process Data File.
 * [analysis_method](analysis_method.md) - The Analysis Process associated with an entity.
     * [AnalysisMethodSupportingFile➞analysis_method](AnalysisMethodSupportingFile_analysis_method.md)
     * [Analysis➞analysis_method](Analysis_analysis_method.md) - The alias of the Analysis Method that is associated with this Analysis.
 * [analysis_method_supporting_files](analysis_method_supporting_files.md) - The Analysis Method Supporting Files associated with an entity.
     * [Submission➞analysis_method_supporting_files](Submission_analysis_method_supporting_files.md) - One or more Analysis Method Supporting Files associated with this Submission.
 * [analysis_methods](analysis_methods.md) - The Analysis Processes associated with an entity.
     * [Submission➞analysis_methods](Submission_analysis_methods.md) - The Analysis Methods that are part of this Submission.
 * [ancestry_ids](ancestry_ids.md) - A person's descent or lineage from a population.
     * [Individual➞ancestry_ids](Individual_ancestry_ids.md)
 * [ancestry_terms](ancestry_terms.md) - A person's descent or lineage from a population.
     * [Individual➞ancestry_terms](Individual_ancestry_terms.md)
 * [attributes](attributes.md) - Key/value pairs corresponding to an entity.
     * [AttributeMixin➞attributes](AttributeMixin_attributes.md)
         * [ExperimentMethod➞attributes](ExperimentMethod_attributes.md) - One or more attributes that further characterize this Experiment Method.
         * [Study➞attributes](Study_attributes.md) - One or more attributes that further characterize this Study.
 * [author](author.md) - The individual who is responsible for the content of the Publication.
     * [Publication➞author](Publication_author.md) - Author(s) of this Publication.
 * [biological_replicate](biological_replicate.md) - An integer to indicate the number of a biological replicate.
     * [Sample➞biological_replicate](Sample_biological_replicate.md)
 * [biospecimen_age_at_sampling](biospecimen_age_at_sampling.md) - The age of the Individual at the time of isolating this biospecimen.
     * [Sample➞biospecimen_age_at_sampling](Sample_biospecimen_age_at_sampling.md)
 * [biospecimen_description](biospecimen_description.md) - The description of a biospecimen.
     * [Sample➞biospecimen_description](Sample_biospecimen_description.md) - A concise description about the Biospecimen source, the collection method, and the protocol which was followed to process this Biospecimen.
 * [biospecimen_isolation](biospecimen_isolation.md) - Method or device employed for collecting/isolating a Biospecimen or a Sample.
     * [Sample➞biospecimen_isolation](Sample_biospecimen_isolation.md) - Method or device employed for collecting/isolating this Biospecimen.
 * [biospecimen_name](biospecimen_name.md) - The name for a biospecimen.
     * [Sample➞biospecimen_name](Sample_biospecimen_name.md) - A descriptive name of this Biospecimen (e.g., GHGAB_caudate_nucleus_biospecimen). This property must not include any personally identifiable data.
 * [biospecimen_storage](biospecimen_storage.md) - Methods by which a Biospecimen is stored.
     * [Sample➞biospecimen_storage](Sample_biospecimen_storage.md) - Methods by which this Biospecimen is stored.
 * [biospecimen_tissue_id](biospecimen_tissue_id.md) - The corresponding ontology ID for the biospecimen_tissue_term (e.g., BTO:0000671, BTO:0000089, BTO:0000848).
     * [Sample➞biospecimen_tissue_id](Sample_biospecimen_tissue_id.md)
 * [biospecimen_tissue_term](biospecimen_tissue_term.md) - The tissue this Biospecimen originated from. Should be a term from the BRENDA Tissue Ontology vocabulary (e.g., kidney, blood, melanoma cell).
     * [Sample➞biospecimen_tissue_term](Sample_biospecimen_tissue_term.md)
 * [biospecimen_type](biospecimen_type.md) - The type of a biospecimen. Note: Not to be confused with rdf:type.
     * [Sample➞biospecimen_type](Sample_biospecimen_type.md) - The type of Biospecimen.
 * [biospecimen_vital_status_at_sampling](biospecimen_vital_status_at_sampling.md) - Vital Status of the Individual at the time of isolating this biospecimen (e.g., alive).
     * [Sample➞biospecimen_vital_status_at_sampling](Sample_biospecimen_vital_status_at_sampling.md)
 * [case_control_status](case_control_status.md) - Whether a Condition corresponds to a treatment or a control.
     * [Sample➞case_control_status](Sample_case_control_status.md)
 * [checksum](checksum.md) - The checksum of the File.
     * [File➞checksum](File_checksum.md)
 * [checksum_type](checksum_type.md) - The type of algorithm used to generate the checksum of the File.
     * [File➞checksum_type](File_checksum_type.md)
 * [data_access_committee](data_access_committee.md) - Data Access Committee associated with an entity.
     * [DataAccessPolicy➞data_access_committee](DataAccessPolicy_data_access_committee.md) - The Data Access Committee linked to this Data Use Policy.
 * [data_access_committees](data_access_committees.md) - Data Access Committees associated with an entity.
     * [Submission➞data_access_committees](Submission_data_access_committees.md) - The Data Access Committees that apply to the Data Access Policies in this Submission.
 * [data_access_policies](data_access_policies.md) - Data Access Policies associated with an entity.
     * [Submission➞data_access_policies](Submission_data_access_policies.md) - The Data Access Policies that apply to the Datasets in this Submission.
 * [data_access_policy](data_access_policy.md) - Data Access Policy associated with an entity.
     * [Dataset➞data_access_policy](Dataset_data_access_policy.md) - The Data Access Policy that applies to this Dataset.
 * [data_use_modifier_ids](data_use_modifier_ids.md) - The DUO IDs corresponding to the Data Use Modifier terms (e.g., DUO:0000043).
     * [DataAccessPolicy➞data_use_modifier_ids](DataAccessPolicy_data_use_modifier_ids.md)
 * [data_use_modifier_terms](data_use_modifier_terms.md) - Data Use Modifiers for the Data Use Permission associated with an entity. The used terms should be descendants of 'DUO:0000017: data use modifier'. Please use 'USER_SPECIFIC_RESTRICTION' if no other modifier applies.
     * [DataAccessPolicy➞data_use_modifier_terms](DataAccessPolicy_data_use_modifier_terms.md) - One or more Data Use Modifiers for the Data Use Permission associated with this Data Use Policy. The used terms should be descendants of 'DUO:0000017: data use modifier' (e.g., clinical care use). Please use 'USER_SPECIFIC_RESTRICTION' if no other modifier applies.
 * [data_use_permission_id](data_use_permission_id.md) - The DUO IDs corresponding to the Data Use Modifier terms (e.g., DUO:DUO:0000004).
     * [DataAccessPolicy➞data_use_permission_id](DataAccessPolicy_data_use_permission_id.md) - The DUO ID corresponding to the Data Use Permission term (e.g., DUO:0000004).
 * [data_use_permission_term](data_use_permission_term.md) - Data Use Permission associated with an entity. The used term should be a descendant of 'DUO:0000001: data use permission'.
     * [DataAccessPolicy➞data_use_permission_term](DataAccessPolicy_data_use_permission_term.md) - The Data Use Permission associated with this Data Use Policy. The used term should be a descendant of 'DUO:0000001: data use permission' (e.g., no restriction).
 * [dataset](dataset.md) - The Dataset associated with an entity.
     * [File➞dataset](File_dataset.md) - The Dataset alias associated with this File.
 * [datasets](datasets.md) - The Datasets associated with an entity.
     * [Submission➞datasets](Submission_datasets.md) - One or more Dataset entities that are part of this Submission.
 * [description](description.md) - Description of an entity.
     * [AnalysisMethod➞description](AnalysisMethod_description.md)
     * [Analysis➞description](Analysis_description.md) - A description summarizing how this Analysis was carried out (e.g., description of computational tools, pipelines, workflows).
     * [DataAccessPolicy➞description](DataAccessPolicy_description.md) - A short description for this Data Access Policy.
     * [Dataset➞description](Dataset_description.md) - A description summarizing this Dataset.
     * [ExperimentMethod➞description](ExperimentMethod_description.md) - A short description of this Experiment Method.
     * [Experiment➞description](Experiment_description.md) - A detailed description of this Experiment.
     * [Sample➞description](Sample_description.md) - A concise description about the Sample source, the collection method, and the protocol which was followed to process this Sample.
     * [Study➞description](Study_description.md) - A detailed description (abstract) that describes the goals of this Study.
 * [diagnosis_ids](diagnosis_ids.md) - One or more diagnoses that the entity is associated with at the time of retrieval from the organism. The diagnosis is captured using a code from ICD-10 (WHO version). Please restrict the ICD code to the chapter letter and two digits for the main diagnosis (e.g., E10, C01).
     * [Individual➞diagnosis_ids](Individual_diagnosis_ids.md)
 * [diagnosis_terms](diagnosis_terms.md) - The ICD-10 terms corresponding to the ICD-10 codes (e.g., Type 1 diabetes mellitus, Malignant neoplasm of base of tongue).
     * [Individual➞diagnosis_terms](Individual_diagnosis_terms.md)
 * [disease_or_healthy](disease_or_healthy.md) - Whether a Condition corresponds to a disease or a healthy state.
     * [Sample➞disease_or_healthy](Sample_disease_or_healthy.md)
 * [doi](doi.md) - DOI identifier of a publication.
     * [Publication➞doi](Publication_doi.md)
 * [ega_accession](ega_accession.md) - The EGA accession ID of an entity.
     * [Analysis➞ega_accession](Analysis_ega_accession.md) - The EGA accession of the 'Analysis' entity (EGAZ).
     * [DataAccessCommittee➞ega_accession](DataAccessCommittee_ega_accession.md)
     * [DataAccessPolicy➞ega_accession](DataAccessPolicy_ega_accession.md)
     * [Dataset➞ega_accession](Dataset_ega_accession.md)
     * [ExperimentMethod➞ega_accession](ExperimentMethod_ega_accession.md) - The EGA accession of the 'Experiment' entity (EGAX).
     * [Experiment➞ega_accession](Experiment_ega_accession.md) - The EGA accession of the 'Run' entity (EGAR).
     * [ProcessDataFile➞ega_accession](ProcessDataFile_ega_accession.md)
     * [ResearchDataFile➞ega_accession](ResearchDataFile_ega_accession.md)
     * [Sample➞ega_accession](Sample_ega_accession.md)
     * [Study➞ega_accession](Study_ega_accession.md)
 * [email](email.md) - Email of a Data Access Committee (e.g., DAC[at]email.com). This property must not include any personally identifiable information.
     * [DataAccessCommittee➞email](DataAccessCommittee_email.md) - The email of the Data Access Committee (e.g., DAC[at]email.com). This property must not include any personally identifiable data.
 * [end_bias](end_bias.md) - The end of the cDNA molecule that is preferentially sequenced (e.g., 3/5 prime end, full-length).
     * [ExperimentMethod➞end_bias](ExperimentMethod_end_bias.md)
 * [experiment](experiment.md) - The Experiment associated with an entity.
     * [ResearchDataFile➞experiment](ResearchDataFile_experiment.md) - The alias of the Experiment that produced this Research Data File.
 * [experiment_method](experiment_method.md) - The Experiment Method associated with an entity.
     * [ExperimentMethodSupportingFile➞experiment_method](ExperimentMethodSupportingFile_experiment_method.md)
     * [Experiment➞experiment_method](Experiment_experiment_method.md) - The alias of one or more Experiment Methods that are associated with this Experiment.
 * [experiment_method_supporting_files](experiment_method_supporting_files.md) - The Experiment Method Supporting Files associated with an entity.
     * [Submission➞experiment_method_supporting_files](Submission_experiment_method_supporting_files.md) - One or more Experiment Method Supporting Files associated with this Submission.
 * [experiment_methods](experiment_methods.md) - The Experiment Methods associated with an entity.
     * [Submission➞experiment_methods](Submission_experiment_methods.md) - The Experiment Methods that are part of this Submission.
 * [experiments](experiments.md) - The Experiments associated with an entity.
     * [Submission➞experiments](Submission_experiments.md) - One or more Experiment entities associated with this Submission.
 * [flow_cell_id](flow_cell_id.md) - Flow cell ID (e.g., Experiment ID_Cell 1_Lane_1).
     * [ExperimentMethod➞flow_cell_id](ExperimentMethod_flow_cell_id.md)
 * [flow_cell_type](flow_cell_type.md) - Type of flow cell used (e.g., S4, S2 for NovaSeq; PromethION, Flongle for Nanopore).
     * [ExperimentMethod➞flow_cell_type](ExperimentMethod_flow_cell_type.md)
 * [format](format.md) - The format of the File (e.g., BAM, SAM, CRAM, BAI).
     * [AnalysisMethodSupportingFile➞format](AnalysisMethodSupportingFile_format.md) - The file format of the Supporting File (e.g., TXT, JSON).
     * [ExperimentMethodSupportingFile➞format](ExperimentMethodSupportingFile_format.md) - The file format of the Supporting File (e.g., TXT, JSON).
     * [IndividualSupportingFile➞format](IndividualSupportingFile_format.md) - The file format of the Supporting File (e.g., TXT, JSON).
     * [ProcessDataFile➞format](ProcessDataFile_format.md) - The file format of the Process Data File (e.g., CRAM, BAM).
     * [ResearchDataFile➞format](ResearchDataFile_format.md) - The file format of the Research Data File (e.g., FASTQ, uBAM, FASTA).
 * [geographical_region_id](geographical_region_id.md) - The geographical region where the Individual is located.
     * [Individual➞geographical_region_id](Individual_geographical_region_id.md)
 * [geographical_region_term](geographical_region_term.md) - The geographical region where the Individual is located.
     * [Individual➞geographical_region_term](Individual_geographical_region_term.md)
 * [included_in_submission](included_in_submission.md) - Whether a File is included in the Submission or not.
     * [File➞included_in_submission](File_included_in_submission.md)
 * [index_sequence](index_sequence.md) - A unique nucleotide sequence that is added to a sample during library preparation to serve as a unique identifier for the Sample.
 * [individual](individual.md) - The Individual associated with an entity.
     * [IndividualSupportingFile➞individual](IndividualSupportingFile_individual.md)
     * [Sample➞individual](Sample_individual.md) - The alias of the Individual entity from which this Biospecimen or Sample was derived.
 * [individual_supporting_files](individual_supporting_files.md) - The Individual Supporting Files associated with an entity.
     * [Submission➞individual_supporting_files](Submission_individual_supporting_files.md) - One or more Individual Supporting Files associated with this Submission.
 * [individuals](individuals.md) - The Individuals associated with an entity.
     * [Submission➞individuals](Submission_individuals.md) - One or more Individual entities associated with this Submission.
 * [institute](institute.md) - The Institute a person is affiliated with.
     * [DataAccessCommittee➞institute](DataAccessCommittee_institute.md)
 * [instrument_model](instrument_model.md) - The name and model of the technology platform used to perform sequencing.
     * [ExperimentMethod➞instrument_model](ExperimentMethod_instrument_model.md)
 * [journal](journal.md) - The name of the journal.
     * [Publication➞journal](Publication_journal.md)
 * [key](key.md) - The key of an attribute.
     * [Attribute➞key](Attribute_key.md)
 * [key_type](key_type.md) - A semantic type that characterizes the attribute key (e.g., oxygen saturation measurement (MAXO:0000616)).
     * [Attribute➞key_type](Attribute_key_type.md)
 * [library_name](library_name.md) - A short name identifying the library. The same name may refer to multiple versions of the same continually updated library.
 * [library_preparation](library_preparation.md) - The general method for preparation of the sequencing library (e.g., KAPA PCR-free).
     * [ExperimentMethod➞library_preparation](ExperimentMethod_library_preparation.md)
 * [library_preparation_kit_manufacturer](library_preparation_kit_manufacturer.md) - The manufacturer of the kit used for library preparation.
     * [ExperimentMethod➞library_preparation_kit_manufacturer](ExperimentMethod_library_preparation_kit_manufacturer.md)
 * [library_preparation_kit_retail_name](library_preparation_kit_retail_name.md) - The retail name for the kit used to construct a genomic library. This may include the vendor name, kit name and kit version (e.g., Agilent sure select Human Exome V8, Twist RefSeq Exome).
     * [ExperimentMethod➞library_preparation_kit_retail_name](ExperimentMethod_library_preparation_kit_retail_name.md)
 * [library_selection_methods](library_selection_methods.md) - One or more methods used to select for or against, enrich, or screen the material being sequenced (e.g., random, PCA, cDNA).
     * [ExperimentMethod➞library_selection_methods](ExperimentMethod_library_selection_methods.md)
 * [library_type](library_type.md) - Describe the level of omics analysis (e.g., WGS, ATAC).
     * [ExperimentMethod➞library_type](ExperimentMethod_library_type.md)
 * [name](name.md) - The name for an entity.
     * [AnalysisMethod➞name](AnalysisMethod_name.md) - A name identifying this Analysis Method.
     * [DataAccessPolicy➞name](DataAccessPolicy_name.md) - A name for this Data Access Policy.
     * [ExperimentMethod➞name](ExperimentMethod_name.md) - A short name identifying this Experiment Method.
     * [File➞name](File_name.md) - The given filename.
     * [Sample➞name](Sample_name.md) - A descriptive name of this Sample (e.g., GHGAS_Blood_Sample1 or GHGAS_PBMC_RNAseq_S1). This property must not include any personally identifiable data.
 * [parameters](parameters.md) - Key/value pairs where key corresponds to a parameter name and value corresponds to a parameter value (e.g., 'aligner' = 'star_salmon',  'hisat2_build_memory' = '200.GB', 'split_fastq' = 50000000).
     * [AnalysisMethod➞parameters](AnalysisMethod_parameters.md)
 * [phenotypic_features_ids](phenotypic_features_ids.md) - The corresponding ID to the HPO vocabulary (e.g., HP:0002732, HP:0012735, HP:0002615).
     * [Individual➞phenotypic_features_ids](Individual_phenotypic_features_ids.md)
 * [phenotypic_features_terms](phenotypic_features_terms.md) - The phenotypic feature concepts that the entity is associated with at the time of retrieval from the organism. The Phenotypic Feature is captured using a concept from the Human Phenotype Ontology (e.g., Lymph node hypoplasia, Cough, Hypotension).
     * [Individual➞phenotypic_features_terms](Individual_phenotypic_features_terms.md)
 * [policy_text](policy_text.md) - The complete text for the Data Access Policy.
     * [DataAccessPolicy➞policy_text](DataAccessPolicy_policy_text.md)
 * [policy_url](policy_url.md) - An alternative to the Data Access Policy text is to provide the URL for the policy. This is useful if the terms of the policy are available online at a resolvable URL.
     * [DataAccessPolicy➞policy_url](DataAccessPolicy_policy_url.md)
 * [primer](primer.md) - The type of primer used for reverse transcription (e.g., oligo-dT or random).
     * [ExperimentMethod➞primer](ExperimentMethod_primer.md)
 * [process_data_files](process_data_files.md) - The Process Data Files associated with an entity.
     * [Submission➞process_data_files](Submission_process_data_files.md) - One or more Process Data Files associated with this Submission.
 * [publications](publications.md) - The Publication associated with an entity.
     * [Submission➞publications](Submission_publications.md) - One or more Publication entities associated with this Submission.
 * [research_data_files](research_data_files.md) - The Research Data Files associated with an entity.
     * [Analysis➞research_data_files](Analysis_research_data_files.md) - One or more aliases of the Research Data Files that this Analysis used as input to create Process Data Files.
     * [Submission➞research_data_files](Submission_research_data_files.md) - One or more Research Data Files associated with this Submission.
 * [rnaseq_strandedness](rnaseq_strandedness.md) - The strandedness of the library, whether reads come from both strands of the cDNA or only from the first (antisense) or the second (sense) strand.
     * [ExperimentMethod➞rnaseq_strandedness](ExperimentMethod_rnaseq_strandedness.md)
 * [sample](sample.md) - The Sample associated with an entity.
     * [Experiment➞sample](Experiment_sample.md) - The alias of one or more Samples that are associated with this Experiment.
 * [sample_barcode_read](sample_barcode_read.md) - The type of read that contains the sample barcode (e.g., index1, index2, read1, read2).
     * [ExperimentMethod➞sample_barcode_read](ExperimentMethod_sample_barcode_read.md)
 * [samples](samples.md) - The Samples associated with an entity.
     * [Submission➞samples](Submission_samples.md) - One or more Sample entities associated with this Submission.
 * [sequencing_center](sequencing_center.md) - Center where sample was sequenced.
     * [ExperimentMethod➞sequencing_center](ExperimentMethod_sequencing_center.md)
 * [sequencing_lane_id](sequencing_lane_id.md) - The identifier of a sequencing lane.
     * [ResearchDataFile➞sequencing_lane_id](ResearchDataFile_sequencing_lane_id.md)
 * [sequencing_layout](sequencing_layout.md) - Describe whether the library was sequenced in single-end (forward or reverse) or paired-end mode.
     * [ExperimentMethod➞sequencing_layout](ExperimentMethod_sequencing_layout.md)
 * [sequencing_read_length](sequencing_read_length.md) - Length of sequencing reads (e.g., long or short or actual number of the read length).
     * [ExperimentMethod➞sequencing_read_length](ExperimentMethod_sequencing_read_length.md)
 * [sex](sex.md) - The genotypic sex of the Individual (e.g., female).
     * [Individual➞sex](Individual_sex.md)
 * [size](size.md) - The size of the File in bytes.
     * [File➞size](File_size.md)
 * [software_versions](software_versions.md) - key/value pairs where key corresponds to a software name and value corresponds to a version descriptor (e.g., `salmon` = '1.3.0', `trim-galore` = '0.6.6', `bedtools` = '2.29.2').
     * [AnalysisMethod➞software_versions](AnalysisMethod_software_versions.md)
 * [storage](storage.md) - Methods by which a Sample is stored.
     * [Sample➞storage](Sample_storage.md)
 * [studies](studies.md) - The Study associated with an entity.
     * [Submission➞studies](Submission_studies.md) - Study entities associated with this Submission.
 * [study](study.md) - The Study associated with an entity.
     * [Dataset➞study](Dataset_study.md) - The Study associated with this Dataset.
     * [Publication➞study](Publication_study.md) - The Study entity associated with this Publication.
 * [target_coverage](target_coverage.md) - Mean coverage for whole genome sequencing, or mean target coverage for whole exome and targeted sequencing, (i.e. the number of times a particular locus was sequenced).
     * [ExperimentMethod➞target_coverage](ExperimentMethod_target_coverage.md)
 * [target_regions](target_regions.md) - Subset of genes or specific regions of the genome, which are most likely to be involved in the phenotype under study.
     * [ExperimentMethod➞target_regions](ExperimentMethod_target_regions.md)
 * [technical_replicate](technical_replicate.md) - An integer to indicate the technical replicate of this File.
     * [ResearchDataFile➞technical_replicate](ResearchDataFile_technical_replicate.md)
 * [title](title.md) - The title that describes an entity.
     * [Analysis➞title](Analysis_title.md)
     * [Dataset➞title](Dataset_title.md) - A title for this Dataset.
     * [Experiment➞title](Experiment_title.md) - The title for this Experiment (e.g., GHGAE_PBMC_RNAseq).
     * [Publication➞title](Publication_title.md) - The title for this Publication.
     * [Study➞title](Study_title.md) - A comprehensive title for this Study.
 * [type](type.md) - The type of an entity. Note: Not to be confused with rdf:type.
     * [AnalysisMethod➞type](AnalysisMethod_type.md)
     * [Analysis➞type](Analysis_type.md) - The type of this Analysis.
     * [ExperimentMethod➞type](ExperimentMethod_type.md) - The type associated with this Experiment Method.
     * [Experiment➞type](Experiment_type.md) - The type of this Experiment.
     * [Sample➞type](Sample_type.md) - The type of the Sample.
 * [types](types.md) - The types of an entity. Note: Not to be confused with rdf:type.
     * [Dataset➞types](Dataset_types.md) - The type of this Dataset.
     * [Study➞types](Study_types.md) - One or more types of this Study (e.g., Cancer Genomics, Epigenetics, Exome Sequencing).
 * [value](value.md) - The value for an attribute (e.g., a numerical value without the units).
     * [Attribute➞value](Attribute_value.md)
 * [value_type](value_type.md) - The value_type that characterizes the attribute value (e.g., percentage (SIO:001413)).
     * [Attribute➞value_type](Attribute_value_type.md)
 * [workflow_doi](workflow_doi.md) - A digital object identifier for the workflow. Can be a publication or the workflow commit that was used for the Analysis.
     * [AnalysisMethod➞workflow_doi](AnalysisMethod_workflow_doi.md)
 * [workflow_name](workflow_name.md) - The workflow name.
     * [AnalysisMethod➞workflow_name](AnalysisMethod_workflow_name.md)
 * [workflow_repository](workflow_repository.md) - The workflow repository (e.g., the URL).
     * [AnalysisMethod➞workflow_repository](AnalysisMethod_workflow_repository.md)
 * [workflow_tasks](workflow_tasks.md) - Tasks performed by the workflow
     * [AnalysisMethod➞workflow_tasks](AnalysisMethod_workflow_tasks.md)
 * [workflow_version](workflow_version.md) - The workflow version.
     * [AnalysisMethod➞workflow_version](AnalysisMethod_workflow_version.md)
 * [xref](xref.md) - Database cross references for an entity.
     * [Publication➞xref](Publication_xref.md) - One or more cross-references for this Publication.
     * [Sample➞xref](Sample_xref.md) - One or more cross-references for this Sample (e.g., this Sample may have an EBI BioSamples accession ID).
 * [year](year.md) - The year in which the paper was published.
     * [Publication➞year](Publication_year.md)

### Enums

 * [AgeRangeEnum](AgeRangeEnum.md) - Enum to capture the age range that an Indiviudal belongs to.
 * [AncestryEnum](AncestryEnum.md) - Permitted values for ancestry.
 * [CaseControlStatusEnum](CaseControlStatusEnum.md) - Enum to capture whether a condition corresponds to a case or a control condition.
 * [DataUseModifierEnum](DataUseModifierEnum.md) - Permitted values for data use modifier.
 * [DataUsePermissionEnum](DataUsePermissionEnum.md) - Permitted values for data use permission.
 * [DiseaseOrHealthyEnum](DiseaseOrHealthyEnum.md) - Enum to capture whether a condition corresponds to a disease or a healthy state.
 * [EndBiasEnum](EndBiasEnum.md) - Permitted values for end bias.
 * [FlowCellTypeEnum](FlowCellTypeEnum.md) - Permitted values for flow cell type.
 * [GeographicalRegionEnum](GeographicalRegionEnum.md) - Permitted values for geographical region.
 * [IndividualSexEnum](IndividualSexEnum.md) - The sex of an Individual as as defined in a specific medical and clinical context.
 * [InstrumentModelEnum](InstrumentModelEnum.md) - Permitted values for the instrument model.
 * [IsolationEnum](IsolationEnum.md) - Describes how biomaterial was isolated.
 * [LibraryPreparationKitRetailNameEnum](LibraryPreparationKitRetailNameEnum.md) - Permitted values for library preparation kit retail name.
 * [LibraryPreparationLibrarySelectionEnum](LibraryPreparationLibrarySelectionEnum.md) - Permitted vocabulary for library selections.
 * [LibraryPreparationLibraryTypeEnum](LibraryPreparationLibraryTypeEnum.md) - The type of the library.
 * [LibraryPreparationRNASeqStrandednessEnum](LibraryPreparationRNASeqStrandednessEnum.md) - Permitted values for library preparation RNASeq strandedness.
 * [PhenotypicFeaturesEnum](PhenotypicFeaturesEnum.md) - An enum describing permissible phenotype descriptors.
 * [PrimerEnum](PrimerEnum.md) - Permitted values for primer.
 * [ProcessDataFileFormatEnum](ProcessDataFileFormatEnum.md) - Enum to capture Process Data File formats.
 * [ResearchDataFileFormatEnum](ResearchDataFileFormatEnum.md) - Enum to capture Research Data File formats.
 * [SampleBarcodeReadEnum](SampleBarcodeReadEnum.md) - Permitted values for sample barcode read.
 * [SampleTypeEnum](SampleTypeEnum.md) - The type of a sample
 * [SequencingProtocolSequencingLayoutEnum](SequencingProtocolSequencingLayoutEnum.md) - Single-end vs paired-end sequencing.
 * [StorageEnum](StorageEnum.md) - Enum to capture how a Sample or Biospecimen was stored.
 * [StudyTypeEnum](StudyTypeEnum.md) - Enum to capture the type of a study.
 * [SupportingFileFormatEnum](SupportingFileFormatEnum.md) - Enum to capture Supporting File types.
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
