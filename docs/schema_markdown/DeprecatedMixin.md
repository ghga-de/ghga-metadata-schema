
# Class: DeprecatedMixin


Mixin for entities that can be deprecated.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/DeprecatedMixin](https://w3id.org/GHGA-Submission-Metadata-Schema/DeprecatedMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[NamedThing]<replaced_by%201..1-%20[DeprecatedMixin&#124;deprecation_date:string])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[NamedThing]<replaced_by%201..1-%20[DeprecatedMixin&#124;deprecation_date:string])

## Referenced by Class


## Attributes


### Own

 * [DeprecatedMixin➞replaced_by](DeprecatedMixin_replaced_by.md)  <sub>1..1</sub>
     * Description: Refers to the entity which replaces a currently deprecated entity.
     * Range: [NamedThing](NamedThing.md)
 * [DeprecatedMixin➞deprecation_date](DeprecatedMixin_deprecation_date.md)  <sub>1..1</sub>
     * Description: The timestamp (in ISO 8601 format) when the entity was deprecated.
     * Range: [String](types/String.md)
