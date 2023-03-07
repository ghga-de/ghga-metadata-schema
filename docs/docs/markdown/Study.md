
# Class: study


Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

URI: [GHGA:Study](https://w3id.org/GHGA/Study)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Attribute]<has%20attribute%200..*-++[Study&#124;type:study_type_enum;affiliation:string%20%2B;alias:string;title:string;description:string;release_status:release_status_enum%20%3F;accession:string%20%3F;ega_accession:string%20%3F;release_date:string%20%3F;id(i):string;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Publication]<has%20publication%200..*-++[Study],[File]<has%20file%200..*-++[Study],[Project]<has%20project%200..1-++[Study],[Analysis]++-%20has%20study%201..1>[Study],[Dataset]++-%20has%20study%201..*>[Study],[Experiment]++-%20has%20study%201..1>[Study],[Experiment]-%20has%20study(i)%200..1>[Study],[Analysis]-%20has%20study(i)%200..1>[Study],[Dataset]-%20has%20study(i)%200..1>[Study],[Submission]-%20has%20study(i)%200..1>[Study],[Submission]++-%20has%20study%201..1>[Study],[Study]uses%20-.->[AccessionMixin],[Study]uses%20-.->[EgaAccessionMixin],[Study]uses%20-.->[PublicationMixin],[Study]uses%20-.->[AttributeMixin],[Study]uses%20-.->[ReleaseStatusMixin],[Investigation]^-[Study],[ReleaseStatusMixin],[PublicationMixin],[Publication],[Project],[Investigation],[File],[Experiment],[EgaAccessionMixin],[Dataset],[AttributeMixin],[Attribute],[Analysis],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Attribute]<has%20attribute%200..*-++[Study&#124;type:study_type_enum;affiliation:string%20%2B;alias:string;title:string;description:string;release_status:release_status_enum%20%3F;accession:string%20%3F;ega_accession:string%20%3F;release_date:string%20%3F;id(i):string;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Publication]<has%20publication%200..*-++[Study],[File]<has%20file%200..*-++[Study],[Project]<has%20project%200..1-++[Study],[Analysis]++-%20has%20study%201..1>[Study],[Dataset]++-%20has%20study%201..*>[Study],[Experiment]++-%20has%20study%201..1>[Study],[Experiment]-%20has%20study(i)%200..1>[Study],[Analysis]-%20has%20study(i)%200..1>[Study],[Dataset]-%20has%20study(i)%200..1>[Study],[Submission]-%20has%20study(i)%200..1>[Study],[Submission]++-%20has%20study%201..1>[Study],[Study]uses%20-.->[AccessionMixin],[Study]uses%20-.->[EgaAccessionMixin],[Study]uses%20-.->[PublicationMixin],[Study]uses%20-.->[AttributeMixin],[Study]uses%20-.->[ReleaseStatusMixin],[Investigation]^-[Study],[ReleaseStatusMixin],[PublicationMixin],[Publication],[Project],[Investigation],[File],[Experiment],[EgaAccessionMixin],[Dataset],[AttributeMixin],[Attribute],[Analysis],[AccessionMixin])

## Parents

 *  is_a: [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an EGA accession, in addition to GHGA accession.
 *  mixin: [PublicationMixin](PublicationMixin.md) - Mixin for entities that can have one or more publications.
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.
 *  mixin: [ReleaseStatusMixin](ReleaseStatusMixin.md) - Mixin for entities that can be released at a later point in time.

## Referenced by Class

 *  **[Analysis](Analysis.md)** *[analysis➞has study](analysis_has_study.md)*  <sub>1..1</sub>  **[Study](Study.md)**
 *  **[Dataset](Dataset.md)** *[dataset➞has study](dataset_has_study.md)*  <sub>1..\*</sub>  **[Study](Study.md)**
 *  **[Experiment](Experiment.md)** *[experiment➞has study](experiment_has_study.md)*  <sub>1..1</sub>  **[Study](Study.md)**
 *  **None** *[has study](has_study.md)*  <sub>0..1</sub>  **[Study](Study.md)**
 *  **[Submission](Submission.md)** *[submission➞has study](submission_has_study.md)*  <sub>1..1</sub>  **[Study](Study.md)**

## Attributes


### Own

 * [study➞type](study_type.md)  <sub>1..1</sub>
     * Description: The type of Study. For example, 'Cancer Genomics', 'Epigenetics', 'Exome Sequencing'.
     * Range: [study type enum](study type enum.md)
     * in subsets: (essential,public)
 * [study➞affiliation](study_affiliation.md)  <sub>1..\*</sub>
     * Description: The Institution(s) associated with an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [study➞has project](study_has_project.md)  <sub>0..1</sub>
     * Description: The project associated with this Study.
     * Range: [Project](Project.md)
     * in subsets: (optional,public)
 * [study➞has file](study_has_file.md)  <sub>0..\*</sub>
     * Description: Additional/supplementary files associated with a Study.
     * Range: [File](File.md)
     * in subsets: (essential,restricted)
 * [study➞alias](study_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [study➞title](study_title.md)  <sub>1..1</sub>
     * Description: A comprehensive title for the study.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [study➞description](study_description.md)  <sub>1..1</sub>
     * Description: A detailed description (abstract) that describes the goals of this Study.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [study➞has publication](study_has_publication.md)  <sub>0..\*</sub>
     * Description: One or more Publication entities associated with this Study.
     * Range: [Publication](Publication.md)
     * in subsets: (optional,public)
 * [study➞has attribute](study_has_attribute.md)  <sub>0..\*</sub>
     * Description: Custom key/value pairs that further characterizes the Study. (e.g.: approaches - single-cell, bulk etc)
     * Range: [Attribute](Attribute.md)
     * in subsets: (optional,restricted)
 * [study➞release status](study_release_status.md)  <sub>0..1</sub>
     * Description: The release status of a Study.
     * Range: [release status enum](release status enum.md)

### Inherited from investigation:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [named thing➞xref](named_thing_xref.md)  <sub>0..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)
     * in subsets: (optional,public)
 * [named thing➞creation date](named_thing_creation_date.md)  <sub>0..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was created.
     * Range: [String](types/String.md)
 * [named thing➞update date](named_thing_update_date.md)  <sub>0..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was updated.
     * Range: [String](types/String.md)

### Mixed in from accession mixin:

 * [accession](accession.md)  <sub>0..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

### Mixed in from ega accession mixin:

 * [ega accession](ega_accession.md)  <sub>0..1</sub>
     * Description: A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
     * Range: [String](types/String.md)

### Mixed in from release status mixin:

 * [release date](release_date.md)  <sub>0..1</sub>
     * Description: The timestamp (in ISO 8601 format) when the entity was released for public consumption.
     * Range: [String](types/String.md)
