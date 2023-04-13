
# Class: DataTransformation


A DataTransformation technique used to analyze and interpret data to gain a better understanding of it.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/DataTransformation](https://w3id.org/GHGA-Submission-Metadata-Schema/DataTransformation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PlannedProcess],[DataTransformation&#124;title:string%20%3F;description:string%20%3F;id(i):string;alias(i):string;xref(i):string%20*]^-[Analysis],[PlannedProcess]^-[DataTransformation],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[PlannedProcess],[DataTransformation&#124;title:string%20%3F;description:string%20%3F;id(i):string;alias(i):string;xref(i):string%20*]^-[Analysis],[PlannedProcess]^-[DataTransformation],[Analysis])

## Parents

 *  is_a: [PlannedProcess](PlannedProcess.md) - A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and depends on some entity during the time it occurs.

## Children

 * [Analysis](Analysis.md) - An Analysis is a data transformation that transforms input data to output data. The workflow used to achieve this transformation and the individual steps are also captured.

## Referenced by Class


## Attributes


### Own

 * [title](title.md)  <sub>0..1</sub>
     * Description: The title that describes an entity.
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)

### Inherited from PlannedProcess:

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | OBI:0200000 |

