```mermaid
erDiagram
Submission {
    string id  
    string affiliation  
    string submission_date  
    string creation_date  
    string update_date  
    string submission_status  
    string schema_type  
    string schema_version  
}
Publication {
    string title  
    string abstract  
    string author  
    integer year  
    string journal  
    string id  
    string alias  
    stringList xref  
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
}
DataAccessCommittee {
    string name  
    string description  
    member main_contact  
    string accession  
    string ega_accession  
    string id  
    string alias  
    stringList xref  
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
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
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
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
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
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
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
}
Dataset {
    string title  
    string description  
    stringList type  
    string accession  
    string ega_accession  
    release status enum release_status  
    string release_date  
    string id  
    string alias  
    stringList xref  
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
}
File {
    string drs_uri  
    string name  
    file format enum format  
    integer size  
    string checksum  
    string checksum_type  
    string accession  
    string ega_accession  
    string id  
    string alias  
    stringList xref  
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
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
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
}
Study {
    study type enum type  
    stringList affiliation  
    string accession  
    string ega_accession  
    release status enum release_status  
    string release_date  
    string title  
    string description  
    string id  
    string alias  
    stringList xref  
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
}
Project {
    string accession  
    string title  
    string description  
    string id  
    string alias  
    stringList xref  
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
}
Sample {
    string name  
    string type  
    string description  
    case control status enum case_control_status  
    vital status enum vital_status_at_sampling  
    string isolation  
    string storage  
    string accession  
    string ega_accession  
    string id  
    string alias  
    stringList xref  
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
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
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
}
Individual {
    biological sex enum sex  
    string karyotype  
    age range enum age  
    vital status enum vital_status  
    string geographical_region  
    string accession  
    string ega_accession  
    string given_name  
    string family_name  
    string additional_name  
    string id  
    string alias  
    stringList xref  
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
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
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
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
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
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
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
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
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
}
Experiment {
    string type  
    string biological_replicates  
    string technical_replicates  
    string experimental_replicates  
    string accession  
    string ega_accession  
    string title  
    string description  
    string id  
    string alias  
    stringList xref  
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
}
Protocol {
    string name  
    string type  
    string description  
    string url  
    string id  
    string alias  
    stringList xref  
    string creation_date  
    string update_date  
    string schema_type  
    string schema_version  
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
Submission ||--}o Publication : "has publication"
DataAccessCommittee ||--}| Attribute : "has attribute"
DataAccessPolicy ||--|| DataAccessCommittee : "has data access committee"
DataAccessPolicy ||--|| DataUsePermission : "has data use permission"
DataAccessPolicy ||--}o DataUseModifier : "has data use modifier"
DataAccessPolicy ||--}| Attribute : "has attribute"
Dataset ||--}| Study : "has study"
Dataset ||--}o Experiment : "has experiment"
Dataset ||--}| Sample : "has sample"
Dataset ||--}o Analysis : "has analysis"
Dataset ||--}| File : "has file"
Dataset ||--|| DataAccessPolicy : "has data access policy"
Dataset ||--}| Attribute : "has attribute"
File ||--}| Attribute : "has attribute"
Analysis ||--}| File : "has input"
Analysis ||--|| Study : "has study"
Analysis ||--}| File : "has output"
Study ||--|o Project : "has project"
Study ||--}o File : "has file"
Study ||--}o Publication : "has publication"
Study ||--}| Attribute : "has attribute"
Project ||--}| Attribute : "has attribute"
Sample ||--|| Individual : "has individual"
Sample ||--}o AnatomicalEntity : "has anatomical entity"
Sample ||--|o Biospecimen : "has biospecimen"
Sample ||--}| Attribute : "has attribute"
Biospecimen ||--|| Individual : "has individual"
Individual ||--}o Ancestry : "has ancestry"
Individual ||--}o Individual : "has parent"
Individual ||--}o Individual : "has children"
Individual ||--}| Disease : "has disease"
Individual ||--}o PhenotypicFeature : "has phenotypic feature"
Individual ||--}o File : "has file"
Experiment ||--|| Study : "has study"
Experiment ||--}| Sample : "has sample"
Experiment ||--}o File : "has file"
Experiment ||--}| Protocol : "has protocol"
Experiment ||--}| Attribute : "has attribute"
Protocol ||--}| Attribute : "has attribute"

```

