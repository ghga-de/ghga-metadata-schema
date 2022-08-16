
# Subset: essential


Subset of properties that are considered to be essential for the functionality of GHGA.

URI: [GHGA:essential](https://w3id.org/GHGA/essential)


### Classes


### Mixins


### Slots

 * [affiliation](affiliation.md) - The Institution(s) associated with an entity.
 * [age](age.md) - Age of an individual.
 * [alias](alias.md) - The alias for an entity.
 * [analysis process➞has input](analysis_process_has_input.md) - The input data File entities used in the Analysis Process.
 * [analysis➞alias](analysis_alias.md) - An alias uniquely identifying this Analysis entitiy.
 * [analysis➞description](analysis_description.md) - Describing how an Analysis was carried out. (e.g.: computational tools, settings, etc.).
 * [analysis➞has input](analysis_has_input.md) - The input data File entities used in the Analysis.
 * [analysis➞has study](analysis_has_study.md) - The Study entity associated with this Analysis.
 * [analysis➞reference chromosome](analysis_reference_chromosome.md)
 * [analysis➞reference genome](analysis_reference_genome.md)
 * [analysis➞type](analysis_type.md) - The type of the Analysis. Either Reference Alignment (BAM) or Sequence Variation (VCF)
 * [biospecimen➞alias](biospecimen_alias.md) - The alias for an entity.
 * [biospecimen➞has disease](biospecimen_has_disease.md) - The Disease entity that is associated with the Individual. Typically, a concept from Mondo Disease Ontology. For example, 'MONDO:0005267' indicates that the Individual suffers from 'Heart Disease'.
 * [biospecimen➞has individual](biospecimen_has_individual.md) - The Individual entity from which this Biospecimen was derived.
 * [biospecimen➞has phenotypic feature](biospecimen_has_phenotypic_feature.md) - The Phenotypic Feature entity that is associated with the Individual. Typically, a concept from Human Phenotype Ontology. For example, 'HP:0100244' indicates that the Individual exhibits 'Fibrosarcoma' as one of its phenotype.
 * [biospecimen➞type](biospecimen_type.md) - The type of Biospecimen.
 * [checksum](checksum.md) - A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data. The receiving system recomputes the checksum based upon the received data and compares this value with the one sent with the data. If the two values are the same, the receiver has some confidence that the data was received correctly.
 * [checksum type](checksum_type.md) - The type of algorithm used to generate the checksum of a file.
 * [data access committee➞alias](data_access_committee_alias.md) - The alias for an entity.
 * [data access committee➞description](data_access_committee_description.md) - A description for the Data Access Committee.
 * [data access committee➞main contact](data_access_committee_main_contact.md) - The main contact for the Data Access Committee.
 * [data access committee➞name](data_access_committee_name.md) - The name for the Data Access Committee.
 * [data access policy➞alias](data_access_policy_alias.md) - The alias for an entity.
 * [data access policy➞description](data_access_policy_description.md) - A short description for the Data Access Policy.
 * [data access policy➞has data access committee](data_access_policy_has_data_access_committee.md) - The Data Access Committee linked to this policy.
 * [data access policy➞name](data_access_policy_name.md) - A name for the Data Access Policy.
 * [data access policy➞policy text](data_access_policy_policy_text.md) - The terms of data use and policy verbiage should be captured here.
 * [dataset➞alias](dataset_alias.md) - The alias for an entity.
 * [dataset➞description](dataset_description.md)
 * [dataset➞has analysis](dataset_has_analysis.md) - One or more Analysis entities that are referenced by this Dataset.
 * [dataset➞has data access policy](dataset_has_data_access_policy.md) - The Data Access Policy that applies to this Dataset.
 * [dataset➞has experiment](dataset_has_experiment.md) - One or more Experiment entities that are referenced by this Dataset.
 * [dataset➞has file](dataset_has_file.md) - One or more File entities that collectively are part of this Dataset.
 * [dataset➞has sample](dataset_has_sample.md) - One or more Sample entities that are referenced by this Dataset.
 * [dataset➞has study](dataset_has_study.md) - One or more Study entities that are referenced by this Dataset.
 * [dataset➞title](dataset_title.md) - A title for the submitted Dataset.
 * [dataset➞type](dataset_type.md)
 * [description](description.md) - Description of an entity.
 * [experiment process➞has input](experiment_process_has_input.md) - The input to the Experiment Process. Usually a Sample entity.
 * [experiment process➞has protocol](experiment_process_has_protocol.md) - The Protocol entity used by this Experiment Process.
 * [experiment process➞title](experiment_process_title.md) - A descriptive title that explains the step(s) involved in performing the experiment leading up to the sequencing of the sample and generation of raw data from the instrument. (eg: Sample extraction -> Target Enrichment)
 * [experiment process➞type](experiment_process_type.md) - The type of experiment process.
 * [experiment➞alias](experiment_alias.md) - The alias for an entity.
 * [experiment➞description](experiment_description.md) - A detailed description of the Experiment.
 * [experiment➞has experiment process](experiment_has_experiment_process.md) - One or more Experiment Processes entities associated with this Experiment.
 * [experiment➞has file](experiment_has_file.md) - One or more Files entities that are generated as output of this Experiment.
 * [experiment➞has protocol](experiment_has_protocol.md) - One or more Protocol entities associated with this Experiment.
 * [experiment➞has sample](experiment_has_sample.md) - The Sample entity associated with this Experiment.
 * [experiment➞has study](experiment_has_study.md) - The Study entity associated with this Experiment.
 * [experiment➞title](experiment_title.md) - Name for the experiment (eg: GHGAE_PBMC_RNAseq).
 * [experiment➞type](experiment_type.md) - The type of Experiment.
 * [file➞alias](file_alias.md) - The alias for an entity.
 * [file➞checksum](file_checksum.md)
 * [file➞checksum type](file_checksum_type.md)
 * [file➞format](file_format.md)
 * [file➞name](file_name.md) - The given filename.
 * [format](format.md) - The format of the file: BAM, SAM, CRAM, BAI, etc.
 * [has analysis](has_analysis.md) - The analysis associated with an entity.
 * [has data access committee](has_data_access_committee.md) - Data Access Committee associated with an entity.
 * [has data access policy](has_data_access_policy.md) - Data Access Policy associated with an entity.
 * [has disease](has_disease.md) - Disease concept that the entity is associated with.
 * [has experiment](has_experiment.md) - The experiment associated with an entity.
 * [has experiment process](has_experiment_process.md)
 * [has file](has_file.md) - The file associated with an entity.
 * [has individual](has_individual.md) - The subject/individual associated with an entity.
 * [has input](has_input.md) - The input to a Planned Process.
 * [has phenotypic feature](has_phenotypic_feature.md) - Phenotypic feature concept that the entity is associated with.
 * [has protocol](has_protocol.md) - The protocol associated with an entity.
 * [has sample](has_sample.md) - The sample associated with an entity.
 * [has study](has_study.md) - The study associated with an entity.
 * [id](id.md) - An identifier that uniquely represents an entity.
 * [individual➞age](individual_age.md)
 * [individual➞alias](individual_alias.md) - The alias for an entity.
 * [individual➞has disease](individual_has_disease.md) - The Disease entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Mondo Disease Ontology. For example, 'MONDO:0003742' indicates that the Individual - from which the Biospecimen was extracted from - suffers from 'Heart Fibrosarcoma'.
 * [individual➞has file](individual_has_file.md) - Additional/supplementary files associated with an Individual. Typically, a phenopacket or pedigree file.
 * [individual➞has phenotypic feature](individual_has_phenotypic_feature.md) - The Phenotypic Feature entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Human Phenotype Ontology. For example, 'HP:0100244' indicates that the Individual - from which the Biospecimen was extracted from - exhibits 'Fibrosarcoma' as one of its phenotype.
 * [individual➞sex](individual_sex.md)
 * [individual➞vital status](individual_vital_status.md) - Last known Vital Status of an Individual.
 * [instrument model](instrument_model.md) - The name and model of the technology platform used to perform sequencing.
 * [library layout](library_layout.md) - Describe whether the library was sequenced in single-end (forward or reverse) or paired-end mode
 * [library name](library_name.md) - A short name identifying the library to potential users. The same name may refer to multiple versions of the same continually updated library.
 * [library preparation](library_preparation.md) - The general method for sequencing library preparation (e.g. KAPA PCR-free).
 * [library preparation protocol➞alias](library_preparation_protocol_alias.md)
 * [library preparation protocol➞description](library_preparation_protocol_description.md) - Description about how a sequencing library was prepared (eg: Library construction method).
 * [library preparation protocol➞library layout](library_preparation_protocol_library_layout.md)
 * [library preparation protocol➞library name](library_preparation_protocol_library_name.md)
 * [library preparation protocol➞library preparation](library_preparation_protocol_library_preparation.md)
 * [library preparation protocol➞library selection](library_preparation_protocol_library_selection.md)
 * [library preparation protocol➞library type](library_preparation_protocol_library_type.md)
 * [library selection](library_selection.md) - Whether any method was used to select for or against, enrich, or screen the material being sequenced. Library Selection method (e.g. random, PCA, cDNA, etc )
 * [library type](library_type.md) - Describe the level of omics analysis (eg: Metagenome, transcriptome, etc)
 * [main contact](main_contact.md) - The person who is the main contact for a committee.
 * [name](name.md) - The name for an entity.
 * [named thing➞alias](named_thing_alias.md) - The alias (alternate identifier) for an entity.
 * [named thing➞id](named_thing_id.md) - The internal unique identifier for an entity.
 * [ontology class mixin➞description](ontology_class_mixin_description.md) - The description or definition of an ontology class.
 * [ontology class mixin➞name](ontology_class_mixin_name.md) - The name or label (rdfs:label) of an ontology class.
 * [policy text](policy_text.md) - The complete text for the Data Access Policy.
 * [project➞alias](project_alias.md) - The alias for an entity.
 * [project➞description](project_description.md) - Short textual description of the project.
 * [project➞title](project_title.md) - Comprehensive title for the project.
 * [protocol➞alias](protocol_alias.md) - The alias for an entity.
 * [protocol➞description](protocol_description.md) - Detailed description of the Protocol.
 * [protocol➞has file](protocol_has_file.md) - A document that describes the Protocol.
 * [protocol➞name](protocol_name.md) - Name of the protocol (eg: Sample extraction_PCR amplification).
 * [protocol➞type](protocol_type.md) - Type of the protocol (eg: Target enrichment).
 * [publication➞alias](publication_alias.md) - The alias for an entity.
 * [publication➞id](publication_id.md) - An identifier that uniquely represents an entity.
 * [publication➞title](publication_title.md) - The title for the Publication.
 * [reference chromosome](reference_chromosome.md) - The reference chromosome used for this Analysis.
 * [reference genome](reference_genome.md) - A published genetic sequence that is used as a reference sequence against which other sequences are compared. Reference genome(s) or annotation(s) used for prior analyses (eg: GRCh38.p13).
 * [sample➞alias](sample_alias.md) - The alias for an entity.
 * [sample➞description](sample_description.md) - Short textual description of the sample (How the sample was collected, sample source, protocol followed for processing the sample etc).
 * [sample➞has individual](sample_has_individual.md) - The Individual from which this Sample was derived from.
 * [sample➞name](sample_name.md) - Name of the sample (eg:GHGAS_Blood_Sample1 or GHGAS_PBMC_RNAseq_S1).
 * [sample➞type](sample_type.md) - The type of sample.
 * [sequencing protocol➞alias](sequencing_protocol_alias.md)
 * [sequencing protocol➞description](sequencing_protocol_description.md) - Description about the sequencing protocol (eg: mRNA-seq,Whole exome long-read sequencing etc).
 * [sequencing protocol➞instrument model](sequencing_protocol_instrument_model.md)
 * [sequencing protocol➞type](sequencing_protocol_type.md) - Name of the library preparation protocol (eg: mRNA-seq,Whole exome long-read sequencing etc).
 * [sex](sex.md) - The assemblage of physical properties or qualities by which male is distinguished from female; the physical difference between male and female; the distinguishing peculiarity of male or female.
 * [study➞affiliation](study_affiliation.md)
 * [study➞alias](study_alias.md) - The alias for an entity.
 * [study➞description](study_description.md) - A detailed description (abstract) that describes the goals of this Study.
 * [study➞has file](study_has_file.md) - Additional/supplementary files associated with a Study.
 * [study➞title](study_title.md) - A comprehensive title for the study.
 * [study➞type](study_type.md) - The type of Study. For example, 'Cancer Genomics', 'Epigenetics', 'Exome Sequencing'.
 * [submission➞affiliation](submission_affiliation.md) - Institution/Center/Data Hub that is providing this submission.
 * [submission➞has analysis](submission_has_analysis.md) - Information about one or more Analysis entities associated with this submission.
 * [submission➞has data access committee](submission_has_data_access_committee.md) - The Data Access Committee that applies to Dataset in this submission.
 * [submission➞has data access policy](submission_has_data_access_policy.md) - The Data Access Policy that applies to Dataset in this submission.
 * [submission➞has experiment](submission_has_experiment.md) - Information about one or more Experiment entities associated with this submission.
 * [submission➞has file](submission_has_file.md) - Information about one or more File entities associated with this submission.
 * [submission➞has individual](submission_has_individual.md) - Information about one or more Individual entities associated with this submission.
 * [submission➞has protocol](submission_has_protocol.md) - One or more Protocol entities associated with this Submission.
 * [submission➞has sample](submission_has_sample.md) - Information about one or more Sample entities associated with this submission.
 * [submission➞has study](submission_has_study.md) - Information about a Study entities associated with this submission.
 * [submission➞id](submission_id.md) - A internal unique identifier for the Submission.
 * [target regions](target_regions.md) - Subset of genes or specific regions of the genome, which are most likely to be involved in the phenotype under study.
 * [tissue](tissue.md) - An anatomical structure consisting of similarly specialized cells and intercellular matrix, aggregated according to genetically determined spatial relationships, performing a specific function.
 * [title](title.md) - The title that describes an entity.
 * [type](type.md) - The type of an entity.
 * [vital status](vital_status.md) - The state or condition of being living or deceased; also includes the case where the vital status is unknown.
 * [workflow➞alias](workflow_alias.md) - The alias for an entity.
 * [workflow➞name](workflow_name.md)

### Types


### Enums

