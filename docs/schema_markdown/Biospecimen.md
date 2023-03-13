
# Class: biospecimen


A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics, treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is derived.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Biospecimen](https://w3id.org/GHGA-Submission-Metadata-Schema/Biospecimen)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample],[MaterialEntity],[Individual],[Individual]<has%20individual%201..1-++[Biospecimen&#124;name:string%20%3F;type:string%20%3F;description:string%20%3F;isolation:string%20%3F;storage:string%20%3F;accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Sample]-%20has%20biospecimen(i)%200..1>[Biospecimen],[Submission]-%20has%20biospecimen(i)%200..1>[Biospecimen],[Sample]++-%20has%20biospecimen%200..1>[Biospecimen],[Submission]++-%20has%20biospecimen%200..*>[Biospecimen],[Biospecimen]uses%20-.->[AccessionMixin],[MaterialEntity]^-[Biospecimen],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample],[MaterialEntity],[Individual],[Individual]<has%20individual%201..1-++[Biospecimen&#124;name:string%20%3F;type:string%20%3F;description:string%20%3F;isolation:string%20%3F;storage:string%20%3F;accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Sample]-%20has%20biospecimen(i)%200..1>[Biospecimen],[Submission]-%20has%20biospecimen(i)%200..1>[Biospecimen],[Sample]++-%20has%20biospecimen%200..1>[Biospecimen],[Submission]++-%20has%20biospecimen%200..*>[Biospecimen],[Biospecimen]uses%20-.->[AccessionMixin],[MaterialEntity]^-[Biospecimen],[AccessionMixin])

## Parents

 *  is_a: [MaterialEntity](MaterialEntity.md) - A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.

## Referenced by Class

 *  **None** *[has biospecimen](has_biospecimen.md)*  <sub>0..1</sub>  **[Biospecimen](Biospecimen.md)**
 *  **[Sample](Sample.md)** *[sample➞has biospecimen](sample_has_biospecimen.md)*  <sub>0..1</sub>  **[Biospecimen](Biospecimen.md)**
 *  **[Submission](Submission.md)** *[submission➞has biospecimen](submission_has_biospecimen.md)*  <sub>0..\*</sub>  **[Biospecimen](Biospecimen.md)**

## Attributes


### Own

 * [biospecimen➞name](biospecimen_name.md)  <sub>0..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)
 * [biospecimen➞type](biospecimen_type.md)  <sub>0..1</sub>
     * Description: The type of Biospecimen.
     * Range: [String](types/String.md)
 * [biospecimen➞description](biospecimen_description.md)  <sub>0..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)
 * [biospecimen➞isolation](biospecimen_isolation.md)  <sub>0..1</sub>
     * Description: Method or device employed for collecting/isolating a biospecimen or a sample.
     * Range: [String](types/String.md)
 * [biospecimen➞storage](biospecimen_storage.md)  <sub>0..1</sub>
     * Description: Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).
     * Range: [String](types/String.md)
 * [biospecimen➞has individual](biospecimen_has_individual.md)  <sub>1..1</sub>
     * Description: The Individual entity from which this Biospecimen was derived.
     * Range: [Individual](Individual.md)
     * in subsets: (restricted)

### Inherited from material entity:

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

### Mixed in from accession mixin:

 * [accession mixin➞accession](accession_mixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | OBI:0100051 |

