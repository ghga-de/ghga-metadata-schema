
# Class: Individual


An Individual is a Person who is participating in a Study.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Individual](https://w3id.org/GHGA-Submission-Metadata-Schema/Individual)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Person],[File]<files%200..*-%20[Individual&#124;sex:IndividualSexEnum;karyotype:KaryotypeEnum%20%3F;age_at_sampling:AgeRangeEnum;vital_status:VitalStatusEnum;geographical_region:GeographicalRegionEnum%20%3F;phenotypic_features:PhenotypicFeaturesEnum%20*;alias:string;given_name(i):string%20%3F;family_name(i):string%20%3F;additional_name(i):string%20%3F],[Disease]<diseases%201..*-++[Individual],[Individual]<children%200..*-%20[Individual],[Individual]<parents%200..*-%20[Individual],[Ancestry]<ancestries%200..*-++[Individual],[Biospecimen]-%20individual%201..1>[Individual],[Submission]++-%20individuals%200..*>[Individual],[Biospecimen]-%20individual(i)%200..1>[Individual],[Submission]-%20individuals(i)%200..*>[Individual],[Individual]uses%20-.->[IdentifiedByAliasMixin],[Person]^-[Individual],[IdentifiedByAliasMixin],[File],[Disease],[Biospecimen],[Ancestry])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Person],[File]<files%200..*-%20[Individual&#124;sex:IndividualSexEnum;karyotype:KaryotypeEnum%20%3F;age_at_sampling:AgeRangeEnum;vital_status:VitalStatusEnum;geographical_region:GeographicalRegionEnum%20%3F;phenotypic_features:PhenotypicFeaturesEnum%20*;alias:string;given_name(i):string%20%3F;family_name(i):string%20%3F;additional_name(i):string%20%3F],[Disease]<diseases%201..*-++[Individual],[Individual]<children%200..*-%20[Individual],[Individual]<parents%200..*-%20[Individual],[Ancestry]<ancestries%200..*-++[Individual],[Biospecimen]-%20individual%201..1>[Individual],[Submission]++-%20individuals%200..*>[Individual],[Biospecimen]-%20individual(i)%200..1>[Individual],[Submission]-%20individuals(i)%200..*>[Individual],[Individual]uses%20-.->[IdentifiedByAliasMixin],[Person]^-[Individual],[IdentifiedByAliasMixin],[File],[Disease],[Biospecimen],[Ancestry])

## Parents

 *  is_a: [Person](Person.md) - A member of the species Homo sapiens.

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

 *  **[Biospecimen](Biospecimen.md)** *[Biospecimen➞individual](Biospecimen_individual.md)*  <sub>1..1</sub>  **[Individual](Individual.md)**
 *  **[Individual](Individual.md)** *[Individual➞children](Individual_children.md)*  <sub>0..\*</sub>  **[Individual](Individual.md)**
 *  **[Individual](Individual.md)** *[Individual➞parents](Individual_parents.md)*  <sub>0..\*</sub>  **[Individual](Individual.md)**
 *  **[Submission](Submission.md)** *[Submission➞individuals](Submission_individuals.md)*  <sub>0..\*</sub>  **[Individual](Individual.md)**
 *  **None** *[children](children.md)*  <sub>0..\*</sub>  **[Individual](Individual.md)**
 *  **None** *[individual](individual.md)*  <sub>0..1</sub>  **[Individual](Individual.md)**
 *  **None** *[individuals](individuals.md)*  <sub>0..\*</sub>  **[Individual](Individual.md)**
 *  **None** *[parents](parents.md)*  <sub>0..\*</sub>  **[Individual](Individual.md)**

## Attributes


### Own

 * [Individual➞sex](Individual_sex.md)  <sub>1..1</sub>
     * Description: The assemblage of physical properties or qualities by which male is distinguished from female; the physical difference between male and female; the distinguishing peculiarity of male or female.
     * Range: [IndividualSexEnum](IndividualSexEnum.md)
     * in subsets: (restricted)
 * [Individual➞karyotype](Individual_karyotype.md)  <sub>0..1</sub>
     * Description: The karyotype of an individual if defined.
     * Range: [KaryotypeEnum](KaryotypeEnum.md)
     * in subsets: (restricted)
 * [Individual➞age_at_sampling](Individual_age_at_sampling.md)  <sub>1..1</sub>
     * Description: Age of an individual.
     * Range: [AgeRangeEnum](AgeRangeEnum.md)
     * in subsets: (restricted)
 * [Individual➞vital_status](Individual_vital_status.md)  <sub>1..1</sub>
     * Description: Last known Vital Status of an Individual.
     * Range: [VitalStatusEnum](VitalStatusEnum.md)
     * in subsets: (restricted)
 * [Individual➞geographical_region](Individual_geographical_region.md)  <sub>0..1</sub>
     * Description: The geographical region where the Individual is located. Any demarcated area of the Earth; may be determined by both natural and human boundaries.
     * Range: [GeographicalRegionEnum](GeographicalRegionEnum.md)
     * in subsets: (restricted)
 * [Individual➞ancestries](Individual_ancestries.md)  <sub>0..\*</sub>
     * Description: A person's descent or lineage, from a person or from a population. Typically this is a value from HANCESTRO (Human Ancestry Ontology).
     * Range: [Ancestry](Ancestry.md)
     * in subsets: (restricted)
 * [Individual➞parents](Individual_parents.md)  <sub>0..\*</sub>
     * Description: One or more parent for an Individual.
     * Range: [Individual](Individual.md)
     * in subsets: (restricted)
 * [Individual➞children](Individual_children.md)  <sub>0..\*</sub>
     * Description: One or more children for an Individual.
     * Range: [Individual](Individual.md)
     * in subsets: (restricted)
 * [Individual➞diseases](Individual_diseases.md)  <sub>1..\*</sub>
     * Description: The Disease entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Mondo Disease Ontology. For example, 'MONDO:0003742' indicates that the Individual - from_which_the_Biospecimen was extracted from - suffers_from_'Heart_Fibrosarcoma'.
     * Range: [Disease](Disease.md)
 * [Individual➞phenotypic_features](Individual_phenotypic_features.md)  <sub>0..\*</sub>
     * Description: The Phenotypic Feature entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Human Phenotype Ontology. For example, 'HP:0100244' indicates that the Individual - from_which_the_Biospecimen was extracted from - exhibits_'Fibrosarcoma'_as_one_of_its_phenotype.
     * Range: [PhenotypicFeaturesEnum](PhenotypicFeaturesEnum.md)
     * in subsets: (restricted)
 * [Individual➞files](Individual_files.md)  <sub>0..\*</sub>
     * Description: Additional/supplementary files associated with an Individual. Typically, a phenopacket or pedigree file.
     * Range: [File](File.md)
     * in subsets: (restricted)

### Inherited from Person:

 * [Person➞given_name](Person_given_name.md)  <sub>0..1</sub>
     * Description: First name.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [Person➞family_name](Person_family_name.md)  <sub>0..1</sub>
     * Description: Last name.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [Person➞additional_name](Person_additional_name.md)  <sub>0..1</sub>
     * Description: additional_name(s).
     * Range: [String](types/String.md)
     * in subsets: (restricted)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
     * in subsets: (restricted)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | subject |
|  | | patient |

