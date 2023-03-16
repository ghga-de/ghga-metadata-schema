
# Class: file


A file is an object that contains information generated from a process, either an Experiment or an Analysis.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/File](https://w3id.org/GHGA-Submission-Metadata-Schema/File)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[InformationContentEntity],[Individual],[Analysis]++-%20has%20input%201..*>[File&#124;name:string;format:file_format_enum;size:integer;checksum:string;checksum_type:string;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Analysis]++-%20has%20output%201..*>[File],[Dataset]++-%20has%20file%201..*>[File],[Experiment]++-%20has%20file%201..*>[File],[Experiment]-%20has%20file(i)%200..1>[File],[Individual]-%20has%20file(i)%200..1>[File],[Dataset]-%20has%20file(i)%200..1>[File],[Submission]-%20has%20file(i)%200..1>[File],[Analysis]-%20has%20input(i)%200..1>[File],[Analysis]-%20has%20output(i)%200..1>[File],[Individual]++-%20has%20file%200..*>[File],[Submission]++-%20has%20file%201..*>[File],[File]uses%20-.->[AccessionMixin],[File]uses%20-.->[EgaAccessionMixin],[File]uses%20-.->[AttributeMixin],[InformationContentEntity]^-[File],[Experiment],[EgaAccessionMixin],[Dataset],[AttributeMixin],[Attribute],[Analysis],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[InformationContentEntity],[Individual],[Analysis]++-%20has%20input%201..*>[File&#124;name:string;format:file_format_enum;size:integer;checksum:string;checksum_type:string;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Analysis]++-%20has%20output%201..*>[File],[Dataset]++-%20has%20file%201..*>[File],[Experiment]++-%20has%20file%201..*>[File],[Experiment]-%20has%20file(i)%200..1>[File],[Individual]-%20has%20file(i)%200..1>[File],[Dataset]-%20has%20file(i)%200..1>[File],[Submission]-%20has%20file(i)%200..1>[File],[Analysis]-%20has%20input(i)%200..1>[File],[Analysis]-%20has%20output(i)%200..1>[File],[Individual]++-%20has%20file%200..*>[File],[Submission]++-%20has%20file%201..*>[File],[File]uses%20-.->[AccessionMixin],[File]uses%20-.->[EgaAccessionMixin],[File]uses%20-.->[AttributeMixin],[InformationContentEntity]^-[File],[Experiment],[EgaAccessionMixin],[Dataset],[AttributeMixin],[Attribute],[Analysis],[AccessionMixin])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an EGA accession, in addition to GHGA accession.
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[Analysis](Analysis.md)** *[analysis➞has input](analysis_has_input.md)*  <sub>1..\*</sub>  **[File](File.md)**
 *  **[Analysis](Analysis.md)** *[analysis➞has output](analysis_has_output.md)*  <sub>1..\*</sub>  **[File](File.md)**
 *  **[Dataset](Dataset.md)** *[dataset➞has file](dataset_has_file.md)*  <sub>1..\*</sub>  **[File](File.md)**
 *  **[Experiment](Experiment.md)** *[experiment➞has file](experiment_has_file.md)*  <sub>1..\*</sub>  **[File](File.md)**
 *  **None** *[has file](has_file.md)*  <sub>0..1</sub>  **[File](File.md)**
 *  **None** *[has input](has_input.md)*  <sub>0..1</sub>  **[File](File.md)**
 *  **None** *[has output](has_output.md)*  <sub>0..1</sub>  **[File](File.md)**
 *  **[Individual](Individual.md)** *[individual➞has file](individual_has_file.md)*  <sub>0..\*</sub>  **[File](File.md)**
 *  **[Submission](Submission.md)** *[submission➞has file](submission_has_file.md)*  <sub>1..\*</sub>  **[File](File.md)**

## Attributes


### Own

 * [file➞name](file_name.md)  <sub>1..1</sub>
     * Description: The given filename.
     * Range: [String](types/String.md)
 * [file➞format](file_format.md)  <sub>1..1</sub>
     * Description: The format of the file: BAM, SAM, CRAM, BAI, etc.
     * Range: [file format enum](file format enum.md)
 * [file➞size](file_size.md)  <sub>1..1</sub>
     * Description: The size of a file in bytes.
     * Range: [Integer](types/Integer.md)
 * [file➞checksum](file_checksum.md)  <sub>1..1</sub>
     * Description: A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data. The receiving system recomputes the checksum based upon the received data and compares this value with the one sent with the data. If the two values are the same, the receiver has some confidence that the data was received correctly.
     * Range: [String](types/String.md)
 * [file➞checksum type](file_checksum_type.md)  <sub>1..1</sub>
     * Description: The type of algorithm used to generate the checksum of a file.
     * Range: [String](types/String.md)

### Inherited from information content entity:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞alias](named_thing_alias.md)  <sub>1..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞xref](named_thing_xref.md)  <sub>0..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)

### Mixed in from accession mixin:

 * [accession mixin➞accession](accession_mixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

### Mixed in from ega accession mixin:

 * [ega accession mixin➞ega accession](ega_accession_mixin_ega_accession.md)  <sub>1..1</sub>
     * Description: A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
     * Range: [String](types/String.md)

### Mixed in from attribute mixin:

 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | file object |

