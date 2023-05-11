
# GHGA-Submission-Metadata-Schema


**metamodel version:** 1.7.0

**version:** 0.9.0


The submission centric metadata schema for the German Human Genome-Phenome Archive (GHGA).


### Classes

 * [AnalysisProcess](AnalysisProcess.md)
 * [Attribute](Attribute.md) - A key/value pair that further characterizes an entity.
 * [BiologicalQuality](BiologicalQuality.md) - A BiologicalQuality is a quality held by a biological entity.
     * [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) - Disease or Phenotypic Feature that the entity is associated with. This entity is a union of Disease and Phenotypic Feature and exists to accommodate situations where Disease concepts are used interchangeably with Phenotype concepts or vice-versa.
         * [Disease](Disease.md) - A disease is a disposition to undergo pathological processes that exists in an organism because of one or more disorders in that organism.
         * [PhenotypicFeature](PhenotypicFeature.md) - The observable form taken by some character (or group of characters) in an individual or an organism, excluding pathology and disease. The detectable outward manifestations of a specific genotype.
 * [Committee](Committee.md) - A group of people organized for a specific purpose.
     * [DataAccessCommittee](DataAccessCommittee.md) - A group of members that are delegated to grant access to one or more datasets after ensuring the minimum criteria for data sharing has been met, and request for data use does not raise ethical and/or legal concerns.
 * [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.
     * [DataAccessPolicy](DataAccessPolicy.md) - A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.
     * [DataUseModifier](DataUseModifier.md) - Data use modifiers indicate additional conditions for use.
     * [DataUsePermission](DataUsePermission.md) - A data item that is used to indicate consent permissions for datasets and/or materials and relates to the purposes for which datasets and/or material might be removed, stored or used.
     * [Dataset](Dataset.md) - A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
     * [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.
         * [AnalysisProcessOutputFile](AnalysisProcessOutputFile.md) - A AnalysisProcessOutputFile is a File that is associated as an output file with an AnalysisProcess.
         * [SampleFile](SampleFile.md) - A SampleFile is a File that is associated with a Sample.
         * [SequencingProcessFile](SequencingProcessFile.md) - A SequencingProcessFile is a File that is associated with a SequencingProcess.
         * [StudyFile](StudyFile.md) - A StudyFile is a File that is associated with a Study.
     * [Protocol](Protocol.md) - A plan specification which has sufficient level of detail and quantitative information to communicate it between Investigation agents, so that different Investigation agents will reliably be able to independently reproduce the process.
         * [LibraryPreparationProtocol](LibraryPreparationProtocol.md) - Information about the library_preparation of an sequencing experiment.
         * [SequencingProtocol](SequencingProtocol.md) - Information about the sequencing of a sample.
     * [Publication](Publication.md) - The Publication entity represents a publication. While a publication can be any article that is published, the minimum expectation is that the publication has a valid DOI.
 * [MaterialEntity](MaterialEntity.md) - A MaterialEntity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.
     * [AnatomicalEntity](AnatomicalEntity.md) - Biological entity that is either an individual member of a biological species or constitutes the structural organization of an individual member of a biological species.
     * [Biospecimen](Biospecimen.md) - A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics, treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is derived.
     * [Population](Population.md) - A Population is a collection of individuals from the same taxonomic class living, counted or sampled at a particular site or in a particular area.
         * [Ancestry](Ancestry.md) - Population category defined using ancestries informative markers (AIMs) based on genetic/genomic data.
     * [Sample](Sample.md) - A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).
 * [Person](Person.md) - A member of the species Homo sapiens.
     * [Individual](Individual.md) - An Individual is a Person who is participating in a Study.
     * [Member](Member.md) - Member of an Organization or a Committee.
 * [PlannedProcess](PlannedProcess.md) - A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and depends on some entity during the time it occurs.
     * [DataTransformation](DataTransformation.md) - A DataTransformation technique used to analyze and interpret data to gain a better understanding of it.
         * [Analysis](Analysis.md) - An Analysis is a data transformation that transforms input data to output data. The workflow used to achieve this transformation and the individual steps are also captured.
     * [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.
         * [Condition](Condition.md) - An condition that is linked to comparable samples.
         * [SequencingExperiment](SequencingExperiment.md) - An sequencing experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
         * [SequencingProcess](SequencingProcess.md) - A sequencing process linking a sample to sequencing output.
         * [Study](Study.md) - Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.
     * [ResearchActivity](ResearchActivity.md) - A PlannedProcess executed in the performance of scientific research wherein systematic Investigations are performed to establish facts and reach new conclusions about phenomena in the world.
 * [Submission](Submission.md) - A grouping entity that represents information about one or more entities. A submission can be considered as a set of inter-related (and inter-connected) entities that represent a data submission to GHGA.

### Mixins

 * [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 * [AliasMixin](AliasMixin.md) - Mixin for entities that can be assigned an alias at the time of metadata submission.
     * [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 * [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.
 * [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an ega_accession, in addition to GHGA accession.
 * [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 * [OntologyClassMixin](OntologyClassMixin.md) - Mixin for entities that represent an class/term/concept from an ontology.

### Slots

 * [abstract](abstract.md) - The study abstract that describes the goals.  Can also hold abstract from a publication related to this study
     * [Publication➞abstract](Publication_abstract.md) - The study abstract that describes the goals. Can also hold abstract from a publication related to this study.
 * [accession](accession.md) - A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * [AccessionMixin➞accession](AccessionMixin_accession.md)
 * [additional_name](additional_name.md) - additional_name(s).
     * [Person➞additional_name](Person_additional_name.md)
 * [affiliation](affiliation.md) - The Institution(s) associated with an entity.
 * [affiliations](affiliations.md) - The Institution(s) associated with an entity.
     * [Study➞affiliations](Study_affiliations.md)
 * [age](age.md) - Age of an individual.
     * [Individual➞age](Individual_age.md)
 * [alias](alias.md) - The alias for an entity at the time of submission.
     * [AliasMixin➞alias](AliasMixin_alias.md)
         * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)
     * [Analysis➞alias](Analysis_alias.md) - An alias uniquely identifying this Analysis entitiy.
     * [Study➞alias](Study_alias.md)
 * [analyses](analyses.md) - The analyses associated with an entity.
     * [Submission➞analyses](Submission_analyses.md) - Information about one or more Analysis entities associated with this submission.
 * [analysis](analysis.md) - The Analysis associated with an entity
     * [AnalysisProcess➞analysis](AnalysisProcess_analysis.md) - The Analysis the AnalysisProcess was part of
 * [analysis_process](analysis_process.md) - The AnalysisProcess associated with an entity.
     * [AnalysisProcessOutputFile➞analysis_process](AnalysisProcessOutputFile_analysis_process.md)
 * [analysis_process_output_files](analysis_process_output_files.md) - The AnalysisProcessOutputFiles associated with an entity.
     * [Submission➞analysis_process_output_files](Submission_analysis_process_output_files.md) - The AnalysisProcessOutputFiles that are part of this submission.
 * [anatomical_entities](anatomical_entities.md) - Anatomical sites associated with an entity.
     * [Biospecimen➞anatomical_entities](Biospecimen_anatomical_entities.md)
 * [ancestries](ancestries.md) - A person's descent or lineage, from a person or from a population. Typically this is a value from HANCESTRO (Human Ancestry Ontology).
     * [Individual➞ancestries](Individual_ancestries.md)
 * [attributes](attributes.md) - Key/value pairs corresponding to an entity.
     * [LibraryPreparationProtocol➞attributes](LibraryPreparationProtocol_attributes.md) - One or more attributes that further characterizes this library_preparation Protocol.
     * [Protocol➞attributes](Protocol_attributes.md) - One or more attributes that further characterizes this protocol.
     * [SequencingProtocol➞attributes](SequencingProtocol_attributes.md) - One or more attributes that further characterizes this Sequencing Protocol.
     * [Study➞attributes](Study_attributes.md) - Custom key/value pairs that further characterizes the Study. (e.g.: approaches - single-cell,_bulk_etc)
 * [author](author.md) - The individual who is responsible for the content of a document version.
     * [Publication➞author](Publication_author.md)
 * [biological_replicates](biological_replicates.md) - A biological replicate is a replicate role that consists of independent biological replicates made from different individual biosamples.
 * [biospecimen](biospecimen.md) - The biospecimen associated with an entity.
     * [Sample➞biospecimen](Sample_biospecimen.md) - The Biospecimen from which this Sample was prepared from.
 * [biospecimens](biospecimens.md) - The biospecimens associated with an entity.
     * [Submission➞biospecimens](Submission_biospecimens.md) - Information about one or more Biospecimen entities associated with this submission.
 * [category](category.md) - The category for this file: Whole Genome Sequencing, Whole Exome Sequencing, etc.
 * [cell_barcode_offset](cell_barcode_offset.md) - The offset in sequence of the cell identifying barcode. (Eg. '0').
     * [SequencingProtocol➞cell_barcode_offset](SequencingProtocol_cell_barcode_offset.md)
 * [cell_barcode_read](cell_barcode_read.md) - The type of read that contains the cell barcode (eg: index1/index2/read1/read2).
     * [SequencingProtocol➞cell_barcode_read](SequencingProtocol_cell_barcode_read.md)
 * [cell_barcode_size](cell_barcode_size.md) - The size of the cell identifying barcode (E.g. '16').
     * [SequencingProtocol➞cell_barcode_size](SequencingProtocol_cell_barcode_size.md)
 * [checksum](checksum.md) - A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data. The receiving system recomputes the checksum based upon the received data and compares this value with the one sent with the data. If the two values are the same, the receiver has some confidence that the data was received correctly.
     * [File➞checksum](File_checksum.md)
 * [checksum_type](checksum_type.md) - The type of algorithm used to generate the checksum of a file.
     * [File➞checksum_type](File_checksum_type.md)
 * [children](children.md) - One or more children for an Individual.
     * [Individual➞children](Individual_children.md)
 * [concept_identifier](concept_identifier.md) - The Compact URI (CURIE) that uniquely identifies a concept from an ontology, thesaurus, or terminology.
     * [OntologyClassMixin➞concept_identifier](OntologyClassMixin_concept_identifier.md) - The Compact URI (CURIE) that uniquely identifies this ontology class.
 * [concept_name](concept_name.md) - The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.
     * [OntologyClassMixin➞concept_name](OntologyClassMixin_concept_name.md)
 * [condition](condition.md) - The condition associated with an entity.
     * [Sample➞condition](Sample_condition.md)
 * [conditions](conditions.md) - The condition associated with an entity.
     * [Study➞conditions](Study_conditions.md)
 * [data_access_committee](data_access_committee.md) - Data Access Committee associated with an entity.
     * [DataAccessPolicy➞data_access_committee](DataAccessPolicy_data_access_committee.md) - The Data Access Committee linked to this policy.
 * [data_access_committees](data_access_committees.md) - Data Access Committees associated with an entity.
     * [Submission➞data_access_committees](Submission_data_access_committees.md) - The Data Access Committee that applies to Dataset in this submission.
 * [data_access_policies](data_access_policies.md) - Data Access Policies associated with an entity.
     * [Submission➞data_access_policies](Submission_data_access_policies.md) - The Data Access Policy that applies to Dataset in this submission.
 * [data_access_policy](data_access_policy.md) - Data Access Policy associated with an entity.
     * [Dataset➞data_access_policy](Dataset_data_access_policy.md) - The Data Access Policy that applies to this Dataset.
 * [data_request_form](data_request_form.md) - Data Request Form that is associated with a Data Access Policy.
     * [DataAccessPolicy➞data_request_form](DataAccessPolicy_data_request_form.md) - Data Request Form that is associated with this Data Access Policy.
 * [data_use_modifiers](data_use_modifiers.md) - Modifier for Data use permission associated with an entity. Should be descendants of 'DUO:0000017 data use modifier'
     * [DataAccessPolicy➞data_use_modifiers](DataAccessPolicy_data_use_modifiers.md) - Modifier for Data use permission associated with a policy. Should be descendants of 'DUO:0000017 data use modifier'
 * [data_use_permission](data_use_permission.md) - Data use permission associated with an entity. Typically one or more terms from DUO. Should be descendants of 'DUO:0000001 data use permission'.
     * [DataAccessPolicy➞data_use_permission](DataAccessPolicy_data_use_permission.md) - Data use permission associated with a policy. Typically one or more terms from DUO and should be descendants of 'DUO:0000001 data use permission'.
 * [data_use_permissions](data_use_permissions.md) - Data use permissions associated with an entity. Typically one or more terms from DUO. Should be descendants of 'DUO:0000001 data use permission'.
 * [datasets](datasets.md) - The Datasets associated with an entity.
     * [Submission➞datasets](Submission_datasets.md) - One or more Dataset that are part of this submission.
 * [deprecation_date](deprecation_date.md) - The timestamp (in ISO 8601 format) when the entity was deprecated.
 * [description](description.md) - Description of an entity.
     * [Analysis➞description](Analysis_description.md) - Describing how an Analysis was carried out. (e.g.: computational tools, settings, etc.).
     * [Biospecimen➞description](Biospecimen_description.md)
     * [Condition➞description](Condition_description.md)
     * [DataAccessCommittee➞description](DataAccessCommittee_description.md) - A description for the Data Access Committee.
     * [DataAccessPolicy➞description](DataAccessPolicy_description.md) - A short description for the Data Access Policy.
     * [Dataset➞description](Dataset_description.md)
     * [LibraryPreparationProtocol➞description](LibraryPreparationProtocol_description.md) - Description about how a sequencing library was prepared (eg: Library construction method).
     * [OntologyClassMixin➞description](OntologyClassMixin_description.md) - The description or definition of an ontology class.
     * [Protocol➞description](Protocol_description.md) - Detailed description of the protocol.
     * [ResearchActivity➞description](ResearchActivity_description.md)
     * [Sample➞description](Sample_description.md) - Short textual description of the sample (How the sample was collected, sample source, Protocol followed for processing the sample etc).
     * [SequencingExperiment➞description](SequencingExperiment_description.md) - A detailed description of the Experiment.
     * [SequencingProcess➞description](SequencingProcess_description.md)
     * [SequencingProtocol➞description](SequencingProtocol_description.md) - Description about the sequencing Protocol (eg: mRNA-seq,Whole exome long-read sequencing etc).
     * [Study➞description](Study_description.md) - A detailed description (abstract) that describes the goals of this Study.
 * [disease_or_healthy](disease_or_healthy.md) - Whether a condition corresponds to a disease or a healthy state.
     * [Condition➞disease_or_healthy](Condition_disease_or_healthy.md)
 * [diseases](diseases.md) - Diseases concept that the entity is associated with.
     * [Individual➞diseases](Individual_diseases.md) - The Disease entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Mondo Disease Ontology. For example, 'MONDO:0003742' indicates that the Individual - from_which_the_Biospecimen was extracted from - suffers_from_'Heart_Fibrosarcoma'.
 * [doi](doi.md) - DOI identifier of a publication.
     * [Publication➞doi](Publication_doi.md) - DOI identifier of the Publication.
 * [ega_accession](ega_accession.md) - A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
     * [EgaAccessionMixin➞ega_accession](EgaAccessionMixin_ega_accession.md)
 * [email](email.md) - Email of a person.
     * [Member➞email](Member_email.md) - The email of the Member.
 * [end_bias](end_bias.md) - The end of the cDNA molecule that is preferentially sequenced, e.g. 3/5 prime tag or end, or the full-length transcript.
     * [LibraryPreparationProtocol➞end_bias](LibraryPreparationProtocol_end_bias.md)
 * [family_name](family_name.md) - Last name.
     * [Person➞family_name](Person_family_name.md)
 * [files](files.md) - The files associated with an entity.
     * [Dataset➞files](Dataset_files.md) - One or more File entities that collectively are part of this Dataset.
     * [Individual➞files](Individual_files.md) - Additional/supplementary files associated with an Individual. Typically, a phenopacket or pedigree file.
 * [flow_cell_id](flow_cell_id.md) - Flow Cell ID (eg: Experiment ID_Cell 1_Lane_1). The barcode assigned to a flow cell used in nucleotide sequencing.
     * [SequencingProtocol➞flow_cell_id](SequencingProtocol_flow_cell_id.md)
 * [flow_cell_type](flow_cell_type.md) - Type of flow cell used (e.g. S4, S2 for NovaSeq; PromethION, Flongle for Nanopore). Aparatus in the fluidic subsystem where the sheath and sample meet. Can be one of several types; jet-in-air, quartz cuvette, or a hybrid of the two. The sample flows through the center of a fluid column of sheath fluid in the flow cell.
     * [SequencingProtocol➞flow_cell_type](SequencingProtocol_flow_cell_type.md)
 * [format](format.md) - The format of the file: BAM, SAM, CRAM, BAI, etc.
     * [File➞format](File_format.md)
 * [forward_or_reverse](forward_or_reverse.md) - Denotes whether a submitted FASTQ file contains forward (R1) or reverse (R2) reads for paired-end sequencing. The number that identifies each read direction in a paired-end nucleotide sequencing reaction.
     * [SequencingProtocol➞forward_or_reverse](SequencingProtocol_forward_or_reverse.md)
 * [geographical_region](geographical_region.md) - The geographical region where the Individual is located. Any demarcated area of the Earth; may be determined by both natural and human boundaries.
     * [Individual➞geographical_region](Individual_geographical_region.md)
 * [given_name](given_name.md) - First name.
     * [Person➞given_name](Person_given_name.md)
 * [id](id.md) - An identifier that uniquely represents an entity.
     * [OntologyClassMixin➞id](OntologyClassMixin_id.md)
 * [index_sequence](index_sequence.md) - A unique nucleotide sequence that is added to a sample during library_preparation to serve as a unique identifier for the sample.
     * [SequencingProtocol➞index_sequence](SequencingProtocol_index_sequence.md)
 * [individual](individual.md) - The subject/individual associated with an entity.
     * [Biospecimen➞individual](Biospecimen_individual.md) - The Individual entity from which this Biospecimen was derived.
 * [individuals](individuals.md) - The subjects/individuals associated with an entity.
     * [Submission➞individuals](Submission_individuals.md) - Information about one or more Individual entities associated with this submission.
 * [inputs](inputs.md) - The inputs to a Planned Process.
 * [instrument_model](instrument_model.md) - The name and model of the technology platform used to perform sequencing.
     * [SequencingProtocol➞instrument_model](SequencingProtocol_instrument_model.md)
 * [isolation](isolation.md) - Method or device employed for collecting/isolating a biospecimen or a sample.
     * [Biospecimen➞isolation](Biospecimen_isolation.md)
 * [journal](journal.md) - Name of the journal.
     * [Publication➞journal](Publication_journal.md)
 * [karyotype](karyotype.md) - The karyotype of an individual if defined.
     * [Individual➞karyotype](Individual_karyotype.md)
 * [key](key.md) - The key of an attribute.
     * [Attribute➞key](Attribute_key.md) - The key for an attribute.
 * [key_type](key_type.md) - The semantic type for the key of an attribute.
     * [Attribute➞key_type](Attribute_key_type.md) - A semantic type that characterizes the attribute key. Usually this is a term from an ontology. For example, 'MAXO:0000616' indicates that the attribute is a measurement of oxygen saturation in the blood.
 * [lane_number](lane_number.md) - The numerical identifier for the lane or machine unit where a sample was located during nucleotide sequencing.
     * [SequencingProtocol➞lane_number](SequencingProtocol_lane_number.md)
 * [library_layout](library_layout.md) - Describe whether the library was sequenced in single-end (forward or reverse) or paired-end mode
     * [LibraryPreparationProtocol➞library_layout](LibraryPreparationProtocol_library_layout.md)
 * [library_name](library_name.md) - A short name identifying the library to potential users. The same name may refer to multiple versions of the same continually updated library.
     * [LibraryPreparationProtocol➞library_name](LibraryPreparationProtocol_library_name.md)
 * [library_preparation](library_preparation.md) - The general method for sequencing library_preparation (e.g. KAPA PCR-free).
     * [LibraryPreparationProtocol➞library_preparation](LibraryPreparationProtocol_library_preparation.md)
 * [library_preparation_kit_manufacturer](library_preparation_kit_manufacturer.md) - Manufacturer of library_preparation kit
     * [LibraryPreparationProtocol➞library_preparation_kit_manufacturer](LibraryPreparationProtocol_library_preparation_kit_manufacturer.md)
 * [library_preparation_kit_retail_name](library_preparation_kit_retail_name.md) - A unique identifier for the kit used to construct a genomic library. This may include the vendor name, kit name and kit version  (e.g. Agilent sure select Human Exome V8, Twist RefSeq Exome, etc.)
     * [LibraryPreparationProtocol➞library_preparation_kit_retail_name](LibraryPreparationProtocol_library_preparation_kit_retail_name.md)
 * [library_preparation_protocol](library_preparation_protocol.md) - The library_preparation Protocol associated with an entity.
     * [SequencingExperiment➞library_preparation_protocol](SequencingExperiment_library_preparation_protocol.md)
 * [library_preparation_protocols](library_preparation_protocols.md) - The library_preparation Protocol associated with an entity.
     * [Submission➞library_preparation_protocols](Submission_library_preparation_protocols.md) - One or more library preparation protocol entities associated with this Submission.
 * [library_selection](library_selection.md) - Whether any method was used to select for or against, enrich, or screen the material being sequenced. library_selection method (e.g. random, PCA, cDNA, etc )
     * [LibraryPreparationProtocol➞library_selection](LibraryPreparationProtocol_library_selection.md)
 * [library_type](library_type.md) - Describe the level of omics analysis (eg: Metagenome, transcriptome, etc)
     * [LibraryPreparationProtocol➞library_type](LibraryPreparationProtocol_library_type.md)
 * [main_contact](main_contact.md) - The person who is the main contact for a committee.
     * [DataAccessCommittee➞main_contact](DataAccessCommittee_main_contact.md) - The main contact for the Data Access Committee.
 * [members](members.md) - The members associated with a committee.
     * [DataAccessCommittee➞members](DataAccessCommittee_members.md) - All the members that are part of this Data Access Committee.
     * [Submission➞members](Submission_members.md) - The members associated with a committee referenced in this submission
 * [mutant_or_wildtype](mutant_or_wildtype.md) - Whether a condition corresponds to a mutant or a wildtype.
     * [Condition➞mutant_or_wildtype](Condition_mutant_or_wildtype.md)
 * [name](name.md) - The name for an entity.
     * [Biospecimen➞name](Biospecimen_name.md)
     * [Committee➞name](Committee_name.md)
     * [Condition➞name](Condition_name.md)
     * [DataAccessCommittee➞name](DataAccessCommittee_name.md) - The name for the Data Access Committee.
     * [DataAccessPolicy➞name](DataAccessPolicy_name.md) - A name for the Data Access Policy.
     * [File➞name](File_name.md) - The given filename.
     * [Population➞name](Population_name.md)
     * [Protocol➞name](Protocol_name.md) - Name of the Protocol (eg: Sample extraction_PCR amplification).
     * [Sample➞name](Sample_name.md) - Name of the sample (eg:GHGAS_Blood_Sample1 or GHGAS_PBMC_RNAseq_S1).
     * [SequencingProcess➞name](SequencingProcess_name.md)
 * [ontology_name](ontology_name.md) - The name of the ontology from which this ontology class was chosen.
     * [OntologyClassMixin➞ontology_name](OntologyClassMixin_ontology_name.md) - The name or label (rdfs:label) of an ontology class.
 * [ontology_version](ontology_version.md) - The version of the ontology from which this ontology class was chosen.
     * [OntologyClassMixin➞ontology_version](OntologyClassMixin_ontology_version.md)
 * [organization](organization.md) - The organization associated with a person.
     * [Member➞organization](Member_organization.md) - The organization that the Member is part of.
 * [outputs](outputs.md) - The outputs of a Planned Process entity.
 * [parents](parents.md) - One or more parent for an Individual.
     * [Individual➞parents](Individual_parents.md)
 * [phenotypic_features](phenotypic_features.md) - Phenotypic feature concepts that the entity is associated with.
     * [Individual➞phenotypic_features](Individual_phenotypic_features.md) - The Phenotypic Feature entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Human Phenotype Ontology. For example, 'HP:0100244' indicates that the Individual - from_which_the_Biospecimen was extracted from - exhibits_'Fibrosarcoma'_as_one_of_its_phenotype.
 * [policy_text](policy_text.md) - The complete text for the Data Access Policy.
     * [DataAccessPolicy➞policy_text](DataAccessPolicy_policy_text.md) - The terms of data use and policy verbiage should be captured here.
 * [policy_url](policy_url.md) - Alternative to pasting the Data Access Policy text.
     * [DataAccessPolicy➞policy_url](DataAccessPolicy_policy_url.md) - URL for the policy, if available. This is useful if the terms of the policy is made available online at a resolvable URL.
 * [primer](primer.md) - The type of primer used for reverse transcription, e.g. 'oligo-dT' or 'random' primer. This allows users to identify content of the cDNA library input e.g. enriched for mRNA.
     * [LibraryPreparationProtocol➞primer](LibraryPreparationProtocol_primer.md)
 * [protocol](protocol.md) - The protocol associated with an entity.
 * [publications](publications.md) - The Publication associated with an entity.
     * [Submission➞publications](Submission_publications.md) - One or more Publication entities associated with this Submission.
 * [reference_chromosome](reference_chromosome.md) - The reference chromosome used for this Analysis.
     * [Analysis➞reference_chromosome](Analysis_reference_chromosome.md)
 * [reference_genome](reference_genome.md) - A published genetic sequence that is used as a reference sequence against which other sequences are compared. Reference genome(s) or annotation(s) used for prior analyses (eg: GRCh38.p13).
     * [Analysis➞reference_genome](Analysis_reference_genome.md)
 * [rnaseq_strandedness](rnaseq_strandedness.md) - The strandedness of the library, whether reads come from both strands of the cDNA or only from the first (antisense) or the second (sense) strand.
     * [LibraryPreparationProtocol➞rnaseq_strandedness](LibraryPreparationProtocol_rnaseq_strandedness.md)
 * [sample](sample.md) - The sample associated with an entity.
     * [SampleFile➞sample](SampleFile_sample.md)
     * [SequencingProcess➞sample](SequencingProcess_sample.md)
 * [sample_barcode_read](sample_barcode_read.md) - The type of read that contains the sample barcode (eg: index1/index2/read1/read2).
     * [SequencingProtocol➞sample_barcode_read](SequencingProtocol_sample_barcode_read.md)
 * [sample_files](sample_files.md) - The SampleFiles associated with an entity.
     * [Submission➞sample_files](Submission_sample_files.md) - The SampleFiles that are part of this submission.
 * [samples](samples.md) - The samples associated with an entity.
     * [Submission➞samples](Submission_samples.md) - Information about one or more Sample entities associated with this submission.
 * [sequencing_center](sequencing_center.md) - Center where sample was sequenced.
     * [SequencingProtocol➞sequencing_center](SequencingProtocol_sequencing_center.md)
 * [sequencing_experiment](sequencing_experiment.md) - The sequencing experiment associated with an entity.
     * [SequencingProcess➞sequencing_experiment](SequencingProcess_sequencing_experiment.md)
 * [sequencing_experiments](sequencing_experiments.md) - The sequencing experiments associated with an entity.
     * [Submission➞sequencing_experiments](Submission_sequencing_experiments.md) - Information about one or more Experiment entities associated with this submission.
 * [sequencing_lane_id](sequencing_lane_id.md) - The identifier of a sequencing lane.
     * [SequencingProcess➞sequencing_lane_id](SequencingProcess_sequencing_lane_id.md) - Identifier of the sequencing lane. Used for batch correction.
 * [sequencing_machine_id](sequencing_machine_id.md) - The identifier of a sequencing machine.
     * [SequencingProcess➞sequencing_machine_id](SequencingProcess_sequencing_machine_id.md) - Identifier of the sequencing machine. Used for batch correction.
 * [sequencing_process](sequencing_process.md) - The SequencingProcess associated with an entity.
     * [SequencingProcessFile➞sequencing_process](SequencingProcessFile_sequencing_process.md)
 * [sequencing_process_files](sequencing_process_files.md) - The SequencingProcessFiles associated with an entity.
     * [AnalysisProcess➞sequencing_process_files](AnalysisProcess_sequencing_process_files.md)
     * [Submission➞sequencing_process_files](Submission_sequencing_process_files.md) - The SequencingProcessFiles that are part of this submission.
 * [sequencing_protocol](sequencing_protocol.md) - The sequencing protocol associated with an entity.
     * [SequencingExperiment➞sequencing_protocol](SequencingExperiment_sequencing_protocol.md)
 * [sequencing_protocols](sequencing_protocols.md) - The sequencing protocol associated with an entity.
     * [Submission➞sequencing_protocols](Submission_sequencing_protocols.md) - One or more sequencing protocol entities associated with this Submission.
 * [sequencing_read_length](sequencing_read_length.md) - Length of sequencing reads (eg: Long or short or actual number of the read length etc). The number of nucleotides successfully ordered from each side of a nucleic acid fragment obtained after the completion of a sequencing process
     * [SequencingProtocol➞sequencing_read_length](SequencingProtocol_sequencing_read_length.md)
 * [sequencing_run_id](sequencing_run_id.md) - The identifier of a sequencing run.
     * [SequencingProcess➞sequencing_run_id](SequencingProcess_sequencing_run_id.md) - Identifier of the sequencing run. Used for batch correction.
 * [sex](sex.md) - The assemblage of physical properties or qualities by which male is distinguished from female; the physical difference between male and female; the distinguishing peculiarity of male or female.
     * [Individual➞sex](Individual_sex.md)
 * [size](size.md) - The size of a file in bytes.
     * [File➞size](File_size.md)
 * [storage](storage.md) - Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).
     * [Biospecimen➞storage](Biospecimen_storage.md)
     * [Sample➞storage](Sample_storage.md)
 * [studies](studies.md) - The study associated with an entity.
     * [Submission➞studies](Submission_studies.md) - Information about a Study entities associated with this submission.
 * [study](study.md) - The study associated with an entity.
     * [Analysis➞study](Analysis_study.md) - The Study entity associated with this Analysis.
     * [Publication➞study](Publication_study.md) - The Study entity associated with this Publication.
     * [StudyFile➞study](StudyFile_study.md)
 * [study_files](study_files.md) - The StudyFiles associated with an entity.
     * [Submission➞study_files](Submission_study_files.md) - The StudyFiles that are part of this submission.
 * [submission_date](submission_date.md) - The timestamp (in ISO 8601 format) when submission was marked completed.
 * [submission_status](submission_status.md) - The status of a submission.
 * [target_coverage](target_coverage.md) - Mean coverage for whole genome sequencing, or mean target coverage for whole exome and targeted sequencing. The number of times a particular locus (site, nucleotide, amplicon, region) was sequenced.
     * [SequencingProtocol➞target_coverage](SequencingProtocol_target_coverage.md)
 * [target_regions](target_regions.md) - Subset of genes or specific regions of the genome, which are most likely to be involved in the phenotype under study.
     * [LibraryPreparationProtocol➞target_regions](LibraryPreparationProtocol_target_regions.md)
 * [technical_replicates](technical_replicates.md) - A technical replicate is a replicate role where the same BioSample is use e.g. the same pool of RNA used to assess technical (as opposed to biological) variation within an sequencing experiment.
 * [telephone](telephone.md) - The telephone number associated with a person.
     * [Member➞telephone](Member_telephone.md) - The telephone number of the Member.
 * [title](title.md) - The title that describes an entity.
     * [Dataset➞title](Dataset_title.md) - A title for the submitted Dataset.
     * [Publication➞title](Publication_title.md) - The title for the Publication.
     * [ResearchActivity➞title](ResearchActivity_title.md)
     * [SequencingExperiment➞title](SequencingExperiment_title.md) - Name for the experiment (eg: GHGAE_PBMC_RNAseq).
     * [Study➞title](Study_title.md) - A comprehensive title for the study.
 * [treatment_or_control](treatment_or_control.md) - Whether a condition corresponds to a treatment or a control.
     * [Condition➞treatment_or_control](Condition_treatment_or_control.md)
 * [type](type.md) - The type of an entity. Note: Not to be confused with rdf:type
     * [Analysis➞type](Analysis_type.md) - The type of the Analysis. Either Reference Alignment (BAM) or Sequence Variation (VCF)
     * [Biospecimen➞type](Biospecimen_type.md) - The type of Biospecimen.
     * [Protocol➞type](Protocol_type.md) - Type of the protocol (eg: Target enrichment).
     * [Sample➞type](Sample_type.md) - The type of sample.
     * [SequencingExperiment➞type](SequencingExperiment_type.md) - The type of sequencing experiment.
     * [SequencingProtocol➞type](SequencingProtocol_type.md) - Name of the library_preparation Protocol (eg: mRNA-seq,Whole exome long-read sequencing etc).
     * [Study➞type](Study_type.md) - The type of Study. For example, 'Cancer Genomics', 'Epigenetics', 'Exome Sequencing'.
 * [types](types.md) - The types of an entity. Note: Not to be confused with rdf:type
     * [Dataset➞types](Dataset_types.md) - The type of a dataset.
 * [umi_barcode_offset](umi_barcode_offset.md) - The offset in sequence of the UMI identifying barcode. (E.g. '16').
     * [SequencingProtocol➞umi_barcode_offset](SequencingProtocol_umi_barcode_offset.md)
 * [umi_barcode_read](umi_barcode_read.md) - The type of read that contains the UMI barcode (Eg: index1/index2/read1/read2).
     * [SequencingProtocol➞umi_barcode_read](SequencingProtocol_umi_barcode_read.md)
 * [umi_barcode_size](umi_barcode_size.md) - The size of the UMI identifying barcode (Eg. '10').
     * [SequencingProtocol➞umi_barcode_size](SequencingProtocol_umi_barcode_size.md)
 * [url](url.md) - A URL to a resource.
     * [Protocol➞url](Protocol_url.md) - URL for the resource that describes this protocol.
 * [value](value.md) - The value of an attribute
     * [Attribute➞value](Attribute_value.md) - The value for an attribute. Usually this is a numerical value (without the units).
 * [value_type](value_type.md) - The semantic type for the value of an attribute.
     * [Attribute➞value_type](Attribute_value_type.md) - The value_type that characterizes the attribute value. Usually this is a term from an ontology that describes how to interpret the value. For example, 'SIO:001413' indicates that the value is to be interpreted as a percentage.
 * [vital_status](vital_status.md) - The state or condition of being living or deceased; also includes the case where the vital status is unknown.
     * [Individual➞vital_status](Individual_vital_status.md) - Last known Vital Status of an Individual.
 * [vital_status_at_sampling](vital_status_at_sampling.md) - Vital Status of an Individual at the point of sampling (eg:'Alive', 'Deceased').
     * [Biospecimen➞vital_status_at_sampling](Biospecimen_vital_status_at_sampling.md)
 * [xref](xref.md) - Database cross references for an entity.
     * [Protocol➞xref](Protocol_xref.md) - One or more cross-references for this protocol.  (Eg: manufacturer protocol, protocol from publication etc )
     * [Publication➞xref](Publication_xref.md) - One or more cross-references for this Publication.
     * [Sample➞xref](Sample_xref.md) - One or more cross-references for this Sample. For example, this Sample may have an EBI BioSamples accession or an EGA Sample accession.
 * [year](year.md) - Year in which the paper was published.
     * [Publication➞year](Publication_year.md)

### Enums

 * [AgeRangeEnum](AgeRangeEnum.md) - Enum to capture the age range that an Indiviudal belongs to.
 * [BiologicalSexEnum](BiologicalSexEnum.md) - The biological sex of an Individual as determined by their chromosomes.
 * [DiseaseOrHealthyEnum](DiseaseOrHealthyEnum.md) - Enum to capture whether a condition corresponds to a disease or a healthy state.
 * [FileFormatEnum](FileFormatEnum.md) - Enum to capture file types.
 * [ForwardOrReverseEnum](ForwardOrReverseEnum.md) - Enum to capture whether the reads from paired-end sequencing are forward (R1) or reverse (R2).
 * [MutantOrWildtypeEnum](MutantOrWildtypeEnum.md) - Enum to capture whether a condition corresponds to a mutant or a wildtype.
 * [StudyTypeEnum](StudyTypeEnum.md) - Enum to capture the type of a study.
 * [TreatmentOrControlEnum](TreatmentOrControlEnum.md) - Enum to capture whether a condition corresponds to a treatment or a control.
 * [VitalStatusEnum](VitalStatusEnum.md) - Enum to capture the vital status of an individual.

### Subsets

 * [Restricted](Restricted.md) - Subset of properties that are considered to be restricted.

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
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
