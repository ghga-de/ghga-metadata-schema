# Entity Relationship Diagrams

## Global Overview

An overview of the entire submission schema.  

```mermaid
erDiagram
Submission {

}
Publication {

}
Study {

}
Attribute {

}
Condition {

}
Project {

}
Member {

}
DataAccessCommittee {

}
DataAccessPolicy {

}
DataUseModifier {

}
DataUsePermission {

}
Dataset {

}
File {

}
Analysis {

}
Protocol {

}
SequencingExperiment {

}
LibraryPreparationProtocol {

}
SequencingProtocol {

}
Individual {

}
PhenotypicFeature {

}
Disease {

}
Ancestry {

}
Biospecimen {

}
AnatomicalEntity {

}
Sample {

}

Submission ||--|| Study : "has_study"
Submission ||--|o Project : "has_project"
Submission ||--}o Sample : "has_sample"
Submission ||--}o Biospecimen : "has_biospecimen"
Submission ||--}o Individual : "has_individual"
Submission ||--}o SequencingExperiment : "has_sequencing_experiment"
Submission ||--}o Protocol : "has_protocol"
Submission ||--}o Analysis : "has_analysis"
Submission ||--}| File : "has_file"
Submission ||--}| Dataset : "has_dataset"
Submission ||--}| DataAccessPolicy : "has_data_access_policy"
Submission ||--}| DataAccessCommittee : "has_data_access_committee"
Submission ||--}| Member : "has_member"
Submission ||--}o Publication : "has_publication"
Publication ||--|| Study : "has_study"
Study ||--|o Project : "has_project"
Study ||--}| Condition : "has_condition"
Study ||--}o Attribute : "has_attribute"
Condition ||--}o Attribute : "has_attribute"
Project ||--}o Attribute : "has_attribute"
DataAccessCommittee ||--|| Member : "main_contact"
DataAccessCommittee ||--}o Member : "has_member"
DataAccessCommittee ||--}o Attribute : "has_attribute"
DataAccessPolicy ||--|| DataAccessCommittee : "has_data_access_committee"
DataAccessPolicy ||--|| DataUsePermission : "has_data_use_permission"
DataAccessPolicy ||--}o DataUseModifier : "has_data_use_modifier"
DataAccessPolicy ||--}o Attribute : "has_attribute"
Dataset ||--}| File : "has_file"
Dataset ||--|o Publication : "has_publication"
Dataset ||--|| DataAccessPolicy : "has_data_access_policy"
Dataset ||--}o Attribute : "has_attribute"
File ||--}o Attribute : "has_attribute"
Analysis ||--}| File : "has_input"
Analysis ||--|| Study : "has_study"
Analysis ||--}| File : "has_output"
Protocol ||--}| Attribute : "has_attribute"
SequencingExperiment ||--|| SequencingProtocol : "has_sequencing_protocol"
SequencingExperiment ||--|| LibraryPreparationProtocol : "has_library_preparation_protocol"
SequencingExperiment ||--}o Attribute : "has_attribute"
LibraryPreparationProtocol ||--}| Attribute : "has_attribute"
SequencingProtocol ||--}| Attribute : "has_attribute"
Individual ||--}o Ancestry : "has_ancestry"
Individual ||--}o Individual : "has_parent"
Individual ||--}o Individual : "has_children"
Individual ||--}| Disease : "has_disease"
Individual ||--}o PhenotypicFeature : "has_phenotypic_feature"
Individual ||--}o File : "has_file"
Biospecimen ||--|| Individual : "has_individual"
Biospecimen ||--}| AnatomicalEntity : "has_anatomical_entity"
Sample ||--|o Biospecimen : "has_biospecimen"
Sample ||--|| Condition : "has_condition"
Sample ||--}o Attribute : "has_attribute"

```



## Sample, Biospecimen, & Individual

Focusses on the relation between Sample, Biospecimen, and Individual.  

```mermaid
erDiagram
Individual {

}
Biospecimen {

}
Sample {

}

Individual ||--}o Ancestry : "has_ancestry"
Individual ||--}o Individual : "has_parent"
Individual ||--}o Individual : "has_children"
Individual ||--}| Disease : "has_disease"
Individual ||--}o PhenotypicFeature : "has_phenotypic_feature"
Individual ||--}o File : "has_file"
Biospecimen ||--|| Individual : "has_individual"
Biospecimen ||--}| AnatomicalEntity : "has_anatomical_entity"
Sample ||--|o Biospecimen : "has_biospecimen"
Sample ||--|| Condition : "has_condition"
Sample ||--}o Attribute : "has_attribute"

```



## Experiment, Sample, & File

Focusses on the relation between Experiment, Sample, and File.  

```mermaid
erDiagram
SequencingProcess {

}
File {

}
Sample {

}
SequencingExperiment {

}

SequencingProcess ||--}| File : "has_file"
SequencingProcess ||--|| SequencingExperiment : "has_sequencing_experiment"
SequencingProcess ||--|| Sample : "has_sample"
SequencingProcess ||--}o Attribute : "has_attribute"
File ||--}o Attribute : "has_attribute"
Sample ||--|o Biospecimen : "has_biospecimen"
Sample ||--|| Condition : "has_condition"
Sample ||--}o Attribute : "has_attribute"
SequencingExperiment ||--|| SequencingProtocol : "has_sequencing_protocol"
SequencingExperiment ||--|| LibraryPreparationProtocol : "has_library_preparation_protocol"
SequencingExperiment ||--}o Attribute : "has_attribute"

```



