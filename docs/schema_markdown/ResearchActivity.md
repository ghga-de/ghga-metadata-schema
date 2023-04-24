
# Class: ResearchActivity


A PlannedProcess executed in the performance of scientific research wherein systematic Investigations are performed to establish facts and reach new conclusions about phenomena in the world.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/ResearchActivity](https://w3id.org/GHGA-Submission-Metadata-Schema/ResearchActivity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PlannedProcess]^-[ResearchActivity&#124;title:string;description:string;id(i):string;alias(i):string;xref(i):string%20*],[PlannedProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[PlannedProcess]^-[ResearchActivity&#124;title:string;description:string;id(i):string;alias(i):string;xref(i):string%20*],[PlannedProcess])

## Parents

 *  is_a: [PlannedProcess](PlannedProcess.md) - A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and depends on some entity during the time it occurs.

## Referenced by Class


## Attributes


### Own

 * [ResearchActivity➞title](ResearchActivity_title.md)  <sub>1..1</sub>
     * Description: The title that describes an entity.
     * Range: [String](types/String.md)
 * [ResearchActivity➞description](ResearchActivity_description.md)  <sub>1..1</sub>
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
| **Exact Mappings:** | | SEPIO:0000004 |

