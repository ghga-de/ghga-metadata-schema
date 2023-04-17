
# Class: DataAccessPolicy


A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/DataAccessPolicy](https://w3id.org/GHGA-Submission-Metadata-Schema/DataAccessPolicy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[InformationContentEntity],[EgaAccessionMixin],[Dataset],[DataUsePermission],[DataUseModifier],[DataUseModifier]<data_use_modifiers%200..1-++[DataAccessPolicy&#124;name:string;description:string;policy_text:string;policy_url:string%20%3F;data_request_form:string%20%3F;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[DataUsePermission]<data_use_permission%201..1-++[DataAccessPolicy],[DataAccessCommittee]<data_access_committee%201..1-++[DataAccessPolicy],[Dataset]++-%20data_access_policy%201..1>[DataAccessPolicy],[Submission]++-%20data_access_policies%201..*>[DataAccessPolicy],[Submission]-%20data_access_policies(i)%200..*>[DataAccessPolicy],[Dataset]-%20data_access_policy(i)%200..1>[DataAccessPolicy],[DataAccessPolicy]uses%20-.->[AttributeMixin],[DataAccessPolicy]uses%20-.->[AccessionMixin],[DataAccessPolicy]uses%20-.->[EgaAccessionMixin],[InformationContentEntity]^-[DataAccessPolicy],[DataAccessCommittee],[AttributeMixin],[Attribute],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[InformationContentEntity],[EgaAccessionMixin],[Dataset],[DataUsePermission],[DataUseModifier],[DataUseModifier]<data_use_modifiers%200..1-++[DataAccessPolicy&#124;name:string;description:string;policy_text:string;policy_url:string%20%3F;data_request_form:string%20%3F;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[DataUsePermission]<data_use_permission%201..1-++[DataAccessPolicy],[DataAccessCommittee]<data_access_committee%201..1-++[DataAccessPolicy],[Dataset]++-%20data_access_policy%201..1>[DataAccessPolicy],[Submission]++-%20data_access_policies%201..*>[DataAccessPolicy],[Submission]-%20data_access_policies(i)%200..*>[DataAccessPolicy],[Dataset]-%20data_access_policy(i)%200..1>[DataAccessPolicy],[DataAccessPolicy]uses%20-.->[AttributeMixin],[DataAccessPolicy]uses%20-.->[AccessionMixin],[DataAccessPolicy]uses%20-.->[EgaAccessionMixin],[InformationContentEntity]^-[DataAccessPolicy],[DataAccessCommittee],[AttributeMixin],[Attribute],[AccessionMixin])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Uses Mixin

 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.
 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an ega_accession, in addition to GHGA accession.

## Referenced by Class

 *  **[Dataset](Dataset.md)** *[Dataset➞data_access_policy](Dataset_data_access_policy.md)*  <sub>1..1</sub>  **[DataAccessPolicy](DataAccessPolicy.md)**
 *  **[Submission](Submission.md)** *[Submission➞data_access_policies](Submission_data_access_policies.md)*  <sub>1..\*</sub>  **[DataAccessPolicy](DataAccessPolicy.md)**
 *  **None** *[data_access_policies](data_access_policies.md)*  <sub>0..\*</sub>  **[DataAccessPolicy](DataAccessPolicy.md)**
 *  **None** *[data_access_policy](data_access_policy.md)*  <sub>0..1</sub>  **[DataAccessPolicy](DataAccessPolicy.md)**

## Attributes


### Own

 * [DataAccessPolicy➞name](DataAccessPolicy_name.md)  <sub>1..1</sub>
     * Description: A name for the Data Access Policy.
     * Range: [String](types/String.md)
 * [DataAccessPolicy➞description](DataAccessPolicy_description.md)  <sub>1..1</sub>
     * Description: A short description for the Data Access Policy.
     * Range: [String](types/String.md)
 * [DataAccessPolicy➞policy_text](DataAccessPolicy_policy_text.md)  <sub>1..1</sub>
     * Description: The terms of data use and policy verbiage should be captured here.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [DataAccessPolicy➞policy_url](DataAccessPolicy_policy_url.md)  <sub>0..1</sub>
     * Description: URL for the policy, if available. This is useful if the terms of the policy is made available online at a resolvable URL.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [DataAccessPolicy➞data_access_committee](DataAccessPolicy_data_access_committee.md)  <sub>1..1</sub>
     * Description: The Data Access Committee linked to this policy.
     * Range: [DataAccessCommittee](DataAccessCommittee.md)
     * in subsets: (restricted)
 * [DataAccessPolicy➞data_use_permission](DataAccessPolicy_data_use_permission.md)  <sub>1..1</sub>
     * Description: Data use permission associated with a policy. Typically one or more terms from DUO and should be descendants of 'DUO:0000001 data use permission'.
     * Range: [DataUsePermission](DataUsePermission.md)
     * in subsets: (restricted)
 * [DataAccessPolicy➞data_use_modifiers](DataAccessPolicy_data_use_modifiers.md)  <sub>0..1</sub>
     * Description: Modifier for Data use permission associated with a policy. Should be descendants of 'DUO:0000017 data use modifier'
     * Range: [DataUseModifier](DataUseModifier.md)
     * in subsets: (restricted)
 * [DataAccessPolicy➞data_request_form](DataAccessPolicy_data_request_form.md)  <sub>0..1</sub>
     * Description: Data Request Form that is associated with this Data Access Policy.
     * Range: [String](types/String.md)

### Inherited from InformationContentEntity:

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
