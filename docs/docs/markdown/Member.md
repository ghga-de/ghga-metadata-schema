
# Class: member


Member of an Organization or a Committee.

URI: [GHGA:Member](https://w3id.org/GHGA/Member)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Person],[DataAccessCommittee]++-%20has%20member%200..*>[Member&#124;email:string;telephone:string%20%3F;organization:string;given_name(i):string%20%3F;family_name(i):string%20%3F;additional_name(i):string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[DataAccessCommittee]++-%20main%20contact%200..1>[Member],[DataAccessCommittee]-%20main%20contact(i)%200..1>[Member],[Person]^-[Member],[DataAccessCommittee])](https://yuml.me/diagram/nofunky;dir:TB/class/[Person],[DataAccessCommittee]++-%20has%20member%200..*>[Member&#124;email:string;telephone:string%20%3F;organization:string;given_name(i):string%20%3F;family_name(i):string%20%3F;additional_name(i):string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[DataAccessCommittee]++-%20main%20contact%200..1>[Member],[DataAccessCommittee]-%20main%20contact(i)%200..1>[Member],[Person]^-[Member],[DataAccessCommittee])

## Parents

 *  is_a: [Person](Person.md) - A member of the species Homo sapiens.

## Referenced by Class

 *  **[DataAccessCommittee](DataAccessCommittee.md)** *[data access committee➞has member](data_access_committee_has_member.md)*  <sub>0..\*</sub>  **[Member](Member.md)**
 *  **[DataAccessCommittee](DataAccessCommittee.md)** *[data access committee➞main contact](data_access_committee_main_contact.md)*  <sub>0..1</sub>  **[Member](Member.md)**
 *  **None** *[main contact](main_contact.md)*  <sub>0..1</sub>  **[Member](Member.md)**

## Attributes


### Own

 * [member➞email](member_email.md)  <sub>1..1</sub>
     * Description: The email of the Member.
     * Range: [String](types/String.md)
 * [member➞telephone](member_telephone.md)  <sub>0..1</sub>
     * Description: The telephone number of the Member.
     * Range: [String](types/String.md)
 * [member➞organization](member_organization.md)  <sub>1..1</sub>
     * Description: The organization that the Member is part of.
     * Range: [String](types/String.md)

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
