
# Class: sequencing process


A sequencing process linking a sample to sequencing output.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/SequencingProcess](https://w3id.org/GHGA-Submission-Metadata-Schema/SequencingProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SequencingReplicate],[Sample]<has%20sample%201..1-%20[SequencingProcess&#124;accession:string;title(i):string%20%3F;description(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[SequencingExperiment]<has%20sequencing%20experiment%201..1-%20[SequencingProcess],[SequencingReplicate]-%20has%20sequencing%20process(i)%200..1>[SequencingProcess],[SequencingReplicate]-%20has%20sequencing%20process%201..1>[SequencingProcess],[SequencingProcess]uses%20-.->[AccessionMixin],[SequencingProcess]uses%20-.->[AttributeMixin],[Investigation]^-[SequencingProcess],[SequencingExperiment],[Sample],[Investigation],[AttributeMixin],[Attribute],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[SequencingReplicate],[Sample]<has%20sample%201..1-%20[SequencingProcess&#124;accession:string;title(i):string%20%3F;description(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[SequencingExperiment]<has%20sequencing%20experiment%201..1-%20[SequencingProcess],[SequencingReplicate]-%20has%20sequencing%20process(i)%200..1>[SequencingProcess],[SequencingReplicate]-%20has%20sequencing%20process%201..1>[SequencingProcess],[SequencingProcess]uses%20-.->[AccessionMixin],[SequencingProcess]uses%20-.->[AttributeMixin],[Investigation]^-[SequencingProcess],[SequencingExperiment],[Sample],[Investigation],[AttributeMixin],[Attribute],[AccessionMixin])

## Parents

 *  is_a: [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **None** *[has sequencing process](has_sequencing_process.md)*  <sub>0..1</sub>  **[SequencingProcess](SequencingProcess.md)**
 *  **[SequencingReplicate](SequencingReplicate.md)** *[sequencing replicate➞has sequencing process](sequencing_replicate_has_sequencing_process.md)*  <sub>1..1</sub>  **[SequencingProcess](SequencingProcess.md)**

## Attributes


### Own

 * [sequencing process➞has sequencing experiment](sequencing_process_has_sequencing_experiment.md)  <sub>1..1</sub>
     * Description: The sequencing experiment associated with an entity.
     * Range: [SequencingExperiment](SequencingExperiment.md)
     * in subsets: (restricted)
 * [sequencing process➞has sample](sequencing_process_has_sample.md)  <sub>1..1</sub>
     * Description: The sample associated with an entity.
     * Range: [Sample](Sample.md)
     * in subsets: (restricted)

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
 * [description](description.md)  <sub>0..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)

### Mixed in from accession mixin:

 * [accession mixin➞accession](accession_mixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

### Mixed in from attribute mixin:

 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)
