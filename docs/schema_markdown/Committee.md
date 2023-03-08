
# Class: committee


A group of people organized for a specific purpose.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Committee](https://w3id.org/GHGA-Submission-Metadata-Schema/Committee)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DataAccessCommittee],[Committee&#124;name:string;id(i):string;alias(i):string;xref(i):string%20*]^-[DataAccessCommittee],[NamedThing]^-[Committee])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[DataAccessCommittee],[Committee&#124;name:string;id(i):string;alias(i):string;xref(i):string%20*]^-[DataAccessCommittee],[NamedThing]^-[Committee])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A database entity, concept or class. This is a generic class that is the root of all the other classes.

## Children

 * [DataAccessCommittee](DataAccessCommittee.md) - A group of members that are delegated to grant access to one or more datasets after ensuring the minimum criteria for data sharing has been met, and request for data use does not raise ethical and/or legal concerns.

## Referenced by Class


## Attributes


### Own

 * [committee➞name](committee_name.md)  <sub>1..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)

### Inherited from named thing:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞alias](named_thing_alias.md)  <sub>1..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞xref](named_thing_xref.md)  <sub>0..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)
