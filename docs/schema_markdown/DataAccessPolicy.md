
# Class: DataAccessPolicy


A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.

URI: [GHGA:DataAccessPolicy](https://w3id.org/GHGA/DataAccessPolicy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[IdentifiedByAliasMixin],[Dataset],[DataAccessCommittee]<data_access_committee%201..1-%20[DataAccessPolicy&#124;name:string;description:string;policy_text:string;policy_url:string%20%3F;data_use_permission_term:DataUsePermissionEnum;data_use_permission_id:string;data_use_modifier_terms:DataUseModifierEnum%20*;data_use_modifier_ids:string%20*;ega_accession:string%20%3F;alias:string],[Dataset]-%20data_access_policy%201..1>[DataAccessPolicy],[Submission]++-%20data_access_policies%201..*>[DataAccessPolicy],[Submission]-%20data_access_policies(i)%200..*>[DataAccessPolicy],[Dataset]-%20data_access_policy(i)%200..1>[DataAccessPolicy],[DataAccessPolicy]uses%20-.->[IdentifiedByAliasMixin],[DataAccessCommittee])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[IdentifiedByAliasMixin],[Dataset],[DataAccessCommittee]<data_access_committee%201..1-%20[DataAccessPolicy&#124;name:string;description:string;policy_text:string;policy_url:string%20%3F;data_use_permission_term:DataUsePermissionEnum;data_use_permission_id:string;data_use_modifier_terms:DataUseModifierEnum%20*;data_use_modifier_ids:string%20*;ega_accession:string%20%3F;alias:string],[Dataset]-%20data_access_policy%201..1>[DataAccessPolicy],[Submission]++-%20data_access_policies%201..*>[DataAccessPolicy],[Submission]-%20data_access_policies(i)%200..*>[DataAccessPolicy],[Dataset]-%20data_access_policy(i)%200..1>[DataAccessPolicy],[DataAccessPolicy]uses%20-.->[IdentifiedByAliasMixin],[DataAccessCommittee])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

 *  **[Dataset](Dataset.md)** *[Dataset➞data_access_policy](Dataset_data_access_policy.md)*  <sub>1..1</sub>  **[DataAccessPolicy](DataAccessPolicy.md)**
 *  **[Submission](Submission.md)** *[Submission➞data_access_policies](Submission_data_access_policies.md)*  <sub>1..\*</sub>  **[DataAccessPolicy](DataAccessPolicy.md)**
 *  **None** *[data_access_policies](data_access_policies.md)*  <sub>0..\*</sub>  **[DataAccessPolicy](DataAccessPolicy.md)**
 *  **None** *[data_access_policy](data_access_policy.md)*  <sub>0..1</sub>  **[DataAccessPolicy](DataAccessPolicy.md)**

## Attributes


### Own

 * [DataAccessPolicy➞name](DataAccessPolicy_name.md)  <sub>1..1</sub>
     * Description: A name for this Data Access Policy.
     * Range: [String](types/String.md)
 * [DataAccessPolicy➞description](DataAccessPolicy_description.md)  <sub>1..1</sub>
     * Description: A short description for this Data Access Policy.
     * Range: [String](types/String.md)
 * [DataAccessPolicy➞policy_text](DataAccessPolicy_policy_text.md)  <sub>1..1</sub>
     * Description: The complete text for the Data Access Policy.
     * Range: [String](types/String.md)
 * [DataAccessPolicy➞policy_url](DataAccessPolicy_policy_url.md)  <sub>0..1</sub>
     * Description: An alternative to the Data Access Policy text is to provide the URL for the policy. This is useful if the terms of the policy are available online at a resolvable URL.
     * Range: [String](types/String.md)
 * [DataAccessPolicy➞data_use_permission_term](DataAccessPolicy_data_use_permission_term.md)  <sub>1..1</sub>
     * Description: The Data Use Permission associated with this Data Use Policy. The used term should be a descendant of 'DUO:0000001: data use permission' (e.g., no restriction).
     * Range: [DataUsePermissionEnum](DataUsePermissionEnum.md)
 * [DataAccessPolicy➞data_use_permission_id](DataAccessPolicy_data_use_permission_id.md)  <sub>1..1</sub>
     * Description: The DUO ID corresponding to the Data Use Permission term (e.g., DUO:0000004).
     * Range: [String](types/String.md)
 * [DataAccessPolicy➞data_use_modifier_terms](DataAccessPolicy_data_use_modifier_terms.md)  <sub>0..\*</sub>
     * Description: One or more Data Use Modifiers for the Data Use Permission associated with this Data Use Policy. The used terms should be descendants of 'DUO:0000017: data use modifier' (e.g., clinical care use). Please use 'USER_SPECIFIC_RESTRICTION' if no other modifier applies.
     * Range: [DataUseModifierEnum](DataUseModifierEnum.md)
 * [DataAccessPolicy➞data_use_modifier_ids](DataAccessPolicy_data_use_modifier_ids.md)  <sub>0..\*</sub>
     * Description: The DUO IDs corresponding to the Data Use Modifier terms (e.g., DUO:0000043).
     * Range: [String](types/String.md)
 * [DataAccessPolicy➞ega_accession](DataAccessPolicy_ega_accession.md)  <sub>0..1</sub>
     * Description: The EGA accession ID of an entity.
     * Range: [String](types/String.md)
 * [DataAccessPolicy➞data_access_committee](DataAccessPolicy_data_access_committee.md)  <sub>1..1</sub>
     * Description: The Data Access Committee linked to this Data Use Policy.
     * Range: [DataAccessCommittee](DataAccessCommittee.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
