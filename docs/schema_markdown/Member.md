
# Class: Member


Member of an Organization or a Committee.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Member](https://w3id.org/GHGA-Submission-Metadata-Schema/Member)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Person],[DataAccessCommittee]++-%20has_member%200..*>[Member&#124;email:string;telephone:string%20%3F;organization:string;given_name(i):string%20%3F;family_name(i):string%20%3F;additional_name(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[DataAccessCommittee]++-%20main_contact%201..1>[Member],[Submission]++-%20has_member%201..*>[Member],[DataAccessCommittee]++-%20has_member(i)%200..1>[Member],[Submission]++-%20has_member(i)%200..1>[Member],[DataAccessCommittee]-%20main_contact(i)%200..1>[Member],[Person]^-[Member],[DataAccessCommittee])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Person],[DataAccessCommittee]++-%20has_member%200..*>[Member&#124;email:string;telephone:string%20%3F;organization:string;given_name(i):string%20%3F;family_name(i):string%20%3F;additional_name(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[DataAccessCommittee]++-%20main_contact%201..1>[Member],[Submission]++-%20has_member%201..*>[Member],[DataAccessCommittee]++-%20has_member(i)%200..1>[Member],[Submission]++-%20has_member(i)%200..1>[Member],[DataAccessCommittee]-%20main_contact(i)%200..1>[Member],[Person]^-[Member],[DataAccessCommittee])

## Parents

 *  is_a: [Person](Person.md) - A member of the species Homo sapiens.

## Referenced by Class

 *  **[DataAccessCommittee](DataAccessCommittee.md)** *[DataAccessCommittee➞has_member](DataAccessCommittee_has_member.md)*  <sub>0..\*</sub>  **[Member](Member.md)**
 *  **[DataAccessCommittee](DataAccessCommittee.md)** *[DataAccessCommittee➞main_contact](DataAccessCommittee_main_contact.md)*  <sub>1..1</sub>  **[Member](Member.md)**
 *  **[Submission](Submission.md)** *[Submission➞has_member](Submission_has_member.md)*  <sub>1..\*</sub>  **[Member](Member.md)**
 *  **None** *[has_member](has_member.md)*  <sub>0..1</sub>  **[Member](Member.md)**
 *  **None** *[main_contact](main_contact.md)*  <sub>0..1</sub>  **[Member](Member.md)**

## Attributes


### Own

 * [Member➞email](Member_email.md)  <sub>1..1</sub>
     * Description: The email of the Member.
     * Range: [String](types/String.md)
 * [Member➞telephone](Member_telephone.md)  <sub>0..1</sub>
     * Description: The telephone number of the Member.
     * Range: [String](types/String.md)
 * [Member➞organization](Member_organization.md)  <sub>1..1</sub>
     * Description: The organization that the Member is part of.
     * Range: [String](types/String.md)

### Inherited from Person:

 * [NamedThing➞id](NamedThing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [NamedThing➞alias](NamedThing_alias.md)  <sub>1..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [NamedThing➞xref](NamedThing_xref.md)  <sub>0..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)
 * [Person➞given_name](Person_given_name.md)  <sub>0..1</sub>
     * Description: First name.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [Person➞family_name](Person_family_name.md)  <sub>0..1</sub>
     * Description: Last name.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [Person➞additional_name](Person_additional_name.md)  <sub>0..1</sub>
     * Description: additional_name(s).
     * Range: [String](types/String.md)
     * in subsets: (restricted)