## Study, Condition, & Sample

Focusses on the relation between Study, Condition, and Sample.  

```mermaid
erDiagram
Sample {

}
Condition {

}
Study {

}

Sample ||--|o Biospecimen : "has_biospecimen"
Sample ||--|| Condition : "has_condition"
Sample ||--}o Attribute : "has_attribute"
Condition ||--}o Attribute : "has_attribute"
Study ||--|o Project : "has_project"
Study ||--}| Condition : "has_condition"
Study ||--}o Attribute : "has_attribute"

```



## Sample, Biospecimen, & Individual (with attributes)

Focusses on the details of the relation between Sample, Biospecimen, and Individual.  

```mermaid
erDiagram
Individual {
    BiologicalSexEnum sex  
    string karyotype  
    AgeRangeEnum age  
    VitalStatusEnum vital_status  
    string geographical_region  
    string accession  
    string ega_accession  
    string given_name  
    string family_name  
    string additional_name  
    string id  
    string alias  
    stringList xref  
}
Biospecimen {
    string name  
    string type  
    string description  
    string isolation  
    string storage  
    VitalStatusEnum vital_status_at_sampling  
    string accession  
    string id  
    string alias  
    stringList xref  
}
Sample {
    string name  
    string type  
    string description  
    string isolation  
    string storage  
    string accession  
    string ega_accession  
    string id  
    string alias  
    stringList xref  
}

Individual ||--}o Ancestry : "has_ancestry"
Individual ||--}o Individual : "has_parent"
Individual ||--}o Individual : "has_children"
Individual ||--}| Disease : "has_disease"
Individual ||--}o PhenotypicFeature : "has_phenotypic_feature"
Individual ||--}o File : "has_file"
Biospecimen ||--|| Individual : "has_individual"
Biospecimen ||--}| AnatomicalEntity : "has_anatomical_entity"
Sample ||--|o Biospecimen : "has_biospecimen"
Sample ||--|| Condition : "has_condition"
Sample ||--}o Attribute : "has_attribute"

```


## Experiment, Sample, & File (with attributes)

Focusses on the relation between Experiment, Sample, and File.  

```mermaid
erDiagram
SequencingProcess {
    string name  
    string description  
    string sequencing_run_id  
    string sequencing_lane_id  
    string sequencing_machine_id  
    string accession  
    string title  
    string id  
    string alias  
    stringList xref  
}
File {
    string name  
    FileFormatEnum format  
    integer size  
    string checksum  
    string checksum_type  
    string accession  
    string ega_accession  
    string id  
    string alias  
    stringList xref  
}
Sample {
    string name  
    string type  
    string description  
    string isolation  
    string storage  
    string accession  
    string ega_accession  
    string id  
    string alias  
    stringList xref  
}
SequencingExperiment {
    string type  
    string accession  
    string ega_accession  
    string title  
    string description  
    string id  
    string alias  
    stringList xref  
}

SequencingProcess ||--}| File : "has_file"
SequencingProcess ||--|| SequencingExperiment : "has_sequencing_experiment"
SequencingProcess ||--|| Sample : "has_sample"
SequencingProcess ||--}o Attribute : "has_attribute"
File ||--}o Attribute : "has_attribute"
Sample ||--|o Biospecimen : "has_biospecimen"
Sample ||--|| Condition : "has_condition"
Sample ||--}o Attribute : "has_attribute"
SequencingExperiment ||--|| SequencingProtocol : "has_sequencing_protocol"
SequencingExperiment ||--|| LibraryPreparationProtocol : "has_library_preparation_protocol"
SequencingExperiment ||--}o Attribute : "has_attribute"

```


## Study, Condition, & Sample (with attributes)

Focusses on the relation between Study, Condition, and Sample.  

```mermaid
erDiagram
Sample {
    string name  
    string type  
    string description  
    string isolation  
    string storage  
    string accession  
    string ega_accession  
    string id  
    string alias  
    stringList xref  
}
Condition {
    string name  
    string description  
    DiseaseOrHealthyEnum disease_or_healthy  
    TreatmentOrControlEnum treatment_or_control  
    MutantOrWildtypeEnum mutant_or_wildtype  
    string accession  
    string title  
    string id  
    string alias  
    stringList xref  
}
Study {
    StudyTypeEnum type  
    stringList affiliation  
    string accession  
    string ega_accession  
    string title  
    string description  
    string id  
    string alias  
    stringList xref  
}

Sample ||--|o Biospecimen : "has_biospecimen"
Sample ||--|| Condition : "has_condition"
Sample ||--}o Attribute : "has_attribute"
Condition ||--}o Attribute : "has_attribute"
Study ||--|o Project : "has_project"
Study ||--}| Condition : "has_condition"
Study ||--}o Attribute : "has_attribute"

```
