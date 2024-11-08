
# Class: Individual


An Individual is a Person who is participating in a Study.

URI: [GHGA:Individual](https://w3id.org/GHGA/Individual)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample],[IndividualSupportingFile],[IndividualSupportingFile]-%20individual%201..1>[Individual&#124;phenotypic_features_terms:string%20*;phenotypic_features_ids:string%20*;diagnosis_ids:string%20*;diagnosis_terms:string%20*;sex:IndividualSexEnum;geographical_region_term:string%20%3F;geographical_region_id:string%20%3F;ancestry_terms:string%20*;ancestry_ids:string%20*;alias:string],[Sample]-%20individual%201..1>[Individual],[Submission]++-%20individuals%201..*>[Individual],[Sample]-%20individual(i)%200..1>[Individual],[IndividualSupportingFile]-%20individual(i)%200..1>[Individual],[Submission]-%20individuals(i)%200..*>[Individual],[Individual]uses%20-.->[IdentifiedByAliasMixin],[IdentifiedByAliasMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample],[IndividualSupportingFile],[IndividualSupportingFile]-%20individual%201..1>[Individual&#124;phenotypic_features_terms:string%20*;phenotypic_features_ids:string%20*;diagnosis_ids:string%20*;diagnosis_terms:string%20*;sex:IndividualSexEnum;geographical_region_term:string%20%3F;geographical_region_id:string%20%3F;ancestry_terms:string%20*;ancestry_ids:string%20*;alias:string],[Sample]-%20individual%201..1>[Individual],[Submission]++-%20individuals%201..*>[Individual],[Sample]-%20individual(i)%200..1>[Individual],[IndividualSupportingFile]-%20individual(i)%200..1>[Individual],[Submission]-%20individuals(i)%200..*>[Individual],[Individual]uses%20-.->[IdentifiedByAliasMixin],[IdentifiedByAliasMixin])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

 *  **[IndividualSupportingFile](IndividualSupportingFile.md)** *[IndividualSupportingFile➞individual](IndividualSupportingFile_individual.md)*  <sub>1..1</sub>  **[Individual](Individual.md)**
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
     * Description: The biological sex of the Individual (e.g., female).
     * Range: [IndividualSexEnum](IndividualSexEnum.md)
 * [Individual➞geographical_region_term](Individual_geographical_region_term.md)  <sub>0..1</sub>
     * Description: The geographical region where the Individual is located. The Geographical Region is captured using a concept from the NCIT "country" class (NCIT:C25464) (e.g., Austria, Germany, Italy).
     * Range: [String](types/String.md)
     * in subsets: (ontology)
 * [Individual➞geographical_region_id](Individual_geographical_region_id.md)  <sub>0..1</sub>
     * Description: The corresponding ID to the NCIT vocabulary (e.g., NCIT:C16312, NCIT:C16636, NCIT:C16761).
     * Range: [String](types/String.md)
     * in subsets: (ontology)
 * [Individual➞ancestry_terms](Individual_ancestry_terms.md)  <sub>0..\*</sub>
     * Description: A person's descent or lineage from a population. The Ancestry is captured using a concept from the Human Ancestry Ontology "ancestry category" (HANCESTRO:0004) branch (e.g., African, European, Oceanian).
     * Range: [String](types/String.md)
     * in subsets: (ontology)
 * [Individual➞ancestry_ids](Individual_ancestry_ids.md)  <sub>0..\*</sub>
     * Description: The corresponding ID to the HANCESTRO vocabulary (e.g., HANCESTRO:0010, HANCESTRO:0005, HANCESTRO:0017).
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

