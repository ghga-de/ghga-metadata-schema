
# Class: condition


An condition that is linked to comparable samples.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Condition](https://w3id.org/GHGA-Submission-Metadata-Schema/Condition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[StudyDesign],[Sample],[Investigation],[StudyDesign]-%20has%20condition(i)%200..1>[Condition&#124;name:string;description:string;disease_or_healthy:disease_or_healthy_enum;treatment_or_control:treatment_or_control_enum;mutant_or_wildtype:mutant_or_wildtype_enum;accession:string;title(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[Sample]-%20has%20condition(i)%200..1>[Condition],[Sample]-%20has%20condition%201..1>[Condition],[StudyDesign]-%20has%20condition%201..*>[Condition],[Condition]uses%20-.->[AccessionMixin],[Investigation]^-[Condition],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[StudyDesign],[Sample],[Investigation],[StudyDesign]-%20has%20condition(i)%200..1>[Condition&#124;name:string;description:string;disease_or_healthy:disease_or_healthy_enum;treatment_or_control:treatment_or_control_enum;mutant_or_wildtype:mutant_or_wildtype_enum;accession:string;title(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[Sample]-%20has%20condition(i)%200..1>[Condition],[Sample]-%20has%20condition%201..1>[Condition],[StudyDesign]-%20has%20condition%201..*>[Condition],[Condition]uses%20-.->[AccessionMixin],[Investigation]^-[Condition],[AccessionMixin])

## Parents

 *  is_a: [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.

## Referenced by Class

 *  **None** *[has condition](has_condition.md)*  <sub>0..1</sub>  **[Condition](Condition.md)**
 *  **[Sample](Sample.md)** *[sample➞has condition](sample_has_condition.md)*  <sub>1..1</sub>  **[Condition](Condition.md)**
 *  **[StudyDesign](StudyDesign.md)** *[study design➞has condition](study_design_has_condition.md)*  <sub>1..\*</sub>  **[Condition](Condition.md)**

## Attributes


### Own

 * [condition➞name](condition_name.md)  <sub>1..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)
 * [condition➞description](condition_description.md)  <sub>1..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)
 * [condition➞disease or healthy](condition_disease_or_healthy.md)  <sub>1..1</sub>
     * Description: Whether a condition corresponds to a disease or a healthy state.
     * Range: [disease or healthy enum](disease or healthy enum.md)
 * [condition➞treatment or control](condition_treatment_or_control.md)  <sub>1..1</sub>
     * Description: Whether a condition corresponds to a treatment or a control.
     * Range: [treatment or control enum](treatment or control enum.md)
 * [condition➞mutant or wildtype](condition_mutant_or_wildtype.md)  <sub>1..1</sub>
     * Description: Whether a condition corresponds to a mutant or a wildtype.
     * Range: [mutant or wildtype enum](mutant or wildtype enum.md)

### Inherited from investigation:

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
 * [title](title.md)  <sub>0..1</sub>
     * Description: The title that describes an entity.
     * Range: [String](types/String.md)

### Mixed in from accession mixin:

 * [accession mixin➞accession](accession_mixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)
