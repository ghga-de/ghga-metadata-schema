
# Class: SampleFile


A Sample File is a File that is associated with a Sample.

URI: [GHGA:SampleFile](https://w3id.org/GHGA/SampleFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample]<sample%201..1-%20[SampleFile&#124;name(i):string;format(i):FileFormatEnum;size(i):integer;checksum(i):string;checksum_type(i):string;forward_or_reverse(i):ForwardOrReverseEnum%20%3F;alias(i):string],[AnalysisProcess]-%20sample_input_files%200..*>[SampleFile],[Submission]++-%20sample_files%201..*>[SampleFile],[Submission]-%20sample_files(i)%200..*>[SampleFile],[AnalysisProcess]-%20sample_input_files(i)%200..*>[SampleFile],[File]^-[SampleFile],[Sample],[File],[Dataset],[AnalysisProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample]<sample%201..1-%20[SampleFile&#124;name(i):string;format(i):FileFormatEnum;size(i):integer;checksum(i):string;checksum_type(i):string;forward_or_reverse(i):ForwardOrReverseEnum%20%3F;alias(i):string],[AnalysisProcess]-%20sample_input_files%200..*>[SampleFile],[Submission]++-%20sample_files%201..*>[SampleFile],[Submission]-%20sample_files(i)%200..*>[SampleFile],[AnalysisProcess]-%20sample_input_files(i)%200..*>[SampleFile],[File]^-[SampleFile],[Sample],[File],[Dataset],[AnalysisProcess])

## Parents

 *  is_a: [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.

## Referenced by Class

 *  **[AnalysisProcess](AnalysisProcess.md)** *[AnalysisProcess➞sample_input_files](AnalysisProcess_sample_input_files.md)*  <sub>0..\*</sub>  **[SampleFile](SampleFile.md)**
 *  **[Submission](Submission.md)** *[Submission➞sample_files](Submission_sample_files.md)*  <sub>1..\*</sub>  **[SampleFile](SampleFile.md)**
 *  **None** *[sample_files](sample_files.md)*  <sub>0..\*</sub>  **[SampleFile](SampleFile.md)**
 *  **None** *[sample_input_files](sample_input_files.md)*  <sub>0..\*</sub>  **[SampleFile](SampleFile.md)**

## Attributes


### Own

 * [SampleFile➞sample](SampleFile_sample.md)  <sub>1..1</sub>
     * Description: The Sample that is associated with this Sample File.
     * Range: [Sample](Sample.md)

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
