
CREATE TYPE status_enum AS ENUM ('in progress', 'submitted', 'unreleased', 'released', 'deprecated');
CREATE TYPE biological_sex_enum AS ENUM ('XX', 'XY', 'none');
CREATE TYPE vital_status_enum AS ENUM ('alive', 'deceased', 'unknown');
CREATE TYPE file_type_enum AS ENUM ('bam', 'complete_genomics', 'cram', 'fasta', 'fastq', 'pacbio_hdf5', 'sff', 'srf', 'vcf');
CREATE TYPE case_control_enum AS ENUM ('control', 'case');
CREATE TYPE study_type_enum AS ENUM ('whole_genome_sequencing', 'metagenomics', 'transcriptome_analysis', 'resequencing', 'epigenetics', 'synthetic_genomics', 'forensic_paleo_genomics', 'gene_regulation', 'cancer_genomics', 'population_genomics', 'rna_seq', 'exome_sequencing', 'pooled_clone_sequencing', 'other');
CREATE TYPE user_role_enum AS ENUM ('data requester', 'data steward');

CREATE TABLE accession_mixin (
	accession TEXT, 
	PRIMARY KEY (accession)
);

CREATE TABLE agent (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE anatomical_entity (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE attribute (
	key TEXT NOT NULL, 
	key_type TEXT, 
	value TEXT NOT NULL, 
	value_type TEXT, 
	PRIMARY KEY (key, key_type, value, value_type)
);

CREATE TABLE attribute_mixin (
	has_attribute TEXT, 
	PRIMARY KEY (has_attribute)
);

CREATE TABLE biological_quality (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE cell_line (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE cohort (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	name TEXT, 
	has_member TEXT, 
	accession TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE committee (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE data_transformation (
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	id TEXT NOT NULL, 
	title TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE dataset (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	has_study TEXT NOT NULL, 
	has_experiment TEXT NOT NULL, 
	has_sample TEXT NOT NULL, 
	has_analysis TEXT NOT NULL, 
	has_file TEXT NOT NULL, 
	has_data_access_policy TEXT NOT NULL, 
	type TEXT NOT NULL, 
	has_publication TEXT, 
	accession TEXT, 
	status status_enum, 
	PRIMARY KEY (id)
);

CREATE TABLE disease (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE disease_or_phenotypic_feature (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE donor (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	given_name TEXT, 
	family_name TEXT, 
	additional_name TEXT, 
	gender TEXT, 
	sex biological_sex_enum NOT NULL, 
	age INTEGER NOT NULL, 
	year_of_birth TEXT, 
	vital_status vital_status_enum NOT NULL, 
	geographical_region TEXT, 
	ethnicity TEXT, 
	ancestry TEXT, 
	has_parent TEXT, 
	has_children TEXT, 
	has_disease TEXT, 
	has_phenotypic_feature TEXT, 
	accession TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE file (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT NOT NULL, 
	format TEXT, 
	size TEXT, 
	checksum TEXT, 
	file_index TEXT, 
	category TEXT, 
	type file_type_enum, 
	accession TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE individual (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	given_name TEXT, 
	family_name TEXT, 
	additional_name TEXT, 
	gender TEXT, 
	sex biological_sex_enum NOT NULL, 
	age INTEGER NOT NULL, 
	year_of_birth TEXT, 
	vital_status vital_status_enum NOT NULL, 
	geographical_region TEXT, 
	ethnicity TEXT, 
	ancestry TEXT, 
	has_parent TEXT, 
	has_children TEXT, 
	has_disease TEXT, 
	has_phenotypic_feature TEXT, 
	accession TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE information_content_entity (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE investigation (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	title TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE library_preparation_protocol (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	url TEXT, 
	type TEXT, 
	library_name TEXT NOT NULL, 
	library_layout TEXT NOT NULL, 
	library_type TEXT NOT NULL, 
	library_selection TEXT NOT NULL, 
	library_construction TEXT NOT NULL, 
	library_preparation TEXT NOT NULL, 
	library_level TEXT, 
	library_construction_kit_retail_name TEXT NOT NULL, 
	library_construction_kit_manufacturer TEXT NOT NULL, 
	primer TEXT, 
	end_bias TEXT, 
	target_regions TEXT, 
	rnaseq_strandedness TEXT, 
	name TEXT NOT NULL, 
	description TEXT NOT NULL, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE material_entity (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE member (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	given_name TEXT, 
	family_name TEXT, 
	additional_name TEXT, 
	email TEXT NOT NULL, 
	telephone TEXT NOT NULL, 
	organization TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE named_thing (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE ontology_class_mixin (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE person (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	given_name TEXT, 
	family_name TEXT, 
	additional_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE phenotypic_feature (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE planned_process (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE population (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE project (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	has_publication TEXT, 
	has_attribute TEXT, 
	accession TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE protocol (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT, 
	description TEXT, 
	url TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE publication (
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	title TEXT, 
	abstract TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE release_mixin (
	release_date TEXT, 
	PRIMARY KEY (release_date)
);

CREATE TABLE research_activity (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	title TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE sequencing_protocol (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	url TEXT, 
	type TEXT, 
	sequencing_center TEXT NOT NULL, 
	instrument_model TEXT NOT NULL, 
	read_length TEXT, 
	read_pair_number TEXT, 
	sequencing_length TEXT, 
	target_coverage TEXT, 
	reference_annotation TEXT, 
	lane_number TEXT, 
	flow_cell_id TEXT, 
	flow_cell_type TEXT, 
	umi_barcode_read TEXT, 
	umi_barcode_size TEXT, 
	umi_barcode_offset TEXT, 
	cell_barcode_read TEXT, 
	cell_barcode_offset TEXT, 
	cell_barcode_size TEXT, 
	sample_barcode_read TEXT, 
	name TEXT, 
	description TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE status_mixin (
	status status_enum, 
	PRIMARY KEY (status)
);

CREATE TABLE technology (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "user" (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	given_name TEXT, 
	family_name TEXT, 
	additional_name TEXT, 
	email TEXT, 
	role user_role_enum, 
	PRIMARY KEY (id)
);

CREATE TABLE workflow (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE workflow_step (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE biospecimen (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT, 
	has_individual TEXT, 
	has_anatomical_entity TEXT, 
	has_disease TEXT, 
	has_phenotypic_feature TEXT, 
	accession TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_individual) REFERENCES individual (id), 
	FOREIGN KEY(has_anatomical_entity) REFERENCES anatomical_entity (id)
);

CREATE TABLE data_access_committee (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	main_contact TEXT, 
	has_member TEXT, 
	accession TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(main_contact) REFERENCES member (id)
);

CREATE TABLE deprecated_mixin (
	replaced_by TEXT, 
	deprecation_date TEXT, 
	PRIMARY KEY (replaced_by, deprecation_date), 
	FOREIGN KEY(replaced_by) REFERENCES named_thing (id)
);

CREATE TABLE family (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	name TEXT, 
	has_member TEXT, 
	has_proband TEXT, 
	accession TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_proband) REFERENCES individual (id)
);

CREATE TABLE publication_mixin (
	has_publication TEXT, 
	PRIMARY KEY (has_publication), 
	FOREIGN KEY(has_publication) REFERENCES publication (id)
);

CREATE TABLE study (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	has_experiment TEXT, 
	has_analysis TEXT, 
	has_project TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	type study_type_enum NOT NULL, 
	has_publication TEXT, 
	has_attribute TEXT, 
	status status_enum, 
	accession TEXT, 
	release_date TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_project) REFERENCES project (id)
);

CREATE TABLE workflow_parameter (
	key TEXT, 
	value TEXT, 
	workflow_step_id TEXT, 
	PRIMARY KEY (key, value, workflow_step_id), 
	FOREIGN KEY(workflow_step_id) REFERENCES workflow_step (id)
);

CREATE TABLE agent_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES agent (id)
);

CREATE TABLE anatomical_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity (id)
);

CREATE TABLE biological_quality_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES biological_quality (id)
);

CREATE TABLE cell_line_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES cell_line (id)
);

CREATE TABLE cohort_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES cohort (id)
);

CREATE TABLE committee_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES committee (id)
);

CREATE TABLE data_transformation_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES data_transformation (id)
);

CREATE TABLE dataset_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES dataset (id)
);

CREATE TABLE disease_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES disease (id)
);

CREATE TABLE disease_or_phenotypic_feature_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature (id)
);

CREATE TABLE donor_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES donor (id)
);

CREATE TABLE file_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES file (id)
);

CREATE TABLE individual_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES individual (id)
);

CREATE TABLE information_content_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES information_content_entity (id)
);

CREATE TABLE investigation_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES investigation (id)
);

CREATE TABLE library_preparation_protocol_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES library_preparation_protocol (id)
);

CREATE TABLE material_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES material_entity (id)
);

CREATE TABLE member_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES member (id)
);

CREATE TABLE named_thing_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES named_thing (id)
);

CREATE TABLE person_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES person (id)
);

CREATE TABLE phenotypic_feature_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES phenotypic_feature (id)
);

CREATE TABLE planned_process_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES planned_process (id)
);

CREATE TABLE population_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES population (id)
);

CREATE TABLE project_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES project (id)
);

CREATE TABLE protocol_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES protocol (id)
);

CREATE TABLE publication_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE research_activity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES research_activity (id)
);

CREATE TABLE sequencing_protocol_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES sequencing_protocol (id)
);

CREATE TABLE technology_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES technology (id)
);

