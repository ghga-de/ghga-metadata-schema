
# Class: SequencingProtocol


The Sequencing Protocol captures information about parameters and metadata associated with a Sequencing Experiment.

URI: [GHGA:SequencingProtocol](https://w3id.org/GHGA/SequencingProtocol)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Attribute]<attributes%200..*-++[SequencingProtocol&#124;name:string;description:string;type:string%20%3F;instrument_model:InstrumentModelEnum;sequencing_center:string%20%3F;sequencing_read_length:string%20%3F;target_coverage:string%20%3F;flow_cell_id:string%20%3F;flow_cell_type:FlowCellTypeEnum%20%3F;umi_barcode_read:IndexReadEnum%20%3F;umi_barcode_offset:string%20%3F;umi_barcode_size:string%20%3F;cell_barcode_read:IndexReadEnum%20%3F;cell_barcode_offset:string%20%3F;cell_barcode_size:string%20%3F;sample_barcode_read:SampleBarcodeReadEnum%20%3F;alias:string],[SequencingExperiment]-%20sequencing_protocol%201..1>[SequencingProtocol],[Submission]++-%20sequencing_protocols%201..*>[SequencingProtocol],[SequencingExperiment]-%20sequencing_protocol(i)%200..1>[SequencingProtocol],[Submission]-%20sequencing_protocols(i)%200..*>[SequencingProtocol],[SequencingProtocol]uses%20-.->[IdentifiedByAliasMixin],[SequencingProtocol]uses%20-.->[AttributeMixin],[SequencingExperiment],[IdentifiedByAliasMixin],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Attribute]<attributes%200..*-++[SequencingProtocol&#124;name:string;description:string;type:string%20%3F;instrument_model:InstrumentModelEnum;sequencing_center:string%20%3F;sequencing_read_length:string%20%3F;target_coverage:string%20%3F;flow_cell_id:string%20%3F;flow_cell_type:FlowCellTypeEnum%20%3F;umi_barcode_read:IndexReadEnum%20%3F;umi_barcode_offset:string%20%3F;umi_barcode_size:string%20%3F;cell_barcode_read:IndexReadEnum%20%3F;cell_barcode_offset:string%20%3F;cell_barcode_size:string%20%3F;sample_barcode_read:SampleBarcodeReadEnum%20%3F;alias:string],[SequencingExperiment]-%20sequencing_protocol%201..1>[SequencingProtocol],[Submission]++-%20sequencing_protocols%201..*>[SequencingProtocol],[SequencingExperiment]-%20sequencing_protocol(i)%200..1>[SequencingProtocol],[Submission]-%20sequencing_protocols(i)%200..*>[SequencingProtocol],[SequencingProtocol]uses%20-.->[IdentifiedByAliasMixin],[SequencingProtocol]uses%20-.->[AttributeMixin],[SequencingExperiment],[IdentifiedByAliasMixin],[AttributeMixin],[Attribute])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[SequencingExperiment](SequencingExperiment.md)** *[SequencingExperiment➞sequencing_protocol](SequencingExperiment_sequencing_protocol.md)*  <sub>1..1</sub>  **[SequencingProtocol](SequencingProtocol.md)**
 *  **[Submission](Submission.md)** *[Submission➞sequencing_protocols](Submission_sequencing_protocols.md)*  <sub>1..\*</sub>  **[SequencingProtocol](SequencingProtocol.md)**
 *  **None** *[sequencing_protocol](sequencing_protocol.md)*  <sub>0..1</sub>  **[SequencingProtocol](SequencingProtocol.md)**
 *  **None** *[sequencing_protocols](sequencing_protocols.md)*  <sub>0..\*</sub>  **[SequencingProtocol](SequencingProtocol.md)**

## Attributes


### Own

 * [SequencingProtocol➞name](SequencingProtocol_name.md)  <sub>1..1</sub>
     * Description: A short name identifying this Sequencing Protocol.
     * Range: [String](types/String.md)
 * [SequencingProtocol➞description](SequencingProtocol_description.md)  <sub>1..1</sub>
     * Description: A description summarizing the Sequencing Protocol.
     * Range: [String](types/String.md)
 * [SequencingProtocol➞type](SequencingProtocol_type.md)  <sub>0..1</sub>
     * Description: Type of the Sequencing Protocol (e.g., mRNA-seq, Whole exome long-read sequencing).
     * Range: [String](types/String.md)
 * [SequencingProtocol➞instrument_model](SequencingProtocol_instrument_model.md)  <sub>1..1</sub>
     * Description: The name and model of the technology platform used to perform sequencing.
     * Range: [InstrumentModelEnum](InstrumentModelEnum.md)
 * [SequencingProtocol➞sequencing_center](SequencingProtocol_sequencing_center.md)  <sub>0..1</sub>
     * Description: Center where sample was sequenced.
     * Range: [String](types/String.md)
 * [SequencingProtocol➞sequencing_read_length](SequencingProtocol_sequencing_read_length.md)  <sub>0..1</sub>
     * Description: Length of sequencing reads (e.g., long or short or actual number of the read length).
     * Range: [String](types/String.md)
 * [SequencingProtocol➞target_coverage](SequencingProtocol_target_coverage.md)  <sub>0..1</sub>
     * Description: Mean coverage for whole genome sequencing, or mean target coverage for whole exome and targeted sequencing, (i.e. the number of times a particular locus was sequenced).
     * Range: [String](types/String.md)
 * [SequencingProtocol➞flow_cell_id](SequencingProtocol_flow_cell_id.md)  <sub>0..1</sub>
     * Description: Flow cell ID (e.g., Experiment ID_Cell 1_Lane_1).
     * Range: [String](types/String.md)
 * [SequencingProtocol➞flow_cell_type](SequencingProtocol_flow_cell_type.md)  <sub>0..1</sub>
     * Description: Type of flow cell used (e.g., S4, S2 for NovaSeq; PromethION, Flongle for Nanopore).
     * Range: [FlowCellTypeEnum](FlowCellTypeEnum.md)
 * [SequencingProtocol➞umi_barcode_read](SequencingProtocol_umi_barcode_read.md)  <sub>0..1</sub>
     * Description: The type of read that contains the UMI barcode (e.g., index1, index2, read1, read2).
     * Range: [IndexReadEnum](IndexReadEnum.md)
 * [SequencingProtocol➞umi_barcode_offset](SequencingProtocol_umi_barcode_offset.md)  <sub>0..1</sub>
     * Description: The offset in sequence of the UMI identifying barcode (e.g., 16).
     * Range: [String](types/String.md)
 * [SequencingProtocol➞umi_barcode_size](SequencingProtocol_umi_barcode_size.md)  <sub>0..1</sub>
     * Description: The size of the UMI identifying barcode (e.g., 10).
     * Range: [String](types/String.md)
 * [SequencingProtocol➞cell_barcode_read](SequencingProtocol_cell_barcode_read.md)  <sub>0..1</sub>
     * Description: The type of read that contains the cell barcode (e.g., index1, index2, read1, read2).
     * Range: [IndexReadEnum](IndexReadEnum.md)
 * [SequencingProtocol➞cell_barcode_offset](SequencingProtocol_cell_barcode_offset.md)  <sub>0..1</sub>
     * Description: The offset in sequence of the cell identifying barcode (e.g., 0).
     * Range: [String](types/String.md)
 * [SequencingProtocol➞cell_barcode_size](SequencingProtocol_cell_barcode_size.md)  <sub>0..1</sub>
     * Description: The size of the cell identifying barcode (e.g., 16).
     * Range: [String](types/String.md)
 * [SequencingProtocol➞sample_barcode_read](SequencingProtocol_sample_barcode_read.md)  <sub>0..1</sub>
     * Description: The type of read that contains the sample barcode (e.g., index1, index2, read1, read2).
     * Range: [SampleBarcodeReadEnum](SampleBarcodeReadEnum.md)
 * [SequencingProtocol➞attributes](SequencingProtocol_attributes.md)  <sub>0..\*</sub>
     * Description: One or more attributes that further characterize this Sequencing Protocol.
     * Range: [Attribute](Attribute.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
