
# Class: Study


A Study is an experimental investigation of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

URI: [GHGA:Study](https://w3id.org/GHGA/Study)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[StudyFile],[Attribute]<attributes%200..*-++[Study&#124;title:string;description:string;type:StudyTypeEnum;affiliations:string%20%2B;alias:string],[Condition]-%20study%201..1>[Study],[Publication]-%20study%201..1>[Study],[StudyFile]-%20study%201..1>[Study],[Submission]++-%20studies%201..*>[Study],[Submission]-%20studies(i)%200..*>[Study],[Condition]-%20study(i)%200..1>[Study],[StudyFile]-%20study(i)%200..1>[Study],[Publication]-%20study(i)%200..1>[Study],[Study]uses%20-.->[IdentifiedByAliasMixin],[Study]uses%20-.->[AttributeMixin],[Publication],[IdentifiedByAliasMixin],[Condition],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[StudyFile],[Attribute]<attributes%200..*-++[Study&#124;title:string;description:string;type:StudyTypeEnum;affiliations:string%20%2B;alias:string],[Condition]-%20study%201..1>[Study],[Publication]-%20study%201..1>[Study],[StudyFile]-%20study%201..1>[Study],[Submission]++-%20studies%201..*>[Study],[Submission]-%20studies(i)%200..*>[Study],[Condition]-%20study(i)%200..1>[Study],[StudyFile]-%20study(i)%200..1>[Study],[Publication]-%20study(i)%200..1>[Study],[Study]uses%20-.->[IdentifiedByAliasMixin],[Study]uses%20-.->[AttributeMixin],[Publication],[IdentifiedByAliasMixin],[Condition],[AttributeMixin],[Attribute])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[Condition](Condition.md)** *[Condition➞study](Condition_study.md)*  <sub>1..1</sub>  **[Study](Study.md)**
 *  **[Publication](Publication.md)** *[Publication➞study](Publication_study.md)*  <sub>1..1</sub>  **[Study](Study.md)**
 *  **[StudyFile](StudyFile.md)** *[StudyFile➞study](StudyFile_study.md)*  <sub>1..1</sub>  **[Study](Study.md)**
 *  **[Submission](Submission.md)** *[Submission➞studies](Submission_studies.md)*  <sub>1..\*</sub>  **[Study](Study.md)**
 *  **None** *[studies](studies.md)*  <sub>0..\*</sub>  **[Study](Study.md)**
 *  **None** *[study](study.md)*  <sub>0..1</sub>  **[Study](Study.md)**

## Attributes


### Own

 * [Study➞title](Study_title.md)  <sub>1..1</sub>
     * Description: A comprehensive title for this Study.
     * Range: [String](types/String.md)
 * [Study➞description](Study_description.md)  <sub>1..1</sub>
     * Description: A detailed description (abstract) that describes the goals of this Study.
     * Range: [String](types/String.md)
 * [Study➞type](Study_type.md)  <sub>1..1</sub>
     * Description: The type of this Study (e.g., Cancer Genomics, Epigenetics, Exome Sequencing).
     * Range: [StudyTypeEnum](StudyTypeEnum.md)
 * [Study➞affiliations](Study_affiliations.md)  <sub>1..\*</sub>
     * Description: The affiliations associated with this Study.
     * Range: [String](types/String.md)
 * [Study➞attributes](Study_attributes.md)  <sub>0..\*</sub>
     * Description: One or more attributes that further characterize this Study.
     * Range: [Attribute](Attribute.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
