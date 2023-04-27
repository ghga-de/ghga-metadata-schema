
# Class: SequencingExperiment


An sequencing experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/SequencingExperiment](https://w3id.org/GHGA-Submission-Metadata-Schema/SequencingExperiment)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProtocol],[SequencingProcess],[LibraryPreparationProtocol]<library_preparation_protocol%201..1-++[SequencingExperiment&#124;type:string%20%3F;title:string%20%3F;description:string;alias:string],[SequencingProtocol]<sequencing_protocol%201..1-++[SequencingExperiment],[SequencingProcess]-%20sequencing_experiment%201..1>[SequencingExperiment],[Submission]++-%20sequencing_experiments%200..*>[SequencingExperiment],[SequencingProcess]-%20sequencing_experiment(i)%200..1>[SequencingExperiment],[Submission]-%20sequencing_experiments(i)%200..*>[SequencingExperiment],[SequencingExperiment]uses%20-.->[IdentifiedByAliasMixin],[SequencingExperiment]uses%20-.->[AttributeMixin],[Investigation]^-[SequencingExperiment],[LibraryPreparationProtocol],[Investigation],[IdentifiedByAliasMixin],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProtocol],[SequencingProcess],[LibraryPreparationProtocol]<library_preparation_protocol%201..1-++[SequencingExperiment&#124;type:string%20%3F;title:string%20%3F;description:string;alias:string],[SequencingProtocol]<sequencing_protocol%201..1-++[SequencingExperiment],[SequencingProcess]-%20sequencing_experiment%201..1>[SequencingExperiment],[Submission]++-%20sequencing_experiments%200..*>[SequencingExperiment],[SequencingProcess]-%20sequencing_experiment(i)%200..1>[SequencingExperiment],[Submission]-%20sequencing_experiments(i)%200..*>[SequencingExperiment],[SequencingExperiment]uses%20-.->[IdentifiedByAliasMixin],[SequencingExperiment]uses%20-.->[AttributeMixin],[Investigation]^-[SequencingExperiment],[LibraryPreparationProtocol],[Investigation],[IdentifiedByAliasMixin],[AttributeMixin],[Attribute])

## Parents

 *  is_a: [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[SequencingProcess](SequencingProcess.md)** *[SequencingProcess➞sequencing_experiment](SequencingProcess_sequencing_experiment.md)*  <sub>1..1</sub>  **[SequencingExperiment](SequencingExperiment.md)**
 *  **[Submission](Submission.md)** *[Submission➞sequencing_experiments](Submission_sequencing_experiments.md)*  <sub>0..\*</sub>  **[SequencingExperiment](SequencingExperiment.md)**
 *  **None** *[sequencing_experiment](sequencing_experiment.md)*  <sub>0..1</sub>  **[SequencingExperiment](SequencingExperiment.md)**
 *  **None** *[sequencing_experiments](sequencing_experiments.md)*  <sub>0..\*</sub>  **[SequencingExperiment](SequencingExperiment.md)**

## Attributes


### Own

 * [SequencingExperiment➞type](SequencingExperiment_type.md)  <sub>0..1</sub>
     * Description: The type of sequencing experiment.
     * Range: [String](types/String.md)
 * [SequencingExperiment➞sequencing_protocol](SequencingExperiment_sequencing_protocol.md)  <sub>1..1</sub>
     * Description: The sequencing protocol associated with an entity.
     * Range: [SequencingProtocol](SequencingProtocol.md)
 * [SequencingExperiment➞library_preparation_protocol](SequencingExperiment_library_preparation_protocol.md)  <sub>1..1</sub>
     * Description: The library_preparation Protocol associated with an entity.
     * Range: [LibraryPreparationProtocol](LibraryPreparationProtocol.md)
 * [SequencingExperiment➞title](SequencingExperiment_title.md)  <sub>0..1</sub>
     * Description: Name for the experiment (eg: GHGAE_PBMC_RNAseq).
     * Range: [String](types/String.md)
 * [SequencingExperiment➞description](SequencingExperiment_description.md)  <sub>1..1</sub>
     * Description: A detailed description of the Experiment.
     * Range: [String](types/String.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
     * in subsets: (restricted)

### Mixed in from AttributeMixin:

 * [attributes](attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:000994 |

