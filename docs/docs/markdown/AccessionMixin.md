
# Class: accession mixin


Mixin for entities that can be assigned a GHGA accession.

URI: [GHGA:AccessionMixin](https://w3id.org/GHGA/AccessionMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]uses%20-.->[AccessionMixin&#124;accession:string],[Sample]uses%20-.->[AccessionMixin],[Project]uses%20-.->[AccessionMixin],[Individual]uses%20-.->[AccessionMixin],[File]uses%20-.->[AccessionMixin],[Family]uses%20-.->[AccessionMixin],[Experiment]uses%20-.->[AccessionMixin],[Dataset]uses%20-.->[AccessionMixin],[DataAccessPolicy]uses%20-.->[AccessionMixin],[DataAccessCommittee]uses%20-.->[AccessionMixin],[Cohort]uses%20-.->[AccessionMixin],[Biospecimen]uses%20-.->[AccessionMixin],[Analysis]uses%20-.->[AccessionMixin],[Study],[Sample],[Project],[Individual],[File],[Family],[Experiment],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Cohort],[Biospecimen],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]uses%20-.->[AccessionMixin&#124;accession:string],[Sample]uses%20-.->[AccessionMixin],[Project]uses%20-.->[AccessionMixin],[Individual]uses%20-.->[AccessionMixin],[File]uses%20-.->[AccessionMixin],[Family]uses%20-.->[AccessionMixin],[Experiment]uses%20-.->[AccessionMixin],[Dataset]uses%20-.->[AccessionMixin],[DataAccessPolicy]uses%20-.->[AccessionMixin],[DataAccessCommittee]uses%20-.->[AccessionMixin],[Cohort]uses%20-.->[AccessionMixin],[Biospecimen]uses%20-.->[AccessionMixin],[Analysis]uses%20-.->[AccessionMixin],[Study],[Sample],[Project],[Individual],[File],[Family],[Experiment],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Cohort],[Biospecimen],[Analysis])

## Mixin for

 * [Analysis](Analysis.md) (mixin)  - An Analysis is a data transformation that transforms input data to output data. The workflow used to achieve this transformation and the individual steps are also captured.
 * [Biospecimen](Biospecimen.md) (mixin)  - A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics, treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is derived.
 * [Cohort](Cohort.md) (mixin)  - A cohort is a collection of individuals that share a common characteristic/observation and have been grouped together for a research study/investigation.
 * [DataAccessCommittee](DataAccessCommittee.md) (mixin)  - A group of members that are delegated to grant access to one or more datasets after ensuring the minimum criteria for data sharing has been met, and request for data use does not raise ethical and/or legal concerns.
 * [DataAccessPolicy](DataAccessPolicy.md) (mixin)  - A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.
 * [Dataset](Dataset.md) (mixin)  - A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
 * [Experiment](Experiment.md) (mixin)  - An experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
 * [Family](Family.md) (mixin)  - A domestic group, or a number of domestic groups linked through descent (demonstrated or stipulated) from a common ancestor, marriage, or adoption.
 * [File](File.md) (mixin)  - A file is an object that contains information generated from a process, either an Experiment or an Analysis.
 * [Individual](Individual.md) (mixin)  - An Individual is a Person who is participating in a Study.
 * [Project](Project.md) (mixin)  - A high level organization for a collection of studies based on a research proposal that aims to achieve certain goals.
 * [Sample](Sample.md) (mixin)  - A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).
 * [Study](Study.md) (mixin)  - Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

## Referenced by Class


## Attributes


### Own

 * [accession mixin➞accession](accession_mixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)
