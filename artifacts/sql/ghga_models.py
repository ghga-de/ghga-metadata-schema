
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


tbl_activity = Table('activity', metadata, 
    Column('id', Text, primary_key=True),
)
tbl_anatomical_entity = Table('anatomical_entity', metadata, 
    Column('id', Text, primary_key=True),
)
tbl_attribute = Table('attribute', metadata, 
    Column('key', Text, primary_key=True),
    Column('key_type', Text, primary_key=True),
    Column('value', Text, primary_key=True),
    Column('value_type', Text, primary_key=True),
    Column('study_id', Text, ForeignKey('study.id'), primary_key=True),
)
tbl_biological_entity = Table('biological_entity', metadata, 
    Column('id', Text, primary_key=True),
)
tbl_cell_line = Table('cell_line', metadata, 
    Column('id', Text, primary_key=True),
)
tbl_committee = Table('committee', metadata, 
    Column('id', Text, primary_key=True),
)
tbl_data_access_committee = Table('data_access_committee', metadata, 
    Column('id', Text, primary_key=True),
    Column('title', Text),
    Column('description', Text),
    Column('main_contact', Text, ForeignKey('member.id')),
    Column('has_members', Text),
)
tbl_data_access_policy = Table('data_access_policy', metadata, 
    Column('id', Text, primary_key=True),
    Column('description', Text),
    Column('policy_text', Text),
    Column('policy_url', Text),
    Column('has_data_access_committee', Text, ForeignKey('data_access_committee.id')),
)
tbl_dataset = Table('dataset', metadata, 
    Column('id', Text, primary_key=True),
    Column('title', Text),
    Column('description', Text),
    Column('type', Text),
    Column('files', Text),
    Column('has_data_access_policy', Text, ForeignKey('data_access_policy.id')),
)
tbl_disease_or_phenotypic_feature = Table('disease_or_phenotypic_feature', metadata, 
    Column('id', Text, primary_key=True),
)
tbl_experiment = Table('experiment', metadata, 
    Column('id', Text, primary_key=True),
    Column('name', Text),
    Column('description', Text),
    Column('has_study', Text, ForeignKey('study.id')),
    Column('instrument_model', Text),
    Column('has_library', Text, ForeignKey('library.id')),
    Column('has_sample', Text, ForeignKey('sample.id')),
    Column('has_protocol', Text, ForeignKey('protocol.id')),
)
tbl_file = Table('file', metadata, 
    Column('id', Text, primary_key=True),
    Column('name', Text),
    Column('format', Text),
    Column('type', Text),
    Column('size', Text),
    Column('md5sum', Text),
    Column('file_index', Text),
    Column('category', Text),
)
tbl_individual = Table('individual', metadata, 
    Column('id', Text, primary_key=True),
    Column('name', Text),
    Column('gender', Text),
    Column('age', Text),
)
tbl_information_content_entity = Table('information_content_entity', metadata, 
    Column('id', Text, primary_key=True),
)
tbl_library = Table('library', metadata, 
    Column('id', Text, primary_key=True),
    Column('name', Text),
    Column('layout', Text),
    Column('source', Text),
    Column('selection', Text),
    Column('strategy', Text),
    Column('construction_protocol', Text),
)
tbl_material_entity = Table('material_entity', metadata, 
    Column('id', Text, primary_key=True),
)
tbl_member = Table('member', metadata, 
    Column('id', Text, primary_key=True),
    Column('name', Text),
    Column('title', Text),
    Column('email', Text),
    Column('telephone', Text),
    Column('organization', Text),
    Column('main_contact', Text, ForeignKey('member.id')),
)
tbl_named_thing = Table('named_thing', metadata, 
    Column('id', Text, primary_key=True),
)
tbl_person = Table('person', metadata, 
    Column('id', Text, primary_key=True),
)
tbl_processed_dataset = Table('processed_dataset', metadata, 
    Column('id', Text, primary_key=True),
    Column('title', Text),
    Column('description', Text),
    Column('type', Text),
    Column('files', Text),
    Column('has_data_access_policy', Text, ForeignKey('data_access_policy.id')),
)
tbl_protocol = Table('protocol', metadata, 
    Column('id', Text, primary_key=True),
)
tbl_publication = Table('publication', metadata, 
    Column('id', Text, primary_key=True),
    Column('title', Text),
    Column('study_id', Text, ForeignKey('study.id')),
)
tbl_research_activity = Table('research_activity', metadata, 
    Column('id', Text, primary_key=True),
)
tbl_sample = Table('sample', metadata, 
    Column('id', Text, primary_key=True),
    Column('name', Text),
    Column('type', Text),
    Column('description', Text),
    Column('subject', Text, ForeignKey('individual.id')),
    Column('biosample_accession', Text),
    Column('has_anatomical_site', Text, ForeignKey('anatomical_entity.id')),
    Column('has_cell_line', Text, ForeignKey('cell_line.id')),
    Column('geographical_region', Text),
    Column('has_disease_of_phenotypic_feature', Text, ForeignKey('disease_or_phenotypic_feature.id')),
    Column('files', Text),
)
tbl_study = Table('study', metadata, 
    Column('id', Text, primary_key=True),
    Column('title', Text),
    Column('type', Text),
    Column('name', Text),
    Column('abstract', Text),
)
tbl_synthetic_dataset = Table('synthetic_dataset', metadata, 
    Column('id', Text, primary_key=True),
    Column('title', Text),
    Column('description', Text),
    Column('type', Text),
    Column('files', Text),
    Column('has_data_access_policy', Text, ForeignKey('data_access_policy.id')),
)
mapper_registry.map_imperatively(Activity, tbl_activity, properties={
})
mapper_registry.map_imperatively(AnatomicalEntity, tbl_anatomical_entity, properties={
})
mapper_registry.map_imperatively(Attribute, tbl_attribute, properties={
})
mapper_registry.map_imperatively(BiologicalEntity, tbl_biological_entity, properties={
})
mapper_registry.map_imperatively(CellLine, tbl_cell_line, properties={
})
mapper_registry.map_imperatively(Committee, tbl_committee, properties={
})
mapper_registry.map_imperatively(DataAccessCommittee, tbl_data_access_committee, properties={
})
mapper_registry.map_imperatively(DataAccessPolicy, tbl_data_access_policy, properties={
})
mapper_registry.map_imperatively(Dataset, tbl_dataset, properties={
})
mapper_registry.map_imperatively(DiseaseOrPhenotypicFeature, tbl_disease_or_phenotypic_feature, properties={
})
mapper_registry.map_imperatively(Experiment, tbl_experiment, properties={
})
mapper_registry.map_imperatively(File, tbl_file, properties={
})
mapper_registry.map_imperatively(Individual, tbl_individual, properties={
})
mapper_registry.map_imperatively(InformationContentEntity, tbl_information_content_entity, properties={
})
mapper_registry.map_imperatively(Library, tbl_library, properties={
})
mapper_registry.map_imperatively(MaterialEntity, tbl_material_entity, properties={
})
mapper_registry.map_imperatively(Member, tbl_member, properties={
})
mapper_registry.map_imperatively(NamedThing, tbl_named_thing, properties={
})
mapper_registry.map_imperatively(Person, tbl_person, properties={
})
mapper_registry.map_imperatively(ProcessedDataset, tbl_processed_dataset, properties={
})
mapper_registry.map_imperatively(Protocol, tbl_protocol, properties={
})
mapper_registry.map_imperatively(Publication, tbl_publication, properties={
})
mapper_registry.map_imperatively(ResearchActivity, tbl_research_activity, properties={
})
mapper_registry.map_imperatively(Sample, tbl_sample, properties={
})
mapper_registry.map_imperatively(Study, tbl_study, properties={

    'publications': 
        relationship(publication, 
                      foreign_keys=tbl_publication.columns["study_id"],
                      backref='Study'),


    'attributes': 
        relationship(attribute, 
                      foreign_keys=tbl_attribute.columns["study_id"],
                      backref='Study'),

})
mapper_registry.map_imperatively(SyntheticDataset, tbl_synthetic_dataset, properties={
})
