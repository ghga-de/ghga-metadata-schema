# Entity Relationship Diagrams

## Global Overview

An overview of the entire submission schema.  

```mermaid
erDiagram
Submission {

}
Trio {

}
Individual {

}
StudyFile {

}
Dataset {

}
DataAccessPolicy {

}
DataAccessCommittee {

}
Study {

}
Attribute {

}
SequencingProtocol {

}
SequencingProcess {

}
Sample {

}
Condition {

}
Biospecimen {

}
SequencingExperiment {

}
LibraryPreparationProtocol {

}
SequencingProcessFile {

}
SampleFile {

}
Publication {

}
AnalysisProcess {

}
Analysis {

}
AnalysisProcessOutputFile {

}

Submission ||--}| Analysis : "analyses"
Submission ||--}| AnalysisProcessOutputFile : "analysis_process_output_files"
Submission ||--}| AnalysisProcess : "analysis_processes"
Submission ||--}| Biospecimen : "biospecimens"
Submission ||--}| Condition : "conditions"
Submission ||--}| DataAccessCommittee : "data_access_committees"
Submission ||--}| DataAccessPolicy : "data_access_policies"
Submission ||--}| Dataset : "datasets"
Submission ||--}| Individual : "individuals"
Submission ||--}| LibraryPreparationProtocol : "library_preparation_protocols"
Submission ||--}| Publication : "publications"
Submission ||--}| SampleFile : "sample_files"
Submission ||--}| Sample : "samples"
Submission ||--}| SequencingExperiment : "sequencing_experiments"
Submission ||--}| SequencingProcessFile : "sequencing_process_files"
Submission ||--}| SequencingProcess : "sequencing_processes"
Submission ||--}| SequencingProtocol : "sequencing_protocols"
Submission ||--}| Study : "studies"
Submission ||--}| StudyFile : "study_files"
Submission ||--}| Trio : "trios"
Trio ||--|| Individual : "mother"
Trio ||--|| Individual : "father"
Trio ||--|| Individual : "child"
StudyFile ||--|| Study : "study"
StudyFile ||--|| Dataset : "dataset"
Dataset ||--|| DataAccessPolicy : "data_access_policy"
DataAccessPolicy ||--|| DataAccessCommittee : "data_access_committee"
Study ||--}o Attribute : "attributes"
SequencingProtocol ||--}o Attribute : "attributes"
SequencingProcess ||--|| SequencingExperiment : "sequencing_experiment"
SequencingProcess ||--|| Sample : "sample"
SequencingProcess ||--}o Attribute : "attributes"
Sample ||--|o Biospecimen : "biospecimen"
Sample ||--|| Condition : "condition"
Sample ||--}o Attribute : "attributes"
Condition ||--|| Study : "study"
Condition ||--}o Attribute : "attributes"
Biospecimen ||--|| Individual : "individual"
SequencingExperiment ||--|| SequencingProtocol : "sequencing_protocol"
SequencingExperiment ||--|| LibraryPreparationProtocol : "library_preparation_protocol"
SequencingExperiment ||--}o Attribute : "attributes"
LibraryPreparationProtocol ||--}o Attribute : "attributes"
SequencingProcessFile ||--|| SequencingProcess : "sequencing_process"
SequencingProcessFile ||--|| Dataset : "dataset"
SampleFile ||--|| Sample : "sample"
SampleFile ||--|| Dataset : "dataset"
Publication ||--|| Study : "study"
AnalysisProcess ||--|| Analysis : "analysis"
AnalysisProcess ||--}| StudyFile : "study_input_files"
AnalysisProcess ||--}| SampleFile : "sample_input_files"
AnalysisProcess ||--}| SequencingProcessFile : "sequencing_process_input_files"
AnalysisProcessOutputFile ||--|| AnalysisProcess : "analysis_process"
AnalysisProcessOutputFile ||--|| Dataset : "dataset"

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

Biospecimen ||--|| Individual : "individual"
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
File ||--|| Dataset : "dataset"
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
Condition ||--|| Study : "study"
Condition ||--}o Attribute : "attributes"
Study ||--}o Attribute : "attributes"

```



## Sample, Biospecimen, & Individual (with attributes)

Focusses on the details of the relation between Sample, Biospecimen, and Individual.  

```mermaid
erDiagram
Individual {
    IndividualSexEnum sex  
    KaryotypeEnum karyotype  
    string geographical_region  
    stringList ancestries  
    stringList phenotypic_features  
    string alias  
}
Biospecimen {
    string name  
    string type  
    string description  
    string isolation  
    string storage  
    AgeRangeEnum age_at_sampling  
    VitalStatusEnum vital_status_at_sampling  
    string tissue  
    string alias  
}
Sample {
    string name  
    SampleTypeEnum type  
    string description  
    string isolation  
    string storage  
    stringList xref  
    string alias  
}

Biospecimen ||--|| Individual : "individual"
Sample ||--|o Biospecimen : "biospecimen"
Sample ||--|| Condition : "condition"
Sample ||--}o Attribute : "attributes"

```



## Experiment, Sample, & File (with attributes)

Focusses on the relation between Experiment, Sample, and File.  

```mermaid
erDiagram
SequencingProcess {
    string title  
    string description  
    string name  
    string sequencing_run_id  
    string sequencing_lane_id  
    string sequencing_machine_id  
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
    SampleTypeEnum type  
    string description  
    string isolation  
    string storage  
    stringList xref  
    string alias  
}
SequencingExperiment {
    string title  
    string description  
    string type  
    string alias  
}

SequencingProcess ||--|| SequencingExperiment : "sequencing_experiment"
SequencingProcess ||--|| Sample : "sample"
SequencingProcess ||--}o Attribute : "attributes"
File ||--|| Dataset : "dataset"
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
    SampleTypeEnum type  
    string description  
    string isolation  
    string storage  
    stringList xref  
    string alias  
}
Condition {
    string title  
    string description  
    string name  
    DiseaseOrHealthyEnum disease_or_healthy  
    CaseControlStatusEnum case_control_status  
    MutantOrWildtypeEnum mutant_or_wildtype  
    string alias  
}
Study {
    string title  
    string description  
    StudyTypeEnum type  
    stringList affiliations  
    string alias  
}

Sample ||--|o Biospecimen : "biospecimen"
Sample ||--|| Condition : "condition"
Sample ||--}o Attribute : "attributes"
Condition ||--|| Study : "study"
Condition ||--}o Attribute : "attributes"
Study ||--}o Attribute : "attributes"

```

