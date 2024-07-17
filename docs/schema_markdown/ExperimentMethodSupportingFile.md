
# Class: ExperimentMethodSupportingFile


An Experiment Method Supporting File is a File that contains additional information relevant for the Experiment Method, such as (unstructured) protocols.

URI: [GHGA:ExperimentMethodSupportingFile](https://w3id.org/GHGA/ExperimentMethodSupportingFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[File],[ExperimentMethod]<experiment_method%201..1-%20[ExperimentMethodSupportingFile&#124;format:SupportingFileFormatEnum;name(i):string;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[Submission]++-%20experiment_method_supporting_files%200..*>[ExperimentMethodSupportingFile],[Submission]-%20experiment_method_supporting_files(i)%200..*>[ExperimentMethodSupportingFile],[File]^-[ExperimentMethodSupportingFile],[ExperimentMethod],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[File],[ExperimentMethod]<experiment_method%201..1-%20[ExperimentMethodSupportingFile&#124;format:SupportingFileFormatEnum;name(i):string;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[Submission]++-%20experiment_method_supporting_files%200..*>[ExperimentMethodSupportingFile],[Submission]-%20experiment_method_supporting_files(i)%200..*>[ExperimentMethodSupportingFile],[File]^-[ExperimentMethodSupportingFile],[ExperimentMethod],[Dataset])

## Parents

 *  is_a: [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.

## Referenced by Class

 *  **[Submission](Submission.md)** *[Submission➞experiment_method_supporting_files](Submission_experiment_method_supporting_files.md)*  <sub>0..\*</sub>  **[ExperimentMethodSupportingFile](ExperimentMethodSupportingFile.md)**
 *  **None** *[experiment_method_supporting_file](experiment_method_supporting_file.md)*  <sub>0..1</sub>  **[ExperimentMethodSupportingFile](ExperimentMethodSupportingFile.md)**
 *  **None** *[experiment_method_supporting_files](experiment_method_supporting_files.md)*  <sub>0..\*</sub>  **[ExperimentMethodSupportingFile](ExperimentMethodSupportingFile.md)**

## Attributes


### Own

 * [ExperimentMethodSupportingFile➞format](ExperimentMethodSupportingFile_format.md)  <sub>1..1</sub>
     * Description: The file format of the Supporting File (e.g., TXT, JSON).
     * Range: [SupportingFileFormatEnum](SupportingFileFormatEnum.md)
 * [ExperimentMethodSupportingFile➞experiment_method](ExperimentMethodSupportingFile_experiment_method.md)  <sub>1..1</sub>
     * Description: The Experiment Method associated with an entity.
     * Range: [ExperimentMethod](ExperimentMethod.md)

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
