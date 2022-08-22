
# Class: cohort


A cohort is a collection of individuals that share a common characteristic/observation and have been grouped together for a research study/investigation.

URI: [GHGA:Cohort](https://w3id.org/GHGA/Cohort)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Population],[Individual],[Individual]<has%20individual%200..*-++[Cohort&#124;accession:string%20%3F;name(i):string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Cohort]uses%20-.->[AccessionMixin],[Population]^-[Cohort],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Population],[Individual],[Individual]<has%20individual%200..*-++[Cohort&#124;accession:string%20%3F;name(i):string%20%3F;id(i):string;alias(i):string%20%3F;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Cohort]uses%20-.->[AccessionMixin],[Population]^-[Cohort],[AccessionMixin])

## Parents

 *  is_a: [Population](Population.md) - A population is a collection of individuals from the same taxonomic class living, counted or sampled at a particular site or in a particular area.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.

## Referenced by Class


## Attributes


### Own

 * [cohort➞has individual](cohort_has_individual.md)  <sub>0..\*</sub>
     * Description: One or more Individuals that collectively define this Cohort.
     * Range: [Individual](Individual.md)
     * in subsets: (essential,restricted)

### Inherited from population:

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
 * [name](name.md)  <sub>0..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)

### Mixed in from accession mixin:

 * [accession](accession.md)  <sub>0..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)
