
# Class: release status mixin


Mixin for entities that can be released at a later point in time.

URI: [GHGA:ReleaseStatusMixin](https://w3id.org/GHGA/ReleaseStatusMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]uses%20-.->[ReleaseStatusMixin&#124;release_status:string;release_date:string],[Dataset]uses%20-.->[ReleaseStatusMixin],[Study],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]uses%20-.->[ReleaseStatusMixin&#124;release_status:string;release_date:string],[Dataset]uses%20-.->[ReleaseStatusMixin],[Study],[Dataset])

## Mixin for

 * [Dataset](Dataset.md) (mixin)  - A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
 * [Study](Study.md) (mixin)  - Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

## Referenced by Class


## Attributes


### Own

 * [release status mixin➞release status](release_status_mixin_release_status.md)  <sub>1..1</sub>
     * Description: The release status of an entity.
     * Range: [String](types/String.md)
 * [release status mixin➞release date](release_status_mixin_release_date.md)  <sub>1..1</sub>
     * Description: The timestamp (in ISO 8601 format) when the entity was released for public consumption.
     * Range: [String](types/String.md)
