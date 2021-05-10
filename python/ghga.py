# Auto generated from ghga.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-10 09:45
# Schema: GHGA-Schema
#
# id: https://w3id.org/my_core
# description: The GHGA Core Schema is similar to the EGA Schema.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from biolinkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from includes.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
GHGA = CurieNamespace('GHGA', 'https://w3id.org/GHGA/')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
DEFAULT_ = GHGA


# Types

# Class references
class NamedThingId(extended_str):
    pass


class StudyId(NamedThingId):
    pass


class SampleId(NamedThingId):
    pass


class ExperimentId(NamedThingId):
    pass


class DataAccessCommitteeId(NamedThingId):
    pass


class DataAccessPolicyId(NamedThingId):
    pass


class DatasetId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A databased entity, concept or class. This is a generic class that is the root of all the other classes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.NamedThing
    class_class_curie: ClassVar[str] = "GHGA:NamedThing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = GHGA.NamedThing

    id: Union[str, NamedThingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Study(NamedThing):
    """
    Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and
    analysis of a subject to learn more about the phenomenon being studied.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Study
    class_class_curie: ClassVar[str] = "GHGA:Study"
    class_name: ClassVar[str] = "study"
    class_model_uri: ClassVar[URIRef] = GHGA.Study

    id: Union[str, StudyId] = None
    descriptive_title: str = None
    study_type: str = None
    abstract: str = None
    short_name: Optional[str] = None
    pubmed_id: Optional[str] = None
    custom_tags: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self.descriptive_title is None:
            raise ValueError("descriptive_title must be supplied")
        if not isinstance(self.descriptive_title, str):
            self.descriptive_title = str(self.descriptive_title)

        if self.study_type is None:
            raise ValueError("study_type must be supplied")
        if not isinstance(self.study_type, str):
            self.study_type = str(self.study_type)

        if self.abstract is None:
            raise ValueError("abstract must be supplied")
        if not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.short_name is not None and not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if self.pubmed_id is not None and not isinstance(self.pubmed_id, str):
            self.pubmed_id = str(self.pubmed_id)

        if self.custom_tags is None:
            self.custom_tags = []
        if not isinstance(self.custom_tags, list):
            self.custom_tags = [self.custom_tags]
        self.custom_tags = [v if isinstance(v, str) else str(v) for v in self.custom_tags]

        super().__post_init__(**kwargs)


@dataclass
class Sample(NamedThing):
    """
    A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation,
    demonstration, or trial use. This could be either an individual, or sets of individuals from a population, or a
    portion of a substance like an isolate or tissue.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Sample
    class_class_curie: ClassVar[str] = "GHGA:Sample"
    class_name: ClassVar[str] = "sample"
    class_model_uri: ClassVar[URIRef] = GHGA.Sample

    id: Union[str, SampleId] = None
    alias: str = None
    subject_id: str = None
    gender: str = None
    phenotype_or_disease: str = None
    files: Union[str, List[str]] = None
    title: Optional[str] = None
    description: Optional[str] = None
    biosample_id: Optional[str] = None
    case_or_control: Optional[str] = None
    organism_part: Optional[str] = None
    cell_line: Optional[str] = None
    geographical_region: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self.alias is None:
            raise ValueError("alias must be supplied")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self.subject_id is None:
            raise ValueError("subject_id must be supplied")
        if not isinstance(self.subject_id, str):
            self.subject_id = str(self.subject_id)

        if self.gender is None:
            raise ValueError("gender must be supplied")
        if not isinstance(self.gender, str):
            self.gender = str(self.gender)

        if self.phenotype_or_disease is None:
            raise ValueError("phenotype_or_disease must be supplied")
        if not isinstance(self.phenotype_or_disease, str):
            self.phenotype_or_disease = str(self.phenotype_or_disease)

        if self.files is None:
            raise ValueError("files must be supplied")
        elif not isinstance(self.files, list):
            self.files = [self.files]
        elif len(self.files) == 0:
            raise ValueError(f"files must be a non-empty list")
        self.files = [v if isinstance(v, str) else str(v) for v in self.files]

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.biosample_id is not None and not isinstance(self.biosample_id, str):
            self.biosample_id = str(self.biosample_id)

        if self.case_or_control is not None and not isinstance(self.case_or_control, str):
            self.case_or_control = str(self.case_or_control)

        if self.organism_part is not None and not isinstance(self.organism_part, str):
            self.organism_part = str(self.organism_part)

        if self.cell_line is not None and not isinstance(self.cell_line, str):
            self.cell_line = str(self.cell_line)

        if self.geographical_region is not None and not isinstance(self.geographical_region, str):
            self.geographical_region = str(self.geographical_region)

        super().__post_init__(**kwargs)


@dataclass
class Experiment(NamedThing):
    """
    An experiment is an investigation that consists of a coordinated set of actions and observations designed to
    generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Experiment
    class_class_curie: ClassVar[str] = "GHGA:Experiment"
    class_name: ClassVar[str] = "experiment"
    class_model_uri: ClassVar[URIRef] = GHGA.Experiment

    id: Union[str, ExperimentId] = None
    related_study: str = None
    design_name: str = None
    instrument_model: str = None
    library_layout: str = None
    library_source: str = None
    library_selection: str = None
    library_strategy: str = None
    library_name: Optional[str] = None
    library_construction_protocol: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ExperimentId):
            self.id = ExperimentId(self.id)

        if self.related_study is None:
            raise ValueError("related_study must be supplied")
        if not isinstance(self.related_study, str):
            self.related_study = str(self.related_study)

        if self.design_name is None:
            raise ValueError("design_name must be supplied")
        if not isinstance(self.design_name, str):
            self.design_name = str(self.design_name)

        if self.instrument_model is None:
            raise ValueError("instrument_model must be supplied")
        if not isinstance(self.instrument_model, str):
            self.instrument_model = str(self.instrument_model)

        if self.library_layout is None:
            raise ValueError("library_layout must be supplied")
        if not isinstance(self.library_layout, str):
            self.library_layout = str(self.library_layout)

        if self.library_source is None:
            raise ValueError("library_source must be supplied")
        if not isinstance(self.library_source, str):
            self.library_source = str(self.library_source)

        if self.library_selection is None:
            raise ValueError("library_selection must be supplied")
        if not isinstance(self.library_selection, str):
            self.library_selection = str(self.library_selection)

        if self.library_strategy is None:
            raise ValueError("library_strategy must be supplied")
        if not isinstance(self.library_strategy, str):
            self.library_strategy = str(self.library_strategy)

        if self.library_name is not None and not isinstance(self.library_name, str):
            self.library_name = str(self.library_name)

        if self.library_construction_protocol is not None and not isinstance(self.library_construction_protocol, str):
            self.library_construction_protocol = str(self.library_construction_protocol)

        super().__post_init__(**kwargs)


@dataclass
class DataAccessCommittee(NamedThing):
    """
    A group of members that are delegated to grant access to one or more datasets after ensuring the minimum criteria
    for data sharing has been met, and request for data use does not raise ethical and/or legal concerns.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.DataAccessCommittee
    class_class_curie: ClassVar[str] = "GHGA:DataAccessCommittee"
    class_name: ClassVar[str] = "data access committee"
    class_model_uri: ClassVar[URIRef] = GHGA.DataAccessCommittee

    id: Union[str, DataAccessCommitteeId] = None
    title: str = None
    name: str = None
    telephone: str = None
    organization: str = None
    main_contact: str = None
    email: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DataAccessCommitteeId):
            self.id = DataAccessCommitteeId(self.id)

        if self.title is None:
            raise ValueError("title must be supplied")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.name is None:
            raise ValueError("name must be supplied")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.telephone is None:
            raise ValueError("telephone must be supplied")
        if not isinstance(self.telephone, str):
            self.telephone = str(self.telephone)

        if self.organization is None:
            raise ValueError("organization must be supplied")
        if not isinstance(self.organization, str):
            self.organization = str(self.organization)

        if self.main_contact is None:
            raise ValueError("main_contact must be supplied")
        if not isinstance(self.main_contact, str):
            self.main_contact = str(self.main_contact)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        super().__post_init__(**kwargs)


