
# Class: Disease


A disease is a disposition to undergo pathological processes that exists in an organism because of one or more disorders in that organism.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Disease](https://w3id.org/GHGA-Submission-Metadata-Schema/Disease)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Individual],[DiseaseOrPhenotypicFeature],[Individual]++-%20diseases%201..*>[Disease&#124;id(i):string;concept_identifier(i):string%20%3F;concept_name(i):string%20%3F;description(i):string%20%3F;ontology_name(i):string%20%3F;ontology_version(i):string%20%3F],[Individual]++-%20diseases(i)%200..*>[Disease],[DiseaseOrPhenotypicFeature]^-[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[Individual],[DiseaseOrPhenotypicFeature],[Individual]++-%20diseases%201..*>[Disease&#124;id(i):string;concept_identifier(i):string%20%3F;concept_name(i):string%20%3F;description(i):string%20%3F;ontology_name(i):string%20%3F;ontology_version(i):string%20%3F],[Individual]++-%20diseases(i)%200..*>[Disease],[DiseaseOrPhenotypicFeature]^-[Disease])

## Parents

 *  is_a: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) - Disease or Phenotypic Feature that the entity is associated with. This entity is a union of Disease and Phenotypic Feature and exists to accommodate situations where Disease concepts are used interchangeably with Phenotype concepts or vice-versa.

## Referenced by Class

 *  **[Individual](Individual.md)** *[Individual➞diseases](Individual_diseases.md)*  <sub>1..\*</sub>  **[Disease](Disease.md)**
 *  **None** *[diseases](diseases.md)*  <sub>0..\*</sub>  **[Disease](Disease.md)**

## Attributes


## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | EFO:0000408 |
|  | | MONDO:0000001 |

