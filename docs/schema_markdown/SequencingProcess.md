
# Class: SequencingProcess


A sequencing process linking a sample to sequencing output.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/SequencingProcess](https://w3id.org/GHGA-Submission-Metadata-Schema/SequencingProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample]<sample%201..1-%20[SequencingProcess&#124;name:string;description:string;sequencing_run_id:string%20%3F;sequencing_lane_id:string%20%3F;sequencing_machine_id:string%20%3F;alias:string;title(i):string%20%3F],[SequencingExperiment]<sequencing_experiment%201..1-%20[SequencingProcess],[File]<files%201..*-%20[SequencingProcess],[SequencingProcess]uses%20-.->[IdentifiedByAliasMixin],[SequencingProcess]uses%20-.->[AttributeMixin],[Investigation]^-[SequencingProcess],[SequencingExperiment],[Sample],[Investigation],[IdentifiedByAliasMixin],[File],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample]<sample%201..1-%20[SequencingProcess&#124;name:string;description:string;sequencing_run_id:string%20%3F;sequencing_lane_id:string%20%3F;sequencing_machine_id:string%20%3F;alias:string;title(i):string%20%3F],[SequencingExperiment]<sequencing_experiment%201..1-%20[SequencingProcess],[File]<files%201..*-%20[SequencingProcess],[SequencingProcess]uses%20-.->[IdentifiedByAliasMixin],[SequencingProcess]uses%20-.->[AttributeMixin],[Investigation]^-[SequencingProcess],[SequencingExperiment],[Sample],[Investigation],[IdentifiedByAliasMixin],[File],[AttributeMixin],[Attribute])

## Parents

 *  is_a: [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class


## Attributes


### Own

 * [SequencingProcess➞name](SequencingProcess_name.md)  <sub>1..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)
 * [SequencingProcess➞description](SequencingProcess_description.md)  <sub>1..1</sub>
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
 * [SequencingProcess➞files](SequencingProcess_files.md)  <sub>1..\*</sub>
     * Description: The files associated with an entity.
     * Range: [File](File.md)
     * in subsets: (restricted)
 * [SequencingProcess➞sequencing_experiment](SequencingProcess_sequencing_experiment.md)  <sub>1..1</sub>
     * Description: The sequencing experiment associated with an entity.
     * Range: [SequencingExperiment](SequencingExperiment.md)
     * in subsets: (restricted)
 * [SequencingProcess➞sample](SequencingProcess_sample.md)  <sub>1..1</sub>
     * Description: The sample associated with an entity.
     * Range: [Sample](Sample.md)
     * in subsets: (restricted)

### Inherited from Investigation:

 * [title](title.md)  <sub>0..1</sub>
     * Description: The title that describes an entity.
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
