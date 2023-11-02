
# Class: SequencingProcess


The Sequencing Process captures the technical parameters that were used to produce sequencing output from a Sample. It links a Sample to sequencing output.

URI: [GHGA:SequencingProcess](https://w3id.org/GHGA/SequencingProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProcessFile],[Sample]<sample%201..1-%20[SequencingProcess&#124;name:string;description:string;sequencing_run_id:string%20%3F;sequencing_lane_id:string%20%3F;sequencing_machine_id:string%20%3F;index_sequence:string%20%3F;alias:string],[SequencingExperiment]<sequencing_experiment%201..1-%20[SequencingProcess],[SequencingProcessFile]-%20sequencing_process%201..1>[SequencingProcess],[Submission]++-%20sequencing_processes%201..*>[SequencingProcess],[SequencingProcessFile]-%20sequencing_process(i)%200..1>[SequencingProcess],[Submission]-%20sequencing_processes(i)%200..*>[SequencingProcess],[SequencingProcess]uses%20-.->[IdentifiedByAliasMixin],[SequencingProcess]uses%20-.->[AttributeMixin],[SequencingExperiment],[Sample],[IdentifiedByAliasMixin],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProcessFile],[Sample]<sample%201..1-%20[SequencingProcess&#124;name:string;description:string;sequencing_run_id:string%20%3F;sequencing_lane_id:string%20%3F;sequencing_machine_id:string%20%3F;index_sequence:string%20%3F;alias:string],[SequencingExperiment]<sequencing_experiment%201..1-%20[SequencingProcess],[SequencingProcessFile]-%20sequencing_process%201..1>[SequencingProcess],[Submission]++-%20sequencing_processes%201..*>[SequencingProcess],[SequencingProcessFile]-%20sequencing_process(i)%200..1>[SequencingProcess],[Submission]-%20sequencing_processes(i)%200..*>[SequencingProcess],[SequencingProcess]uses%20-.->[IdentifiedByAliasMixin],[SequencingProcess]uses%20-.->[AttributeMixin],[SequencingExperiment],[Sample],[IdentifiedByAliasMixin],[AttributeMixin],[Attribute])

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

 * [SequencingProcess➞name](SequencingProcess_name.md)  <sub>1..1</sub>
     * Description: A short name identifying the Sequencing Process to potential users.
     * Range: [String](types/String.md)
 * [SequencingProcess➞description](SequencingProcess_description.md)  <sub>1..1</sub>
     * Description: A short description of the Sequencing Process.
     * Range: [String](types/String.md)
 * [SequencingProcess➞sequencing_run_id](SequencingProcess_sequencing_run_id.md)  <sub>0..1</sub>
     * Description: The identifier of a sequencing run.
     * Range: [String](types/String.md)
 * [SequencingProcess➞sequencing_lane_id](SequencingProcess_sequencing_lane_id.md)  <sub>0..1</sub>
     * Description: The identifier of a sequencing lane.
     * Range: [String](types/String.md)
 * [SequencingProcess➞sequencing_machine_id](SequencingProcess_sequencing_machine_id.md)  <sub>0..1</sub>
     * Description: The identifier of a sequencing machine.
     * Range: [String](types/String.md)
 * [SequencingProcess➞index_sequence](SequencingProcess_index_sequence.md)  <sub>0..1</sub>
     * Description: A unique nucleotide sequence that is added to a sample during library_preparation to serve as a unique identifier for the sample.
     * Range: [String](types/String.md)
 * [SequencingProcess➞sequencing_experiment](SequencingProcess_sequencing_experiment.md)  <sub>1..1</sub>
     * Description: The Sequencing Experiment associated with this Sequencing Process.
     * Range: [SequencingExperiment](SequencingExperiment.md)
 * [SequencingProcess➞sample](SequencingProcess_sample.md)  <sub>1..1</sub>
     * Description: The Sample associated with this Sequencing Process.
     * Range: [Sample](Sample.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)

### Mixed in from AttributeMixin:

 * [AttributeMixin➞attributes](AttributeMixin_attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
