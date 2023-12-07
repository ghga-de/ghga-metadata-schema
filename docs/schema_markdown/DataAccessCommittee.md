
# Class: DataAccessCommittee


A group of members that are delegated to grant access to one or more datasets after ensuring the criteria for data sharing has been met,  and request for data use does not raise ethical and/or legal concerns.

URI: [GHGA:DataAccessCommittee](https://w3id.org/GHGA/DataAccessCommittee)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[IdentifiedByAliasMixin],[DataAccessPolicy],[DataAccessPolicy]-%20data_access_committee%201..1>[DataAccessCommittee&#124;email:string;institute:string;alias:string],[Submission]++-%20data_access_committees%201..*>[DataAccessCommittee],[DataAccessPolicy]-%20data_access_committee(i)%200..1>[DataAccessCommittee],[Submission]-%20data_access_committees(i)%200..*>[DataAccessCommittee],[DataAccessCommittee]uses%20-.->[IdentifiedByAliasMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[IdentifiedByAliasMixin],[DataAccessPolicy],[DataAccessPolicy]-%20data_access_committee%201..1>[DataAccessCommittee&#124;email:string;institute:string;alias:string],[Submission]++-%20data_access_committees%201..*>[DataAccessCommittee],[DataAccessPolicy]-%20data_access_committee(i)%200..1>[DataAccessCommittee],[Submission]-%20data_access_committees(i)%200..*>[DataAccessCommittee],[DataAccessCommittee]uses%20-.->[IdentifiedByAliasMixin])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

 *  **[DataAccessPolicy](DataAccessPolicy.md)** *[DataAccessPolicy➞data_access_committee](DataAccessPolicy_data_access_committee.md)*  <sub>1..1</sub>  **[DataAccessCommittee](DataAccessCommittee.md)**
 *  **[Submission](Submission.md)** *[Submission➞data_access_committees](Submission_data_access_committees.md)*  <sub>1..\*</sub>  **[DataAccessCommittee](DataAccessCommittee.md)**
 *  **None** *[data_access_committee](data_access_committee.md)*  <sub>0..1</sub>  **[DataAccessCommittee](DataAccessCommittee.md)**
 *  **None** *[data_access_committees](data_access_committees.md)*  <sub>0..\*</sub>  **[DataAccessCommittee](DataAccessCommittee.md)**

## Attributes


### Own

 * [DataAccessCommittee➞email](DataAccessCommittee_email.md)  <sub>1..1</sub>
     * Description: The email of the Data Access Committee (e.g., DAC[at]email.com). This property must not include any personally identifiable data.
     * Range: [String](types/String.md)
 * [DataAccessCommittee➞institute](DataAccessCommittee_institute.md)  <sub>1..1</sub>
     * Description: The Institute a person is affiliated with.
     * Range: [String](types/String.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
