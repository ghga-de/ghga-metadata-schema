
# Class: sample


A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).

URI: [GHGA:Sample](https://w3id.org/GHGA/Sample)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Biospecimen]<has%20biospecimen%200..1-++[Sample&#124;name:string;type:string%20%3F;description:string;case_control_status:case_control_status_enum%20%3F;vital_status_at_sampling:vital_status_enum%20%3F;isolation:string%20%3F;storage:string%20%3F;sample_index_sequence:string%20%3F;lane_number:string%20%3F;alias:string;xref:string%20*;accession:string%20%3F;ega_accession:string%20%3F;id(i):string;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[AnatomicalEntity]<has%20anatomical%20entity%201..*-++[Sample],[Individual]<has%20individual%200..1-++[Sample],[Dataset]++-%20has%20sample%201..*>[Sample],[ExperimentProcess]++-%20has%20input%200..1>[Sample],[Experiment]++-%20has%20sample%201..*>[Sample],[Experiment]-%20has%20sample(i)%200..1>[Sample],[Dataset]-%20has%20sample(i)%200..1>[Sample],[Submission]-%20has%20sample(i)%200..1>[Sample],[Submission]++-%20has%20sample%200..*>[Sample],[Sample]uses%20-.->[AccessionMixin],[Sample]uses%20-.->[EgaAccessionMixin],[Sample]uses%20-.->[AttributeMixin],[MaterialEntity]^-[Sample],[MaterialEntity],[Individual],[ExperimentProcess],[Experiment],[EgaAccessionMixin],[Dataset],[Biospecimen],[AttributeMixin],[Attribute],[AnatomicalEntity],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Biospecimen]<has%20biospecimen%200..1-++[Sample&#124;name:string;type:string%20%3F;description:string;case_control_status:case_control_status_enum%20%3F;vital_status_at_sampling:vital_status_enum%20%3F;isolation:string%20%3F;storage:string%20%3F;sample_index_sequence:string%20%3F;lane_number:string%20%3F;alias:string;xref:string%20*;accession:string%20%3F;ega_accession:string%20%3F;id(i):string;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[AnatomicalEntity]<has%20anatomical%20entity%201..*-++[Sample],[Individual]<has%20individual%200..1-++[Sample],[Dataset]++-%20has%20sample%201..*>[Sample],[ExperimentProcess]++-%20has%20input%200..1>[Sample],[Experiment]++-%20has%20sample%201..*>[Sample],[Experiment]-%20has%20sample(i)%200..1>[Sample],[Dataset]-%20has%20sample(i)%200..1>[Sample],[Submission]-%20has%20sample(i)%200..1>[Sample],[Submission]++-%20has%20sample%200..*>[Sample],[Sample]uses%20-.->[AccessionMixin],[Sample]uses%20-.->[EgaAccessionMixin],[Sample]uses%20-.->[AttributeMixin],[MaterialEntity]^-[Sample],[MaterialEntity],[Individual],[ExperimentProcess],[Experiment],[EgaAccessionMixin],[Dataset],[Biospecimen],[AttributeMixin],[Attribute],[AnatomicalEntity],[AccessionMixin])

## Parents

 *  is_a: [MaterialEntity](MaterialEntity.md) - A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an EGA accession, in addition to GHGA accession.
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[Dataset](Dataset.md)** *[dataset➞has sample](dataset_has_sample.md)*  <sub>1..\*</sub>  **[Sample](Sample.md)**
 *  **[ExperimentProcess](ExperimentProcess.md)** *[experiment process➞has input](experiment_process_has_input.md)*  <sub>0..1</sub>  **[Sample](Sample.md)**
 *  **[Experiment](Experiment.md)** *[experiment➞has sample](experiment_has_sample.md)*  <sub>1..\*</sub>  **[Sample](Sample.md)**
 *  **None** *[has sample](has_sample.md)*  <sub>0..1</sub>  **[Sample](Sample.md)**
 *  **[Submission](Submission.md)** *[submission➞has sample](submission_has_sample.md)*  <sub>0..\*</sub>  **[Sample](Sample.md)**

## Attributes


### Own

 * [sample➞name](sample_name.md)  <sub>1..1</sub>
     * Description: Name of the sample (eg:GHGAS_Blood_Sample1 or GHGAS_PBMC_RNAseq_S1).
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [sample➞type](sample_type.md)  <sub>0..1</sub>
     * Description: The type of sample.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [sample➞description](sample_description.md)  <sub>1..1</sub>
     * Description: Short textual description of the sample (How the sample was collected, sample source, protocol followed for processing the sample etc).
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [case control status](case_control_status.md)  <sub>0..1</sub>
     * Description: Whether the sample is to be treated as Case or Control in a Study.
     * Range: [case control status enum](case control status enum.md)
     * in subsets: (recommended,public)
 * [vital status at sampling](vital_status_at_sampling.md)  <sub>0..1</sub>
     * Description: Vital Status of an Individual at the point of sampling (eg:'Alive', 'Deceased').
     * Range: [vital status enum](vital status enum.md)
     * in subsets: (recommended,public)
 * [isolation](isolation.md)  <sub>0..1</sub>
     * Description: Method or device employed for collecting/isolating a biospecimen or a sample.
     * Range: [String](types/String.md)
     * in subsets: (recommended,public)
 * [storage](storage.md)  <sub>0..1</sub>
     * Description: Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).
     * Range: [String](types/String.md)
     * in subsets: (recommended,public)
 * [sample➞has individual](sample_has_individual.md)  <sub>0..1</sub>
     * Description: The Individual from which this Sample was derived from.
     * Range: [Individual](Individual.md)
     * in subsets: (essential,restricted)
 * [sample➞has anatomical entity](sample_has_anatomical_entity.md)  <sub>1..\*</sub>
     * Description: Anatomical site associated with an entity.
     * Range: [AnatomicalEntity](AnatomicalEntity.md)
     * in subsets: (recommended,public)
 * [sample➞has biospecimen](sample_has_biospecimen.md)  <sub>0..1</sub>
     * Description: The Biospecimen from which this Sample was prepared from.
     * Range: [Biospecimen](Biospecimen.md)
     * in subsets: (optional,restricted)
 * [sample index sequence](sample_index_sequence.md)  <sub>0..1</sub>
     * Description: A unique nucleotide sequence that is added to a sample during library preparation to serve as a unique identifier for the sample.
     * Range: [String](types/String.md)
 * [lane number](lane_number.md)  <sub>0..1</sub>
     * Description: The numerical identifier for the lane or machine unit where a sample was located during nucleotide sequencing.
     * Range: [String](types/String.md)
     * in subsets: (recommended,public)
 * [sample➞alias](sample_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [sample➞xref](sample_xref.md)  <sub>0..\*</sub>
     * Description: One or more cross-references for this Sample. For example, this Sample may have an EBI BioSamples accession or an EGA Sample accession.
     * Range: [String](types/String.md)
     * in subsets: (optional,public)

### Inherited from material entity:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [named thing➞creation date](named_thing_creation_date.md)  <sub>0..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was created.
     * Range: [String](types/String.md)
 * [named thing➞update date](named_thing_update_date.md)  <sub>0..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was updated.
     * Range: [String](types/String.md)

### Mixed in from accession mixin:

 * [accession](accession.md)  <sub>0..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

### Mixed in from ega accession mixin:

 * [ega accession](ega_accession.md)  <sub>0..1</sub>
     * Description: A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
     * Range: [String](types/String.md)

### Mixed in from attribute mixin:

 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (optional,restricted)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:001050 |
|  | | biolink:MaterialSample |

