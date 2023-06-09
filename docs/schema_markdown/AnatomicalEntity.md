
# Class: AnatomicalEntity


Biological entity that is either an individual member of a biological species or constitutes the structural organization of an individual member of a biological species.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/AnatomicalEntity](https://w3id.org/GHGA-Submission-Metadata-Schema/AnatomicalEntity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClassMixin],[MaterialEntity],[AnatomicalEntity&#124;id:string;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F]uses%20-.->[OntologyClassMixin],[MaterialEntity]^-[AnatomicalEntity])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClassMixin],[MaterialEntity],[AnatomicalEntity&#124;id:string;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F]uses%20-.->[OntologyClassMixin],[MaterialEntity]^-[AnatomicalEntity])

## Parents

 *  is_a: [MaterialEntity](MaterialEntity.md) - A MaterialEntity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.

## Uses Mixin

 *  mixin: [OntologyClassMixin](OntologyClassMixin.md) - Mixin for entities that represent an class/term/concept from an ontology.

## Referenced by Class

 *  **None** *[anatomical_entities](anatomical_entities.md)*  <sub>0..\*</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**

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
| **Exact Mappings:** | | UBERON:0001062 |

