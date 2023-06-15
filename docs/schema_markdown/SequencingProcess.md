
# Class: SequencingProcess


A sequencing process linking a sample to sequencing output.

URI: [GHGA:SequencingProcess](https://w3id.org/GHGA/SequencingProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProcessFile],[Sample]<sample%201..1-%20[SequencingProcess&#124;title:string%20%3F;description:string;name:string;sequencing_run_id:string%20%3F;sequencing_lane_id:string%20%3F;sequencing_machine_id:string%20%3F;alias:string],[SequencingExperiment]<sequencing_experiment%201..1-%20[SequencingProcess],[SequencingProcessFile]-%20sequencing_process%201..1>[SequencingProcess],[Submission]++-%20sequencing_processes%201..*>[SequencingProcess],[SequencingProcessFile]-%20sequencing_process(i)%200..1>[SequencingProcess],[Submission]-%20sequencing_processes(i)%200..*>[SequencingProcess],[SequencingProcess]uses%20-.->[IdentifiedByAliasMixin],[SequencingProcess]uses%20-.->[AttributeMixin],[SequencingExperiment],[Sample],[IdentifiedByAliasMixin],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProcessFile],[Sample]<sample%201..1-%20[SequencingProcess&#124;title:string%20%3F;description:string;name:string;sequencing_run_id:string%20%3F;sequencing_lane_id:string%20%3F;sequencing_machine_id:string%20%3F;alias:string],[SequencingExperiment]<sequencing_experiment%201..1-%20[SequencingProcess],[SequencingProcessFile]-%20sequencing_process%201..1>[SequencingProcess],[Submission]++-%20sequencing_processes%201..*>[SequencingProcess],[SequencingProcessFile]-%20sequencing_process(i)%200..1>[SequencingProcess],[Submission]-%20sequencing_processes(i)%200..*>[SequencingProcess],[SequencingProcess]uses%20-.->[IdentifiedByAliasMixin],[SequencingProcess]uses%20-.->[AttributeMixin],[SequencingExperiment],[Sample],[IdentifiedByAliasMixin],[AttributeMixin],[Attribute])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[SequencingProcessFile](SequencingProcessFile.md)** *[SequencingProcessFile➞sequencing_process](SequencingProcessFile_sequencing_process.md)*  <sub>1..1</sub>  **[SequencingProcess](SequencingProcess.md)**
 *  **[Submission](Submission.md)** *[Submission➞sequencing_processes](Submission_sequencing_processes.md)*  <sub>1..\*</sub>  **[SequencingProcess](SequencingProcess.md)**
 *  **None** *[sequencing_process](sequencing_process.md)*  <sub>0..1</sub>  **[SequencingProcess](SequencingProcess.md)**
 *  **None** *[sequencing_processes](sequencing_processes.md)*  <sub>0..\*</sub>  **[SequencingProcess](SequencingProcess.md)**

## Attributes


### Own

 * [title](title.md)  <sub>0..1</sub>
     * Description: The title that describes an entity.
     * Range: [String](types/String.md)
 * [SequencingProcess➞description](SequencingProcess_description.md)  <sub>1..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)
 * [SequencingProcess➞name](SequencingProcess_name.md)  <sub>1..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)
 * [SequencingProcess➞sequencing_run_id](SequencingProcess_sequencing_run_id.md)  <sub>0..1</sub>
     * Description: Identifier of the sequencing run. Used for batch correction.
     * Range: [String](types/String.md)
 * [SequencingProcess➞sequencing_lane_id](SequencingProcess_sequencing_lane_id.md)  <sub>0..1</sub>
     * Description: Identifier of the sequencing lane. Used for batch correction.
     * Range: [String](types/String.md)
 * [SequencingProcess➞sequencing_machine_id](SequencingProcess_sequencing_machine_id.md)  <sub>0..1</sub>
     * Description: Identifier of the sequencing machine. Used for batch correction.
     * Range: [String](types/String.md)
 * [SequencingProcess➞sequencing_experiment](SequencingProcess_sequencing_experiment.md)  <sub>1..1</sub>
     * Description: The sequencing experiment associated with an entity.
     * Range: [SequencingExperiment](SequencingExperiment.md)
 * [SequencingProcess➞sample](SequencingProcess_sample.md)  <sub>1..1</sub>
     * Description: The sample associated with an entity.
     * Range: [Sample](Sample.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)

### Mixed in from AttributeMixin:

 * [AttributeMixin➞attributes](AttributeMixin_attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
