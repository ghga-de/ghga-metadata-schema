
# Class: library preparation protocol


Information about the library preparation of an Experiment.

URI: [GHGA:LibraryPreparationProtocol](https://w3id.org/GHGA/LibraryPreparationProtocol)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Protocol],[Attribute]<has%20attribute%200..*-++[LibraryPreparationProtocol&#124;library_name:string;library_layout:string;library_type:string;library_selection:string;library_preparation:string;library_preparation_kit_retail_name:string%20%3F;library_preparation_kit_manufacturer:string%20%3F;primer:string%20%3F;end_bias:string%20%3F;target_regions:string;rnaseq_strandedness:string%20%3F;alias:string;description:string;name(i):string%20%3F;type(i):string%20%3F;url(i):string%20%3F;xref(i):string%20*;id(i):string;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Protocol]^-[LibraryPreparationProtocol],[File],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Protocol],[Attribute]<has%20attribute%200..*-++[LibraryPreparationProtocol&#124;library_name:string;library_layout:string;library_type:string;library_selection:string;library_preparation:string;library_preparation_kit_retail_name:string%20%3F;library_preparation_kit_manufacturer:string%20%3F;primer:string%20%3F;end_bias:string%20%3F;target_regions:string;rnaseq_strandedness:string%20%3F;alias:string;description:string;name(i):string%20%3F;type(i):string%20%3F;url(i):string%20%3F;xref(i):string%20*;id(i):string;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Protocol]^-[LibraryPreparationProtocol],[File],[Attribute])

## Parents

 *  is_a: [Protocol](Protocol.md) - A plan specification which has sufficient level of detail and quantitative information to communicate it between investigation agents, so that different investigation agents will reliably be able to independently reproduce the process.

## Referenced by Class


## Attributes


### Own

 * [library preparation protocol➞library name](library_preparation_protocol_library_name.md)  <sub>1..1</sub>
     * Description: A short name identifying the library to potential users. The same name may refer to multiple versions of the same continually updated library.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [library preparation protocol➞library layout](library_preparation_protocol_library_layout.md)  <sub>1..1</sub>
     * Description: Describe whether the library was sequenced in single-end (forward or reverse) or paired-end mode
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [library preparation protocol➞library type](library_preparation_protocol_library_type.md)  <sub>1..1</sub>
     * Description: Describe the level of omics analysis (eg: Metagenome, transcriptome, etc)
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [library preparation protocol➞library selection](library_preparation_protocol_library_selection.md)  <sub>1..1</sub>
     * Description: Whether any method was used to select for or against, enrich, or screen the material being sequenced. Library Selection method (e.g. random, PCA, cDNA, etc )
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [library preparation protocol➞library preparation](library_preparation_protocol_library_preparation.md)  <sub>1..1</sub>
     * Description: The general method for sequencing library preparation (e.g. KAPA PCR-free).
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [library preparation protocol➞library preparation kit retail name](library_preparation_protocol_library_preparation_kit_retail_name.md)  <sub>0..1</sub>
     * Description: A unique identifier for the kit used to construct a genomic library. This may include the vendor name, kit name and kit version  (e.g. Agilent sure select Human Exome V8, Twist RefSeq Exome, etc.)
     * Range: [String](types/String.md)
     * in subsets: (recommended,public)
 * [library preparation protocol➞library preparation kit manufacturer](library_preparation_protocol_library_preparation_kit_manufacturer.md)  <sub>0..1</sub>
     * Description: Manufacturer of library preparation kit
     * Range: [String](types/String.md)
     * in subsets: (recommended,public)
 * [primer](primer.md)  <sub>0..1</sub>
     * Description: The type of primer used for reverse transcription, e.g. 'oligo-dT' or 'random' primer. This allows users to identify content of the cDNA library input e.g. enriched for mRNA.
     * Range: [String](types/String.md)
     * in subsets: (recommended,public)
 * [end bias](end_bias.md)  <sub>0..1</sub>
     * Description: The end of the cDNA molecule that is preferentially sequenced, e.g. 3/5 prime tag or end, or the full-length transcript.
     * Range: [String](types/String.md)
     * in subsets: (recommended,public)
 * [library preparation protocol➞target regions](library_preparation_protocol_target_regions.md)  <sub>1..1</sub>
     * Description: Subset of genes or specific regions of the genome, which are most likely to be involved in the phenotype under study.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [rnaseq strandedness](rnaseq_strandedness.md)  <sub>0..1</sub>
     * Description: The strandedness of the library, whether reads come from both strands of the cDNA or only from the first (antisense) or the second (sense) strand.
     * Range: [String](types/String.md)
     * in subsets: (recommended,public)
 * [library preparation protocol➞alias](library_preparation_protocol_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [library preparation protocol➞description](library_preparation_protocol_description.md)  <sub>1..1</sub>
     * Description: Description about how a sequencing library was prepared (eg: Library construction method).
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [library preparation protocol➞has attribute](library_preparation_protocol_has_attribute.md)  <sub>0..\*</sub>
     * Description: One or more attributes that further characterizes this Library Preparation Protocol.
     * Range: [Attribute](Attribute.md)
     * in subsets: (optional,restricted)

### Inherited from protocol:

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
 * [protocol➞name](protocol_name.md)  <sub>0..1</sub>
     * Description: Name of the protocol (eg: Sample extraction_PCR amplification).
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [protocol➞type](protocol_type.md)  <sub>0..1</sub>
     * Description: Type of the protocol (eg: Target enrichment).
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [protocol➞url](protocol_url.md)  <sub>0..1</sub>
     * Description: URL for the resource that describes this Protocol.
     * Range: [String](types/String.md)
 * [protocol➞has file](protocol_has_file.md)  <sub>0..1</sub>
     * Description: A document that describes the Protocol.
     * Range: [File](File.md)
     * in subsets: (essential,restricted)
 * [protocol➞xref](protocol_xref.md)  <sub>0..\*</sub>
     * Description: One or more cross-references for this Protocol.  (Eg: manufacturer protocol, protocol from publication etc )
     * Range: [String](types/String.md)
     * in subsets: (optional,public)
