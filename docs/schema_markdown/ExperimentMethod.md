
# Class: ExperimentMethod


The Experiment Method captures technical metadata describing the parameters used to generate output from the Sample.

URI: [GHGA:ExperimentMethod](https://w3id.org/GHGA/ExperimentMethod)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[IdentifiedByAliasMixin],[ExperimentMethodSupportingFile],[Attribute]<attributes%200..*-++[ExperimentMethod&#124;name:string;description:string;type:string;library_type:LibraryPreparationLibraryTypeEnum;library_selection_methods:LibraryPreparationLibrarySelectionEnum%20%2B;library_preparation:string;library_preparation_kit_retail_name:LibraryPreparationKitRetailNameEnum%20%3F;library_preparation_kit_manufacturer:string%20%3F;primer:PrimerEnum%20%3F;end_bias:EndBiasEnum%20%3F;target_regions:string%20*;rnaseq_strandedness:LibraryPreparationRNASeqStrandednessEnum%20%3F;instrument_model:InstrumentModelEnum;sequencing_center:string%20%3F;sequencing_read_length:string%20%3F;sequencing_layout:SequencingProtocolSequencingLayoutEnum;target_coverage:string%20%3F;flow_cell_id:string%20%3F;flow_cell_type:FlowCellTypeEnum%20%3F;sample_barcode_read:SampleBarcodeReadEnum%20%3F;ega_accession:string%20%3F;alias:string],[ExperimentMethodSupportingFile]-%20experiment_method%201..1>[ExperimentMethod],[Experiment]-%20experiment_method%201..1>[ExperimentMethod],[Submission]++-%20experiment_methods%201..*>[ExperimentMethod],[Experiment]-%20experiment_method(i)%200..1>[ExperimentMethod],[ExperimentMethodSupportingFile]-%20experiment_method(i)%200..1>[ExperimentMethod],[Submission]-%20experiment_methods(i)%200..*>[ExperimentMethod],[ExperimentMethod]uses%20-.->[IdentifiedByAliasMixin],[ExperimentMethod]uses%20-.->[AttributeMixin],[Experiment],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[IdentifiedByAliasMixin],[ExperimentMethodSupportingFile],[Attribute]<attributes%200..*-++[ExperimentMethod&#124;name:string;description:string;type:string;library_type:LibraryPreparationLibraryTypeEnum;library_selection_methods:LibraryPreparationLibrarySelectionEnum%20%2B;library_preparation:string;library_preparation_kit_retail_name:LibraryPreparationKitRetailNameEnum%20%3F;library_preparation_kit_manufacturer:string%20%3F;primer:PrimerEnum%20%3F;end_bias:EndBiasEnum%20%3F;target_regions:string%20*;rnaseq_strandedness:LibraryPreparationRNASeqStrandednessEnum%20%3F;instrument_model:InstrumentModelEnum;sequencing_center:string%20%3F;sequencing_read_length:string%20%3F;sequencing_layout:SequencingProtocolSequencingLayoutEnum;target_coverage:string%20%3F;flow_cell_id:string%20%3F;flow_cell_type:FlowCellTypeEnum%20%3F;sample_barcode_read:SampleBarcodeReadEnum%20%3F;ega_accession:string%20%3F;alias:string],[ExperimentMethodSupportingFile]-%20experiment_method%201..1>[ExperimentMethod],[Experiment]-%20experiment_method%201..1>[ExperimentMethod],[Submission]++-%20experiment_methods%201..*>[ExperimentMethod],[Experiment]-%20experiment_method(i)%200..1>[ExperimentMethod],[ExperimentMethodSupportingFile]-%20experiment_method(i)%200..1>[ExperimentMethod],[Submission]-%20experiment_methods(i)%200..*>[ExperimentMethod],[ExperimentMethod]uses%20-.->[IdentifiedByAliasMixin],[ExperimentMethod]uses%20-.->[AttributeMixin],[Experiment],[AttributeMixin],[Attribute])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[ExperimentMethodSupportingFile](ExperimentMethodSupportingFile.md)** *[ExperimentMethodSupportingFile➞experiment_method](ExperimentMethodSupportingFile_experiment_method.md)*  <sub>1..1</sub>  **[ExperimentMethod](ExperimentMethod.md)**
 *  **[Experiment](Experiment.md)** *[Experiment➞experiment_method](Experiment_experiment_method.md)*  <sub>1..1</sub>  **[ExperimentMethod](ExperimentMethod.md)**
 *  **[Submission](Submission.md)** *[Submission➞experiment_methods](Submission_experiment_methods.md)*  <sub>1..\*</sub>  **[ExperimentMethod](ExperimentMethod.md)**
 *  **None** *[experiment_method](experiment_method.md)*  <sub>0..1</sub>  **[ExperimentMethod](ExperimentMethod.md)**
 *  **None** *[experiment_methods](experiment_methods.md)*  <sub>0..\*</sub>  **[ExperimentMethod](ExperimentMethod.md)**

## Attributes


### Own

 * [ExperimentMethod➞name](ExperimentMethod_name.md)  <sub>1..1</sub>
     * Description: A short name identifying this Experiment Method.
     * Range: [String](types/String.md)
 * [ExperimentMethod➞description](ExperimentMethod_description.md)  <sub>1..1</sub>
     * Description: A short description of this Experiment Method.
     * Range: [String](types/String.md)
 * [ExperimentMethod➞type](ExperimentMethod_type.md)  <sub>1..1</sub>
     * Description: The type associated with this Experiment Method.
     * Range: [String](types/String.md)
 * [ExperimentMethod➞library_type](ExperimentMethod_library_type.md)  <sub>1..1</sub>
     * Description: Describe the level of omics analysis (e.g., WGS, ATAC).
     * Range: [LibraryPreparationLibraryTypeEnum](LibraryPreparationLibraryTypeEnum.md)
 * [ExperimentMethod➞library_selection_methods](ExperimentMethod_library_selection_methods.md)  <sub>1..\*</sub>
     * Description: One or more methods used to select for or against, enrich, or screen the material being sequenced (e.g., random, PCA, cDNA).
     * Range: [LibraryPreparationLibrarySelectionEnum](LibraryPreparationLibrarySelectionEnum.md)
 * [ExperimentMethod➞library_preparation](ExperimentMethod_library_preparation.md)  <sub>1..1</sub>
     * Description: The general method for preparation of the sequencing library (e.g., KAPA PCR-free).
     * Range: [String](types/String.md)
 * [ExperimentMethod➞library_preparation_kit_retail_name](ExperimentMethod_library_preparation_kit_retail_name.md)  <sub>0..1</sub>
     * Description: The retail name for the kit used to construct a genomic library. This may include the vendor name, kit name and kit version (e.g., Agilent sure select Human Exome V8, Twist RefSeq Exome).
     * Range: [LibraryPreparationKitRetailNameEnum](LibraryPreparationKitRetailNameEnum.md)
 * [ExperimentMethod➞library_preparation_kit_manufacturer](ExperimentMethod_library_preparation_kit_manufacturer.md)  <sub>0..1</sub>
     * Description: The manufacturer of the kit used for library preparation.
     * Range: [String](types/String.md)
 * [ExperimentMethod➞primer](ExperimentMethod_primer.md)  <sub>0..1</sub>
     * Description: The type of primer used for reverse transcription (e.g., oligo-dT or random).
     * Range: [PrimerEnum](PrimerEnum.md)
 * [ExperimentMethod➞end_bias](ExperimentMethod_end_bias.md)  <sub>0..1</sub>
     * Description: The end of the cDNA molecule that is preferentially sequenced (e.g., 3/5 prime end, full-length).
     * Range: [EndBiasEnum](EndBiasEnum.md)
 * [ExperimentMethod➞target_regions](ExperimentMethod_target_regions.md)  <sub>0..\*</sub>
     * Description: Subset of genes or specific regions of the genome, which are most likely to be involved in the phenotype under study.
     * Range: [String](types/String.md)
 * [ExperimentMethod➞rnaseq_strandedness](ExperimentMethod_rnaseq_strandedness.md)  <sub>0..1</sub>
     * Description: The strandedness of the library, whether reads come from both strands of the cDNA or only from the first (antisense) or the second (sense) strand.
     * Range: [LibraryPreparationRNASeqStrandednessEnum](LibraryPreparationRNASeqStrandednessEnum.md)
 * [ExperimentMethod➞instrument_model](ExperimentMethod_instrument_model.md)  <sub>1..1</sub>
     * Description: The name and model of the technology platform used to perform sequencing.
     * Range: [InstrumentModelEnum](InstrumentModelEnum.md)
 * [ExperimentMethod➞sequencing_center](ExperimentMethod_sequencing_center.md)  <sub>0..1</sub>
     * Description: Center where sample was sequenced.
     * Range: [String](types/String.md)
 * [ExperimentMethod➞sequencing_read_length](ExperimentMethod_sequencing_read_length.md)  <sub>0..1</sub>
     * Description: Length of sequencing reads (e.g., long or short or actual number of the read length).
     * Range: [String](types/String.md)
 * [ExperimentMethod➞sequencing_layout](ExperimentMethod_sequencing_layout.md)  <sub>1..1</sub>
     * Description: Describe whether the library was sequenced in single-end (forward or reverse) or paired-end mode.
     * Range: [SequencingProtocolSequencingLayoutEnum](SequencingProtocolSequencingLayoutEnum.md)
 * [ExperimentMethod➞target_coverage](ExperimentMethod_target_coverage.md)  <sub>0..1</sub>
     * Description: Mean coverage for whole genome sequencing, or mean target coverage for whole exome and targeted sequencing, (i.e. the number of times a particular locus was sequenced).
     * Range: [String](types/String.md)
 * [ExperimentMethod➞flow_cell_id](ExperimentMethod_flow_cell_id.md)  <sub>0..1</sub>
     * Description: Flow cell ID (e.g., Experiment ID_Cell 1_Lane_1).
     * Range: [String](types/String.md)
 * [ExperimentMethod➞flow_cell_type](ExperimentMethod_flow_cell_type.md)  <sub>0..1</sub>
     * Description: Type of flow cell used (e.g., S4, S2 for NovaSeq; PromethION, Flongle for Nanopore).
     * Range: [FlowCellTypeEnum](FlowCellTypeEnum.md)
 * [ExperimentMethod➞sample_barcode_read](ExperimentMethod_sample_barcode_read.md)  <sub>0..1</sub>
     * Description: The type of read that contains the sample barcode (e.g., index1, index2, read1, read2).
     * Range: [SampleBarcodeReadEnum](SampleBarcodeReadEnum.md)
 * [ExperimentMethod➞ega_accession](ExperimentMethod_ega_accession.md)  <sub>0..1</sub>
     * Description: The EGA accession of the EGA 'Experiment' entity.
     * Range: [String](types/String.md)
 * [attributes](attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
 * [ExperimentMethod➞attributes](ExperimentMethod_attributes.md)  <sub>0..\*</sub>
     * Description: One or more attributes that further characterize this Experiment Method.
     * Range: [Attribute](Attribute.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
