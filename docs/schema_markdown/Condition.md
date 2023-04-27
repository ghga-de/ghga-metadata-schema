
# Class: Condition


An condition that is linked to comparable samples.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Condition](https://w3id.org/GHGA-Submission-Metadata-Schema/Condition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[Sample],[Investigation],[IdentifiedByAliasMixin],[Sample]++-%20condition%201..1>[Condition&#124;name:string;description:string;disease_or_healthy:DiseaseOrHealthyEnum;treatment_or_control:TreatmentOrControlEnum;mutant_or_wildtype:MutantOrWildtypeEnum;title(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[Study]++-%20conditions%201..*>[Condition],[Sample]++-%20condition(i)%200..1>[Condition],[Study]++-%20conditions(i)%200..*>[Condition],[Condition]uses%20-.->[IdentifiedByAliasMixin],[Condition]uses%20-.->[AttributeMixin],[Investigation]^-[Condition],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[Sample],[Investigation],[IdentifiedByAliasMixin],[Sample]++-%20condition%201..1>[Condition&#124;name:string;description:string;disease_or_healthy:DiseaseOrHealthyEnum;treatment_or_control:TreatmentOrControlEnum;mutant_or_wildtype:MutantOrWildtypeEnum;title(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[Study]++-%20conditions%201..*>[Condition],[Sample]++-%20condition(i)%200..1>[Condition],[Study]++-%20conditions(i)%200..*>[Condition],[Condition]uses%20-.->[IdentifiedByAliasMixin],[Condition]uses%20-.->[AttributeMixin],[Investigation]^-[Condition],[AttributeMixin],[Attribute])

## Parents

 *  is_a: [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[Sample](Sample.md)** *[Sample➞condition](Sample_condition.md)*  <sub>1..1</sub>  **[Condition](Condition.md)**
 *  **[Study](Study.md)** *[Study➞conditions](Study_conditions.md)*  <sub>1..\*</sub>  **[Condition](Condition.md)**
 *  **None** *[condition](condition.md)*  <sub>0..1</sub>  **[Condition](Condition.md)**
 *  **None** *[conditions](conditions.md)*  <sub>0..\*</sub>  **[Condition](Condition.md)**

## Attributes


### Own

 * [Condition➞name](Condition_name.md)  <sub>1..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)
 * [Condition➞description](Condition_description.md)  <sub>1..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)
 * [Condition➞disease_or_healthy](Condition_disease_or_healthy.md)  <sub>1..1</sub>
     * Description: Whether a condition corresponds to a disease or a healthy state.
     * Range: [DiseaseOrHealthyEnum](DiseaseOrHealthyEnum.md)
 * [Condition➞treatment_or_control](Condition_treatment_or_control.md)  <sub>1..1</sub>
     * Description: Whether a condition corresponds to a treatment or a control.
     * Range: [TreatmentOrControlEnum](TreatmentOrControlEnum.md)
 * [Condition➞mutant_or_wildtype](Condition_mutant_or_wildtype.md)  <sub>1..1</sub>
     * Description: Whether a condition corresponds to a mutant or a wildtype.
     * Range: [MutantOrWildtypeEnum](MutantOrWildtypeEnum.md)

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
 * [title](title.md)  <sub>0..1</sub>
     * Description: The title that describes an entity.
     * Range: [String](types/String.md)

### Mixed in from AttributeMixin:

 * [attributes](attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)
