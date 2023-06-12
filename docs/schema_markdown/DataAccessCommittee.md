
# Class: DataAccessCommittee


A group of members that are delegated to grant access to one or more datasets after ensuring the minimum criteria for data sharing has been met, and request for data use does not raise ethical and/or legal concerns.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/DataAccessCommittee](https://w3id.org/GHGA-Submission-Metadata-Schema/DataAccessCommittee)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[IdentifiedByAliasMixin],[DataAccessPolicy],[DataAccessPolicy]-%20data_access_committee%201..1>[DataAccessCommittee&#124;name:string;description:string%20%3F;alias:string],[Submission]++-%20data_access_committees%201..*>[DataAccessCommittee],[DataAccessPolicy]-%20data_access_committee(i)%200..1>[DataAccessCommittee],[Submission]-%20data_access_committees(i)%200..*>[DataAccessCommittee],[DataAccessCommittee]uses%20-.->[AttributeMixin],[DataAccessCommittee]uses%20-.->[IdentifiedByAliasMixin],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[IdentifiedByAliasMixin],[DataAccessPolicy],[DataAccessPolicy]-%20data_access_committee%201..1>[DataAccessCommittee&#124;name:string;description:string%20%3F;alias:string],[Submission]++-%20data_access_committees%201..*>[DataAccessCommittee],[DataAccessPolicy]-%20data_access_committee(i)%200..1>[DataAccessCommittee],[Submission]-%20data_access_committees(i)%200..*>[DataAccessCommittee],[DataAccessCommittee]uses%20-.->[AttributeMixin],[DataAccessCommittee]uses%20-.->[IdentifiedByAliasMixin],[AttributeMixin],[Attribute])

## Uses Mixin

 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.
 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

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

### Mixed in from AttributeMixin:

 * [AttributeMixin➞attributes](AttributeMixin_attributes.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
