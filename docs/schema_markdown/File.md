
# Class: File


A file is an object that contains information generated from a process, either an Experiment or an Analysis.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/File](https://w3id.org/GHGA-Submission-Metadata-Schema/File)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProcess],[InformationContentEntity],[Individual],[Analysis]++-%20inputs%201..*>[File&#124;name:string;format:FileFormatEnum;size:integer;checksum:string;checksum_type:string;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Analysis]++-%20outputs%201..*>[File],[Dataset]++-%20files%201..*>[File],[Individual]++-%20files%200..*>[File],[SequencingProcess]-%20files%201..*>[File],[Submission]++-%20files%201..*>[File],[SequencingProcess]-%20files(i)%200..*>[File],[Individual]-%20files(i)%200..*>[File],[Dataset]-%20files(i)%200..*>[File],[Submission]-%20files(i)%200..*>[File],[Analysis]-%20inputs(i)%200..*>[File],[Analysis]-%20outputs(i)%200..*>[File],[File]uses%20-.->[AccessionMixin],[File]uses%20-.->[EgaAccessionMixin],[File]uses%20-.->[AttributeMixin],[InformationContentEntity]^-[File],[EgaAccessionMixin],[Dataset],[AttributeMixin],[Attribute],[Analysis],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProcess],[InformationContentEntity],[Individual],[Analysis]++-%20inputs%201..*>[File&#124;name:string;format:FileFormatEnum;size:integer;checksum:string;checksum_type:string;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Analysis]++-%20outputs%201..*>[File],[Dataset]++-%20files%201..*>[File],[Individual]++-%20files%200..*>[File],[SequencingProcess]-%20files%201..*>[File],[Submission]++-%20files%201..*>[File],[SequencingProcess]-%20files(i)%200..*>[File],[Individual]-%20files(i)%200..*>[File],[Dataset]-%20files(i)%200..*>[File],[Submission]-%20files(i)%200..*>[File],[Analysis]-%20inputs(i)%200..*>[File],[Analysis]-%20outputs(i)%200..*>[File],[File]uses%20-.->[AccessionMixin],[File]uses%20-.->[EgaAccessionMixin],[File]uses%20-.->[AttributeMixin],[InformationContentEntity]^-[File],[EgaAccessionMixin],[Dataset],[AttributeMixin],[Attribute],[Analysis],[AccessionMixin])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an ega_accession, in addition to GHGA accession.
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[Analysis](Analysis.md)** *[Analysis➞inputs](Analysis_inputs.md)*  <sub>1..\*</sub>  **[File](File.md)**
 *  **[Analysis](Analysis.md)** *[Analysis➞outputs](Analysis_outputs.md)*  <sub>1..\*</sub>  **[File](File.md)**
 *  **[Dataset](Dataset.md)** *[Dataset➞files](Dataset_files.md)*  <sub>1..\*</sub>  **[File](File.md)**
 *  **[Individual](Individual.md)** *[Individual➞files](Individual_files.md)*  <sub>0..\*</sub>  **[File](File.md)**
 *  **[SequencingProcess](SequencingProcess.md)** *[SequencingProcess➞files](SequencingProcess_files.md)*  <sub>1..\*</sub>  **[File](File.md)**
 *  **[Submission](Submission.md)** *[Submission➞files](Submission_files.md)*  <sub>1..\*</sub>  **[File](File.md)**
 *  **None** *[files](files.md)*  <sub>0..\*</sub>  **[File](File.md)**
 *  **None** *[inputs](inputs.md)*  <sub>0..\*</sub>  **[File](File.md)**
 *  **None** *[outputs](outputs.md)*  <sub>0..\*</sub>  **[File](File.md)**

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

 * [attributes](attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | file object |

