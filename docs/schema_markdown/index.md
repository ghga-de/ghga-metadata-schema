
# GHGA-Submission-Metadata-Schema


**metamodel version:** 1.7.0

**version:** 0.9.0


The submission centric metadata schema for the German Human Genome-Phenome Archive (GHGA).


### Classes

 * [Attribute](Attribute.md) - A key/value pair that further characterizes an entity.
 * [NamedThing](NamedThing.md) - A database entity, concept or class. This is a generic class that is the root of all the other classes.
     * [BiologicalQuality](BiologicalQuality.md) - A biological quality is a quality held by a biological entity.
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
         * [Protocol](Protocol.md) - A plan specification which has sufficient level of detail and quantitative information to communicate it between investigation agents, so that different investigation agents will reliably be able to independently reproduce the process.
             * [LibraryPreparationProtocol](LibraryPreparationProtocol.md) - Information about the library preparation of an sequencing experiment.
             * [SequencingProtocol](SequencingProtocol.md) - Information about the sequencing of a sample.
         * [Publication](Publication.md) - The Publication entity represents a publication. While a publication can be any article that is published, the minimum expectation is that the publication has a valid DOI.
     * [MaterialEntity](MaterialEntity.md) - A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.
         * [AnatomicalEntity](AnatomicalEntity.md) - Biological entity that is either an individual member of a biological species or constitutes the structural organization of an individual member of a biological species.
         * [Biospecimen](Biospecimen.md) - A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics, treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is derived.
         * [Population](Population.md) - A population is a collection of individuals from the same taxonomic class living, counted or sampled at a particular site or in a particular area.
             * [Ancestry](Ancestry.md) - Population category defined using ancestry informative markers (AIMs) based on genetic/genomic data.
         * [Sample](Sample.md) - A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).
     * [Person](Person.md) - A member of the species Homo sapiens.
         * [Individual](Individual.md) - An Individual is a Person who is participating in a Study.
         * [Member](Member.md) - Member of an Organization or a Committee.
     * [PlannedProcess](PlannedProcess.md) - A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and depends on some entity during the time it occurs.
         * [DataTransformation](DataTransformation.md) - A data transformation technique used to analyze and interpret data to gain a better understanding of it.
             * [Analysis](Analysis.md) - An Analysis is a data transformation that transforms input data to output data. The workflow used to achieve this transformation and the individual steps are also captured.
         * [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.
             * [Condition](Condition.md) - An condition that is linked to comparable samples.
             * [SequencingExperiment](SequencingExperiment.md) - An sequencing experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
             * [SequencingProcess](SequencingProcess.md) - A sequencing process linking a sample to sequencing output.
             * [Study](Study.md) - Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.
         * [ResearchActivity](ResearchActivity.md) - A planned process executed in the performance of scientific research wherein systematic investigations are performed to establish facts and reach new conclusions about phenomena in the world.
             * [Project](Project.md) - A high level organization for a collection of studies based on a research proposal that aims to achieve certain goals.
 * [Submission](Submission.md) - A grouping entity that represents information about one or more entities. A submission can be considered as a set of inter-related (and inter-connected) entities that represent a data submission to GHGA.

### Mixins

 * [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 * [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.
 * [DeprecatedMixin](DeprecatedMixin.md) - Mixin for entities that can be deprecated.
 * [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an EGA accession, in addition to GHGA accession.
 * [OntologyClassMixin](OntologyClassMixin.md) - Mixin for entities that represent an class/term/concept from an ontology.
 * [PublicationMixin](PublicationMixin.md) - Mixin for entities that can have one or more publications.

### Slots

 * [abstract](abstract.md) - The study abstract that describes the goals.  Can also hold abstract from a publication related to this study
     * [publication➞abstract](publication_abstract.md) - The study abstract that describes the goals. Can also hold abstract from a publication related to this study.
 * [accession](accession.md) - A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * [accession mixin➞accession](accession_mixin_accession.md)
 * [additional name](additional_name.md) - Additional name(s).
     * [person➞additional name](person_additional_name.md)
 * [affiliation](affiliation.md) - The Institution(s) associated with an entity.
     * [study➞affiliation](study_affiliation.md)
     * [submission➞affiliation](submission_affiliation.md) - Institution/Center/Data Hub that is providing this submission.
 * [age](age.md) - Age of an individual.
     * [individual➞age](individual_age.md)
 * [alias](alias.md) - The alias for an entity.
     * [analysis➞alias](analysis_alias.md) - An alias uniquely identifying this Analysis entitiy.
     * [library preparation protocol➞alias](library_preparation_protocol_alias.md)
     * [named thing➞alias](named_thing_alias.md) - The alias (alternate identifier) for an entity.
         * [protocol➞alias](protocol_alias.md) - The alias for an entity.
     * [sequencing protocol➞alias](sequencing_protocol_alias.md)
 * [author](author.md) - The individual who is responsible for the content of a document version.
     * [publication➞author](publication_author.md)
 * [biological replicates](biological_replicates.md) - A biological replicate is a replicate role that consists of independent biological replicates made from different individual biosamples.
 * [category](category.md) - The category for this file: Whole Genome Sequencing, Whole Exome Sequencing, etc.
 * [cell barcode offset](cell_barcode_offset.md) - The offset in sequence of the cell identifying barcode. (Eg. '0').
     * [sequencing protocol➞cell barcode offset](sequencing_protocol_cell_barcode_offset.md)
 * [cell barcode read](cell_barcode_read.md) - The type of read that contains the cell barcode (eg: index1/index2/read1/read2).
     * [sequencing protocol➞cell barcode read](sequencing_protocol_cell_barcode_read.md)
 * [cell barcode size](cell_barcode_size.md) - The size of the cell identifying barcode (E.g. '16').
     * [sequencing protocol➞cell barcode size](sequencing_protocol_cell_barcode_size.md)
 * [checksum](checksum.md) - A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data. The receiving system recomputes the checksum based upon the received data and compares this value with the one sent with the data. If the two values are the same, the receiver has some confidence that the data was received correctly.
     * [file➞checksum](file_checksum.md)
 * [checksum type](checksum_type.md) - The type of algorithm used to generate the checksum of a file.
     * [file➞checksum type](file_checksum_type.md)
 * [concept identifier](concept_identifier.md) - The Compact URI (CURIE) that uniquely identifies a concept from an ontology, thesaurus, or terminology.
     * [ontology class mixin➞concept identifier](ontology_class_mixin_concept_identifier.md) - The Compact URI (CURIE) that uniquely identifies this ontology class.
 * [concept name](concept_name.md) - The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.
     * [ontology class mixin➞concept name](ontology_class_mixin_concept_name.md)
 * [data request form](data_request_form.md) - Data Request Form that is associated with a Data Access Policy.
     * [data access policy➞data request form](data_access_policy_data_request_form.md) - Data Request Form that is associated with this Data Access Policy.
 * [deprecation date](deprecation_date.md) - The timestamp (in ISO 8601 format) when the entity was deprecated.
     * [deprecated mixin➞deprecation date](deprecated_mixin_deprecation_date.md)
 * [description](description.md) - Description of an entity.
     * [analysis➞description](analysis_description.md) - Describing how an Analysis was carried out. (e.g.: computational tools, settings, etc.).
     * [biospecimen➞description](biospecimen_description.md)
     * [condition➞description](condition_description.md)
     * [data access committee➞description](data_access_committee_description.md) - A description for the Data Access Committee.
     * [data access policy➞description](data_access_policy_description.md) - A short description for the Data Access Policy.
     * [dataset➞description](dataset_description.md)
     * [library preparation protocol➞description](library_preparation_protocol_description.md) - Description about how a sequencing library was prepared (eg: Library construction method).
     * [ontology class mixin➞description](ontology_class_mixin_description.md) - The description or definition of an ontology class.
     * [project➞description](project_description.md) - Short textual description of the project.
     * [protocol➞description](protocol_description.md) - Detailed description of the Protocol.
     * [research activity➞description](research_activity_description.md)
     * [sample➞description](sample_description.md) - Short textual description of the sample (How the sample was collected, sample source, protocol followed for processing the sample etc).
     * [sequencing experiment➞description](sequencing_experiment_description.md) - A detailed description of the Experiment.
     * [sequencing process➞description](sequencing_process_description.md)
     * [sequencing protocol➞description](sequencing_protocol_description.md) - Description about the sequencing protocol (eg: mRNA-seq,Whole exome long-read sequencing etc).
     * [study➞description](study_description.md) - A detailed description (abstract) that describes the goals of this Study.
 * [disease or healthy](disease_or_healthy.md) - Whether a condition corresponds to a disease or a healthy state.
     * [condition➞disease or healthy](condition_disease_or_healthy.md)
 * [doi](doi.md) - DOI identifier of a publication.
     * [publication➞doi](publication_doi.md) - DOI identifier of the Publication.
 * [ega accession](ega_accession.md) - A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
     * [ega accession mixin➞ega accession](ega_accession_mixin_ega_accession.md)
 * [email](email.md) - Email of a person.
     * [member➞email](member_email.md) - The email of the Member.
 * [end bias](end_bias.md) - The end of the cDNA molecule that is preferentially sequenced, e.g. 3/5 prime tag or end, or the full-length transcript.
     * [library preparation protocol➞end bias](library_preparation_protocol_end_bias.md)
 * [family name](family_name.md) - Last name.
     * [person➞family name](person_family_name.md)
 * [flow cell id](flow_cell_id.md) - Flow Cell ID (eg: Experiment ID_Cell 1_Lane_1). The barcode assigned to a flow cell used in nucleotide sequencing.
     * [sequencing protocol➞flow cell id](sequencing_protocol_flow_cell_id.md)
 * [flow cell type](flow_cell_type.md) - Type of flow cell used (e.g. S4, S2 for NovaSeq; PromethION, Flongle for Nanopore). Aparatus in the fluidic subsystem where the sheath and sample meet. Can be one of several types; jet-in-air, quartz cuvette, or a hybrid of the two. The sample flows through the center of a fluid column of sheath fluid in the flow cell.
     * [sequencing protocol➞flow cell type](sequencing_protocol_flow_cell_type.md)
 * [format](format.md) - The format of the file: BAM, SAM, CRAM, BAI, etc.
     * [file➞format](file_format.md)
 * [forward or reverse](forward_or_reverse.md) - Denotes whether a submitted FASTQ file contains forward (R1) or reverse (R2) reads for paired-end sequencing. The number that identifies each read direction in a paired-end nucleotide sequencing reaction.
     * [sequencing protocol➞forward or reverse](sequencing_protocol_forward_or_reverse.md)
 * [geographical region](geographical_region.md) - The geographical region where the Individual is located. Any demarcated area of the Earth; may be determined by both natural and human boundaries.
     * [individual➞geographical region](individual_geographical_region.md)
 * [given name](given_name.md) - First name.
     * [person➞given name](person_given_name.md)
 * [has analysis](has_analysis.md) - The analysis associated with an entity.
     * [submission➞has analysis](submission_has_analysis.md) - Information about one or more Analysis entities associated with this submission.
 * [has anatomical entity](has_anatomical_entity.md) - Anatomical site associated with an entity.
     * [biospecimen➞has anatomical entity](biospecimen_has_anatomical_entity.md)
 * [has ancestry](has_ancestry.md) - A person's descent or lineage, from a person or from a population. Typically this is a value from HANCESTRO (Human Ancestry Ontology).
     * [individual➞has ancestry](individual_has_ancestry.md)
 * [has attribute](has_attribute.md) - Key/value pairs corresponding to an entity.
     * [library preparation protocol➞has attribute](library_preparation_protocol_has_attribute.md) - One or more attributes that further characterizes this Library Preparation Protocol.
     * [project➞has attribute](project_has_attribute.md) - Custom attributes for the Project  (eg: Cancer - Colon cancer, prostrate cancer, blood cancer etc)
     * [protocol➞has attribute](protocol_has_attribute.md) - One or more attributes that further characterizes this Protocol.
     * [sequencing protocol➞has attribute](sequencing_protocol_has_attribute.md) - One or more attributes that further characterizes this Sequencing Protocol.
     * [study➞has attribute](study_has_attribute.md) - Custom key/value pairs that further characterizes the Study. (e.g.: approaches - single-cell, bulk etc)
 * [has biospecimen](has_biospecimen.md) - The biospecimen associated with an entity.
     * [sample➞has biospecimen](sample_has_biospecimen.md) - The Biospecimen from which this Sample was prepared from.
     * [submission➞has biospecimen](submission_has_biospecimen.md) - Information about one or more Biospecimen entities associated with this submission.
 * [has children](has_children.md) - The children of an entity.
     * [individual➞has children](individual_has_children.md) - One or more children for this Individual.
 * [has condition](has_condition.md) - The condition associated with an entity.
     * [sample➞has condition](sample_has_condition.md)
     * [study➞has condition](study_has_condition.md)
 * [has data access committee](has_data_access_committee.md) - Data Access Committee associated with an entity.
     * [data access policy➞has data access committee](data_access_policy_has_data_access_committee.md) - The Data Access Committee linked to this policy.
     * [submission➞has data access committee](submission_has_data_access_committee.md) - The Data Access Committee that applies to Dataset in this submission.
 * [has data access policy](has_data_access_policy.md) - Data Access Policy associated with an entity.
     * [dataset➞has data access policy](dataset_has_data_access_policy.md) - The Data Access Policy that applies to this Dataset.
     * [submission➞has data access policy](submission_has_data_access_policy.md) - The Data Access Policy that applies to Dataset in this submission.
 * [has data use modifier](has_data_use_modifier.md) - Modifier for Data use permission associated with an entity. Should be descendants of 'DUO:0000017 data use modifier'
     * [data access policy➞has data use modifier](data_access_policy_has_data_use_modifier.md) - Modifier for Data use permission associated with a policy. Should be descendants of 'DUO:0000017 data use modifier'
 * [has data use permission](has_data_use_permission.md) - Data use permission associated with an entity. Typically one or more terms from DUO. Should be descendants of 'DUO:0000001 data use permission'.
     * [data access policy➞has data use permission](data_access_policy_has_data_use_permission.md) - Data use permission associated with a policy. Typically one or more terms from DUO and should be descendants of 'DUO:0000001 data use permission'.
 * [has dataset](has_dataset.md) - The Dataset associated with an entity.
     * [submission➞has dataset](submission_has_dataset.md) - One or more Dataset that are part of this submission.
 * [has disease](has_disease.md) - Disease concept that the entity is associated with.
     * [individual➞has disease](individual_has_disease.md) - The Disease entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Mondo Disease Ontology. For example, 'MONDO:0003742' indicates that the Individual - from which the Biospecimen was extracted from - suffers from 'Heart Fibrosarcoma'.
 * [has file](has_file.md) - The file associated with an entity.
     * [dataset➞has file](dataset_has_file.md) - One or more File entities that collectively are part of this Dataset.
     * [individual➞has file](individual_has_file.md) - Additional/supplementary files associated with an Individual. Typically, a phenopacket or pedigree file.
     * [sequencing process➞has file](sequencing_process_has_file.md)
     * [submission➞has file](submission_has_file.md) - Information about one or more File entities associated with this submission.
 * [has individual](has_individual.md) - The subject/individual associated with an entity.
     * [biospecimen➞has individual](biospecimen_has_individual.md) - The Individual entity from which this Biospecimen was derived.
     * [submission➞has individual](submission_has_individual.md) - Information about one or more Individual entities associated with this submission.
 * [has input](has_input.md) - The input to a Planned Process.
     * [analysis➞has input](analysis_has_input.md) - The input data File entities used in the Analysis.
 * [has library preparation protocol](has_library_preparation_protocol.md) - The Library Preparation Protocol associated with an entity.
     * [sequencing experiment➞has library preparation protocol](sequencing_experiment_has_library_preparation_protocol.md)
 * [has member](has_member.md) - The members associated with a committee.
     * [data access committee➞has member](data_access_committee_has_member.md) - All the members that are part of this Data Access Committee.
     * [submission➞has member](submission_has_member.md) - The members associated with a committee referenced in this submission
 * [has output](has_output.md) - The output of a Planned Process entity.
     * [analysis➞has output](analysis_has_output.md) - The output data File entities generated by this Analysis.
 * [has parent](has_parent.md) - The parent of an entity.
     * [individual➞has parent](individual_has_parent.md) - One or more parent for this Individual.
 * [has phenotypic feature](has_phenotypic_feature.md) - Phenotypic feature concept that the entity is associated with.
     * [individual➞has phenotypic feature](individual_has_phenotypic_feature.md) - The Phenotypic Feature entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Human Phenotype Ontology. For example, 'HP:0100244' indicates that the Individual - from which the Biospecimen was extracted from - exhibits 'Fibrosarcoma' as one of its phenotype.
 * [has project](has_project.md) - The project associated with an entity.
     * [study➞has project](study_has_project.md) - The project associated with this Study.
     * [submission➞has project](submission_has_project.md) - Information about a Project entity associated with this submission.
 * [has protocol](has_protocol.md) - The protocol associated with an entity.
     * [submission➞has protocol](submission_has_protocol.md) - One or more Protocol entities associated with this Submission.
 * [has publication](has_publication.md) - The Publication associated with an entity.
     * [publication mixin➞has publication](publication_mixin_has_publication.md)
     * [submission➞has publication](submission_has_publication.md) - One or more Publication entities associated with this Submission.
 * [has sample](has_sample.md) - The sample associated with an entity.
     * [sequencing process➞has sample](sequencing_process_has_sample.md)
     * [submission➞has sample](submission_has_sample.md) - Information about one or more Sample entities associated with this submission.
 * [has sequencing experiment](has_sequencing_experiment.md) - The sequencing experiment associated with an entity.
     * [sequencing process➞has sequencing experiment](sequencing_process_has_sequencing_experiment.md)
     * [submission➞has sequencing experiment](submission_has_sequencing_experiment.md) - Information about one or more Experiment entities associated with this submission.
 * [has sequencing protocol](has_sequencing_protocol.md) - The sequencing protocol associated with an entity.
     * [sequencing experiment➞has sequencing protocol](sequencing_experiment_has_sequencing_protocol.md)
 * [has study](has_study.md) - The study associated with an entity.
     * [analysis➞has study](analysis_has_study.md) - The Study entity associated with this Analysis.
     * [publication➞has study](publication_has_study.md) - The Study entity associated with this Publication.
     * [submission➞has study](submission_has_study.md) - Information about a Study entities associated with this submission.
 * [id](id.md) - An identifier that uniquely represents an entity.
     * [named thing➞id](named_thing_id.md) - The internal unique identifier for an entity.
     * [ontology class mixin➞id](ontology_class_mixin_id.md)
     * [submission➞id](submission_id.md) - A internal unique identifier for the Submission.
 * [index sequence](index_sequence.md) - A unique nucleotide sequence that is added to a sample during library preparation to serve as a unique identifier for the sample.
     * [sequencing protocol➞index sequence](sequencing_protocol_index_sequence.md)
 * [instrument model](instrument_model.md) - The name and model of the technology platform used to perform sequencing.
     * [sequencing protocol➞instrument model](sequencing_protocol_instrument_model.md)
 * [isolation](isolation.md) - Method or device employed for collecting/isolating a biospecimen or a sample.
     * [biospecimen➞isolation](biospecimen_isolation.md)
 * [journal](journal.md) - Name of the journal.
     * [publication➞journal](publication_journal.md)
 * [karyotype](karyotype.md) - The karyotype of an individual if defined.
     * [individual➞karyotype](individual_karyotype.md)
 * [key](key.md) - The key of an attribute.
     * [attribute➞key](attribute_key.md) - The key for an attribute.
 * [key type](key_type.md) - The semantic type for the key of an attribute.
     * [attribute➞key type](attribute_key_type.md) - A semantic type that characterizes the attribute key. Usually this is a term from an ontology. For example, 'MAXO:0000616' indicates that the attribute is a measurement of oxygen saturation in the blood.
 * [lane number](lane_number.md) - The numerical identifier for the lane or machine unit where a sample was located during nucleotide sequencing.
     * [sequencing protocol➞lane number](sequencing_protocol_lane_number.md)
 * [library layout](library_layout.md) - Describe whether the library was sequenced in single-end (forward or reverse) or paired-end mode
     * [library preparation protocol➞library layout](library_preparation_protocol_library_layout.md)
 * [library name](library_name.md) - A short name identifying the library to potential users. The same name may refer to multiple versions of the same continually updated library.
     * [library preparation protocol➞library name](library_preparation_protocol_library_name.md)
 * [library preparation](library_preparation.md) - The general method for sequencing library preparation (e.g. KAPA PCR-free).
     * [library preparation protocol➞library preparation](library_preparation_protocol_library_preparation.md)
 * [library preparation kit manufacturer](library_preparation_kit_manufacturer.md) - Manufacturer of library preparation kit
     * [library preparation protocol➞library preparation kit manufacturer](library_preparation_protocol_library_preparation_kit_manufacturer.md)
 * [library preparation kit retail name](library_preparation_kit_retail_name.md) - A unique identifier for the kit used to construct a genomic library. This may include the vendor name, kit name and kit version  (e.g. Agilent sure select Human Exome V8, Twist RefSeq Exome, etc.)
     * [library preparation protocol➞library preparation kit retail name](library_preparation_protocol_library_preparation_kit_retail_name.md)
 * [library selection](library_selection.md) - Whether any method was used to select for or against, enrich, or screen the material being sequenced. Library Selection method (e.g. random, PCA, cDNA, etc )
     * [library preparation protocol➞library selection](library_preparation_protocol_library_selection.md)
 * [library type](library_type.md) - Describe the level of omics analysis (eg: Metagenome, transcriptome, etc)
     * [library preparation protocol➞library type](library_preparation_protocol_library_type.md)
 * [main contact](main_contact.md) - The person who is the main contact for a committee.
     * [data access committee➞main contact](data_access_committee_main_contact.md) - The main contact for the Data Access Committee.
 * [mutant or wildtype](mutant_or_wildtype.md) - Whether a condition corresponds to a mutant or a wildtype.
     * [condition➞mutant or wildtype](condition_mutant_or_wildtype.md)
 * [name](name.md) - The name for an entity.
     * [biospecimen➞name](biospecimen_name.md)
     * [committee➞name](committee_name.md)
     * [condition➞name](condition_name.md)
     * [data access committee➞name](data_access_committee_name.md) - The name for the Data Access Committee.
     * [data access policy➞name](data_access_policy_name.md) - A name for the Data Access Policy.
     * [file➞name](file_name.md) - The given filename.
     * [population➞name](population_name.md)
     * [protocol➞name](protocol_name.md) - Name of the protocol (eg: Sample extraction_PCR amplification).
     * [sample➞name](sample_name.md) - Name of the sample (eg:GHGAS_Blood_Sample1 or GHGAS_PBMC_RNAseq_S1).
     * [sequencing process➞name](sequencing_process_name.md)
 * [ontology name](ontology_name.md) - The name of the ontology from which this ontology class was chosen.
     * [ontology class mixin➞ontology name](ontology_class_mixin_ontology_name.md) - The name or label (rdfs:label) of an ontology class.
 * [ontology version](ontology_version.md) - The version of the ontology from which this ontology class was chosen.
     * [ontology class mixin➞ontology version](ontology_class_mixin_ontology_version.md)
 * [organization](organization.md) - The organization associated with a person.
     * [member➞organization](member_organization.md) - The organization that the Member is part of.
 * [policy text](policy_text.md) - The complete text for the Data Access Policy.
     * [data access policy➞policy text](data_access_policy_policy_text.md) - The terms of data use and policy verbiage should be captured here.
 * [policy url](policy_url.md) - Alternative to pasting the Data Access Policy text.
     * [data access policy➞policy url](data_access_policy_policy_url.md) - URL for the policy, if available. This is useful if the terms of the policy is made available online at a resolvable URL.
 * [primer](primer.md) - The type of primer used for reverse transcription, e.g. 'oligo-dT' or 'random' primer. This allows users to identify content of the cDNA library input e.g. enriched for mRNA.
     * [library preparation protocol➞primer](library_preparation_protocol_primer.md)
 * [reference chromosome](reference_chromosome.md) - The reference chromosome used for this Analysis.
     * [analysis➞reference chromosome](analysis_reference_chromosome.md)
 * [reference genome](reference_genome.md) - A published genetic sequence that is used as a reference sequence against which other sequences are compared. Reference genome(s) or annotation(s) used for prior analyses (eg: GRCh38.p13).
     * [analysis➞reference genome](analysis_reference_genome.md)
 * [replaced by](replaced_by.md) - Refers to the entity which replaces a currently deprecated entity.
     * [deprecated mixin➞replaced by](deprecated_mixin_replaced_by.md)
 * [replaces](replaces.md) - Refers to a deprecated entity that is being replaced by the current entity.
 * [rnaseq strandedness](rnaseq_strandedness.md) - The strandedness of the library, whether reads come from both strands of the cDNA or only from the first (antisense) or the second (sense) strand.
     * [library preparation protocol➞rnaseq strandedness](library_preparation_protocol_rnaseq_strandedness.md)
 * [sample barcode read](sample_barcode_read.md) - The type of read that contains the sample barcode (eg: index1/index2/read1/read2).
     * [sequencing protocol➞sample barcode read](sequencing_protocol_sample_barcode_read.md)
 * [sequencing center](sequencing_center.md) - Center where sample was sequenced.
     * [sequencing protocol➞sequencing center](sequencing_protocol_sequencing_center.md)
 * [sequencing lane id](sequencing_lane_id.md) - The identifier of a sequencing lane.
     * [sequencing process➞sequencing lane id](sequencing_process_sequencing_lane_id.md) - Identifier of the sequencing lane. Used for batch correction.
 * [sequencing machine id](sequencing_machine_id.md) - The identifier of a sequencing machine.
     * [sequencing process➞sequencing machine id](sequencing_process_sequencing_machine_id.md) - Identifier of the sequencing machine. Used for batch correction.
 * [sequencing read length](sequencing_read_length.md) - Length of sequencing reads (eg: Long or short or actual number of the read length etc). The number of nucleotides successfully ordered from each side of a nucleic acid fragment obtained after the completion of a sequencing process
     * [sequencing protocol➞sequencing read length](sequencing_protocol_sequencing_read_length.md)
 * [sequencing run id](sequencing_run_id.md) - The identifier of a sequencing run.
     * [sequencing process➞sequencing run id](sequencing_process_sequencing_run_id.md) - Identifier of the sequencing run. Used for batch correction.
 * [sex](sex.md) - The assemblage of physical properties or qualities by which male is distinguished from female; the physical difference between male and female; the distinguishing peculiarity of male or female.
     * [individual➞sex](individual_sex.md)
 * [size](size.md) - The size of a file in bytes.
     * [file➞size](file_size.md)
 * [storage](storage.md) - Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).
     * [biospecimen➞storage](biospecimen_storage.md)
     * [sample➞storage](sample_storage.md)
 * [submission date](submission_date.md) - The timestamp (in ISO 8601 format) when submission was marked completed.
 * [submission status](submission_status.md) - The status of a submission.
     * [submission➞submission status](submission_submission_status.md) - The status of a Submission.
 * [target coverage](target_coverage.md) - Mean coverage for whole genome sequencing, or mean target coverage for whole exome and targeted sequencing. The number of times a particular locus (site, nucleotide, amplicon, region) was sequenced.
     * [sequencing protocol➞target coverage](sequencing_protocol_target_coverage.md)
 * [target regions](target_regions.md) - Subset of genes or specific regions of the genome, which are most likely to be involved in the phenotype under study.
     * [library preparation protocol➞target regions](library_preparation_protocol_target_regions.md)
 * [technical replicates](technical_replicates.md) - A technical replicate is a replicate role where the same BioSample is use e.g. the same pool of RNA used to assess technical (as opposed to biological) variation within an sequencing experiment.
 * [telephone](telephone.md) - The telephone number associated with a person.
     * [member➞telephone](member_telephone.md) - The telephone number of the Member.
 * [title](title.md) - The title that describes an entity.
     * [dataset➞title](dataset_title.md) - A title for the submitted Dataset.
     * [project➞title](project_title.md) - Comprehensive title for the project.
     * [publication➞title](publication_title.md) - The title for the Publication.
     * [research activity➞title](research_activity_title.md)
     * [sequencing experiment➞title](sequencing_experiment_title.md) - Name for the experiment (eg: GHGAE_PBMC_RNAseq).
     * [study➞title](study_title.md) - A comprehensive title for the study.
 * [treatment or control](treatment_or_control.md) - Whether a condition corresponds to a treatment or a control.
     * [condition➞treatment or control](condition_treatment_or_control.md)
 * [type](type.md) - The type of an entity.
     * [analysis➞type](analysis_type.md) - The type of the Analysis. Either Reference Alignment (BAM) or Sequence Variation (VCF)
     * [biospecimen➞type](biospecimen_type.md) - The type of Biospecimen.
     * [dataset➞type](dataset_type.md) - The type of a dataset.
     * [protocol➞type](protocol_type.md) - Type of the protocol (eg: Target enrichment).
     * [sample➞type](sample_type.md) - The type of sample.
     * [sequencing experiment➞type](sequencing_experiment_type.md) - The type of sequencing experiment.
     * [sequencing protocol➞type](sequencing_protocol_type.md) - Name of the library preparation protocol (eg: mRNA-seq,Whole exome long-read sequencing etc).
     * [study➞type](study_type.md) - The type of Study. For example, 'Cancer Genomics', 'Epigenetics', 'Exome Sequencing'.
 * [umi barcode offset](umi_barcode_offset.md) - The offset in sequence of the UMI identifying barcode. (E.g. '16').
     * [sequencing protocol➞umi barcode offset](sequencing_protocol_umi_barcode_offset.md)
 * [umi barcode read](umi_barcode_read.md) - The type of read that contains the UMI barcode (Eg: index1/index2/read1/read2).
     * [sequencing protocol➞umi barcode read](sequencing_protocol_umi_barcode_read.md)
 * [umi barcode size](umi_barcode_size.md) - The size of the UMI identifying barcode (Eg. '10').
     * [sequencing protocol➞umi barcode size](sequencing_protocol_umi_barcode_size.md)
 * [url](url.md) - A URL to a resource.
     * [protocol➞url](protocol_url.md) - URL for the resource that describes this Protocol.
 * [value](value.md) - The value of an attribute
     * [attribute➞value](attribute_value.md) - The value for an attribute. Usually this is a numerical value (without the units).
 * [value type](value_type.md) - The semantic type for the value of an attribute.
     * [attribute➞value type](attribute_value_type.md) - The value type that characterizes the attribute value. Usually this is a term from an ontology that describes how to interpret the value. For example, 'SIO:001413' indicates that the value is to be interpreted as a percentage.
 * [vital status](vital_status.md) - The state or condition of being living or deceased; also includes the case where the vital status is unknown.
     * [individual➞vital status](individual_vital_status.md) - Last known Vital Status of an Individual.
 * [vital status at sampling](vital_status_at_sampling.md) - Vital Status of an Individual at the point of sampling (eg:'Alive', 'Deceased').
     * [biospecimen➞vital status at sampling](biospecimen_vital_status_at_sampling.md)
 * [xref](xref.md) - Database cross references for an entity.
     * [named thing➞xref](named_thing_xref.md) - Holds one or more database cross references for an entity.
         * [protocol➞xref](protocol_xref.md) - One or more cross-references for this Protocol.  (Eg: manufacturer protocol, protocol from publication etc )
     * [publication➞xref](publication_xref.md) - One or more cross-references for this Publication.
     * [sample➞xref](sample_xref.md) - One or more cross-references for this Sample. For example, this Sample may have an EBI BioSamples accession or an EGA Sample accession.
 * [year](year.md) - Year in which the paper was published.
     * [publication➞year](publication_year.md)

### Enums

 * [age range enum](age range enum.md) - Enum to capture the age range that an Indiviudal belongs to.
 * [biological sex enum](biological sex enum.md) - The biological sex of an Individual as determined by their chromosomes.
 * [disease or healthy enum](disease or healthy enum.md) - Enum to capture whether a condition corresponds to a disease or a healthy state.
 * [file format enum](file format enum.md) - Enum to capture file types.
 * [forward or reverse enum](forward or reverse enum.md) - Enum to capture whether the reads from paired-end sequencing are forward (R1) or reverse (R2).
 * [mutant or wildtype enum](mutant or wildtype enum.md) - Enum to capture whether a condition corresponds to a mutant or a wildtype.
 * [study type enum](study type enum.md) - Enum to capture the type of a study.
 * [treatment or control enum](treatment or control enum.md) - Enum to capture whether a condition corresponds to a treatment or a control.
 * [vital status enum](vital status enum.md) - Enum to capture the vital status of an individual.

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
