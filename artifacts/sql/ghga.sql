

CREATE TABLE activity (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE anatomical_entity (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE biological_entity (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE cell_line (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE committee (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE disease_or_phenotypic_feature (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE file (
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
	id TEXT NOT NULL, 
	name TEXT, 
	gender TEXT NOT NULL, 
	sex TEXT NOT NULL, 
	age INTEGER, 
	PRIMARY KEY (id)
);

CREATE TABLE information_content_entity (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE library (
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
	PRIMARY KEY (id)
);

CREATE TABLE member (
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
	PRIMARY KEY (id)
);

CREATE TABLE person (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE protocol (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE research_activity (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE study (
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
	id TEXT NOT NULL, 
	title TEXT NOT NULL, 
	description TEXT, 
	main_contact TEXT, 
	has_members TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(main_contact) REFERENCES member (id)
);

CREATE TABLE publication (
	id TEXT NOT NULL, 
	title TEXT, 
	study_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(study_id) REFERENCES study (id)
);

CREATE TABLE sample (
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

CREATE TABLE data_access_policy (
	id TEXT NOT NULL, 
	description TEXT NOT NULL, 
	policy_text TEXT NOT NULL, 
	policy_url TEXT, 
	has_data_access_committee TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_data_access_committee) REFERENCES data_access_committee (id)
);

CREATE TABLE experiment (
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

CREATE TABLE dataset (
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

