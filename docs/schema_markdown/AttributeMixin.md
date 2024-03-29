
# Class: AttributeMixin


Mixin for entities that can have one or more attributes.

URI: [GHGA:AttributeMixin](https://w3id.org/GHGA/AttributeMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Attribute]<attributes%200..*-++[AttributeMixin],[Study]uses%20-.->[AttributeMixin],[SequencingProtocol]uses%20-.->[AttributeMixin],[SequencingProcess]uses%20-.->[AttributeMixin],[SequencingExperiment]uses%20-.->[AttributeMixin],[Sample]uses%20-.->[AttributeMixin],[LibraryPreparationProtocol]uses%20-.->[AttributeMixin],[Condition]uses%20-.->[AttributeMixin],[Study],[SequencingProtocol],[SequencingProcess],[SequencingExperiment],[Sample],[LibraryPreparationProtocol],[Condition],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Attribute]<attributes%200..*-++[AttributeMixin],[Study]uses%20-.->[AttributeMixin],[SequencingProtocol]uses%20-.->[AttributeMixin],[SequencingProcess]uses%20-.->[AttributeMixin],[SequencingExperiment]uses%20-.->[AttributeMixin],[Sample]uses%20-.->[AttributeMixin],[LibraryPreparationProtocol]uses%20-.->[AttributeMixin],[Condition]uses%20-.->[AttributeMixin],[Study],[SequencingProtocol],[SequencingProcess],[SequencingExperiment],[Sample],[LibraryPreparationProtocol],[Condition],[Attribute])

## Mixin for

 * [Condition](Condition.md) (mixin)  - A Condition specifies which special characteristics and treatments apply to a Sample (e.g., whether the Sample comes from a disease or a healthy tissue).
 * [LibraryPreparationProtocol](LibraryPreparationProtocol.md) (mixin)  - The Library Preparation Protocol captures information about the library preparation of a Sequencing Experiment.
 * [Sample](Sample.md) (mixin)  - A Sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use.  It is prepared from a Biospecimen.
 * [SequencingExperiment](SequencingExperiment.md) (mixin)  - A Sequencing Experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
 * [SequencingProcess](SequencingProcess.md) (mixin)  - The Sequencing Process captures the technical parameters that were used to produce sequencing output from the Sample. It links the Sample to sequencing output.
 * [SequencingProtocol](SequencingProtocol.md) (mixin)  - The Sequencing Protocol captures information about parameters and metadata associated with a Sequencing Experiment.
 * [Study](Study.md) (mixin)  - A Study is an experimental investigation of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

## Referenced by Class


## Attributes


### Own

 * [AttributeMixin➞attributes](AttributeMixin_attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
