
# Class: phenotypic feature


The observable form taken by some character (or group of characters) in an individual or an organism, excluding pathology and disease. The detectable outward manifestations of a specific genotype.

URI: [GHGA:PhenotypicFeature](https://w3id.org/GHGA/PhenotypicFeature)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Biospecimen]++-%20has%20phenotypic%20feature%200..*>[PhenotypicFeature&#124;concept_identifier(i):string%20%3F;concept_name(i):string%20%3F;description(i):string%20%3F;ontology_name(i):string%20%3F;ontology_version(i):string%20%3F;name(i):string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Biospecimen]-%20has%20phenotypic%20feature(i)%200..1>[PhenotypicFeature],[Individual]-%20has%20phenotypic%20feature(i)%200..1>[PhenotypicFeature],[Individual]++-%20has%20phenotypic%20feature%200..*>[PhenotypicFeature],[DiseaseOrPhenotypicFeature]^-[PhenotypicFeature],[Individual],[DiseaseOrPhenotypicFeature],[Biospecimen])](https://yuml.me/diagram/nofunky;dir:TB/class/[Biospecimen]++-%20has%20phenotypic%20feature%200..*>[PhenotypicFeature&#124;concept_identifier(i):string%20%3F;concept_name(i):string%20%3F;description(i):string%20%3F;ontology_name(i):string%20%3F;ontology_version(i):string%20%3F;name(i):string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Biospecimen]-%20has%20phenotypic%20feature(i)%200..1>[PhenotypicFeature],[Individual]-%20has%20phenotypic%20feature(i)%200..1>[PhenotypicFeature],[Individual]++-%20has%20phenotypic%20feature%200..*>[PhenotypicFeature],[DiseaseOrPhenotypicFeature]^-[PhenotypicFeature],[Individual],[DiseaseOrPhenotypicFeature],[Biospecimen])

## Parents

 *  is_a: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) - Disease or Phenotypic Feature that the entity is associated with. This entity is a union of Disease and Phenotypic Feature and exists to accommodate situations where Disease concepts are used interchangeably with Phenotype concepts or vice-versa.

## Referenced by Class

 *  **[Biospecimen](Biospecimen.md)** *[biospecimen➞has phenotypic feature](biospecimen_has_phenotypic_feature.md)*  <sub>0..\*</sub>  **[PhenotypicFeature](PhenotypicFeature.md)**
 *  **None** *[has phenotypic feature](has_phenotypic_feature.md)*  <sub>0..1</sub>  **[PhenotypicFeature](PhenotypicFeature.md)**
 *  **[Individual](Individual.md)** *[individual➞has phenotypic feature](individual_has_phenotypic_feature.md)*  <sub>0..\*</sub>  **[PhenotypicFeature](PhenotypicFeature.md)**

## Attributes


### Inherited from disease or phenotypic feature:

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
| **Exact Mappings:** | | HP:0000118 |
|  | | EFO:0000651 |
|  | | SIO:010056 |

