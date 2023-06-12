
# Class: File


A file is an object that contains information generated from a process, either an Experiment or an Analysis.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/File](https://w3id.org/GHGA-Submission-Metadata-Schema/File)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[StudyFile],[SequencingProcessFile],[SampleFile],[Individual],[IdentifiedByAliasMixin],[Dataset]<dataset%201..1-%20[File&#124;name:string;format:FileFormatEnum;size:integer;checksum:string;checksum_type:string;alias:string],[Individual]-%20files%200..*>[File],[Individual]-%20files(i)%200..*>[File],[File]uses%20-.->[IdentifiedByAliasMixin],[File]uses%20-.->[AttributeMixin],[File]^-[StudyFile],[File]^-[SequencingProcessFile],[File]^-[SampleFile],[File]^-[AnalysisProcessOutputFile],[Dataset],[AttributeMixin],[Attribute],[AnalysisProcessOutputFile])](https://yuml.me/diagram/nofunky;dir:TB/class/[StudyFile],[SequencingProcessFile],[SampleFile],[Individual],[IdentifiedByAliasMixin],[Dataset]<dataset%201..1-%20[File&#124;name:string;format:FileFormatEnum;size:integer;checksum:string;checksum_type:string;alias:string],[Individual]-%20files%200..*>[File],[Individual]-%20files(i)%200..*>[File],[File]uses%20-.->[IdentifiedByAliasMixin],[File]uses%20-.->[AttributeMixin],[File]^-[StudyFile],[File]^-[SequencingProcessFile],[File]^-[SampleFile],[File]^-[AnalysisProcessOutputFile],[Dataset],[AttributeMixin],[Attribute],[AnalysisProcessOutputFile])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Children

 * [AnalysisProcessOutputFile](AnalysisProcessOutputFile.md) - A AnalysisProcessOutputFile is a File that is associated as an output file with an AnalysisProcess.
 * [SampleFile](SampleFile.md) - A SampleFile is a File that is associated with a Sample.
 * [SequencingProcessFile](SequencingProcessFile.md) - A SequencingProcessFile is a File that is associated with a SequencingProcess.
 * [StudyFile](StudyFile.md) - A StudyFile is a File that is associated with a Study.

## Referenced by Class

 *  **[Individual](Individual.md)** *[Individual➞files](Individual_files.md)*  <sub>0..\*</sub>  **[File](File.md)**
 *  **None** *[files](files.md)*  <sub>0..\*</sub>  **[File](File.md)**

## Attributes


### Own

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

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)

### Mixed in from AttributeMixin:

 * [AttributeMixin➞attributes](AttributeMixin_attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | file object |

