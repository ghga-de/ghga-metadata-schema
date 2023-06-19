
# Class: SampleFile


A SampleFile is a File that is associated with a Sample.

URI: [GHGA:SampleFile](https://w3id.org/GHGA/SampleFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample]<sample%201..1-%20[SampleFile&#124;name(i):string;format(i):FileFormatEnum;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[AnalysisProcess]-%20sample_input_files%201..*>[SampleFile],[Submission]++-%20sample_files%201..*>[SampleFile],[Submission]-%20sample_files(i)%200..*>[SampleFile],[AnalysisProcess]-%20sample_input_files(i)%200..*>[SampleFile],[File]^-[SampleFile],[Sample],[File],[Dataset],[AnalysisProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample]<sample%201..1-%20[SampleFile&#124;name(i):string;format(i):FileFormatEnum;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[AnalysisProcess]-%20sample_input_files%201..*>[SampleFile],[Submission]++-%20sample_files%201..*>[SampleFile],[Submission]-%20sample_files(i)%200..*>[SampleFile],[AnalysisProcess]-%20sample_input_files(i)%200..*>[SampleFile],[File]^-[SampleFile],[Sample],[File],[Dataset],[AnalysisProcess])

## Parents

 *  is_a: [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.

## Referenced by Class

 *  **[AnalysisProcess](AnalysisProcess.md)** *[AnalysisProcess➞sample_input_files](AnalysisProcess_sample_input_files.md)*  <sub>1..\*</sub>  **[SampleFile](SampleFile.md)**
 *  **[Submission](Submission.md)** *[Submission➞sample_files](Submission_sample_files.md)*  <sub>1..\*</sub>  **[SampleFile](SampleFile.md)**
 *  **None** *[sample_files](sample_files.md)*  <sub>0..\*</sub>  **[SampleFile](SampleFile.md)**
 *  **None** *[sample_input_files](sample_input_files.md)*  <sub>0..\*</sub>  **[SampleFile](SampleFile.md)**

## Attributes


### Own

 * [SampleFile➞sample](SampleFile_sample.md)  <sub>1..1</sub>
     * Description: The sample associated with an entity.
     * Range: [Sample](Sample.md)

### Inherited from File:

 * [File➞name](File_name.md)  <sub>1..1</sub>
     * Description: The given filename.
     * Range: [String](types/String.md)
 * [File➞format](File_format.md)  <sub>1..1</sub>
     * Description: The format of the file: BAM, SAM, CRAM, BAI, etc.
     * Range: [FileFormatEnum](FileFormatEnum.md)
 * [File➞size](File_size.md)  <sub>1..1</sub>
     * Description: The size of a file in bytes.
     * Range: [Integer](types/Integer.md)
 * [File➞checksum](File_checksum.md)  <sub>1..1</sub>
     * Description: A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data. The receiving system recomputes the checksum based upon the received data and compares this value with the one sent with the data. If the two values are the same, the receiver has some confidence that the data was received correctly.
     * Range: [String](types/String.md)
 * [File➞checksum_type](File_checksum_type.md)  <sub>1..1</sub>
     * Description: The type of algorithm used to generate the checksum of a file.
     * Range: [String](types/String.md)
 * [File➞dataset](File_dataset.md)  <sub>1..1</sub>
     * Description: The Dataset associated with an entity.
     * Range: [Dataset](Dataset.md)
