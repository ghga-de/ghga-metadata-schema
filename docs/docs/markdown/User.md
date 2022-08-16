
# Class: user


A user in GHGA.

URI: [GHGA:User](https://w3id.org/GHGA/User)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Person]^-[User&#124;email:string%20%3F;role:user_role_enum%20%3F;given_name(i):string%20%3F;family_name(i):string%20%3F;additional_name(i):string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Person])](https://yuml.me/diagram/nofunky;dir:TB/class/[Person]^-[User&#124;email:string%20%3F;role:user_role_enum%20%3F;given_name(i):string%20%3F;family_name(i):string%20%3F;additional_name(i):string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Person])

## Parents

 *  is_a: [Person](Person.md) - A member of the species Homo sapiens.

## Referenced by Class


## Attributes


### Own

 * [email](email.md)  <sub>0..1</sub>
     * Description: Email of a person.
     * Range: [String](types/String.md)
 * [user➞role](user_role.md)  <sub>0..1</sub>
     * Description: The role of the user
     * Range: [user role enum](user role enum.md)

### Inherited from person:

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