CREATE TABLE user_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES "user" (id)
);

CREATE TABLE workflow_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES workflow (id)
);

CREATE TABLE workflow_step_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES workflow_step (id)
);

CREATE TABLE analysis (
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	id TEXT NOT NULL, 
	title TEXT, 
	description TEXT, 
	has_input TEXT, 
	has_study TEXT, 
	has_workflow TEXT, 
	has_output TEXT, 
	accession TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_study) REFERENCES study (id), 
	FOREIGN KEY(has_workflow) REFERENCES workflow (id)
);

CREATE TABLE data_access_policy (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	name TEXT, 
	description TEXT NOT NULL, 
	policy_text TEXT NOT NULL, 
	policy_url TEXT, 
	has_data_access_committee TEXT NOT NULL, 
	accession TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_data_access_committee) REFERENCES data_access_committee (id)
);

CREATE TABLE sample (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT NOT NULL, 
	description TEXT NOT NULL, 
	vital_status_at_sampling TEXT, 
	tissue TEXT NOT NULL, 
	isolation TEXT, 
	storage TEXT, 
	has_individual TEXT NOT NULL, 
	has_biospecimen TEXT, 
	type case_control_enum, 
	accession TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_individual) REFERENCES individual (id), 
	FOREIGN KEY(has_biospecimen) REFERENCES biospecimen (id)
);

