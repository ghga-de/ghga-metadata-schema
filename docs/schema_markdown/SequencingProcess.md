
# Class: SequencingProcess


A sequencing process linking a sample to sequencing output.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/SequencingProcess](https://w3id.org/GHGA-Submission-Metadata-Schema/SequencingProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SequencingProcessFile],[Sample]<sample%201..1-%20[SequencingProcess&#124;name:string;description:string;sequencing_run_id:string%20%3F;sequencing_lane_id:string%20%3F;sequencing_machine_id:string%20%3F;accession:string;title(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[SequencingExperiment]<sequencing_experiment%201..1-%20[SequencingProcess],[SequencingProcessFile]-%20sequencing_process%201..1>[SequencingProcess],[SequencingProcessFile]-%20sequencing_process(i)%200..1>[SequencingProcess],[SequencingProcess]uses%20-.->[AccessionMixin],[SequencingProcess]uses%20-.->[AttributeMixin],[Investigation]^-[SequencingProcess],[SequencingExperiment],[Sample],[Investigation],[AttributeMixin],[Attribute],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[SequencingProcessFile],[Sample]<sample%201..1-%20[SequencingProcess&#124;name:string;description:string;sequencing_run_id:string%20%3F;sequencing_lane_id:string%20%3F;sequencing_machine_id:string%20%3F;accession:string;title(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[SequencingExperiment]<sequencing_experiment%201..1-%20[SequencingProcess],[SequencingProcessFile]-%20sequencing_process%201..1>[SequencingProcess],[SequencingProcessFile]-%20sequencing_process(i)%200..1>[SequencingProcess],[SequencingProcess]uses%20-.->[AccessionMixin],[SequencingProcess]uses%20-.->[AttributeMixin],[Investigation]^-[SequencingProcess],[SequencingExperiment],[Sample],[Investigation],[AttributeMixin],[Attribute],[AccessionMixin])

## Parents

 *  is_a: [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[SequencingProcessFile](SequencingProcessFile.md)** *[SequencingProcessFile➞sequencing_process](SequencingProcessFile_sequencing_process.md)*  <sub>1..1</sub>  **[SequencingProcess](SequencingProcess.md)**
 *  **None** *[sequencing_process](sequencing_process.md)*  <sub>0..1</sub>  **[SequencingProcess](SequencingProcess.md)**

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
 * [SequencingProcess➞sequencing_experiment](SequencingProcess_sequencing_experiment.md)  <sub>1..1</sub>
     * Description: The sequencing experiment associated with an entity.
     * Range: [SequencingExperiment](SequencingExperiment.md)
     * in subsets: (restricted)
 * [SequencingProcess➞sample](SequencingProcess_sample.md)  <sub>1..1</sub>
     * Description: The sample associated with an entity.
     * Range: [Sample](Sample.md)
     * in subsets: (restricted)

### Inherited from Investigation:

 * [NamedThing➞id](NamedThing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [NamedThing➞alias](NamedThing_alias.md)  <sub>1..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [NamedThing➞xref](NamedThing_xref.md)  <sub>0..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)
 * [title](title.md)  <sub>0..1</sub>
     * Description: The title that describes an entity.
     * Range: [String](types/String.md)

### Mixed in from AccessionMixin:

 * [AccessionMixin➞accession](AccessionMixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

### Mixed in from AttributeMixin:

 * [attributes](attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)
