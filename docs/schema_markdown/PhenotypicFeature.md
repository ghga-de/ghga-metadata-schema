
# Class: PhenotypicFeature


The observable form taken by some character (or group of characters) in an individual or an organism, excluding pathology and disease. The detectable outward manifestations of a specific genotype.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/PhenotypicFeature](https://w3id.org/GHGA-Submission-Metadata-Schema/PhenotypicFeature)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Individual]++-%20phenotypic_features%200..*>[PhenotypicFeature&#124;concept_identifier(i):string%20%3F;concept_name(i):string%20%3F;description(i):string%20%3F;ontology_name(i):string%20%3F;ontology_version(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[Individual]-%20phenotypic_features(i)%200..*>[PhenotypicFeature],[DiseaseOrPhenotypicFeature]^-[PhenotypicFeature],[Individual],[DiseaseOrPhenotypicFeature])](https://yuml.me/diagram/nofunky;dir:TB/class/[Individual]++-%20phenotypic_features%200..*>[PhenotypicFeature&#124;concept_identifier(i):string%20%3F;concept_name(i):string%20%3F;description(i):string%20%3F;ontology_name(i):string%20%3F;ontology_version(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[Individual]-%20phenotypic_features(i)%200..*>[PhenotypicFeature],[DiseaseOrPhenotypicFeature]^-[PhenotypicFeature],[Individual],[DiseaseOrPhenotypicFeature])

## Parents

 *  is_a: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) - Disease or Phenotypic Feature that the entity is associated with. This entity is a union of Disease and Phenotypic Feature and exists to accommodate situations where Disease concepts are used interchangeably with Phenotype concepts or vice-versa.

## Referenced by Class

 *  **[Individual](Individual.md)** *[Individual➞phenotypic_features](Individual_phenotypic_features.md)*  <sub>0..\*</sub>  **[PhenotypicFeature](PhenotypicFeature.md)**
 *  **None** *[phenotypic_features](phenotypic_features.md)*  <sub>0..\*</sub>  **[PhenotypicFeature](PhenotypicFeature.md)**

## Attributes


### Inherited from DiseaseOrPhenotypicFeature:

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
| **Exact Mappings:** | | HP:0000118 |
|  | | EFO:0000651 |
|  | | SIO:010056 |

