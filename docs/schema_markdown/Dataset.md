
# Class: Dataset


A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Dataset](https://w3id.org/GHGA-Submission-Metadata-Schema/Dataset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[InformationContentEntity],[File],[EgaAccessionMixin],[DataAccessPolicy]<data_access_policy%201..1-%20[Dataset&#124;title:string;description:string;types:string%20%2B;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[File]<files%201..*-%20[Dataset],[Submission]++-%20datasets%201..*>[Dataset],[Submission]-%20datasets(i)%200..*>[Dataset],[Dataset]uses%20-.->[AccessionMixin],[Dataset]uses%20-.->[EgaAccessionMixin],[Dataset]uses%20-.->[AttributeMixin],[InformationContentEntity]^-[Dataset],[DataAccessPolicy],[AttributeMixin],[Attribute],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[InformationContentEntity],[File],[EgaAccessionMixin],[DataAccessPolicy]<data_access_policy%201..1-%20[Dataset&#124;title:string;description:string;types:string%20%2B;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[File]<files%201..*-%20[Dataset],[Submission]++-%20datasets%201..*>[Dataset],[Submission]-%20datasets(i)%200..*>[Dataset],[Dataset]uses%20-.->[AccessionMixin],[Dataset]uses%20-.->[EgaAccessionMixin],[Dataset]uses%20-.->[AttributeMixin],[InformationContentEntity]^-[Dataset],[DataAccessPolicy],[AttributeMixin],[Attribute],[AccessionMixin])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an ega_accession, in addition to GHGA accession.
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[Submission](Submission.md)** *[Submission➞datasets](Submission_datasets.md)*  <sub>1..\*</sub>  **[Dataset](Dataset.md)**
 *  **None** *[datasets](datasets.md)*  <sub>0..\*</sub>  **[Dataset](Dataset.md)**

## Attributes


### Own

 * [Dataset➞title](Dataset_title.md)  <sub>1..1</sub>
     * Description: A title for the submitted Dataset.
     * Range: [String](types/String.md)
 * [Dataset➞description](Dataset_description.md)  <sub>1..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)
 * [Dataset➞types](Dataset_types.md)  <sub>1..\*</sub>
     * Description: The type of a dataset.
     * Range: [String](types/String.md)
 * [Dataset➞files](Dataset_files.md)  <sub>1..\*</sub>
     * Description: One or more File entities that collectively are part of this Dataset.
     * Range: [File](File.md)
     * in subsets: (restricted)
 * [Dataset➞data_access_policy](Dataset_data_access_policy.md)  <sub>1..1</sub>
     * Description: The Data Access Policy that applies to this Dataset.
     * Range: [DataAccessPolicy](DataAccessPolicy.md)
     * in subsets: (restricted)

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
| **Exact Mappings:** | | SIO:000089 |

