
# Class: AccessionMixin


Mixin for entities that can be assigned a GHGA accession.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/AccessionMixin](https://w3id.org/GHGA-Submission-Metadata-Schema/AccessionMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]uses%20-.->[AccessionMixin&#124;accession:string],[SequencingProcess]uses%20-.->[AccessionMixin],[SequencingExperiment]uses%20-.->[AccessionMixin],[Sample]uses%20-.->[AccessionMixin],[Project]uses%20-.->[AccessionMixin],[Individual]uses%20-.->[AccessionMixin],[File]uses%20-.->[AccessionMixin],[Dataset]uses%20-.->[AccessionMixin],[DataAccessPolicy]uses%20-.->[AccessionMixin],[DataAccessCommittee]uses%20-.->[AccessionMixin],[Condition]uses%20-.->[AccessionMixin],[Biospecimen]uses%20-.->[AccessionMixin],[Analysis]uses%20-.->[AccessionMixin],[Study],[SequencingProcess],[SequencingExperiment],[Sample],[Project],[Individual],[File],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Condition],[Biospecimen],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]uses%20-.->[AccessionMixin&#124;accession:string],[SequencingProcess]uses%20-.->[AccessionMixin],[SequencingExperiment]uses%20-.->[AccessionMixin],[Sample]uses%20-.->[AccessionMixin],[Project]uses%20-.->[AccessionMixin],[Individual]uses%20-.->[AccessionMixin],[File]uses%20-.->[AccessionMixin],[Dataset]uses%20-.->[AccessionMixin],[DataAccessPolicy]uses%20-.->[AccessionMixin],[DataAccessCommittee]uses%20-.->[AccessionMixin],[Condition]uses%20-.->[AccessionMixin],[Biospecimen]uses%20-.->[AccessionMixin],[Analysis]uses%20-.->[AccessionMixin],[Study],[SequencingProcess],[SequencingExperiment],[Sample],[Project],[Individual],[File],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Condition],[Biospecimen],[Analysis])

## Mixin for

 * [Analysis](Analysis.md) (mixin)  - An Analysis is a data transformation that transforms input data to output data. The workflow used to achieve this transformation and the individual steps are also captured.
 * [Biospecimen](Biospecimen.md) (mixin)  - A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics, treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is derived.
 * [Condition](Condition.md) (mixin)  - An condition that is linked to comparable samples.
 * [DataAccessCommittee](DataAccessCommittee.md) (mixin)  - A group of members that are delegated to grant access to one or more datasets after ensuring the minimum criteria for data sharing has been met, and request for data use does not raise ethical and/or legal concerns.
 * [DataAccessPolicy](DataAccessPolicy.md) (mixin)  - A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.
 * [Dataset](Dataset.md) (mixin)  - A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
 * [File](File.md) (mixin)  - A file is an object that contains information generated from a process, either an Experiment or an Analysis.
 * [Individual](Individual.md) (mixin)  - An Individual is a Person who is participating in a Study.
 * [Project](Project.md) (mixin)  - A high level organization for a collection of studies based on a research proposal that aims to achieve certain goals.
 * [Sample](Sample.md) (mixin)  - A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).
 * [SequencingExperiment](SequencingExperiment.md) (mixin)  - An sequencing experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
 * [SequencingProcess](SequencingProcess.md) (mixin)  - A sequencing process linking a sample to sequencing output.
 * [Study](Study.md) (mixin)  - Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

## Referenced by Class


## Attributes


### Own

 * [AccessionMixin➞accession](AccessionMixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)
