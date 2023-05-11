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
AnalysisProcessOutputFile {

}
AnalysisProcess {

}
SequencingProcessFile {

}
SequencingProcess {

}
Sample {

}
Biospecimen {

}
AnatomicalEntity {

}
Individual {

}
PhenotypicFeature {

}
Disease {

}
Ancestry {

}
SequencingExperiment {

}
LibraryPreparationProtocol {

}
SequencingProtocol {

}
Analysis {

}
SampleFile {

}
StudyFile {

}

Submission ||--}| Study : "studies"
Submission ||--}o Sample : "samples"
Submission ||--}o Biospecimen : "biospecimens"
Submission ||--}o Individual : "individuals"
Submission ||--}o SequencingExperiment : "sequencing_experiments"
Submission ||--}o SequencingProtocol : "sequencing_protocols"
Submission ||--}o LibraryPreparationProtocol : "library_preparation_protocols"
Submission ||--}o Analysis : "analyses"
Submission ||--}| StudyFile : "study_files"
Submission ||--}| SampleFile : "sample_files"
Submission ||--}| SequencingProcessFile : "sequencing_process_files"
Submission ||--}| AnalysisProcessOutputFile : "analysis_process_output_files"
Submission ||--}| Dataset : "datasets"
Submission ||--}| DataAccessPolicy : "data_access_policies"
Submission ||--}| DataAccessCommittee : "data_access_committees"
Submission ||--}| Member : "members"
Submission ||--}o Publication : "publications"
Publication ||--|| Study : "study"
Study ||--}| Condition : "conditions"
Study ||--}o Attribute : "attributes"
Condition ||--}o Attribute : "attributes"
DataAccessCommittee ||--|| Member : "main_contact"
DataAccessCommittee ||--}o Member : "members"
DataAccessCommittee ||--}o Attribute : "attributes"
DataAccessPolicy ||--|| DataAccessCommittee : "data_access_committee"
DataAccessPolicy ||--|| DataUsePermission : "data_use_permission"
DataAccessPolicy ||--|o DataUseModifier : "data_use_modifiers"
DataAccessPolicy ||--}o Attribute : "attributes"
Dataset ||--}| File : "files"
Dataset ||--|| DataAccessPolicy : "data_access_policy"
Dataset ||--}o Attribute : "attributes"
File ||--}o Attribute : "attributes"
AnalysisProcessOutputFile ||--|| AnalysisProcess : "analysis_process"
AnalysisProcessOutputFile ||--}o Attribute : "attributes"
AnalysisProcess ||--|| Analysis : "analysis"
AnalysisProcess ||--}| SequencingProcessFile : "sequencing_process_files"
SequencingProcessFile ||--|| SequencingProcess : "sequencing_process"
SequencingProcessFile ||--}o Attribute : "attributes"
SequencingProcess ||--|| SequencingExperiment : "sequencing_experiment"
SequencingProcess ||--|| Sample : "sample"
SequencingProcess ||--}o Attribute : "attributes"
Sample ||--|o Biospecimen : "biospecimen"
Sample ||--|| Condition : "condition"
Sample ||--}o Attribute : "attributes"
Biospecimen ||--|| Individual : "individual"
Biospecimen ||--}| AnatomicalEntity : "anatomical_entities"
Individual ||--}o Ancestry : "ancestries"
Individual ||--}o Individual : "parents"
Individual ||--}o Individual : "children"
Individual ||--}| Disease : "diseases"
Individual ||--}o PhenotypicFeature : "phenotypic_features"
Individual ||--}o File : "files"
SequencingExperiment ||--|| SequencingProtocol : "sequencing_protocol"
SequencingExperiment ||--|| LibraryPreparationProtocol : "library_preparation_protocol"
SequencingExperiment ||--}o Attribute : "attributes"
LibraryPreparationProtocol ||--}| Attribute : "attributes"
SequencingProtocol ||--}| Attribute : "attributes"
Analysis ||--}o File : "inputs"
Analysis ||--|| Study : "study"
Analysis ||--}o File : "outputs"
SampleFile ||--|| Sample : "sample"
SampleFile ||--}o Attribute : "attributes"
StudyFile ||--|| Study : "study"
StudyFile ||--}o Attribute : "attributes"

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

