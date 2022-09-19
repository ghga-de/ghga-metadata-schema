
# Class: material entity


A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.

URI: [GHGA:MaterialEntity](https://w3id.org/GHGA/MaterialEntity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[Population],[NamedThing],[MaterialEntity&#124;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F]^-[Sample],[MaterialEntity]^-[Population],[MaterialEntity]^-[CellLine],[MaterialEntity]^-[Biospecimen],[MaterialEntity]^-[AnatomicalEntity],[NamedThing]^-[MaterialEntity],[CellLine],[Biospecimen],[AnatomicalEntity])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[Population],[NamedThing],[MaterialEntity&#124;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F]^-[Sample],[MaterialEntity]^-[Population],[MaterialEntity]^-[CellLine],[MaterialEntity]^-[Biospecimen],[MaterialEntity]^-[AnatomicalEntity],[NamedThing]^-[MaterialEntity],[CellLine],[Biospecimen],[AnatomicalEntity])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A databased entity, concept or class. This is a generic class that is the root of all the other classes.

## Children

 * [AnatomicalEntity](AnatomicalEntity.md) - Biological entity that is either an individual member of a biological species or constitutes the structural organization of an individual member of a biological species.
 * [Biospecimen](Biospecimen.md) - A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics, treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is derived.
 * [CellLine](CellLine.md) - A cultured cell population that represents a genetically stable and homogenous population of cultured cells that shares a common propagation history.
 * [Population](Population.md) - A population is a collection of individuals from the same taxonomic class living, counted or sampled at a particular site or in a particular area.
 * [Sample](Sample.md) - A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).

## Referenced by Class


## Attributes


### Inherited from named thing:

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:000004 |

