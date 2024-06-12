
# Class: SupportingFile


A Supporting File is a File that contains additional information relevant for the entity, such as phenopackets, RO-Crates, imaging data or (unstructured) protocols.

URI: [GHGA:SupportingFile](https://w3id.org/GHGA/SupportingFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExperimentalMethod]-%20supporting_files%200..*>[SupportingFile&#124;format:SupportingFileFormatEnum;name(i):string;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[Individual]-%20supporting_files%200..*>[SupportingFile],[Submission]++-%20supporting_files%200..*>[SupportingFile],[ExperimentalMethod]-%20supporting_files(i)%200..*>[SupportingFile],[Individual]-%20supporting_files(i)%200..*>[SupportingFile],[Submission]-%20supporting_files(i)%200..*>[SupportingFile],[File]^-[SupportingFile],[Submission],[Individual],[File],[ExperimentalMethod],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExperimentalMethod]-%20supporting_files%200..*>[SupportingFile&#124;format:SupportingFileFormatEnum;name(i):string;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[Individual]-%20supporting_files%200..*>[SupportingFile],[Submission]++-%20supporting_files%200..*>[SupportingFile],[ExperimentalMethod]-%20supporting_files(i)%200..*>[SupportingFile],[Individual]-%20supporting_files(i)%200..*>[SupportingFile],[Submission]-%20supporting_files(i)%200..*>[SupportingFile],[File]^-[SupportingFile],[Submission],[Individual],[File],[ExperimentalMethod],[Dataset])

## Parents

 *  is_a: [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.

## Referenced by Class

 *  **[ExperimentalMethod](ExperimentalMethod.md)** *[ExperimentalMethod➞supporting_files](ExperimentalMethod_supporting_files.md)*  <sub>0..\*</sub>  **[SupportingFile](SupportingFile.md)**
 *  **[Individual](Individual.md)** *[Individual➞supporting_files](Individual_supporting_files.md)*  <sub>0..\*</sub>  **[SupportingFile](SupportingFile.md)**
 *  **[Submission](Submission.md)** *[Submission➞supporting_files](Submission_supporting_files.md)*  <sub>0..\*</sub>  **[SupportingFile](SupportingFile.md)**
 *  **None** *[supporting_files](supporting_files.md)*  <sub>0..\*</sub>  **[SupportingFile](SupportingFile.md)**

## Attributes


### Own

 * [SupportingFile➞format](SupportingFile_format.md)  <sub>1..1</sub>
     * Description: The format of the File (e.g., BAM, SAM, CRAM, BAI).
     * Range: [SupportingFileFormatEnum](SupportingFileFormatEnum.md)

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
     * Description: The Dataset associated with this File.
     * Range: [Dataset](Dataset.md)
