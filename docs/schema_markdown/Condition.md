
# Class: Condition


An condition that is linked to comparable samples.

URI: [GHGA:Condition](https://w3id.org/GHGA/Condition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[Sample],[IdentifiedByAliasMixin],[Study]<study%201..1-%20[Condition&#124;title:string%20%3F;description:string;name:string;disease_or_healthy:DiseaseOrHealthyEnum;case_control_status:CaseControlStatusEnum;mutant_or_wildtype:MutantOrWildtypeEnum;alias:string],[Sample]-%20condition%201..1>[Condition],[Submission]++-%20conditions%201..*>[Condition],[Sample]-%20condition(i)%200..1>[Condition],[Submission]-%20conditions(i)%200..*>[Condition],[Condition]uses%20-.->[IdentifiedByAliasMixin],[Condition]uses%20-.->[AttributeMixin],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[Sample],[IdentifiedByAliasMixin],[Study]<study%201..1-%20[Condition&#124;title:string%20%3F;description:string;name:string;disease_or_healthy:DiseaseOrHealthyEnum;case_control_status:CaseControlStatusEnum;mutant_or_wildtype:MutantOrWildtypeEnum;alias:string],[Sample]-%20condition%201..1>[Condition],[Submission]++-%20conditions%201..*>[Condition],[Sample]-%20condition(i)%200..1>[Condition],[Submission]-%20conditions(i)%200..*>[Condition],[Condition]uses%20-.->[IdentifiedByAliasMixin],[Condition]uses%20-.->[AttributeMixin],[AttributeMixin],[Attribute])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[Sample](Sample.md)** *[Sample➞condition](Sample_condition.md)*  <sub>1..1</sub>  **[Condition](Condition.md)**
 *  **[Submission](Submission.md)** *[Submission➞conditions](Submission_conditions.md)*  <sub>1..\*</sub>  **[Condition](Condition.md)**
 *  **None** *[condition](condition.md)*  <sub>0..1</sub>  **[Condition](Condition.md)**
 *  **None** *[conditions](conditions.md)*  <sub>0..\*</sub>  **[Condition](Condition.md)**

## Attributes


### Own

 * [title](title.md)  <sub>0..1</sub>
     * Description: The title that describes an entity.
     * Range: [String](types/String.md)
 * [Condition➞description](Condition_description.md)  <sub>1..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)
 * [Condition➞name](Condition_name.md)  <sub>1..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)
 * [Condition➞disease_or_healthy](Condition_disease_or_healthy.md)  <sub>1..1</sub>
     * Description: Whether a condition corresponds to a disease or a healthy state.
     * Range: [DiseaseOrHealthyEnum](DiseaseOrHealthyEnum.md)
 * [Condition➞case_control_status](Condition_case_control_status.md)  <sub>1..1</sub>
     * Description: Whether a condition corresponds to a treatment or a control.
     * Range: [CaseControlStatusEnum](CaseControlStatusEnum.md)
 * [Condition➞mutant_or_wildtype](Condition_mutant_or_wildtype.md)  <sub>1..1</sub>
     * Description: Whether a condition corresponds to a mutant or a wildtype.
     * Range: [MutantOrWildtypeEnum](MutantOrWildtypeEnum.md)
 * [Condition➞study](Condition_study.md)  <sub>1..1</sub>
     * Description: The study associated with an entity.
     * Range: [Study](Study.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)

### Mixed in from AttributeMixin:

 * [AttributeMixin➞attributes](AttributeMixin_attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
