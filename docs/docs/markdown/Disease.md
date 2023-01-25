
# Class: disease


A disease is a disposition to undergo pathological processes that exists in an organism because of one or more disorders in that organism.

URI: [GHGA:Disease](https://w3id.org/GHGA/Disease)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Individual],[DiseaseOrPhenotypicFeature],[Individual]-%20has%20disease(i)%200..1>[Disease&#124;concept_identifier(i):string;concept_name(i):string%20%3F;description(i):string;ontology_name(i):string;ontology_version(i):string;id(i):string;alias(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[Individual]++-%20has%20disease%201..*>[Disease],[DiseaseOrPhenotypicFeature]^-[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[Individual],[DiseaseOrPhenotypicFeature],[Individual]-%20has%20disease(i)%200..1>[Disease&#124;concept_identifier(i):string;concept_name(i):string%20%3F;description(i):string;ontology_name(i):string;ontology_version(i):string;id(i):string;alias(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[Individual]++-%20has%20disease%201..*>[Disease],[DiseaseOrPhenotypicFeature]^-[Disease])

## Parents

 *  is_a: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) - Disease or Phenotypic Feature that the entity is associated with. This entity is a union of Disease and Phenotypic Feature and exists to accommodate situations where Disease concepts are used interchangeably with Phenotype concepts or vice-versa.

## Referenced by Class

 *  **None** *[has disease](has_disease.md)*  <sub>0..1</sub>  **[Disease](Disease.md)**
 *  **[Individual](Individual.md)** *[individual➞has disease](individual_has_disease.md)*  <sub>1..\*</sub>  **[Disease](Disease.md)**

## Attributes


### Inherited from disease or phenotypic feature:

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
| **Exact Mappings:** | | EFO:0000408 |
|  | | MONDO:0000001 |

