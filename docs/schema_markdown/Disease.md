
# Class: disease


A disease is a disposition to undergo pathological processes that exists in an organism because of one or more disorders in that organism.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Disease](https://w3id.org/GHGA-Submission-Metadata-Schema/Disease)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Individual],[DiseaseOrPhenotypicFeature],[Individual]-%20has%20disease(i)%200..1>[Disease&#124;concept_identifier(i):string%20%3F;concept_name(i):string%20%3F;description(i):string%20%3F;ontology_name(i):string%20%3F;ontology_version(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[Individual]++-%20has%20disease%201..*>[Disease],[DiseaseOrPhenotypicFeature]^-[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[Individual],[DiseaseOrPhenotypicFeature],[Individual]-%20has%20disease(i)%200..1>[Disease&#124;concept_identifier(i):string%20%3F;concept_name(i):string%20%3F;description(i):string%20%3F;ontology_name(i):string%20%3F;ontology_version(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[Individual]++-%20has%20disease%201..*>[Disease],[DiseaseOrPhenotypicFeature]^-[Disease])

## Parents

 *  is_a: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) - Disease or Phenotypic Feature that the entity is associated with. This entity is a union of Disease and Phenotypic Feature and exists to accommodate situations where Disease concepts are used interchangeably with Phenotype concepts or vice-versa.

## Referenced by Class

 *  **None** *[has disease](has_disease.md)*  <sub>0..1</sub>  **[Disease](Disease.md)**
 *  **[Individual](Individual.md)** *[individual➞has disease](individual_has_disease.md)*  <sub>1..\*</sub>  **[Disease](Disease.md)**

## Attributes


### Inherited from disease or phenotypic feature:

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

|                     |     |               |
| ------------------- | --- | ------------- |
| **Exact Mappings:** |     | EFO:0000408   |
|                     |     | MONDO:0000001 |

