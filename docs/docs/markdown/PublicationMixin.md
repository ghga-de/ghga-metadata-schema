
# Class: publication mixin


Mixin for entities that can have one or more publications.

URI: [GHGA:PublicationMixin](https://w3id.org/GHGA/PublicationMixin)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Publication]<has%20publication%200..1-%20[PublicationMixin],[Study]uses%20-.->[PublicationMixin],[Dataset]uses%20-.->[PublicationMixin],[Study],[Publication],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[Publication]<has%20publication%200..1-%20[PublicationMixin],[Study]uses%20-.->[PublicationMixin],[Dataset]uses%20-.->[PublicationMixin],[Study],[Publication],[Dataset])

## Mixin for

 * [Dataset](Dataset.md) (mixin)  - A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
 * [Study](Study.md) (mixin)  - Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.

## Referenced by Class


## Attributes


### Own

 * [has publication](has_publication.md)  <sub>0..1</sub>
     * Description: The Publication associated with an entity.
     * Range: [Publication](Publication.md)
     * in subsets: (optional,public)
