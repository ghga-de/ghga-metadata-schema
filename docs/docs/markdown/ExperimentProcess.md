
# Class: experiment process


An Experiment Process is a process that describes how a Sample is transformed to a File via an assay. The Experiment Process also keeps track of the Protocol used and the Agent that is running the experiment.

URI: [GHGA:ExperimentProcess](https://w3id.org/GHGA/ExperimentProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[Protocol],[PlannedProcess],[File],[File]<has%20output%201..*-++[ExperimentProcess&#124;type:experiment_process_type_enum;title:string%20%3F;id(i):string;alias(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[Agent]<has%20agent%201..1-++[ExperimentProcess],[Protocol]<has%20protocol%201..1-++[ExperimentProcess],[Sample]<has%20input%201..1-++[ExperimentProcess],[Experiment]++-%20has%20experiment%20process%201..*>[ExperimentProcess],[Experiment]-%20has%20experiment%20process(i)%200..1>[ExperimentProcess],[ExperimentProcess]uses%20-.->[AttributeMixin],[PlannedProcess]^-[ExperimentProcess],[Experiment],[AttributeMixin],[Attribute],[Agent])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample],[Protocol],[PlannedProcess],[File],[File]<has%20output%201..*-++[ExperimentProcess&#124;type:experiment_process_type_enum;title:string%20%3F;id(i):string;alias(i):string;xref(i):string%20%2B;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[Agent]<has%20agent%201..1-++[ExperimentProcess],[Protocol]<has%20protocol%201..1-++[ExperimentProcess],[Sample]<has%20input%201..1-++[ExperimentProcess],[Experiment]++-%20has%20experiment%20process%201..*>[ExperimentProcess],[Experiment]-%20has%20experiment%20process(i)%200..1>[ExperimentProcess],[ExperimentProcess]uses%20-.->[AttributeMixin],[PlannedProcess]^-[ExperimentProcess],[Experiment],[AttributeMixin],[Attribute],[Agent])

## Parents

 *  is_a: [PlannedProcess](PlannedProcess.md) - A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and depends on some entity during the time it occurs.

## Uses Mixin

 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Referenced by Class

 *  **[Experiment](Experiment.md)** *[experiment➞has experiment process](experiment_has_experiment_process.md)*  <sub>1..\*</sub>  **[ExperimentProcess](ExperimentProcess.md)**
 *  **None** *[has experiment process](has_experiment_process.md)*  <sub>0..1</sub>  **[ExperimentProcess](ExperimentProcess.md)**

## Attributes


### Own

 * [experiment process➞type](experiment_process_type.md)  <sub>1..1</sub>
     * Description: The type of experiment process.
     * Range: [experiment process type enum](experiment process type enum.md)
 * [experiment process➞title](experiment_process_title.md)  <sub>0..1</sub>
     * Description: A descriptive title that explains the step(s) involved in performing the experiment leading up to the sequencing of the sample and generation of raw data from the instrument. (eg: Sample extraction -> Target Enrichment)
     * Range: [String](types/String.md)
 * [experiment process➞has input](experiment_process_has_input.md)  <sub>1..1</sub>
     * Description: The input to the Experiment Process. Usually a Sample entity.
     * Range: [Sample](Sample.md)
     * in subsets: (restricted)
 * [experiment process➞has protocol](experiment_process_has_protocol.md)  <sub>1..1</sub>
     * Description: The Protocol entity used by this Experiment Process.
     * Range: [Protocol](Protocol.md)
     * in subsets: (restricted)
 * [experiment process➞has agent](experiment_process_has_agent.md)  <sub>1..1</sub>
     * Description: The Agent - a software, institution, or human - that is executing or responsible for executing the Experiment Process.
     * Range: [Agent](Agent.md)
     * in subsets: (restricted)
 * [experiment process➞has output](experiment_process_has_output.md)  <sub>1..\*</sub>
     * Description: The output of this Experiment Process. Usually a File entity.
     * Range: [File](File.md)
     * in subsets: (restricted)

### Inherited from planned process:

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

### Mixed in from attribute mixin:

 * [attribute mixin➞has attribute](attribute_mixin_has_attribute.md)  <sub>1..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)
