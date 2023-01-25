
# Class: research activity


A planned process executed in the performance of scientific research wherein systematic investigations are performed to establish facts and reach new conclusions about phenomena in the world.

URI: [GHGA:ResearchActivity](https://w3id.org/GHGA/ResearchActivity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ResearchActivity&#124;title:string;description:string;id(i):string;alias(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string]^-[Project],[PlannedProcess]^-[ResearchActivity],[Project],[PlannedProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[ResearchActivity&#124;title:string;description:string;id(i):string;alias(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string]^-[Project],[PlannedProcess]^-[ResearchActivity],[Project],[PlannedProcess])

## Parents

 *  is_a: [PlannedProcess](PlannedProcess.md) - A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and depends on some entity during the time it occurs.

## Children

 * [Project](Project.md) - A high level organization for a collection of studies based on a research proposal that aims to achieve certain goals.

## Referenced by Class


## Attributes


### Own

 * [research activity➞title](research_activity_title.md)  <sub>1..1</sub>
     * Description: The title that describes an entity.
     * Range: [String](types/String.md)
 * [research activity➞description](research_activity_description.md)  <sub>1..1</sub>
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
| **Exact Mappings:** | | SEPIO:0000004 |

