
# Class: sequencing replicate


A technical sequencing replicate. E.g. the same sample sequenced across multiple lanes.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/SequencingReplicate](https://w3id.org/GHGA-Submission-Metadata-Schema/SequencingReplicate)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SequencingProcess]<has%20sequencing%20process%201..1-%20[SequencingReplicate&#124;name:string;description:string;sequencing_run_id:string%20%3F;sequencing_lane_id:string%20%3F;sequencing_machine_id:string%20%3F;accession:string;title(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[File]<has%20file%201..*-%20[SequencingReplicate],[SequencingReplicate]uses%20-.->[AccessionMixin],[Investigation]^-[SequencingReplicate],[SequencingProcess],[Investigation],[File],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[SequencingProcess]<has%20sequencing%20process%201..1-%20[SequencingReplicate&#124;name:string;description:string;sequencing_run_id:string%20%3F;sequencing_lane_id:string%20%3F;sequencing_machine_id:string%20%3F;accession:string;title(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[File]<has%20file%201..*-%20[SequencingReplicate],[SequencingReplicate]uses%20-.->[AccessionMixin],[Investigation]^-[SequencingReplicate],[SequencingProcess],[Investigation],[File],[AccessionMixin])

## Parents

 *  is_a: [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.

## Referenced by Class

 *  **None** *[has sequencing replicate](has_sequencing_replicate.md)*  <sub>0..1</sub>  **[SequencingReplicate](SequencingReplicate.md)**

## Attributes


### Own

 * [sequencing replicate➞name](sequencing_replicate_name.md)  <sub>1..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)
 * [sequencing replicate➞description](sequencing_replicate_description.md)  <sub>1..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)
 * [sequencing replicate➞sequencing run id](sequencing_replicate_sequencing_run_id.md)  <sub>0..1</sub>
     * Description: Identifier of the sequencing run. Used for batch correction.
     * Range: [String](types/String.md)
 * [sequencing replicate➞sequencing lane id](sequencing_replicate_sequencing_lane_id.md)  <sub>0..1</sub>
     * Description: Identifier of the sequencing lane. Used for batch correction.
     * Range: [String](types/String.md)
 * [sequencing replicate➞sequencing machine id](sequencing_replicate_sequencing_machine_id.md)  <sub>0..1</sub>
     * Description: Identifier of the sequencing machine. Used for batch correction.
     * Range: [String](types/String.md)
 * [sequencing replicate➞has file](sequencing_replicate_has_file.md)  <sub>1..\*</sub>
     * Description: The file associated with an entity.
     * Range: [File](File.md)
     * in subsets: (restricted)
 * [sequencing replicate➞has sequencing process](sequencing_replicate_has_sequencing_process.md)  <sub>1..1</sub>
     * Description: The sequencing process associated with an entity.
     * Range: [SequencingProcess](SequencingProcess.md)

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
 * [title](title.md)  <sub>0..1</sub>
     * Description: The title that describes an entity.
     * Range: [String](types/String.md)

### Mixed in from accession mixin:

 * [accession mixin➞accession](accession_mixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)
