
# Class: investigation


Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.

URI: [GHGA:Investigation](https://w3id.org/GHGA/Investigation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[PlannedProcess],[Investigation&#124;title:string;description:string;id(i):string;alias(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string]^-[Study],[Investigation]^-[Experiment],[PlannedProcess]^-[Investigation],[Experiment])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[PlannedProcess],[Investigation&#124;title:string;description:string;id(i):string;alias(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string]^-[Study],[Investigation]^-[Experiment],[PlannedProcess]^-[Investigation],[Experiment])

## Parents

 *  is_a: [PlannedProcess](PlannedProcess.md) - A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and depends on some entity during the time it occurs.

## Children

 * [Experiment](Experiment.md) - An experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
 * [Study](Study.md) - Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

## Referenced by Class


## Attributes


### Own

 * [investigation➞title](investigation_title.md)  <sub>1..1</sub>
     * Description: The title that describes an entity.
     * Range: [String](types/String.md)
 * [investigation➞description](investigation_description.md)  <sub>1..1</sub>
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
 * [named thing➞xref](named_thing_xref.md)  <sub>1..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)
 * [named thing➞creation date](named_thing_creation_date.md)  <sub>1..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was created.
     * Range: [String](types/String.md)
 * [named thing➞update date](named_thing_update_date.md)  <sub>1..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was updated.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:000747 |
|  | | OBI:0000066 |

