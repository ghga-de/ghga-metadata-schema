
# Class: DataAccessCommittee


A group of members that are delegated to grant access to one or more datasets after ensuring the minimum criteria for data sharing has been met, and request for data use does not raise ethical and/or legal concerns.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/DataAccessCommittee](https://w3id.org/GHGA-Submission-Metadata-Schema/DataAccessCommittee)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Member],[EgaAccessionMixin],[DataAccessPolicy],[Member]<members%200..*-++[DataAccessCommittee&#124;name:string;description:string%20%3F;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Member]<main_contact%201..1-++[DataAccessCommittee],[DataAccessPolicy]++-%20data_access_committee%201..1>[DataAccessCommittee],[Submission]++-%20data_access_committees%201..*>[DataAccessCommittee],[DataAccessPolicy]-%20data_access_committee(i)%200..1>[DataAccessCommittee],[Submission]-%20data_access_committees(i)%200..*>[DataAccessCommittee],[DataAccessCommittee]uses%20-.->[AttributeMixin],[DataAccessCommittee]uses%20-.->[AccessionMixin],[DataAccessCommittee]uses%20-.->[EgaAccessionMixin],[Committee]^-[DataAccessCommittee],[Committee],[AttributeMixin],[Attribute],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Member],[EgaAccessionMixin],[DataAccessPolicy],[Member]<members%200..*-++[DataAccessCommittee&#124;name:string;description:string%20%3F;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[Member]<main_contact%201..1-++[DataAccessCommittee],[DataAccessPolicy]++-%20data_access_committee%201..1>[DataAccessCommittee],[Submission]++-%20data_access_committees%201..*>[DataAccessCommittee],[DataAccessPolicy]-%20data_access_committee(i)%200..1>[DataAccessCommittee],[Submission]-%20data_access_committees(i)%200..*>[DataAccessCommittee],[DataAccessCommittee]uses%20-.->[AttributeMixin],[DataAccessCommittee]uses%20-.->[AccessionMixin],[DataAccessCommittee]uses%20-.->[EgaAccessionMixin],[Committee]^-[DataAccessCommittee],[Committee],[AttributeMixin],[Attribute],[AccessionMixin])

## Parents

 *  is_a: [Committee](Committee.md) - A group of people organized for a specific purpose.

## Uses Mixin

 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.
 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an ega_accession, in addition to GHGA accession.

## Referenced by Class

 *  **[DataAccessPolicy](DataAccessPolicy.md)** *[DataAccessPolicy➞data_access_committee](DataAccessPolicy_data_access_committee.md)*  <sub>1..1</sub>  **[DataAccessCommittee](DataAccessCommittee.md)**
 *  **[Submission](Submission.md)** *[Submission➞data_access_committees](Submission_data_access_committees.md)*  <sub>1..\*</sub>  **[DataAccessCommittee](DataAccessCommittee.md)**
 *  **None** *[data_access_committee](data_access_committee.md)*  <sub>0..1</sub>  **[DataAccessCommittee](DataAccessCommittee.md)**
 *  **None** *[data_access_committees](data_access_committees.md)*  <sub>0..\*</sub>  **[DataAccessCommittee](DataAccessCommittee.md)**

## Attributes


### Own

 * [DataAccessCommittee➞name](DataAccessCommittee_name.md)  <sub>1..1</sub>
     * Description: The name for the Data Access Committee.
     * Range: [String](types/String.md)
 * [DataAccessCommittee➞description](DataAccessCommittee_description.md)  <sub>0..1</sub>
     * Description: A description for the Data Access Committee.
     * Range: [String](types/String.md)
 * [DataAccessCommittee➞main_contact](DataAccessCommittee_main_contact.md)  <sub>1..1</sub>
     * Description: The main contact for the Data Access Committee.
     * Range: [Member](Member.md)
     * in subsets: (restricted)
 * [DataAccessCommittee➞members](DataAccessCommittee_members.md)  <sub>0..\*</sub>
     * Description: All the members that are part of this Data Access Committee.
     * Range: [Member](Member.md)
     * in subsets: (restricted)

### Inherited from Committee:

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

### Mixed in from AttributeMixin:

 * [attributes](attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

### Mixed in from AccessionMixin:

 * [AccessionMixin➞accession](AccessionMixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

### Mixed in from EgaAccessionMixin:

 * [EgaAccessionMixin➞ega_accession](EgaAccessionMixin_ega_accession.md)  <sub>1..1</sub>
     * Description: A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
     * Range: [String](types/String.md)
