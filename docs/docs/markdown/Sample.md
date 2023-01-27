
# Class: sample


A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).

URI: [GHGA:Sample](https://w3id.org/GHGA/Sample)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Biospecimen]<has%20biospecimen%200..1-++[Sample&#124;name:string;type:string;description:string;case_control_status:case_control_status_enum%20%3F;vital_status_at_sampling:vital_status_enum%20%3F;isolation:string%20%3F;storage:string%20%3F;xref:string%20*;accession:string;ega_accession:string;id(i):string;alias(i):string;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[AnatomicalEntity]<has%20anatomical%20entity%200..*-++[Sample],[Individual]<has%20individual%201..1-++[Sample],[Dataset]++-%20has%20sample%201..*>[Sample],[ExperimentProcess]++-%20has%20input%201..1>[Sample],[Experiment]++-%20has%20sample%201..*>[Sample],[Experiment]-%20has%20sample(i)%200..1>[Sample],[Dataset]-%20has%20sample(i)%200..1>[Sample],[Submission]-%20has%20sample(i)%200..1>[Sample],[Submission]++-%20has%20sample%200..*>[Sample],[Sample]uses%20-.->[AccessionMixin],[Sample]uses%20-.->[EgaAccessionMixin],[Sample]uses%20-.->[AttributeMixin],[MaterialEntity]^-[Sample],[MaterialEntity],[Individual],[ExperimentProcess],[Experiment],[EgaAccessionMixin],[Dataset],[Biospecimen],[AttributeMixin],[Attribute],[AnatomicalEntity],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Biospecimen]<has%20biospecimen%200..1-++[Sample&#124;name:string;type:string;description:string;case_control_status:case_control_status_enum%20%3F;vital_status_at_sampling:vital_status_enum%20%3F;isolation:string%20%3F;storage:string%20%3F;xref:string%20*;accession:string;ega_accession:string;id(i):string;alias(i):string;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[AnatomicalEntity]<has%20anatomical%20entity%200..*-++[Sample],[Individual]<has%20individual%201..1-++[Sample],[Dataset]++-%20has%20sample%201..*>[Sample],[ExperimentProcess]++-%20has%20input%201..1>[Sample],[Experiment]++-%20has%20sample%201..*>[Sample],[Experiment]-%20has%20sample(i)%200..1>[Sample],[Dataset]-%20has%20sample(i)%200..1>[Sample],[Submission]-%20has%20sample(i)%200..1>[Sample],[Submission]++-%20has%20sample%200..*>[Sample],[Sample]uses%20-.->[AccessionMixin],[Sample]uses%20-.->[EgaAccessionMixin],[Sample]uses%20-.->[AttributeMixin],[MaterialEntity]^-[Sample],[MaterialEntity],[Individual],[ExperimentProcess],[Experiment],[EgaAccessionMixin],[Dataset],[Biospecimen],[AttributeMixin],[Attribute],[AnatomicalEntity],[AccessionMixin])

## Parents

 *  is_a: [MaterialEntity](MaterialEntity.md) - A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an EGA accession, in addition to GHGA accession.
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[Dataset](Dataset.md)** *[dataset➞has sample](dataset_has_sample.md)*  <sub>1..\*</sub>  **[Sample](Sample.md)**
 *  **[ExperimentProcess](ExperimentProcess.md)** *[experiment process➞has input](experiment_process_has_input.md)*  <sub>1..1</sub>  **[Sample](Sample.md)**
 *  **[Experiment](Experiment.md)** *[experiment➞has sample](experiment_has_sample.md)*  <sub>1..\*</sub>  **[Sample](Sample.md)**
 *  **None** *[has sample](has_sample.md)*  <sub>0..1</sub>  **[Sample](Sample.md)**
 *  **[Submission](Submission.md)** *[submission➞has sample](submission_has_sample.md)*  <sub>0..\*</sub>  **[Sample](Sample.md)**

## Attributes


### Own

 * [sample➞name](sample_name.md)  <sub>1..1</sub>
     * Description: Name of the sample (eg:GHGAS_Blood_Sample1 or GHGAS_PBMC_RNAseq_S1).
     * Range: [String](types/String.md)
 * [sample➞type](sample_type.md)  <sub>1..1</sub>
     * Description: The type of sample.
     * Range: [String](types/String.md)
 * [sample➞description](sample_description.md)  <sub>1..1</sub>
     * Description: Short textual description of the sample (How the sample was collected, sample source, protocol followed for processing the sample etc).
     * Range: [String](types/String.md)
 * [sample➞case control status](sample_case_control_status.md)  <sub>0..1</sub>
     * Description: Whether the sample is to be treated as Case or Control in a Study.
     * Range: [case control status enum](case control status enum.md)
 * [sample➞vital status at sampling](sample_vital_status_at_sampling.md)  <sub>0..1</sub>
     * Description: Vital Status of an Individual at the point of sampling (eg:'Alive', 'Deceased').
     * Range: [vital status enum](vital status enum.md)
 * [sample➞isolation](sample_isolation.md)  <sub>0..1</sub>
     * Description: Method or device employed for collecting/isolating a biospecimen or a sample.
     * Range: [String](types/String.md)
 * [sample➞storage](sample_storage.md)  <sub>0..1</sub>
     * Description: Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).
     * Range: [String](types/String.md)
 * [sample➞has individual](sample_has_individual.md)  <sub>1..1</sub>
     * Description: The Individual from which this Sample was derived from.
     * Range: [Individual](Individual.md)
     * in subsets: (restricted)
 * [sample➞has anatomical entity](sample_has_anatomical_entity.md)  <sub>0..\*</sub>
     * Description: Anatomical site associated with an entity.
     * Range: [AnatomicalEntity](AnatomicalEntity.md)
 * [sample➞has biospecimen](sample_has_biospecimen.md)  <sub>0..1</sub>
     * Description: The Biospecimen from which this Sample was prepared from.
     * Range: [Biospecimen](Biospecimen.md)
     * in subsets: (restricted)
 * [sample➞xref](sample_xref.md)  <sub>0..\*</sub>
     * Description: One or more cross-references for this Sample. For example, this Sample may have an EBI BioSamples accession or an EGA Sample accession.
     * Range: [String](types/String.md)

### Inherited from material entity:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞alias](named_thing_alias.md)  <sub>1..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞creation date](named_thing_creation_date.md)  <sub>1..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was created.
     * Range: [String](types/String.md)
 * [named thing➞update date](named_thing_update_date.md)  <sub>1..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was updated.
     * Range: [String](types/String.md)

### Mixed in from accession mixin:

 * [accession mixin➞accession](accession_mixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

### Mixed in from ega accession mixin:

 * [ega accession mixin➞ega accession](ega_accession_mixin_ega_accession.md)  <sub>1..1</sub>
     * Description: A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
     * Range: [String](types/String.md)

### Mixed in from attribute mixin:

 * [attribute mixin➞has attribute](attribute_mixin_has_attribute.md)  <sub>1..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:001050 |
|  | | biolink:MaterialSample |

