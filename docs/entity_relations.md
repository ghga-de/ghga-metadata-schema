# Entity Relationship Diagrams

## Global Overview

An overview of the entire submission schema.  

```mermaid
erDiagram
Submission {

}
SupportingFile {

}
Dataset {

}
DataAccessPolicy {

}
DataAccessCommittee {

}
ProcessDataFile {

}
ResearchDataFile {

}
Study {

}
Attribute {

}
ExperimentalMethod {

}
Experiment {

}
Sample {

}
Individual {

}
Publication {

}
AnalysisMethod {

}
Analysis {

}

Submission ||--}| Analysis : "analyses"
Submission ||--}| AnalysisMethod : "analysis_methods"
Submission ||--}| DataAccessCommittee : "data_access_committees"
Submission ||--}| DataAccessPolicy : "data_access_policies"
Submission ||--}| Dataset : "datasets"
Submission ||--}| Individual : "individuals"
Submission ||--}| Publication : "publications"
Submission ||--}| Sample : "samples"
Submission ||--}| Experiment : "experiments"
Submission ||--}| ExperimentalMethod : "experimental_methods"
Submission ||--}| Study : "studies"
Submission ||--}| ResearchDataFile : "research_data_files"
Submission ||--}o ProcessDataFile : "process_data_files"
Submission ||--}o SupportingFile : "supporting_files"
SupportingFile ||--|| Dataset : "dataset"
Dataset ||--|| DataAccessPolicy : "data_access_policy"
DataAccessPolicy ||--|| DataAccessCommittee : "data_access_committee"
ProcessDataFile ||--|| Dataset : "dataset"
ResearchDataFile ||--|| Dataset : "dataset"
Study ||--}o Attribute : "attributes"
ExperimentalMethod ||--}o Attribute : "attributes"
ExperimentalMethod ||--}o SupportingFile : "supporting_files"
Experiment ||--}| Sample : "samples"
Experiment ||--}| ResearchDataFile : "research_data_files"
Experiment ||--}| ExperimentalMethod : "experimental_methods"
Experiment ||--}o Attribute : "attributes"
Sample ||--|| Individual : "individual"
Sample ||--}o Attribute : "attributes"
Individual ||--}o SupportingFile : "supporting_files"
Publication ||--|| Study : "study"
Analysis ||--}| ResearchDataFile : "research_data_files"
Analysis ||--}| ProcessDataFile : "process_data_files"
Analysis ||--}| AnalysisMethod : "analysis_methods"

```



## Sample & Individual

Focusses on the relation between Sample and Individual.  

```mermaid
erDiagram
Individual {

}
Sample {

}

Individual ||--}o SupportingFile : "supporting_files"
Sample ||--|| Individual : "individual"
Sample ||--}o Attribute : "attributes"

```



## Experiment, Sample, & File

Focusses on the relation between Experiment, Sample, and File.  

```mermaid
erDiagram
ExperimentalMethod {

}
ResearchDataFile {

}
Sample {

}
Experiment {

}

ExperimentalMethod ||--}o Attribute : "attributes"
ExperimentalMethod ||--}o SupportingFile : "supporting_files"
ResearchDataFile ||--|| Dataset : "dataset"
Sample ||--|| Individual : "individual"
Sample ||--}o Attribute : "attributes"
Experiment ||--}| Sample : "samples"
Experiment ||--}| ResearchDataFile : "research_data_files"
Experiment ||--}| ExperimentalMethod : "experimental_methods"
Experiment ||--}o Attribute : "attributes"

```



## Sample & Individual (with attributes)

Focusses on the details of the relation between Sample, Biospecimen, and Individual.  

```mermaid
erDiagram
Individual {
    stringList phenotypic_features  
    stringList diagnosis  
    IndividualSexEnum sex  
    string geographical_region  
    stringList ancestries  
    string alias  
}
Sample {
    string name  
    SampleTypeEnum type  
    string biological_replicate  
    string description  
    StorageEnum storage  
    DiseaseOrHealthyEnum disease_or_healthy  
    CaseControlStatusEnum case_control_status  
    stringList xref  
    string biospecimen_name  
    string biospecimen_type  
    string biospecimen_description  
    AgeRangeEnum biospecimen_age_at_sampling  
    VitalStatusEnum biospecimen_vital_status_at_sampling  
    string biospecimen_tissue  
    string biospecimen_isolation  
    StorageEnum biospecimen_storage  
    string alias  
}

Individual ||--}o SupportingFile : "supporting_files"
Sample ||--|| Individual : "individual"
Sample ||--}o Attribute : "attributes"

```



## Experiment, Sample, & File (with attributes)

Focusses on the relation between Experiment, Sample, and File.  

```mermaid
erDiagram
ExperimentalMethod {
    string name  
    string description  
    string type  
    LibraryPreparationLibrarySelectionEnumList library_selection_methods  
    string library_preparation  
    LibraryPreparationKitRetailNameEnum library_preparation_kit_retail_name  
    string library_preparation_kit_manufacturer  
    PrimerEnum primer  
    EndBiasEnum end_bias  
    stringList target_regions  
    LibraryPreparationRNASeqStrandednessEnum rnaseq_strandedness  
    InstrumentModelEnum instrument_model  
    string sequencing_center  
    string sequencing_read_length  
    SequencingProtocolSequencingLayoutEnum sequencing_layout  
    string target_coverage  
    string flow_cell_id  
    FlowCellTypeEnum flow_cell_type  
    SampleBarcodeReadEnum sample_barcode_read  
    string alias  
}
ResearchDataFile {
    ResearchDataFileFormatEnum format  
    string technical_replicate  
    string name  
    integer size  
    string checksum  
    string checksum_type  
    string alias  
}
Sample {
    string name  
    SampleTypeEnum type  
    string biological_replicate  
    string description  
    StorageEnum storage  
    DiseaseOrHealthyEnum disease_or_healthy  
    CaseControlStatusEnum case_control_status  
    stringList xref  
    string biospecimen_name  
    string biospecimen_type  
    string biospecimen_description  
    AgeRangeEnum biospecimen_age_at_sampling  
    VitalStatusEnum biospecimen_vital_status_at_sampling  
    string biospecimen_tissue  
    string biospecimen_isolation  
    StorageEnum biospecimen_storage  
    string alias  
}
Experiment {
    string title  
    string description  
    string type  
    string alias  
}

ExperimentalMethod ||--}o Attribute : "attributes"
ExperimentalMethod ||--}o SupportingFile : "supporting_files"
ResearchDataFile ||--|| Dataset : "dataset"
Sample ||--|| Individual : "individual"
Sample ||--}o Attribute : "attributes"
Experiment ||--}| Sample : "samples"
Experiment ||--}| ResearchDataFile : "research_data_files"
Experiment ||--}| ExperimentalMethod : "experimental_methods"
Experiment ||--}o Attribute : "attributes"

```

