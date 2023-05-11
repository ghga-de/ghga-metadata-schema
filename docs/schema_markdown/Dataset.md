
# Class: Dataset


A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Dataset](https://w3id.org/GHGA-Submission-Metadata-Schema/Dataset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[InformationContentEntity],[IdentifiedByAliasMixin],[File],[DataAccessPolicy]<data_access_policy%201..1-%20[Dataset&#124;title:string;description:string;types:string%20%2B;alias:string],[File]<files%201..*-%20[Dataset],[Submission]++-%20datasets%201..*>[Dataset],[Submission]-%20datasets(i)%200..*>[Dataset],[Dataset]uses%20-.->[IdentifiedByAliasMixin],[Dataset]uses%20-.->[AttributeMixin],[InformationContentEntity]^-[Dataset],[DataAccessPolicy],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[InformationContentEntity],[IdentifiedByAliasMixin],[File],[DataAccessPolicy]<data_access_policy%201..1-%20[Dataset&#124;title:string;description:string;types:string%20%2B;alias:string],[File]<files%201..*-%20[Dataset],[Submission]++-%20datasets%201..*>[Dataset],[Submission]-%20datasets(i)%200..*>[Dataset],[Dataset]uses%20-.->[IdentifiedByAliasMixin],[Dataset]uses%20-.->[AttributeMixin],[InformationContentEntity]^-[Dataset],[DataAccessPolicy],[AttributeMixin],[Attribute])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
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

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
     * in subsets: (restricted)

### Mixed in from AttributeMixin:

 * [attributes](attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:000089 |

