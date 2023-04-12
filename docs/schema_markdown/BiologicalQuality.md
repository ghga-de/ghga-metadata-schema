
# Class: biological quality


A biological quality is a quality held by a biological entity.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/BiologicalQuality](https://w3id.org/GHGA-Submission-Metadata-Schema/BiologicalQuality)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DiseaseOrPhenotypicFeature],[BiologicalQuality&#124;id(i):string;alias(i):string;xref(i):string%20*]^-[DiseaseOrPhenotypicFeature],[NamedThing]^-[BiologicalQuality])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DiseaseOrPhenotypicFeature],[BiologicalQuality&#124;id(i):string;alias(i):string;xref(i):string%20*]^-[DiseaseOrPhenotypicFeature],[NamedThing]^-[BiologicalQuality])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A database entity, concept or class. This is a generic class that is the root of all the other classes.

## Children

 * [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) - Disease or Phenotypic Feature that the entity is associated with. This entity is a union of Disease and Phenotypic Feature and exists to accommodate situations where Disease concepts are used interchangeably with Phenotype concepts or vice-versa.

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

|                     |     |            |
| ------------------- | --- | ---------- |
| **Exact Mappings:** |     | SIO:000475 |

