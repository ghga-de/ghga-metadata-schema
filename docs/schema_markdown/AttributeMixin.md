
# Class: AttributeMixin


Mixin for entities that can have one or more attributes.

URI: [GHGA:AttributeMixin](https://w3id.org/GHGA/AttributeMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Attribute]<attributes%200..*-++[AttributeMixin],[Study]uses%20-.->[AttributeMixin],[SequencingProtocol]uses%20-.->[AttributeMixin],[SequencingProcess]uses%20-.->[AttributeMixin],[SequencingExperiment]uses%20-.->[AttributeMixin],[Sample]uses%20-.->[AttributeMixin],[LibraryPreparationProtocol]uses%20-.->[AttributeMixin],[Condition]uses%20-.->[AttributeMixin],[Study],[SequencingProtocol],[SequencingProcess],[SequencingExperiment],[Sample],[LibraryPreparationProtocol],[Condition],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Attribute]<attributes%200..*-++[AttributeMixin],[Study]uses%20-.->[AttributeMixin],[SequencingProtocol]uses%20-.->[AttributeMixin],[SequencingProcess]uses%20-.->[AttributeMixin],[SequencingExperiment]uses%20-.->[AttributeMixin],[Sample]uses%20-.->[AttributeMixin],[LibraryPreparationProtocol]uses%20-.->[AttributeMixin],[Condition]uses%20-.->[AttributeMixin],[Study],[SequencingProtocol],[SequencingProcess],[SequencingExperiment],[Sample],[LibraryPreparationProtocol],[Condition],[Attribute])

## Mixin for

 * [Condition](Condition.md) (mixin)  - An condition that is linked to comparable samples.
 * [LibraryPreparationProtocol](LibraryPreparationProtocol.md) (mixin)  - Information about the library_preparation of an sequencing experiment.
 * [Sample](Sample.md) (mixin)  - A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).
 * [SequencingExperiment](SequencingExperiment.md) (mixin)  - An sequencing experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
 * [SequencingProcess](SequencingProcess.md) (mixin)  - A sequencing process linking a sample to sequencing output.
 * [SequencingProtocol](SequencingProtocol.md) (mixin)  - Information about the sequencing of a sample.
 * [Study](Study.md) (mixin)  - Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

## Referenced by Class


## Attributes


### Own

 * [AttributeMixin➞attributes](AttributeMixin_attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
