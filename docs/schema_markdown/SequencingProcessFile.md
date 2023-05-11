
# Class: SequencingProcessFile


A SequencingProcessFile is a File that is associated with a SequencingProcess.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/SequencingProcessFile](https://w3id.org/GHGA-Submission-Metadata-Schema/SequencingProcessFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProcess]<sequencing_process%201..1-%20[SequencingProcessFile&#124;name(i):string;format(i):FileFormatEnum;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[AnalysisProcess]-%20sequencing_process_files%201..*>[SequencingProcessFile],[Submission]++-%20sequencing_process_files%201..*>[SequencingProcessFile],[AnalysisProcess]-%20sequencing_process_files(i)%200..*>[SequencingProcessFile],[Submission]-%20sequencing_process_files(i)%200..*>[SequencingProcessFile],[File]^-[SequencingProcessFile],[SequencingProcess],[File],[Attribute],[AnalysisProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProcess]<sequencing_process%201..1-%20[SequencingProcessFile&#124;name(i):string;format(i):FileFormatEnum;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[AnalysisProcess]-%20sequencing_process_files%201..*>[SequencingProcessFile],[Submission]++-%20sequencing_process_files%201..*>[SequencingProcessFile],[AnalysisProcess]-%20sequencing_process_files(i)%200..*>[SequencingProcessFile],[Submission]-%20sequencing_process_files(i)%200..*>[SequencingProcessFile],[File]^-[SequencingProcessFile],[SequencingProcess],[File],[Attribute],[AnalysisProcess])

## Parents

 *  is_a: [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.

## Referenced by Class

 *  **[AnalysisProcess](AnalysisProcess.md)** *[AnalysisProcess➞sequencing_process_files](AnalysisProcess_sequencing_process_files.md)*  <sub>1..\*</sub>  **[SequencingProcessFile](SequencingProcessFile.md)**
 *  **[Submission](Submission.md)** *[Submission➞sequencing_process_files](Submission_sequencing_process_files.md)*  <sub>1..\*</sub>  **[SequencingProcessFile](SequencingProcessFile.md)**
 *  **None** *[sequencing_process_files](sequencing_process_files.md)*  <sub>0..\*</sub>  **[SequencingProcessFile](SequencingProcessFile.md)**

## Attributes


### Own

 * [SequencingProcessFile➞sequencing_process](SequencingProcessFile_sequencing_process.md)  <sub>1..1</sub>
     * Description: The SequencingProcess associated with an entity.
     * Range: [SequencingProcess](SequencingProcess.md)

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
