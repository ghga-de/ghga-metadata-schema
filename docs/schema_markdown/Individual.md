
# Class: Individual


An Individual is a Person who is participating in a Study.

URI: [GHGA:Individual](https://w3id.org/GHGA/Individual)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Trio],[Submission],[Biospecimen]-%20individual%201..1>[Individual&#124;phenotypic_features:string%20*;sex:IndividualSexEnum;karyotype:KaryotypeEnum%20%3F;geographical_region:string%20%3F;ancestries:string%20*;alias:string],[Submission]++-%20individuals%201..*>[Individual],[Trio]-%20child%201..1>[Individual],[Trio]-%20father%201..1>[Individual],[Trio]-%20mother%201..1>[Individual],[Trio]-%20child(i)%200..1>[Individual],[Trio]-%20father(i)%200..1>[Individual],[Biospecimen]-%20individual(i)%200..1>[Individual],[Submission]-%20individuals(i)%200..*>[Individual],[Trio]-%20mother(i)%200..1>[Individual],[Individual]uses%20-.->[IdentifiedByAliasMixin],[IdentifiedByAliasMixin],[Biospecimen])](https://yuml.me/diagram/nofunky;dir:TB/class/[Trio],[Submission],[Biospecimen]-%20individual%201..1>[Individual&#124;phenotypic_features:string%20*;sex:IndividualSexEnum;karyotype:KaryotypeEnum%20%3F;geographical_region:string%20%3F;ancestries:string%20*;alias:string],[Submission]++-%20individuals%201..*>[Individual],[Trio]-%20child%201..1>[Individual],[Trio]-%20father%201..1>[Individual],[Trio]-%20mother%201..1>[Individual],[Trio]-%20child(i)%200..1>[Individual],[Trio]-%20father(i)%200..1>[Individual],[Biospecimen]-%20individual(i)%200..1>[Individual],[Submission]-%20individuals(i)%200..*>[Individual],[Trio]-%20mother(i)%200..1>[Individual],[Individual]uses%20-.->[IdentifiedByAliasMixin],[IdentifiedByAliasMixin],[Biospecimen])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

 *  **[Biospecimen](Biospecimen.md)** *[Biospecimen➞individual](Biospecimen_individual.md)*  <sub>1..1</sub>  **[Individual](Individual.md)**
 *  **[Submission](Submission.md)** *[Submission➞individuals](Submission_individuals.md)*  <sub>1..\*</sub>  **[Individual](Individual.md)**
 *  **[Trio](Trio.md)** *[Trio➞child](Trio_child.md)*  <sub>1..1</sub>  **[Individual](Individual.md)**
 *  **[Trio](Trio.md)** *[Trio➞father](Trio_father.md)*  <sub>1..1</sub>  **[Individual](Individual.md)**
 *  **[Trio](Trio.md)** *[Trio➞mother](Trio_mother.md)*  <sub>1..1</sub>  **[Individual](Individual.md)**
 *  **None** *[child](child.md)*  <sub>0..1</sub>  **[Individual](Individual.md)**
 *  **None** *[father](father.md)*  <sub>0..1</sub>  **[Individual](Individual.md)**
 *  **None** *[individual](individual.md)*  <sub>0..1</sub>  **[Individual](Individual.md)**
 *  **None** *[individuals](individuals.md)*  <sub>0..\*</sub>  **[Individual](Individual.md)**
 *  **None** *[mother](mother.md)*  <sub>0..1</sub>  **[Individual](Individual.md)**

## Attributes


### Own

 * [Individual➞phenotypic_features](Individual_phenotypic_features.md)  <sub>0..\*</sub>
     * Description: The phenotypic feature concepts that the entity is associated with at the time of retrieval from the organism. The Phenotypic Feature is captured using a concept from the Human Phenotype Ontology.
     * Range: [String](types/String.md)
     * in subsets: (ontology)
 * [Individual➞sex](Individual_sex.md)  <sub>1..1</sub>
     * Description: The genotypic sex of the Individual (e.g., female).
     * Range: [IndividualSexEnum](IndividualSexEnum.md)
 * [Individual➞karyotype](Individual_karyotype.md)  <sub>0..1</sub>
     * Description: The karyotype of the Individual.
     * Range: [KaryotypeEnum](KaryotypeEnum.md)
 * [Individual➞geographical_region](Individual_geographical_region.md)  <sub>0..1</sub>
     * Description: The geographical region where the Individual is located.
     * Range: [String](types/String.md)
     * in subsets: (ontology)
 * [Individual➞ancestries](Individual_ancestries.md)  <sub>0..\*</sub>
     * Description: A person's descent or lineage from a population.
     * Range: [String](types/String.md)
     * in subsets: (ontology)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | subject |
|  | | patient |

