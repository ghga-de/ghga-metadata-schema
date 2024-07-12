
# Class: SoftwareVersionMixin


Mixin for entities that can have one or more software versions.

URI: [GHGA:SoftwareVersionMixin](https://w3id.org/GHGA/SoftwareVersionMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SoftwareVersion]<software_versions%200..1-++[SoftwareVersionMixin],[AnalysisMethod]uses%20-.->[SoftwareVersionMixin],[SoftwareVersion],[AnalysisMethod])](https://yuml.me/diagram/nofunky;dir:TB/class/[SoftwareVersion]<software_versions%200..1-++[SoftwareVersionMixin],[AnalysisMethod]uses%20-.->[SoftwareVersionMixin],[SoftwareVersion],[AnalysisMethod])

## Mixin for

 * [AnalysisMethod](AnalysisMethod.md) (mixin)  - An Analysis Method captures the workflow steps that were performed to analyze data obtained from an Experiment.

## Referenced by Class


## Attributes


### Own

 * [SoftwareVersionMixin➞software_versions](SoftwareVersionMixin_software_versions.md)  <sub>0..1</sub>
     * Description: Software/version pairs corresponding to an entity.
     * Range: [SoftwareVersion](SoftwareVersion.md)
