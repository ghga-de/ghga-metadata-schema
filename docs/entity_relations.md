# Entity Relationship Diagrams

## Global Overview

An overview of the entire submission schema.  

```mermaid
erDiagram
Submission {

}
Publication {

}
Member {

}
DataAccessCommittee {

}
Attribute {

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
Study {

}
Project {

}
Sample {

}
Biospecimen {

}
Individual {

}
PhenotypicFeature {

}
Disease {

}
Ancestry {

}
AnatomicalEntity {

}
Experiment {

}
Protocol {

}

Submission ||--|| Study : "has study"
Submission ||--|o Project : "has project"
Submission ||--}o Sample : "has sample"
Submission ||--}o Biospecimen : "has biospecimen"
Submission ||--}o Individual : "has individual"
Submission ||--}o Experiment : "has experiment"
Submission ||--}o Protocol : "has protocol"
Submission ||--}o Analysis : "has analysis"
Submission ||--}| File : "has file"
Submission ||--}| Dataset : "has dataset"
Submission ||--}| DataAccessPolicy : "has data access policy"
Submission ||--}| DataAccessCommittee : "has data access committee"
Submission ||--}| Member : "has member"
Submission ||--}o Publication : "has publication"
DataAccessCommittee ||--|| Member : "main contact"
DataAccessCommittee ||--}o Member : "has member"
DataAccessCommittee ||--}o Attribute : "has attribute"
DataAccessPolicy ||--|| DataAccessCommittee : "has data access committee"
DataAccessPolicy ||--|| DataUsePermission : "has data use permission"
DataAccessPolicy ||--}o DataUseModifier : "has data use modifier"
DataAccessPolicy ||--}o Attribute : "has attribute"
Dataset ||--}| Study : "has study"
Dataset ||--}| Experiment : "has experiment"
Dataset ||--}| Sample : "has sample"
Dataset ||--}o Analysis : "has analysis"
Dataset ||--}| File : "has file"
Dataset ||--}o Publication : "has publication"
Dataset ||--|| DataAccessPolicy : "has data access policy"
Dataset ||--}o Attribute : "has attribute"
File ||--}o Attribute : "has attribute"
Analysis ||--}| File : "has input"
Analysis ||--|| Study : "has study"
Analysis ||--}| File : "has output"
Study ||--|o Project : "has project"
Study ||--}o File : "has file"
Study ||--}o Publication : "has publication"
Study ||--}o Attribute : "has attribute"
Project ||--}o Attribute : "has attribute"
Sample ||--|| Individual : "has individual"
Sample ||--}| AnatomicalEntity : "has anatomical entity"
Sample ||--|o Biospecimen : "has biospecimen"
Sample ||--}o Attribute : "has attribute"
Biospecimen ||--|| Individual : "has individual"
Individual ||--}o Ancestry : "has ancestry"
Individual ||--}o Individual : "has parent"
Individual ||--}o Individual : "has children"
Individual ||--}| Disease : "has disease"
Individual ||--}o PhenotypicFeature : "has phenotypic feature"
Individual ||--}o File : "has file"
Experiment ||--|| Study : "has study"
Experiment ||--}| Sample : "has sample"
Experiment ||--}| File : "has file"
Experiment ||--}| Protocol : "has protocol"
Experiment ||--}o Attribute : "has attribute"
Protocol ||--}| Attribute : "has attribute"

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

Submission ||--|| Study : "has study"
Submission ||--|o Project : "has project"
Submission ||--}o Sample : "has sample"
Submission ||--}o Biospecimen : "has biospecimen"
Submission ||--}o Individual : "has individual"
Submission ||--}o Experiment : "has experiment"
Submission ||--}o Protocol : "has protocol"
Submission ||--}o Analysis : "has analysis"
Submission ||--}| File : "has file"
Submission ||--}| Dataset : "has dataset"
Submission ||--}| DataAccessPolicy : "has data access policy"
Submission ||--}| DataAccessCommittee : "has data access committee"
Submission ||--}| Member : "has member"
Submission ||--}o Publication : "has publication"
DataAccessCommittee ||--|| Member : "main contact"
DataAccessCommittee ||--}o Member : "has member"
DataAccessCommittee ||--}o Attribute : "has attribute"
DataAccessPolicy ||--|| DataAccessCommittee : "has data access committee"
DataAccessPolicy ||--|| DataUsePermission : "has data use permission"
DataAccessPolicy ||--}o DataUseModifier : "has data use modifier"
DataAccessPolicy ||--}o Attribute : "has attribute"
Dataset ||--}| Study : "has study"
Dataset ||--}| Experiment : "has experiment"
Dataset ||--}| Sample : "has sample"
Dataset ||--}o Analysis : "has analysis"
Dataset ||--}| File : "has file"
Dataset ||--}o Publication : "has publication"
Dataset ||--|| DataAccessPolicy : "has data access policy"
Dataset ||--}o Attribute : "has attribute"
File ||--}o Attribute : "has attribute"
Analysis ||--}| File : "has input"
Analysis ||--|| Study : "has study"
Analysis ||--}| File : "has output"
Study ||--|o Project : "has project"
Study ||--}o File : "has file"
Study ||--}o Publication : "has publication"
Study ||--}o Attribute : "has attribute"
Project ||--}o Attribute : "has attribute"
Sample ||--|| Individual : "has individual"
Sample ||--}| AnatomicalEntity : "has anatomical entity"
Sample ||--|o Biospecimen : "has biospecimen"
Sample ||--}o Attribute : "has attribute"
Biospecimen ||--|| Individual : "has individual"
Individual ||--}o Ancestry : "has ancestry"
Individual ||--}o Individual : "has parent"
Individual ||--}o Individual : "has children"
Individual ||--}| Disease : "has disease"
Individual ||--}o PhenotypicFeature : "has phenotypic feature"
Individual ||--}o File : "has file"
Biospecimen ||--|| Individual : "has individual"
Sample ||--|| Individual : "has individual"
Sample ||--}| AnatomicalEntity : "has anatomical entity"
Sample ||--|o Biospecimen : "has biospecimen"
Sample ||--}o Attribute : "has attribute"

```



