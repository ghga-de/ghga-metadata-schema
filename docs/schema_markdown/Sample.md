
# Class: Sample


A Sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use.  It is prepared from a Biospecimen.

URI: [GHGA:Sample](https://w3id.org/GHGA/Sample)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProcess],[SampleFile],[Condition]<condition%201..1-%20[Sample&#124;name:string;type:SampleTypeEnum%20%3F;description:string;storage:StorageEnum%20%3F;xref:string%20*;alias:string],[Biospecimen]<biospecimen%200..1-%20[Sample],[SampleFile]-%20sample%201..1>[Sample],[SequencingProcess]-%20sample%201..1>[Sample],[Submission]++-%20samples%201..*>[Sample],[SequencingProcess]-%20sample(i)%200..1>[Sample],[SampleFile]-%20sample(i)%200..1>[Sample],[Submission]-%20samples(i)%200..*>[Sample],[Sample]uses%20-.->[IdentifiedByAliasMixin],[Sample]uses%20-.->[AttributeMixin],[IdentifiedByAliasMixin],[Condition],[Biospecimen],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProcess],[SampleFile],[Condition]<condition%201..1-%20[Sample&#124;name:string;type:SampleTypeEnum%20%3F;description:string;storage:StorageEnum%20%3F;xref:string%20*;alias:string],[Biospecimen]<biospecimen%200..1-%20[Sample],[SampleFile]-%20sample%201..1>[Sample],[SequencingProcess]-%20sample%201..1>[Sample],[Submission]++-%20samples%201..*>[Sample],[SequencingProcess]-%20sample(i)%200..1>[Sample],[SampleFile]-%20sample(i)%200..1>[Sample],[Submission]-%20samples(i)%200..*>[Sample],[Sample]uses%20-.->[IdentifiedByAliasMixin],[Sample]uses%20-.->[AttributeMixin],[IdentifiedByAliasMixin],[Condition],[Biospecimen],[AttributeMixin],[Attribute])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[SampleFile](SampleFile.md)** *[SampleFile➞sample](SampleFile_sample.md)*  <sub>1..1</sub>  **[Sample](Sample.md)**
 *  **[SequencingProcess](SequencingProcess.md)** *[SequencingProcess➞sample](SequencingProcess_sample.md)*  <sub>1..1</sub>  **[Sample](Sample.md)**
 *  **[Submission](Submission.md)** *[Submission➞samples](Submission_samples.md)*  <sub>1..\*</sub>  **[Sample](Sample.md)**
 *  **None** *[sample](sample.md)*  <sub>0..1</sub>  **[Sample](Sample.md)**
 *  **None** *[samples](samples.md)*  <sub>0..\*</sub>  **[Sample](Sample.md)**

## Attributes


### Own

 * [Sample➞name](Sample_name.md)  <sub>1..1</sub>
     * Description: A descriptive name of this Sample (e.g., GHGAS_Blood_Sample1 or GHGAS_PBMC_RNAseq_S1). This property must not include any personally identifiable data.
     * Range: [String](types/String.md)
 * [Sample➞type](Sample_type.md)  <sub>0..1</sub>
     * Description: The type of the Sample.
     * Range: [SampleTypeEnum](SampleTypeEnum.md)
     * in subsets: (ontology)
 * [Sample➞description](Sample_description.md)  <sub>1..1</sub>
     * Description: A concise description about the Sample source, the collection method, and the protocol which was followed to process this Sample.
     * Range: [String](types/String.md)
 * [Sample➞storage](Sample_storage.md)  <sub>0..1</sub>
     * Description: Methods by which this Sample is stored.
     * Range: [StorageEnum](StorageEnum.md)
 * [Sample➞xref](Sample_xref.md)  <sub>0..\*</sub>
     * Description: One or more cross-references for this Sample (e.g., this Sample may have an EBI BioSamples accession ID).
     * Range: [String](types/String.md)
 * [Sample➞biospecimen](Sample_biospecimen.md)  <sub>0..1</sub>
     * Description: The Biospecimen which this Sample was prepared from.
     * Range: [Biospecimen](Biospecimen.md)
 * [Sample➞condition](Sample_condition.md)  <sub>1..1</sub>
     * Description: The Condition that applies to this Sample. The Condition is used to link comparable Samples (e.g., healthy Samples, wildtype Samples).
     * Range: [Condition](Condition.md)

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

