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

Submission ||--|| Study : "has study"
Submission ||--|o Project : "has project"
Submission ||--}o Sample : "has sample"
Submission ||--}o Biospecimen : "has biospecimen"
Submission ||--}o Individual : "has individual"
Submission ||--}o SequencingExperiment : "has sequencing experiment"
Submission ||--}o Protocol : "has protocol"
Submission ||--}o Analysis : "has analysis"
Submission ||--}| File : "has file"
Submission ||--}| Dataset : "has dataset"
Submission ||--}| DataAccessPolicy : "has data access policy"
Submission ||--}| DataAccessCommittee : "has data access committee"
Submission ||--}| Member : "has member"
Submission ||--}o Publication : "has publication"
Publication ||--|| Study : "has study"
Study ||--|o Project : "has project"
Study ||--}| Condition : "has condition"
Study ||--}o Attribute : "has attribute"
Condition ||--}o Attribute : "has attribute"
Project ||--}o Attribute : "has attribute"
DataAccessCommittee ||--|| Member : "main contact"
DataAccessCommittee ||--}o Member : "has member"
DataAccessCommittee ||--}o Attribute : "has attribute"
DataAccessPolicy ||--|| DataAccessCommittee : "has data access committee"
DataAccessPolicy ||--|| DataUsePermission : "has data use permission"
DataAccessPolicy ||--}o DataUseModifier : "has data use modifier"
DataAccessPolicy ||--}o Attribute : "has attribute"
Dataset ||--}| File : "has file"
Dataset ||--|o Publication : "has publication"
Dataset ||--|| DataAccessPolicy : "has data access policy"
Dataset ||--}o Attribute : "has attribute"
File ||--}o Attribute : "has attribute"
Analysis ||--}| File : "has input"
Analysis ||--|| Study : "has study"
Analysis ||--}| File : "has output"
Protocol ||--}| Attribute : "has attribute"
SequencingExperiment ||--|| SequencingProtocol : "has sequencing protocol"
SequencingExperiment ||--|| LibraryPreparationProtocol : "has library preparation protocol"
SequencingExperiment ||--}o Attribute : "has attribute"
LibraryPreparationProtocol ||--}| Attribute : "has attribute"
SequencingProtocol ||--}| Attribute : "has attribute"
Individual ||--}o Ancestry : "has ancestry"
Individual ||--}o Individual : "has parent"
Individual ||--}o Individual : "has children"
Individual ||--}| Disease : "has disease"
Individual ||--}o PhenotypicFeature : "has phenotypic feature"
Individual ||--}o File : "has file"
Biospecimen ||--|| Individual : "has individual"
Biospecimen ||--}| AnatomicalEntity : "has anatomical entity"
Sample ||--|o Biospecimen : "has biospecimen"
Sample ||--|| Condition : "has condition"
Sample ||--}o Attribute : "has attribute"

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

Individual ||--}o Ancestry : "has ancestry"
Individual ||--}o Individual : "has parent"
Individual ||--}o Individual : "has children"
Individual ||--}| Disease : "has disease"
Individual ||--}o PhenotypicFeature : "has phenotypic feature"
Individual ||--}o File : "has file"
Biospecimen ||--|| Individual : "has individual"
Biospecimen ||--}| AnatomicalEntity : "has anatomical entity"
Sample ||--|o Biospecimen : "has biospecimen"
Sample ||--|| Condition : "has condition"
Sample ||--}o Attribute : "has attribute"

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

SequencingProcess ||--}| File : "has file"
SequencingProcess ||--|| SequencingExperiment : "has sequencing experiment"
SequencingProcess ||--|| Sample : "has sample"
SequencingProcess ||--}o Attribute : "has attribute"
File ||--}o Attribute : "has attribute"
Sample ||--|o Biospecimen : "has biospecimen"
Sample ||--|| Condition : "has condition"
Sample ||--}o Attribute : "has attribute"
SequencingExperiment ||--|| SequencingProtocol : "has sequencing protocol"
SequencingExperiment ||--|| LibraryPreparationProtocol : "has library preparation protocol"
SequencingExperiment ||--}o Attribute : "has attribute"

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

Sample ||--|o Biospecimen : "has biospecimen"
Sample ||--|| Condition : "has condition"
Sample ||--}o Attribute : "has attribute"
Condition ||--}o Attribute : "has attribute"
Study ||--|o Project : "has project"
Study ||--}| Condition : "has condition"
Study ||--}o Attribute : "has attribute"

```



## Sample, Biospecimen, & Individual (with attributes)

Focusses on the details of the relation between Sample, Biospecimen, and Individual.  

```mermaid
erDiagram
Individual {
    string biological_sex
    string karyotype  
    string age_range
    string vital_status
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
    string vital_status
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

Individual ||--}o Ancestry : "has ancestry"
Individual ||--}o Individual : "has parent"
Individual ||--}o Individual : "has children"
Individual ||--}| Disease : "has disease"
Individual ||--}o PhenotypicFeature : "has phenotypic feature"
Individual ||--}o File : "has file"
Biospecimen ||--|| Individual : "has individual"
Biospecimen ||--}| AnatomicalEntity : "has anatomical entity"
Sample ||--|o Biospecimen : "has biospecimen"
Sample ||--|| Condition : "has condition"
Sample ||--}o Attribute : "has attribute"

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
    string file_format
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

SequencingProcess ||--}| File : "has file"
SequencingProcess ||--|| SequencingExperiment : "has sequencing experiment"
SequencingProcess ||--|| Sample : "has sample"
SequencingProcess ||--}o Attribute : "has attribute"
File ||--}o Attribute : "has attribute"
Sample ||--|o Biospecimen : "has biospecimen"
Sample ||--|| Condition : "has condition"
Sample ||--}o Attribute : "has attribute"
SequencingExperiment ||--|| SequencingProtocol : "has sequencing protocol"
SequencingExperiment ||--|| LibraryPreparationProtocol : "has library preparation protocol"
SequencingExperiment ||--}o Attribute : "has attribute"

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
    string disease_or_healthy
    string treatment_or_control
    string mutant_or_wildtype
    string accession  
    string title  
    string id  
    string alias  
    stringList xref  
}
Study {
    string study_type
    stringList affiliation  
    string accession  
    string ega_accession  
    string title  
    string description  
    string id  
    string alias  
    stringList xref  
}

Sample ||--|o Biospecimen : "has biospecimen"
Sample ||--|| Condition : "has condition"
Sample ||--}o Attribute : "has attribute"
Condition ||--}o Attribute : "has attribute"
Study ||--|o Project : "has project"
Study ||--}| Condition : "has condition"
Study ||--}o Attribute : "has attribute"

```
