
# Class: LibraryPreparationProtocol


Information about the library_preparation of an sequencing experiment.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/LibraryPreparationProtocol](https://w3id.org/GHGA-Submission-Metadata-Schema/LibraryPreparationProtocol)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingExperiment],[Protocol],[Attribute]<attributes%200..*-++[LibraryPreparationProtocol&#124;library_name:string;library_layout:LibraryPreparationLibraryLayoutEnum;library_type:LibraryPreparationLibraryTypeEnum;library_selection:LibraryPreparationLibrarySelectionEnum;library_preparation:string;library_preparation_kit_retail_name:LibraryPreparationKitRetailNameEnum%20%3F;library_preparation_kit_manufacturer:string%20%3F;primer:PrimerEnum%20%3F;end_bias:EndBiasEnum%20%3F;target_regions:string%20*;rnaseq_strandedness:LibraryPreparationRNASeqStrandednessEnum%20%3F;description:string;alias:string;name(i):string;type(i):string;url(i):string;xref(i):string%20%2B],[SequencingExperiment]-%20library_preparation_protocol%201..1>[LibraryPreparationProtocol],[Submission]++-%20library_preparation_protocols%200..*>[LibraryPreparationProtocol],[SequencingExperiment]-%20library_preparation_protocol(i)%200..1>[LibraryPreparationProtocol],[Submission]-%20library_preparation_protocols(i)%200..*>[LibraryPreparationProtocol],[LibraryPreparationProtocol]uses%20-.->[IdentifiedByAliasMixin],[Protocol]^-[LibraryPreparationProtocol],[IdentifiedByAliasMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingExperiment],[Protocol],[Attribute]<attributes%200..*-++[LibraryPreparationProtocol&#124;library_name:string;library_layout:LibraryPreparationLibraryLayoutEnum;library_type:LibraryPreparationLibraryTypeEnum;library_selection:LibraryPreparationLibrarySelectionEnum;library_preparation:string;library_preparation_kit_retail_name:LibraryPreparationKitRetailNameEnum%20%3F;library_preparation_kit_manufacturer:string%20%3F;primer:PrimerEnum%20%3F;end_bias:EndBiasEnum%20%3F;target_regions:string%20*;rnaseq_strandedness:LibraryPreparationRNASeqStrandednessEnum%20%3F;description:string;alias:string;name(i):string;type(i):string;url(i):string;xref(i):string%20%2B],[SequencingExperiment]-%20library_preparation_protocol%201..1>[LibraryPreparationProtocol],[Submission]++-%20library_preparation_protocols%200..*>[LibraryPreparationProtocol],[SequencingExperiment]-%20library_preparation_protocol(i)%200..1>[LibraryPreparationProtocol],[Submission]-%20library_preparation_protocols(i)%200..*>[LibraryPreparationProtocol],[LibraryPreparationProtocol]uses%20-.->[IdentifiedByAliasMixin],[Protocol]^-[LibraryPreparationProtocol],[IdentifiedByAliasMixin],[Attribute])

## Parents

 *  is_a: [Protocol](Protocol.md) - A plan specification which has sufficient level of detail and quantitative information to communicate it between Investigation agents, so that different Investigation agents will reliably be able to independently reproduce the process.

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

 *  **[SequencingExperiment](SequencingExperiment.md)** *[SequencingExperiment➞library_preparation_protocol](SequencingExperiment_library_preparation_protocol.md)*  <sub>1..1</sub>  **[LibraryPreparationProtocol](LibraryPreparationProtocol.md)**
 *  **[Submission](Submission.md)** *[Submission➞library_preparation_protocols](Submission_library_preparation_protocols.md)*  <sub>0..\*</sub>  **[LibraryPreparationProtocol](LibraryPreparationProtocol.md)**
 *  **None** *[library_preparation_protocol](library_preparation_protocol.md)*  <sub>0..1</sub>  **[LibraryPreparationProtocol](LibraryPreparationProtocol.md)**
 *  **None** *[library_preparation_protocols](library_preparation_protocols.md)*  <sub>0..\*</sub>  **[LibraryPreparationProtocol](LibraryPreparationProtocol.md)**

## Attributes


### Own

 * [LibraryPreparationProtocol➞library_name](LibraryPreparationProtocol_library_name.md)  <sub>1..1</sub>
     * Description: A short name identifying the library to potential users. The same name may refer to multiple versions of the same continually updated library.
     * Range: [String](types/String.md)
 * [LibraryPreparationProtocol➞library_layout](LibraryPreparationProtocol_library_layout.md)  <sub>1..1</sub>
     * Description: Describe whether the library was sequenced in single-end (forward or reverse) or paired-end mode
     * Range: [LibraryPreparationLibraryLayoutEnum](LibraryPreparationLibraryLayoutEnum.md)
 * [LibraryPreparationProtocol➞library_type](LibraryPreparationProtocol_library_type.md)  <sub>1..1</sub>
     * Description: Describe the level of omics analysis (eg: Metagenome, transcriptome, etc)
     * Range: [LibraryPreparationLibraryTypeEnum](LibraryPreparationLibraryTypeEnum.md)
 * [LibraryPreparationProtocol➞library_selection](LibraryPreparationProtocol_library_selection.md)  <sub>1..1</sub>
     * Description: Whether any method was used to select for or against, enrich, or screen the material being sequenced. library_selection method (e.g. random, PCA, cDNA, etc )
     * Range: [LibraryPreparationLibrarySelectionEnum](LibraryPreparationLibrarySelectionEnum.md)
 * [LibraryPreparationProtocol➞library_preparation](LibraryPreparationProtocol_library_preparation.md)  <sub>1..1</sub>
     * Description: The general method for sequencing library_preparation (e.g. KAPA PCR-free).
     * Range: [String](types/String.md)
 * [LibraryPreparationProtocol➞library_preparation_kit_retail_name](LibraryPreparationProtocol_library_preparation_kit_retail_name.md)  <sub>0..1</sub>
     * Description: A unique identifier for the kit used to construct a genomic library. This may include the vendor name, kit name and kit version  (e.g. Agilent sure select Human Exome V8, Twist RefSeq Exome, etc.)
     * Range: [LibraryPreparationKitRetailNameEnum](LibraryPreparationKitRetailNameEnum.md)
 * [LibraryPreparationProtocol➞library_preparation_kit_manufacturer](LibraryPreparationProtocol_library_preparation_kit_manufacturer.md)  <sub>0..1</sub>
     * Description: Manufacturer of library_preparation kit
     * Range: [String](types/String.md)
 * [LibraryPreparationProtocol➞primer](LibraryPreparationProtocol_primer.md)  <sub>0..1</sub>
     * Description: The type of primer used for reverse transcription, e.g. 'oligo-dT' or 'random' primer. This allows users to identify content of the cDNA library input e.g. enriched for mRNA.
     * Range: [PrimerEnum](PrimerEnum.md)
 * [LibraryPreparationProtocol➞end_bias](LibraryPreparationProtocol_end_bias.md)  <sub>0..1</sub>
     * Description: The end of the cDNA molecule that is preferentially sequenced, e.g. 3/5 prime tag or end, or the full-length transcript.
     * Range: [EndBiasEnum](EndBiasEnum.md)
 * [LibraryPreparationProtocol➞target_regions](LibraryPreparationProtocol_target_regions.md)  <sub>0..\*</sub>
     * Description: Subset of genes or specific regions of the genome, which are most likely to be involved in the phenotype under study.
     * Range: [String](types/String.md)
 * [LibraryPreparationProtocol➞rnaseq_strandedness](LibraryPreparationProtocol_rnaseq_strandedness.md)  <sub>0..1</sub>
     * Description: The strandedness of the library, whether reads come from both strands of the cDNA or only from the first (antisense) or the second (sense) strand.
     * Range: [LibraryPreparationRNASeqStrandednessEnum](LibraryPreparationRNASeqStrandednessEnum.md)
 * [LibraryPreparationProtocol➞description](LibraryPreparationProtocol_description.md)  <sub>1..1</sub>
     * Description: Description about how a sequencing library was prepared (eg: Library construction method).
     * Range: [String](types/String.md)
 * [LibraryPreparationProtocol➞attributes](LibraryPreparationProtocol_attributes.md)  <sub>0..\*</sub>
     * Description: One or more attributes that further characterizes this library_preparation Protocol.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

### Inherited from Protocol:

 * [Protocol➞name](Protocol_name.md)  <sub>1..1</sub>
     * Description: Name of the Protocol (eg: Sample extraction_PCR amplification).
     * Range: [String](types/String.md)
 * [Protocol➞type](Protocol_type.md)  <sub>1..1</sub>
     * Description: Type of the protocol (eg: Target enrichment).
     * Range: [String](types/String.md)
 * [Protocol➞url](Protocol_url.md)  <sub>1..1</sub>
     * Description: URL for the resource that describes this protocol.
     * Range: [String](types/String.md)
 * [Protocol➞xref](Protocol_xref.md)  <sub>1..\*</sub>
     * Description: One or more cross-references for this protocol.  (Eg: manufacturer protocol, protocol from publication etc )
     * Range: [String](types/String.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
