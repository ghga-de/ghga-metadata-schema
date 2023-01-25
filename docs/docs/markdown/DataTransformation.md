
# Class: data transformation


A data transformation technique used to analyze and interpret data to gain a better understanding of it.

URI: [GHGA:DataTransformation](https://w3id.org/GHGA/DataTransformation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PlannedProcess],[DataTransformation&#124;title:string;description:string;id(i):string;alias(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string]^-[Analysis],[PlannedProcess]^-[DataTransformation],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[PlannedProcess],[DataTransformation&#124;title:string;description:string;id(i):string;alias(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string]^-[Analysis],[PlannedProcess]^-[DataTransformation],[Analysis])

## Parents

 *  is_a: [PlannedProcess](PlannedProcess.md) - A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and depends on some entity during the time it occurs.

## Children

 * [Analysis](Analysis.md) - An Analysis is a data transformation that transforms input data to output data. The workflow used to achieve this transformation and the individual steps are also captured.

## Referenced by Class


## Attributes


### Own

 * [data transformation➞title](data_transformation_title.md)  <sub>1..1</sub>
     * Description: The title that describes an entity.
     * Range: [String](types/String.md)
 * [data transformation➞description](data_transformation_description.md)  <sub>1..1</sub>
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
| **Exact Mappings:** | | OBI:0200000 |

