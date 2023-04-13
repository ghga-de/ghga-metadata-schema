
# Class: InformationContentEntity


A generically dependent continuant that is about some thing.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/InformationContentEntity](https://w3id.org/GHGA-Submission-Metadata-Schema/InformationContentEntity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Protocol],[NamedThing],[InformationContentEntity&#124;id(i):string;alias(i):string;xref(i):string%20*]^-[Publication],[InformationContentEntity]^-[Protocol],[InformationContentEntity]^-[File],[InformationContentEntity]^-[Dataset],[InformationContentEntity]^-[DataUsePermission],[InformationContentEntity]^-[DataUseModifier],[InformationContentEntity]^-[DataAccessPolicy],[NamedThing]^-[InformationContentEntity],[File],[Dataset],[DataUsePermission],[DataUseModifier],[DataAccessPolicy])](https://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Protocol],[NamedThing],[InformationContentEntity&#124;id(i):string;alias(i):string;xref(i):string%20*]^-[Publication],[InformationContentEntity]^-[Protocol],[InformationContentEntity]^-[File],[InformationContentEntity]^-[Dataset],[InformationContentEntity]^-[DataUsePermission],[InformationContentEntity]^-[DataUseModifier],[InformationContentEntity]^-[DataAccessPolicy],[NamedThing]^-[InformationContentEntity],[File],[Dataset],[DataUsePermission],[DataUseModifier],[DataAccessPolicy])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A database entity, concept or class. This is a generic class that is the root of all the other classes.

## Children

 * [DataAccessPolicy](DataAccessPolicy.md) - A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.
 * [DataUseModifier](DataUseModifier.md) - Data use modifiers indicate additional conditions for use.
 * [DataUsePermission](DataUsePermission.md) - A data item that is used to indicate consent permissions for datasets and/or materials and relates to the purposes for which datasets and/or material might be removed, stored or used.
 * [Dataset](Dataset.md) - A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
 * [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.
 * [Protocol](Protocol.md) - A plan specification which has sufficient level of detail and quantitative information to communicate it between Investigation agents, so that different Investigation agents will reliably be able to independently reproduce the process.
 * [Publication](Publication.md) - The Publication entity represents a publication. While a publication can be any article that is published, the minimum expectation is that the publication has a valid DOI.

## Referenced by Class


## Attributes


### Inherited from NamedThing:

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | IAO:0000030 |

