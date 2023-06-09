
# Class: IdentifiedByAliasMixin




URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/IdentifiedByAliasMixin](https://w3id.org/GHGA-Submission-Metadata-Schema/IdentifiedByAliasMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]uses%20-.->[IdentifiedByAliasMixin&#124;alias:string],[SequencingProtocol]uses%20-.->[IdentifiedByAliasMixin],[SequencingProcess]uses%20-.->[IdentifiedByAliasMixin],[SequencingExperiment]uses%20-.->[IdentifiedByAliasMixin],[Sample]uses%20-.->[IdentifiedByAliasMixin],[LibraryPreparationProtocol]uses%20-.->[IdentifiedByAliasMixin],[Individual]uses%20-.->[IdentifiedByAliasMixin],[File]uses%20-.->[IdentifiedByAliasMixin],[Dataset]uses%20-.->[IdentifiedByAliasMixin],[DataAccessPolicy]uses%20-.->[IdentifiedByAliasMixin],[DataAccessCommittee]uses%20-.->[IdentifiedByAliasMixin],[Condition]uses%20-.->[IdentifiedByAliasMixin],[Biospecimen]uses%20-.->[IdentifiedByAliasMixin],[Analysis]uses%20-.->[IdentifiedByAliasMixin],[AliasMixin]^-[IdentifiedByAliasMixin],[Study],[SequencingProtocol],[SequencingProcess],[SequencingExperiment],[Sample],[LibraryPreparationProtocol],[Individual],[File],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Condition],[Biospecimen],[Analysis],[AliasMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]uses%20-.->[IdentifiedByAliasMixin&#124;alias:string],[SequencingProtocol]uses%20-.->[IdentifiedByAliasMixin],[SequencingProcess]uses%20-.->[IdentifiedByAliasMixin],[SequencingExperiment]uses%20-.->[IdentifiedByAliasMixin],[Sample]uses%20-.->[IdentifiedByAliasMixin],[LibraryPreparationProtocol]uses%20-.->[IdentifiedByAliasMixin],[Individual]uses%20-.->[IdentifiedByAliasMixin],[File]uses%20-.->[IdentifiedByAliasMixin],[Dataset]uses%20-.->[IdentifiedByAliasMixin],[DataAccessPolicy]uses%20-.->[IdentifiedByAliasMixin],[DataAccessCommittee]uses%20-.->[IdentifiedByAliasMixin],[Condition]uses%20-.->[IdentifiedByAliasMixin],[Biospecimen]uses%20-.->[IdentifiedByAliasMixin],[Analysis]uses%20-.->[IdentifiedByAliasMixin],[AliasMixin]^-[IdentifiedByAliasMixin],[Study],[SequencingProtocol],[SequencingProcess],[SequencingExperiment],[Sample],[LibraryPreparationProtocol],[Individual],[File],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Condition],[Biospecimen],[Analysis],[AliasMixin])

## Parents

 *  is_a: [AliasMixin](AliasMixin.md) - Mixin for entities that can be assigned an alias at the time of metadata submission.

## Mixin for

 * [Analysis](Analysis.md) (mixin)  - An Analysis is a data transformation that transforms input data to output data. The workflow used to achieve this transformation and the individual steps are also captured.
 * [Biospecimen](Biospecimen.md) (mixin)  - A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics, treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is derived.
 * [Condition](Condition.md) (mixin)  - An condition that is linked to comparable samples.
 * [DataAccessCommittee](DataAccessCommittee.md) (mixin)  - A group of members that are delegated to grant access to one or more datasets after ensuring the minimum criteria for data sharing has been met, and request for data use does not raise ethical and/or legal concerns.
 * [DataAccessPolicy](DataAccessPolicy.md) (mixin)  - A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.
 * [Dataset](Dataset.md) (mixin)  - A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
 * [File](File.md) (mixin)  - A file is an object that contains information generated from a process, either an Experiment or an Analysis.
 * [Individual](Individual.md) (mixin)  - An Individual is a Person who is participating in a Study.
 * [LibraryPreparationProtocol](LibraryPreparationProtocol.md) (mixin)  - Information about the library_preparation of an sequencing experiment.
 * [Sample](Sample.md) (mixin)  - A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).
 * [SequencingExperiment](SequencingExperiment.md) (mixin)  - An sequencing experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
 * [SequencingProcess](SequencingProcess.md) (mixin)  - A sequencing process linking a sample to sequencing output.
 * [SequencingProtocol](SequencingProtocol.md) (mixin)  - Information about the sequencing of a sample.
 * [Study](Study.md) (mixin)  - Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

## Referenced by Class


## Attributes


### Own

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
