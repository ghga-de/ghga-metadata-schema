
# Class: named thing


A databased entity, concept or class. This is a generic class that is the root of all the other classes.

URI: [GHGA:NamedThing](https://w3id.org/GHGA/NamedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PlannedProcess],[Person],[DeprecatedMixin]-%20replaced%20by%200..1>[NamedThing&#124;id:string;alias:string%20%3F;xref:string%20*;creation_date:string%20%3F;update_date:string%20%3F;schema_type:string%20%3F;schema_version:string%20%3F],[NamedThing]uses%20-.->[MetadataMixin],[NamedThing]^-[PlannedProcess],[NamedThing]^-[Person],[NamedThing]^-[MaterialEntity],[NamedThing]^-[InformationContentEntity],[NamedThing]^-[Committee],[NamedThing]^-[BiologicalQuality],[NamedThing]^-[Agent],[MetadataMixin],[MaterialEntity],[InformationContentEntity],[DeprecatedMixin],[Committee],[BiologicalQuality],[Agent])](https://yuml.me/diagram/nofunky;dir:TB/class/[PlannedProcess],[Person],[DeprecatedMixin]-%20replaced%20by%200..1>[NamedThing&#124;id:string;alias:string%20%3F;xref:string%20*;creation_date:string%20%3F;update_date:string%20%3F;schema_type:string%20%3F;schema_version:string%20%3F],[NamedThing]uses%20-.->[MetadataMixin],[NamedThing]^-[PlannedProcess],[NamedThing]^-[Person],[NamedThing]^-[MaterialEntity],[NamedThing]^-[InformationContentEntity],[NamedThing]^-[Committee],[NamedThing]^-[BiologicalQuality],[NamedThing]^-[Agent],[MetadataMixin],[MaterialEntity],[InformationContentEntity],[DeprecatedMixin],[Committee],[BiologicalQuality],[Agent])

## Uses Mixin

 *  mixin: [MetadataMixin](MetadataMixin.md) - Mixin for tracking schema specific metadata about an instance.

## Children

 * [Agent](Agent.md) - An agent is something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity. Agents include a Person, Organization, or Software that performs an activity.
 * [BiologicalQuality](BiologicalQuality.md) - A biological quality is a quality held by a biological entity.
 * [Committee](Committee.md) - A group of people organized for a specific purpose.
 * [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.
 * [MaterialEntity](MaterialEntity.md) - A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.
 * [Person](Person.md) - A member of the species Homo sapiens.
 * [PlannedProcess](PlannedProcess.md) - A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and depends on some entity during the time it occurs.

## Referenced by Class

 *  **[NamedThing](NamedThing.md)** *[replaced by](replaced_by.md)*  <sub>0..1</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[replaces](replaces.md)*  <sub>0..1</sub>  **[NamedThing](NamedThing.md)**

## Attributes


### Own

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [named thing➞alias](named_thing_alias.md)  <sub>0..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [named thing➞xref](named_thing_xref.md)  <sub>0..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)
     * in subsets: (optional,public)
 * [named thing➞creation date](named_thing_creation_date.md)  <sub>0..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was created.
     * Range: [String](types/String.md)
 * [named thing➞update date](named_thing_update_date.md)  <sub>0..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was updated.
     * Range: [String](types/String.md)

### Mixed in from metadata mixin:

 * [schema type](schema_type.md)  <sub>0..1</sub>
     * Description: The schema type an instance corresponds to.
     * Range: [String](types/String.md)

### Mixed in from metadata mixin:

 * [schema version](schema_version.md)  <sub>0..1</sub>
     * Description: The version of the schema an instance corresponds to.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | named entity |
|  | | entity |
|  | | object |

