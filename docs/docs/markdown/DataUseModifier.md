
# Class: data use modifier


Data use modifiers indicate additional conditions for use.

URI: [GHGA:DataUseModifier](https://w3id.org/GHGA/DataUseModifier)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClassMixin],[InformationContentEntity],[DataAccessPolicy]++-%20has%20data%20use%20modifier%200..*>[DataUseModifier&#124;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F;name:string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[DataAccessPolicy]++-%20has%20data%20use%20modifier(i)%200..1>[DataUseModifier],[DataUseModifier]uses%20-.->[OntologyClassMixin],[InformationContentEntity]^-[DataUseModifier],[DataAccessPolicy])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClassMixin],[InformationContentEntity],[DataAccessPolicy]++-%20has%20data%20use%20modifier%200..*>[DataUseModifier&#124;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F;name:string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[DataAccessPolicy]++-%20has%20data%20use%20modifier(i)%200..1>[DataUseModifier],[DataUseModifier]uses%20-.->[OntologyClassMixin],[InformationContentEntity]^-[DataUseModifier],[DataAccessPolicy])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Uses Mixin

 *  mixin: [OntologyClassMixin](OntologyClassMixin.md) - Mixin for entities that represent an class/term/concept from an ontology.

## Referenced by Class

 *  **[DataAccessPolicy](DataAccessPolicy.md)** *[data access policy➞has data use modifier](data_access_policy_has_data_use_modifier.md)*  <sub>0..\*</sub>  **[DataUseModifier](DataUseModifier.md)**
 *  **None** *[has data use modifier](has_data_use_modifier.md)*  <sub>0..1</sub>  **[DataUseModifier](DataUseModifier.md)**

## Attributes


### Inherited from information content entity:

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

### Mixed in from ontology class mixin:

 * [ontology class mixin➞concept identifier](ontology_class_mixin_concept_identifier.md)  <sub>0..1</sub>
     * Description: The Compact URI (CURIE) that uniquely identifies this ontology class.
     * Range: [String](types/String.md)

### Mixed in from ontology class mixin:

 * [concept name](concept_name.md)  <sub>0..1</sub>
     * Description: The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.
     * Range: [String](types/String.md)

### Mixed in from ontology class mixin:

 * [ontology class mixin➞description](ontology_class_mixin_description.md)  <sub>0..1</sub>
     * Description: The description or definition of an ontology class.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)

### Mixed in from ontology class mixin:

 * [ontology name](ontology_name.md)  <sub>0..1</sub>
     * Description: The name of the ontology from which this ontology class was chosen.
     * Range: [String](types/String.md)

### Mixed in from ontology class mixin:

 * [ontology version](ontology_version.md)  <sub>0..1</sub>
     * Description: The version of the ontology from which this ontology class was chosen.
     * Range: [String](types/String.md)

### Mixed in from ontology class mixin:

 * [ontology class mixin➞name](ontology_class_mixin_name.md)  <sub>0..1</sub>
     * Description: The name or label (rdfs:label) of an ontology class.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | DUO:0000017 |

