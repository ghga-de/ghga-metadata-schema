
# Class: LibraryPreparationProtocol


The Library Preparation Protocol captures information about the library preparation of a Sequencing Experiment.

URI: [GHGA:LibraryPreparationProtocol](https://w3id.org/GHGA/LibraryPreparationProtocol)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingExperiment],[Attribute]<attributes%200..*-++[LibraryPreparationProtocol&#124;description:string;library_name:string;library_layout:LibraryPreparationLibraryLayoutEnum;library_type:LibraryPreparationLibraryTypeEnum;library_selection:LibraryPreparationLibrarySelectionEnum;library_preparation:string;library_preparation_kit_retail_name:LibraryPreparationKitRetailNameEnum%20%3F;library_preparation_kit_manufacturer:string%20%3F;primer:PrimerEnum%20%3F;end_bias:EndBiasEnum%20%3F;target_regions:string%20*;rnaseq_strandedness:LibraryPreparationRNASeqStrandednessEnum%20%3F;alias:string],[SequencingExperiment]-%20library_preparation_protocol%201..1>[LibraryPreparationProtocol],[Submission]++-%20library_preparation_protocols%201..*>[LibraryPreparationProtocol],[SequencingExperiment]-%20library_preparation_protocol(i)%200..1>[LibraryPreparationProtocol],[Submission]-%20library_preparation_protocols(i)%200..*>[LibraryPreparationProtocol],[LibraryPreparationProtocol]uses%20-.->[IdentifiedByAliasMixin],[LibraryPreparationProtocol]uses%20-.->[AttributeMixin],[IdentifiedByAliasMixin],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingExperiment],[Attribute]<attributes%200..*-++[LibraryPreparationProtocol&#124;description:string;library_name:string;library_layout:LibraryPreparationLibraryLayoutEnum;library_type:LibraryPreparationLibraryTypeEnum;library_selection:LibraryPreparationLibrarySelectionEnum;library_preparation:string;library_preparation_kit_retail_name:LibraryPreparationKitRetailNameEnum%20%3F;library_preparation_kit_manufacturer:string%20%3F;primer:PrimerEnum%20%3F;end_bias:EndBiasEnum%20%3F;target_regions:string%20*;rnaseq_strandedness:LibraryPreparationRNASeqStrandednessEnum%20%3F;alias:string],[SequencingExperiment]-%20library_preparation_protocol%201..1>[LibraryPreparationProtocol],[Submission]++-%20library_preparation_protocols%201..*>[LibraryPreparationProtocol],[SequencingExperiment]-%20library_preparation_protocol(i)%200..1>[LibraryPreparationProtocol],[Submission]-%20library_preparation_protocols(i)%200..*>[LibraryPreparationProtocol],[LibraryPreparationProtocol]uses%20-.->[IdentifiedByAliasMixin],[LibraryPreparationProtocol]uses%20-.->[AttributeMixin],[IdentifiedByAliasMixin],[AttributeMixin],[Attribute])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[SequencingExperiment](SequencingExperiment.md)** *[SequencingExperiment➞library_preparation_protocol](SequencingExperiment_library_preparation_protocol.md)*  <sub>1..1</sub>  **[LibraryPreparationProtocol](LibraryPreparationProtocol.md)**
 *  **[Submission](Submission.md)** *[Submission➞library_preparation_protocols](Submission_library_preparation_protocols.md)*  <sub>1..\*</sub>  **[LibraryPreparationProtocol](LibraryPreparationProtocol.md)**
 *  **None** *[library_preparation_protocol](library_preparation_protocol.md)*  <sub>0..1</sub>  **[LibraryPreparationProtocol](LibraryPreparationProtocol.md)**
 *  **None** *[library_preparation_protocols](library_preparation_protocols.md)*  <sub>0..\*</sub>  **[LibraryPreparationProtocol](LibraryPreparationProtocol.md)**

## Attributes


### Own

 * [LibraryPreparationProtocol➞description](LibraryPreparationProtocol_description.md)  <sub>1..1</sub>
     * Description: Description summarizing how a sequencing library was prepared.
     * Range: [String](types/String.md)
 * [LibraryPreparationProtocol➞library_name](LibraryPreparationProtocol_library_name.md)  <sub>1..1</sub>
     * Description: A short name identifying the library. The same name may refer to multiple versions of the same continually updated library.
     * Range: [String](types/String.md)
 * [LibraryPreparationProtocol➞library_layout](LibraryPreparationProtocol_library_layout.md)  <sub>1..1</sub>
     * Description: Describe whether the library was sequenced in single-end (forward or reverse) or paired-end mode.
     * Range: [LibraryPreparationLibraryLayoutEnum](LibraryPreparationLibraryLayoutEnum.md)
 * [LibraryPreparationProtocol➞library_type](LibraryPreparationProtocol_library_type.md)  <sub>1..1</sub>
     * Description: Describe the level of omics analysis (e.g., metagenome, transcriptome)
     * Range: [LibraryPreparationLibraryTypeEnum](LibraryPreparationLibraryTypeEnum.md)
 * [LibraryPreparationProtocol➞library_selection](LibraryPreparationProtocol_library_selection.md)  <sub>1..1</sub>
     * Description: The method used to select for or against, enrich, or screen the material being sequenced (e.g., random, PCA, cDNA).
     * Range: [LibraryPreparationLibrarySelectionEnum](LibraryPreparationLibrarySelectionEnum.md)
 * [LibraryPreparationProtocol➞library_preparation](LibraryPreparationProtocol_library_preparation.md)  <sub>1..1</sub>
     * Description: The general method for preparation of the sequencing library (e.g., KAPA PCR-free).
     * Range: [String](types/String.md)
 * [LibraryPreparationProtocol➞library_preparation_kit_retail_name](LibraryPreparationProtocol_library_preparation_kit_retail_name.md)  <sub>0..1</sub>
     * Description: The retail name for the kit used to construct a genomic library. This may include the vendor name, kit name and kit version (e.g., Agilent sure select Human Exome V8, Twist RefSeq Exome).
     * Range: [LibraryPreparationKitRetailNameEnum](LibraryPreparationKitRetailNameEnum.md)
 * [LibraryPreparationProtocol➞library_preparation_kit_manufacturer](LibraryPreparationProtocol_library_preparation_kit_manufacturer.md)  <sub>0..1</sub>
     * Description: The manufacturer of the kit used for library preparation.
     * Range: [String](types/String.md)
 * [LibraryPreparationProtocol➞primer](LibraryPreparationProtocol_primer.md)  <sub>0..1</sub>
     * Description: The type of primer used for reverse transcription (e.g., oligo-dT or random).
     * Range: [PrimerEnum](PrimerEnum.md)
 * [LibraryPreparationProtocol➞end_bias](LibraryPreparationProtocol_end_bias.md)  <sub>0..1</sub>
     * Description: The end of the cDNA molecule that is preferentially sequenced (e.g., 3/5 prime end, full-length).
     * Range: [EndBiasEnum](EndBiasEnum.md)
 * [LibraryPreparationProtocol➞target_regions](LibraryPreparationProtocol_target_regions.md)  <sub>0..\*</sub>
     * Description: Subset of genes or specific regions of the genome, which are most likely to be involved in the phenotype under study.
     * Range: [String](types/String.md)
 * [LibraryPreparationProtocol➞rnaseq_strandedness](LibraryPreparationProtocol_rnaseq_strandedness.md)  <sub>0..1</sub>
     * Description: The strandedness of the library, whether reads come from both strands of the cDNA or only from the first (antisense) or the second (sense) strand.
     * Range: [LibraryPreparationRNASeqStrandednessEnum](LibraryPreparationRNASeqStrandednessEnum.md)
 * [LibraryPreparationProtocol➞attributes](LibraryPreparationProtocol_attributes.md)  <sub>0..\*</sub>
     * Description: One or more attributes that further characterize this Library Preparation Protocol.
     * Range: [Attribute](Attribute.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
