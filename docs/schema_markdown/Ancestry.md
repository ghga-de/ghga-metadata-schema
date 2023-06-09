
# Class: Ancestry


Population category defined using ancestries informative markers (AIMs) based on genetic/genomic data.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Ancestry](https://w3id.org/GHGA-Submission-Metadata-Schema/Ancestry)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Population],[OntologyClassMixin],[Ancestry&#124;id:string;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F;name(i):string]uses%20-.->[OntologyClassMixin],[Population]^-[Ancestry])](https://yuml.me/diagram/nofunky;dir:TB/class/[Population],[OntologyClassMixin],[Ancestry&#124;id:string;concept_identifier:string%20%3F;concept_name:string%20%3F;description:string%20%3F;ontology_name:string%20%3F;ontology_version:string%20%3F;name(i):string]uses%20-.->[OntologyClassMixin],[Population]^-[Ancestry])

## Parents

 *  is_a: [Population](Population.md) - A Population is a collection of individuals from the same taxonomic class living, counted or sampled at a particular site or in a particular area.

## Uses Mixin

 *  mixin: [OntologyClassMixin](OntologyClassMixin.md) - Mixin for entities that represent an class/term/concept from an ontology.

## Attributes


### Inherited from Population:

 * [Population➞name](Population_name.md)  <sub>1..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)

### Mixed in from OntologyClassMixin:

 * [OntologyClassMixin➞id](OntologyClassMixin_id.md)  <sub>1..1</sub>
     * Description: An identifier that uniquely represents an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)

### Mixed in from OntologyClassMixin:

 * [OntologyClassMixin➞concept_identifier](OntologyClassMixin_concept_identifier.md)  <sub>0..1</sub>
     * Description: The Compact URI (CURIE) that uniquely identifies this ontology class.
     * Range: [String](types/String.md)

### Mixed in from OntologyClassMixin:

 * [OntologyClassMixin➞concept_name](OntologyClassMixin_concept_name.md)  <sub>0..1</sub>
     * Description: The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.
     * Range: [String](types/String.md)

### Mixed in from OntologyClassMixin:

 * [OntologyClassMixin➞description](OntologyClassMixin_description.md)  <sub>0..1</sub>
     * Description: The description or definition of an ontology class.
     * Range: [String](types/String.md)

### Mixed in from OntologyClassMixin:

 * [OntologyClassMixin➞ontology_name](OntologyClassMixin_ontology_name.md)  <sub>0..1</sub>
     * Description: The name or label (rdfs:label) of an ontology class.
     * Range: [String](types/String.md)

### Mixed in from OntologyClassMixin:

 * [OntologyClassMixin➞ontology_version](OntologyClassMixin_ontology_version.md)  <sub>0..1</sub>
     * Description: The version of the ontology from which this ontology class was chosen.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | ancestral group |
|  | | ancestries category |
| **Exact Mappings:** | | HANCESTRO:0004 |