@dataclass
class DataAccessPolicy(NamedThing):
    """
    A data access policy specifies under which circumstances, legal or otherwise, a user can have access to one or
    more datasets belonging to one or more studies.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.DataAccessPolicy
    class_class_curie: ClassVar[str] = "GHGA:DataAccessPolicy"
    class_name: ClassVar[str] = "data access policy"
    class_model_uri: ClassVar[URIRef] = GHGA.DataAccessPolicy

    id: Union[str, DataAccessPolicyId] = None
    data_access_committees: str = None
    short_description: str = None
    policy: str = None
    policy_url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DataAccessPolicyId):
            self.id = DataAccessPolicyId(self.id)

        if self.data_access_committees is None:
            raise ValueError("data_access_committees must be supplied")
        if not isinstance(self.data_access_committees, str):
            self.data_access_committees = str(self.data_access_committees)

        if self.short_description is None:
            raise ValueError("short_description must be supplied")
        if not isinstance(self.short_description, str):
            self.short_description = str(self.short_description)

        if self.policy is None:
            raise ValueError("policy must be supplied")
        if not isinstance(self.policy, str):
            self.policy = str(self.policy)

        if self.policy_url is not None and not isinstance(self.policy_url, str):
            self.policy_url = str(self.policy_url)

        super().__post_init__(**kwargs)


@dataclass
class Dataset(NamedThing):
    """
    A dataset is a collection of files that represents data generated from a particular sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Dataset
    class_class_curie: ClassVar[str] = "GHGA:Dataset"
    class_name: ClassVar[str] = "dataset"
    class_model_uri: ClassVar[URIRef] = GHGA.Dataset

    id: Union[str, DatasetId] = None
    data_access_policies: str = None
    dataset_title: str = None
    dataset_description: str = None
    dataset_type: str = None
    files: Union[str, List[str]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if self.data_access_policies is None:
            raise ValueError("data_access_policies must be supplied")
        if not isinstance(self.data_access_policies, str):
            self.data_access_policies = str(self.data_access_policies)

        if self.dataset_title is None:
            raise ValueError("dataset_title must be supplied")
        if not isinstance(self.dataset_title, str):
            self.dataset_title = str(self.dataset_title)

        if self.dataset_description is None:
            raise ValueError("dataset_description must be supplied")
        if not isinstance(self.dataset_description, str):
            self.dataset_description = str(self.dataset_description)

        if self.dataset_type is None:
            raise ValueError("dataset_type must be supplied")
        if not isinstance(self.dataset_type, str):
            self.dataset_type = str(self.dataset_type)

        if self.files is None:
            raise ValueError("files must be supplied")
        elif not isinstance(self.files, list):
            self.files = [self.files]
        elif len(self.files) == 0:
            raise ValueError(f"files must be a non-empty list")
        self.files = [v if isinstance(v, str) else str(v) for v in self.files]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=GHGA.id, name="id", curie=GHGA.curie('id'),
                   model_uri=GHGA.id, domain=None, range=URIRef)

