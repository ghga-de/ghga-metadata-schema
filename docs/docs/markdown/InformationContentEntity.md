
# Class: information content entity


A generically dependent continuant that is about some thing.

URI: [GHGA:InformationContentEntity](https://w3id.org/GHGA/InformationContentEntity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowStep],[Workflow],[Technology],[Publication],[Protocol],[NamedThing],[InformationContentEntity&#124;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F]^-[WorkflowStep],[InformationContentEntity]^-[Workflow],[InformationContentEntity]^-[Technology],[InformationContentEntity]^-[Publication],[InformationContentEntity]^-[Protocol],[InformationContentEntity]^-[File],[InformationContentEntity]^-[Dataset],[InformationContentEntity]^-[DataUsePermission],[InformationContentEntity]^-[DataUseModifier],[InformationContentEntity]^-[DataUseCondition],[InformationContentEntity]^-[DataAccessPolicy],[NamedThing]^-[InformationContentEntity],[File],[Dataset],[DataUsePermission],[DataUseModifier],[DataUseCondition],[DataAccessPolicy])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowStep],[Workflow],[Technology],[Publication],[Protocol],[NamedThing],[InformationContentEntity&#124;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F]^-[WorkflowStep],[InformationContentEntity]^-[Workflow],[InformationContentEntity]^-[Technology],[InformationContentEntity]^-[Publication],[InformationContentEntity]^-[Protocol],[InformationContentEntity]^-[File],[InformationContentEntity]^-[Dataset],[InformationContentEntity]^-[DataUsePermission],[InformationContentEntity]^-[DataUseModifier],[InformationContentEntity]^-[DataUseCondition],[InformationContentEntity]^-[DataAccessPolicy],[NamedThing]^-[InformationContentEntity],[File],[Dataset],[DataUsePermission],[DataUseModifier],[DataUseCondition],[DataAccessPolicy])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A databased entity, concept or class. This is a generic class that is the root of all the other classes.

## Children

 * [DataAccessPolicy](DataAccessPolicy.md) - A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.
 * [DataUseCondition](DataUseCondition.md) - Data Use Condition represents the use conditions associated with a policy.
 * [DataUseModifier](DataUseModifier.md) - Data use modifiers indicate additional conditions for use.
 * [DataUsePermission](DataUsePermission.md) - A data item that is used to indicate consent permissions for datasets and/or materials and relates to the purposes for which datasets and/or material might be removed, stored or used.
 * [Dataset](Dataset.md) - A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
 * [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.
 * [Protocol](Protocol.md) - A plan specification which has sufficient level of detail and quantitative information to communicate it between investigation agents, so that different investigation agents will reliably be able to independently reproduce the process.
 * [Publication](Publication.md) - The Publication entity represents a publication. While a publication can be any article that is published, the minimum expectation is that the publication has a valid DOI.
 * [Technology](Technology.md) - A Technology is an abstraction that represents the instrument used for an assay. The Technology entity captures instrument-specific attributes that are relevant for an Experiment entity. The Technology entity may be further characterized by its children where each child has fields that are relevant to that particular technology.
 * [Workflow](Workflow.md) - A Workflow is an abstraction that represents the workflow used to perform an analysis. The Workflow entity captures workflow-specific attributes that are relevant for an Analysis entity. The Workflow entity may be further characterized by its children where each child has fields that are relevant to that particular workflow.
 * [WorkflowStep](WorkflowStep.md) - A Workflow Step represents each individual step performed in a Workflow. If the Workflow is a single-step workflow then the Workflow has just one Workflow Step entity. If the Workflow is a multi-step workflow then the Workflow has a Workflow Step entity for each step. All Workflow step specific attributes like parameters, and metadata about execution environment are captured by the Workflow Step entity.

## Referenced by Class


## Attributes


### Inherited from named thing:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [named thing➞alias](named_thing_alias.md)  <sub>0..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [named thing➞xref](named_thing_xref.md)  <sub>0..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)
     * in subsets: (optional,public)
 * [named thing➞creation date](named_thing_creation_date.md)  <sub>0..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was created.
     * Range: [String](types/String.md)
 * [named thing➞update date](named_thing_update_date.md)  <sub>0..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was updated.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | IAO:0000030 |

