
# Class: deprecated mixin


Mixin for entities that can be deprecated.

URI: [GHGA:DeprecatedMixin](https://w3id.org/GHGA/DeprecatedMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[NamedThing]<replaced%20by%200..1-%20[DeprecatedMixin&#124;deprecation_date:string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[NamedThing]<replaced%20by%200..1-%20[DeprecatedMixin&#124;deprecation_date:string%20%3F])

## Attributes


### Own

 * [replaced by](replaced_by.md)  <sub>0..1</sub>
     * Description: Refers to the entity which replaces a currently deprecated entity.
     * Range: [NamedThing](NamedThing.md)
 * [deprecation date](deprecation_date.md)  <sub>0..1</sub>
     * Description: The timestamp (in ISO 8601 format) when the entity was deprecated.
     * Range: [String](types/String.md)
