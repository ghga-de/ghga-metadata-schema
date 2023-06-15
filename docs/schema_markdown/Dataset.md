
# Class: Dataset


A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.

URI: [GHGA:Dataset](https://w3id.org/GHGA/Dataset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[IdentifiedByAliasMixin],[File],[DataAccessPolicy]<data_access_policy%201..1-%20[Dataset&#124;title:string;description:string;types:string%20%2B;alias:string],[File]-%20dataset%201..1>[Dataset],[Submission]++-%20datasets%201..*>[Dataset],[File]-%20dataset(i)%200..1>[Dataset],[Submission]-%20datasets(i)%200..*>[Dataset],[Dataset]uses%20-.->[IdentifiedByAliasMixin],[Dataset]uses%20-.->[AttributeMixin],[DataAccessPolicy],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[IdentifiedByAliasMixin],[File],[DataAccessPolicy]<data_access_policy%201..1-%20[Dataset&#124;title:string;description:string;types:string%20%2B;alias:string],[File]-%20dataset%201..1>[Dataset],[Submission]++-%20datasets%201..*>[Dataset],[File]-%20dataset(i)%200..1>[Dataset],[Submission]-%20datasets(i)%200..*>[Dataset],[Dataset]uses%20-.->[IdentifiedByAliasMixin],[Dataset]uses%20-.->[AttributeMixin],[DataAccessPolicy],[AttributeMixin],[Attribute])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[File](File.md)** *[File➞dataset](File_dataset.md)*  <sub>1..1</sub>  **[Dataset](Dataset.md)**
 *  **[Submission](Submission.md)** *[Submission➞datasets](Submission_datasets.md)*  <sub>1..\*</sub>  **[Dataset](Dataset.md)**
 *  **None** *[dataset](dataset.md)*  <sub>0..1</sub>  **[Dataset](Dataset.md)**
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
 * [Dataset➞data_access_policy](Dataset_data_access_policy.md)  <sub>1..1</sub>
     * Description: The Data Access Policy that applies to this Dataset.
     * Range: [DataAccessPolicy](DataAccessPolicy.md)

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
| **Exact Mappings:** | | SIO:000089 |