slots.descriptive_title = Slot(uri=GHGA.descriptive_title, name="descriptive title", curie=GHGA.curie('descriptive_title'),
                   model_uri=GHGA.descriptive_title, domain=None, range=Optional[str])

slots.study_type = Slot(uri=GHGA.study_type, name="study type", curie=GHGA.curie('study_type'),
                   model_uri=GHGA.study_type, domain=None, range=Optional[str])

slots.short_name = Slot(uri=GHGA.short_name, name="short name", curie=GHGA.curie('short_name'),
                   model_uri=GHGA.short_name, domain=None, range=Optional[str])

slots.abstract = Slot(uri=GHGA.abstract, name="abstract", curie=GHGA.curie('abstract'),
                   model_uri=GHGA.abstract, domain=None, range=Optional[str])

slots.pubmed_id = Slot(uri=GHGA.pubmed_id, name="pubmed id", curie=GHGA.curie('pubmed_id'),
                   model_uri=GHGA.pubmed_id, domain=None, range=Optional[str])

slots.custom_tags = Slot(uri=GHGA.custom_tags, name="custom tags", curie=GHGA.curie('custom_tags'),
                   model_uri=GHGA.custom_tags, domain=None, range=Optional[str])

slots.title = Slot(uri=GHGA.title, name="title", curie=GHGA.curie('title'),
                   model_uri=GHGA.title, domain=None, range=Optional[str])

