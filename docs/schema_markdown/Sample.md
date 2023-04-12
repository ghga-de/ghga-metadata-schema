
# Class: sample


A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Sample](https://w3id.org/GHGA-Submission-Metadata-Schema/Sample)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProcess],[Condition]<has%20condition%201..1-%20[Sample&#124;name:string;type:string%20%3F;description:string;isolation:string%20%3F;storage:string%20%3F;xref:string%20*;accession:string;ega_accession:string;id(i):string;alias(i):string],[Biospecimen]<has%20biospecimen%200..1-++[Sample],[SequencingProcess]-%20has%20sample(i)%200..1>[Sample],[Submission]-%20has%20sample(i)%200..1>[Sample],[SequencingProcess]-%20has%20sample%201..1>[Sample],[Submission]++-%20has%20sample%200..*>[Sample],[Sample]uses%20-.->[AccessionMixin],[Sample]uses%20-.->[EgaAccessionMixin],[Sample]uses%20-.->[AttributeMixin],[MaterialEntity]^-[Sample],[MaterialEntity],[EgaAccessionMixin],[Condition],[Biospecimen],[AttributeMixin],[Attribute],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProcess],[Condition]<has%20condition%201..1-%20[Sample&#124;name:string;type:string%20%3F;description:string;isolation:string%20%3F;storage:string%20%3F;xref:string%20*;accession:string;ega_accession:string;id(i):string;alias(i):string],[Biospecimen]<has%20biospecimen%200..1-++[Sample],[SequencingProcess]-%20has%20sample(i)%200..1>[Sample],[Submission]-%20has%20sample(i)%200..1>[Sample],[SequencingProcess]-%20has%20sample%201..1>[Sample],[Submission]++-%20has%20sample%200..*>[Sample],[Sample]uses%20-.->[AccessionMixin],[Sample]uses%20-.->[EgaAccessionMixin],[Sample]uses%20-.->[AttributeMixin],[MaterialEntity]^-[Sample],[MaterialEntity],[EgaAccessionMixin],[Condition],[Biospecimen],[AttributeMixin],[Attribute],[AccessionMixin])

## Parents

 *  is_a: [MaterialEntity](MaterialEntity.md) - A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an EGA accession, in addition to GHGA accession.
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **None** *[has sample](has_sample.md)*  <sub>0..1</sub>  **[Sample](Sample.md)**
 *  **[SequencingProcess](SequencingProcess.md)** *[sequencing process➞has sample](sequencing_process_has_sample.md)*  <sub>1..1</sub>  **[Sample](Sample.md)**
 *  **[Submission](Submission.md)** *[submission➞has sample](submission_has_sample.md)*  <sub>0..\*</sub>  **[Sample](Sample.md)**

## Attributes


### Own

 * [sample➞name](sample_name.md)  <sub>1..1</sub>
     * Description: Name of the sample (eg:GHGAS_Blood_Sample1 or GHGAS_PBMC_RNAseq_S1).
     * Range: [String](types/String.md)
 * [sample➞type](sample_type.md)  <sub>0..1</sub>
     * Description: The type of sample.
     * Range: [String](types/String.md)
 * [sample➞description](sample_description.md)  <sub>1..1</sub>
     * Description: Short textual description of the sample (How the sample was collected, sample source, protocol followed for processing the sample etc).
     * Range: [String](types/String.md)
 * [isolation](isolation.md)  <sub>0..1</sub>
     * Description: Method or device employed for collecting/isolating a biospecimen or a sample.
     * Range: [String](types/String.md)
 * [sample➞storage](sample_storage.md)  <sub>0..1</sub>
     * Description: Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).
     * Range: [String](types/String.md)
 * [sample➞has biospecimen](sample_has_biospecimen.md)  <sub>0..1</sub>
     * Description: The Biospecimen from which this Sample was prepared from.
     * Range: [Biospecimen](Biospecimen.md)
     * in subsets: (restricted)
 * [sample➞has condition](sample_has_condition.md)  <sub>1..1</sub>
     * Description: The condition associated with an entity.
     * Range: [Condition](Condition.md)
 * [sample➞xref](sample_xref.md)  <sub>0..\*</sub>
     * Description: One or more cross-references for this Sample. For example, this Sample may have an EBI BioSamples accession or an EGA Sample accession.
     * Range: [String](types/String.md)

### Inherited from material entity:

 * [NamedThing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [NamedThing➞alias](named_thing_alias.md)  <sub>1..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)

### Mixed in from accession mixin:

 * [accession mixin➞accession](accession_mixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

### Mixed in from ega accession mixin:

 * [ega accession mixin➞ega accession](ega_accession_mixin_ega_accession.md)  <sub>1..1</sub>
     * Description: A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
     * Range: [String](types/String.md)

### Mixed in from attribute mixin:

 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

## Other properties

|                     |     |                        |
| ------------------- | --- | ---------------------- |
| **Exact Mappings:** |     | SIO:001050             |
|                     |     | biolink:MaterialSample |

