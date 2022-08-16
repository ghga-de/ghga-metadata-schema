
# Class: agent


An agent is something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity. Agents include a Person, Organization, or Software that performs an activity.

URI: [GHGA:Agent](https://w3id.org/GHGA/Agent)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[ExperimentProcess],[AnalysisProcess],[AnalysisProcess]++-%20has%20agent%200..1>[Agent&#124;name:string%20%3F;description:string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[ExperimentProcess]++-%20has%20agent%200..1>[Agent],[ExperimentProcess]-%20has%20agent(i)%200..1>[Agent],[AnalysisProcess]-%20has%20agent(i)%200..1>[Agent],[NamedThing]^-[Agent])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[ExperimentProcess],[AnalysisProcess],[AnalysisProcess]++-%20has%20agent%200..1>[Agent&#124;name:string%20%3F;description:string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[ExperimentProcess]++-%20has%20agent%200..1>[Agent],[ExperimentProcess]-%20has%20agent(i)%200..1>[Agent],[AnalysisProcess]-%20has%20agent(i)%200..1>[Agent],[NamedThing]^-[Agent])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A databased entity, concept or class. This is a generic class that is the root of all the other classes.

## Referenced by Class

 *  **[AnalysisProcess](AnalysisProcess.md)** *[analysis process➞has agent](analysis_process_has_agent.md)*  <sub>0..1</sub>  **[Agent](Agent.md)**
 *  **[ExperimentProcess](ExperimentProcess.md)** *[experiment process➞has agent](experiment_process_has_agent.md)*  <sub>0..1</sub>  **[Agent](Agent.md)**
 *  **None** *[has agent](has_agent.md)*  <sub>0..1</sub>  **[Agent](Agent.md)**

## Attributes


### Own

 * [name](name.md)  <sub>0..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [description](description.md)  <sub>0..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)

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
| **Exact Mappings:** | | prov:Agent |

