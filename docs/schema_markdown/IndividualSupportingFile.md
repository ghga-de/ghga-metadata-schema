
# Class: IndividualSupportingFile


An Individual Supporting File is a File that contains additional information relevant for the Individual, such as ped-files, phenopackets or imaging data.

URI: [GHGA:IndividualSupportingFile](https://w3id.org/GHGA/IndividualSupportingFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Individual]<individual%201..1-%20[IndividualSupportingFile&#124;format:SupportingFileFormatEnum;name(i):string;ega_accession(i):string%20%3F;included_in_submission(i):boolean;alias(i):string],[Submission]++-%20individual_supporting_files%201..*>[IndividualSupportingFile],[Submission]-%20individual_supporting_files(i)%200..*>[IndividualSupportingFile],[File]^-[IndividualSupportingFile],[Individual],[File],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Individual]<individual%201..1-%20[IndividualSupportingFile&#124;format:SupportingFileFormatEnum;name(i):string;ega_accession(i):string%20%3F;included_in_submission(i):boolean;alias(i):string],[Submission]++-%20individual_supporting_files%201..*>[IndividualSupportingFile],[Submission]-%20individual_supporting_files(i)%200..*>[IndividualSupportingFile],[File]^-[IndividualSupportingFile],[Individual],[File],[Dataset])

## Parents

 *  is_a: [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.

## Referenced by Class

 *  **[Submission](Submission.md)** *[Submission➞individual_supporting_files](Submission_individual_supporting_files.md)*  <sub>1..\*</sub>  **[IndividualSupportingFile](IndividualSupportingFile.md)**
 *  **None** *[individual_supporting_files](individual_supporting_files.md)*  <sub>0..\*</sub>  **[IndividualSupportingFile](IndividualSupportingFile.md)**

## Attributes


### Own

 * [IndividualSupportingFile➞format](IndividualSupportingFile_format.md)  <sub>1..1</sub>
     * Description: The file format of the Supporting File (e.g., TXT, JSON).
     * Range: [SupportingFileFormatEnum](SupportingFileFormatEnum.md)
 * [IndividualSupportingFile➞individual](IndividualSupportingFile_individual.md)  <sub>1..1</sub>
     * Description: The Individual associated with an entity.
     * Range: [Individual](Individual.md)

### Inherited from File:

 * [File➞name](File_name.md)  <sub>1..1</sub>
     * Description: The given filename.
     * Range: [String](types/String.md)
 * [File➞dataset](File_dataset.md)  <sub>1..1</sub>
     * Description: The Dataset alias associated with this File.
     * Range: [Dataset](Dataset.md)
 * [File➞ega_accession](File_ega_accession.md)  <sub>0..1</sub>
     * Description: The EGA accession ID of an entity.
     * Range: [String](types/String.md)
 * [File➞included_in_submission](File_included_in_submission.md)  <sub>1..1</sub>
     * Description: Whether a File is included in the Submission or not.
     * Range: [Boolean](types/Boolean.md)
