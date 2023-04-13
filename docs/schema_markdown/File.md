
# Class: File


A file is an object that contains information generated from a process, either an Experiment or an Analysis.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/File](https://w3id.org/GHGA-Submission-Metadata-Schema/File)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProcess],[InformationContentEntity],[Individual],[Analysis]++-%20has_input%201..*>[File&#124;name:string;format:FileFormatEnum;size:integer;checksum:string;checksum_type:string;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Analysis]++-%20has_output%201..*>[File],[Dataset]++-%20has_file%201..*>[File],[Individual]++-%20has_file%200..*>[File],[SequencingProcess]-%20has_file%201..*>[File],[Submission]++-%20has_file%201..*>[File],[SequencingProcess]-%20has_file(i)%200..1>[File],[Individual]-%20has_file(i)%200..1>[File],[Dataset]-%20has_file(i)%200..1>[File],[Submission]-%20has_file(i)%200..1>[File],[Analysis]-%20has_input(i)%200..1>[File],[Analysis]-%20has_output(i)%200..1>[File],[File]uses%20-.->[AccessionMixin],[File]uses%20-.->[EgaAccessionMixin],[File]uses%20-.->[AttributeMixin],[InformationContentEntity]^-[File],[EgaAccessionMixin],[Dataset],[AttributeMixin],[Attribute],[Analysis],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProcess],[InformationContentEntity],[Individual],[Analysis]++-%20has_input%201..*>[File&#124;name:string;format:FileFormatEnum;size:integer;checksum:string;checksum_type:string;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Analysis]++-%20has_output%201..*>[File],[Dataset]++-%20has_file%201..*>[File],[Individual]++-%20has_file%200..*>[File],[SequencingProcess]-%20has_file%201..*>[File],[Submission]++-%20has_file%201..*>[File],[SequencingProcess]-%20has_file(i)%200..1>[File],[Individual]-%20has_file(i)%200..1>[File],[Dataset]-%20has_file(i)%200..1>[File],[Submission]-%20has_file(i)%200..1>[File],[Analysis]-%20has_input(i)%200..1>[File],[Analysis]-%20has_output(i)%200..1>[File],[File]uses%20-.->[AccessionMixin],[File]uses%20-.->[EgaAccessionMixin],[File]uses%20-.->[AttributeMixin],[InformationContentEntity]^-[File],[EgaAccessionMixin],[Dataset],[AttributeMixin],[Attribute],[Analysis],[AccessionMixin])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an ega_accession, in addition to GHGA accession.
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[Analysis](Analysis.md)** *[Analysis➞has_input](Analysis_has_input.md)*  <sub>1..\*</sub>  **[File](File.md)**
 *  **[Analysis](Analysis.md)** *[Analysis➞has_output](Analysis_has_output.md)*  <sub>1..\*</sub>  **[File](File.md)**
 *  **[Dataset](Dataset.md)** *[Dataset➞has_file](Dataset_has_file.md)*  <sub>1..\*</sub>  **[File](File.md)**
 *  **[Individual](Individual.md)** *[Individual➞has_file](Individual_has_file.md)*  <sub>0..\*</sub>  **[File](File.md)**
 *  **[SequencingProcess](SequencingProcess.md)** *[SequencingProcess➞has_file](SequencingProcess_has_file.md)*  <sub>1..\*</sub>  **[File](File.md)**
 *  **[Submission](Submission.md)** *[Submission➞has_file](Submission_has_file.md)*  <sub>1..\*</sub>  **[File](File.md)**
 *  **None** *[has_file](has_file.md)*  <sub>0..1</sub>  **[File](File.md)**
 *  **None** *[has_input](has_input.md)*  <sub>0..1</sub>  **[File](File.md)**
 *  **None** *[has_output](has_output.md)*  <sub>0..1</sub>  **[File](File.md)**

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

### Inherited from InformationContentEntity:

 * [NamedThing➞id](NamedThing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [NamedThing➞alias](NamedThing_alias.md)  <sub>1..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [NamedThing➞xref](NamedThing_xref.md)  <sub>0..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)

### Mixed in from AccessionMixin:

 * [AccessionMixin➞accession](AccessionMixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

### Mixed in from EgaAccessionMixin:

 * [EgaAccessionMixin➞ega_accession](EgaAccessionMixin_ega_accession.md)  <sub>1..1</sub>
     * Description: A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
     * Range: [String](types/String.md)

### Mixed in from AttributeMixin:

 * [has_attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | file object |

