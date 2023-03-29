
# Class: sequencing experiment


An sequencing experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/SequencingExperiment](https://w3id.org/GHGA-Submission-Metadata-Schema/SequencingExperiment)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[SequencingProtocol],[SequencingProcess],[LibraryPreparationProtocol]<has%20library%20preparation%20protocol%201..1-%20[SequencingExperiment&#124;type:string%20%3F;title:string%20%3F;description:string;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[SequencingProtocol]<has%20sequencing%20protocol%201..1-%20[SequencingExperiment],[Study]<has%20study%201..1-++[SequencingExperiment],[SequencingProcess]-%20has%20sequencing%20experiment(i)%200..1>[SequencingExperiment],[Submission]-%20has%20sequencing%20experiment(i)%200..1>[SequencingExperiment],[SequencingProcess]-%20has%20sequencing%20experiment%201..1>[SequencingExperiment],[Submission]++-%20has%20sequencing%20experiment%200..*>[SequencingExperiment],[SequencingExperiment]uses%20-.->[AttributeMixin],[SequencingExperiment]uses%20-.->[AccessionMixin],[SequencingExperiment]uses%20-.->[EgaAccessionMixin],[Investigation]^-[SequencingExperiment],[LibraryPreparationProtocol],[Investigation],[EgaAccessionMixin],[AttributeMixin],[Attribute],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[SequencingProtocol],[SequencingProcess],[LibraryPreparationProtocol]<has%20library%20preparation%20protocol%201..1-%20[SequencingExperiment&#124;type:string%20%3F;title:string%20%3F;description:string;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[SequencingProtocol]<has%20sequencing%20protocol%201..1-%20[SequencingExperiment],[Study]<has%20study%201..1-++[SequencingExperiment],[SequencingProcess]-%20has%20sequencing%20experiment(i)%200..1>[SequencingExperiment],[Submission]-%20has%20sequencing%20experiment(i)%200..1>[SequencingExperiment],[SequencingProcess]-%20has%20sequencing%20experiment%201..1>[SequencingExperiment],[Submission]++-%20has%20sequencing%20experiment%200..*>[SequencingExperiment],[SequencingExperiment]uses%20-.->[AttributeMixin],[SequencingExperiment]uses%20-.->[AccessionMixin],[SequencingExperiment]uses%20-.->[EgaAccessionMixin],[Investigation]^-[SequencingExperiment],[LibraryPreparationProtocol],[Investigation],[EgaAccessionMixin],[AttributeMixin],[Attribute],[AccessionMixin])

## Parents

 *  is_a: [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.

## Uses Mixin

 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.
 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an EGA accession, in addition to GHGA accession.

## Referenced by Class

 *  **None** *[has sequencing experiment](has_sequencing_experiment.md)*  <sub>0..1</sub>  **[SequencingExperiment](SequencingExperiment.md)**
 *  **[SequencingProcess](SequencingProcess.md)** *[sequencing process➞has sequencing experiment](sequencing_process_has_sequencing_experiment.md)*  <sub>1..1</sub>  **[SequencingExperiment](SequencingExperiment.md)**
 *  **[Submission](Submission.md)** *[submission➞has sequencing experiment](submission_has_sequencing_experiment.md)*  <sub>0..\*</sub>  **[SequencingExperiment](SequencingExperiment.md)**

## Attributes


### Own

 * [sequencing experiment➞type](sequencing_experiment_type.md)  <sub>0..1</sub>
     * Description: The type of sequencing experiment.
     * Range: [String](types/String.md)
 * [sequencing experiment➞has study](sequencing_experiment_has_study.md)  <sub>1..1</sub>
     * Description: The Study entity associated with this Experiment.
     * Range: [Study](Study.md)
 * [sequencing experiment➞has sequencing protocol](sequencing_experiment_has_sequencing_protocol.md)  <sub>1..1</sub>
     * Description: The sequencing protocol associated with an entity.
     * Range: [SequencingProtocol](SequencingProtocol.md)
 * [sequencing experiment➞has library preparation protocol](sequencing_experiment_has_library_preparation_protocol.md)  <sub>1..1</sub>
     * Description: The Library Preparation Protocol associated with an entity.
     * Range: [LibraryPreparationProtocol](LibraryPreparationProtocol.md)
 * [sequencing experiment➞title](sequencing_experiment_title.md)  <sub>0..1</sub>
     * Description: Name for the experiment (eg: GHGAE_PBMC_RNAseq).
     * Range: [String](types/String.md)
 * [sequencing experiment➞description](sequencing_experiment_description.md)  <sub>1..1</sub>
     * Description: A detailed description of the Experiment.
     * Range: [String](types/String.md)

### Inherited from investigation:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞alias](named_thing_alias.md)  <sub>1..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞xref](named_thing_xref.md)  <sub>0..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)

### Mixed in from attribute mixin:

 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

### Mixed in from accession mixin:

 * [accession mixin➞accession](accession_mixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

### Mixed in from ega accession mixin:

 * [ega accession mixin➞ega accession](ega_accession_mixin_ega_accession.md)  <sub>1..1</sub>
     * Description: A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:000994 |

