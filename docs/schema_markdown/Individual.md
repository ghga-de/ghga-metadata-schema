
# Class: individual


An Individual is a Person who is participating in a Study.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Individual](https://w3id.org/GHGA-Submission-Metadata-Schema/Individual)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample],[PhenotypicFeature],[Person],[File]<has%20file%200..*-++[Individual&#124;sex:biological_sex_enum;karyotype:string%20%3F;age:age_range_enum;vital_status:vital_status_enum;geographical_region:string%20%3F;accession:string;ega_accession:string;given_name(i):string%20%3F;family_name(i):string%20%3F;additional_name(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[PhenotypicFeature]<has%20phenotypic%20feature%200..*-++[Individual],[Disease]<has%20disease%201..*-++[Individual],[Individual]<has%20children%200..*-++[Individual],[Individual]<has%20parent%200..*-++[Individual],[Ancestry]<has%20ancestry%200..*-++[Individual],[Biospecimen]++-%20has%20individual%201..1>[Individual],[Biospecimen]-%20has%20individual(i)%200..1>[Individual],[Sample]-%20has%20individual(i)%200..1>[Individual],[Submission]-%20has%20individual(i)%200..1>[Individual],[Sample]++-%20has%20individual%201..1>[Individual],[Submission]++-%20has%20individual%200..*>[Individual],[Individual]uses%20-.->[AccessionMixin],[Individual]uses%20-.->[EgaAccessionMixin],[Person]^-[Individual],[File],[EgaAccessionMixin],[Disease],[Biospecimen],[Ancestry],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample],[PhenotypicFeature],[Person],[File]<has%20file%200..*-++[Individual&#124;sex:biological_sex_enum;karyotype:string%20%3F;age:age_range_enum;vital_status:vital_status_enum;geographical_region:string%20%3F;accession:string;ega_accession:string;given_name(i):string%20%3F;family_name(i):string%20%3F;additional_name(i):string%20%3F;id(i):string;alias(i):string;xref(i):string%20*],[PhenotypicFeature]<has%20phenotypic%20feature%200..*-++[Individual],[Disease]<has%20disease%201..*-++[Individual],[Individual]<has%20children%200..*-++[Individual],[Individual]<has%20parent%200..*-++[Individual],[Ancestry]<has%20ancestry%200..*-++[Individual],[Biospecimen]++-%20has%20individual%201..1>[Individual],[Biospecimen]-%20has%20individual(i)%200..1>[Individual],[Sample]-%20has%20individual(i)%200..1>[Individual],[Submission]-%20has%20individual(i)%200..1>[Individual],[Sample]++-%20has%20individual%201..1>[Individual],[Submission]++-%20has%20individual%200..*>[Individual],[Individual]uses%20-.->[AccessionMixin],[Individual]uses%20-.->[EgaAccessionMixin],[Person]^-[Individual],[File],[EgaAccessionMixin],[Disease],[Biospecimen],[Ancestry],[AccessionMixin])

## Parents

 *  is_a: [Person](Person.md) - A member of the species Homo sapiens.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an EGA accession, in addition to GHGA accession.

## Referenced by Class

 *  **[Biospecimen](Biospecimen.md)** *[biospecimen➞has individual](biospecimen_has_individual.md)*  <sub>1..1</sub>  **[Individual](Individual.md)**
 *  **None** *[has individual](has_individual.md)*  <sub>0..1</sub>  **[Individual](Individual.md)**
 *  **[Individual](Individual.md)** *[individual➞has children](individual_has_children.md)*  <sub>0..\*</sub>  **[Individual](Individual.md)**
 *  **[Individual](Individual.md)** *[individual➞has parent](individual_has_parent.md)*  <sub>0..\*</sub>  **[Individual](Individual.md)**
 *  **[Sample](Sample.md)** *[sample➞has individual](sample_has_individual.md)*  <sub>1..1</sub>  **[Individual](Individual.md)**
 *  **[Submission](Submission.md)** *[submission➞has individual](submission_has_individual.md)*  <sub>0..\*</sub>  **[Individual](Individual.md)**

## Attributes


### Own

 * [individual➞sex](individual_sex.md)  <sub>1..1</sub>
     * Description: The assemblage of physical properties or qualities by which male is distinguished from female; the physical difference between male and female; the distinguishing peculiarity of male or female.
     * Range: [biological sex enum](biological sex enum.md)
     * in subsets: (restricted)
 * [individual➞karyotype](individual_karyotype.md)  <sub>0..1</sub>
     * Description: The karyotype of an individual if defined.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [individual➞age](individual_age.md)  <sub>1..1</sub>
     * Description: Age of an individual.
     * Range: [age range enum](age range enum.md)
     * in subsets: (restricted)
 * [individual➞vital status](individual_vital_status.md)  <sub>1..1</sub>
     * Description: Last known Vital Status of an Individual.
     * Range: [vital status enum](vital status enum.md)
     * in subsets: (restricted)
 * [individual➞geographical region](individual_geographical_region.md)  <sub>0..1</sub>
     * Description: The geographical region where the Individual is located. Any demarcated area of the Earth; may be determined by both natural and human boundaries.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [individual➞has ancestry](individual_has_ancestry.md)  <sub>0..\*</sub>
     * Description: A person's descent or lineage, from a person or from a population. Typically this is a value from HANCESTRO (Human Ancestry Ontology).
     * Range: [Ancestry](Ancestry.md)
     * in subsets: (restricted)
 * [individual➞has parent](individual_has_parent.md)  <sub>0..\*</sub>
     * Description: One or more parent for this Individual.
     * Range: [Individual](Individual.md)
     * in subsets: (restricted)
 * [individual➞has children](individual_has_children.md)  <sub>0..\*</sub>
     * Description: One or more children for this Individual.
     * Range: [Individual](Individual.md)
     * in subsets: (restricted)
 * [individual➞has disease](individual_has_disease.md)  <sub>1..\*</sub>
     * Description: The Disease entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Mondo Disease Ontology. For example, 'MONDO:0003742' indicates that the Individual - from which the Biospecimen was extracted from - suffers from 'Heart Fibrosarcoma'.
     * Range: [Disease](Disease.md)
 * [individual➞has phenotypic feature](individual_has_phenotypic_feature.md)  <sub>0..\*</sub>
     * Description: The Phenotypic Feature entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Human Phenotype Ontology. For example, 'HP:0100244' indicates that the Individual - from which the Biospecimen was extracted from - exhibits 'Fibrosarcoma' as one of its phenotype.
     * Range: [PhenotypicFeature](PhenotypicFeature.md)
     * in subsets: (restricted)
 * [individual➞has file](individual_has_file.md)  <sub>0..\*</sub>
     * Description: Additional/supplementary files associated with an Individual. Typically, a phenopacket or pedigree file.
     * Range: [File](File.md)
     * in subsets: (restricted)

### Inherited from person:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞alias](named_thing_alias.md)  <sub>1..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞xref](named_thing_xref.md)  <sub>0..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)
 * [person➞given name](person_given_name.md)  <sub>0..1</sub>
     * Description: First name.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [person➞family name](person_family_name.md)  <sub>0..1</sub>
     * Description: Last name.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [person➞additional name](person_additional_name.md)  <sub>0..1</sub>
     * Description: Additional name(s).
     * Range: [String](types/String.md)
     * in subsets: (restricted)

### Mixed in from accession mixin:

 * [accession mixin➞accession](accession_mixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

### Mixed in from ega accession mixin:

 * [ega accession mixin➞ega accession](ega_accession_mixin_ega_accession.md)  <sub>1..1</sub>
     * Description: A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | subject |
|  | | patient |

