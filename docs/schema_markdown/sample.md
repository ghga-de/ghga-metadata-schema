
# Class: Sample


A Sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use.  It is prepared from a Biospecimen.

URI: [GHGA:Sample](https://w3id.org/GHGA/Sample)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Individual]<individual%201..1-%20[Sample&#124;name:string;type:SampleTypeEnum%20%3F;biological_replicate:integer%20%3F;description:string;storage:StorageEnum%20%3F;disease_or_healthy:DiseaseOrHealthyEnum%20%3F;case_control_status:CaseControlStatusEnum;ega_accession:string%20%3F;xref:string%20*;biospecimen_name:string%20%3F;biospecimen_type:string%20%3F;biospecimen_description:string%20%3F;biospecimen_age_at_sampling:AgeRangeEnum;biospecimen_vital_status_at_sampling:VitalStatusEnum%20%3F;biospecimen_tissue_term:string%20%3F;biospecimen_tissue_id:string%20%3F;biospecimen_isolation:IsolationEnum%20%3F;biospecimen_storage:StorageEnum%20%3F;alias:string],[Experiment]-%20sample%201..1>[Sample],[Submission]++-%20samples%201..*>[Sample],[Experiment]-%20sample(i)%200..1>[Sample],[Submission]-%20samples(i)%200..*>[Sample],[Sample]uses%20-.->[IdentifiedByAliasMixin],[Sample]uses%20-.->[AttributeMixin],[Individual],[IdentifiedByAliasMixin],[Experiment],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Individual]<individual%201..1-%20[Sample&#124;name:string;type:SampleTypeEnum%20%3F;biological_replicate:integer%20%3F;description:string;storage:StorageEnum%20%3F;disease_or_healthy:DiseaseOrHealthyEnum%20%3F;case_control_status:CaseControlStatusEnum;ega_accession:string%20%3F;xref:string%20*;biospecimen_name:string%20%3F;biospecimen_type:string%20%3F;biospecimen_description:string%20%3F;biospecimen_age_at_sampling:AgeRangeEnum;biospecimen_vital_status_at_sampling:VitalStatusEnum%20%3F;biospecimen_tissue_term:string%20%3F;biospecimen_tissue_id:string%20%3F;biospecimen_isolation:IsolationEnum%20%3F;biospecimen_storage:StorageEnum%20%3F;alias:string],[Experiment]-%20sample%201..1>[Sample],[Submission]++-%20samples%201..*>[Sample],[Experiment]-%20sample(i)%200..1>[Sample],[Submission]-%20samples(i)%200..*>[Sample],[Sample]uses%20-.->[IdentifiedByAliasMixin],[Sample]uses%20-.->[AttributeMixin],[Individual],[IdentifiedByAliasMixin],[Experiment],[AttributeMixin],[Attribute])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[Experiment](Experiment.md)** *[Experiment➞sample](Experiment_sample.md)*  <sub>1..1</sub>  **[Sample](Sample.md)**
 *  **[Submission](Submission.md)** *[Submission➞samples](Submission_samples.md)*  <sub>1..\*</sub>  **[Sample](Sample.md)**
 *  **None** *[sample](sample.md)*  <sub>0..1</sub>  **[Sample](Sample.md)**
 *  **None** *[samples](samples.md)*  <sub>0..\*</sub>  **[Sample](Sample.md)**

## Attributes


### Own

 * [Sample➞individual](Sample_individual.md)  <sub>1..1</sub>
     * Description: The alias of the Individual entity from which this Biospecimen or Sample was derived.
     * Range: [Individual](Individual.md)
 * [Sample➞name](Sample_name.md)  <sub>1..1</sub>
     * Description: A descriptive name of this Sample (e.g., GHGAS_Blood_Sample1 or GHGAS_PBMC_RNAseq_S1). This property must not include any personally identifiable data.
     * Range: [String](types/String.md)
 * [Sample➞type](Sample_type.md)  <sub>0..1</sub>
     * Description: The type of the Sample.
     * Range: [SampleTypeEnum](SampleTypeEnum.md)
 * [Sample➞biological_replicate](Sample_biological_replicate.md)  <sub>0..1</sub>
     * Description: An integer to indicate the number of a biological replicate.
     * Range: [Integer](types/Integer.md)
 * [Sample➞description](Sample_description.md)  <sub>1..1</sub>
     * Description: A concise description about the Sample source, the collection method, and the protocol which was followed to process this Sample.
     * Range: [String](types/String.md)
 * [Sample➞storage](Sample_storage.md)  <sub>0..1</sub>
     * Description: Methods by which a Sample is stored.
     * Range: [StorageEnum](StorageEnum.md)
 * [Sample➞disease_or_healthy](Sample_disease_or_healthy.md)  <sub>0..1</sub>
     * Description: Whether a Condition corresponds to a disease or a healthy state.
     * Range: [DiseaseOrHealthyEnum](DiseaseOrHealthyEnum.md)
 * [Sample➞case_control_status](Sample_case_control_status.md)  <sub>1..1</sub>
     * Description: Whether a Condition corresponds to a treatment or a control.
     * Range: [CaseControlStatusEnum](CaseControlStatusEnum.md)
 * [Sample➞ega_accession](Sample_ega_accession.md)  <sub>0..1</sub>
     * Description: The EGA accession ID of an entity.
     * Range: [String](types/String.md)
 * [Sample➞xref](Sample_xref.md)  <sub>0..\*</sub>
     * Description: One or more cross-references for this Sample (e.g., this Sample may have an EBI BioSamples accession ID).
     * Range: [String](types/String.md)
 * [Sample➞biospecimen_name](Sample_biospecimen_name.md)  <sub>0..1</sub>
     * Description: A descriptive name of this Biospecimen (e.g., GHGAB_caudate_nucleus_biospecimen). This property must not include any personally identifiable data.
     * Range: [String](types/String.md)
 * [Sample➞biospecimen_type](Sample_biospecimen_type.md)  <sub>0..1</sub>
     * Description: The type of Biospecimen.
     * Range: [String](types/String.md)
 * [Sample➞biospecimen_description](Sample_biospecimen_description.md)  <sub>0..1</sub>
     * Description: A concise description about the Biospecimen source, the collection method, and the protocol which was followed to process this Biospecimen.
     * Range: [String](types/String.md)
 * [Sample➞biospecimen_age_at_sampling](Sample_biospecimen_age_at_sampling.md)  <sub>1..1</sub>
     * Description: The age of the Individual at the time of isolating this biospecimen.
     * Range: [AgeRangeEnum](AgeRangeEnum.md)
 * [Sample➞biospecimen_vital_status_at_sampling](Sample_biospecimen_vital_status_at_sampling.md)  <sub>0..1</sub>
     * Description: Vital Status of the Individual at the time of isolating this biospecimen (e.g., alive).
     * Range: [VitalStatusEnum](VitalStatusEnum.md)
 * [Sample➞biospecimen_tissue_term](Sample_biospecimen_tissue_term.md)  <sub>0..1</sub>
     * Description: The tissue this Biospecimen originated from. Should be a term from the BRENDA Tissue Ontology vocabulary (e.g., kidney, blood, melanoma cell).
     * Range: [String](types/String.md)
     * in subsets: (ontology)
 * [Sample➞biospecimen_tissue_id](Sample_biospecimen_tissue_id.md)  <sub>0..1</sub>
     * Description: The corresponding ontology ID for the biospecimen_tissue_term (e.g., BTO:0000671, BTO:0000089, BTO:0000848).
     * Range: [String](types/String.md)
     * in subsets: (ontology)
 * [Sample➞biospecimen_isolation](Sample_biospecimen_isolation.md)  <sub>0..1</sub>
     * Description: Method or device employed for collecting/isolating this Biospecimen.
     * Range: [IsolationEnum](IsolationEnum.md)
 * [Sample➞biospecimen_storage](Sample_biospecimen_storage.md)  <sub>0..1</sub>
     * Description: Methods by which this Biospecimen is stored.
     * Range: [StorageEnum](StorageEnum.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)

### Mixed in from AttributeMixin:

 * [AttributeMixin➞attributes](AttributeMixin_attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:001050 |
|  | | biolink:MaterialSample |

