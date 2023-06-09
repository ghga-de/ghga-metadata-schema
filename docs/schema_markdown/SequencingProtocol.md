
# Class: SequencingProtocol


Information about the sequencing of a sample.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/SequencingProtocol](https://w3id.org/GHGA-Submission-Metadata-Schema/SequencingProtocol)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Attribute]<attributes%200..*-++[SequencingProtocol&#124;description:string;type:string%20%3F;instrument_model:InstrumentModelEnum;sequencing_center:string%20%3F;sequencing_read_length:string%20%3F;forward_or_reverse:ForwardOrReverseEnum%20%3F;target_coverage:string%20%3F;flow_cell_id:string%20%3F;flow_cell_type:FlowCellTypeEnum%20%3F;umi_barcode_read:IndexReadEnum%20%3F;umi_barcode_offset:string%20%3F;umi_barcode_size:string%20%3F;cell_barcode_read:IndexReadEnum%20%3F;cell_barcode_offset:string%20%3F;cell_barcode_size:string%20%3F;sample_barcode_read:SampleBarcodeReadEnum%20%3F;index_sequence:string%20%3F;lane_number:string%20%3F;alias:string],[SequencingExperiment]-%20sequencing_protocol%201..1>[SequencingProtocol],[Submission]++-%20sequencing_protocols%200..*>[SequencingProtocol],[SequencingExperiment]-%20sequencing_protocol(i)%200..1>[SequencingProtocol],[Submission]-%20sequencing_protocols(i)%200..*>[SequencingProtocol],[SequencingProtocol]uses%20-.->[IdentifiedByAliasMixin],[SequencingProtocol]uses%20-.->[AttributeMixin],[SequencingExperiment],[IdentifiedByAliasMixin],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Attribute]<attributes%200..*-++[SequencingProtocol&#124;description:string;type:string%20%3F;instrument_model:InstrumentModelEnum;sequencing_center:string%20%3F;sequencing_read_length:string%20%3F;forward_or_reverse:ForwardOrReverseEnum%20%3F;target_coverage:string%20%3F;flow_cell_id:string%20%3F;flow_cell_type:FlowCellTypeEnum%20%3F;umi_barcode_read:IndexReadEnum%20%3F;umi_barcode_offset:string%20%3F;umi_barcode_size:string%20%3F;cell_barcode_read:IndexReadEnum%20%3F;cell_barcode_offset:string%20%3F;cell_barcode_size:string%20%3F;sample_barcode_read:SampleBarcodeReadEnum%20%3F;index_sequence:string%20%3F;lane_number:string%20%3F;alias:string],[SequencingExperiment]-%20sequencing_protocol%201..1>[SequencingProtocol],[Submission]++-%20sequencing_protocols%200..*>[SequencingProtocol],[SequencingExperiment]-%20sequencing_protocol(i)%200..1>[SequencingProtocol],[Submission]-%20sequencing_protocols(i)%200..*>[SequencingProtocol],[SequencingProtocol]uses%20-.->[IdentifiedByAliasMixin],[SequencingProtocol]uses%20-.->[AttributeMixin],[SequencingExperiment],[IdentifiedByAliasMixin],[AttributeMixin],[Attribute])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[SequencingExperiment](SequencingExperiment.md)** *[SequencingExperiment➞sequencing_protocol](SequencingExperiment_sequencing_protocol.md)*  <sub>1..1</sub>  **[SequencingProtocol](SequencingProtocol.md)**
 *  **[Submission](Submission.md)** *[Submission➞sequencing_protocols](Submission_sequencing_protocols.md)*  <sub>0..\*</sub>  **[SequencingProtocol](SequencingProtocol.md)**
 *  **None** *[sequencing_protocol](sequencing_protocol.md)*  <sub>0..1</sub>  **[SequencingProtocol](SequencingProtocol.md)**
 *  **None** *[sequencing_protocols](sequencing_protocols.md)*  <sub>0..\*</sub>  **[SequencingProtocol](SequencingProtocol.md)**

## Attributes


### Own

 * [SequencingProtocol➞description](SequencingProtocol_description.md)  <sub>1..1</sub>
     * Description: Description about the sequencing Protocol (eg: mRNA-seq,Whole exome long-read sequencing etc).
     * Range: [String](types/String.md)
 * [SequencingProtocol➞type](SequencingProtocol_type.md)  <sub>0..1</sub>
     * Description: Name of the library_preparation Protocol (eg: mRNA-seq,Whole exome long-read sequencing etc).
     * Range: [String](types/String.md)
 * [SequencingProtocol➞instrument_model](SequencingProtocol_instrument_model.md)  <sub>1..1</sub>
     * Description: The name and model of the technology platform used to perform sequencing.
     * Range: [InstrumentModelEnum](InstrumentModelEnum.md)
 * [SequencingProtocol➞sequencing_center](SequencingProtocol_sequencing_center.md)  <sub>0..1</sub>
     * Description: Center where sample was sequenced.
     * Range: [String](types/String.md)
 * [SequencingProtocol➞sequencing_read_length](SequencingProtocol_sequencing_read_length.md)  <sub>0..1</sub>
     * Description: Length of sequencing reads (eg: Long or short or actual number of the read length etc). The number of nucleotides successfully ordered from each side of a nucleic acid fragment obtained after the completion of a sequencing process
     * Range: [String](types/String.md)
 * [SequencingProtocol➞forward_or_reverse](SequencingProtocol_forward_or_reverse.md)  <sub>0..1</sub>
     * Description: Denotes whether a submitted FASTQ file contains forward (R1) or reverse (R2) reads for paired-end sequencing. The number that identifies each read direction in a paired-end nucleotide sequencing reaction.
     * Range: [ForwardOrReverseEnum](ForwardOrReverseEnum.md)
 * [SequencingProtocol➞target_coverage](SequencingProtocol_target_coverage.md)  <sub>0..1</sub>
     * Description: Mean coverage for whole genome sequencing, or mean target coverage for whole exome and targeted sequencing. The number of times a particular locus (site, nucleotide, amplicon, region) was sequenced.
     * Range: [String](types/String.md)
 * [SequencingProtocol➞flow_cell_id](SequencingProtocol_flow_cell_id.md)  <sub>0..1</sub>
     * Description: Flow Cell ID (eg: Experiment ID_Cell 1_Lane_1). The barcode assigned to a flow cell used in nucleotide sequencing.
     * Range: [String](types/String.md)
 * [SequencingProtocol➞flow_cell_type](SequencingProtocol_flow_cell_type.md)  <sub>0..1</sub>
     * Description: Type of flow cell used (e.g. S4, S2 for NovaSeq; PromethION, Flongle for Nanopore). Aparatus in the fluidic subsystem where the sheath and sample meet. Can be one of several types; jet-in-air, quartz cuvette, or a hybrid of the two. The sample flows through the center of a fluid column of sheath fluid in the flow cell.
     * Range: [FlowCellTypeEnum](FlowCellTypeEnum.md)
 * [SequencingProtocol➞umi_barcode_read](SequencingProtocol_umi_barcode_read.md)  <sub>0..1</sub>
     * Description: The type of read that contains the UMI barcode (Eg: index1/index2/read1/read2).
     * Range: [IndexReadEnum](IndexReadEnum.md)
 * [SequencingProtocol➞umi_barcode_offset](SequencingProtocol_umi_barcode_offset.md)  <sub>0..1</sub>
     * Description: The offset in sequence of the UMI identifying barcode. (E.g. '16').
     * Range: [String](types/String.md)
 * [SequencingProtocol➞umi_barcode_size](SequencingProtocol_umi_barcode_size.md)  <sub>0..1</sub>
     * Description: The size of the UMI identifying barcode (Eg. '10').
     * Range: [String](types/String.md)
 * [SequencingProtocol➞cell_barcode_read](SequencingProtocol_cell_barcode_read.md)  <sub>0..1</sub>
     * Description: The type of read that contains the cell barcode (eg: index1/index2/read1/read2).
     * Range: [IndexReadEnum](IndexReadEnum.md)
 * [SequencingProtocol➞cell_barcode_offset](SequencingProtocol_cell_barcode_offset.md)  <sub>0..1</sub>
     * Description: The offset in sequence of the cell identifying barcode. (Eg. '0').
     * Range: [String](types/String.md)
 * [SequencingProtocol➞cell_barcode_size](SequencingProtocol_cell_barcode_size.md)  <sub>0..1</sub>
     * Description: The size of the cell identifying barcode (E.g. '16').
     * Range: [String](types/String.md)
 * [SequencingProtocol➞sample_barcode_read](SequencingProtocol_sample_barcode_read.md)  <sub>0..1</sub>
     * Description: The type of read that contains the sample barcode (eg: index1/index2/read1/read2).
     * Range: [SampleBarcodeReadEnum](SampleBarcodeReadEnum.md)
 * [SequencingProtocol➞index_sequence](SequencingProtocol_index_sequence.md)  <sub>0..1</sub>
     * Description: A unique nucleotide sequence that is added to a sample during library_preparation to serve as a unique identifier for the sample.
     * Range: [String](types/String.md)
 * [SequencingProtocol➞lane_number](SequencingProtocol_lane_number.md)  <sub>0..1</sub>
     * Description: The numerical identifier for the lane or machine unit where a sample was located during nucleotide sequencing.
     * Range: [String](types/String.md)
 * [SequencingProtocol➞attributes](SequencingProtocol_attributes.md)  <sub>0..\*</sub>
     * Description: One or more attributes that further characterizes this Sequencing Protocol.
     * Range: [Attribute](Attribute.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
