
# Class: IdentifiedByAliasMixin




URI: [GHGA:IdentifiedByAliasMixin](https://w3id.org/GHGA/IdentifiedByAliasMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]uses%20-.->[IdentifiedByAliasMixin&#124;alias:string],[Sample]uses%20-.->[IdentifiedByAliasMixin],[Publication]uses%20-.->[IdentifiedByAliasMixin],[Individual]uses%20-.->[IdentifiedByAliasMixin],[File]uses%20-.->[IdentifiedByAliasMixin],[ExperimentalMethod]uses%20-.->[IdentifiedByAliasMixin],[Experiment]uses%20-.->[IdentifiedByAliasMixin],[Dataset]uses%20-.->[IdentifiedByAliasMixin],[DataAccessPolicy]uses%20-.->[IdentifiedByAliasMixin],[DataAccessCommittee]uses%20-.->[IdentifiedByAliasMixin],[AnalysisMethod]uses%20-.->[IdentifiedByAliasMixin],[Analysis]uses%20-.->[IdentifiedByAliasMixin],[AliasMixin]^-[IdentifiedByAliasMixin],[Study],[Sample],[Publication],[Individual],[File],[ExperimentalMethod],[Experiment],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[AnalysisMethod],[Analysis],[AliasMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]uses%20-.->[IdentifiedByAliasMixin&#124;alias:string],[Sample]uses%20-.->[IdentifiedByAliasMixin],[Publication]uses%20-.->[IdentifiedByAliasMixin],[Individual]uses%20-.->[IdentifiedByAliasMixin],[File]uses%20-.->[IdentifiedByAliasMixin],[ExperimentalMethod]uses%20-.->[IdentifiedByAliasMixin],[Experiment]uses%20-.->[IdentifiedByAliasMixin],[Dataset]uses%20-.->[IdentifiedByAliasMixin],[DataAccessPolicy]uses%20-.->[IdentifiedByAliasMixin],[DataAccessCommittee]uses%20-.->[IdentifiedByAliasMixin],[AnalysisMethod]uses%20-.->[IdentifiedByAliasMixin],[Analysis]uses%20-.->[IdentifiedByAliasMixin],[AliasMixin]^-[IdentifiedByAliasMixin],[Study],[Sample],[Publication],[Individual],[File],[ExperimentalMethod],[Experiment],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[AnalysisMethod],[Analysis],[AliasMixin])

## Parents

 *  is_a: [AliasMixin](AliasMixin.md) - Mixin for entities that can be assigned an alias at the time of metadata submission.

## Mixin for

 * [Analysis](Analysis.md) (mixin)  - An Analysis is a data transformation that transforms input data to output data.
 * [AnalysisMethod](AnalysisMethod.md) (mixin)  - An Analysis Method captures the workflow steps that were performed to analyze data obtained from an Experiment.
 * [DataAccessCommittee](DataAccessCommittee.md) (mixin)  - A group of members that are delegated to grant access to one or more datasets after ensuring the criteria for data sharing has been met,  and request for data use does not raise ethical and/or legal concerns.
 * [DataAccessPolicy](DataAccessPolicy.md) (mixin)  - A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.
 * [Dataset](Dataset.md) (mixin)  - A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
 * [Experiment](Experiment.md) (mixin)  - An Experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
 * [ExperimentalMethod](ExperimentalMethod.md) (mixin)  - The Experimental Method captures the technical parameters that were used to produce output from the Sample.
 * [File](File.md) (mixin)  - A file is an object that contains information generated from a process, either an Experiment or an Analysis.
 * [Individual](Individual.md) (mixin)  - An Individual is a Person who is participating in a Study.
 * [Publication](Publication.md) (mixin)  - A Publication represents an article that is published. The minimum expectation is that the publication has a valid DOI.
 * [Sample](Sample.md) (mixin)  - A Sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use.  It is prepared from a Biospecimen.
 * [Study](Study.md) (mixin)  - A Study is an experimental investigation of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

## Referenced by Class


## Attributes


### Own

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
