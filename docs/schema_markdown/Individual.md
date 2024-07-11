
# Class: Individual


An Individual is a Person who is participating in a Study.

URI: [GHGA:Individual](https://w3id.org/GHGA/Individual)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SupportingFile],[Submission],[Sample],[SupportingFile]<supporting_files%200..*-%20[Individual&#124;phenotypic_features_terms:string%20*;phenotypic_features_ids:string%20*;diagnosis_ids:string%20*;diagnosis_terms:string%20*;sex:IndividualSexEnum;geographical_region:string%20%3F;ancestries:string%20*;ega_accession:string%20%3F;alias:string],[Sample]-%20individual%201..1>[Individual],[Submission]++-%20individuals%201..*>[Individual],[Sample]-%20individual(i)%200..1>[Individual],[Submission]-%20individuals(i)%200..*>[Individual],[Individual]uses%20-.->[IdentifiedByAliasMixin],[IdentifiedByAliasMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[SupportingFile],[Submission],[Sample],[SupportingFile]<supporting_files%200..*-%20[Individual&#124;phenotypic_features_terms:string%20*;phenotypic_features_ids:string%20*;diagnosis_ids:string%20*;diagnosis_terms:string%20*;sex:IndividualSexEnum;geographical_region:string%20%3F;ancestries:string%20*;ega_accession:string%20%3F;alias:string],[Sample]-%20individual%201..1>[Individual],[Submission]++-%20individuals%201..*>[Individual],[Sample]-%20individual(i)%200..1>[Individual],[Submission]-%20individuals(i)%200..*>[Individual],[Individual]uses%20-.->[IdentifiedByAliasMixin],[IdentifiedByAliasMixin])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

 *  **[Sample](Sample.md)** *[Sample➞individual](Sample_individual.md)*  <sub>1..1</sub>  **[Individual](Individual.md)**
 *  **[Submission](Submission.md)** *[Submission➞individuals](Submission_individuals.md)*  <sub>1..\*</sub>  **[Individual](Individual.md)**
 *  **None** *[individual](individual.md)*  <sub>0..1</sub>  **[Individual](Individual.md)**
 *  **None** *[individuals](individuals.md)*  <sub>0..\*</sub>  **[Individual](Individual.md)**

## Attributes


### Own

 * [Individual➞phenotypic_features_terms](Individual_phenotypic_features_terms.md)  <sub>0..\*</sub>
     * Description: The phenotypic feature concepts that the entity is associated with at the time of retrieval from the organism. The Phenotypic Feature is captured using a concept from the Human Phenotype Ontology (e.g., Lymph node hypoplasia, Cough, Hypotension).
     * Range: [String](types/String.md)
     * in subsets: (ontology)
 * [Individual➞phenotypic_features_ids](Individual_phenotypic_features_ids.md)  <sub>0..\*</sub>
     * Description: The corresponding ID to the HPO vocabulary (e.g., HP:0002732, HP:0012735, HP:0002615).
     * Range: [String](types/String.md)
     * in subsets: (ontology)
 * [Individual➞diagnosis_ids](Individual_diagnosis_ids.md)  <sub>0..\*</sub>
     * Description: One or more diagnoses that the entity is associated with at the time of retrieval from the organism. The diagnosis is captured using a code from ICD-10 (WHO version). Please restrict the ICD code to the chapter letter and two digits for the main diagnosis (e.g., E10, C01).
     * Range: [String](types/String.md)
     * in subsets: (ontology)
 * [Individual➞diagnosis_terms](Individual_diagnosis_terms.md)  <sub>0..\*</sub>
     * Description: The ICD-10 terms corresponding to the ICD-10 codes (e.g., Type 1 diabetes mellitus, Malignant neoplasm of base of tongue).
     * Range: [String](types/String.md)
     * in subsets: (ontology)
 * [Individual➞sex](Individual_sex.md)  <sub>1..1</sub>
     * Description: The genotypic sex of the Individual (e.g., female).
     * Range: [IndividualSexEnum](IndividualSexEnum.md)
 * [Individual➞geographical_region](Individual_geographical_region.md)  <sub>0..1</sub>
     * Description: The geographical region where the Individual is located.
     * Range: [String](types/String.md)
     * in subsets: (ontology)
 * [Individual➞ancestries](Individual_ancestries.md)  <sub>0..\*</sub>
     * Description: A person's descent or lineage from a population.
     * Range: [String](types/String.md)
     * in subsets: (ontology)
 * [Individual➞ega_accession](Individual_ega_accession.md)  <sub>0..1</sub>
     * Description: The EGA accession ID of an entity.
     * Range: [String](types/String.md)
 * [Individual➞supporting_files](Individual_supporting_files.md)  <sub>0..\*</sub>
     * Description: The alias of one or more Supporting Files that are associated with this Individual.
     * Range: [SupportingFile](SupportingFile.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | subject |
|  | | patient |

