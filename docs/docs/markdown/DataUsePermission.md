
# Class: data use permission


A data item that is used to indicate consent permissions for datasets and/or materials and relates to the purposes for which datasets and/or material might be removed, stored or used.

URI: [GHGA:DataUsePermission](https://w3id.org/GHGA/DataUsePermission)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClassMixin],[InformationContentEntity],[DataUseCondition]++-%20has%20data%20use%20permission%201..1>[DataUsePermission&#124;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F;id(i):string;alias(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[DataUseCondition]++-%20has%20data%20use%20permission(i)%200..1>[DataUsePermission],[DataUsePermission]uses%20-.->[OntologyClassMixin],[InformationContentEntity]^-[DataUsePermission],[DataUseCondition])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClassMixin],[InformationContentEntity],[DataUseCondition]++-%20has%20data%20use%20permission%201..1>[DataUsePermission&#124;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F;id(i):string;alias(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[DataUseCondition]++-%20has%20data%20use%20permission(i)%200..1>[DataUsePermission],[DataUsePermission]uses%20-.->[OntologyClassMixin],[InformationContentEntity]^-[DataUsePermission],[DataUseCondition])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Uses Mixin

 *  mixin: [OntologyClassMixin](OntologyClassMixin.md) - Mixin for entities that represent an class/term/concept from an ontology.

## Referenced by Class

 *  **[DataUseCondition](DataUseCondition.md)** *[data use condition➞has data use permission](data_use_condition_has_data_use_permission.md)*  <sub>1..1</sub>  **[DataUsePermission](DataUsePermission.md)**
 *  **None** *[has data use permission](has_data_use_permission.md)*  <sub>0..1</sub>  **[DataUsePermission](DataUsePermission.md)**

## Attributes


### Inherited from information content entity:

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

### Mixed in from ontology class mixin:

 * [ontology class mixin➞concept identifier](ontology_class_mixin_concept_identifier.md)  <sub>0..1</sub>
     * Description: The Compact URI (CURIE) that uniquely identifies this ontology class.
     * Range: [String](types/String.md)

### Mixed in from ontology class mixin:

 * [ontology class mixin➞concept name](ontology_class_mixin_concept_name.md)  <sub>0..1</sub>
     * Description: The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.
     * Range: [String](types/String.md)

### Mixed in from ontology class mixin:

 * [ontology class mixin➞description](ontology_class_mixin_description.md)  <sub>0..1</sub>
     * Description: The description or definition of an ontology class.
     * Range: [String](types/String.md)

### Mixed in from ontology class mixin:

 * [ontology class mixin➞ontology name](ontology_class_mixin_ontology_name.md)  <sub>0..1</sub>
     * Description: The name or label (rdfs:label) of an ontology class.
     * Range: [String](types/String.md)

### Mixed in from ontology class mixin:

 * [ontology class mixin➞ontology version](ontology_class_mixin_ontology_version.md)  <sub>0..1</sub>
     * Description: The version of the ontology from which this ontology class was chosen.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | DUO:0000001 |

