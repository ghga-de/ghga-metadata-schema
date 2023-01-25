
# Class: ~~technology~~ _(deprecated)_


A Technology is an abstraction that represents the instrument used for an assay. The Technology entity captures instrument-specific attributes that are relevant for an Experiment entity. The Technology entity may be further characterized by its children where each child has fields that are relevant to that particular technology.

URI: [GHGA:Technology](https://w3id.org/GHGA/Technology)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[InformationContentEntity]^-[Technology&#124;id(i):string;alias(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[InformationContentEntity])](https://yuml.me/diagram/nofunky;dir:TB/class/[InformationContentEntity]^-[Technology&#124;id(i):string;alias(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[InformationContentEntity])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Referenced by Class

 *  **None** *[has technology](has_technology.md)*  <sub>0..1</sub>  **[Technology](Technology.md)**

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
