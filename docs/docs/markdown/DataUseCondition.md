
# Class: data use condition


Data Use Condition represents the use conditions associated with a policy.

URI: [GHGA:DataUseCondition](https://w3id.org/GHGA/DataUseCondition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[InformationContentEntity],[DataUsePermission],[DataUseModifier],[DataUseModifier]<has%20data%20use%20modifier%200..1-++[DataUseCondition&#124;id(i):string;alias(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[DataUsePermission]<has%20data%20use%20permission%201..1-++[DataUseCondition],[DataAccessPolicy]++-%20has%20data%20use%20condition%200..*>[DataUseCondition],[DataAccessPolicy]-%20has%20data%20use%20condition(i)%200..1>[DataUseCondition],[InformationContentEntity]^-[DataUseCondition],[DataAccessPolicy])](https://yuml.me/diagram/nofunky;dir:TB/class/[InformationContentEntity],[DataUsePermission],[DataUseModifier],[DataUseModifier]<has%20data%20use%20modifier%200..1-++[DataUseCondition&#124;id(i):string;alias(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[DataUsePermission]<has%20data%20use%20permission%201..1-++[DataUseCondition],[DataAccessPolicy]++-%20has%20data%20use%20condition%200..*>[DataUseCondition],[DataAccessPolicy]-%20has%20data%20use%20condition(i)%200..1>[DataUseCondition],[InformationContentEntity]^-[DataUseCondition],[DataAccessPolicy])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Referenced by Class

 *  **[DataAccessPolicy](DataAccessPolicy.md)** *[data access policy➞has data use condition](data_access_policy_has_data_use_condition.md)*  <sub>0..\*</sub>  **[DataUseCondition](DataUseCondition.md)**
 *  **None** *[has data use condition](has_data_use_condition.md)*  <sub>0..1</sub>  **[DataUseCondition](DataUseCondition.md)**

## Attributes


### Own

 * [data use condition➞has data use permission](data_use_condition_has_data_use_permission.md)  <sub>1..1</sub>
     * Description: Data use permission associated with a policy. Typically one or more terms from DUO and should be descendants of 'DUO:0000001 data use permission'.
     * Range: [DataUsePermission](DataUsePermission.md)
     * in subsets: (restricted)
 * [data use condition➞has data use modifier](data_use_condition_has_data_use_modifier.md)  <sub>0..1</sub>
     * Description: Modifier for Data use permission associated with a policy. Should be descendants of 'DUO:0000017 data use modifier'
     * Range: [DataUseModifier](DataUseModifier.md)
     * in subsets: (restricted)

### Inherited from information content entity:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞alias](named_thing_alias.md)  <sub>1..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞xref](named_thing_xref.md)  <sub>1..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)
 * [named thing➞creation date](named_thing_creation_date.md)  <sub>1..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was created.
     * Range: [String](types/String.md)
 * [named thing➞update date](named_thing_update_date.md)  <sub>1..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was updated.
     * Range: [String](types/String.md)
