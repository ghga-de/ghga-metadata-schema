
# Class: AnalysisProcessOutputFile


A AnalysisProcessOutputFile is a File that is associated as an output file with an AnalysisProcess.

URI: [GHGA:AnalysisProcessOutputFile](https://w3id.org/GHGA/AnalysisProcessOutputFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[File],[Dataset],[AnalysisProcess]<analysis_process%201..1-%20[AnalysisProcessOutputFile&#124;name(i):string;format(i):FileFormatEnum;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[Submission]++-%20analysis_process_output_files%201..*>[AnalysisProcessOutputFile],[Submission]-%20analysis_process_output_files(i)%200..*>[AnalysisProcessOutputFile],[File]^-[AnalysisProcessOutputFile],[AnalysisProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[File],[Dataset],[AnalysisProcess]<analysis_process%201..1-%20[AnalysisProcessOutputFile&#124;name(i):string;format(i):FileFormatEnum;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[Submission]++-%20analysis_process_output_files%201..*>[AnalysisProcessOutputFile],[Submission]-%20analysis_process_output_files(i)%200..*>[AnalysisProcessOutputFile],[File]^-[AnalysisProcessOutputFile],[AnalysisProcess])

## Parents

 *  is_a: [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.

## Referenced by Class

 *  **[Submission](Submission.md)** *[Submission➞analysis_process_output_files](Submission_analysis_process_output_files.md)*  <sub>1..\*</sub>  **[AnalysisProcessOutputFile](AnalysisProcessOutputFile.md)**
 *  **None** *[analysis_process_output_files](analysis_process_output_files.md)*  <sub>0..\*</sub>  **[AnalysisProcessOutputFile](AnalysisProcessOutputFile.md)**

## Attributes


### Own

 * [AnalysisProcessOutputFile➞analysis_process](AnalysisProcessOutputFile_analysis_process.md)  <sub>1..1</sub>
     * Description: The AnalysisProcess associated with an entity.
     * Range: [AnalysisProcess](AnalysisProcess.md)

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