slots.alias = Slot(uri=GHGA.alias, name="alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.alias, domain=None, range=Optional[str])

slots.description = Slot(uri=GHGA.description, name="description", curie=GHGA.curie('description'),
                   model_uri=GHGA.description, domain=None, range=Optional[str])

slots.subject_id = Slot(uri=GHGA.subject_id, name="subject id", curie=GHGA.curie('subject_id'),
                   model_uri=GHGA.subject_id, domain=None, range=Optional[str])

slots.biosample_id = Slot(uri=GHGA.biosample_id, name="biosample id", curie=GHGA.curie('biosample_id'),
                   model_uri=GHGA.biosample_id, domain=None, range=Optional[str])

slots.case_or_control = Slot(uri=GHGA.case_or_control, name="case or control", curie=GHGA.curie('case_or_control'),
                   model_uri=GHGA.case_or_control, domain=None, range=Optional[str])

slots.gender = Slot(uri=GHGA.gender, name="gender", curie=GHGA.curie('gender'),
                   model_uri=GHGA.gender, domain=None, range=Optional[str])

slots.organism_part = Slot(uri=GHGA.organism_part, name="organism part", curie=GHGA.curie('organism_part'),
                   model_uri=GHGA.organism_part, domain=None, range=Optional[str])

slots.cell_line = Slot(uri=GHGA.cell_line, name="cell line", curie=GHGA.curie('cell_line'),
                   model_uri=GHGA.cell_line, domain=None, range=Optional[str])

slots.geographical_region = Slot(uri=GHGA.geographical_region, name="geographical region", curie=GHGA.curie('geographical_region'),
                   model_uri=GHGA.geographical_region, domain=None, range=Optional[str])

slots.phenotype_or_disease = Slot(uri=GHGA.phenotype_or_disease, name="phenotype or disease", curie=GHGA.curie('phenotype_or_disease'),
                   model_uri=GHGA.phenotype_or_disease, domain=None, range=Optional[str])

slots.files = Slot(uri=GHGA.files, name="files", curie=GHGA.curie('files'),
                   model_uri=GHGA.files, domain=None, range=Optional[Union[str, List[str]]])

slots.related_study = Slot(uri=GHGA.related_study, name="related study", curie=GHGA.curie('related_study'),
                   model_uri=GHGA.related_study, domain=None, range=Optional[str])

slots.design_name = Slot(uri=GHGA.design_name, name="design name", curie=GHGA.curie('design_name'),
                   model_uri=GHGA.design_name, domain=None, range=Optional[str])

slots.instrument_model = Slot(uri=GHGA.instrument_model, name="instrument model", curie=GHGA.curie('instrument_model'),
                   model_uri=GHGA.instrument_model, domain=None, range=Optional[str])

slots.library_name = Slot(uri=GHGA.library_name, name="library name", curie=GHGA.curie('library_name'),
                   model_uri=GHGA.library_name, domain=None, range=Optional[str])

slots.library_layout = Slot(uri=GHGA.library_layout, name="library layout", curie=GHGA.curie('library_layout'),
                   model_uri=GHGA.library_layout, domain=None, range=Optional[str])

slots.library_source = Slot(uri=GHGA.library_source, name="library source", curie=GHGA.curie('library_source'),
                   model_uri=GHGA.library_source, domain=None, range=Optional[str])

slots.library_selection = Slot(uri=GHGA.library_selection, name="library selection", curie=GHGA.curie('library_selection'),
                   model_uri=GHGA.library_selection, domain=None, range=Optional[str])

slots.library_strategy = Slot(uri=GHGA.library_strategy, name="library strategy", curie=GHGA.curie('library_strategy'),
                   model_uri=GHGA.library_strategy, domain=None, range=Optional[str])

slots.library_construction_protocol = Slot(uri=GHGA.library_construction_protocol, name="library construction protocol", curie=GHGA.curie('library_construction_protocol'),
                   model_uri=GHGA.library_construction_protocol, domain=None, range=Optional[str])

slots.name = Slot(uri=GHGA.name, name="name", curie=GHGA.curie('name'),
                   model_uri=GHGA.name, domain=None, range=Optional[str])

slots.telephone = Slot(uri=GHGA.telephone, name="telephone", curie=GHGA.curie('telephone'),
                   model_uri=GHGA.telephone, domain=None, range=Optional[str])

slots.organization = Slot(uri=GHGA.organization, name="organization", curie=GHGA.curie('organization'),
                   model_uri=GHGA.organization, domain=None, range=Optional[str])

slots.email = Slot(uri=GHGA.email, name="email", curie=GHGA.curie('email'),
                   model_uri=GHGA.email, domain=None, range=Optional[str])

slots.main_contact = Slot(uri=GHGA.main_contact, name="main contact", curie=GHGA.curie('main_contact'),
                   model_uri=GHGA.main_contact, domain=None, range=Optional[str])

slots.data_access_committees = Slot(uri=GHGA.data_access_committees, name="data access committees", curie=GHGA.curie('data_access_committees'),
                   model_uri=GHGA.data_access_committees, domain=None, range=Optional[str])

slots.short_description = Slot(uri=GHGA.short_description, name="short description", curie=GHGA.curie('short_description'),
                   model_uri=GHGA.short_description, domain=None, range=Optional[str])

slots.policy = Slot(uri=GHGA.policy, name="policy", curie=GHGA.curie('policy'),
                   model_uri=GHGA.policy, domain=None, range=Optional[str])

slots.policy_url = Slot(uri=GHGA.policy_url, name="policy url", curie=GHGA.curie('policy_url'),
                   model_uri=GHGA.policy_url, domain=None, range=Optional[str])

slots.data_access_policies = Slot(uri=GHGA.data_access_policies, name="data access policies", curie=GHGA.curie('data_access_policies'),
                   model_uri=GHGA.data_access_policies, domain=None, range=Optional[str])

slots.dataset_title = Slot(uri=GHGA.dataset_title, name="dataset title", curie=GHGA.curie('dataset_title'),
                   model_uri=GHGA.dataset_title, domain=None, range=Optional[str])

slots.dataset_description = Slot(uri=GHGA.dataset_description, name="dataset description", curie=GHGA.curie('dataset_description'),
                   model_uri=GHGA.dataset_description, domain=None, range=Optional[str])

slots.dataset_type = Slot(uri=GHGA.dataset_type, name="dataset type", curie=GHGA.curie('dataset_type'),
                   model_uri=GHGA.dataset_type, domain=None, range=Optional[str])

slots.study_descriptive_title = Slot(uri=GHGA.descriptive_title, name="study_descriptive title", curie=GHGA.curie('descriptive_title'),
                   model_uri=GHGA.study_descriptive_title, domain=Study, range=str)

slots.study_study_type = Slot(uri=GHGA.study_type, name="study_study type", curie=GHGA.curie('study_type'),
                   model_uri=GHGA.study_study_type, domain=Study, range=str)

slots.study_abstract = Slot(uri=GHGA.abstract, name="study_abstract", curie=GHGA.curie('abstract'),
                   model_uri=GHGA.study_abstract, domain=Study, range=str)

slots.study_custom_tags = Slot(uri=GHGA.custom_tags, name="study_custom tags", curie=GHGA.curie('custom_tags'),
                   model_uri=GHGA.study_custom_tags, domain=Study, range=Optional[Union[str, List[str]]])

slots.sample_title = Slot(uri=GHGA.title, name="sample_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.sample_title, domain=Sample, range=Optional[str])

slots.sample_alias = Slot(uri=GHGA.alias, name="sample_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.sample_alias, domain=Sample, range=str)

slots.sample_subject_id = Slot(uri=GHGA.subject_id, name="sample_subject id", curie=GHGA.curie('subject_id'),
                   model_uri=GHGA.sample_subject_id, domain=Sample, range=str)

slots.sample_gender = Slot(uri=GHGA.gender, name="sample_gender", curie=GHGA.curie('gender'),
                   model_uri=GHGA.sample_gender, domain=Sample, range=str)

slots.sample_phenotype_or_disease = Slot(uri=GHGA.phenotype_or_disease, name="sample_phenotype or disease", curie=GHGA.curie('phenotype_or_disease'),
                   model_uri=GHGA.sample_phenotype_or_disease, domain=Sample, range=str)

slots.sample_files = Slot(uri=GHGA.files, name="sample_files", curie=GHGA.curie('files'),
                   model_uri=GHGA.sample_files, domain=Sample, range=Union[str, List[str]])

slots.experiment_related_study = Slot(uri=GHGA.related_study, name="experiment_related study", curie=GHGA.curie('related_study'),
                   model_uri=GHGA.experiment_related_study, domain=Experiment, range=str)

slots.experiment_design_name = Slot(uri=GHGA.design_name, name="experiment_design name", curie=GHGA.curie('design_name'),
                   model_uri=GHGA.experiment_design_name, domain=Experiment, range=str)

slots.experiment_instrument_model = Slot(uri=GHGA.instrument_model, name="experiment_instrument model", curie=GHGA.curie('instrument_model'),
                   model_uri=GHGA.experiment_instrument_model, domain=Experiment, range=str)

slots.experiment_library_layout = Slot(uri=GHGA.library_layout, name="experiment_library layout", curie=GHGA.curie('library_layout'),
                   model_uri=GHGA.experiment_library_layout, domain=Experiment, range=str)

slots.experiment_library_source = Slot(uri=GHGA.library_source, name="experiment_library source", curie=GHGA.curie('library_source'),
                   model_uri=GHGA.experiment_library_source, domain=Experiment, range=str)

slots.experiment_library_selection = Slot(uri=GHGA.library_selection, name="experiment_library selection", curie=GHGA.curie('library_selection'),
                   model_uri=GHGA.experiment_library_selection, domain=Experiment, range=str)

slots.experiment_library_strategy = Slot(uri=GHGA.library_strategy, name="experiment_library strategy", curie=GHGA.curie('library_strategy'),
                   model_uri=GHGA.experiment_library_strategy, domain=Experiment, range=str)

slots.data_access_committee_title = Slot(uri=GHGA.title, name="data access committee_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.data_access_committee_title, domain=DataAccessCommittee, range=str)

slots.data_access_committee_name = Slot(uri=GHGA.name, name="data access committee_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.data_access_committee_name, domain=DataAccessCommittee, range=str)

slots.data_access_committee_telephone = Slot(uri=GHGA.telephone, name="data access committee_telephone", curie=GHGA.curie('telephone'),
                   model_uri=GHGA.data_access_committee_telephone, domain=DataAccessCommittee, range=str)

slots.data_access_committee_organization = Slot(uri=GHGA.organization, name="data access committee_organization", curie=GHGA.curie('organization'),
                   model_uri=GHGA.data_access_committee_organization, domain=DataAccessCommittee, range=str)

slots.data_access_committee_main_contact = Slot(uri=GHGA.main_contact, name="data access committee_main contact", curie=GHGA.curie('main_contact'),
                   model_uri=GHGA.data_access_committee_main_contact, domain=DataAccessCommittee, range=str)

slots.data_access_policy_data_access_committees = Slot(uri=GHGA.data_access_committees, name="data access policy_data access committees", curie=GHGA.curie('data_access_committees'),
                   model_uri=GHGA.data_access_policy_data_access_committees, domain=DataAccessPolicy, range=str)

slots.data_access_policy_short_description = Slot(uri=GHGA.short_description, name="data access policy_short description", curie=GHGA.curie('short_description'),
                   model_uri=GHGA.data_access_policy_short_description, domain=DataAccessPolicy, range=str)

slots.data_access_policy_policy = Slot(uri=GHGA.policy, name="data access policy_policy", curie=GHGA.curie('policy'),
                   model_uri=GHGA.data_access_policy_policy, domain=DataAccessPolicy, range=str)

slots.dataset_data_access_policies = Slot(uri=GHGA.data_access_policies, name="dataset_data access policies", curie=GHGA.curie('data_access_policies'),
                   model_uri=GHGA.dataset_data_access_policies, domain=Dataset, range=str)

slots.dataset_dataset_title = Slot(uri=GHGA.dataset_title, name="dataset_dataset title", curie=GHGA.curie('dataset_title'),
                   model_uri=GHGA.dataset_dataset_title, domain=Dataset, range=str)

slots.dataset_dataset_description = Slot(uri=GHGA.dataset_description, name="dataset_dataset description", curie=GHGA.curie('dataset_description'),
                   model_uri=GHGA.dataset_dataset_description, domain=Dataset, range=str)

slots.dataset_dataset_type = Slot(uri=GHGA.dataset_type, name="dataset_dataset type", curie=GHGA.curie('dataset_type'),
                   model_uri=GHGA.dataset_dataset_type, domain=Dataset, range=str)

slots.dataset_files = Slot(uri=GHGA.files, name="dataset_files", curie=GHGA.curie('files'),
                   model_uri=GHGA.dataset_files, domain=Dataset, range=Union[str, List[str]])
