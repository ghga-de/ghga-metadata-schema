
# Class: Individual


An Individual is a Person who is participating in a Study.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Individual](https://w3id.org/GHGA-Submission-Metadata-Schema/Individual)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Trio],[Submission],[Biospecimen]-%20individual%201..1>[Individual&#124;sex:IndividualSexEnum;karyotype:KaryotypeEnum%20%3F;age_at_sampling:AgeRangeEnum;vital_status:VitalStatusEnum;geographical_region:GeographicalRegionEnum%20%3F;ancestries:AncestryEnum%20*;phenotypic_features:PhenotypicFeaturesEnum%20*;alias:string],[Submission]++-%20individuals%200..*>[Individual],[Trio]-%20child%201..1>[Individual],[Trio]-%20father%201..1>[Individual],[Trio]-%20mother%201..1>[Individual],[Trio]-%20child(i)%200..1>[Individual],[Trio]-%20father(i)%200..1>[Individual],[Biospecimen]-%20individual(i)%200..1>[Individual],[Submission]-%20individuals(i)%200..*>[Individual],[Trio]-%20mother(i)%200..1>[Individual],[Individual]uses%20-.->[IdentifiedByAliasMixin],[IdentifiedByAliasMixin],[Biospecimen])](https://yuml.me/diagram/nofunky;dir:TB/class/[Trio],[Submission],[Biospecimen]-%20individual%201..1>[Individual&#124;sex:IndividualSexEnum;karyotype:KaryotypeEnum%20%3F;age_at_sampling:AgeRangeEnum;vital_status:VitalStatusEnum;geographical_region:GeographicalRegionEnum%20%3F;ancestries:AncestryEnum%20*;phenotypic_features:PhenotypicFeaturesEnum%20*;alias:string],[Submission]++-%20individuals%200..*>[Individual],[Trio]-%20child%201..1>[Individual],[Trio]-%20father%201..1>[Individual],[Trio]-%20mother%201..1>[Individual],[Trio]-%20child(i)%200..1>[Individual],[Trio]-%20father(i)%200..1>[Individual],[Biospecimen]-%20individual(i)%200..1>[Individual],[Submission]-%20individuals(i)%200..*>[Individual],[Trio]-%20mother(i)%200..1>[Individual],[Individual]uses%20-.->[IdentifiedByAliasMixin],[IdentifiedByAliasMixin],[Biospecimen])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

 *  **[Biospecimen](Biospecimen.md)** *[Biospecimen➞individual](Biospecimen_individual.md)*  <sub>1..1</sub>  **[Individual](Individual.md)**
 *  **[Submission](Submission.md)** *[Submission➞individuals](Submission_individuals.md)*  <sub>0..\*</sub>  **[Individual](Individual.md)**
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

 * [Individual➞sex](Individual_sex.md)  <sub>1..1</sub>
     * Description: The assemblage of physical properties or qualities by which male is distinguished from female; the physical difference between male and female; the distinguishing peculiarity of male or female.
     * Range: [IndividualSexEnum](IndividualSexEnum.md)
 * [Individual➞karyotype](Individual_karyotype.md)  <sub>0..1</sub>
     * Description: The karyotype of an individual if defined.
     * Range: [KaryotypeEnum](KaryotypeEnum.md)
 * [Individual➞age_at_sampling](Individual_age_at_sampling.md)  <sub>1..1</sub>
     * Description: Age of an individual.
     * Range: [AgeRangeEnum](AgeRangeEnum.md)
 * [Individual➞vital_status](Individual_vital_status.md)  <sub>1..1</sub>
     * Description: Last known Vital Status of an Individual.
     * Range: [VitalStatusEnum](VitalStatusEnum.md)
 * [Individual➞geographical_region](Individual_geographical_region.md)  <sub>0..1</sub>
     * Description: The geographical region where the Individual is located. Any demarcated area of the Earth; may be determined by both natural and human boundaries.
     * Range: [GeographicalRegionEnum](GeographicalRegionEnum.md)
 * [Individual➞ancestries](Individual_ancestries.md)  <sub>0..\*</sub>
     * Description: A person's descent or lineage, from a person or from a population.
     * Range: [AncestryEnum](AncestryEnum.md)
 * [Individual➞phenotypic_features](Individual_phenotypic_features.md)  <sub>0..\*</sub>
     * Description: The Phenotypic Feature entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Human Phenotype Ontology. For example, 'HP:0100244' indicates that the Individual - from_which_the_Biospecimen was extracted from - exhibits_'Fibrosarcoma'_as_one_of_its_phenotype.
     * Range: [PhenotypicFeaturesEnum](PhenotypicFeaturesEnum.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | subject |
|  | | patient |

