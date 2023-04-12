
# Class: population


A population is a collection of individuals from the same taxonomic class living, counted or sampled at a particular site or in a particular area.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Population](https://w3id.org/GHGA-Submission-Metadata-Schema/Population)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Population&#124;name:string;id(i):string;alias(i):string;xref(i):string%20*]^-[Ancestry],[MaterialEntity]^-[Population],[MaterialEntity],[Ancestry])](https://yuml.me/diagram/nofunky;dir:TB/class/[Population&#124;name:string;id(i):string;alias(i):string;xref(i):string%20*]^-[Ancestry],[MaterialEntity]^-[Population],[MaterialEntity],[Ancestry])

## Parents

 *  is_a: [MaterialEntity](MaterialEntity.md) - A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.

## Children

 * [Ancestry](Ancestry.md) - Population category defined using ancestry informative markers (AIMs) based on genetic/genomic data.

## Referenced by Class


## Attributes


### Own

 * [population➞name](population_name.md)  <sub>1..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)

### Inherited from material entity:

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
