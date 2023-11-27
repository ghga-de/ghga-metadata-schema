
# Class: File


A file is an object that contains information generated from a process, either an Experiment or an Analysis.

URI: [GHGA:File](https://w3id.org/GHGA/File)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[StudyFile],[SequencingProcessFile],[SampleFile],[IdentifiedByAliasMixin],[Dataset]<dataset%201..1-%20[File&#124;name:string;format:FileFormatEnum;size:integer;checksum:string;checksum_type:string;forward_or_reverse:ForwardOrReverseEnum%20%3F;alias:string],[File]uses%20-.->[IdentifiedByAliasMixin],[File]^-[StudyFile],[File]^-[SequencingProcessFile],[File]^-[SampleFile],[File]^-[AnalysisProcessOutputFile],[Dataset],[AnalysisProcessOutputFile])](https://yuml.me/diagram/nofunky;dir:TB/class/[StudyFile],[SequencingProcessFile],[SampleFile],[IdentifiedByAliasMixin],[Dataset]<dataset%201..1-%20[File&#124;name:string;format:FileFormatEnum;size:integer;checksum:string;checksum_type:string;forward_or_reverse:ForwardOrReverseEnum%20%3F;alias:string],[File]uses%20-.->[IdentifiedByAliasMixin],[File]^-[StudyFile],[File]^-[SequencingProcessFile],[File]^-[SampleFile],[File]^-[AnalysisProcessOutputFile],[Dataset],[AnalysisProcessOutputFile])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Children

 * [AnalysisProcessOutputFile](AnalysisProcessOutputFile.md) - A Analysis Process OutputFile is a File that is associated as an output file with an Analysis Process.
 * [SampleFile](SampleFile.md) - A Sample File is a File that is associated with a Sample.
 * [SequencingProcessFile](SequencingProcessFile.md) - A Sequencing Process File is a File that is associated with a Sequencing Process.
 * [StudyFile](StudyFile.md) - A Study File is a File that is associated with a Study.

## Referenced by Class


## Attributes


### Own

 * [File➞name](File_name.md)  <sub>1..1</sub>
     * Description: The given filename.
     * Range: [String](types/String.md)
 * [File➞format](File_format.md)  <sub>1..1</sub>
     * Description: The format of the File (e.g., BAM, SAM, CRAM, BAI).
     * Range: [FileFormatEnum](FileFormatEnum.md)
 * [File➞size](File_size.md)  <sub>1..1</sub>
     * Description: The size of the File in bytes.
     * Range: [Integer](types/Integer.md)
 * [File➞checksum](File_checksum.md)  <sub>1..1</sub>
     * Description: The checksum of the File.
     * Range: [String](types/String.md)
 * [File➞checksum_type](File_checksum_type.md)  <sub>1..1</sub>
     * Description: The type of algorithm used to generate the checksum of the File.
     * Range: [String](types/String.md)
 * [File➞forward_or_reverse](File_forward_or_reverse.md)  <sub>0..1</sub>
     * Description: Denotes whether a submitted FASTQ file contains forward (R1) or reverse (R2) reads for paired-end sequencing.
     * Range: [ForwardOrReverseEnum](ForwardOrReverseEnum.md)
 * [File➞dataset](File_dataset.md)  <sub>1..1</sub>
     * Description: The Dataset associated with this File.
     * Range: [Dataset](Dataset.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