Individual ||--}o Ancestry : "ancestries"
Individual ||--}o Individual : "parents"
Individual ||--}o Individual : "children"
Individual ||--}| Disease : "diseases"
Individual ||--}o PhenotypicFeature : "phenotypic_features"
Individual ||--}o File : "files"
Biospecimen ||--|| Individual : "individual"
Biospecimen ||--}| AnatomicalEntity : "anatomical_entities"
Sample ||--|o Biospecimen : "biospecimen"
Sample ||--|| Condition : "condition"
Sample ||--}o Attribute : "attributes"

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

SequencingProcess ||--|| SequencingExperiment : "sequencing_experiment"
SequencingProcess ||--|| Sample : "sample"
SequencingProcess ||--}o Attribute : "attributes"
File ||--}o Attribute : "attributes"
Sample ||--|o Biospecimen : "biospecimen"
Sample ||--|| Condition : "condition"
Sample ||--}o Attribute : "attributes"
SequencingExperiment ||--|| SequencingProtocol : "sequencing_protocol"
SequencingExperiment ||--|| LibraryPreparationProtocol : "library_preparation_protocol"
SequencingExperiment ||--}o Attribute : "attributes"

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

Sample ||--|o Biospecimen : "biospecimen"
Sample ||--|| Condition : "condition"
Sample ||--}o Attribute : "attributes"
Condition ||--}o Attribute : "attributes"
Study ||--}| Condition : "conditions"
Study ||--}o Attribute : "attributes"

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
    string given_name  
    string family_name  
    string additional_name  
    string alias  
}
Biospecimen {
    string name  
    string type  
    string description  
    string isolation  
    string storage  
    VitalStatusEnum vital_status_at_sampling  
    string alias  
}
Sample {
    string name  
    string type  
    string description  
    string isolation  
    string storage  
    stringList xref  
    string alias  
}

Individual ||--}o Ancestry : "ancestries"
Individual ||--}o Individual : "parents"
Individual ||--}o Individual : "children"
Individual ||--}| Disease : "diseases"
Individual ||--}o PhenotypicFeature : "phenotypic_features"
Individual ||--}o File : "files"
Biospecimen ||--|| Individual : "individual"
Biospecimen ||--}| AnatomicalEntity : "anatomical_entities"
Sample ||--|o Biospecimen : "biospecimen"
Sample ||--|| Condition : "condition"
Sample ||--}o Attribute : "attributes"

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
    string title  
    string alias  
}
File {
    string name  
    FileFormatEnum format  
    integer size  
    string checksum  
    string checksum_type  
    string alias  
}
Sample {
    string name  
    string type  
    string description  
    string isolation  
    string storage  
    stringList xref  
    string alias  
}
SequencingExperiment {
    string type  
    string title  
    string description  
    string alias  
}

SequencingProcess ||--|| SequencingExperiment : "sequencing_experiment"
SequencingProcess ||--|| Sample : "sample"
SequencingProcess ||--}o Attribute : "attributes"
File ||--}o Attribute : "attributes"
Sample ||--|o Biospecimen : "biospecimen"
Sample ||--|| Condition : "condition"
Sample ||--}o Attribute : "attributes"
SequencingExperiment ||--|| SequencingProtocol : "sequencing_protocol"
SequencingExperiment ||--|| LibraryPreparationProtocol : "library_preparation_protocol"
SequencingExperiment ||--}o Attribute : "attributes"

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
    stringList xref  
    string alias  
}
Condition {
    string name  
    string description  
    DiseaseOrHealthyEnum disease_or_healthy  
    TreatmentOrControlEnum treatment_or_control  
    MutantOrWildtypeEnum mutant_or_wildtype  
    string title  
    string alias  
}
Study {
    StudyTypeEnum type  
    stringList affiliations  
    string title  
    string description  
    string alias  
}

Sample ||--|o Biospecimen : "biospecimen"
Sample ||--|| Condition : "condition"
Sample ||--}o Attribute : "attributes"
Condition ||--}o Attribute : "attributes"
Study ||--}| Condition : "conditions"
Study ||--}o Attribute : "attributes"

```

