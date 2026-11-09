
# Subset: ontology


This slot is part of an ontology which is currently not otherwise encoded in the schema.

URI: [GHGA:ontology](https://w3id.org/GHGA/ontology)


### Classes


### Mixins


### Slots

 * [Individual➞ancestry_ids](Individual_ancestry_ids.md)
 * [Individual➞ancestry_terms](Individual_ancestry_terms.md)
 * [Individual➞diagnosis_ids](Individual_diagnosis_ids.md)
 * [Individual➞diagnosis_terms](Individual_diagnosis_terms.md)
 * [Individual➞geographical_region_id](Individual_geographical_region_id.md)
 * [Individual➞geographical_region_term](Individual_geographical_region_term.md)
 * [Individual➞phenotypic_features_ids](Individual_phenotypic_features_ids.md)
 * [Individual➞phenotypic_features_terms](Individual_phenotypic_features_terms.md)
 * [Sample➞biospecimen_tissue_id](Sample_biospecimen_tissue_id.md)
 * [Sample➞biospecimen_tissue_term](Sample_biospecimen_tissue_term.md)
 * [ancestry_ids](ancestry_ids.md) - The HANCESTRO IDs corresponding to the ancestry terms (e.g., 'HANCESTRO:0010; HANCESTRO:0005').
 * [ancestry_terms](ancestry_terms.md) - A person's descent or lineage from a population. The used terms should be descendants of 'HANCESTRO:0004: ancestry category' (e.g., 'African; European').
 * [biospecimen_tissue_id](biospecimen_tissue_id.md) - The BTO ID corresponding to the biospecimen tissue term (e.g., 'BTO:0000671').
 * [biospecimen_tissue_term](biospecimen_tissue_term.md) - The tissue this Biospecimen originated from. Should be a term from the BRENDA Tissue Ontology vocabulary (e.g., 'kidney').
 * [diagnosis_ids](diagnosis_ids.md) - One or more diagnoses that the entity is associated with at the time of retrieval from the organism. The diagnosis is captured using a code from ICD-10 (WHO version). Please restrict the ICD code to the chapter letter and two digits for the main diagnosis (e.g., 'E10; C01').
 * [diagnosis_terms](diagnosis_terms.md) - The ICD-10 terms corresponding to the ICD-10 codes (e.g., 'Type 1 diabetes mellitus; Malignant neoplasm of base of tongue').
 * [geographical_region_id](geographical_region_id.md) - The NCIT ID corresponding to the geographical region term (e.g., 'NCIT:C16636').
 * [geographical_region_term](geographical_region_term.md) - The Individual's geographical region. The used term should be a descendant of 'NCIT:C25464: country' (e.g., 'Germany').
 * [phenotypic_features_ids](phenotypic_features_ids.md) - The HPO IDs corresponding to the phenotypic feature terms (e.g., 'HP:0002732; HP:0012735').
 * [phenotypic_features_terms](phenotypic_features_terms.md) - The phenotypic feature concepts that the entity is associated with at the time of retrieval from the organism. The Phenotypic Feature is captured using a concept from the Human Phenotype Ontology (e.g., 'Lymph node hypoplasia; Cough').

### Types


### Enums

