
# Class: OntologyClassMixin


Mixin for entities that represent an class/term/concept from an ontology.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/OntologyClassMixin](https://w3id.org/GHGA-Submission-Metadata-Schema/OntologyClassMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DiseaseOrPhenotypicFeature]uses%20-.->[OntologyClassMixin&#124;id:string;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F],[DataUseModifier]uses%20-.->[OntologyClassMixin],[AnatomicalEntity]uses%20-.->[OntologyClassMixin],[DiseaseOrPhenotypicFeature],[DataUseModifier],[AnatomicalEntity])](https://yuml.me/diagram/nofunky;dir:TB/class/[DiseaseOrPhenotypicFeature]uses%20-.->[OntologyClassMixin&#124;id:string;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F],[DataUseModifier]uses%20-.->[OntologyClassMixin],[AnatomicalEntity]uses%20-.->[OntologyClassMixin],[DiseaseOrPhenotypicFeature],[DataUseModifier],[AnatomicalEntity])

## Mixin for

 * [AnatomicalEntity](AnatomicalEntity.md) (mixin)  - Biological entity that is either an individual member of a biological species or constitutes the structural organization of an individual member of a biological species.
 * [DataUseModifier](DataUseModifier.md) (mixin)  - Data use modifiers indicate additional conditions for use.
 * [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) (mixin)  - Disease or Phenotypic Feature that the entity is associated with. This entity is a union of Disease and Phenotypic Feature and exists to accommodate situations where Disease concepts are used interchangeably with Phenotype concepts or vice-versa.

## Referenced by Class


## Attributes


### Own

 * [OntologyClassMixin➞id](OntologyClassMixin_id.md)  <sub>1..1</sub>
     * Description: An identifier that uniquely represents an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [OntologyClassMixin➞concept_identifier](OntologyClassMixin_concept_identifier.md)  <sub>0..1</sub>
     * Description: The Compact URI (CURIE) that uniquely identifies this ontology class.
     * Range: [String](types/String.md)
 * [OntologyClassMixin➞concept_name](OntologyClassMixin_concept_name.md)  <sub>0..1</sub>
     * Description: The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.
     * Range: [String](types/String.md)
 * [OntologyClassMixin➞description](OntologyClassMixin_description.md)  <sub>0..1</sub>
     * Description: The description or definition of an ontology class.
     * Range: [String](types/String.md)
 * [OntologyClassMixin➞ontology_name](OntologyClassMixin_ontology_name.md)  <sub>0..1</sub>
     * Description: The name or label (rdfs:label) of an ontology class.
     * Range: [String](types/String.md)
 * [OntologyClassMixin➞ontology_version](OntologyClassMixin_ontology_version.md)  <sub>0..1</sub>
     * Description: The version of the ontology from which this ontology class was chosen.
     * Range: [String](types/String.md)
