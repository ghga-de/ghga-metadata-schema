
# Class: ExperimentalMethodSupportingFile


An Experimental Method Supporting File is a File that contains additional information relevant for the Experimental Method, such as (unstructured) protocols.

URI: [GHGA:ExperimentalMethodSupportingFile](https://w3id.org/GHGA/ExperimentalMethodSupportingFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[File],[ExperimentalMethod]<experimental_method%201..1-%20[ExperimentalMethodSupportingFile&#124;format:SupportingFileFormatEnum;name(i):string;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[Submission]++-%20experimental_method_supporting_files%200..*>[ExperimentalMethodSupportingFile],[Submission]-%20experimental_method_supporting_files(i)%200..*>[ExperimentalMethodSupportingFile],[File]^-[ExperimentalMethodSupportingFile],[ExperimentalMethod],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[File],[ExperimentalMethod]<experimental_method%201..1-%20[ExperimentalMethodSupportingFile&#124;format:SupportingFileFormatEnum;name(i):string;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[Submission]++-%20experimental_method_supporting_files%200..*>[ExperimentalMethodSupportingFile],[Submission]-%20experimental_method_supporting_files(i)%200..*>[ExperimentalMethodSupportingFile],[File]^-[ExperimentalMethodSupportingFile],[ExperimentalMethod],[Dataset])

## Parents

 *  is_a: [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.

## Referenced by Class

 *  **[Submission](Submission.md)** *[Submission➞experimental_method_supporting_files](Submission_experimental_method_supporting_files.md)*  <sub>0..\*</sub>  **[ExperimentalMethodSupportingFile](ExperimentalMethodSupportingFile.md)**
 *  **None** *[experimental_method_supporting_file](experimental_method_supporting_file.md)*  <sub>0..1</sub>  **[ExperimentalMethodSupportingFile](ExperimentalMethodSupportingFile.md)**
 *  **None** *[experimental_method_supporting_files](experimental_method_supporting_files.md)*  <sub>0..\*</sub>  **[ExperimentalMethodSupportingFile](ExperimentalMethodSupportingFile.md)**

## Attributes


### Own

 * [ExperimentalMethodSupportingFile➞format](ExperimentalMethodSupportingFile_format.md)  <sub>1..1</sub>
     * Description: The file format of the Supporting File (e.g., txt, json)
     * Range: [SupportingFileFormatEnum](SupportingFileFormatEnum.md)
 * [ExperimentalMethodSupportingFile➞experimental_method](ExperimentalMethodSupportingFile_experimental_method.md)  <sub>1..1</sub>
     * Description: The Experimental Method associated with an entity.
     * Range: [ExperimentalMethod](ExperimentalMethod.md)

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
