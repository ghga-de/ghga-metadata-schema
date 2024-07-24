
# Class: AnalysisMethodSupportingFile


An Analysis Method Supporting File is a File that contains additional information relevant for the Analysis Method, such as (unstructured) protocols or task descriptions.

URI: [GHGA:AnalysisMethodSupportingFile](https://w3id.org/GHGA/AnalysisMethodSupportingFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[File],[Dataset],[AnalysisMethod]<analysis_method%201..1-%20[AnalysisMethodSupportingFile&#124;format:SupportingFileFormatEnum;name(i):string;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[Submission]++-%20analysis_method_supporting_files%201..*>[AnalysisMethodSupportingFile],[Submission]-%20analysis_method_supporting_files(i)%200..*>[AnalysisMethodSupportingFile],[File]^-[AnalysisMethodSupportingFile],[AnalysisMethod])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[File],[Dataset],[AnalysisMethod]<analysis_method%201..1-%20[AnalysisMethodSupportingFile&#124;format:SupportingFileFormatEnum;name(i):string;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[Submission]++-%20analysis_method_supporting_files%201..*>[AnalysisMethodSupportingFile],[Submission]-%20analysis_method_supporting_files(i)%200..*>[AnalysisMethodSupportingFile],[File]^-[AnalysisMethodSupportingFile],[AnalysisMethod])

## Parents

 *  is_a: [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.

## Referenced by Class

 *  **[Submission](Submission.md)** *[Submission➞analysis_method_supporting_files](Submission_analysis_method_supporting_files.md)*  <sub>1..\*</sub>  **[AnalysisMethodSupportingFile](AnalysisMethodSupportingFile.md)**
 *  **None** *[analysis_method_supporting_files](analysis_method_supporting_files.md)*  <sub>0..\*</sub>  **[AnalysisMethodSupportingFile](AnalysisMethodSupportingFile.md)**

## Attributes


### Own

 * [AnalysisMethodSupportingFile➞format](AnalysisMethodSupportingFile_format.md)  <sub>1..1</sub>
     * Description: The file format of the Supporting File (e.g., TXT, JSON).
     * Range: [SupportingFileFormatEnum](SupportingFileFormatEnum.md)
 * [AnalysisMethodSupportingFile➞analysis_method](AnalysisMethodSupportingFile_analysis_method.md)  <sub>1..1</sub>
     * Description: The Analysis Process associated with an entity.
     * Range: [AnalysisMethod](AnalysisMethod.md)

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
