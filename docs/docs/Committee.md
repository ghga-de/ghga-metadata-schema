
# Class: committee


A group of people organized for a specific purpose.

URI: [GHGA:Committee](https://w3id.org/GHGA/Committee)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DataAccessCommittee],[Committee&#124;name:string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F]^-[DataAccessCommittee],[NamedThing]^-[Committee])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DataAccessCommittee],[Committee&#124;name:string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F]^-[DataAccessCommittee],[NamedThing]^-[Committee])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A databased entity, concept or class. This is a generic class that is the root of all the other classes.

## Children

 * [DataAccessCommittee](DataAccessCommittee.md) - A group of members that are delegated to grant access to one or more datasets after ensuring the minimum criteria for data sharing has been met, and request for data use does not raise ethical and/or legal concerns.

## Referenced by Class


## Attributes


### Own

 * [name](name.md)  <sub>0..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)

### Inherited from named thing:

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
