
# Class: MaterialEntity


A MaterialEntity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/MaterialEntity](https://w3id.org/GHGA-Submission-Metadata-Schema/MaterialEntity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[Population],[NamedThing],[MaterialEntity&#124;id(i):string;alias(i):string;xref(i):string%20*]^-[Sample],[MaterialEntity]^-[Population],[MaterialEntity]^-[Biospecimen],[MaterialEntity]^-[AnatomicalEntity],[NamedThing]^-[MaterialEntity],[Biospecimen],[AnatomicalEntity])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[Population],[NamedThing],[MaterialEntity&#124;id(i):string;alias(i):string;xref(i):string%20*]^-[Sample],[MaterialEntity]^-[Population],[MaterialEntity]^-[Biospecimen],[MaterialEntity]^-[AnatomicalEntity],[NamedThing]^-[MaterialEntity],[Biospecimen],[AnatomicalEntity])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A database entity, concept or class. This is a generic class that is the root of all the other classes.

## Children

 * [AnatomicalEntity](AnatomicalEntity.md) - Biological entity that is either an individual member of a biological species or constitutes the structural organization of an individual member of a biological species.
 * [Biospecimen](Biospecimen.md) - A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics, treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is derived.
 * [Population](Population.md) - A Population is a collection of individuals from the same taxonomic class living, counted or sampled at a particular site or in a particular area.
 * [Sample](Sample.md) - A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).

## Referenced by Class


## Attributes


### Inherited from NamedThing:

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
| **Exact Mappings:** | | SIO:000004 |

