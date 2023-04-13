
# Class: Study


Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Study](https://w3id.org/GHGA-Submission-Metadata-Schema/Study)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Attribute]<has_attribute%200..*-++[Study&#124;type:StudyTypeEnum;affiliation:string%20%2B;title:string;description:string;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Condition]<has_condition%201..*-%20[Study],[Project]<has_project%200..1-++[Study],[Analysis]++-%20has_study%201..1>[Study],[Publication]++-%20has_study%201..1>[Study],[Submission]++-%20has_study%201..1>[Study],[Analysis]-%20has_study(i)%200..1>[Study],[Publication]-%20has_study(i)%200..1>[Study],[Submission]-%20has_study(i)%200..1>[Study],[Study]uses%20-.->[AccessionMixin],[Study]uses%20-.->[EgaAccessionMixin],[Study]uses%20-.->[AttributeMixin],[Investigation]^-[Study],[Publication],[Project],[Investigation],[EgaAccessionMixin],[Condition],[AttributeMixin],[Attribute],[Analysis],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Attribute]<has_attribute%200..*-++[Study&#124;type:StudyTypeEnum;affiliation:string%20%2B;title:string;description:string;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Condition]<has_condition%201..*-%20[Study],[Project]<has_project%200..1-++[Study],[Analysis]++-%20has_study%201..1>[Study],[Publication]++-%20has_study%201..1>[Study],[Submission]++-%20has_study%201..1>[Study],[Analysis]-%20has_study(i)%200..1>[Study],[Publication]-%20has_study(i)%200..1>[Study],[Submission]-%20has_study(i)%200..1>[Study],[Study]uses%20-.->[AccessionMixin],[Study]uses%20-.->[EgaAccessionMixin],[Study]uses%20-.->[AttributeMixin],[Investigation]^-[Study],[Publication],[Project],[Investigation],[EgaAccessionMixin],[Condition],[AttributeMixin],[Attribute],[Analysis],[AccessionMixin])

## Parents

 *  is_a: [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an ega_accession, in addition to GHGA accession.
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[Analysis](Analysis.md)** *[Analysis➞has_study](Analysis_has_study.md)*  <sub>1..1</sub>  **[Study](Study.md)**
 *  **[Publication](Publication.md)** *[Publication➞has_study](Publication_has_study.md)*  <sub>1..1</sub>  **[Study](Study.md)**
 *  **[Submission](Submission.md)** *[Submission➞has_study](Submission_has_study.md)*  <sub>1..1</sub>  **[Study](Study.md)**
 *  **None** *[has_study](has_study.md)*  <sub>0..1</sub>  **[Study](Study.md)**

## Attributes


### Own

 * [Study➞type](Study_type.md)  <sub>1..1</sub>
     * Description: The type of Study. For example, 'Cancer Genomics', 'Epigenetics', 'Exome Sequencing'.
     * Range: [StudyTypeEnum](StudyTypeEnum.md)
 * [Study➞affiliation](Study_affiliation.md)  <sub>1..\*</sub>
     * Description: The Institution(s) associated with an entity.
     * Range: [String](types/String.md)
 * [Study➞has_project](Study_has_project.md)  <sub>0..1</sub>
     * Description: The project associated with this Study.
     * Range: [Project](Project.md)
 * [Study➞has_condition](Study_has_condition.md)  <sub>1..\*</sub>
     * Description: The condition associated with an entity.
     * Range: [Condition](Condition.md)
 * [Study➞title](Study_title.md)  <sub>1..1</sub>
     * Description: A comprehensive title for the study.
     * Range: [String](types/String.md)
 * [Study➞description](Study_description.md)  <sub>1..1</sub>
     * Description: A detailed description (abstract) that describes the goals of this Study.
     * Range: [String](types/String.md)
 * [Study➞has_attribute](Study_has_attribute.md)  <sub>0..\*</sub>
     * Description: Custom key/value pairs that further characterizes the Study. (e.g.: approaches - single-cell,_bulk_etc)
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

### Inherited from Investigation:

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
