
# Class: DataUseModifier


Data use modifiers indicate additional conditions for use.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/DataUseModifier](https://w3id.org/GHGA-Submission-Metadata-Schema/DataUseModifier)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClassMixin],[InformationContentEntity],[DataAccessPolicy]++-%20data_use_modifiers%200..1>[DataUseModifier&#124;id:string;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F],[DataAccessPolicy]++-%20data_use_modifiers(i)%200..1>[DataUseModifier],[DataUseModifier]uses%20-.->[OntologyClassMixin],[InformationContentEntity]^-[DataUseModifier],[DataAccessPolicy])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClassMixin],[InformationContentEntity],[DataAccessPolicy]++-%20data_use_modifiers%200..1>[DataUseModifier&#124;id:string;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F],[DataAccessPolicy]++-%20data_use_modifiers(i)%200..1>[DataUseModifier],[DataUseModifier]uses%20-.->[OntologyClassMixin],[InformationContentEntity]^-[DataUseModifier],[DataAccessPolicy])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Uses Mixin

 *  mixin: [OntologyClassMixin](OntologyClassMixin.md) - Mixin for entities that represent an class/term/concept from an ontology.

## Referenced by Class

 *  **[DataAccessPolicy](DataAccessPolicy.md)** *[DataAccessPolicy➞data_use_modifiers](DataAccessPolicy_data_use_modifiers.md)*  <sub>0..1</sub>  **[DataUseModifier](DataUseModifier.md)**
 *  **None** *[data_use_modifiers](data_use_modifiers.md)*  <sub>0..1</sub>  **[DataUseModifier](DataUseModifier.md)**

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
| **Exact Mappings:** | | DUO:0000017 |

