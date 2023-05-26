
# Subset: restricted


Subset of properties that are considered to be restricted.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/restricted](https://w3id.org/GHGA-Submission-Metadata-Schema/restricted)


### Classes


### Mixins


### Slots

 * [AliasMixin➞alias](AliasMixin_alias.md)
 * [Analysis➞alias](Analysis_alias.md) - An alias uniquely identifying this Analysis entitiy.
 * [Biospecimen➞individual](Biospecimen_individual.md) - The Individual entity from which this Biospecimen was derived.
 * [DataAccessCommittee➞main_contact](DataAccessCommittee_main_contact.md) - The main contact for the Data Access Committee.
 * [DataAccessCommittee➞members](DataAccessCommittee_members.md) - All the members that are part of this Data Access Committee.
 * [DataAccessPolicy➞data_access_committee](DataAccessPolicy_data_access_committee.md) - The Data Access Committee linked to this policy.
 * [DataAccessPolicy➞data_use_modifiers](DataAccessPolicy_data_use_modifiers.md) - Modifier for Data use permission associated with a policy. Should be descendants of 'DUO:0000017 data use modifier'
 * [DataAccessPolicy➞data_use_permission](DataAccessPolicy_data_use_permission.md) - Data use permission associated with a policy. Typically one or more terms from DUO and should be descendants of 'DUO:0000001 data use permission'.
 * [DataAccessPolicy➞policy_text](DataAccessPolicy_policy_text.md) - The terms of data use and policy verbiage should be captured here.
 * [DataAccessPolicy➞policy_url](DataAccessPolicy_policy_url.md) - URL for the policy, if available. This is useful if the terms of the policy is made available online at a resolvable URL.
 * [Dataset➞data_access_policy](Dataset_data_access_policy.md) - The Data Access Policy that applies to this Dataset.
 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)
 * [Individual➞age_at_sampling](Individual_age_at_sampling.md)
 * [Individual➞ancestries](Individual_ancestries.md)
 * [Individual➞children](Individual_children.md)
 * [Individual➞files](Individual_files.md) - Additional/supplementary files associated with an Individual. Typically, a phenopacket or pedigree file.
 * [Individual➞geographical_region](Individual_geographical_region.md)
 * [Individual➞karyotype](Individual_karyotype.md)
 * [Individual➞parents](Individual_parents.md)
 * [Individual➞phenotypic_features](Individual_phenotypic_features.md) - The Phenotypic Feature entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Human Phenotype Ontology. For example, 'HP:0100244' indicates that the Individual - from_which_the_Biospecimen was extracted from - exhibits_'Fibrosarcoma'_as_one_of_its_phenotype.
 * [Individual➞sex](Individual_sex.md)
 * [Individual➞vital_status](Individual_vital_status.md) - Last known Vital Status of an Individual.
 * [LibraryPreparationProtocol➞attributes](LibraryPreparationProtocol_attributes.md) - One or more attributes that further characterizes this library_preparation Protocol.
 * [OntologyClassMixin➞id](OntologyClassMixin_id.md)
 * [Person➞additional_name](Person_additional_name.md)
 * [Person➞family_name](Person_family_name.md)
 * [Person➞given_name](Person_given_name.md)
 * [Protocol➞attributes](Protocol_attributes.md) - One or more attributes that further characterizes this protocol.
 * [SampleFile➞sample](SampleFile_sample.md)
 * [Sample➞biospecimen](Sample_biospecimen.md) - The Biospecimen from which this Sample was prepared from.
 * [SequencingProcess➞sample](SequencingProcess_sample.md)
 * [SequencingProcess➞sequencing_experiment](SequencingProcess_sequencing_experiment.md)
 * [SequencingProtocol➞attributes](SequencingProtocol_attributes.md) - One or more attributes that further characterizes this Sequencing Protocol.
 * [Study➞alias](Study_alias.md)
 * [Study➞attributes](Study_attributes.md) - Custom key/value pairs that further characterizes the Study. (e.g.: approaches - single-cell,_bulk_etc)
 * [Submission➞analyses](Submission_analyses.md) - Information about one or more Analysis entities associated with this submission.
 * [Submission➞biospecimens](Submission_biospecimens.md) - Information about one or more Biospecimen entities associated with this submission.
 * [Submission➞data_access_committees](Submission_data_access_committees.md) - The Data Access Committee that applies to Dataset in this submission.
 * [Submission➞data_access_policies](Submission_data_access_policies.md) - The Data Access Policy that applies to Dataset in this submission.
 * [Submission➞individuals](Submission_individuals.md) - Information about one or more Individual entities associated with this submission.
 * [Submission➞members](Submission_members.md) - The members associated with a committee referenced in this submission
 * [Submission➞samples](Submission_samples.md) - Information about one or more Sample entities associated with this submission.
 * [Submission➞sequencing_experiments](Submission_sequencing_experiments.md) - Information about one or more Experiment entities associated with this submission.
 * [additional_name](additional_name.md) - additional_name(s).
 * [age_at_sampling](age_at_sampling.md) - Age of an individual.
 * [alias](alias.md) - The alias for an entity at the time of submission.
 * [analyses](analyses.md) - The analyses associated with an entity.
 * [ancestries](ancestries.md) - A person's descent or lineage, from a person or from a population.
 * [attributes](attributes.md) - Key/value pairs corresponding to an entity.
 * [biospecimen](biospecimen.md) - The biospecimen associated with an entity.
 * [biospecimens](biospecimens.md) - The biospecimens associated with an entity.
 * [children](children.md) - One or more children for an Individual.
 * [data_access_committee](data_access_committee.md) - Data Access Committee associated with an entity.
 * [data_access_committees](data_access_committees.md) - Data Access Committees associated with an entity.
 * [data_access_policies](data_access_policies.md) - Data Access Policies associated with an entity.
 * [data_access_policy](data_access_policy.md) - Data Access Policy associated with an entity.
 * [data_use_modifiers](data_use_modifiers.md) - Modifier for Data use permission associated with an entity. Should be descendants of 'DUO:0000017 data use modifier'
 * [data_use_permission](data_use_permission.md) - Data use permission associated with an entity. Typically one or more terms from DUO. Should be descendants of 'DUO:0000001 data use permission'.
 * [family_name](family_name.md) - Last name.
 * [files](files.md) - The files associated with an entity.
 * [geographical_region](geographical_region.md) - The geographical region where the Individual is located. Any demarcated area of the Earth; may be determined by both natural and human boundaries.
 * [given_name](given_name.md) - First name.
 * [id](id.md) - An identifier that uniquely represents an entity.
 * [individual](individual.md) - The subject/individual associated with an entity.
 * [individuals](individuals.md) - The subjects/individuals associated with an entity.
 * [inputs](inputs.md) - The inputs to a Planned Process.
 * [karyotype](karyotype.md) - The karyotype of an individual if defined.
 * [main_contact](main_contact.md) - The person who is the main contact for a committee.
 * [members](members.md) - The members associated with a committee.
 * [outputs](outputs.md) - The outputs of a Planned Process entity.
 * [parents](parents.md) - One or more parent for an Individual.
 * [phenotypic_features](phenotypic_features.md) - Phenotypic feature concepts that the entity is associated with.
 * [policy_text](policy_text.md) - The complete text for the Data Access Policy.
 * [policy_url](policy_url.md) - Alternative to pasting the Data Access Policy text.
 * [protocol](protocol.md) - The protocol associated with an entity.
 * [sample](sample.md) - The sample associated with an entity.
 * [samples](samples.md) - The samples associated with an entity.
 * [sequencing_experiment](sequencing_experiment.md) - The sequencing experiment associated with an entity.
 * [sequencing_experiments](sequencing_experiments.md) - The sequencing experiments associated with an entity.
 * [sex](sex.md) - The assemblage of physical properties or qualities by which male is distinguished from female; the physical difference between male and female; the distinguishing peculiarity of male or female.
 * [vital_status](vital_status.md) - The state or condition of being living or deceased; also includes the case where the vital status is unknown.

### Types


### Enums

