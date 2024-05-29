
# Class: Condition


A Condition specifies which special characteristics and treatments apply to a Sample (e.g., whether the Sample comes from a disease or a healthy tissue).

URI: [GHGA:Condition](https://w3id.org/GHGA/Condition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[Sample],[IdentifiedByAliasMixin],[Study]<study%201..1-%20[Condition&#124;name:string;description:string;disease_or_healthy:DiseaseOrHealthyEnum;case_control_status:CaseControlStatusEnum;alias:string],[Sample]-%20condition%201..1>[Condition],[Submission]++-%20conditions%201..*>[Condition],[Sample]-%20condition(i)%200..1>[Condition],[Submission]-%20conditions(i)%200..*>[Condition],[Condition]uses%20-.->[IdentifiedByAliasMixin],[Condition]uses%20-.->[AttributeMixin],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[Sample],[IdentifiedByAliasMixin],[Study]<study%201..1-%20[Condition&#124;name:string;description:string;disease_or_healthy:DiseaseOrHealthyEnum;case_control_status:CaseControlStatusEnum;alias:string],[Sample]-%20condition%201..1>[Condition],[Submission]++-%20conditions%201..*>[Condition],[Sample]-%20condition(i)%200..1>[Condition],[Submission]-%20conditions(i)%200..*>[Condition],[Condition]uses%20-.->[IdentifiedByAliasMixin],[Condition]uses%20-.->[AttributeMixin],[AttributeMixin],[Attribute])

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

 * [Condition➞name](Condition_name.md)  <sub>1..1</sub>
     * Description: The name of this Condition.
     * Range: [String](types/String.md)
 * [Condition➞description](Condition_description.md)  <sub>1..1</sub>
     * Description: A concise description of the applied Condition.
     * Range: [String](types/String.md)
 * [Condition➞disease_or_healthy](Condition_disease_or_healthy.md)  <sub>1..1</sub>
     * Description: Whether a Condition corresponds to a disease or a healthy state.
     * Range: [DiseaseOrHealthyEnum](DiseaseOrHealthyEnum.md)
 * [Condition➞case_control_status](Condition_case_control_status.md)  <sub>1..1</sub>
     * Description: Whether a Condition corresponds to a treatment or a control.
     * Range: [CaseControlStatusEnum](CaseControlStatusEnum.md)
 * [Condition➞study](Condition_study.md)  <sub>1..1</sub>
     * Description: The Study associated with this Condition.
     * Range: [Study](Study.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)

### Mixed in from AttributeMixin:

 * [AttributeMixin➞attributes](AttributeMixin_attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
