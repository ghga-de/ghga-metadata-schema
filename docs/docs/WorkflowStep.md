
# Class: workflow step


A Workflow Step represents each individual step performed in a Workflow. If the Workflow is a single-step workflow then the Workflow has just one Workflow Step entity. If the Workflow is a multi-step workflow then the Workflow has a Workflow Step entity for each step. All Workflow step specific attributes like parameters, and metadata about execution environment are captured by the Workflow Step entity.

URI: [GHGA:WorkflowStep](https://w3id.org/GHGA/WorkflowStep)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowParameter]<has%20workflow%20parameter%200..*-++[WorkflowStep&#124;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Workflow]-%20has%20workflow%20step(i)%200..1>[WorkflowStep],[Workflow]++-%20has%20workflow%20step%200..*>[WorkflowStep],[InformationContentEntity]^-[WorkflowStep],[WorkflowParameter],[Workflow],[InformationContentEntity])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowParameter]<has%20workflow%20parameter%200..*-++[WorkflowStep&#124;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Workflow]-%20has%20workflow%20step(i)%200..1>[WorkflowStep],[Workflow]++-%20has%20workflow%20step%200..*>[WorkflowStep],[InformationContentEntity]^-[WorkflowStep],[WorkflowParameter],[Workflow],[InformationContentEntity])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Referenced by Class

 *  **None** *[has workflow step](has_workflow_step.md)*  <sub>0..1</sub>  **[WorkflowStep](WorkflowStep.md)**
 *  **[Workflow](Workflow.md)** *[workflow➞has workflow step](workflow_has_workflow_step.md)*  <sub>0..\*</sub>  **[WorkflowStep](WorkflowStep.md)**

## Attributes


### Own

 * [workflow step➞has workflow parameter](workflow_step_has_workflow_parameter.md)  <sub>0..\*</sub>
     * Description: One or more parameters that are associated with this Workflow Step.
     * Range: [WorkflowParameter](WorkflowParameter.md)

### Inherited from information content entity:

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
