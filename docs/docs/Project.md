
# Class: project


A high level organization for a collection of studies based on a research proposal that aims to achieve certain goals.

URI: [GHGA:Project](https://w3id.org/GHGA/Project)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[ResearchActivity],[Publication],[Attribute]<has%20attribute%200..*-++[Project&#124;alias:string;title:string;description:string;accession:string%20%3F;id(i):string;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Publication]<has%20publication%200..*-++[Project],[Study]-%20has%20project(i)%200..1>[Project],[Submission]-%20has%20project(i)%200..1>[Project],[Study]++-%20has%20project%200..1>[Project],[Submission]++-%20has%20project%200..1>[Project],[Project]uses%20-.->[AccessionMixin],[Project]uses%20-.->[AttributeMixin],[ResearchActivity]^-[Project],[AttributeMixin],[Attribute],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[ResearchActivity],[Publication],[Attribute]<has%20attribute%200..*-++[Project&#124;alias:string;title:string;description:string;accession:string%20%3F;id(i):string;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Publication]<has%20publication%200..*-++[Project],[Study]-%20has%20project(i)%200..1>[Project],[Submission]-%20has%20project(i)%200..1>[Project],[Study]++-%20has%20project%200..1>[Project],[Submission]++-%20has%20project%200..1>[Project],[Project]uses%20-.->[AccessionMixin],[Project]uses%20-.->[AttributeMixin],[ResearchActivity]^-[Project],[AttributeMixin],[Attribute],[AccessionMixin])

## Parents

 *  is_a: [ResearchActivity](ResearchActivity.md) - A planned process executed in the performance of scientific research wherein systematic investigations are performed to establish facts and reach new conclusions about phenomena in the world.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **None** *[has project](has_project.md)*  <sub>0..1</sub>  **[Project](Project.md)**
 *  **[Study](Study.md)** *[study➞has project](study_has_project.md)*  <sub>0..1</sub>  **[Project](Project.md)**
 *  **[Submission](Submission.md)** *[submission➞has project](submission_has_project.md)*  <sub>0..1</sub>  **[Project](Project.md)**

## Attributes


### Own

 * [project➞alias](project_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [project➞title](project_title.md)  <sub>1..1</sub>
     * Description: Comprehensive title for the project.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [project➞description](project_description.md)  <sub>1..1</sub>
     * Description: Short textual description of the project.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [project➞has publication](project_has_publication.md)  <sub>0..\*</sub>
     * Description: One or more Publication entities associated with this Project.
     * Range: [Publication](Publication.md)
     * in subsets: (optional,public)
 * [project➞has attribute](project_has_attribute.md)  <sub>0..\*</sub>
     * Description: Custom attributes for the Project  (eg: Cancer - Colon cancer, prostrate cancer, blood cancer etc)
     * Range: [Attribute](Attribute.md)
     * in subsets: (optional,restricted)

### Inherited from research activity:

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
