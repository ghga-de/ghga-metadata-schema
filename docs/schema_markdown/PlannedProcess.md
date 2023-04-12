
# Class: planned process


A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and depends on some entity during the time it occurs.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/PlannedProcess](https://w3id.org/GHGA-Submission-Metadata-Schema/PlannedProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ResearchActivity],[PlannedProcess&#124;id(i):string;alias(i):string;xref(i):string%20*]^-[ResearchActivity],[PlannedProcess]^-[Investigation],[PlannedProcess]^-[DataTransformation],[NamedThing]^-[PlannedProcess],[NamedThing],[Investigation],[DataTransformation])](https://yuml.me/diagram/nofunky;dir:TB/class/[ResearchActivity],[PlannedProcess&#124;id(i):string;alias(i):string;xref(i):string%20*]^-[ResearchActivity],[PlannedProcess]^-[Investigation],[PlannedProcess]^-[DataTransformation],[NamedThing]^-[PlannedProcess],[NamedThing],[Investigation],[DataTransformation])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A database entity, concept or class. This is a generic class that is the root of all the other classes.

## Children

 * [DataTransformation](DataTransformation.md) - A data transformation technique used to analyze and interpret data to gain a better understanding of it.
 * [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.
 * [ResearchActivity](ResearchActivity.md) - A planned process executed in the performance of scientific research wherein systematic investigations are performed to establish facts and reach new conclusions about phenomena in the world.

## Referenced by Class


## Attributes


### Inherited from NamedThing:

 * [NamedThing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [NamedThing➞alias](named_thing_alias.md)  <sub>1..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [NamedThing➞xref](named_thing_xref.md)  <sub>0..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)

## Other properties

|                     |     |             |
| ------------------- | --- | ----------- |
| **Exact Mappings:** |     | EFO:0004542 |
|                     |     | OBI:0000011 |
|                     |     | COB:0000082 |

