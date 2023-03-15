
# Class: dataset


A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Dataset](https://w3id.org/GHGA-Submission-Metadata-Schema/Dataset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[Sample],[Publication],[InformationContentEntity],[File],[Experiment],[EgaAccessionMixin],[DataAccessPolicy]<has%20data%20access%20policy%201..1-++[Dataset&#124;title:string;description:string;type:string%20%2B;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Publication]<has%20publication%200..*-++[Dataset],[File]<has%20file%201..*-++[Dataset],[Analysis]<has%20analysis%200..*-++[Dataset],[Sample]<has%20sample%201..*-++[Dataset],[Experiment]<has%20experiment%201..*-++[Dataset],[Study]<has%20study%201..*-++[Dataset],[Submission]-%20has%20dataset(i)%200..1>[Dataset],[Submission]++-%20has%20dataset%201..*>[Dataset],[Dataset]uses%20-.->[AccessionMixin],[Dataset]uses%20-.->[EgaAccessionMixin],[Dataset]uses%20-.->[AttributeMixin],[InformationContentEntity]^-[Dataset],[DataAccessPolicy],[AttributeMixin],[Attribute],[Analysis],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[Sample],[Publication],[InformationContentEntity],[File],[Experiment],[EgaAccessionMixin],[DataAccessPolicy]<has%20data%20access%20policy%201..1-++[Dataset&#124;title:string;description:string;type:string%20%2B;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Publication]<has%20publication%200..*-++[Dataset],[File]<has%20file%201..*-++[Dataset],[Analysis]<has%20analysis%200..*-++[Dataset],[Sample]<has%20sample%201..*-++[Dataset],[Experiment]<has%20experiment%201..*-++[Dataset],[Study]<has%20study%201..*-++[Dataset],[Submission]-%20has%20dataset(i)%200..1>[Dataset],[Submission]++-%20has%20dataset%201..*>[Dataset],[Dataset]uses%20-.->[AccessionMixin],[Dataset]uses%20-.->[EgaAccessionMixin],[Dataset]uses%20-.->[AttributeMixin],[InformationContentEntity]^-[Dataset],[DataAccessPolicy],[AttributeMixin],[Attribute],[Analysis],[AccessionMixin])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an EGA accession, in addition to GHGA accession.
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **None** *[has dataset](has_dataset.md)*  <sub>0..1</sub>  **[Dataset](Dataset.md)**
 *  **[Submission](Submission.md)** *[submission➞has dataset](submission_has_dataset.md)*  <sub>1..\*</sub>  **[Dataset](Dataset.md)**

## Attributes


### Own

 * [dataset➞title](dataset_title.md)  <sub>1..1</sub>
     * Description: A title for the submitted Dataset.
     * Range: [String](types/String.md)
 * [dataset➞description](dataset_description.md)  <sub>1..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)
 * [dataset➞type](dataset_type.md)  <sub>1..\*</sub>
     * Description: The type of a dataset.
     * Range: [String](types/String.md)
 * [dataset➞has study](dataset_has_study.md)  <sub>1..\*</sub>
     * Description: One or more Study entities that are referenced by this Dataset.
     * Range: [Study](Study.md)
 * [dataset➞has experiment](dataset_has_experiment.md)  <sub>1..\*</sub>
     * Description: One or more Experiment entities that are referenced by this Dataset.
     * Range: [Experiment](Experiment.md)
     * in subsets: (restricted)
 * [dataset➞has sample](dataset_has_sample.md)  <sub>1..\*</sub>
     * Description: One or more Sample entities that are referenced by this Dataset.
     * Range: [Sample](Sample.md)
     * in subsets: (restricted)
 * [dataset➞has analysis](dataset_has_analysis.md)  <sub>0..\*</sub>
     * Description: One or more Analysis entities that are referenced by this Dataset.
     * Range: [Analysis](Analysis.md)
     * in subsets: (restricted)
 * [dataset➞has file](dataset_has_file.md)  <sub>1..\*</sub>
     * Description: One or more File entities that collectively are part of this Dataset.
     * Range: [File](File.md)
     * in subsets: (restricted)
 * [dataset➞has publication](dataset_has_publication.md)  <sub>0..\*</sub>
     * Description: One or more Publication entities associated with this Dataset.
     * Range: [Publication](Publication.md)
 * [dataset➞has data access policy](dataset_has_data_access_policy.md)  <sub>1..1</sub>
     * Description: The Data Access Policy that applies to this Dataset.
     * Range: [DataAccessPolicy](DataAccessPolicy.md)
     * in subsets: (restricted)

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
| **Exact Mappings:** | | SIO:000089 |

