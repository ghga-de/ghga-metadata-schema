# Entity Relationship Diagrams

## Global Overview

An overview of the entire submission schema.  

```mermaid
erDiagram
Submission {

}
IndividualSupportingFile {

}
Dataset {

}
Study {

}
Attribute {

}
DataAccessPolicy {

}
DataAccessCommittee {

}
Individual {

}
AnalysisMethodSupportingFile {

}
AnalysisMethod {

}
ExperimentMethodSupportingFile {

}
ExperimentMethod {

}
ProcessDataFile {

}
Analysis {

}
ResearchDataFile {

}
Experiment {

}
Sample {

}
Publication {

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
Submission ||--}| ExperimentMethod : "experiment_methods"
Submission ||--}| Study : "studies"
Submission ||--}| ResearchDataFile : "research_data_files"
Submission ||--}o ProcessDataFile : "process_data_files"
Submission ||--}o ExperimentMethodSupportingFile : "experiment_method_supporting_files"
Submission ||--}o AnalysisMethodSupportingFile : "analysis_method_supporting_files"
Submission ||--}o IndividualSupportingFile : "individual_supporting_files"
IndividualSupportingFile ||--|| Individual : "individual"
IndividualSupportingFile ||--|| Dataset : "dataset"
Dataset ||--|| DataAccessPolicy : "data_access_policy"
Dataset ||--|| Study : "study"
Study ||--}o Attribute : "attributes"
DataAccessPolicy ||--|| DataAccessCommittee : "data_access_committee"
AnalysisMethodSupportingFile ||--|| AnalysisMethod : "analysis_method"
AnalysisMethodSupportingFile ||--|| Dataset : "dataset"
AnalysisMethod ||--}o Attribute : "parameters"
AnalysisMethod ||--}o Attribute : "software_versions"
ExperimentMethodSupportingFile ||--|| ExperimentMethod : "experiment_method"
ExperimentMethodSupportingFile ||--|| Dataset : "dataset"
ExperimentMethod ||--}o Attribute : "attributes"
ProcessDataFile ||--|| Analysis : "analysis"
ProcessDataFile ||--|| Dataset : "dataset"
Analysis ||--|| AnalysisMethod : "analysis_method"
Analysis ||--}| ResearchDataFile : "research_data_files"
ResearchDataFile ||--}| Experiment : "experiment"
ResearchDataFile ||--|| Dataset : "dataset"
Experiment ||--|| ExperimentMethod : "experiment_method"
Experiment ||--|| Sample : "sample"
Experiment ||--}o Attribute : "attributes"
Sample ||--|| Individual : "individual"
Sample ||--}o Attribute : "attributes"
Publication ||--|| Study : "study"

```



## Sample & Individual

Focusses on the relation between Sample and Individual.  

```mermaid
erDiagram
Individual {

}
Sample {

}

Sample ||--|| Individual : "individual"
Sample ||--}o Attribute : "attributes"

```



## Experiment, Sample, & File

Focusses on the relation between Experiment, Sample, and File.  

```mermaid
erDiagram
ExperimentMethodSupportingFile {

}
ExperimentMethod {

}
ResearchDataFile {

}
Sample {

}
Experiment {

}

ExperimentMethodSupportingFile ||--|| ExperimentMethod : "experiment_method"
ExperimentMethodSupportingFile ||--|| Dataset : "dataset"
ExperimentMethod ||--}o Attribute : "attributes"
ResearchDataFile ||--}| Experiment : "experiment"
ResearchDataFile ||--|| Dataset : "dataset"
Sample ||--|| Individual : "individual"
Sample ||--}o Attribute : "attributes"
Experiment ||--|| ExperimentMethod : "experiment_method"
Experiment ||--|| Sample : "sample"
Experiment ||--}o Attribute : "attributes"

```



## Sample & Individual (with attributes)

Focusses on the details of the relation between Sample, Biospecimen, and Individual.  

```mermaid
erDiagram
Individual {
    stringList phenotypic_features_terms  
    stringList phenotypic_features_ids  
    stringList diagnosis_ids  
    stringList diagnosis_terms  
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
    string ega_accession  
    stringList xref  
    string biospecimen_name  
    string biospecimen_type  
    string biospecimen_description  
    AgeRangeEnum biospecimen_age_at_sampling  
    VitalStatusEnum biospecimen_vital_status_at_sampling  
    string biospecimen_tissue_term  
    string biospecimen_tissue_id  
    IsolationEnum biospecimen_isolation  
    StorageEnum biospecimen_storage  
    string alias  
}

Sample ||--|| Individual : "individual"
Sample ||--}o Attribute : "attributes"

```



## Experiment, Sample, & File (with attributes)

Focusses on the relation between Experiment, Sample, and File.  

```mermaid
erDiagram
ExperimentMethodSupportingFile {
    SupportingFileFormatEnum format  
    string name  
    integer size  
    string checksum  
    string checksum_type  
    string alias  
}
ExperimentMethod {
    string name  
    string description  
    string type  
    LibraryPreparationLibraryTypeEnum library_type  
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
    string ega_accession  
    string alias  
}
ResearchDataFile {
    ResearchDataFileFormatEnum format  
    string technical_replicate  
    string sequencing_lane_id  
    PseudofileEnum is_pseudofile  
    string ega_accession  
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
    string ega_accession  
    stringList xref  
    string biospecimen_name  
    string biospecimen_type  
    string biospecimen_description  
    AgeRangeEnum biospecimen_age_at_sampling  
    VitalStatusEnum biospecimen_vital_status_at_sampling  
    string biospecimen_tissue_term  
    string biospecimen_tissue_id  
    IsolationEnum biospecimen_isolation  
    StorageEnum biospecimen_storage  
    string alias  
}
Experiment {
    string title  
    string description  
    string type  
    string ega_accession  
    string alias  
}

ExperimentMethodSupportingFile ||--|| ExperimentMethod : "experiment_method"
ExperimentMethodSupportingFile ||--|| Dataset : "dataset"
ExperimentMethod ||--}o Attribute : "attributes"
ResearchDataFile ||--}| Experiment : "experiment"
ResearchDataFile ||--|| Dataset : "dataset"
Sample ||--|| Individual : "individual"
Sample ||--}o Attribute : "attributes"
Experiment ||--|| ExperimentMethod : "experiment_method"
Experiment ||--|| Sample : "sample"
Experiment ||--}o Attribute : "attributes"

```

