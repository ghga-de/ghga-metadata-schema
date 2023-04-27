
# Class: IdentifiedByAliasMixin




URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/IdentifiedByAliasMixin](https://w3id.org/GHGA-Submission-Metadata-Schema/IdentifiedByAliasMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]uses%20-.->[IdentifiedByAliasMixin&#124;alias:string],[SequencingProtocol]uses%20-.->[IdentifiedByAliasMixin],[SequencingProcess]uses%20-.->[IdentifiedByAliasMixin],[SequencingExperiment]uses%20-.->[IdentifiedByAliasMixin],[LibraryPreparationProtocol]uses%20-.->[IdentifiedByAliasMixin],[Condition]uses%20-.->[IdentifiedByAliasMixin],[Biospecimen]uses%20-.->[IdentifiedByAliasMixin],[AliasMixin]^-[IdentifiedByAliasMixin],[Study],[SequencingProtocol],[SequencingProcess],[SequencingExperiment],[LibraryPreparationProtocol],[Condition],[Biospecimen],[AliasMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]uses%20-.->[IdentifiedByAliasMixin&#124;alias:string],[SequencingProtocol]uses%20-.->[IdentifiedByAliasMixin],[SequencingProcess]uses%20-.->[IdentifiedByAliasMixin],[SequencingExperiment]uses%20-.->[IdentifiedByAliasMixin],[LibraryPreparationProtocol]uses%20-.->[IdentifiedByAliasMixin],[Condition]uses%20-.->[IdentifiedByAliasMixin],[Biospecimen]uses%20-.->[IdentifiedByAliasMixin],[AliasMixin]^-[IdentifiedByAliasMixin],[Study],[SequencingProtocol],[SequencingProcess],[SequencingExperiment],[LibraryPreparationProtocol],[Condition],[Biospecimen],[AliasMixin])

## Parents

 *  is_a: [AliasMixin](AliasMixin.md) - Mixin for entities that can be assigned an alias at the time of metadata submission.

## Mixin for

 * [Biospecimen](Biospecimen.md) (mixin)  - A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics, treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is derived.
 * [Condition](Condition.md) (mixin)  - An condition that is linked to comparable samples.
 * [LibraryPreparationProtocol](LibraryPreparationProtocol.md) (mixin)  - Information about the library_preparation of an sequencing experiment.
 * [SequencingExperiment](SequencingExperiment.md) (mixin)  - An sequencing experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
 * [SequencingProcess](SequencingProcess.md) (mixin)  - A sequencing process linking a sample to sequencing output.
 * [SequencingProtocol](SequencingProtocol.md) (mixin)  - Information about the sequencing of a sample.
 * [Study](Study.md) (mixin)  - Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

## Referenced by Class


## Attributes


### Own

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
