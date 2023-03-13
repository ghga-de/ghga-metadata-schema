
# Class: attribute mixin


Mixin for entities that can have one or more attributes.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/AttributeMixin](https://w3id.org/GHGA-Submission-Metadata-Schema/AttributeMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Attribute]<has%20attribute%200..*-++[AttributeMixin],[Study]uses%20-.->[AttributeMixin],[Sample]uses%20-.->[AttributeMixin],[Protocol]uses%20-.->[AttributeMixin],[Project]uses%20-.->[AttributeMixin],[File]uses%20-.->[AttributeMixin],[Experiment]uses%20-.->[AttributeMixin],[Dataset]uses%20-.->[AttributeMixin],[DataAccessPolicy]uses%20-.->[AttributeMixin],[DataAccessCommittee]uses%20-.->[AttributeMixin],[Study],[Sample],[Protocol],[Project],[File],[Experiment],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Attribute]<has%20attribute%200..*-++[AttributeMixin],[Study]uses%20-.->[AttributeMixin],[Sample]uses%20-.->[AttributeMixin],[Protocol]uses%20-.->[AttributeMixin],[Project]uses%20-.->[AttributeMixin],[File]uses%20-.->[AttributeMixin],[Experiment]uses%20-.->[AttributeMixin],[Dataset]uses%20-.->[AttributeMixin],[DataAccessPolicy]uses%20-.->[AttributeMixin],[DataAccessCommittee]uses%20-.->[AttributeMixin],[Study],[Sample],[Protocol],[Project],[File],[Experiment],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Attribute])

## Mixin for

 * [DataAccessCommittee](DataAccessCommittee.md) (mixin)  - A group of members that are delegated to grant access to one or more datasets after ensuring the minimum criteria for data sharing has been met, and request for data use does not raise ethical and/or legal concerns.
 * [DataAccessPolicy](DataAccessPolicy.md) (mixin)  - A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.
 * [Dataset](Dataset.md) (mixin)  - A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
 * [Experiment](Experiment.md) (mixin)  - An experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
 * [File](File.md) (mixin)  - A file is an object that contains information generated from a process, either an Experiment or an Analysis.
 * [Project](Project.md) (mixin)  - A high level organization for a collection of studies based on a research proposal that aims to achieve certain goals.
 * [Protocol](Protocol.md) (mixin)  - A plan specification which has sufficient level of detail and quantitative information to communicate it between investigation agents, so that different investigation agents will reliably be able to independently reproduce the process.
 * [Sample](Sample.md) (mixin)  - A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).
 * [Study](Study.md) (mixin)  - Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

## Referenced by Class


## Attributes


### Own

 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)
