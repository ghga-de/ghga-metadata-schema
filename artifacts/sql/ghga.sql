
CREATE TYPE biological_sex_enum AS ENUM ('XX', 'XY', 'none');
CREATE TYPE case_control_enum AS ENUM ('control', 'case');
CREATE TYPE user_role_enum AS ENUM ('data requester', 'data steward');

CREATE TABLE agent (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE aggregate_dataset (
	id TEXT NOT NULL, 
	accession TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	has_file TEXT NOT NULL, 
	has_publication TEXT, 
	type TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE analysis_dataset (
	id TEXT NOT NULL, 
	accession TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	has_file TEXT NOT NULL, 
	has_publication TEXT, 
	type TEXT NOT NULL, 
	has_data_access_policy TEXT NOT NULL, 
	has_study TEXT NOT NULL, 
	has_analysis TEXT, 
	has_experiment TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE anatomical_entity (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE attribute (
	key TEXT NOT NULL, 
	key_type TEXT, 
	value TEXT NOT NULL, 
	value_type TEXT, 
	PRIMARY KEY (key, key_type, value, value_type)
);

CREATE TABLE biological_quality (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE cell_line (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE cohort (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT, 
	has_member TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE committee (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE data_transformation (
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	id TEXT NOT NULL, 
	title TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE disease (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE disease_or_phenotypic_feature (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE donor (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	given_name TEXT, 
	family_name TEXT, 
	additional_name TEXT, 
	gender TEXT, 
	sex biological_sex_enum NOT NULL, 
	age INTEGER, 
	year_of_birth TEXT, 
	vital_status TEXT, 
	geographical_region TEXT, 
	ethnicity TEXT, 
	ancestry TEXT, 
	has_parent TEXT, 
	has_children TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE experiment_dataset (
	id TEXT NOT NULL, 
	accession TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	has_file TEXT NOT NULL, 
	has_publication TEXT, 
	type TEXT NOT NULL, 
	has_data_access_policy TEXT NOT NULL, 
	has_study TEXT NOT NULL, 
	has_experiment TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE file (
	id TEXT NOT NULL, 
	accession TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT, 
	format TEXT, 
	size TEXT, 
	checksum TEXT, 
	file_index TEXT, 
	category TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE individual (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	given_name TEXT, 
	family_name TEXT, 
	additional_name TEXT, 
	gender TEXT, 
	sex biological_sex_enum NOT NULL, 
	age INTEGER, 
	year_of_birth TEXT, 
	vital_status TEXT, 
	geographical_region TEXT, 
	ethnicity TEXT, 
	ancestry TEXT, 
	has_parent TEXT, 
	has_children TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE information_content_entity (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE library_preparation_protocol (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE material_entity (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE member (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	given_name TEXT, 
	family_name TEXT, 
	additional_name TEXT, 
	email TEXT NOT NULL, 
	telephone TEXT NOT NULL, 
	organization TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE named_thing (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE person (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	given_name TEXT, 
	family_name TEXT, 
	additional_name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE phenotypic_feature (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE planned_process (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE population (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE project (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	title TEXT, 
	description TEXT, 
	has_publication TEXT, 
	has_study TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE protocol (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT, 
	description TEXT, 
	url TEXT, 
	has_library_preparation_protocol TEXT, 
	has_sequencing_protocol TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE publication (
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	title TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE sequencing_protocol (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE study (
	id TEXT NOT NULL, 
	accession TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	type TEXT NOT NULL, 
	short_name TEXT, 
	has_publication TEXT, 
	has_experiment TEXT, 
	has_analysis TEXT, 
	has_attribute TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE technology (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "user" (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	given_name TEXT, 
	family_name TEXT, 
	additional_name TEXT, 
	email TEXT, 
	role user_role_enum, 
	PRIMARY KEY (id)
);

CREATE TABLE workflow (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE workflow_step (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE analysis (
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	id TEXT NOT NULL, 
	title TEXT, 
	description TEXT, 
	has_input TEXT, 
	has_study TEXT, 
	has_workflow TEXT, 
	has_output TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_study) REFERENCES study (id), 
	FOREIGN KEY(has_workflow) REFERENCES workflow (id)
);

CREATE TABLE biospecimen (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT, 
	description TEXT, 
	has_individual TEXT, 
	has_anatomical_entity TEXT, 
	has_disease TEXT, 
	has_phenotypic_feature TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_individual) REFERENCES individual (id), 
	FOREIGN KEY(has_anatomical_entity) REFERENCES anatomical_entity (id), 
	FOREIGN KEY(has_disease) REFERENCES disease (id), 
	FOREIGN KEY(has_phenotypic_feature) REFERENCES phenotypic_feature (id)
);

CREATE TABLE data_access_committee (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	main_contact TEXT, 
	has_member TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(main_contact) REFERENCES member (id)
);

CREATE TABLE dataset (
	id TEXT NOT NULL, 
	accession TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	has_file TEXT NOT NULL, 
	has_publication TEXT, 
	type TEXT NOT NULL, 
	aggregate_dataset_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(aggregate_dataset_id) REFERENCES aggregate_dataset (id)
);

CREATE TABLE family (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT, 
	has_member TEXT, 
	proband TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(proband) REFERENCES individual (id)
);

CREATE TABLE investigation (
	id TEXT NOT NULL, 
	accession TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	title TEXT, 
	description TEXT, 
	type TEXT, 
	has_publication TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_publication) REFERENCES publication (id)
);

CREATE TABLE research_activity (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	title TEXT, 
	description TEXT, 
	has_publication TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_publication) REFERENCES publication (id)
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

CREATE TABLE aggregate_dataset_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES aggregate_dataset (id)
);

CREATE TABLE analysis_dataset_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES analysis_dataset (id)
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

CREATE TABLE experiment_dataset_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES experiment_dataset (id)
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

CREATE TABLE sequencing_protocol_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES sequencing_protocol (id)
);

CREATE TABLE study_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES study (id)
);

CREATE TABLE study_institution (
	backref_id TEXT, 
	institution TEXT NOT NULL, 
	PRIMARY KEY (backref_id, institution), 
	FOREIGN KEY(backref_id) REFERENCES study (id)
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

CREATE TABLE analysis_process (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	title TEXT, 
	has_input TEXT, 
	has_workflow_step TEXT, 
	has_agent TEXT, 
	has_output TEXT, 
	analysis_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_workflow_step) REFERENCES workflow_step (id), 
	FOREIGN KEY(has_agent) REFERENCES agent (id), 
	FOREIGN KEY(has_output) REFERENCES file (id), 
	FOREIGN KEY(analysis_id) REFERENCES analysis (id)
);

CREATE TABLE data_access_policy (
	id TEXT NOT NULL, 
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT, 
	description TEXT NOT NULL, 
	policy_text TEXT NOT NULL, 
	policy_url TEXT, 
	has_data_access_committee TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_data_access_committee) REFERENCES data_access_committee (id)
);

CREATE TABLE sample (
	id TEXT NOT NULL, 
	accession TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	name TEXT, 
	description TEXT, 
	has_individual TEXT NOT NULL, 
	has_biospecimen TEXT, 
	type case_control_enum, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_individual) REFERENCES individual (id), 
	FOREIGN KEY(has_biospecimen) REFERENCES biospecimen (id)
);

CREATE TABLE analysis_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES analysis (id)
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

CREATE TABLE dataset_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES dataset (id)
);

CREATE TABLE family_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES family (id)
);

CREATE TABLE investigation_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES investigation (id)
);

CREATE TABLE research_activity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES research_activity (id)
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
	accession TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
	title TEXT, 
	type TEXT, 
	has_publication TEXT, 
	name TEXT NOT NULL, 
	description TEXT, 
	has_study TEXT NOT NULL, 
	has_sample TEXT NOT NULL, 
	has_technology TEXT, 
	has_file TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_publication) REFERENCES publication (id), 
	FOREIGN KEY(has_study) REFERENCES study (id), 
	FOREIGN KEY(has_sample) REFERENCES sample (id), 
	FOREIGN KEY(has_technology) REFERENCES technology (id)
);

CREATE TABLE analysis_process_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES analysis_process (id)
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
	accession TEXT, 
	type TEXT, 
	has_attribute TEXT, 
	creation_date TEXT, 
	update_date TEXT, 
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