## Experiment, Sample, & File

Focusses on the relation between Experiment, Sample, and File.  

```mermaid
erDiagram
File {

}
Sample {

}
Experiment {

}

Submission ||--|| Study : "has study"
Submission ||--|o Project : "has project"
Submission ||--}o Sample : "has sample"
Submission ||--}o Biospecimen : "has biospecimen"
Submission ||--}o Individual : "has individual"
Submission ||--}o Experiment : "has experiment"
Submission ||--}o Protocol : "has protocol"
Submission ||--}o Analysis : "has analysis"
Submission ||--}| File : "has file"
Submission ||--}| Dataset : "has dataset"
Submission ||--}| DataAccessPolicy : "has data access policy"
Submission ||--}| DataAccessCommittee : "has data access committee"
Submission ||--}| Member : "has member"
Submission ||--}o Publication : "has publication"
DataAccessCommittee ||--|| Member : "main contact"
DataAccessCommittee ||--}o Member : "has member"
DataAccessCommittee ||--}o Attribute : "has attribute"
DataAccessPolicy ||--|| DataAccessCommittee : "has data access committee"
DataAccessPolicy ||--|| DataUsePermission : "has data use permission"
DataAccessPolicy ||--}o DataUseModifier : "has data use modifier"
DataAccessPolicy ||--}o Attribute : "has attribute"
Dataset ||--}| Study : "has study"
Dataset ||--}| Experiment : "has experiment"
Dataset ||--}| Sample : "has sample"
Dataset ||--}o Analysis : "has analysis"
Dataset ||--}| File : "has file"
Dataset ||--}o Publication : "has publication"
Dataset ||--|| DataAccessPolicy : "has data access policy"
Dataset ||--}o Attribute : "has attribute"
File ||--}o Attribute : "has attribute"
Sample ||--|| Individual : "has individual"
Sample ||--}| AnatomicalEntity : "has anatomical entity"
Sample ||--|o Biospecimen : "has biospecimen"
Sample ||--}o Attribute : "has attribute"
Experiment ||--|| Study : "has study"
Experiment ||--}| Sample : "has sample"
Experiment ||--}| File : "has file"
Experiment ||--}| Protocol : "has protocol"
Experiment ||--}o Attribute : "has attribute"

```


### Detailed Diagram:

