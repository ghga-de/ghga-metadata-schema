
# Class: Dataset


A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Dataset](https://w3id.org/GHGA-Submission-Metadata-Schema/Dataset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Publication],[InformationContentEntity],[File],[EgaAccessionMixin],[DataAccessPolicy]<has_data_access_policy%201..1-++[Dataset&#124;title:string;description:string;type:string%20%2B;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Publication]<has_publication%200..1-%20[Dataset],[File]<has_file%201..*-++[Dataset],[Submission]++-%20has_dataset%201..*>[Dataset],[Submission]-%20has_dataset(i)%200..1>[Dataset],[Dataset]uses%20-.->[AccessionMixin],[Dataset]uses%20-.->[EgaAccessionMixin],[Dataset]uses%20-.->[AttributeMixin],[InformationContentEntity]^-[Dataset],[DataAccessPolicy],[AttributeMixin],[Attribute],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Publication],[InformationContentEntity],[File],[EgaAccessionMixin],[DataAccessPolicy]<has_data_access_policy%201..1-++[Dataset&#124;title:string;description:string;type:string%20%2B;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Publication]<has_publication%200..1-%20[Dataset],[File]<has_file%201..*-++[Dataset],[Submission]++-%20has_dataset%201..*>[Dataset],[Submission]-%20has_dataset(i)%200..1>[Dataset],[Dataset]uses%20-.->[AccessionMixin],[Dataset]uses%20-.->[EgaAccessionMixin],[Dataset]uses%20-.->[AttributeMixin],[InformationContentEntity]^-[Dataset],[DataAccessPolicy],[AttributeMixin],[Attribute],[AccessionMixin])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an ega_accession, in addition to GHGA accession.
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[Submission](Submission.md)** *[Submission➞has_dataset](Submission_has_dataset.md)*  <sub>1..\*</sub>  **[Dataset](Dataset.md)**
 *  **None** *[has_dataset](has_dataset.md)*  <sub>0..1</sub>  **[Dataset](Dataset.md)**

## Attributes


### Own

 * [Dataset➞title](Dataset_title.md)  <sub>1..1</sub>
     * Description: A title for the submitted Dataset.
     * Range: [String](types/String.md)
 * [Dataset➞description](Dataset_description.md)  <sub>1..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)
 * [Dataset➞type](Dataset_type.md)  <sub>1..\*</sub>
     * Description: The type of a dataset.
     * Range: [String](types/String.md)
 * [Dataset➞has_file](Dataset_has_file.md)  <sub>1..\*</sub>
     * Description: One or more File entities that collectively are part of this Dataset.
     * Range: [File](File.md)
     * in subsets: (restricted)
 * [has_publication](has_publication.md)  <sub>0..1</sub>
     * Description: The Publication associated with an entity.
     * Range: [Publication](Publication.md)
 * [Dataset➞has_data_access_policy](Dataset_has_data_access_policy.md)  <sub>1..1</sub>
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

 * [has_attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:000089 |

