
# Class: deprecated mixin


Mixin for entities that can be deprecated.

URI: [GHGA:DeprecatedMixin](https://w3id.org/GHGA/DeprecatedMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[NamedThing]<replaced%20by%201..1-%20[DeprecatedMixin&#124;deprecation_date:string])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[NamedThing]<replaced%20by%201..1-%20[DeprecatedMixin&#124;deprecation_date:string])

## Referenced by Class


## Attributes


### Own

 * [deprecated mixin➞replaced by](deprecated_mixin_replaced_by.md)  <sub>1..1</sub>
     * Description: Refers to the entity which replaces a currently deprecated entity.
     * Range: [NamedThing](NamedThing.md)
 * [deprecated mixin➞deprecation date](deprecated_mixin_deprecation_date.md)  <sub>1..1</sub>
     * Description: The timestamp (in ISO 8601 format) when the entity was deprecated.
     * Range: [String](types/String.md)
