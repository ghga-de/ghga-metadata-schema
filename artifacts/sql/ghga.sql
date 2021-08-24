

CREATE TABLE activity (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE anatomical_entity (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE biological_entity (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE cell_line (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE committee (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE disease_or_phenotypic_feature (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE file (
	creation_date TEXT, 
	update_date TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	format TEXT, 
	type TEXT, 
	size TEXT, 
	checksum TEXT, 
	file_index TEXT, 
	category TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE individual (
	creation_date TEXT, 
	update_date TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	gender TEXT NOT NULL, 
	sex TEXT NOT NULL, 
	age INTEGER, 
	PRIMARY KEY (id)
);

CREATE TABLE information_content_entity (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE library (
	creation_date TEXT, 
	update_date TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	layout TEXT NOT NULL, 
	source TEXT NOT NULL, 
	selection TEXT NOT NULL, 
	strategy TEXT NOT NULL, 
	construction_protocol TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE material_entity (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE member (
	creation_date TEXT, 
	update_date TEXT, 
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	title TEXT, 
	email TEXT, 
	telephone TEXT NOT NULL, 
	organization TEXT NOT NULL, 
	main_contact TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(main_contact) REFERENCES member (id)
);

CREATE TABLE named_thing (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE person (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE protocol (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE research_activity (
	id TEXT NOT NULL, 
	creation_date TEXT, 
	update_date TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE study (
	creation_date TEXT, 
	update_date TEXT, 
	id TEXT NOT NULL, 
	title TEXT NOT NULL, 
	type TEXT NOT NULL, 
	name TEXT, 
	abstract TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE attribute (
	key TEXT NOT NULL, 
	key_type TEXT, 
	value TEXT NOT NULL, 
	value_type TEXT, 
	study_id TEXT, 
	PRIMARY KEY (key, key_type, value, value_type, study_id), 
	FOREIGN KEY(study_id) REFERENCES study (id)
);

CREATE TABLE data_access_committee (
	creation_date TEXT, 
	update_date TEXT, 
	id TEXT NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	main_contact TEXT, 
	has_members TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(main_contact) REFERENCES member (id)
);

CREATE TABLE publication (
	creation_date TEXT, 
	update_date TEXT, 
	id TEXT NOT NULL, 
	title TEXT, 
	study_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(study_id) REFERENCES study (id)
);

CREATE TABLE sample (
	creation_date TEXT, 
	update_date TEXT, 
	id TEXT NOT NULL, 
	name TEXT, 
	type TEXT, 
	description TEXT, 
	subject TEXT NOT NULL, 
	biosample_accession TEXT, 
	has_anatomical_site TEXT, 
	has_cell_line TEXT, 
	geographical_region TEXT, 
	has_disease_of_phenotypic_feature TEXT NOT NULL, 
	files TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subject) REFERENCES individual (id), 
	FOREIGN KEY(has_anatomical_site) REFERENCES anatomical_entity (id), 
	FOREIGN KEY(has_cell_line) REFERENCES cell_line (id), 
	FOREIGN KEY(has_disease_of_phenotypic_feature) REFERENCES disease_or_phenotypic_feature (id)
);

CREATE TABLE activity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES activity (id)
);

CREATE TABLE anatomical_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES anatomical_entity (id)
);

CREATE TABLE biological_entity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES biological_entity (id)
);

CREATE TABLE cell_line_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES cell_line (id)
);

CREATE TABLE committee_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES committee (id)
);

CREATE TABLE disease_or_phenotypic_feature_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES disease_or_phenotypic_feature (id)
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

CREATE TABLE library_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES library (id)
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

CREATE TABLE protocol_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES protocol (id)
);

CREATE TABLE research_activity_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES research_activity (id)
);

CREATE TABLE study_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES study (id)
);

CREATE TABLE data_access_policy (
	creation_date TEXT, 
	update_date TEXT, 
	id TEXT NOT NULL, 
	description TEXT NOT NULL, 
	policy_text TEXT NOT NULL, 
	policy_url TEXT, 
	has_data_access_committee TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_data_access_committee) REFERENCES data_access_committee (id)
);

CREATE TABLE experiment (
	creation_date TEXT, 
	update_date TEXT, 
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	has_study TEXT NOT NULL, 
	instrument_model TEXT NOT NULL, 
	has_library TEXT NOT NULL, 
	has_sample TEXT NOT NULL, 
	has_protocol TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_study) REFERENCES study (id), 
	FOREIGN KEY(has_library) REFERENCES library (id), 
	FOREIGN KEY(has_sample) REFERENCES sample (id), 
	FOREIGN KEY(has_protocol) REFERENCES protocol (id)
);

CREATE TABLE data_access_committee_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES data_access_committee (id)
);

CREATE TABLE publication_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES publication (id)
);

CREATE TABLE sample_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES sample (id)
);

CREATE TABLE dataset (
	creation_date TEXT, 
	update_date TEXT, 
	id TEXT NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	type TEXT NOT NULL, 
	files TEXT NOT NULL, 
	has_data_access_policy TEXT NOT NULL, 
	has_study TEXT NOT NULL, 
	has_experiment TEXT NOT NULL, 
	has_file TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_data_access_policy) REFERENCES data_access_policy (id), 
	FOREIGN KEY(has_study) REFERENCES study (id), 
	FOREIGN KEY(has_experiment) REFERENCES experiment (id), 
	FOREIGN KEY(has_file) REFERENCES file (id)
);

CREATE TABLE processed_dataset (
	creation_date TEXT, 
	update_date TEXT, 
	id TEXT NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	type TEXT NOT NULL, 
	files TEXT NOT NULL, 
	has_data_access_policy TEXT NOT NULL, 
	has_study TEXT NOT NULL, 
	has_experiment TEXT NOT NULL, 
	has_file TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_data_access_policy) REFERENCES data_access_policy (id), 
	FOREIGN KEY(has_study) REFERENCES study (id), 
	FOREIGN KEY(has_experiment) REFERENCES experiment (id), 
	FOREIGN KEY(has_file) REFERENCES file (id)
);

CREATE TABLE synthetic_dataset (
	creation_date TEXT, 
	update_date TEXT, 
	id TEXT NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT NOT NULL, 
	type TEXT NOT NULL, 
	files TEXT NOT NULL, 
	has_data_access_policy TEXT NOT NULL, 
	has_study TEXT NOT NULL, 
	has_experiment TEXT NOT NULL, 
	has_file TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_data_access_policy) REFERENCES data_access_policy (id), 
	FOREIGN KEY(has_study) REFERENCES study (id), 
	FOREIGN KEY(has_experiment) REFERENCES experiment (id), 
	FOREIGN KEY(has_file) REFERENCES file (id)
);

CREATE TABLE data_access_policy_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES data_access_policy (id)
);

CREATE TABLE experiment_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES experiment (id)
);

CREATE TABLE dataset_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES dataset (id)
);

CREATE TABLE processed_dataset_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES processed_dataset (id)
);

CREATE TABLE synthetic_dataset_xref (
	backref_id TEXT, 
	xref TEXT, 
	PRIMARY KEY (backref_id, xref), 
	FOREIGN KEY(backref_id) REFERENCES synthetic_dataset (id)
);

