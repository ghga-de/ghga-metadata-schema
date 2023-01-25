
# Class: metadata mixin


Mixin for tracking schema specific metadata about an instance.

URI: [GHGA:MetadataMixin](https://w3id.org/GHGA/MetadataMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission]uses%20-.->[MetadataMixin&#124;schema_type:string;schema_version:string],[NamedThing]uses%20-.->[MetadataMixin],[Submission],[NamedThing])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission]uses%20-.->[MetadataMixin&#124;schema_type:string;schema_version:string],[NamedThing]uses%20-.->[MetadataMixin],[Submission],[NamedThing])

## Mixin for

 * [NamedThing](NamedThing.md) (mixin)  - A databased entity, concept or class. This is a generic class that is the root of all the other classes.
 * [Submission](Submission.md) (mixin)  - A grouping entity that represents information about one or more entities. A submission can be considered as a set of inter-related (and inter-connected) entities that represent a data submission to GHGA.

## Referenced by Class


## Attributes


### Own

 * [metadata mixin➞schema type](metadata_mixin_schema_type.md)  <sub>1..1</sub>
     * Description: The schema type an instance corresponds to.
     * Range: [String](types/String.md)
 * [metadata mixin➞schema version](metadata_mixin_schema_version.md)  <sub>1..1</sub>
     * Description: The version of the schema an instance corresponds to.
     * Range: [String](types/String.md)
