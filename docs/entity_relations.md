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

