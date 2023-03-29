
# Class: investigation


Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Investigation](https://w3id.org/GHGA-Submission-Metadata-Schema/Investigation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[StudyDesign],[Study],[SequencingReplicate],[SequencingProcess],[SequencingExperiment],[PlannedProcess],[Investigation&#124;title:string%20%3F;description:string%20%3F;id(i):string;alias(i):string;xref(i):string%20*]^-[StudyDesign],[Investigation]^-[Study],[Investigation]^-[SequencingReplicate],[Investigation]^-[SequencingProcess],[Investigation]^-[SequencingExperiment],[Investigation]^-[Condition],[PlannedProcess]^-[Investigation],[Condition])](https://yuml.me/diagram/nofunky;dir:TB/class/[StudyDesign],[Study],[SequencingReplicate],[SequencingProcess],[SequencingExperiment],[PlannedProcess],[Investigation&#124;title:string%20%3F;description:string%20%3F;id(i):string;alias(i):string;xref(i):string%20*]^-[StudyDesign],[Investigation]^-[Study],[Investigation]^-[SequencingReplicate],[Investigation]^-[SequencingProcess],[Investigation]^-[SequencingExperiment],[Investigation]^-[Condition],[PlannedProcess]^-[Investigation],[Condition])

## Parents

 *  is_a: [PlannedProcess](PlannedProcess.md) - A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and depends on some entity during the time it occurs.

## Children

 * [Condition](Condition.md) - An condition that is linked to comparable samples.
 * [SequencingExperiment](SequencingExperiment.md) - An sequencing experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
 * [SequencingProcess](SequencingProcess.md) - A sequencing process linking a sample to sequencing output.
 * [SequencingReplicate](SequencingReplicate.md) - A technical sequencing replicate. E.g. the same sample sequenced across multiple lanes.
 * [Study](Study.md) - Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.
 * [StudyDesign](StudyDesign.md) - The design of the study that defines all conditions that are compared.

## Referenced by Class


## Attributes


### Own

 * [title](title.md)  <sub>0..1</sub>
     * Description: The title that describes an entity.
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)

### Inherited from planned process:

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:000747 |
|  | | OBI:0000066 |

