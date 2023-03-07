
# Class: person


A member of the species Homo sapiens.

URI: [GHGA:Person](https://w3id.org/GHGA/Person)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[User],[Person&#124;given_name:string%20%3F;family_name:string%20%3F;additional_name:string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F]^-[User],[Person]^-[Member],[Person]^-[Individual],[NamedThing]^-[Person],[NamedThing],[Member],[Individual])](https://yuml.me/diagram/nofunky;dir:TB/class/[User],[Person&#124;given_name:string%20%3F;family_name:string%20%3F;additional_name:string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F]^-[User],[Person]^-[Member],[Person]^-[Individual],[NamedThing]^-[Person],[NamedThing],[Member],[Individual])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A databased entity, concept or class. This is a generic class that is the root of all the other classes.

## Children

 * [Individual](Individual.md) - An Individual is a Person who is participating in a Study.
 * [Member](Member.md) - Member of an Organization or a Committee.
 * [User](User.md) - A user in GHGA.

## Referenced by Class


## Attributes


### Own

 * [given name](given_name.md)  <sub>0..1</sub>
     * Description: First name.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [family name](family_name.md)  <sub>0..1</sub>
     * Description: Last name.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [additional name](additional_name.md)  <sub>0..1</sub>
     * Description: Additional name(s).
     * Range: [String](types/String.md)
     * in subsets: (restricted)

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | NCIT:C25190 |
|  | | SIO:000498 |
|  | | prov:Person |

