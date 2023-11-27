
# Class: IdentifiedByAliasMixin




URI: [GHGA:IdentifiedByAliasMixin](https://w3id.org/GHGA/IdentifiedByAliasMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Trio]uses%20-.->[IdentifiedByAliasMixin&#124;alias:string],[Study]uses%20-.->[IdentifiedByAliasMixin],[SequencingProtocol]uses%20-.->[IdentifiedByAliasMixin],[SequencingProcess]uses%20-.->[IdentifiedByAliasMixin],[SequencingExperiment]uses%20-.->[IdentifiedByAliasMixin],[Sample]uses%20-.->[IdentifiedByAliasMixin],[Publication]uses%20-.->[IdentifiedByAliasMixin],[LibraryPreparationProtocol]uses%20-.->[IdentifiedByAliasMixin],[Individual]uses%20-.->[IdentifiedByAliasMixin],[File]uses%20-.->[IdentifiedByAliasMixin],[Dataset]uses%20-.->[IdentifiedByAliasMixin],[DataAccessPolicy]uses%20-.->[IdentifiedByAliasMixin],[DataAccessCommittee]uses%20-.->[IdentifiedByAliasMixin],[Condition]uses%20-.->[IdentifiedByAliasMixin],[Biospecimen]uses%20-.->[IdentifiedByAliasMixin],[AnalysisProcess]uses%20-.->[IdentifiedByAliasMixin],[Analysis]uses%20-.->[IdentifiedByAliasMixin],[AliasMixin]^-[IdentifiedByAliasMixin],[Trio],[Study],[SequencingProtocol],[SequencingProcess],[SequencingExperiment],[Sample],[Publication],[LibraryPreparationProtocol],[Individual],[File],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Condition],[Biospecimen],[AnalysisProcess],[Analysis],[AliasMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Trio]uses%20-.->[IdentifiedByAliasMixin&#124;alias:string],[Study]uses%20-.->[IdentifiedByAliasMixin],[SequencingProtocol]uses%20-.->[IdentifiedByAliasMixin],[SequencingProcess]uses%20-.->[IdentifiedByAliasMixin],[SequencingExperiment]uses%20-.->[IdentifiedByAliasMixin],[Sample]uses%20-.->[IdentifiedByAliasMixin],[Publication]uses%20-.->[IdentifiedByAliasMixin],[LibraryPreparationProtocol]uses%20-.->[IdentifiedByAliasMixin],[Individual]uses%20-.->[IdentifiedByAliasMixin],[File]uses%20-.->[IdentifiedByAliasMixin],[Dataset]uses%20-.->[IdentifiedByAliasMixin],[DataAccessPolicy]uses%20-.->[IdentifiedByAliasMixin],[DataAccessCommittee]uses%20-.->[IdentifiedByAliasMixin],[Condition]uses%20-.->[IdentifiedByAliasMixin],[Biospecimen]uses%20-.->[IdentifiedByAliasMixin],[AnalysisProcess]uses%20-.->[IdentifiedByAliasMixin],[Analysis]uses%20-.->[IdentifiedByAliasMixin],[AliasMixin]^-[IdentifiedByAliasMixin],[Trio],[Study],[SequencingProtocol],[SequencingProcess],[SequencingExperiment],[Sample],[Publication],[LibraryPreparationProtocol],[Individual],[File],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Condition],[Biospecimen],[AnalysisProcess],[Analysis],[AliasMixin])

## Parents

 *  is_a: [AliasMixin](AliasMixin.md) - Mixin for entities that can be assigned an alias at the time of metadata submission.

## Mixin for

 * [Analysis](Analysis.md) (mixin)  - An Analysis is a data transformation that transforms input data to output data.
 * [AnalysisProcess](AnalysisProcess.md) (mixin)  - An Analysis Process captures the workflow steps that were performed to analyze data obtained from a Sequencing Experiment.
 * [Biospecimen](Biospecimen.md) (mixin)  - A Biospecimen is any natural material taken from a biological entity for testing, diagnostics, treatment, or research purposes.  It is linked to the Individual from which the Biospecimen is derived.
 * [Condition](Condition.md) (mixin)  - A Condition specifies which special characteristics and treatments apply to a Sample. It is used to link comparable Samples (e.g., healthy Samples, wildtype Samples).
 * [DataAccessCommittee](DataAccessCommittee.md) (mixin)  - A group of members that are delegated to grant access to one or more datasets after ensuring the criteria for data sharing has been met,  and request for data use does not raise ethical and/or legal concerns.
 * [DataAccessPolicy](DataAccessPolicy.md) (mixin)  - A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.
 * [Dataset](Dataset.md) (mixin)  - A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
 * [File](File.md) (mixin)  - A file is an object that contains information generated from a process, either an Experiment or an Analysis.
 * [Individual](Individual.md) (mixin)  - An Individual is a Person who is participating in a Study.
 * [LibraryPreparationProtocol](LibraryPreparationProtocol.md) (mixin)  - The Library Preparation Protocol captures information about the library preparation of a Sequencing Experiment.
 * [Publication](Publication.md) (mixin)  - A Publication represents an article that is published. The minimum expectation is that the publication has a valid DOI.
 * [Sample](Sample.md) (mixin)  - A Sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use.  It is prepared from a Biospecimen.
 * [SequencingExperiment](SequencingExperiment.md) (mixin)  - A Sequencing Experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
 * [SequencingProcess](SequencingProcess.md) (mixin)  - The Sequencing Process captures the technical parameters that were used to produce sequencing output from the Sample. It links the Sample to sequencing output.
 * [SequencingProtocol](SequencingProtocol.md) (mixin)  - The Sequencing Protocol captures information about parameters and metadata associated with a Sequencing Experiment.
 * [Study](Study.md) (mixin)  - A Study is an experimental investigation of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.
 * [Trio](Trio.md) (mixin)  - A Trio is a study design in which the genetic information of three individuals within a family unit is analyzed. It consists of a child and their biological parents.

## Referenced by Class


## Attributes


### Own

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
