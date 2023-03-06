
# Class: planned process


A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and depends on some entity during the time it occurs.

URI: [GHGA:PlannedProcess](https://w3id.org/GHGA/PlannedProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ResearchActivity],[PlannedProcess&#124;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F]^-[ResearchActivity],[PlannedProcess]^-[Investigation],[PlannedProcess]^-[ExperimentProcess],[PlannedProcess]^-[DataTransformation],[PlannedProcess]^-[AnalysisProcess],[NamedThing]^-[PlannedProcess],[NamedThing],[Investigation],[ExperimentProcess],[DataTransformation],[AnalysisProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[ResearchActivity],[PlannedProcess&#124;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F]^-[ResearchActivity],[PlannedProcess]^-[Investigation],[PlannedProcess]^-[ExperimentProcess],[PlannedProcess]^-[DataTransformation],[PlannedProcess]^-[AnalysisProcess],[NamedThing]^-[PlannedProcess],[NamedThing],[Investigation],[ExperimentProcess],[DataTransformation],[AnalysisProcess])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A databased entity, concept or class. This is a generic class that is the root of all the other classes.

## Children

 * [AnalysisProcess](AnalysisProcess.md) - An analysis process is a process that describes how one or more Files, from a Study, are transformed to another set of Files via a Workflow. The analysis process also keeps track of the workflow metadata and the Agent that is running the Analysis.
 * [DataTransformation](DataTransformation.md) - A data transformation technique used to analyze and interpret data to gain a better understanding of it.
 * [ExperimentProcess](ExperimentProcess.md) - An Experiment Process is a process that describes how a Sample is transformed to a File via an assay. The Experiment Process also keeps track of the Protocol used and the Agent that is running the experiment.
 * [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.
 * [ResearchActivity](ResearchActivity.md) - A planned process executed in the performance of scientific research wherein systematic investigations are performed to establish facts and reach new conclusions about phenomena in the world.

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
| **Exact Mappings:** | | EFO:0004542 |
|  | | OBI:0000011 |
|  | | COB:0000082 |

