
# Class: ProcessDataFile


A Process Data File is a File that contains data produced by an Analysis or workflow.

URI: [GHGA:ProcessDataFile](https://w3id.org/GHGA/ProcessDataFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Analysis]<analysis%201..1-%20[ProcessDataFile&#124;format:ProcessDataFileFormatEnum;ega_accession:string%20%3F;name(i):string;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[Submission]++-%20process_data_files%200..*>[ProcessDataFile],[Submission]-%20process_data_files(i)%200..*>[ProcessDataFile],[File]^-[ProcessDataFile],[File],[Dataset],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Analysis]<analysis%201..1-%20[ProcessDataFile&#124;format:ProcessDataFileFormatEnum;ega_accession:string%20%3F;name(i):string;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[Submission]++-%20process_data_files%200..*>[ProcessDataFile],[Submission]-%20process_data_files(i)%200..*>[ProcessDataFile],[File]^-[ProcessDataFile],[File],[Dataset],[Analysis])

## Parents

 *  is_a: [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.

## Referenced by Class

 *  **[Submission](Submission.md)** *[Submission➞process_data_files](Submission_process_data_files.md)*  <sub>0..\*</sub>  **[ProcessDataFile](ProcessDataFile.md)**
 *  **None** *[process_data_file](process_data_file.md)*  <sub>0..1</sub>  **[ProcessDataFile](ProcessDataFile.md)**
 *  **None** *[process_data_files](process_data_files.md)*  <sub>0..\*</sub>  **[ProcessDataFile](ProcessDataFile.md)**

## Attributes


### Own

 * [ProcessDataFile➞format](ProcessDataFile_format.md)  <sub>1..1</sub>
     * Description: The file format of the Process Data File (e.g., CRAM, BAM).
     * Range: [ProcessDataFileFormatEnum](ProcessDataFileFormatEnum.md)
 * [ProcessDataFile➞ega_accession](ProcessDataFile_ega_accession.md)  <sub>0..1</sub>
     * Description: The EGA accession ID of an entity.
     * Range: [String](types/String.md)
 * [ProcessDataFile➞analysis](ProcessDataFile_analysis.md)  <sub>1..1</sub>
     * Description: The alias of the Analysis that produced this Process Data File.
     * Range: [Analysis](Analysis.md)

### Inherited from File:

 * [File➞name](File_name.md)  <sub>1..1</sub>
     * Description: The given filename.
     * Range: [String](types/String.md)
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
     * Description: The Dataset alias associated with this File.
     * Range: [Dataset](Dataset.md)
