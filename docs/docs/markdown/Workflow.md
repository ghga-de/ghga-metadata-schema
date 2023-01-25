
# Class: workflow


A Workflow is an abstraction that represents the workflow used to perform an analysis. The Workflow entity captures workflow-specific attributes that are relevant for an Analysis entity. The Workflow entity may be further characterized by its children where each child has fields that are relevant to that particular workflow.

URI: [GHGA:Workflow](https://w3id.org/GHGA/Workflow)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowStep],[WorkflowStep]<has%20workflow%20step%201..*-++[Workflow&#124;name:string;alias:string;id(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[AnalysisProcess]++-%20has%20workflow%200..1>[Workflow],[Analysis]++-%20has%20workflow%201..*>[Workflow],[Analysis]-%20has%20workflow(i)%200..1>[Workflow],[AnalysisProcess]-%20has%20workflow(i)%200..1>[Workflow],[InformationContentEntity]^-[Workflow],[InformationContentEntity],[AnalysisProcess],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowStep],[WorkflowStep]<has%20workflow%20step%201..*-++[Workflow&#124;name:string;alias:string;id(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[AnalysisProcess]++-%20has%20workflow%200..1>[Workflow],[Analysis]++-%20has%20workflow%201..*>[Workflow],[Analysis]-%20has%20workflow(i)%200..1>[Workflow],[AnalysisProcess]-%20has%20workflow(i)%200..1>[Workflow],[InformationContentEntity]^-[Workflow],[InformationContentEntity],[AnalysisProcess],[Analysis])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Referenced by Class

 *  **[AnalysisProcess](AnalysisProcess.md)** *[analysis process➞has workflow](analysis_process_has_workflow.md)*  <sub>0..1</sub>  **[Workflow](Workflow.md)**
 *  **[Analysis](Analysis.md)** *[analysis➞has workflow](analysis_has_workflow.md)*  <sub>1..\*</sub>  **[Workflow](Workflow.md)**
 *  **None** *[has workflow](has_workflow.md)*  <sub>0..1</sub>  **[Workflow](Workflow.md)**

## Attributes


### Own

 * [workflow➞name](workflow_name.md)  <sub>1..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)
 * [workflow➞has workflow step](workflow_has_workflow_step.md)  <sub>1..\*</sub>
     * Description: The individual workflow step that with other workflow step(s) collectively defines a Workflow entity.
     * Range: [WorkflowStep](WorkflowStep.md)
 * [workflow➞alias](workflow_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)

### Inherited from information content entity:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
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
