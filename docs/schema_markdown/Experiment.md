
# Class: Experiment


An Experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.

URI: [GHGA:Experiment](https://w3id.org/GHGA/Experiment)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample],[ResearchDataFile],[IdentifiedByAliasMixin],[ExperimentMethod],[Sample]<sample%201..1-%20[Experiment&#124;title:string;description:string%20%3F;type:string%20%3F;ega_accession:string%20%3F;alias:string],[ExperimentMethod]<experiment_method%201..1-%20[Experiment],[ResearchDataFile]-%20experiments%201..*>[Experiment],[Submission]++-%20experiments%201..*>[Experiment],[ResearchDataFile]-%20experiments(i)%200..*>[Experiment],[Submission]-%20experiments(i)%200..*>[Experiment],[Experiment]uses%20-.->[IdentifiedByAliasMixin],[Experiment]uses%20-.->[AttributeMixin],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample],[ResearchDataFile],[IdentifiedByAliasMixin],[ExperimentMethod],[Sample]<sample%201..1-%20[Experiment&#124;title:string;description:string%20%3F;type:string%20%3F;ega_accession:string%20%3F;alias:string],[ExperimentMethod]<experiment_method%201..1-%20[Experiment],[ResearchDataFile]-%20experiments%201..*>[Experiment],[Submission]++-%20experiments%201..*>[Experiment],[ResearchDataFile]-%20experiments(i)%200..*>[Experiment],[Submission]-%20experiments(i)%200..*>[Experiment],[Experiment]uses%20-.->[IdentifiedByAliasMixin],[Experiment]uses%20-.->[AttributeMixin],[AttributeMixin],[Attribute])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[ResearchDataFile](ResearchDataFile.md)** *[ResearchDataFile➞experiments](ResearchDataFile_experiments.md)*  <sub>1..\*</sub>  **[Experiment](Experiment.md)**
 *  **[Submission](Submission.md)** *[Submission➞experiments](Submission_experiments.md)*  <sub>1..\*</sub>  **[Experiment](Experiment.md)**
 *  **None** *[experiments](experiments.md)*  <sub>0..\*</sub>  **[Experiment](Experiment.md)**

## Attributes


### Own

 * [Experiment➞experiment_method](Experiment_experiment_method.md)  <sub>1..1</sub>
     * Description: The alias of one or more Experiment Methods that are associated with this Experiment.
     * Range: [ExperimentMethod](ExperimentMethod.md)
 * [Experiment➞title](Experiment_title.md)  <sub>1..1</sub>
     * Description: The title for this Experiment (e.g., GHGAE_PBMC_RNAseq).
     * Range: [String](types/String.md)
 * [Experiment➞description](Experiment_description.md)  <sub>0..1</sub>
     * Description: A detailed description of this Experiment.
     * Range: [String](types/String.md)
 * [Experiment➞type](Experiment_type.md)  <sub>0..1</sub>
     * Description: The type of this Experiment.
     * Range: [String](types/String.md)
 * [Experiment➞ega_accession](Experiment_ega_accession.md)  <sub>0..1</sub>
     * Description: The EGA accession of the 'Run' entity (EGAR).
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

