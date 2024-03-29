
# Class: Biospecimen


A Biospecimen is any natural material taken from a biological entity for testing, diagnostics, treatment, or research purposes.  It is linked to the Individual from which the Biospecimen is derived.

URI: [GHGA:Biospecimen](https://w3id.org/GHGA/Biospecimen)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample],[Individual],[IdentifiedByAliasMixin],[Individual]<individual%201..1-%20[Biospecimen&#124;name:string%20%3F;type:string%20%3F;description:string%20%3F;age_at_sampling:AgeRangeEnum;vital_status_at_sampling:VitalStatusEnum%20%3F;tissue:string;isolation:string%20%3F;storage:StorageEnum%20%3F;alias:string],[Sample]-%20biospecimen%200..1>[Biospecimen],[Submission]++-%20biospecimens%201..*>[Biospecimen],[Sample]-%20biospecimen(i)%200..1>[Biospecimen],[Submission]-%20biospecimens(i)%200..*>[Biospecimen],[Biospecimen]uses%20-.->[IdentifiedByAliasMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample],[Individual],[IdentifiedByAliasMixin],[Individual]<individual%201..1-%20[Biospecimen&#124;name:string%20%3F;type:string%20%3F;description:string%20%3F;age_at_sampling:AgeRangeEnum;vital_status_at_sampling:VitalStatusEnum%20%3F;tissue:string;isolation:string%20%3F;storage:StorageEnum%20%3F;alias:string],[Sample]-%20biospecimen%200..1>[Biospecimen],[Submission]++-%20biospecimens%201..*>[Biospecimen],[Sample]-%20biospecimen(i)%200..1>[Biospecimen],[Submission]-%20biospecimens(i)%200..*>[Biospecimen],[Biospecimen]uses%20-.->[IdentifiedByAliasMixin])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

 *  **[Sample](Sample.md)** *[Sample➞biospecimen](Sample_biospecimen.md)*  <sub>0..1</sub>  **[Biospecimen](Biospecimen.md)**
 *  **[Submission](Submission.md)** *[Submission➞biospecimens](Submission_biospecimens.md)*  <sub>1..\*</sub>  **[Biospecimen](Biospecimen.md)**
 *  **None** *[biospecimen](biospecimen.md)*  <sub>0..1</sub>  **[Biospecimen](Biospecimen.md)**
 *  **None** *[biospecimens](biospecimens.md)*  <sub>0..\*</sub>  **[Biospecimen](Biospecimen.md)**

## Attributes


### Own

 * [Biospecimen➞name](Biospecimen_name.md)  <sub>0..1</sub>
     * Description: A descriptive name of this Biospecimen (e.g., GHGAB_caudate_nucleus_biospecimen). This property must not include any personally identifiable data.
     * Range: [String](types/String.md)
 * [Biospecimen➞type](Biospecimen_type.md)  <sub>0..1</sub>
     * Description: The type of Biospecimen.
     * Range: [String](types/String.md)
 * [Biospecimen➞description](Biospecimen_description.md)  <sub>0..1</sub>
     * Description: A concise description about the Biospecimen source, the collection method, and the protocol which was followed to process this Biospecimen.
     * Range: [String](types/String.md)
 * [Biospecimen➞age_at_sampling](Biospecimen_age_at_sampling.md)  <sub>1..1</sub>
     * Description: The age of the Individual.
     * Range: [AgeRangeEnum](AgeRangeEnum.md)
 * [Biospecimen➞vital_status_at_sampling](Biospecimen_vital_status_at_sampling.md)  <sub>0..1</sub>
     * Description: Vital Status of the Individual at the point of sampling (e.g., alive).
     * Range: [VitalStatusEnum](VitalStatusEnum.md)
 * [Biospecimen➞tissue](Biospecimen_tissue.md)  <sub>1..1</sub>
     * Description: The tissue this Biospecimen originated from.
     * Range: [String](types/String.md)
     * in subsets: (ontology)
 * [Biospecimen➞isolation](Biospecimen_isolation.md)  <sub>0..1</sub>
     * Description: Method or device employed for collecting/isolating this Biospecimen.
     * Range: [String](types/String.md)
     * in subsets: (ontology)
 * [Biospecimen➞storage](Biospecimen_storage.md)  <sub>0..1</sub>
     * Description: Methods by which this Biospecimen is stored.
     * Range: [StorageEnum](StorageEnum.md)
 * [Biospecimen➞individual](Biospecimen_individual.md)  <sub>1..1</sub>
     * Description: The Individual entity from which this Biospecimen was derived.
     * Range: [Individual](Individual.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | OBI:0100051 |

