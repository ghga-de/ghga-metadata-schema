
# GHGA-Metadata-Schema


**metamodel version:** 1.7.0

**version:** 0.9.0


The metadata schema for the German Human Genome-Phenome Archive (GHGA).


### Classes

 * [Attribute](Attribute.md) - A key/value pair that further characterizes an entity.
 * [NamedThing](NamedThing.md) - A databased entity, concept or class. This is a generic class that is the root of all the other classes.
     * [Agent](Agent.md) - An agent is something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity. Agents include a Person, Organization, or Software that performs an activity.
     * [BiologicalQuality](BiologicalQuality.md) - A biological quality is a quality held by a biological entity.
         * [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) - Disease or Phenotypic Feature that the entity is associated with. This entity is a union of Disease and Phenotypic Feature and exists to accommodate situations where Disease concepts are used interchangeably with Phenotype concepts or vice-versa.
             * [Disease](Disease.md) - A disease is a disposition to undergo pathological processes that exists in an organism because of one or more disorders in that organism.
             * [PhenotypicFeature](PhenotypicFeature.md) - The observable form taken by some character (or group of characters) in an individual or an organism, excluding pathology and disease. The detectable outward manifestations of a specific genotype.
     * [Committee](Committee.md) - A group of people organized for a specific purpose.
         * [DataAccessCommittee](DataAccessCommittee.md) - A group of members that are delegated to grant access to one or more datasets after ensuring the minimum criteria for data sharing has been met, and request for data use does not raise ethical and/or legal concerns.
     * [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.
         * [DataAccessPolicy](DataAccessPolicy.md) - A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.
         * [DataUseCondition](DataUseCondition.md) - Data Use Condition represents the use conditions associated with a policy.
         * [DataUseModifier](DataUseModifier.md) - Data use modifiers indicate additional conditions for use.
         * [DataUsePermission](DataUsePermission.md) - A data item that is used to indicate consent permissions for datasets and/or materials and relates to the purposes for which datasets and/or material might be removed, stored or used.
         * [Dataset](Dataset.md) - A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
         * [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.
         * [Protocol](Protocol.md) - A plan specification which has sufficient level of detail and quantitative information to communicate it between investigation agents, so that different investigation agents will reliably be able to independently reproduce the process.
             * [LibraryPreparationProtocol](LibraryPreparationProtocol.md) - Information about the library preparation of an Experiment.
             * [SequencingProtocol](SequencingProtocol.md) - Information about the sequencing of a sample.
         * [Publication](Publication.md) - The Publication entity represents a publication. While a publication can be any article that is published, the minimum expectation is that the publication has a valid DOI.
         * [Technology](Technology.md) - A Technology is an abstraction that represents the instrument used for an assay. The Technology entity captures instrument-specific attributes that are relevant for an Experiment entity. The Technology entity may be further characterized by its children where each child has fields that are relevant to that particular technology.
         * [Workflow](Workflow.md) - A Workflow is an abstraction that represents the workflow used to perform an analysis. The Workflow entity captures workflow-specific attributes that are relevant for an Analysis entity. The Workflow entity may be further characterized by its children where each child has fields that are relevant to that particular workflow.
         * [WorkflowStep](WorkflowStep.md) - A Workflow Step represents each individual step performed in a Workflow. If the Workflow is a single-step workflow then the Workflow has just one Workflow Step entity. If the Workflow is a multi-step workflow then the Workflow has a Workflow Step entity for each step. All Workflow step specific attributes like parameters, and metadata about execution environment are captured by the Workflow Step entity.
     * [MaterialEntity](MaterialEntity.md) - A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.
         * [AnatomicalEntity](AnatomicalEntity.md) - Biological entity that is either an individual member of a biological species or constitutes the structural organization of an individual member of a biological species.
         * [Biospecimen](Biospecimen.md) - A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics, treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is derived.
         * [CellLine](CellLine.md) - A cultured cell population that represents a genetically stable and homogenous population of cultured cells that shares a common propagation history.
         * [Population](Population.md) - A population is a collection of individuals from the same taxonomic class living, counted or sampled at a particular site or in a particular area.
             * [Ancestry](Ancestry.md) - Population category defined using ancestry informative markers (AIMs) based on genetic/genomic data.
             * [Cohort](Cohort.md) - A cohort is a collection of individuals that share a common characteristic/observation and have been grouped together for a research study/investigation.
             * [Family](Family.md) - A domestic group, or a number of domestic groups linked through descent (demonstrated or stipulated) from a common ancestor, marriage, or adoption.
         * [Sample](Sample.md) - A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).
     * [Person](Person.md) - A member of the species Homo sapiens.
         * [Individual](Individual.md) - An Individual is a Person who is participating in a Study.
             * [Donor](Donor.md) - A Donor is an Individual that participates in a research Study by donating a Biospecimen. The use of the Biospecimen is restricted to the consent provided by the Donor.
         * [Member](Member.md) - Member of an Organization or a Committee.
         * [User](User.md) - A user in GHGA.
     * [PlannedProcess](PlannedProcess.md) - A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and depends on some entity during the time it occurs.
         * [AnalysisProcess](AnalysisProcess.md) - An analysis process is a process that describes how one or more Files, from a Study, are transformed to another set of Files via a Workflow. The analysis process also keeps track of the workflow metadata and the Agent that is running the Analysis.
         * [DataTransformation](DataTransformation.md) - A data transformation technique used to analyze and interpret data to gain a better understanding of it.
             * [Analysis](Analysis.md) - An Analysis is a data transformation that transforms input data to output data. The workflow used to achieve this transformation and the individual steps are also captured.
         * [ExperimentProcess](ExperimentProcess.md) - An Experiment Process is a process that describes how a Sample is transformed to a File via an assay. The Experiment Process also keeps track of the Protocol used and the Agent that is running the experiment.
         * [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.
             * [Experiment](Experiment.md) - An experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
             * [Study](Study.md) - Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.
         * [ResearchActivity](ResearchActivity.md) - A planned process executed in the performance of scientific research wherein systematic investigations are performed to establish facts and reach new conclusions about phenomena in the world.
             * [Project](Project.md) - A high level organization for a collection of studies based on a research proposal that aims to achieve certain goals.
 * [Submission](Submission.md) - A grouping entity that represents information about one or more entities. A submission can be considered as a set of inter-related (and inter-connected) entities that represent a data submission to GHGA.
 * [WorkflowParameter](WorkflowParameter.md) - A key/value pair that represents a parameter used in a Workflow Step.

### Mixins

 * [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 * [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.
 * [DeprecatedMixin](DeprecatedMixin.md) - Mixin for entities that can be deprecated.
 * [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an EGA accession, in addition to GHGA accession.
 * [MetadataMixin](MetadataMixin.md) - Mixin for tracking schema specific metadata about an instance.
 * [OntologyClassMixin](OntologyClassMixin.md) - Mixin for entities that represent an class/term/concept from an ontology.
 * [PublicationMixin](PublicationMixin.md) - Mixin for entities that can have one or more publications.
 * [ReleaseStatusMixin](ReleaseStatusMixin.md) - Mixin for entities that can be released at a later point in time.

### Slots

 * [abstract](abstract.md) - The study abstract that describes the goals.  Can also hold abstract from a publication related to this study
     * [publication➞abstract](publication_abstract.md) - The study abstract that describes the goals. Can also hold abstract from a publication related to this study.
 * [accession](accession.md) - A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
 * [additional name](additional_name.md) - Additional name(s).
 * [affiliation](affiliation.md) - The Institution(s) associated with an entity.
     * [study➞affiliation](study_affiliation.md)
     * [submission➞affiliation](submission_affiliation.md) - Institution/Center/Data Hub that is providing this submission.
 * [age](age.md) - Age of an individual.
     * [individual➞age](individual_age.md)
 * [alias](alias.md) - The alias for an entity.
     * [named thing➞alias](named_thing_alias.md) - The alias (alternate identifier) for an entity.
         * [analysis➞alias](analysis_alias.md) - An alias uniquely identifying this Analysis entitiy.
         * [biospecimen➞alias](biospecimen_alias.md) - The alias for an entity.
         * [data access committee➞alias](data_access_committee_alias.md) - The alias for an entity.
         * [data access policy➞alias](data_access_policy_alias.md) - The alias for an entity.
         * [dataset➞alias](dataset_alias.md) - The alias for an entity.
         * [experiment➞alias](experiment_alias.md) - The alias for an entity.
         * [file➞alias](file_alias.md) - The alias for an entity.
         * [individual➞alias](individual_alias.md) - The alias for an entity.
         * [project➞alias](project_alias.md) - The alias for an entity.
         * [protocol➞alias](protocol_alias.md) - The alias for an entity.
             * [library preparation protocol➞alias](library_preparation_protocol_alias.md)
             * [sequencing protocol➞alias](sequencing_protocol_alias.md)
         * [publication➞alias](publication_alias.md) - The alias for an entity.
         * [sample➞alias](sample_alias.md) - The alias for an entity.
         * [study➞alias](study_alias.md) - The alias for an entity.
         * [workflow➞alias](workflow_alias.md) - The alias for an entity.
 * [author](author.md) - The individual who is responsible for the content of a document version.
 * [biological replicates](biological_replicates.md) - A biological replicate is a replicate role that consists of independent biological replicates made from different individual biosamples.
 * [case control status](case_control_status.md) - Whether the sample is to be treated as Case or Control in a Study.
 * [category](category.md) - The category for this file: Whole Genome Sequencing, Whole Exome Sequencing, etc.
 * [cell barcode offset](cell_barcode_offset.md) - The offset in sequence of the cell identifying barcode. (Eg. '0').
 * [cell barcode read](cell_barcode_read.md) - The type of read that contains the cell barcode (eg: index1/index2/read1/read2).
 * [cell barcode size](cell_barcode_size.md) - The size of the cell identifying barcode (E.g. '16').
 * [checksum](checksum.md) - A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data. The receiving system recomputes the checksum based upon the received data and compares this value with the one sent with the data. If the two values are the same, the receiver has some confidence that the data was received correctly.
     * [file➞checksum](file_checksum.md)
 * [checksum type](checksum_type.md) - The type of algorithm used to generate the checksum of a file.
     * [file➞checksum type](file_checksum_type.md)
 * [concept identifier](concept_identifier.md) - The Compact URI (CURIE) that uniquely identifies a concept from an ontology, thesaurus, or terminology.
     * [ontology class mixin➞concept identifier](ontology_class_mixin_concept_identifier.md) - The Compact URI (CURIE) that uniquely identifies this ontology class.
 * [concept name](concept_name.md) - The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.
 * [creation date](creation_date.md) - Timestamp (in ISO 8601 format) when the entity was created.
     * [named thing➞creation date](named_thing_creation_date.md)
     * [submission➞creation date](submission_creation_date.md) - Timestamp (in ISO 8601 format) when the Submission was created.
 * [data request form](data_request_form.md) - Data Request Form that is associated with a Data Access Policy.
     * [data access policy➞data request form](data_access_policy_data_request_form.md) - Data Request Form that is associated with this Data Access Policy.
 * [deprecation date](deprecation_date.md) - The timestamp (in ISO 8601 format) when the entity was deprecated.
 * [description](description.md) - Description of an entity.
     * [analysis➞description](analysis_description.md) - Describing how an Analysis was carried out. (e.g.: computational tools, settings, etc.).
     * [data access committee➞description](data_access_committee_description.md) - A description for the Data Access Committee.
     * [data access policy➞description](data_access_policy_description.md) - A short description for the Data Access Policy.
     * [dataset➞description](dataset_description.md)
     * [experiment➞description](experiment_description.md) - A detailed description of the Experiment.
     * [ontology class mixin➞description](ontology_class_mixin_description.md) - The description or definition of an ontology class.
     * [project➞description](project_description.md) - Short textual description of the project.
     * [protocol➞description](protocol_description.md) - Detailed description of the Protocol.
         * [library preparation protocol➞description](library_preparation_protocol_description.md) - Description about how a sequencing library was prepared (eg: Library construction method).
         * [sequencing protocol➞description](sequencing_protocol_description.md) - Description about the sequencing protocol (eg: mRNA-seq,Whole exome long-read sequencing etc).
     * [sample➞description](sample_description.md) - Short textual description of the sample (How the sample was collected, sample source, protocol followed for processing the sample etc).
     * [study➞description](study_description.md) - A detailed description (abstract) that describes the goals of this Study.
 * [drs uri](drs_uri.md) - GA4GH Data Repository Service (DRS) identifier URI for a file.
 * [ega accession](ega_accession.md) - A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
 * [email](email.md) - Email of a person.
     * [member➞email](member_email.md) - The email of the Member.
 * [end bias](end_bias.md) - The end of the cDNA molecule that is preferentially sequenced, e.g. 3/5 prime tag or end, or the full-length transcript.
 * [experimental replicates](experimental_replicates.md) - The replicate number of the assay, i.e. the numeric iteration for the assay that was repeated.
 * [family name](family_name.md) - Last name.
 * [flow cell id](flow_cell_id.md) - Flow Cell ID (eg: Experiment ID_Cell 1_Lane_1). The barcode assigned to a flow cell used in nucleotide sequencing.
 * [flow cell type](flow_cell_type.md) - Type of flow cell used (e.g. S4, S2 for NovaSeq; PromethION, Flongle for Nanopore). Aparatus in the fluidic subsystem where the sheath and sample meet. Can be one of several types; jet-in-air, quartz cuvette, or a hybrid of the two. The sample flows through the center of a fluid column of sheath fluid in the flow cell.
 * [format](format.md) - The format of the file: BAM, SAM, CRAM, BAI, etc.
     * [file➞format](file_format.md)
 * [geographical region](geographical_region.md) - The geographical region where the Individual is located. Any demarcated area of the Earth; may be determined by both natural and human boundaries.
 * [given name](given_name.md) - First name.
 * [has agent](has_agent.md) - A person or an entity that is performing a Planned Process entity.
     * [analysis process➞has agent](analysis_process_has_agent.md) - The Agent - a software, institution, or human - that is executing or responsible for executing the workflow.
     * [experiment process➞has agent](experiment_process_has_agent.md) - The Agent - a software, institution, or human - that is executing or responsible for executing the Experiment Process.
 * [has analysis](has_analysis.md) - The analysis associated with an entity.
     * [dataset➞has analysis](dataset_has_analysis.md) - One or more Analysis entities that are referenced by this Dataset.
     * [submission➞has analysis](submission_has_analysis.md) - Information about one or more Analysis entities associated with this submission.
 * [has analysis process](has_analysis_process.md)
     * [analysis➞has analysis process](analysis_has_analysis_process.md) - One or more Analysis Process entities associated with this Analysis.
 * [has anatomical entity](has_anatomical_entity.md) - Anatomical site associated with an entity.
     * [sample➞has anatomical entity](sample_has_anatomical_entity.md)
 * [has ancestry](has_ancestry.md) - A person's descent or lineage, from a person or from a population. Typically this is a value from HANCESTRO (Human Ancestry Ontology).
 * [has attribute](has_attribute.md) - Key/value pairs corresponding to an entity.
     * [project➞has attribute](project_has_attribute.md) - Custom attributes for the Project  (eg: Cancer - Colon cancer, prostrate cancer, blood cancer etc)
     * [protocol➞has attribute](protocol_has_attribute.md) - One or more attributes that further characterizes this Protocol.
         * [library preparation protocol➞has attribute](library_preparation_protocol_has_attribute.md) - One or more attributes that further characterizes this Library Preparation Protocol.
         * [sequencing protocol➞has attribute](sequencing_protocol_has_attribute.md) - One or more attributes that further characterizes this Sequencing Protocol.
     * [study➞has attribute](study_has_attribute.md) - Custom key/value pairs that further characterizes the Study. (e.g.: approaches - single-cell, bulk etc)
 * [has biospecimen](has_biospecimen.md) - The biospecimen associated with an entity.
     * [sample➞has biospecimen](sample_has_biospecimen.md) - The Biospecimen from which this Sample was prepared from.
     * [submission➞has biospecimen](submission_has_biospecimen.md) - Information about one or more Biospecimen entities associated with this submission.
 * [has children](has_children.md) - The children of an entity.
     * [individual➞has children](individual_has_children.md) - One or more children for this Individual.
 * [has data access committee](has_data_access_committee.md) - Data Access Committee associated with an entity.
     * [data access policy➞has data access committee](data_access_policy_has_data_access_committee.md) - The Data Access Committee linked to this policy.
     * [submission➞has data access committee](submission_has_data_access_committee.md) - The Data Access Committee that applies to Dataset in this submission.
 * [has data access policy](has_data_access_policy.md) - Data Access Policy associated with an entity.
     * [dataset➞has data access policy](dataset_has_data_access_policy.md) - The Data Access Policy that applies to this Dataset.
     * [submission➞has data access policy](submission_has_data_access_policy.md) - The Data Access Policy that applies to Dataset in this submission.
 * [has data use condition](has_data_use_condition.md) - Data Use Condition entities that are associated with an entity.
     * [data access policy➞has data use condition](data_access_policy_has_data_use_condition.md) - Data Use Condition entities that are associated with the Data Access Policy.
 * [has data use modifier](has_data_use_modifier.md) - Modifier for Data use permission associated with an entity. Should be descendants of 'DUO:0000017 data use modifier'
     * [data use condition➞has data use modifier](data_use_condition_has_data_use_modifier.md) - Modifier for Data use permission associated with a policy. Should be descendants of 'DUO:0000017 data use modifier'
 * [has data use permission](has_data_use_permission.md) - Data use permission associated with an entity. Typically one or more terms from DUO. Should be descendants of 'DUO:0000001 data use permission'.
     * [data use condition➞has data use permission](data_use_condition_has_data_use_permission.md) - Data use permission associated with a policy. Typically one or more terms from DUO and should be descendants of 'DUO:0000001 data use permission'.
 * [has dataset](has_dataset.md) - The Dataset associated with an entity.
     * [submission➞has dataset](submission_has_dataset.md) - One or more Dataset that are part of this submission.
 * [has disease](has_disease.md) - Disease concept that the entity is associated with.
     * [individual➞has disease](individual_has_disease.md) - The Disease entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Mondo Disease Ontology. For example, 'MONDO:0003742' indicates that the Individual - from which the Biospecimen was extracted from - suffers from 'Heart Fibrosarcoma'.
 * [has experiment](has_experiment.md) - The experiment associated with an entity.
     * [dataset➞has experiment](dataset_has_experiment.md) - One or more Experiment entities that are referenced by this Dataset.
     * [submission➞has experiment](submission_has_experiment.md) - Information about one or more Experiment entities associated with this submission.
 * [has experiment process](has_experiment_process.md)
     * [experiment➞has experiment process](experiment_has_experiment_process.md) - One or more Experiment Processes entities associated with this Experiment.
 * [has file](has_file.md) - The file associated with an entity.
     * [dataset➞has file](dataset_has_file.md) - One or more File entities that collectively are part of this Dataset.
     * [experiment➞has file](experiment_has_file.md) - One or more Files entities that are generated as output of this Experiment.
     * [individual➞has file](individual_has_file.md) - Additional/supplementary files associated with an Individual. Typically, a phenopacket or pedigree file.
     * [protocol➞has file](protocol_has_file.md) - A document that describes the Protocol.
     * [study➞has file](study_has_file.md) - Additional/supplementary files associated with a Study.
     * [submission➞has file](submission_has_file.md) - Information about one or more File entities associated with this submission.
 * [has individual](has_individual.md) - The subject/individual associated with an entity.
     * [biospecimen➞has individual](biospecimen_has_individual.md)
     * [sample➞has individual](sample_has_individual.md) - The Individual from which this Sample was derived from.
     * [submission➞has individual](submission_has_individual.md) - Information about one or more Individual entities associated with this submission.
 * [has input](has_input.md) - The input to a Planned Process.
     * [analysis process➞has input](analysis_process_has_input.md) - The input data File entities used in the Analysis Process.
     * [analysis➞has input](analysis_has_input.md) - The input data File entities used in the Analysis.
     * [experiment process➞has input](experiment_process_has_input.md) - The input to the Experiment Process. Usually a Sample entity.
 * [has library preparation protocol](has_library_preparation_protocol.md) - The Library Preparation Protocol associated with an entity.
 * [has member](has_member.md) - The members associated with a committee.
     * [cohort➞has member](cohort_has_member.md) - One or more Individuals that collectively define this Cohort.
     * [data access committee➞has member](data_access_committee_has_member.md) - All the members that are part of this Data Access Committee.
     * [family➞has member](family_has_member.md) - One or more Individuals that collectively define this Family.
     * [submission➞has member](submission_has_member.md) - One or more member that are part of the Data Access Committee referenced in this submission.
 * [has output](has_output.md) - The output of a Planned Process entity.
     * [analysis process➞has output](analysis_process_has_output.md) - The output data File entities generated by the Analysis Process.
     * [analysis➞has output](analysis_has_output.md) - The output data File entities generated by this Analysis.
     * [experiment process➞has output](experiment_process_has_output.md) - The output of this Experiment Process. Usually a File entity.
 * [has parent](has_parent.md) - The parent of an entity.
     * [individual➞has parent](individual_has_parent.md) - One or more parent for this Individual.
 * [has phenotypic feature](has_phenotypic_feature.md) - Phenotypic feature concept that the entity is associated with.
     * [individual➞has phenotypic feature](individual_has_phenotypic_feature.md) - The Phenotypic Feature entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Human Phenotype Ontology. For example, 'HP:0100244' indicates that the Individual - from which the Biospecimen was extracted from - exhibits 'Fibrosarcoma' as one of its phenotype.
 * [has proband](has_proband.md) - The Individual that is reported to have a disorder in a Family.
     * [family➞has proband](family_has_proband.md) - The Individual that is reported to have a disorder which results in the Family being brought into a Study.
 * [has project](has_project.md) - The project associated with an entity.
     * [study➞has project](study_has_project.md) - The project associated with this Study.
     * [submission➞has project](submission_has_project.md) - Information about a Project entity associated with this submission.
 * [has protocol](has_protocol.md) - The protocol associated with an entity.
     * [experiment process➞has protocol](experiment_process_has_protocol.md) - The Protocol entity used by this Experiment Process.
     * [experiment➞has protocol](experiment_has_protocol.md) - One or more Protocol entities associated with this Experiment.
     * [submission➞has protocol](submission_has_protocol.md) - One or more Protocol entities associated with this Submission.
 * [has publication](has_publication.md) - The Publication associated with an entity.
     * [dataset➞has publication](dataset_has_publication.md) - One or more Publication entities associated with this Dataset.
     * [study➞has publication](study_has_publication.md) - One or more Publication entities associated with this Study.
     * [submission➞has publication](submission_has_publication.md) - One or more Publication entities associated with this Submission.
 * [has sample](has_sample.md) - The sample associated with an entity.
     * [dataset➞has sample](dataset_has_sample.md) - One or more Sample entities that are referenced by this Dataset.
     * [experiment➞has sample](experiment_has_sample.md) - The Sample entity associated with this Experiment.
     * [submission➞has sample](submission_has_sample.md) - Information about one or more Sample entities associated with this submission.
 * [has sequencing protocol](has_sequencing_protocol.md) - The sequencing protocol associated with an entity.
 * [has study](has_study.md) - The study associated with an entity.
     * [analysis➞has study](analysis_has_study.md) - The Study entity associated with this Analysis.
     * [dataset➞has study](dataset_has_study.md) - One or more Study entities that are referenced by this Dataset.
     * [experiment➞has study](experiment_has_study.md) - The Study entity associated with this Experiment.
     * [submission➞has study](submission_has_study.md) - Information about a Study entities associated with this submission.
 * [has technology](has_technology.md)
 * [has workflow](has_workflow.md) - The Workflow entity associated wtih a Planned Process entity.
     * [analysis process➞has workflow](analysis_process_has_workflow.md) - The Workflow entity associated with this Analysis Process.
     * [analysis➞has workflow](analysis_has_workflow.md) - One or more Workflow entities associated with this Analysis.
 * [has workflow parameter](has_workflow_parameter.md) - The parameter(s) associated with a Workflow Step entity.
     * [workflow step➞has workflow parameter](workflow_step_has_workflow_parameter.md) - One or more parameters that are associated with this Workflow Step.
 * [has workflow step](has_workflow_step.md) - The individual workflow step that with other workflow step(s) collectively defines a Workflow entity.
     * [workflow➞has workflow step](workflow_has_workflow_step.md)
 * [id](id.md) - An identifier that uniquely represents an entity.
     * [named thing➞id](named_thing_id.md) - The internal unique identifier for an entity.
         * [publication➞id](publication_id.md) - An identifier that uniquely represents an entity.
     * [submission➞id](submission_id.md) - A internal unique identifier for the Submission.
 * [index sequence](index_sequence.md) - A unique nucleotide sequence that is added to a sample during library preparation to serve as a unique identifier for the sample.
 * [instrument model](instrument_model.md) - The name and model of the technology platform used to perform sequencing.
     * [sequencing protocol➞instrument model](sequencing_protocol_instrument_model.md)
 * [isolation](isolation.md) - Method or device employed for collecting/isolating a biospecimen or a sample.
 * [journal](journal.md) - Name of the journal.
 * [karyotype](karyotype.md) - The karyotype of an individual if defined.
 * [key](key.md) - The key of an attribute.
     * [attribute➞key](attribute_key.md) - The key for an attribute.
     * [workflow parameter➞key](workflow_parameter_key.md) - Key that represents the parameter name.
 * [key type](key_type.md) - The semantic type for the key of an attribute.
     * [attribute➞key type](attribute_key_type.md) - A semantic type that characterizes the attribute key. Usually this is a term from an ontology. For example, 'MAXO:0000616' indicates that the attribute is a measurement of oxygen saturation in the blood.
 * [lane number](lane_number.md) - The numerical identifier for the lane or machine unit where a sample was located during nucleotide sequencing.
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
 * [name](name.md) - The name for an entity.
     * [data access committee➞name](data_access_committee_name.md) - The name for the Data Access Committee.
     * [data access policy➞name](data_access_policy_name.md) - A name for the Data Access Policy.
     * [file➞name](file_name.md) - The given filename.
     * [ontology class mixin➞name](ontology_class_mixin_name.md) - The name or label (rdfs:label) of an ontology class.
     * [protocol➞name](protocol_name.md) - Name of the protocol (eg: Sample extraction_PCR amplification).
     * [sample➞name](sample_name.md) - Name of the sample (eg:GHGAS_Blood_Sample1 or GHGAS_PBMC_RNAseq_S1).
     * [workflow➞name](workflow_name.md)
 * [ontology name](ontology_name.md) - The name of the ontology from which this ontology class was chosen.
 * [ontology version](ontology_version.md) - The version of the ontology from which this ontology class was chosen.
 * [organization](organization.md) - The organization associated with a person.
     * [member➞organization](member_organization.md) - The organization that the Member is part of.
 * [paired or single end](paired_or_single_end.md) - Denotes whether a submitted FASTQ file contains forward (R1) or reverse (R2) reads for paired-end sequencing. The number that identifies each read direction in a paired-end nucleotide sequencing replications.
 * [policy text](policy_text.md) - The complete text for the Data Access Policy.
     * [data access policy➞policy text](data_access_policy_policy_text.md) - The terms of data use and policy verbiage should be captured here.
 * [policy url](policy_url.md) - Alternative to pasting the Data Access Policy text.
     * [data access policy➞policy url](data_access_policy_policy_url.md) - URL for the policy, if available. This is useful if the terms of the policy is made available online at a resolvable URL.
 * [primer](primer.md) - The type of primer used for reverse transcription, e.g. 'oligo-dT' or 'random' primer. This allows users to identify content of the cDNA library input e.g. enriched for mRNA.
 * [reference chromosome](reference_chromosome.md) - The reference chromosome used for this Analysis.
     * [analysis➞reference chromosome](analysis_reference_chromosome.md)
 * [reference genome](reference_genome.md) - A published genetic sequence that is used as a reference sequence against which other sequences are compared. Reference genome(s) or annotation(s) used for prior analyses (eg: GRCh38.p13).
     * [analysis➞reference genome](analysis_reference_genome.md)
 * [release date](release_date.md) - The timestamp (in ISO 8601 format) when the entity was released for public consumption.
 * [release status](release_status.md) - The release status of an entity.
     * [dataset➞release status](dataset_release_status.md) - The release status of a Dataset.
     * [study➞release status](study_release_status.md) - The release status of a Study.
 * [replaced by](replaced_by.md) - Refers to the entity which replaces a currently deprecated entity.
 * [replaces](replaces.md) - Refers to a deprecated entity that is being replaced by the current entity.
 * [rnaseq strandedness](rnaseq_strandedness.md) - The strandedness of the library, whether reads come from both strands of the cDNA or only from the first (antisense) or the second (sense) strand.
 * [role](role.md) - The role that a user has within GHGA.
     * [user➞role](user_role.md) - The role of the user
 * [sample barcode read](sample_barcode_read.md) - The type of read that contains the sample barcode (eg: index1/index2/read1/read2).
 * [sample index sequence](sample_index_sequence.md) - A unique nucleotide sequence that is added to a sample during library preparation to serve as a unique identifier for the sample.
 * [sample lane number](sample_lane_number.md) - The numerical identifier for the lane or machine unit where a sample was located during nucleotide sequencing.
 * [schema type](schema_type.md) - The schema type an instance corresponds to.
 * [schema version](schema_version.md) - The version of the schema an instance corresponds to.
 * [sequencing center](sequencing_center.md) - Center where sample was sequenced.
     * [sequencing protocol➞sequencing center](sequencing_protocol_sequencing_center.md)
 * [sequencing read length](sequencing_read_length.md) - Length of sequencing reads (eg: Long or short or actual number of the read length etc). The number of nucleotides successfully ordered from each side of a nucleic acid fragment obtained after the completion of a sequencing process
 * [sex](sex.md) - The assemblage of physical properties or qualities by which male is distinguished from female; the physical difference between male and female; the distinguishing peculiarity of male or female.
     * [individual➞sex](individual_sex.md)
 * [size](size.md) - The size of a file in bytes.
     * [file➞size](file_size.md)
 * [storage](storage.md) - Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).
 * [submission date](submission_date.md) - The timestamp (in ISO 8601 format) when submission was marked completed.
 * [submission status](submission_status.md) - The status of a submission.
     * [submission➞submission status](submission_submission_status.md) - The status of a Submission.
 * [target coverage](target_coverage.md) - Mean coverage for whole genome sequencing, or mean target coverage for whole exome and targeted sequencing. The number of times a particular locus (site, nucleotide, amplicon, region) was sequenced.
 * [target regions](target_regions.md) - Subset of genes or specific regions of the genome, which are most likely to be involved in the phenotype under study.
     * [library preparation protocol➞target regions](library_preparation_protocol_target_regions.md)
 * [technical replicates](technical_replicates.md) - A technical replicate is a replicate role where the same BioSample is use e.g. the same pool of RNA used to assess technical (as opposed to biological) variation within an experiment.
 * [telephone](telephone.md) - The telephone number associated with a person.
     * [member➞telephone](member_telephone.md) - The telephone number of the Member.
 * [tissue](tissue.md) - An anatomical structure consisting of similarly specialized cells and intercellular matrix, aggregated according to genetically determined spatial relationships, performing a specific function.
 * [title](title.md) - The title that describes an entity.
     * [dataset➞title](dataset_title.md) - A title for the submitted Dataset.
     * [experiment process➞title](experiment_process_title.md) - A descriptive title that explains the step(s) involved in performing the experiment leading up to the sequencing of the sample and generation of raw data from the instrument. (eg: Sample extraction -> Target Enrichment)
     * [experiment➞title](experiment_title.md) - Name for the experiment (eg: GHGAE_PBMC_RNAseq).
     * [project➞title](project_title.md) - Comprehensive title for the project.
     * [publication➞title](publication_title.md) - The title for the Publication.
     * [study➞title](study_title.md) - A comprehensive title for the study.
 * [type](type.md) - The type of an entity.
     * [analysis➞type](analysis_type.md) - The type of the Analysis. Either Reference Alignment (BAM) or Sequence Variation (VCF)
     * [biospecimen➞type](biospecimen_type.md) - The type of Biospecimen.
     * [dataset➞type](dataset_type.md)
     * [experiment process➞type](experiment_process_type.md) - The type of experiment process.
     * [experiment➞type](experiment_type.md) - The type of Experiment.
     * [protocol➞type](protocol_type.md) - Type of the protocol (eg: Target enrichment).
         * [sequencing protocol➞type](sequencing_protocol_type.md) - Name of the library preparation protocol (eg: mRNA-seq,Whole exome long-read sequencing etc).
     * [sample➞type](sample_type.md) - The type of sample.
     * [study➞type](study_type.md) - The type of Study. For example, 'Cancer Genomics', 'Epigenetics', 'Exome Sequencing'.
 * [umi barcode offset](umi_barcode_offset.md) - The offset in sequence of the UMI identifying barcode. (E.g. '16').
 * [umi barcode read](umi_barcode_read.md) - The type of read that contains the UMI barcode (Eg: index1/index2/read1/read2).
 * [umi barcode size](umi_barcode_size.md) - The size of the UMI identifying barcode (Eg. '10').
 * [update date](update_date.md) - Timestamp (in ISO 8601 format) when the entity was updated.
     * [named thing➞update date](named_thing_update_date.md)
     * [submission➞update date](submission_update_date.md) - Timestamp (in ISO 8601 format) when the Submission was updated.
 * [url](url.md) - A URL to a resource.
     * [protocol➞url](protocol_url.md) - URL for the resource that describes this Protocol.
 * [value](value.md) - The value of an attribute
     * [attribute➞value](attribute_value.md) - The value for an attribute. Usually this is a numerical value (without the units).
     * [workflow parameter➞value](workflow_parameter_value.md) - Value corresponding to the the parameter key.
 * [value type](value_type.md) - The semantic type for the value of an attribute.
     * [attribute➞value type](attribute_value_type.md) - The value type that characterizes the attribute value. Usually this is a term from an ontology that describes how to interpret the value. For example, 'SIO:001413' indicates that the value is to be interpreted as a percentage.
 * [vital status](vital_status.md) - The state or condition of being living or deceased; also includes the case where the vital status is unknown.
     * [individual➞vital status](individual_vital_status.md) - Last known Vital Status of an Individual.
 * [vital status at sampling](vital_status_at_sampling.md) - Vital Status of an Individual at the point of sampling (eg:'Alive', 'Deceased').
 * [xref](xref.md) - Database cross references for an entity.
     * [named thing➞xref](named_thing_xref.md) - Holds one or more database cross references for an entity.
         * [protocol➞xref](protocol_xref.md) - One or more cross-references for this Protocol.  (Eg: manufacturer protocol, protocol from publication etc )
         * [publication➞xref](publication_xref.md) - One or more cross-references for this Publication.
         * [sample➞xref](sample_xref.md) - One or more cross-references for this Sample. For example, this Sample may have an EBI BioSamples accession or an EGA Sample accession.
 * [year](year.md) - Year in which the paper was published.

### Enums

 * [age range enum](age range enum.md) - Enum to capture the age range that an Indiviudal belongs to.
 * [biological sex enum](biological sex enum.md) - The biological sex of an Individual as determined by their chromosomes.
 * [case control status enum](case control status enum.md) - Enum to capture whether a Sample in a Study is to be considered as Case or Control.
 * [experiment process type enum](experiment process type enum.md) - The different types of Experiment Processes.
 * [file format enum](file format enum.md) - Enum to capture file types.
 * [paired or single end enum](paired or single end enum.md) - Enum to capture whether a sequencing experiment generates reads that are Paired-end or Single-end.
 * [release status enum](release status enum.md) - Enum to capture the release status of an entity.
 * [study type enum](study type enum.md) - Enum to capture the type of a study.
 * [submission status enum](submission status enum.md) - Enum to capture the status of a Submission.
 * [user role enum](user role enum.md) - Enum to capture the different roles a GHGA User can have.
 * [vital status enum](vital status enum.md) - Enum to capture the vital status of an individual.

### Subsets

 * [Essential](Essential.md) - Subset of properties that are considered to be essential for the functionality of GHGA.
 * [Optional](Optional.md) - Subset of properties that are considered to be optional.
 * [Public](Public.md) - Subset of properties that are considered to be public.
 * [Recommended](Recommended.md) - Subset of properties that are considered to be of importance for FAIR data sharing.
 * [Restricted](Restricted.md) - Subset of properties that are considered to be restricted.

### Types


#### Built in

 * **Bool**
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