```mermaid
erDiagram
Submission {
    string id  
    string affiliation  
    string submission_date  
    string submission_status  
}
Publication {
    string title  
    string abstract  
    string author  
    integer year  
    string journal  
    string doi  
    string id  
    string alias  
    stringList xref  
}
Member {
    string email  
    string telephone  
    string organization  
    string given_name  
    string family_name  
    string additional_name  
    string id  
    string alias  
    stringList xref  
}
DataAccessCommittee {
    string name  
    string description  
    string accession  
    string ega_accession  
    string id  
    string alias  
    stringList xref  
}
Attribute {
    string key  
    string key_type  
    string value  
    string value_type  
}
DataAccessPolicy {
    string name  
    string description  
    string policy_text  
    string policy_url  
    string data_request_form  
    string accession  
    string ega_accession  
    string id  
    string alias  
    stringList xref  
}
DataUseModifier {
    string id  
    string concept_identifier  
    string concept_name  
    string description  
    string ontology_name  
    string ontology_version  
    string alias  
    stringList xref  
}
DataUsePermission {
    string id  
    string concept_identifier  
    string concept_name  
    string description  
    string ontology_name  
    string ontology_version  
    string alias  
    stringList xref  
}
Dataset {
    string title  
    string description  
    stringList type  
    string accession  
    string ega_accession  
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
Analysis {
    string type  
    string reference_genome  
    string reference_chromosome  
    string description  
    string accession  
    string ega_accession  
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
Project {
    string accession  
    string title  
    string description  
    string id  
    string alias  
    stringList xref  
}
Sample {
    string name  
    string type  
    string description  
    string case_control_status
    string vital_status
    string isolation  
    string storage  
    string accession  
    string ega_accession  
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
    string accession  
    string id  
    string alias  
    stringList xref  
}
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
PhenotypicFeature {
    string id  
    string concept_identifier  
    string concept_name  
    string description  
    string ontology_name  
    string ontology_version  
    string alias  
    stringList xref  
}
Disease {
    string id  
    string concept_identifier  
    string concept_name  
    string description  
    string ontology_name  
    string ontology_version  
    string alias  
    stringList xref  
}
Ancestry {
    string id  
    string concept_identifier  
    string concept_name  
    string description  
    string ontology_name  
    string ontology_version  
    string name  
    string alias  
    stringList xref  
}
AnatomicalEntity {
    string id  
    string concept_identifier  
    string concept_name  
    string description  
    string ontology_name  
    string ontology_version  
    string alias  
    stringList xref  
}
Experiment {
    string type  
    string biological_replicates  
    string technical_replicates  
    string accession  
    string ega_accession  
    string title  
    string description  
    string id  
    string alias  
    stringList xref  
}
Protocol {
    string name  
    string type  
    string description  
    string url  
    string id  
    string alias  
    stringList xref  
}

Submission ||--|| Study : "has study"
Submission ||--|o Project : "has project"
Submission ||--}o Sample : "has sample"
Submission ||--}o Biospecimen : "has biospecimen"
Submission ||--}o Individual : "has individual"
Submission ||--}o Experiment : "has experiment"
Submission ||--}o Protocol : "has protocol"
Submission ||--}o Analysis : "has analysis"
Submission ||--}| File : "has file"
Submission ||--}| Dataset : "has dataset"
Submission ||--}| DataAccessPolicy : "has data access policy"
Submission ||--}| DataAccessCommittee : "has data access committee"
Submission ||--}| Member : "has member"
Submission ||--}o Publication : "has publication"
DataAccessCommittee ||--|| Member : "main contact"
DataAccessCommittee ||--}o Member : "has member"
DataAccessCommittee ||--}o Attribute : "has attribute"
DataAccessPolicy ||--|| DataAccessCommittee : "has data access committee"
DataAccessPolicy ||--|| DataUsePermission : "has data use permission"
DataAccessPolicy ||--}o DataUseModifier : "has data use modifier"
DataAccessPolicy ||--}o Attribute : "has attribute"
Dataset ||--}| Study : "has study"
Dataset ||--}| Experiment : "has experiment"
Dataset ||--}| Sample : "has sample"
Dataset ||--}o Analysis : "has analysis"
Dataset ||--}| File : "has file"
Dataset ||--}o Publication : "has publication"
Dataset ||--|| DataAccessPolicy : "has data access policy"
Dataset ||--}o Attribute : "has attribute"
File ||--}o Attribute : "has attribute"
Analysis ||--}| File : "has input"
Analysis ||--|| Study : "has study"
Analysis ||--}| File : "has output"
Study ||--|o Project : "has project"
Study ||--}o File : "has file"
Study ||--}o Publication : "has publication"
Study ||--}o Attribute : "has attribute"
Project ||--}o Attribute : "has attribute"
Sample ||--|| Individual : "has individual"
Sample ||--}| AnatomicalEntity : "has anatomical entity"
Sample ||--|o Biospecimen : "has biospecimen"
Sample ||--}o Attribute : "has attribute"
Biospecimen ||--|| Individual : "has individual"
Individual ||--}o Ancestry : "has ancestry"
Individual ||--}o Individual : "has parent"
Individual ||--}o Individual : "has children"
Individual ||--}| Disease : "has disease"
Individual ||--}o PhenotypicFeature : "has phenotypic feature"
Individual ||--}o File : "has file"
Experiment ||--|| Study : "has study"
Experiment ||--}| Sample : "has sample"
Experiment ||--}| File : "has file"
Experiment ||--}| Protocol : "has protocol"
Experiment ||--}o Attribute : "has attribute"
Protocol ||--}| Attribute : "has attribute"

```
