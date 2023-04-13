
# Class: Project


A high level organization for a collection of studies based on a research proposal that aims to achieve certain goals.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Project](https://w3id.org/GHGA-Submission-Metadata-Schema/Project)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[ResearchActivity],[Attribute]<has_attribute%200..*-++[Project&#124;title:string%20%3F;description:string%20%3F;accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Study]++-%20has_project%200..1>[Project],[Submission]++-%20has_project%200..1>[Project],[Study]-%20has_project(i)%200..1>[Project],[Submission]-%20has_project(i)%200..1>[Project],[Project]uses%20-.->[AccessionMixin],[Project]uses%20-.->[AttributeMixin],[ResearchActivity]^-[Project],[AttributeMixin],[Attribute],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[ResearchActivity],[Attribute]<has_attribute%200..*-++[Project&#124;title:string%20%3F;description:string%20%3F;accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Study]++-%20has_project%200..1>[Project],[Submission]++-%20has_project%200..1>[Project],[Study]-%20has_project(i)%200..1>[Project],[Submission]-%20has_project(i)%200..1>[Project],[Project]uses%20-.->[AccessionMixin],[Project]uses%20-.->[AttributeMixin],[ResearchActivity]^-[Project],[AttributeMixin],[Attribute],[AccessionMixin])

## Parents

 *  is_a: [ResearchActivity](ResearchActivity.md) - A PlannedProcess executed in the performance of scientific research wherein systematic Investigations are performed to establish facts and reach new conclusions about phenomena in the world.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[Study](Study.md)** *[Study➞has_project](Study_has_project.md)*  <sub>0..1</sub>  **[Project](Project.md)**
 *  **[Submission](Submission.md)** *[Submission➞has_project](Submission_has_project.md)*  <sub>0..1</sub>  **[Project](Project.md)**
 *  **None** *[has_project](has_project.md)*  <sub>0..1</sub>  **[Project](Project.md)**

## Attributes


### Own

 * [Project➞title](Project_title.md)  <sub>0..1</sub>
     * Description: Comprehensive title for the project.
     * Range: [String](types/String.md)
 * [Project➞description](Project_description.md)  <sub>0..1</sub>
     * Description: Short textual description of the project.
     * Range: [String](types/String.md)
 * [Project➞has_attribute](Project_has_attribute.md)  <sub>0..\*</sub>
     * Description: Custom attributes for the Project  (eg: Cancer - Colon_cancer,_prostrate_cancer,_blood_cancer_etc)
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

### Inherited from ResearchActivity:

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
