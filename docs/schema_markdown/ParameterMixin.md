
# Class: ParameterMixin


Mixin for entities that can have one or more parameters.

URI: [GHGA:ParameterMixin](https://w3id.org/GHGA/ParameterMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Parameter]<parameters%200..*-++[ParameterMixin],[AnalysisMethod]uses%20-.->[ParameterMixin],[Parameter],[AnalysisMethod])](https://yuml.me/diagram/nofunky;dir:TB/class/[Parameter]<parameters%200..*-++[ParameterMixin],[AnalysisMethod]uses%20-.->[ParameterMixin],[Parameter],[AnalysisMethod])

## Mixin for

 * [AnalysisMethod](AnalysisMethod.md) (mixin)  - An Analysis Method captures the workflow steps that were performed to analyze data obtained from an Experiment.

## Referenced by Class


## Attributes


### Own

 * [ParameterMixin➞parameters](ParameterMixin_parameters.md)  <sub>0..\*</sub>
     * Description: Parameter/value pairs corresponding to an entity (e.g., 'aligner' = 'star_salmon',  'hisat2_build_memory' = '200.GB', 'split_fastq' = 50000000).
     * Range: [Parameter](Parameter.md)
