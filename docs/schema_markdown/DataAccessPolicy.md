
# Class: data access policy


A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/DataAccessPolicy](https://w3id.org/GHGA-Submission-Metadata-Schema/DataAccessPolicy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[InformationContentEntity],[EgaAccessionMixin],[Dataset],[DataUsePermission],[DataUseModifier],[DataUseModifier]<has%20data%20use%20modifier%200..*-++[DataAccessPolicy&#124;name:string;description:string;policy_text:string;policy_url:string%20%3F;data_request_form:string%20%3F;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[DataUsePermission]<has%20data%20use%20permission%201..1-++[DataAccessPolicy],[DataAccessCommittee]<has%20data%20access%20committee%201..1-++[DataAccessPolicy],[Dataset]++-%20has%20data%20access%20policy%201..1>[DataAccessPolicy],[Dataset]-%20has%20data%20access%20policy(i)%200..1>[DataAccessPolicy],[Submission]-%20has%20data%20access%20policy(i)%200..1>[DataAccessPolicy],[Submission]++-%20has%20data%20access%20policy%201..*>[DataAccessPolicy],[DataAccessPolicy]uses%20-.->[AttributeMixin],[DataAccessPolicy]uses%20-.->[AccessionMixin],[DataAccessPolicy]uses%20-.->[EgaAccessionMixin],[InformationContentEntity]^-[DataAccessPolicy],[DataAccessCommittee],[AttributeMixin],[Attribute],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[InformationContentEntity],[EgaAccessionMixin],[Dataset],[DataUsePermission],[DataUseModifier],[DataUseModifier]<has%20data%20use%20modifier%200..*-++[DataAccessPolicy&#124;name:string;description:string;policy_text:string;policy_url:string%20%3F;data_request_form:string%20%3F;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[DataUsePermission]<has%20data%20use%20permission%201..1-++[DataAccessPolicy],[DataAccessCommittee]<has%20data%20access%20committee%201..1-++[DataAccessPolicy],[Dataset]++-%20has%20data%20access%20policy%201..1>[DataAccessPolicy],[Dataset]-%20has%20data%20access%20policy(i)%200..1>[DataAccessPolicy],[Submission]-%20has%20data%20access%20policy(i)%200..1>[DataAccessPolicy],[Submission]++-%20has%20data%20access%20policy%201..*>[DataAccessPolicy],[DataAccessPolicy]uses%20-.->[AttributeMixin],[DataAccessPolicy]uses%20-.->[AccessionMixin],[DataAccessPolicy]uses%20-.->[EgaAccessionMixin],[InformationContentEntity]^-[DataAccessPolicy],[DataAccessCommittee],[AttributeMixin],[Attribute],[AccessionMixin])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Uses Mixin

 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.
 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an EGA accession, in addition to GHGA accession.

## Referenced by Class

 *  **[Dataset](Dataset.md)** *[dataset➞has data access policy](dataset_has_data_access_policy.md)*  <sub>1..1</sub>  **[DataAccessPolicy](DataAccessPolicy.md)**
 *  **None** *[has data access policy](has_data_access_policy.md)*  <sub>0..1</sub>  **[DataAccessPolicy](DataAccessPolicy.md)**
 *  **[Submission](Submission.md)** *[submission➞has data access policy](submission_has_data_access_policy.md)*  <sub>1..\*</sub>  **[DataAccessPolicy](DataAccessPolicy.md)**

## Attributes


### Own

 * [data access policy➞name](data_access_policy_name.md)  <sub>1..1</sub>
     * Description: A name for the Data Access Policy.
     * Range: [String](types/String.md)
 * [data access policy➞description](data_access_policy_description.md)  <sub>1..1</sub>
     * Description: A short description for the Data Access Policy.
     * Range: [String](types/String.md)
 * [data access policy➞policy text](data_access_policy_policy_text.md)  <sub>1..1</sub>
     * Description: The terms of data use and policy verbiage should be captured here.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [data access policy➞policy url](data_access_policy_policy_url.md)  <sub>0..1</sub>
     * Description: URL for the policy, if available. This is useful if the terms of the policy is made available online at a resolvable URL.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [data access policy➞has data access committee](data_access_policy_has_data_access_committee.md)  <sub>1..1</sub>
     * Description: The Data Access Committee linked to this policy.
     * Range: [DataAccessCommittee](DataAccessCommittee.md)
     * in subsets: (restricted)
 * [data access policy➞has data use permission](data_access_policy_has_data_use_permission.md)  <sub>1..1</sub>
     * Description: Data use permission associated with a policy. Typically one or more terms from DUO and should be descendants of 'DUO:0000001 data use permission'.
     * Range: [DataUsePermission](DataUsePermission.md)
     * in subsets: (restricted)
 * [data access policy➞has data use modifier](data_access_policy_has_data_use_modifier.md)  <sub>0..\*</sub>
     * Description: Modifier for Data use permission associated with a policy. Should be descendants of 'DUO:0000017 data use modifier'
     * Range: [DataUseModifier](DataUseModifier.md)
     * in subsets: (restricted)
 * [data access policy➞data request form](data_access_policy_data_request_form.md)  <sub>0..1</sub>
     * Description: Data Request Form that is associated with this Data Access Policy.
     * Range: [String](types/String.md)

### Inherited from information content entity:

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

### Mixed in from attribute mixin:

 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

### Mixed in from accession mixin:

 * [accession mixin➞accession](accession_mixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

### Mixed in from ega accession mixin:

 * [ega accession mixin➞ega accession](ega_accession_mixin_ega_accession.md)  <sub>1..1</sub>
     * Description: A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
     * Range: [String](types/String.md)
