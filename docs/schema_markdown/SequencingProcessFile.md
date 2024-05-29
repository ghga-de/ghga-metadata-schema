
# Class: SequencingProcessFile


A Sequencing Process File is a File that is associated with a Sequencing Process.

URI: [GHGA:SequencingProcessFile](https://w3id.org/GHGA/SequencingProcessFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProcess]<sequencing_process%201..1-%20[SequencingProcessFile&#124;name(i):string;format(i):FileFormatEnum;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[AnalysisProcess]-%20sequencing_process_input_files%200..*>[SequencingProcessFile],[Submission]++-%20sequencing_process_files%201..*>[SequencingProcessFile],[Submission]-%20sequencing_process_files(i)%200..*>[SequencingProcessFile],[AnalysisProcess]-%20sequencing_process_input_files(i)%200..*>[SequencingProcessFile],[File]^-[SequencingProcessFile],[SequencingProcess],[File],[Dataset],[AnalysisProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProcess]<sequencing_process%201..1-%20[SequencingProcessFile&#124;name(i):string;format(i):FileFormatEnum;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[AnalysisProcess]-%20sequencing_process_input_files%200..*>[SequencingProcessFile],[Submission]++-%20sequencing_process_files%201..*>[SequencingProcessFile],[Submission]-%20sequencing_process_files(i)%200..*>[SequencingProcessFile],[AnalysisProcess]-%20sequencing_process_input_files(i)%200..*>[SequencingProcessFile],[File]^-[SequencingProcessFile],[SequencingProcess],[File],[Dataset],[AnalysisProcess])

## Parents

 *  is_a: [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.

## Referenced by Class

 *  **[AnalysisProcess](AnalysisProcess.md)** *[AnalysisProcess➞sequencing_process_input_files](AnalysisProcess_sequencing_process_input_files.md)*  <sub>0..\*</sub>  **[SequencingProcessFile](SequencingProcessFile.md)**
 *  **[Submission](Submission.md)** *[Submission➞sequencing_process_files](Submission_sequencing_process_files.md)*  <sub>1..\*</sub>  **[SequencingProcessFile](SequencingProcessFile.md)**
 *  **None** *[sequencing_process_files](sequencing_process_files.md)*  <sub>0..\*</sub>  **[SequencingProcessFile](SequencingProcessFile.md)**
 *  **None** *[sequencing_process_input_files](sequencing_process_input_files.md)*  <sub>0..\*</sub>  **[SequencingProcessFile](SequencingProcessFile.md)**

## Attributes


### Own

 * [SequencingProcessFile➞sequencing_process](SequencingProcessFile_sequencing_process.md)  <sub>1..1</sub>
     * Description: The Sequencing Process associated with this Sequencing Process File.
     * Range: [SequencingProcess](SequencingProcess.md)

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
 * [File➞dataset](File_dataset.md)  <sub>1..1</sub>
     * Description: The Dataset associated with this File.
     * Range: [Dataset](Dataset.md)
