
# Class: Individual


An Individual is a Person who is participating in a Study.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Individual](https://w3id.org/GHGA-Submission-Metadata-Schema/Individual)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[PhenotypicFeature],[Person],[File]<has_file%200..*-++[Individual&#124;sex:BiologicalSexEnum;karyotype:string%20%3F;age:AgeRangeEnum;vital_status:VitalStatusEnum;geographical_region:string%20%3F;accession:string;ega_accession:string;given_name(i):string%20%3F;family_name(i):string%20%3F;additional_name(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[PhenotypicFeature]<has_phenotypic_feature%200..*-++[Individual],[Disease]<has_disease%201..*-++[Individual],[Individual]<has_children%200..*-++[Individual],[Individual]<has_parent%200..*-++[Individual],[Ancestry]<has_ancestry%200..*-++[Individual],[Biospecimen]++-%20has_individual%201..1>[Individual],[Submission]++-%20has_individual%200..*>[Individual],[Biospecimen]-%20has_individual(i)%200..1>[Individual],[Submission]-%20has_individual(i)%200..1>[Individual],[Individual]uses%20-.->[AccessionMixin],[Individual]uses%20-.->[EgaAccessionMixin],[Person]^-[Individual],[File],[EgaAccessionMixin],[Disease],[Biospecimen],[Ancestry],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[PhenotypicFeature],[Person],[File]<has_file%200..*-++[Individual&#124;sex:BiologicalSexEnum;karyotype:string%20%3F;age:AgeRangeEnum;vital_status:VitalStatusEnum;geographical_region:string%20%3F;accession:string;ega_accession:string;given_name(i):string%20%3F;family_name(i):string%20%3F;additional_name(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[PhenotypicFeature]<has_phenotypic_feature%200..*-++[Individual],[Disease]<has_disease%201..*-++[Individual],[Individual]<has_children%200..*-++[Individual],[Individual]<has_parent%200..*-++[Individual],[Ancestry]<has_ancestry%200..*-++[Individual],[Biospecimen]++-%20has_individual%201..1>[Individual],[Submission]++-%20has_individual%200..*>[Individual],[Biospecimen]-%20has_individual(i)%200..1>[Individual],[Submission]-%20has_individual(i)%200..1>[Individual],[Individual]uses%20-.->[AccessionMixin],[Individual]uses%20-.->[EgaAccessionMixin],[Person]^-[Individual],[File],[EgaAccessionMixin],[Disease],[Biospecimen],[Ancestry],[AccessionMixin])

## Parents

 *  is_a: [Person](Person.md) - A member of the species Homo sapiens.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an ega_accession, in addition to GHGA accession.

## Referenced by Class

 *  **[Biospecimen](Biospecimen.md)** *[Biospecimen➞has_individual](Biospecimen_has_individual.md)*  <sub>1..1</sub>  **[Individual](Individual.md)**
 *  **[Individual](Individual.md)** *[Individual➞has_children](Individual_has_children.md)*  <sub>0..\*</sub>  **[Individual](Individual.md)**
 *  **[Individual](Individual.md)** *[Individual➞has_parent](Individual_has_parent.md)*  <sub>0..\*</sub>  **[Individual](Individual.md)**
 *  **[Submission](Submission.md)** *[Submission➞has_individual](Submission_has_individual.md)*  <sub>0..\*</sub>  **[Individual](Individual.md)**
 *  **None** *[has_individual](has_individual.md)*  <sub>0..1</sub>  **[Individual](Individual.md)**

## Attributes


### Own

 * [Individual➞sex](Individual_sex.md)  <sub>1..1</sub>
     * Description: The assemblage of physical properties or qualities by which male is distinguished from female; the physical difference between male and female; the distinguishing peculiarity of male or female.
     * Range: [BiologicalSexEnum](BiologicalSexEnum.md)
     * in subsets: (restricted)
 * [Individual➞karyotype](Individual_karyotype.md)  <sub>0..1</sub>
     * Description: The karyotype of an individual if defined.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [Individual➞age](Individual_age.md)  <sub>1..1</sub>
     * Description: Age of an individual.
     * Range: [AgeRangeEnum](AgeRangeEnum.md)
     * in subsets: (restricted)
 * [Individual➞vital_status](Individual_vital_status.md)  <sub>1..1</sub>
     * Description: Last known Vital Status of an Individual.
     * Range: [VitalStatusEnum](VitalStatusEnum.md)
     * in subsets: (restricted)
 * [Individual➞geographical_region](Individual_geographical_region.md)  <sub>0..1</sub>
     * Description: The geographical region where the Individual is located. Any demarcated area of the Earth; may be determined by both natural and human boundaries.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [Individual➞has_ancestry](Individual_has_ancestry.md)  <sub>0..\*</sub>
     * Description: A person's descent or lineage, from a person or from a population. Typically this is a value from HANCESTRO (Human Ancestry Ontology).
     * Range: [Ancestry](Ancestry.md)
     * in subsets: (restricted)
 * [Individual➞has_parent](Individual_has_parent.md)  <sub>0..\*</sub>
     * Description: One or more parent for this Individual.
     * Range: [Individual](Individual.md)
     * in subsets: (restricted)
 * [Individual➞has_children](Individual_has_children.md)  <sub>0..\*</sub>
     * Description: One or more children for this Individual.
     * Range: [Individual](Individual.md)
     * in subsets: (restricted)
 * [Individual➞has_disease](Individual_has_disease.md)  <sub>1..\*</sub>
     * Description: The Disease entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Mondo Disease Ontology. For example, 'MONDO:0003742' indicates that the Individual - from_which_the_Biospecimen was extracted from - suffers_from_'Heart_Fibrosarcoma'.
     * Range: [Disease](Disease.md)
 * [Individual➞has_phenotypic_feature](Individual_has_phenotypic_feature.md)  <sub>0..\*</sub>
     * Description: The Phenotypic Feature entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Human Phenotype Ontology. For example, 'HP:0100244' indicates that the Individual - from_which_the_Biospecimen was extracted from - exhibits_'Fibrosarcoma'_as_one_of_its_phenotype.
     * Range: [PhenotypicFeature](PhenotypicFeature.md)
     * in subsets: (restricted)
 * [Individual➞has_file](Individual_has_file.md)  <sub>0..\*</sub>
     * Description: Additional/supplementary files associated with an Individual. Typically, a phenopacket or pedigree file.
     * Range: [File](File.md)
     * in subsets: (restricted)

### Inherited from Person:

 * [NamedThing➞id](NamedThing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [NamedThing➞alias](NamedThing_alias.md)  <sub>1..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [NamedThing➞xref](NamedThing_xref.md)  <sub>0..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)
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

### Mixed in from AccessionMixin:

 * [AccessionMixin➞accession](AccessionMixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

### Mixed in from EgaAccessionMixin:

 * [EgaAccessionMixin➞ega_accession](EgaAccessionMixin_ega_accession.md)  <sub>1..1</sub>
     * Description: A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | subject |
|  | | patient |

