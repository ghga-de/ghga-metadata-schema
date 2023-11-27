
# Class: AnalysisProcessOutputFile


A Analysis Process OutputFile is a File that is associated as an output file with an Analysis Process.

URI: [GHGA:AnalysisProcessOutputFile](https://w3id.org/GHGA/AnalysisProcessOutputFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[File],[Dataset],[AnalysisProcess]<analysis_process%201..1-%20[AnalysisProcessOutputFile&#124;name(i):string;format(i):FileFormatEnum;size(i):integer;checksum(i):string;checksum_type(i):string;forward_or_reverse(i):ForwardOrReverseEnum%20%3F;alias(i):string],[Submission]++-%20analysis_process_output_files%201..*>[AnalysisProcessOutputFile],[Submission]-%20analysis_process_output_files(i)%200..*>[AnalysisProcessOutputFile],[File]^-[AnalysisProcessOutputFile],[AnalysisProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[File],[Dataset],[AnalysisProcess]<analysis_process%201..1-%20[AnalysisProcessOutputFile&#124;name(i):string;format(i):FileFormatEnum;size(i):integer;checksum(i):string;checksum_type(i):string;forward_or_reverse(i):ForwardOrReverseEnum%20%3F;alias(i):string],[Submission]++-%20analysis_process_output_files%201..*>[AnalysisProcessOutputFile],[Submission]-%20analysis_process_output_files(i)%200..*>[AnalysisProcessOutputFile],[File]^-[AnalysisProcessOutputFile],[AnalysisProcess])

## Parents

 *  is_a: [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.

## Referenced by Class

 *  **[Submission](Submission.md)** *[Submission➞analysis_process_output_files](Submission_analysis_process_output_files.md)*  <sub>1..\*</sub>  **[AnalysisProcessOutputFile](AnalysisProcessOutputFile.md)**
 *  **None** *[analysis_process_output_files](analysis_process_output_files.md)*  <sub>0..\*</sub>  **[AnalysisProcessOutputFile](AnalysisProcessOutputFile.md)**

## Attributes


### Own

 * [AnalysisProcessOutputFile➞analysis_process](AnalysisProcessOutputFile_analysis_process.md)  <sub>1..1</sub>
     * Description: The Analysis Process this Analysis Process Output File is associated with.
     * Range: [AnalysisProcess](AnalysisProcess.md)

### Inherited from File:

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
