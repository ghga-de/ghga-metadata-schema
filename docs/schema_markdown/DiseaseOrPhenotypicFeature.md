
# Class: DiseaseOrPhenotypicFeature


Disease or Phenotypic Feature that the entity is associated with. This entity is a union of Disease and Phenotypic Feature and exists to accommodate situations where Disease concepts are used interchangeably with Phenotype concepts or vice-versa.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/DiseaseOrPhenotypicFeature](https://w3id.org/GHGA-Submission-Metadata-Schema/DiseaseOrPhenotypicFeature)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClassMixin],[DiseaseOrPhenotypicFeature&#124;id:string;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F]uses%20-.->[OntologyClassMixin],[DiseaseOrPhenotypicFeature]^-[Disease],[BiologicalQuality]^-[DiseaseOrPhenotypicFeature],[Disease],[BiologicalQuality])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClassMixin],[DiseaseOrPhenotypicFeature&#124;id:string;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F]uses%20-.->[OntologyClassMixin],[DiseaseOrPhenotypicFeature]^-[Disease],[BiologicalQuality]^-[DiseaseOrPhenotypicFeature],[Disease],[BiologicalQuality])

## Parents

 *  is_a: [BiologicalQuality](BiologicalQuality.md) - A BiologicalQuality is a quality held by a biological entity.

## Uses Mixin

 *  mixin: [OntologyClassMixin](OntologyClassMixin.md) - Mixin for entities that represent an class/term/concept from an ontology.

## Children

 * [Disease](Disease.md) - A disease is a disposition to undergo pathological processes that exists in an organism because of one or more disorders in that organism.

## Referenced by Class


## Attributes


### Mixed in from OntologyClassMixin:

 * [OntologyClassMixin➞id](OntologyClassMixin_id.md)  <sub>1..1</sub>
     * Description: An identifier that uniquely represents an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)

### Mixed in from OntologyClassMixin:

 * [OntologyClassMixin➞concept_identifier](OntologyClassMixin_concept_identifier.md)  <sub>0..1</sub>
     * Description: The Compact URI (CURIE) that uniquely identifies this ontology class.
     * Range: [String](types/String.md)

### Mixed in from OntologyClassMixin:

 * [OntologyClassMixin➞concept_name](OntologyClassMixin_concept_name.md)  <sub>0..1</sub>
     * Description: The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.
     * Range: [String](types/String.md)

### Mixed in from OntologyClassMixin:

 * [OntologyClassMixin➞description](OntologyClassMixin_description.md)  <sub>0..1</sub>
     * Description: The description or definition of an ontology class.
     * Range: [String](types/String.md)

### Mixed in from OntologyClassMixin:

 * [OntologyClassMixin➞ontology_name](OntologyClassMixin_ontology_name.md)  <sub>0..1</sub>
     * Description: The name or label (rdfs:label) of an ontology class.
     * Range: [String](types/String.md)

### Mixed in from OntologyClassMixin:

 * [OntologyClassMixin➞ontology_version](OntologyClassMixin_ontology_version.md)  <sub>0..1</sub>
     * Description: The version of the ontology from which this ontology class was chosen.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | biolink:DiseaseOrPhenotypicFeature |

