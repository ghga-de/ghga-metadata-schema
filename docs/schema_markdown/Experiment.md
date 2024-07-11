
# Class: Experiment


An Experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.

URI: [GHGA:Experiment](https://w3id.org/GHGA/Experiment)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample],[ResearchDataFile],[IdentifiedByAliasMixin],[ExperimentalMethod],[Sample]<sample%201..1-%20[Experiment&#124;title:string;description:string;type:string%20%3F;ega_accession:string%20%3F;alias:string],[ExperimentalMethod]<experimental_method%201..1-%20[Experiment],[ResearchDataFile]-%20experiment%201..*>[Experiment],[Submission]++-%20experiments%201..*>[Experiment],[ResearchDataFile]-%20experiment(i)%200..1>[Experiment],[Submission]-%20experiments(i)%200..*>[Experiment],[Experiment]uses%20-.->[IdentifiedByAliasMixin],[Experiment]uses%20-.->[AttributeMixin],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample],[ResearchDataFile],[IdentifiedByAliasMixin],[ExperimentalMethod],[Sample]<sample%201..1-%20[Experiment&#124;title:string;description:string;type:string%20%3F;ega_accession:string%20%3F;alias:string],[ExperimentalMethod]<experimental_method%201..1-%20[Experiment],[ResearchDataFile]-%20experiment%201..*>[Experiment],[Submission]++-%20experiments%201..*>[Experiment],[ResearchDataFile]-%20experiment(i)%200..1>[Experiment],[Submission]-%20experiments(i)%200..*>[Experiment],[Experiment]uses%20-.->[IdentifiedByAliasMixin],[Experiment]uses%20-.->[AttributeMixin],[AttributeMixin],[Attribute])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[ResearchDataFile](ResearchDataFile.md)** *[ResearchDataFile➞experiment](ResearchDataFile_experiment.md)*  <sub>1..\*</sub>  **[Experiment](Experiment.md)**
 *  **[Submission](Submission.md)** *[Submission➞experiments](Submission_experiments.md)*  <sub>1..\*</sub>  **[Experiment](Experiment.md)**
 *  **None** *[experiment](experiment.md)*  <sub>0..1</sub>  **[Experiment](Experiment.md)**
 *  **None** *[experiments](experiments.md)*  <sub>0..\*</sub>  **[Experiment](Experiment.md)**

## Attributes


### Own

 * [Experiment➞experimental_method](Experiment_experimental_method.md)  <sub>1..1</sub>
     * Description: The alias of one or more Experimental Methods that are associated with this Experiment.
     * Range: [ExperimentalMethod](ExperimentalMethod.md)
 * [Experiment➞title](Experiment_title.md)  <sub>1..1</sub>
     * Description: The title for this Sequencing Experiment (e.g., GHGAE_PBMC_RNAseq).
     * Range: [String](types/String.md)
 * [Experiment➞description](Experiment_description.md)  <sub>1..1</sub>
     * Description: A detailed description of this Sequencing Experiment.
     * Range: [String](types/String.md)
 * [Experiment➞type](Experiment_type.md)  <sub>0..1</sub>
     * Description: The type of this Sequencing Experiment.
     * Range: [String](types/String.md)
 * [Experiment➞ega_accession](Experiment_ega_accession.md)  <sub>0..1</sub>
     * Description: The EGA accession ID of an entity.
     * Range: [String](types/String.md)
 * [Experiment➞sample](Experiment_sample.md)  <sub>1..1</sub>
     * Description: The alias of one or more Samples that are associated with this Experiment.
     * Range: [Sample](Sample.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)

### Mixed in from AttributeMixin:

 * [AttributeMixin➞attributes](AttributeMixin_attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:000994 |

