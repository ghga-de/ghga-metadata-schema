
# Class: study design


The design of the study that defines all conditions that are compared.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/StudyDesign](https://w3id.org/GHGA-Submission-Metadata-Schema/StudyDesign)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Condition]<has%20condition%201..*-%20[StudyDesign&#124;description:string;accession:string;title(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[Study]<has%20study%201..1-%20[StudyDesign],[StudyDesign]uses%20-.->[AccessionMixin],[StudyDesign]uses%20-.->[AttributeMixin],[Investigation]^-[StudyDesign],[Study],[Investigation],[Condition],[AttributeMixin],[Attribute],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Condition]<has%20condition%201..*-%20[StudyDesign&#124;description:string;accession:string;title(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[Study]<has%20study%201..1-%20[StudyDesign],[StudyDesign]uses%20-.->[AccessionMixin],[StudyDesign]uses%20-.->[AttributeMixin],[Investigation]^-[StudyDesign],[Study],[Investigation],[Condition],[AttributeMixin],[Attribute],[AccessionMixin])

## Parents

 *  is_a: [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class


## Attributes


### Own

 * [study design➞description](study_design_description.md)  <sub>1..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)
 * [study design➞has study](study_design_has_study.md)  <sub>1..1</sub>
     * Description: The study associated with an entity.
     * Range: [Study](Study.md)
 * [study design➞has condition](study_design_has_condition.md)  <sub>1..\*</sub>
     * Description: The condition associated with an entity.
     * Range: [Condition](Condition.md)

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

### Mixed in from attribute mixin:

 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)
