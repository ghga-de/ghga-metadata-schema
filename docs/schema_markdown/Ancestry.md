
# Class: ancestry


Population category defined using ancestry informative markers (AIMs) based on genetic/genomic data.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Ancestry](https://w3id.org/GHGA-Submission-Metadata-Schema/Ancestry)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Population],[OntologyClassMixin],[Individual],[Individual]++-%20has%20ancestry(i)%200..*>[Ancestry&#124;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F;name(i):string;id(i):string;alias(i):string;xref(i):string%20*],[Individual]++-%20has%20ancestry%200..*>[Ancestry],[Ancestry]uses%20-.->[OntologyClassMixin],[Population]^-[Ancestry])](https://yuml.me/diagram/nofunky;dir:TB/class/[Population],[OntologyClassMixin],[Individual],[Individual]++-%20has%20ancestry(i)%200..*>[Ancestry&#124;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F;name(i):string;id(i):string;alias(i):string;xref(i):string%20*],[Individual]++-%20has%20ancestry%200..*>[Ancestry],[Ancestry]uses%20-.->[OntologyClassMixin],[Population]^-[Ancestry])

## Parents

 *  is_a: [Population](Population.md) - A population is a collection of individuals from the same taxonomic class living, counted or sampled at a particular site or in a particular area.

## Uses Mixin

 *  mixin: [OntologyClassMixin](OntologyClassMixin.md) - Mixin for entities that represent an class/term/concept from an ontology.

## Referenced by Class

 *  **None** *[has ancestry](has_ancestry.md)*  <sub>0..\*</sub>  **[Ancestry](Ancestry.md)**
 *  **[Individual](Individual.md)** *[individual➞has ancestry](individual_has_ancestry.md)*  <sub>0..\*</sub>  **[Ancestry](Ancestry.md)**

## Attributes


### Inherited from population:

 * [NamedThing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [NamedThing➞alias](named_thing_alias.md)  <sub>1..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [NamedThing➞xref](named_thing_xref.md)  <sub>0..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)
 * [population➞name](population_name.md)  <sub>1..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)

### Mixed in from ontology class mixin:

 * [ontology class mixin➞concept identifier](ontology_class_mixin_concept_identifier.md)  <sub>0..1</sub>
     * Description: The Compact URI (CURIE) that uniquely identifies this ontology class.
     * Range: [String](types/String.md)

### Mixed in from ontology class mixin:

 * [ontology class mixin➞concept name](ontology_class_mixin_concept_name.md)  <sub>0..1</sub>
     * Description: The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.
     * Range: [String](types/String.md)

### Mixed in from ontology class mixin:

 * [ontology class mixin➞description](ontology_class_mixin_description.md)  <sub>0..1</sub>
     * Description: The description or definition of an ontology class.
     * Range: [String](types/String.md)

### Mixed in from ontology class mixin:

 * [ontology class mixin➞ontology name](ontology_class_mixin_ontology_name.md)  <sub>0..1</sub>
     * Description: The name or label (rdfs:label) of an ontology class.
     * Range: [String](types/String.md)

### Mixed in from ontology class mixin:

 * [ontology class mixin➞ontology version](ontology_class_mixin_ontology_version.md)  <sub>0..1</sub>
     * Description: The version of the ontology from which this ontology class was chosen.
     * Range: [String](types/String.md)

## Other properties

|                     |     |                   |
| ------------------- | --- | ----------------- |
| **Aliases:**        |     | ancestral group   |
|                     |     | ancestry category |
| **Exact Mappings:** |     | HANCESTRO:0004    |

