
# Class: SequencingExperiment


A Sequencing Experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.

URI: [GHGA:SequencingExperiment](https://w3id.org/GHGA/SequencingExperiment)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProtocol],[SequencingProcess],[LibraryPreparationProtocol]<library_preparation_protocol%201..1-%20[SequencingExperiment&#124;title:string;description:string;type:string%20%3F;alias:string],[SequencingProtocol]<sequencing_protocol%201..1-%20[SequencingExperiment],[SequencingProcess]-%20sequencing_experiment%201..1>[SequencingExperiment],[Submission]++-%20sequencing_experiments%201..*>[SequencingExperiment],[SequencingProcess]-%20sequencing_experiment(i)%200..1>[SequencingExperiment],[Submission]-%20sequencing_experiments(i)%200..*>[SequencingExperiment],[SequencingExperiment]uses%20-.->[IdentifiedByAliasMixin],[SequencingExperiment]uses%20-.->[AttributeMixin],[LibraryPreparationProtocol],[IdentifiedByAliasMixin],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProtocol],[SequencingProcess],[LibraryPreparationProtocol]<library_preparation_protocol%201..1-%20[SequencingExperiment&#124;title:string;description:string;type:string%20%3F;alias:string],[SequencingProtocol]<sequencing_protocol%201..1-%20[SequencingExperiment],[SequencingProcess]-%20sequencing_experiment%201..1>[SequencingExperiment],[Submission]++-%20sequencing_experiments%201..*>[SequencingExperiment],[SequencingProcess]-%20sequencing_experiment(i)%200..1>[SequencingExperiment],[Submission]-%20sequencing_experiments(i)%200..*>[SequencingExperiment],[SequencingExperiment]uses%20-.->[IdentifiedByAliasMixin],[SequencingExperiment]uses%20-.->[AttributeMixin],[LibraryPreparationProtocol],[IdentifiedByAliasMixin],[AttributeMixin],[Attribute])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[SequencingProcess](SequencingProcess.md)** *[SequencingProcess➞sequencing_experiment](SequencingProcess_sequencing_experiment.md)*  <sub>1..1</sub>  **[SequencingExperiment](SequencingExperiment.md)**
 *  **[Submission](Submission.md)** *[Submission➞sequencing_experiments](Submission_sequencing_experiments.md)*  <sub>1..\*</sub>  **[SequencingExperiment](SequencingExperiment.md)**
 *  **None** *[sequencing_experiment](sequencing_experiment.md)*  <sub>0..1</sub>  **[SequencingExperiment](SequencingExperiment.md)**
 *  **None** *[sequencing_experiments](sequencing_experiments.md)*  <sub>0..\*</sub>  **[SequencingExperiment](SequencingExperiment.md)**

## Attributes


### Own

 * [SequencingExperiment➞title](SequencingExperiment_title.md)  <sub>1..1</sub>
     * Description: The title for this Sequencing Experiment (e.g., GHGAE_PBMC_RNAseq).
     * Range: [String](types/String.md)
 * [SequencingExperiment➞description](SequencingExperiment_description.md)  <sub>1..1</sub>
     * Description: A detailed description of this Sequencing Experiment.
     * Range: [String](types/String.md)
 * [SequencingExperiment➞type](SequencingExperiment_type.md)  <sub>0..1</sub>
     * Description: The type of this Sequencing Experiment.
     * Range: [String](types/String.md)
 * [SequencingExperiment➞sequencing_protocol](SequencingExperiment_sequencing_protocol.md)  <sub>1..1</sub>
     * Description: The Sequencing Protocol associated with this Sequencing Experiment.
     * Range: [SequencingProtocol](SequencingProtocol.md)
 * [SequencingExperiment➞library_preparation_protocol](SequencingExperiment_library_preparation_protocol.md)  <sub>1..1</sub>
     * Description: The Library Preparation Protocol associated with this Sequencing Experiment.
     * Range: [LibraryPreparationProtocol](LibraryPreparationProtocol.md)

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

