
# Class: biospecimen


A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics, treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is derived.

URI: [GHGA:Biospecimen](https://w3id.org/GHGA/Biospecimen)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample],[PhenotypicFeature],[MaterialEntity],[Individual],[Disease],[PhenotypicFeature]<has%20phenotypic%20feature%200..*-++[Biospecimen&#124;name:string%20%3F;type:string%20%3F;description:string%20%3F;isolation:string%20%3F;storage:string%20%3F;alias:string;accession:string%20%3F;id(i):string;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Disease]<has%20disease%200..*-++[Biospecimen],[AnatomicalEntity]<has%20anatomical%20entity%200..*-++[Biospecimen],[Individual]<has%20individual%200..1-++[Biospecimen],[Sample]-%20has%20biospecimen(i)%200..1>[Biospecimen],[Submission]-%20has%20biospecimen(i)%200..1>[Biospecimen],[Sample]++-%20has%20biospecimen%200..1>[Biospecimen],[Submission]++-%20has%20biospecimen%200..*>[Biospecimen],[Biospecimen]uses%20-.->[AccessionMixin],[MaterialEntity]^-[Biospecimen],[AnatomicalEntity],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Sample],[PhenotypicFeature],[MaterialEntity],[Individual],[Disease],[PhenotypicFeature]<has%20phenotypic%20feature%200..*-++[Biospecimen&#124;name:string%20%3F;type:string%20%3F;description:string%20%3F;isolation:string%20%3F;storage:string%20%3F;alias:string;accession:string%20%3F;id(i):string;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Disease]<has%20disease%200..*-++[Biospecimen],[AnatomicalEntity]<has%20anatomical%20entity%200..*-++[Biospecimen],[Individual]<has%20individual%200..1-++[Biospecimen],[Sample]-%20has%20biospecimen(i)%200..1>[Biospecimen],[Submission]-%20has%20biospecimen(i)%200..1>[Biospecimen],[Sample]++-%20has%20biospecimen%200..1>[Biospecimen],[Submission]++-%20has%20biospecimen%200..*>[Biospecimen],[Biospecimen]uses%20-.->[AccessionMixin],[MaterialEntity]^-[Biospecimen],[AnatomicalEntity],[AccessionMixin])

## Parents

 *  is_a: [MaterialEntity](MaterialEntity.md) - A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.

## Uses Mixin

 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.

## Referenced by Class

 *  **None** *[has biospecimen](has_biospecimen.md)*  <sub>0..1</sub>  **[Biospecimen](Biospecimen.md)**
 *  **[Sample](Sample.md)** *[sample➞has biospecimen](sample_has_biospecimen.md)*  <sub>0..1</sub>  **[Biospecimen](Biospecimen.md)**
 *  **[Submission](Submission.md)** *[submission➞has biospecimen](submission_has_biospecimen.md)*  <sub>0..\*</sub>  **[Biospecimen](Biospecimen.md)**

## Attributes


### Own

 * [name](name.md)  <sub>0..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [biospecimen➞type](biospecimen_type.md)  <sub>0..1</sub>
     * Description: The type of Biospecimen.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [description](description.md)  <sub>0..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [isolation](isolation.md)  <sub>0..1</sub>
     * Description: Method or device employed for collecting/isolating a biospecimen or a sample.
     * Range: [String](types/String.md)
     * in subsets: (recommended,public)
 * [storage](storage.md)  <sub>0..1</sub>
     * Description: Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).
     * Range: [String](types/String.md)
     * in subsets: (recommended,public)
 * [biospecimen➞has individual](biospecimen_has_individual.md)  <sub>0..1</sub>
     * Description: The Individual entity from which this Biospecimen was derived.
     * Range: [Individual](Individual.md)
     * in subsets: (essential,restricted)
 * [biospecimen➞has anatomical entity](biospecimen_has_anatomical_entity.md)  <sub>0..\*</sub>
     * Description: The Anatomical entity, that represents the site, from which the Biospecimen was retrieved. Typically, a concept from Uber-anatomy Ontology (UBERON). For example, 'UBERON:0008307' indicates that the Biospecimen was extracted from the 'Heart Endothelium' of an Individual.
     * Range: [AnatomicalEntity](AnatomicalEntity.md)
     * in subsets: (recommended,public)
 * [biospecimen➞has disease](biospecimen_has_disease.md)  <sub>0..\*</sub>
     * Description: The Disease entity that is associated with the Individual. Typically, a concept from Mondo Disease Ontology. For example, 'MONDO:0005267' indicates that the Individual suffers from 'Heart Disease'.
     * Range: [Disease](Disease.md)
     * in subsets: (essential,public)
 * [biospecimen➞has phenotypic feature](biospecimen_has_phenotypic_feature.md)  <sub>0..\*</sub>
     * Description: The Phenotypic Feature entity that is associated with the Individual. Typically, a concept from Human Phenotype Ontology. For example, 'HP:0100244' indicates that the Individual exhibits 'Fibrosarcoma' as one of its phenotype.
     * Range: [PhenotypicFeature](PhenotypicFeature.md)
     * in subsets: (essential,restricted)
 * [biospecimen➞alias](biospecimen_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)

### Inherited from material entity:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
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

### Mixed in from accession mixin:

 * [accession](accession.md)  <sub>0..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | OBI:0100051 |

