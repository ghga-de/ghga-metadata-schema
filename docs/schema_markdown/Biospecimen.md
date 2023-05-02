
# Class: Biospecimen


A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics, treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is derived.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Biospecimen](https://w3id.org/GHGA-Submission-Metadata-Schema/Biospecimen)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample],[MaterialEntity],[Individual],[AnatomicalEntity]<anatomical_entities%201..*-++[Biospecimen&#124;name:string%20%3F;type:string%20%3F;description:string%20%3F;isolation:string%20%3F;storage:string%20%3F;vital_status_at_sampling:VitalStatusEnum%20%3F;accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Individual]<individual%201..1-%20[Biospecimen],[Sample]-%20biospecimen%200..1>[Biospecimen],[Submission]++-%20biospecimens%200..*>[Biospecimen],[Sample]-%20biospecimen(i)%200..1>[Biospecimen],[Submission]-%20biospecimens(i)%200..*>[Biospecimen],[Biospecimen]uses%20-.->[AccessionMixin],[MaterialEntity]^-[Biospecimen],[AnatomicalEntity],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample],[MaterialEntity],[Individual],[AnatomicalEntity]<anatomical_entities%201..*-++[Biospecimen&#124;name:string%20%3F;type:string%20%3F;description:string%20%3F;isolation:string%20%3F;storage:string%20%3F;vital_status_at_sampling:VitalStatusEnum%20%3F;accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Individual]<individual%201..1-%20[Biospecimen],[Sample]-%20biospecimen%200..1>[Biospecimen],[Submission]++-%20biospecimens%200..*>[Biospecimen],[Sample]-%20biospecimen(i)%200..1>[Biospecimen],[Submission]-%20biospecimens(i)%200..*>[Biospecimen],[Biospecimen]uses%20-.->[AccessionMixin],[MaterialEntity]^-[Biospecimen],[AnatomicalEntity],[AccessionMixin])

## Parents

 *  is_a: [MaterialEntity](MaterialEntity.md) - A MaterialEntity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.

## Referenced by Class

 *  **[Sample](Sample.md)** *[Sample➞biospecimen](Sample_biospecimen.md)*  <sub>0..1</sub>  **[Biospecimen](Biospecimen.md)**
 *  **[Submission](Submission.md)** *[Submission➞biospecimens](Submission_biospecimens.md)*  <sub>0..\*</sub>  **[Biospecimen](Biospecimen.md)**
 *  **None** *[biospecimen](biospecimen.md)*  <sub>0..1</sub>  **[Biospecimen](Biospecimen.md)**
 *  **None** *[biospecimens](biospecimens.md)*  <sub>0..\*</sub>  **[Biospecimen](Biospecimen.md)**

## Attributes


### Own

 * [Biospecimen➞name](Biospecimen_name.md)  <sub>0..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)
 * [Biospecimen➞type](Biospecimen_type.md)  <sub>0..1</sub>
     * Description: The type of Biospecimen.
     * Range: [String](types/String.md)
 * [Biospecimen➞description](Biospecimen_description.md)  <sub>0..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)
 * [Biospecimen➞isolation](Biospecimen_isolation.md)  <sub>0..1</sub>
     * Description: Method or device employed for collecting/isolating a biospecimen or a sample.
     * Range: [String](types/String.md)
 * [Biospecimen➞storage](Biospecimen_storage.md)  <sub>0..1</sub>
     * Description: Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).
     * Range: [String](types/String.md)
 * [Biospecimen➞individual](Biospecimen_individual.md)  <sub>1..1</sub>
     * Description: The Individual entity from which this Biospecimen was derived.
     * Range: [Individual](Individual.md)
     * in subsets: (restricted)
 * [Biospecimen➞vital_status_at_sampling](Biospecimen_vital_status_at_sampling.md)  <sub>0..1</sub>
     * Description: Vital Status of an Individual at the point of sampling (eg:'Alive', 'Deceased').
     * Range: [VitalStatusEnum](VitalStatusEnum.md)
 * [Biospecimen➞anatomical_entities](Biospecimen_anatomical_entities.md)  <sub>1..\*</sub>
     * Description: Anatomical sites associated with an entity.
     * Range: [AnatomicalEntity](AnatomicalEntity.md)

### Inherited from MaterialEntity:

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

### Mixed in from AccessionMixin:

 * [AccessionMixin➞accession](AccessionMixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | OBI:0100051 |

