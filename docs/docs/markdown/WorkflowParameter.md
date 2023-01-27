
# Class: workflow parameter


A key/value pair that represents a parameter used in a Workflow Step.

URI: [GHGA:WorkflowParameter](https://w3id.org/GHGA/WorkflowParameter)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowStep],[WorkflowStep]++-%20has%20workflow%20parameter(i)%200..1>[WorkflowParameter&#124;key:string;value:string],[WorkflowStep]++-%20has%20workflow%20parameter%200..*>[WorkflowParameter])](https://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowStep],[WorkflowStep]++-%20has%20workflow%20parameter(i)%200..1>[WorkflowParameter&#124;key:string;value:string],[WorkflowStep]++-%20has%20workflow%20parameter%200..*>[WorkflowParameter])

## Referenced by Class

 *  **None** *[has workflow parameter](has_workflow_parameter.md)*  <sub>0..1</sub>  **[WorkflowParameter](WorkflowParameter.md)**
 *  **[WorkflowStep](WorkflowStep.md)** *[workflow step➞has workflow parameter](workflow_step_has_workflow_parameter.md)*  <sub>0..\*</sub>  **[WorkflowParameter](WorkflowParameter.md)**

## Attributes


### Own

 * [workflow parameter➞key](workflow_parameter_key.md)  <sub>1..1</sub>
     * Description: Key that represents the parameter name.
     * Range: [String](types/String.md)
 * [workflow parameter➞value](workflow_parameter_value.md)  <sub>1..1</sub>
     * Description: Value corresponding to the the parameter key.
     * Range: [String](types/String.md)
