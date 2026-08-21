
# Class: AttributeMixin


Mixin for entities that can have one or more attributes.

URI: [GHGA:AttributeMixin](https://w3id.org/GHGA/AttributeMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Attribute]<attributes%200..*-++[AttributeMixin],[Study]uses%20-.->[AttributeMixin],[Sample]uses%20-.->[AttributeMixin],[File]uses%20-.->[AttributeMixin],[ExperimentMethod]uses%20-.->[AttributeMixin],[Experiment]uses%20-.->[AttributeMixin],[AnalysisMethod]uses%20-.->[AttributeMixin],[Study],[Sample],[File],[ExperimentMethod],[Experiment],[Attribute],[AnalysisMethod])](https://yuml.me/diagram/nofunky;dir:TB/class/[Attribute]<attributes%200..*-++[AttributeMixin],[Study]uses%20-.->[AttributeMixin],[Sample]uses%20-.->[AttributeMixin],[File]uses%20-.->[AttributeMixin],[ExperimentMethod]uses%20-.->[AttributeMixin],[Experiment]uses%20-.->[AttributeMixin],[AnalysisMethod]uses%20-.->[AttributeMixin],[Study],[Sample],[File],[ExperimentMethod],[Experiment],[Attribute],[AnalysisMethod])

## Mixin for

 * [AnalysisMethod](AnalysisMethod.md) (mixin)  - An Analysis Method captures the workflow steps that were performed to analyze data obtained from an Experiment.
 * [Experiment](Experiment.md) (mixin)  - An Experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
 * [ExperimentMethod](ExperimentMethod.md) (mixin)  - The Experiment Method captures technical metadata describing the parameters used to generate output from the Sample.
 * [File](File.md) (mixin)  - A file is an object that contains information generated from a process, either an Experiment or an Analysis.
 * [Sample](Sample.md) (mixin)  - A Sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use.  It is prepared from a Biospecimen.
 * [Study](Study.md) (mixin)  - A Study is an experimental investigation of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

## Referenced by Class


## Attributes


### Own

 * [AttributeMixin➞attributes](AttributeMixin_attributes.md)  <sub>0..\*</sub>
     * Description: Semicolon-separated key=value pairs associated with the entity (e.g., key=value; key2=value2).
     * Range: [Attribute](Attribute.md)
