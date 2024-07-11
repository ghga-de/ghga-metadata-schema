
# Class: ExperimentalMethod


The Experimental Method captures the technical parameters that were used to produce output from the Sample.

URI: [GHGA:ExperimentalMethod](https://w3id.org/GHGA/ExperimentalMethod)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SupportingFile],[Submission],[IdentifiedByAliasMixin],[SupportingFile]<supporting_files%200..*-%20[ExperimentalMethod&#124;name:string;description:string;type:string;library_selection_methods:LibraryPreparationLibrarySelectionEnum%20%2B;library_preparation:string;library_preparation_kit_retail_name:LibraryPreparationKitRetailNameEnum%20%3F;library_preparation_kit_manufacturer:string%20%3F;primer:PrimerEnum%20%3F;end_bias:EndBiasEnum%20%3F;target_regions:string%20*;rnaseq_strandedness:LibraryPreparationRNASeqStrandednessEnum%20%3F;instrument_model:InstrumentModelEnum;sequencing_center:string%20%3F;sequencing_read_length:string%20%3F;sequencing_layout:SequencingProtocolSequencingLayoutEnum;target_coverage:string%20%3F;flow_cell_id:string%20%3F;flow_cell_type:FlowCellTypeEnum%20%3F;sample_barcode_read:SampleBarcodeReadEnum%20%3F;ega_accession:string%20%3F;alias:string],[Attribute]<attributes%200..*-++[ExperimentalMethod],[Experiment]-%20experimental_method%201..1>[ExperimentalMethod],[Submission]++-%20experimental_methods%201..*>[ExperimentalMethod],[Experiment]-%20experimental_method(i)%200..1>[ExperimentalMethod],[Submission]-%20experimental_methods(i)%200..*>[ExperimentalMethod],[ExperimentalMethod]uses%20-.->[IdentifiedByAliasMixin],[ExperimentalMethod]uses%20-.->[AttributeMixin],[Experiment],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[SupportingFile],[Submission],[IdentifiedByAliasMixin],[SupportingFile]<supporting_files%200..*-%20[ExperimentalMethod&#124;name:string;description:string;type:string;library_selection_methods:LibraryPreparationLibrarySelectionEnum%20%2B;library_preparation:string;library_preparation_kit_retail_name:LibraryPreparationKitRetailNameEnum%20%3F;library_preparation_kit_manufacturer:string%20%3F;primer:PrimerEnum%20%3F;end_bias:EndBiasEnum%20%3F;target_regions:string%20*;rnaseq_strandedness:LibraryPreparationRNASeqStrandednessEnum%20%3F;instrument_model:InstrumentModelEnum;sequencing_center:string%20%3F;sequencing_read_length:string%20%3F;sequencing_layout:SequencingProtocolSequencingLayoutEnum;target_coverage:string%20%3F;flow_cell_id:string%20%3F;flow_cell_type:FlowCellTypeEnum%20%3F;sample_barcode_read:SampleBarcodeReadEnum%20%3F;ega_accession:string%20%3F;alias:string],[Attribute]<attributes%200..*-++[ExperimentalMethod],[Experiment]-%20experimental_method%201..1>[ExperimentalMethod],[Submission]++-%20experimental_methods%201..*>[ExperimentalMethod],[Experiment]-%20experimental_method(i)%200..1>[ExperimentalMethod],[Submission]-%20experimental_methods(i)%200..*>[ExperimentalMethod],[ExperimentalMethod]uses%20-.->[IdentifiedByAliasMixin],[ExperimentalMethod]uses%20-.->[AttributeMixin],[Experiment],[AttributeMixin],[Attribute])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[Experiment](Experiment.md)** *[Experiment➞experimental_method](Experiment_experimental_method.md)*  <sub>1..1</sub>  **[ExperimentalMethod](ExperimentalMethod.md)**
 *  **[Submission](Submission.md)** *[Submission➞experimental_methods](Submission_experimental_methods.md)*  <sub>1..\*</sub>  **[ExperimentalMethod](ExperimentalMethod.md)**
 *  **None** *[experimental_method](experimental_method.md)*  <sub>0..1</sub>  **[ExperimentalMethod](ExperimentalMethod.md)**
 *  **None** *[experimental_methods](experimental_methods.md)*  <sub>0..\*</sub>  **[ExperimentalMethod](ExperimentalMethod.md)**

## Attributes


### Own

 * [ExperimentalMethod➞name](ExperimentalMethod_name.md)  <sub>1..1</sub>
     * Description: A short name identifying this Experimental Method.
     * Range: [String](types/String.md)
 * [ExperimentalMethod➞description](ExperimentalMethod_description.md)  <sub>1..1</sub>
     * Description: A short description of this Experimental Method.
     * Range: [String](types/String.md)
 * [ExperimentalMethod➞type](ExperimentalMethod_type.md)  <sub>1..1</sub>
     * Description: The type associated with this Experimental Method.
     * Range: [String](types/String.md)
 * [ExperimentalMethod➞library_selection_methods](ExperimentalMethod_library_selection_methods.md)  <sub>1..\*</sub>
     * Description: One or more methods used to select for or against, enrich, or screen the material being sequenced (e.g., random, PCA, cDNA).
     * Range: [LibraryPreparationLibrarySelectionEnum](LibraryPreparationLibrarySelectionEnum.md)
 * [ExperimentalMethod➞library_preparation](ExperimentalMethod_library_preparation.md)  <sub>1..1</sub>
     * Description: The general method for preparation of the sequencing library (e.g., KAPA PCR-free).
     * Range: [String](types/String.md)
 * [ExperimentalMethod➞library_preparation_kit_retail_name](ExperimentalMethod_library_preparation_kit_retail_name.md)  <sub>0..1</sub>
     * Description: The retail name for the kit used to construct a genomic library. This may include the vendor name, kit name and kit version (e.g., Agilent sure select Human Exome V8, Twist RefSeq Exome).
     * Range: [LibraryPreparationKitRetailNameEnum](LibraryPreparationKitRetailNameEnum.md)
 * [ExperimentalMethod➞library_preparation_kit_manufacturer](ExperimentalMethod_library_preparation_kit_manufacturer.md)  <sub>0..1</sub>
     * Description: The manufacturer of the kit used for library preparation.
     * Range: [String](types/String.md)
 * [ExperimentalMethod➞primer](ExperimentalMethod_primer.md)  <sub>0..1</sub>
     * Description: The type of primer used for reverse transcription (e.g., oligo-dT or random).
     * Range: [PrimerEnum](PrimerEnum.md)
 * [ExperimentalMethod➞end_bias](ExperimentalMethod_end_bias.md)  <sub>0..1</sub>
     * Description: The end of the cDNA molecule that is preferentially sequenced (e.g., 3/5 prime end, full-length).
     * Range: [EndBiasEnum](EndBiasEnum.md)
 * [ExperimentalMethod➞target_regions](ExperimentalMethod_target_regions.md)  <sub>0..\*</sub>
     * Description: Subset of genes or specific regions of the genome, which are most likely to be involved in the phenotype under study.
     * Range: [String](types/String.md)
 * [ExperimentalMethod➞rnaseq_strandedness](ExperimentalMethod_rnaseq_strandedness.md)  <sub>0..1</sub>
     * Description: The strandedness of the library, whether reads come from both strands of the cDNA or only from the first (antisense) or the second (sense) strand.
     * Range: [LibraryPreparationRNASeqStrandednessEnum](LibraryPreparationRNASeqStrandednessEnum.md)
 * [ExperimentalMethod➞instrument_model](ExperimentalMethod_instrument_model.md)  <sub>1..1</sub>
     * Description: The name and model of the technology platform used to perform sequencing.
     * Range: [InstrumentModelEnum](InstrumentModelEnum.md)
 * [ExperimentalMethod➞sequencing_center](ExperimentalMethod_sequencing_center.md)  <sub>0..1</sub>
     * Description: Center where sample was sequenced.
     * Range: [String](types/String.md)
 * [ExperimentalMethod➞sequencing_read_length](ExperimentalMethod_sequencing_read_length.md)  <sub>0..1</sub>
     * Description: Length of sequencing reads (e.g., long or short or actual number of the read length).
     * Range: [String](types/String.md)
 * [ExperimentalMethod➞sequencing_layout](ExperimentalMethod_sequencing_layout.md)  <sub>1..1</sub>
     * Description: Describe whether the library was sequenced in single-end (forward or reverse) or paired-end mode.
     * Range: [SequencingProtocolSequencingLayoutEnum](SequencingProtocolSequencingLayoutEnum.md)
 * [ExperimentalMethod➞target_coverage](ExperimentalMethod_target_coverage.md)  <sub>0..1</sub>
     * Description: Mean coverage for whole genome sequencing, or mean target coverage for whole exome and targeted sequencing, (i.e. the number of times a particular locus was sequenced).
     * Range: [String](types/String.md)
 * [ExperimentalMethod➞flow_cell_id](ExperimentalMethod_flow_cell_id.md)  <sub>0..1</sub>
     * Description: Flow cell ID (e.g., Experiment ID_Cell 1_Lane_1).
     * Range: [String](types/String.md)
 * [ExperimentalMethod➞flow_cell_type](ExperimentalMethod_flow_cell_type.md)  <sub>0..1</sub>
     * Description: Type of flow cell used (e.g., S4, S2 for NovaSeq; PromethION, Flongle for Nanopore).
     * Range: [FlowCellTypeEnum](FlowCellTypeEnum.md)
 * [ExperimentalMethod➞sample_barcode_read](ExperimentalMethod_sample_barcode_read.md)  <sub>0..1</sub>
     * Description: The type of read that contains the sample barcode (e.g., index1, index2, read1, read2).
     * Range: [SampleBarcodeReadEnum](SampleBarcodeReadEnum.md)
 * [ExperimentalMethod➞ega_accession](ExperimentalMethod_ega_accession.md)  <sub>0..1</sub>
     * Description: The EGA accession of the EGA 'Assay' entity.
     * Range: [String](types/String.md)
 * [attributes](attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
 * [ExperimentalMethod➞supporting_files](ExperimentalMethod_supporting_files.md)  <sub>0..\*</sub>
     * Description: The alias of one or more Supporting Files that are associated with this Experimental Method.
     * Range: [SupportingFile](SupportingFile.md)
 * [ExperimentalMethod➞attributes](ExperimentalMethod_attributes.md)  <sub>0..\*</sub>
     * Description: One or more attributes that further characterize this Experimental Method.
     * Range: [Attribute](Attribute.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