CREATE TABLE biospecimen_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES biospecimen (id)
);

CREATE TABLE data_access_committee_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES data_access_committee (id)
);

CREATE TABLE family_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES family (id)
);

CREATE TABLE study_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES study (id)
);

CREATE TABLE study_affiliation (
	backref_id TEXT, 
	affiliation TEXT NOT NULL, 
	PRIMARY KEY (backref_id, affiliation), 
	FOREIGN KEY(backref_id) REFERENCES study (id)
);

CREATE TABLE analysis_process (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	title TEXT, 
	has_input TEXT, 
	has_workflow_step TEXT, 
	has_agent TEXT, 
	has_output TEXT, 
	analysis_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_workflow_step) REFERENCES workflow_step (id), 
	FOREIGN KEY(has_agent) REFERENCES agent (id), 
	FOREIGN KEY(analysis_id) REFERENCES analysis (id)
);

CREATE TABLE data_use_condition (
	permission TEXT, 
	modifier TEXT, 
	data_access_policy_id TEXT, 
	PRIMARY KEY (permission, modifier, data_access_policy_id), 
	FOREIGN KEY(data_access_policy_id) REFERENCES data_access_policy (id)
);

CREATE TABLE experiment (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	biological_replicates TEXT, 
	technical_replicates TEXT, 
	experimental_replicates TEXT, 
	has_study TEXT NOT NULL, 
	has_sample TEXT NOT NULL, 
	has_technology TEXT, 
	has_file TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	accession TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_study) REFERENCES study (id), 
	FOREIGN KEY(has_sample) REFERENCES sample (id), 
	FOREIGN KEY(has_technology) REFERENCES technology (id)
);

CREATE TABLE submission (
	id TEXT NOT NULL, 
	has_study TEXT, 
	has_project TEXT, 
	has_sample TEXT, 
	has_biospecimen TEXT, 
	has_individual TEXT, 
	has_experiment TEXT, 
	has_analysis TEXT, 
	has_file TEXT, 
	has_data_access_policy TEXT, 
	submission_date TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	status status_enum, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_study) REFERENCES study (id), 
	FOREIGN KEY(has_project) REFERENCES project (id), 
	FOREIGN KEY(has_data_access_policy) REFERENCES data_access_policy (id)
);

CREATE TABLE analysis_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES analysis (id)
);

CREATE TABLE data_access_policy_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES data_access_policy (id)
);

CREATE TABLE sample_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES sample (id)
);

CREATE TABLE experiment_process (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	type TEXT, 
	title TEXT, 
	has_input TEXT, 
	has_protocol TEXT, 
	has_agent TEXT, 
	has_output TEXT, 
	experiment_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_input) REFERENCES sample (id), 
	FOREIGN KEY(has_protocol) REFERENCES protocol (id), 
	FOREIGN KEY(has_agent) REFERENCES agent (id), 
	FOREIGN KEY(has_output) REFERENCES file (id), 
	FOREIGN KEY(experiment_id) REFERENCES experiment (id)
);

CREATE TABLE analysis_process_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES analysis_process (id)
);

CREATE TABLE experiment_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES experiment (id)
);

CREATE TABLE experiment_process_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES experiment_process (id)
);

