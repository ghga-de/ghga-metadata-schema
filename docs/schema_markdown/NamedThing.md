
# Class: NamedThing


A database entity, concept or class. This is a generic class that is the root of all the other classes.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/NamedThing](https://w3id.org/GHGA-Submission-Metadata-Schema/NamedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PlannedProcess],[Person],[DeprecatedMixin]-%20replaced%20by%201..1>[NamedThing&#124;id:string;alias:string;xref:string%20*],[DeprecatedMixin]-%20replaced%20by(i)%200..1>[NamedThing],[NamedThing]^-[PlannedProcess],[NamedThing]^-[Person],[NamedThing]^-[MaterialEntity],[NamedThing]^-[InformationContentEntity],[NamedThing]^-[Committee],[NamedThing]^-[BiologicalQuality],[MaterialEntity],[InformationContentEntity],[DeprecatedMixin],[Committee],[BiologicalQuality])](https://yuml.me/diagram/nofunky;dir:TB/class/[PlannedProcess],[Person],[DeprecatedMixin]-%20replaced%20by%201..1>[NamedThing&#124;id:string;alias:string;xref:string%20*],[DeprecatedMixin]-%20replaced%20by(i)%200..1>[NamedThing],[NamedThing]^-[PlannedProcess],[NamedThing]^-[Person],[NamedThing]^-[MaterialEntity],[NamedThing]^-[InformationContentEntity],[NamedThing]^-[Committee],[NamedThing]^-[BiologicalQuality],[MaterialEntity],[InformationContentEntity],[DeprecatedMixin],[Committee],[BiologicalQuality])

## Children

 * [BiologicalQuality](BiologicalQuality.md) - A biological quality is a quality held by a biological entity.
 * [Committee](Committee.md) - A group of people organized for a specific purpose.
 * [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.
 * [MaterialEntity](MaterialEntity.md) - A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.
 * [Person](Person.md) - A member of the species Homo sapiens.
 * [PlannedProcess](PlannedProcess.md) - A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and depends on some entity during the time it occurs.

## Referenced by Class

 *  **[DeprecatedMixin](DeprecatedMixin.md)** *[deprecated mixin➞replaced by](deprecated_mixin_replaced_by.md)*  <sub>1..1</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[replaced by](replaced_by.md)*  <sub>0..1</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[replaces](replaces.md)*  <sub>0..1</sub>  **[NamedThing](NamedThing.md)**

## Attributes


### Own

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

|              |     |              |
| ------------ | --- | ------------ |
| **Aliases:** |     | named entity |
|              |     | entity       |
|              |     | object       |

