
from dataclasses import dataclass
from dataclasses import field
from typing import List

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import Text
from sqlalchemy import Integer
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship

mapper_registry = registry()
metadata = MetaData()

from GHGA-Metadata-Schema import *


tbl_agent = Table('agent', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('name', Text),
    Column('description', Text),
)
tbl_analysis = Table('analysis', metadata, 
    Column('id', Text, primary_key=True),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('title', Text),
    Column('type', Text),
    Column('reference_genome', Text),
    Column('reference_chromosome', Text),
    Column('has_input', Text),
    Column('has_study', Text, ForeignKey('study.id')),
    Column('has_workflow', Text),
    Column('has_output', Text),
    Column('alias', Text),
    Column('description', Text),
    Column('accession', Text),
    Column('ega_accession', Text),
)
tbl_analysis_process = Table('analysis_process', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('title', Text),
    Column('has_input', Text),
    Column('has_workflow', Text, ForeignKey('workflow.id')),
    Column('has_agent', Text, ForeignKey('agent.id')),
    Column('has_output', Text),
    Column('analysis_id', Text, ForeignKey('analysis.id')),
)
tbl_anatomical_entity = Table('anatomical_entity', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('concept_identifier', Text),
    Column('concept_name', Text),
    Column('description', Text),
    Column('ontology_name', Text),
    Column('ontology_version', Text),
    Column('name', Text),
)
tbl_ancestry = Table('ancestry', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('name', Text),
    Column('concept_identifier', Text),
    Column('concept_name', Text),
    Column('description', Text),
    Column('ontology_name', Text),
    Column('ontology_version', Text),
)
tbl_attribute = Table('attribute', metadata, 
    Column('key', Text, primary_key=True),
    Column('key_type', Text, primary_key=True),
    Column('value', Text, primary_key=True),
    Column('value_type', Text, primary_key=True),
)
tbl_biospecimen = Table('biospecimen', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('name', Text),
    Column('description', Text),
    Column('isolation', Text),
    Column('storage', Text),
    Column('has_individual', Text, ForeignKey('individual.id')),
    Column('has_anatomical_entity', Text),
    Column('has_disease', Text),
    Column('has_phenotypic_feature', Text),
    Column('accession', Text),
)
tbl_cell_line = Table('cell_line', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
)
tbl_cohort = Table('cohort', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('name', Text),
    Column('has_member', Text),
    Column('accession', Text),
)
tbl_data_access_committee = Table('data_access_committee', metadata, 
    Column('id', Text, primary_key=True),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('name', Text),
    Column('description', Text),
    Column('main_contact', Text, ForeignKey('member.id')),
    Column('has_member', Text),
    Column('alias', Text),
    Column('accession', Text),
    Column('ega_accession', Text),
)
tbl_data_access_policy = Table('data_access_policy', metadata, 
    Column('id', Text, primary_key=True),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('name', Text),
    Column('description', Text),
    Column('policy_text', Text),
    Column('policy_url', Text),
    Column('has_data_access_committee', Text, ForeignKey('data_access_committee.id')),
    Column('data_request_form', Text),
    Column('alias', Text),
    Column('accession', Text),
    Column('ega_accession', Text),
)
tbl_data_use_condition = Table('data_use_condition', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('has_data_use_permission', Text, ForeignKey('data_use_permission.id')),
    Column('has_data_use_modifier', Text, ForeignKey('data_use_modifier.id')),
    Column('data_access_policy_id', Text, ForeignKey('data_access_policy.id')),
)
tbl_data_use_modifier = Table('data_use_modifier', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('concept_identifier', Text),
    Column('concept_name', Text),
    Column('description', Text),
    Column('ontology_name', Text),
    Column('ontology_version', Text),
    Column('name', Text),
)
tbl_data_use_permission = Table('data_use_permission', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('concept_identifier', Text),
    Column('concept_name', Text),
    Column('description', Text),
    Column('ontology_name', Text),
    Column('ontology_version', Text),
    Column('name', Text),
)
tbl_dataset = Table('dataset', metadata, 
    Column('id', Text, primary_key=True),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('title', Text),
    Column('description', Text),
    Column('type', Text),
    Column('has_study', Text),
    Column('has_experiment', Text),
    Column('has_sample', Text),
    Column('has_analysis', Text),
    Column('has_file', Text),
    Column('has_data_access_policy', Text, ForeignKey('data_access_policy.id')),
    Column('alias', Text),
    Column('has_publication', Text),
    Column('release_status', Text),
    Column('accession', Text),
    Column('ega_accession', Text),
    Column('release_date', Text),
)
tbl_disease = Table('disease', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('concept_identifier', Text),
    Column('concept_name', Text),
    Column('description', Text),
    Column('ontology_name', Text),
    Column('ontology_version', Text),
    Column('name', Text),
)
tbl_disease_or_phenotypic_feature = Table('disease_or_phenotypic_feature', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('concept_identifier', Text),
    Column('concept_name', Text),
    Column('description', Text),
    Column('ontology_name', Text),
    Column('ontology_version', Text),
    Column('name', Text),
)
tbl_donor = Table('donor', metadata, 
    Column('id', Text, primary_key=True),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('given_name', Text),
    Column('family_name', Text),
    Column('additional_name', Text),
    Column('sex', Text),
    Column('karyotype', Text),
    Column('age', Text),
    Column('vital_status', Text),
    Column('geographical_region', Text),
    Column('has_ancestry', Text),
    Column('has_parent', Text),
    Column('has_children', Text),
    Column('has_disease', Text),
    Column('has_phenotypic_feature', Text),
    Column('alias', Text),
    Column('accession', Text),
    Column('ega_accession', Text),
)
tbl_experiment = Table('experiment', metadata, 
    Column('id', Text, primary_key=True),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('type', Text),
    Column('biological_replicates', Text),
    Column('technical_replicates', Text),
    Column('experimental_replicates', Text),
    Column('has_study', Text, ForeignKey('study.id')),
    Column('has_sample', Text, ForeignKey('sample.id')),
    Column('has_file', Text),
    Column('has_protocol', Text),
    Column('alias', Text),
    Column('title', Text),
    Column('description', Text),
    Column('accession', Text),
    Column('ega_accession', Text),
)
tbl_experiment_process = Table('experiment_process', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('type', Text),
    Column('title', Text),
    Column('has_input', Text, ForeignKey('sample.id')),
    Column('has_protocol', Text, ForeignKey('protocol.id')),
    Column('has_agent', Text, ForeignKey('agent.id')),
    Column('has_output', Text, ForeignKey('file.id')),
    Column('has_attribute', Text),
    Column('experiment_id', Text, ForeignKey('experiment.id')),
)
tbl_family = Table('family', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('name', Text),
    Column('has_member', Text),
    Column('has_proband', Text, ForeignKey('individual.id')),
    Column('accession', Text),
)
tbl_file = Table('file', metadata, 
    Column('id', Text, primary_key=True),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('name', Text),
    Column('format', Text),
    Column('size', Text),
    Column('checksum', Text),
    Column('checksum_type', Text),
    Column('alias', Text),
    Column('accession', Text),
    Column('ega_accession', Text),
)
tbl_individual = Table('individual', metadata, 
    Column('id', Text, primary_key=True),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('given_name', Text),
    Column('family_name', Text),
    Column('additional_name', Text),
    Column('sex', Text),
    Column('karyotype', Text),
    Column('age', Text),
    Column('vital_status', Text),
    Column('geographical_region', Text),
    Column('has_ancestry', Text),
    Column('has_parent', Text),
    Column('has_children', Text),
    Column('has_disease', Text),
    Column('has_phenotypic_feature', Text),
    Column('alias', Text),
    Column('accession', Text),
    Column('ega_accession', Text),
)
tbl_library_preparation_protocol = Table('library_preparation_protocol', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('name', Text),
    Column('type', Text),
    Column('url', Text),
    Column('library_name', Text),
    Column('library_layout', Text),
    Column('library_type', Text),
    Column('library_selection', Text),
    Column('library_preparation', Text),
    Column('library_preparation_kit_retail_name', Text),
    Column('library_preparation_kit_manufacturer', Text),
    Column('primer', Text),
    Column('end_bias', Text),
    Column('target_regions', Text),
    Column('rnaseq_strandedness', Text),
    Column('description', Text),
    Column('has_attribute', Text),
)
tbl_member = Table('member', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('given_name', Text),
    Column('family_name', Text),
    Column('additional_name', Text),
    Column('email', Text),
    Column('telephone', Text),
    Column('organization', Text),
)
tbl_phenotypic_feature = Table('phenotypic_feature', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('concept_identifier', Text),
    Column('concept_name', Text),
    Column('description', Text),
    Column('ontology_name', Text),
    Column('ontology_version', Text),
    Column('name', Text),
)
tbl_project = Table('project', metadata, 
    Column('id', Text, primary_key=True),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('alias', Text),
    Column('title', Text),
    Column('description', Text),
    Column('has_publication', Text),
    Column('has_attribute', Text),
    Column('accession', Text),
)
tbl_protocol = Table('protocol', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('name', Text),
    Column('type', Text),
    Column('description', Text),
    Column('url', Text),
    Column('has_attribute', Text),
)
tbl_publication = Table('publication', metadata, 
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('title', Text),
    Column('abstract', Text),
    Column('id', Text, primary_key=True),
)
tbl_sample = Table('sample', metadata, 
    Column('id', Text, primary_key=True),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('name', Text),
    Column('type', Text),
    Column('description', Text),
    Column('vital_status_at_sampling', Text),
    Column('isolation', Text),
    Column('storage', Text),
    Column('has_individual', Text, ForeignKey('individual.id')),
    Column('has_anatomical_entity', Text),
    Column('has_biospecimen', Text, ForeignKey('biospecimen.id')),
    Column('alias', Text),
    Column('tissue', Text),
    Column('accession', Text),
    Column('ega_accession', Text),
    Column('has_attribute', Text),
)
tbl_sequencing_protocol = Table('sequencing_protocol', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('name', Text),
    Column('url', Text),
    Column('sequencing_center', Text),
    Column('instrument_model', Text),
    Column('paired_or_single_end', Text),
    Column('sequencing_read_length', Text),
    Column('index_sequence', Text),
    Column('target_coverage', Text),
    Column('lane_number', Text),
    Column('flow_cell_id', Text),
    Column('flow_cell_type', Text),
    Column('umi_barcode_read', Text),
    Column('umi_barcode_size', Text),
    Column('umi_barcode_offset', Text),
    Column('cell_barcode_read', Text),
    Column('cell_barcode_offset', Text),
    Column('cell_barcode_size', Text),
    Column('sample_barcode_read', Text),
    Column('type', Text),
    Column('description', Text),
    Column('has_attribute', Text),
)
tbl_study = Table('study', metadata, 
    Column('id', Text, primary_key=True),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('type', Text),
    Column('has_experiment', Text),
    Column('has_analysis', Text),
    Column('has_project', Text, ForeignKey('project.id')),
    Column('alias', Text),
    Column('title', Text),
    Column('description', Text),
    Column('has_publication', Text),
    Column('has_attribute', Text),
    Column('release_status', Text),
    Column('accession', Text),
    Column('ega_accession', Text),
    Column('release_date', Text),
)
tbl_submission = Table('submission', metadata, 
    Column('id', Text, primary_key=True),
    Column('has_study', Text, ForeignKey('study.id')),
    Column('has_project', Text, ForeignKey('project.id')),
    Column('has_sample', Text),
    Column('has_biospecimen', Text),
    Column('has_individual', Text),
    Column('has_experiment', Text),
    Column('has_protocol', Text),
    Column('has_analysis', Text),
    Column('has_file', Text),
    Column('has_publication', Text),
    Column('submission_date', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('submission_status', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
)
tbl_technology = Table('technology', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
)
tbl_user = Table('user', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('given_name', Text),
    Column('family_name', Text),
    Column('additional_name', Text),
    Column('email', Text),
    Column('role', Text),
)
tbl_workflow = Table('workflow', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
)
tbl_workflow_parameter = Table('workflow_parameter', metadata, 
    Column('key', Text, primary_key=True),
    Column('value', Text, primary_key=True),
    Column('workflow_step_id', Text, ForeignKey('workflow_step.id'), primary_key=True),
)
tbl_workflow_step = Table('workflow_step', metadata, 
    Column('id', Text, primary_key=True),
    Column('alias', Text),
    Column('creation_date', Text),
    Column('update_date', Text),
    Column('schema_type', Text),
    Column('schema_version', Text),
    Column('workflow_id', Text, ForeignKey('workflow.id')),
)
tbl_agent_xref = Table('agent_xref', metadata, 
    Column('backref_id', Text, ForeignKey('agent.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_analysis_xref = Table('analysis_xref', metadata, 
    Column('backref_id', Text, ForeignKey('analysis.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_analysis_process_xref = Table('analysis_process_xref', metadata, 
    Column('backref_id', Text, ForeignKey('analysis_process.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_anatomical_entity_xref = Table('anatomical_entity_xref', metadata, 
    Column('backref_id', Text, ForeignKey('anatomical_entity.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_ancestry_xref = Table('ancestry_xref', metadata, 
    Column('backref_id', Text, ForeignKey('ancestry.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_biospecimen_xref = Table('biospecimen_xref', metadata, 
    Column('backref_id', Text, ForeignKey('biospecimen.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_cell_line_xref = Table('cell_line_xref', metadata, 
    Column('backref_id', Text, ForeignKey('cell_line.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_cohort_xref = Table('cohort_xref', metadata, 
    Column('backref_id', Text, ForeignKey('cohort.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_data_access_committee_xref = Table('data_access_committee_xref', metadata, 
    Column('backref_id', Text, ForeignKey('data_access_committee.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_data_access_policy_xref = Table('data_access_policy_xref', metadata, 
    Column('backref_id', Text, ForeignKey('data_access_policy.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_data_use_condition_xref = Table('data_use_condition_xref', metadata, 
    Column('backref_id', Text, ForeignKey('data_use_condition.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_data_use_modifier_xref = Table('data_use_modifier_xref', metadata, 
    Column('backref_id', Text, ForeignKey('data_use_modifier.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_data_use_permission_xref = Table('data_use_permission_xref', metadata, 
    Column('backref_id', Text, ForeignKey('data_use_permission.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_dataset_xref = Table('dataset_xref', metadata, 
    Column('backref_id', Text, ForeignKey('dataset.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_disease_xref = Table('disease_xref', metadata, 
    Column('backref_id', Text, ForeignKey('disease.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_disease_or_phenotypic_feature_xref = Table('disease_or_phenotypic_feature_xref', metadata, 
    Column('backref_id', Text, ForeignKey('disease_or_phenotypic_feature.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_donor_xref = Table('donor_xref', metadata, 
    Column('backref_id', Text, ForeignKey('donor.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_experiment_xref = Table('experiment_xref', metadata, 
    Column('backref_id', Text, ForeignKey('experiment.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_experiment_process_xref = Table('experiment_process_xref', metadata, 
    Column('backref_id', Text, ForeignKey('experiment_process.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_family_xref = Table('family_xref', metadata, 
    Column('backref_id', Text, ForeignKey('family.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_file_xref = Table('file_xref', metadata, 
    Column('backref_id', Text, ForeignKey('file.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_individual_xref = Table('individual_xref', metadata, 
    Column('backref_id', Text, ForeignKey('individual.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_library_preparation_protocol_xref = Table('library_preparation_protocol_xref', metadata, 
    Column('backref_id', Text, ForeignKey('library_preparation_protocol.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_member_xref = Table('member_xref', metadata, 
    Column('backref_id', Text, ForeignKey('member.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_phenotypic_feature_xref = Table('phenotypic_feature_xref', metadata, 
    Column('backref_id', Text, ForeignKey('phenotypic_feature.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_project_xref = Table('project_xref', metadata, 
    Column('backref_id', Text, ForeignKey('project.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_protocol_xref = Table('protocol_xref', metadata, 
    Column('backref_id', Text, ForeignKey('protocol.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_publication_xref = Table('publication_xref', metadata, 
    Column('backref_id', Text, ForeignKey('publication.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_sample_xref = Table('sample_xref', metadata, 
    Column('backref_id', Text, ForeignKey('sample.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_sequencing_protocol_xref = Table('sequencing_protocol_xref', metadata, 
    Column('backref_id', Text, ForeignKey('sequencing_protocol.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_study_xref = Table('study_xref', metadata, 
    Column('backref_id', Text, ForeignKey('study.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_study_affiliation = Table('study_affiliation', metadata, 
    Column('backref_id', Text, ForeignKey('study.id'), primary_key=True),
    Column('affiliation', Text, primary_key=True),
)
tbl_technology_xref = Table('technology_xref', metadata, 
    Column('backref_id', Text, ForeignKey('technology.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_user_xref = Table('user_xref', metadata, 
    Column('backref_id', Text, ForeignKey('user.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_workflow_xref = Table('workflow_xref', metadata, 
    Column('backref_id', Text, ForeignKey('workflow.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
tbl_workflow_step_xref = Table('workflow_step_xref', metadata, 
    Column('backref_id', Text, ForeignKey('workflow_step.id'), primary_key=True),
    Column('xref', Text, primary_key=True),
)
mapper_registry.map_imperatively(Agent, tbl_agent, properties={
})
mapper_registry.map_imperatively(Analysis, tbl_analysis, properties={

    'has_analysis_process': 
        relationship(AnalysisProcess, 
                      foreign_keys=tbl_analysis_process.columns["analysis_id"],
                      backref='Analysis'),

})
mapper_registry.map_imperatively(AnalysisProcess, tbl_analysis_process, properties={
})
mapper_registry.map_imperatively(AnatomicalEntity, tbl_anatomical_entity, properties={
})
mapper_registry.map_imperatively(Ancestry, tbl_ancestry, properties={
})
mapper_registry.map_imperatively(Attribute, tbl_attribute, properties={
})
mapper_registry.map_imperatively(Biospecimen, tbl_biospecimen, properties={
})
mapper_registry.map_imperatively(CellLine, tbl_cell_line, properties={
})
mapper_registry.map_imperatively(Cohort, tbl_cohort, properties={
})
mapper_registry.map_imperatively(DataAccessCommittee, tbl_data_access_committee, properties={
})
mapper_registry.map_imperatively(DataAccessPolicy, tbl_data_access_policy, properties={

    'has_data_use_condition': 
        relationship(DataUseCondition, 
                      foreign_keys=tbl_data_use_condition.columns["data_access_policy_id"],
                      backref='DataAccessPolicy'),

})
mapper_registry.map_imperatively(DataUseCondition, tbl_data_use_condition, properties={
})
mapper_registry.map_imperatively(DataUseModifier, tbl_data_use_modifier, properties={
})
mapper_registry.map_imperatively(DataUsePermission, tbl_data_use_permission, properties={
})
mapper_registry.map_imperatively(Dataset, tbl_dataset, properties={
})
mapper_registry.map_imperatively(Disease, tbl_disease, properties={
})
mapper_registry.map_imperatively(DiseaseOrPhenotypicFeature, tbl_disease_or_phenotypic_feature, properties={
})
mapper_registry.map_imperatively(Donor, tbl_donor, properties={
})
mapper_registry.map_imperatively(Experiment, tbl_experiment, properties={

    'has_experiment_process': 
        relationship(ExperimentProcess, 
                      foreign_keys=tbl_experiment_process.columns["experiment_id"],
                      backref='Experiment'),

})
mapper_registry.map_imperatively(ExperimentProcess, tbl_experiment_process, properties={
})
mapper_registry.map_imperatively(Family, tbl_family, properties={
})
mapper_registry.map_imperatively(File, tbl_file, properties={
})
mapper_registry.map_imperatively(Individual, tbl_individual, properties={
})
mapper_registry.map_imperatively(LibraryPreparationProtocol, tbl_library_preparation_protocol, properties={
})
mapper_registry.map_imperatively(Member, tbl_member, properties={
})
mapper_registry.map_imperatively(PhenotypicFeature, tbl_phenotypic_feature, properties={
})
mapper_registry.map_imperatively(Project, tbl_project, properties={
})
mapper_registry.map_imperatively(Protocol, tbl_protocol, properties={
})
mapper_registry.map_imperatively(Publication, tbl_publication, properties={
})
mapper_registry.map_imperatively(Sample, tbl_sample, properties={
})
mapper_registry.map_imperatively(SequencingProtocol, tbl_sequencing_protocol, properties={
})
mapper_registry.map_imperatively(Study, tbl_study, properties={
})
mapper_registry.map_imperatively(Submission, tbl_submission, properties={
})
mapper_registry.map_imperatively(Technology, tbl_technology, properties={
})
mapper_registry.map_imperatively(User, tbl_user, properties={
})
mapper_registry.map_imperatively(Workflow, tbl_workflow, properties={

    'has_workflow_step': 
        relationship(WorkflowStep, 
                      foreign_keys=tbl_workflow_step.columns["workflow_id"],
                      backref='Workflow'),

})
mapper_registry.map_imperatively(WorkflowParameter, tbl_workflow_parameter, properties={
})
mapper_registry.map_imperatively(WorkflowStep, tbl_workflow_step, properties={

    'has_workflow_parameter': 
        relationship(WorkflowParameter, 
                      foreign_keys=tbl_workflow_parameter.columns["workflow_step_id"],
                      backref='WorkflowStep'),

})
