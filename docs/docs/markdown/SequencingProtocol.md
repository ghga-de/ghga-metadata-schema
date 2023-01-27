
# Class: sequencing protocol


Information about the sequencing of a sample.

URI: [GHGA:SequencingProtocol](https://w3id.org/GHGA/SequencingProtocol)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Attribute]<has%20attribute%201..*-++[SequencingProtocol&#124;sequencing_center:string%20%3F;instrument_model:string;paired_or_single_end:paired_or_single_end_enum%20%3F;forward_or_reverse:forward_or_reverse_enum%20%3F;sequencing_read_length:string%20%3F;index_sequence:string%20%3F;target_coverage:string%20%3F;lane_number:string%20%3F;flow_cell_id:string%20%3F;flow_cell_type:string%20%3F;umi_barcode_read:string%20%3F;umi_barcode_size:string%20%3F;umi_barcode_offset:string%20%3F;cell_barcode_read:string%20%3F;cell_barcode_offset:string%20%3F;cell_barcode_size:string%20%3F;sample_barcode_read:string%20%3F;alias:string;type:string;description:string;name(i):string;url(i):string;xref(i):string%20%2B;id(i):string;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[Protocol]^-[SequencingProtocol],[Protocol],[File],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Attribute]<has%20attribute%201..*-++[SequencingProtocol&#124;sequencing_center:string%20%3F;instrument_model:string;paired_or_single_end:paired_or_single_end_enum%20%3F;forward_or_reverse:forward_or_reverse_enum%20%3F;sequencing_read_length:string%20%3F;index_sequence:string%20%3F;target_coverage:string%20%3F;lane_number:string%20%3F;flow_cell_id:string%20%3F;flow_cell_type:string%20%3F;umi_barcode_read:string%20%3F;umi_barcode_size:string%20%3F;umi_barcode_offset:string%20%3F;cell_barcode_read:string%20%3F;cell_barcode_offset:string%20%3F;cell_barcode_size:string%20%3F;sample_barcode_read:string%20%3F;alias:string;type:string;description:string;name(i):string;url(i):string;xref(i):string%20%2B;id(i):string;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[Protocol]^-[SequencingProtocol],[Protocol],[File],[Attribute])

## Parents

 *  is_a: [Protocol](Protocol.md) - A plan specification which has sufficient level of detail and quantitative information to communicate it between investigation agents, so that different investigation agents will reliably be able to independently reproduce the process.

## Referenced by Class

 *  **None** *[has sequencing protocol](has_sequencing_protocol.md)*  <sub>0..1</sub>  **[SequencingProtocol](SequencingProtocol.md)**

## Attributes


### Own

 * [sequencing protocol➞sequencing center](sequencing_protocol_sequencing_center.md)  <sub>0..1</sub>
     * Description: Center where sample was sequenced.
     * Range: [String](types/String.md)
 * [sequencing protocol➞instrument model](sequencing_protocol_instrument_model.md)  <sub>1..1</sub>
     * Description: The name and model of the technology platform used to perform sequencing.
     * Range: [String](types/String.md)
 * [sequencing protocol➞paired or single end](sequencing_protocol_paired_or_single_end.md)  <sub>0..1</sub>
     * Description: Denotes whether a submitted FASTQ file contains forward (R1) or reverse (R2) reads for paired-end sequencing. The number that identifies each read direction in a paired-end nucleotide sequencing replications.
     * Range: [paired or single end enum](paired or single end enum.md)
 * [sequencing protocol➞forward or reverse](sequencing_protocol_forward_or_reverse.md)  <sub>0..1</sub>
     * Description: Denotes whether a submitted FASTQ file contains forward (R1) or reverse (R2) reads for paired-end sequencing. The number that identifies each read direction in a paired-end nucleotide sequencing reaction.
     * Range: [forward or reverse enum](forward or reverse enum.md)
 * [sequencing protocol➞sequencing read length](sequencing_protocol_sequencing_read_length.md)  <sub>0..1</sub>
     * Description: Length of sequencing reads (eg: Long or short or actual number of the read length etc). The number of nucleotides successfully ordered from each side of a nucleic acid fragment obtained after the completion of a sequencing process
     * Range: [String](types/String.md)
 * [sequencing protocol➞index sequence](sequencing_protocol_index_sequence.md)  <sub>0..1</sub>
     * Description: A unique nucleotide sequence that is added to a sample during library preparation to serve as a unique identifier for the sample.
     * Range: [String](types/String.md)
 * [sequencing protocol➞target coverage](sequencing_protocol_target_coverage.md)  <sub>0..1</sub>
     * Description: Mean coverage for whole genome sequencing, or mean target coverage for whole exome and targeted sequencing. The number of times a particular locus (site, nucleotide, amplicon, region) was sequenced.
     * Range: [String](types/String.md)
 * [sequencing protocol➞lane number](sequencing_protocol_lane_number.md)  <sub>0..1</sub>
     * Description: The numerical identifier for the lane or machine unit where a sample was located during nucleotide sequencing.
     * Range: [String](types/String.md)
 * [sequencing protocol➞flow cell id](sequencing_protocol_flow_cell_id.md)  <sub>0..1</sub>
     * Description: Flow Cell ID (eg: Experiment ID_Cell 1_Lane_1). The barcode assigned to a flow cell used in nucleotide sequencing.
     * Range: [String](types/String.md)
 * [sequencing protocol➞flow cell type](sequencing_protocol_flow_cell_type.md)  <sub>0..1</sub>
     * Description: Type of flow cell used (e.g. S4, S2 for NovaSeq; PromethION, Flongle for Nanopore). Aparatus in the fluidic subsystem where the sheath and sample meet. Can be one of several types; jet-in-air, quartz cuvette, or a hybrid of the two. The sample flows through the center of a fluid column of sheath fluid in the flow cell.
     * Range: [String](types/String.md)
 * [sequencing protocol➞umi barcode read](sequencing_protocol_umi_barcode_read.md)  <sub>0..1</sub>
     * Description: The type of read that contains the UMI barcode (Eg: index1/index2/read1/read2).
     * Range: [String](types/String.md)
 * [sequencing protocol➞umi barcode size](sequencing_protocol_umi_barcode_size.md)  <sub>0..1</sub>
     * Description: The size of the UMI identifying barcode (Eg. '10').
     * Range: [String](types/String.md)
 * [sequencing protocol➞umi barcode offset](sequencing_protocol_umi_barcode_offset.md)  <sub>0..1</sub>
     * Description: The offset in sequence of the UMI identifying barcode. (E.g. '16').
     * Range: [String](types/String.md)
 * [sequencing protocol➞cell barcode read](sequencing_protocol_cell_barcode_read.md)  <sub>0..1</sub>
     * Description: The type of read that contains the cell barcode (eg: index1/index2/read1/read2).
     * Range: [String](types/String.md)
 * [sequencing protocol➞cell barcode offset](sequencing_protocol_cell_barcode_offset.md)  <sub>0..1</sub>
     * Description: The offset in sequence of the cell identifying barcode. (Eg. '0').
     * Range: [String](types/String.md)
 * [sequencing protocol➞cell barcode size](sequencing_protocol_cell_barcode_size.md)  <sub>0..1</sub>
     * Description: The size of the cell identifying barcode (E.g. '16').
     * Range: [String](types/String.md)
 * [sequencing protocol➞sample barcode read](sequencing_protocol_sample_barcode_read.md)  <sub>0..1</sub>
     * Description: The type of read that contains the sample barcode (eg: index1/index2/read1/read2).
     * Range: [String](types/String.md)
 * [sequencing protocol➞alias](sequencing_protocol_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [sequencing protocol➞type](sequencing_protocol_type.md)  <sub>1..1</sub>
     * Description: Name of the library preparation protocol (eg: mRNA-seq,Whole exome long-read sequencing etc).
     * Range: [String](types/String.md)
 * [sequencing protocol➞description](sequencing_protocol_description.md)  <sub>1..1</sub>
     * Description: Description about the sequencing protocol (eg: mRNA-seq,Whole exome long-read sequencing etc).
     * Range: [String](types/String.md)
 * [sequencing protocol➞has attribute](sequencing_protocol_has_attribute.md)  <sub>1..\*</sub>
     * Description: One or more attributes that further characterizes this Sequencing Protocol.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

### Inherited from protocol:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞creation date](named_thing_creation_date.md)  <sub>1..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was created.
     * Range: [String](types/String.md)
 * [named thing➞update date](named_thing_update_date.md)  <sub>1..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was updated.
     * Range: [String](types/String.md)
 * [protocol➞name](protocol_name.md)  <sub>1..1</sub>
     * Description: Name of the protocol (eg: Sample extraction_PCR amplification).
     * Range: [String](types/String.md)
 * [protocol➞url](protocol_url.md)  <sub>1..1</sub>
     * Description: URL for the resource that describes this Protocol.
     * Range: [String](types/String.md)
 * [protocol➞has file](protocol_has_file.md)  <sub>1..1</sub>
     * Description: A document that describes the Protocol.
     * Range: [File](File.md)
     * in subsets: (restricted)
 * [protocol➞xref](protocol_xref.md)  <sub>1..\*</sub>
     * Description: One or more cross-references for this Protocol.  (Eg: manufacturer protocol, protocol from publication etc )
     * Range: [String](types/String.md)
