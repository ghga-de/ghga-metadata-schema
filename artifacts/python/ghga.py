# Auto generated from ghga.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-07-13 11:36
# Schema: GHGA-Metadata-Schema
#
# id: https://w3id.org/GHGA-Metadata-Schema
# description: The metadata schema for the German Human Genome-Phenome Archive (GHGA).
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
GHGA = CurieNamespace('GHGA', 'https://w3id.org/GHGA/')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = GHGA


# Types

# Class references
class NamedThingId(extended_str):
    pass


class CommitteeId(NamedThingId):
    pass


class DataAccessCommitteeId(CommitteeId):
    pass


class ActivityId(NamedThingId):
    pass


class ResearchActivityId(ActivityId):
    pass


class StudyId(ResearchActivityId):
    pass


class ExperimentId(ResearchActivityId):
    pass


class BiologicalEntityId(NamedThingId):
    pass


class SampleId(BiologicalEntityId):
    pass


class AnatomicalEntityId(BiologicalEntityId):
    pass


class CellLineId(BiologicalEntityId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class ProtocolId(InformationContentEntityId):
    pass


class FileId(InformationContentEntityId):
    pass


class DatasetId(InformationContentEntityId):
    pass


class SyntheticDatasetId(DatasetId):
    pass


class ProcessedDatasetId(DatasetId):
    pass


class DataAccessPolicyId(InformationContentEntityId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class DiseaseOrPhenotypicFeatureId(BiologicalEntityId):
    pass


class MaterialEntityId(NamedThingId):
    pass


class LibraryId(MaterialEntityId):
    pass


class PersonId(NamedThingId):
    pass


class IndividualId(PersonId):
    pass


class MemberId(PersonId):
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
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Attribute(YAMLRoot):
    """
    A key/value pair that further characterizes an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Attribute
    class_class_curie: ClassVar[str] = "GHGA:Attribute"
    class_name: ClassVar[str] = "attribute"
    class_model_uri: ClassVar[URIRef] = GHGA.Attribute

    key: str = None
    value: str = None
    key_type: Optional[str] = None
    value_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, str):
            self.key = str(self.key)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.key_type is not None and not isinstance(self.key_type, str):
            self.key_type = str(self.key_type)

        if self.value_type is not None and not isinstance(self.value_type, str):
            self.value_type = str(self.value_type)

        super().__post_init__(**kwargs)


@dataclass
class Committee(NamedThing):
    """
    A group of people organized for a specific purpose.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Committee
    class_class_curie: ClassVar[str] = "GHGA:Committee"
    class_name: ClassVar[str] = "committee"
    class_model_uri: ClassVar[URIRef] = GHGA.Committee

    id: Union[str, CommitteeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommitteeId):
            self.id = CommitteeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DataAccessCommittee(Committee):
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
    description: Optional[str] = None
    main_contact: Optional[Union[str, MemberId]] = None
    has_members: Optional[Union[Union[str, MemberId], List[Union[str, MemberId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataAccessCommitteeId):
            self.id = DataAccessCommitteeId(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.main_contact is not None and not isinstance(self.main_contact, MemberId):
            self.main_contact = MemberId(self.main_contact)

        if not isinstance(self.has_members, list):
            self.has_members = [self.has_members] if self.has_members is not None else []
        self.has_members = [v if isinstance(v, MemberId) else MemberId(v) for v in self.has_members]

        super().__post_init__(**kwargs)


@dataclass
class Activity(NamedThing):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include
    consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Activity
    class_class_curie: ClassVar[str] = "GHGA:Activity"
    class_name: ClassVar[str] = "activity"
    class_model_uri: ClassVar[URIRef] = GHGA.Activity

    id: Union[str, ActivityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ResearchActivity(Activity):
    """
    A planned process executed in the performance of scientific research wherein systematic investigations are
    performed to establish facts and reach new conclusions about phenomena in the world.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.ResearchActivity
    class_class_curie: ClassVar[str] = "GHGA:ResearchActivity"
    class_name: ClassVar[str] = "research activity"
    class_model_uri: ClassVar[URIRef] = GHGA.ResearchActivity

    id: Union[str, ResearchActivityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResearchActivityId):
            self.id = ResearchActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Study(ResearchActivity):
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
    title: str = None
    type: str = None
    abstract: str = None
    name: Optional[str] = None
    publications: Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]] = empty_list()
    attributes: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.abstract):
            self.MissingRequiredField("abstract")
        if not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.publications, list):
            self.publications = [self.publications] if self.publications is not None else []
        self.publications = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.publications]

        self._normalize_inlined_as_dict(slot_name="attributes", slot_type=Attribute, key_name="key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Experiment(ResearchActivity):
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
    name: str = None
    has_study: Union[str, StudyId] = None
    instrument_model: str = None
    has_library: Union[str, LibraryId] = None
    has_sample: Union[str, SampleId] = None
    description: Optional[str] = None
    has_protocol: Optional[Union[str, ProtocolId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExperimentId):
            self.id = ExperimentId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.has_study):
            self.MissingRequiredField("has_study")
        if not isinstance(self.has_study, StudyId):
            self.has_study = StudyId(self.has_study)

        if self._is_empty(self.instrument_model):
            self.MissingRequiredField("instrument_model")
        if not isinstance(self.instrument_model, str):
            self.instrument_model = str(self.instrument_model)

        if self._is_empty(self.has_library):
            self.MissingRequiredField("has_library")
        if not isinstance(self.has_library, LibraryId):
            self.has_library = LibraryId(self.has_library)

        if self._is_empty(self.has_sample):
            self.MissingRequiredField("has_sample")
        if not isinstance(self.has_sample, SampleId):
            self.has_sample = SampleId(self.has_sample)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.has_protocol is not None and not isinstance(self.has_protocol, ProtocolId):
            self.has_protocol = ProtocolId(self.has_protocol)

        super().__post_init__(**kwargs)


@dataclass
class BiologicalEntity(NamedThing):
    """
    A biological entity is a heterogeneous substance that contains genomic material or is the product of a biological
    process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.BiologicalEntity
    class_class_curie: ClassVar[str] = "GHGA:BiologicalEntity"
    class_name: ClassVar[str] = "biological entity"
    class_model_uri: ClassVar[URIRef] = GHGA.BiologicalEntity

    id: Union[str, BiologicalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalEntityId):
            self.id = BiologicalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Sample(BiologicalEntity):
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
    subject: Union[str, IndividualId] = None
    has_disease_of_phenotypic_feature: Union[str, DiseaseOrPhenotypicFeatureId] = None
    files: Union[Union[str, FileId], List[Union[str, FileId]]] = None
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    biosample_accession: Optional[str] = None
    has_anatomical_site: Optional[Union[str, AnatomicalEntityId]] = None
    has_cell_line: Optional[Union[str, CellLineId]] = None
    geographical_region: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, IndividualId):
            self.subject = IndividualId(self.subject)

        if self._is_empty(self.has_disease_of_phenotypic_feature):
            self.MissingRequiredField("has_disease_of_phenotypic_feature")
        if not isinstance(self.has_disease_of_phenotypic_feature, DiseaseOrPhenotypicFeatureId):
            self.has_disease_of_phenotypic_feature = DiseaseOrPhenotypicFeatureId(self.has_disease_of_phenotypic_feature)

        if self._is_empty(self.files):
            self.MissingRequiredField("files")
        if not isinstance(self.files, list):
            self.files = [self.files] if self.files is not None else []
        self.files = [v if isinstance(v, FileId) else FileId(v) for v in self.files]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.biosample_accession is not None and not isinstance(self.biosample_accession, str):
            self.biosample_accession = str(self.biosample_accession)

        if self.has_anatomical_site is not None and not isinstance(self.has_anatomical_site, AnatomicalEntityId):
            self.has_anatomical_site = AnatomicalEntityId(self.has_anatomical_site)

        if self.has_cell_line is not None and not isinstance(self.has_cell_line, CellLineId):
            self.has_cell_line = CellLineId(self.has_cell_line)

        if self.geographical_region is not None and not isinstance(self.geographical_region, str):
            self.geographical_region = str(self.geographical_region)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntity(BiologicalEntity):
    """
    An anatomical entity is an object that is a structural part (material or immaterial) of a biological entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.AnatomicalEntity
    class_class_curie: ClassVar[str] = "GHGA:AnatomicalEntity"
    class_name: ClassVar[str] = "anatomical entity"
    class_model_uri: ClassVar[URIRef] = GHGA.AnatomicalEntity

    id: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CellLine(BiologicalEntity):
    """
    A cultured cell population that represents a genetically stable and homogenous population of cultured cells that
    shares a common propagation history
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CellLine
    class_class_curie: ClassVar[str] = "GHGA:CellLine"
    class_name: ClassVar[str] = "cell line"
    class_model_uri: ClassVar[URIRef] = GHGA.CellLine

    id: Union[str, CellLineId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellLineId):
            self.id = CellLineId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class InformationContentEntity(NamedThing):
    """
    A generically dependent continuant that is about some thing.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.InformationContentEntity
    class_class_curie: ClassVar[str] = "GHGA:InformationContentEntity"
    class_name: ClassVar[str] = "information content entity"
    class_model_uri: ClassVar[URIRef] = GHGA.InformationContentEntity

    id: Union[str, InformationContentEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationContentEntityId):
            self.id = InformationContentEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Protocol(InformationContentEntity):
    """
    A plan specification which has sufficient level of detail and quantitative information to communicate it between
    investigation agents, so that different investigation agents will reliably be able to independently reproduce the
    process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Protocol
    class_class_curie: ClassVar[str] = "GHGA:Protocol"
    class_name: ClassVar[str] = "protocol"
    class_model_uri: ClassVar[URIRef] = GHGA.Protocol

    id: Union[str, ProtocolId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProtocolId):
            self.id = ProtocolId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class File(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.File
    class_class_curie: ClassVar[str] = "GHGA:File"
    class_name: ClassVar[str] = "file"
    class_model_uri: ClassVar[URIRef] = GHGA.File

    id: Union[str, FileId] = None
    name: Optional[str] = None
    format: Optional[str] = None
    type: Optional[str] = None
    size: Optional[str] = None
    md5sum: Optional[str] = None
    file_index: Optional[str] = None
    category: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FileId):
            self.id = FileId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.size is not None and not isinstance(self.size, str):
            self.size = str(self.size)

        if self.md5sum is not None and not isinstance(self.md5sum, str):
            self.md5sum = str(self.md5sum)

        if self.file_index is not None and not isinstance(self.file_index, str):
            self.file_index = str(self.file_index)

        if self.category is not None and not isinstance(self.category, str):
            self.category = str(self.category)

        super().__post_init__(**kwargs)


@dataclass
class Dataset(InformationContentEntity):
    """
    A dataset is a collection of files that represents data generated from a particular sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Dataset
    class_class_curie: ClassVar[str] = "GHGA:Dataset"
    class_name: ClassVar[str] = "dataset"
    class_model_uri: ClassVar[URIRef] = GHGA.Dataset

    id: Union[str, DatasetId] = None
    title: str = None
    description: str = None
    type: str = None
    files: Union[Union[str, FileId], List[Union[str, FileId]]] = None
    has_data_access_policy: Union[str, DataAccessPolicyId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self._is_empty(self.files):
            self.MissingRequiredField("files")
        if not isinstance(self.files, list):
            self.files = [self.files] if self.files is not None else []
        self.files = [v if isinstance(v, FileId) else FileId(v) for v in self.files]

        if self._is_empty(self.has_data_access_policy):
            self.MissingRequiredField("has_data_access_policy")
        if not isinstance(self.has_data_access_policy, DataAccessPolicyId):
            self.has_data_access_policy = DataAccessPolicyId(self.has_data_access_policy)

        super().__post_init__(**kwargs)


@dataclass
class SyntheticDataset(Dataset):
    """
    A dataset that is built by combining one or more datasets.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.SyntheticDataset
    class_class_curie: ClassVar[str] = "GHGA:SyntheticDataset"
    class_name: ClassVar[str] = "synthetic dataset"
    class_model_uri: ClassVar[URIRef] = GHGA.SyntheticDataset

    id: Union[str, SyntheticDatasetId] = None
    title: str = None
    description: str = None
    type: str = None
    files: Union[Union[str, FileId], List[Union[str, FileId]]] = None
    has_data_access_policy: Union[str, DataAccessPolicyId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SyntheticDatasetId):
            self.id = SyntheticDatasetId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ProcessedDataset(Dataset):
    """
    A dataset that is generated by processing an existing dataset.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.ProcessedDataset
    class_class_curie: ClassVar[str] = "GHGA:ProcessedDataset"
    class_name: ClassVar[str] = "processed dataset"
    class_model_uri: ClassVar[URIRef] = GHGA.ProcessedDataset

    id: Union[str, ProcessedDatasetId] = None
    title: str = None
    description: str = None
    type: str = None
    files: Union[Union[str, FileId], List[Union[str, FileId]]] = None
    has_data_access_policy: Union[str, DataAccessPolicyId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessedDatasetId):
            self.id = ProcessedDatasetId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DataAccessPolicy(InformationContentEntity):
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
    description: str = None
    policy_text: str = None
    has_data_access_committee: Union[str, DataAccessCommitteeId] = None
    policy_url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataAccessPolicyId):
            self.id = DataAccessPolicyId(self.id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.policy_text):
            self.MissingRequiredField("policy_text")
        if not isinstance(self.policy_text, str):
            self.policy_text = str(self.policy_text)

        if self._is_empty(self.has_data_access_committee):
            self.MissingRequiredField("has_data_access_committee")
        if not isinstance(self.has_data_access_committee, DataAccessCommitteeId):
            self.has_data_access_committee = DataAccessCommitteeId(self.has_data_access_committee)

        if self.policy_url is not None and not isinstance(self.policy_url, str):
            self.policy_url = str(self.policy_url)

        super().__post_init__(**kwargs)


@dataclass
class Publication(InformationContentEntity):
    """
    Represents a publication.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Publication
    class_class_curie: ClassVar[str] = "GHGA:Publication"
    class_name: ClassVar[str] = "publication"
    class_model_uri: ClassVar[URIRef] = GHGA.Publication

    id: Union[str, PublicationId] = None
    title: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseOrPhenotypicFeature(BiologicalEntity):
    """
    A disease or phenotypic feature.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.DiseaseOrPhenotypicFeature
    class_class_curie: ClassVar[str] = "GHGA:DiseaseOrPhenotypicFeature"
    class_name: ClassVar[str] = "disease or phenotypic feature"
    class_model_uri: ClassVar[URIRef] = GHGA.DiseaseOrPhenotypicFeature

    id: Union[str, DiseaseOrPhenotypicFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureId):
            self.id = DiseaseOrPhenotypicFeatureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntity(NamedThing):
    """
    A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has
    mass.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.MaterialEntity
    class_class_curie: ClassVar[str] = "GHGA:MaterialEntity"
    class_name: ClassVar[str] = "material entity"
    class_model_uri: ClassVar[URIRef] = GHGA.MaterialEntity

    id: Union[str, MaterialEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Library(MaterialEntity):
    """
    A library that is used in an experiment protocol to generate the input for an instrument.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Library
    class_class_curie: ClassVar[str] = "GHGA:Library"
    class_name: ClassVar[str] = "library"
    class_model_uri: ClassVar[URIRef] = GHGA.Library

    id: Union[str, LibraryId] = None
    layout: str = None
    source: str = None
    selection: str = None
    strategy: str = None
    name: Optional[str] = None
    construction_protocol: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LibraryId):
            self.id = LibraryId(self.id)

        if self._is_empty(self.layout):
            self.MissingRequiredField("layout")
        if not isinstance(self.layout, str):
            self.layout = str(self.layout)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.selection):
            self.MissingRequiredField("selection")
        if not isinstance(self.selection, str):
            self.selection = str(self.selection)

        if self._is_empty(self.strategy):
            self.MissingRequiredField("strategy")
        if not isinstance(self.strategy, str):
            self.strategy = str(self.strategy)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.construction_protocol is not None and not isinstance(self.construction_protocol, str):
            self.construction_protocol = str(self.construction_protocol)

        super().__post_init__(**kwargs)


@dataclass
class Person(NamedThing):
    """
    A member of the species Homo sapiens.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Person
    class_class_curie: ClassVar[str] = "GHGA:Person"
    class_name: ClassVar[str] = "person"
    class_model_uri: ClassVar[URIRef] = GHGA.Person

    id: Union[str, PersonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Individual(Person):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Individual
    class_class_curie: ClassVar[str] = "GHGA:Individual"
    class_name: ClassVar[str] = "individual"
    class_model_uri: ClassVar[URIRef] = GHGA.Individual

    id: Union[str, IndividualId] = None
    gender: str = None
    name: Optional[str] = None
    age: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IndividualId):
            self.id = IndividualId(self.id)

        if self._is_empty(self.gender):
            self.MissingRequiredField("gender")
        if not isinstance(self.gender, str):
            self.gender = str(self.gender)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.age is not None and not isinstance(self.age, int):
            self.age = int(self.age)

        super().__post_init__(**kwargs)


@dataclass
class Member(Person):
    """
    Member of an organization or a committee.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Member
    class_class_curie: ClassVar[str] = "GHGA:Member"
    class_name: ClassVar[str] = "member"
    class_model_uri: ClassVar[URIRef] = GHGA.Member

    id: Union[str, MemberId] = None
    name: str = None
    telephone: str = None
    organization: str = None
    main_contact: Union[str, MemberId] = None
    title: Optional[str] = None
    email: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MemberId):
            self.id = MemberId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.telephone):
            self.MissingRequiredField("telephone")
        if not isinstance(self.telephone, str):
            self.telephone = str(self.telephone)

        if self._is_empty(self.organization):
            self.MissingRequiredField("organization")
        if not isinstance(self.organization, str):
            self.organization = str(self.organization)

        if self._is_empty(self.main_contact):
            self.MissingRequiredField("main_contact")
        if not isinstance(self.main_contact, MemberId):
            self.main_contact = MemberId(self.main_contact)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=GHGA.id, name="id", curie=GHGA.curie('id'),
                   model_uri=GHGA.id, domain=None, range=URIRef)

slots.name = Slot(uri=GHGA.name, name="name", curie=GHGA.curie('name'),
                   model_uri=GHGA.name, domain=None, range=Optional[str])

slots.type = Slot(uri=GHGA.type, name="type", curie=GHGA.curie('type'),
                   model_uri=GHGA.type, domain=None, range=Optional[str])

slots.title = Slot(uri=GHGA.title, name="title", curie=GHGA.curie('title'),
                   model_uri=GHGA.title, domain=None, range=Optional[str])

slots.abstract = Slot(uri=GHGA.abstract, name="abstract", curie=GHGA.curie('abstract'),
                   model_uri=GHGA.abstract, domain=None, range=Optional[str])

slots.publications = Slot(uri=GHGA.publications, name="publications", curie=GHGA.curie('publications'),
                   model_uri=GHGA.publications, domain=None, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.attributes = Slot(uri=GHGA.attributes, name="attributes", curie=GHGA.curie('attributes'),
                   model_uri=GHGA.attributes, domain=None, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.description = Slot(uri=GHGA.description, name="description", curie=GHGA.curie('description'),
                   model_uri=GHGA.description, domain=None, range=Optional[str])

slots.instrument_model = Slot(uri=GHGA.instrument_model, name="instrument model", curie=GHGA.curie('instrument_model'),
                   model_uri=GHGA.instrument_model, domain=None, range=Optional[str])

slots.has_study = Slot(uri=GHGA.has_study, name="has study", curie=GHGA.curie('has_study'),
                   model_uri=GHGA.has_study, domain=None, range=Optional[Union[str, StudyId]])

slots.has_library = Slot(uri=GHGA.has_library, name="has library", curie=GHGA.curie('has_library'),
                   model_uri=GHGA.has_library, domain=None, range=Optional[Union[str, LibraryId]])

slots.has_sample = Slot(uri=GHGA.has_sample, name="has sample", curie=GHGA.curie('has_sample'),
                   model_uri=GHGA.has_sample, domain=None, range=Optional[Union[str, SampleId]])

slots.has_protocol = Slot(uri=GHGA.has_protocol, name="has protocol", curie=GHGA.curie('has_protocol'),
                   model_uri=GHGA.has_protocol, domain=None, range=Optional[Union[str, ProtocolId]])

slots.layout = Slot(uri=GHGA.layout, name="layout", curie=GHGA.curie('layout'),
                   model_uri=GHGA.layout, domain=None, range=Optional[str])

slots.source = Slot(uri=GHGA.source, name="source", curie=GHGA.curie('source'),
                   model_uri=GHGA.source, domain=None, range=Optional[str])

slots.selection = Slot(uri=GHGA.selection, name="selection", curie=GHGA.curie('selection'),
                   model_uri=GHGA.selection, domain=None, range=Optional[str])

slots.strategy = Slot(uri=GHGA.strategy, name="strategy", curie=GHGA.curie('strategy'),
                   model_uri=GHGA.strategy, domain=None, range=Optional[str])

slots.construction_protocol = Slot(uri=GHGA.construction_protocol, name="construction protocol", curie=GHGA.curie('construction_protocol'),
                   model_uri=GHGA.construction_protocol, domain=None, range=Optional[str])

slots.subject = Slot(uri=GHGA.subject, name="subject", curie=GHGA.curie('subject'),
                   model_uri=GHGA.subject, domain=None, range=Optional[Union[str, IndividualId]])

slots.biosample_accession = Slot(uri=GHGA.biosample_accession, name="biosample accession", curie=GHGA.curie('biosample_accession'),
                   model_uri=GHGA.biosample_accession, domain=None, range=Optional[str])

slots.has_anatomical_site = Slot(uri=GHGA.has_anatomical_site, name="has anatomical site", curie=GHGA.curie('has_anatomical_site'),
                   model_uri=GHGA.has_anatomical_site, domain=None, range=Optional[Union[str, AnatomicalEntityId]])

slots.has_cell_line = Slot(uri=GHGA.has_cell_line, name="has cell line", curie=GHGA.curie('has_cell_line'),
                   model_uri=GHGA.has_cell_line, domain=None, range=Optional[Union[str, CellLineId]])

slots.geographical_region = Slot(uri=GHGA.geographical_region, name="geographical region", curie=GHGA.curie('geographical_region'),
                   model_uri=GHGA.geographical_region, domain=None, range=Optional[str])

slots.has_disease_of_phenotypic_feature = Slot(uri=GHGA.has_disease_of_phenotypic_feature, name="has disease of phenotypic feature", curie=GHGA.curie('has_disease_of_phenotypic_feature'),
                   model_uri=GHGA.has_disease_of_phenotypic_feature, domain=None, range=Optional[Union[str, DiseaseOrPhenotypicFeatureId]])

slots.files = Slot(uri=GHGA.files, name="files", curie=GHGA.curie('files'),
                   model_uri=GHGA.files, domain=None, range=Optional[Union[Union[str, FileId], List[Union[str, FileId]]]])

slots.gender = Slot(uri=GHGA.gender, name="gender", curie=GHGA.curie('gender'),
                   model_uri=GHGA.gender, domain=None, range=Optional[str])

slots.age = Slot(uri=GHGA.age, name="age", curie=GHGA.curie('age'),
                   model_uri=GHGA.age, domain=None, range=Optional[int])

slots.format = Slot(uri=GHGA.format, name="format", curie=GHGA.curie('format'),
                   model_uri=GHGA.format, domain=None, range=Optional[str])

slots.size = Slot(uri=GHGA.size, name="size", curie=GHGA.curie('size'),
                   model_uri=GHGA.size, domain=None, range=Optional[str])

slots.md5sum = Slot(uri=GHGA.md5sum, name="md5sum", curie=GHGA.curie('md5sum'),
                   model_uri=GHGA.md5sum, domain=None, range=Optional[str])

slots.file_index = Slot(uri=GHGA.file_index, name="file_index", curie=GHGA.curie('file_index'),
                   model_uri=GHGA.file_index, domain=None, range=Optional[str])

slots.category = Slot(uri=GHGA.category, name="category", curie=GHGA.curie('category'),
                   model_uri=GHGA.category, domain=None, range=Optional[str])

slots.has_data_access_policy = Slot(uri=GHGA.has_data_access_policy, name="has data access policy", curie=GHGA.curie('has_data_access_policy'),
                   model_uri=GHGA.has_data_access_policy, domain=None, range=Optional[Union[str, DataAccessPolicyId]])

slots.policy_text = Slot(uri=GHGA.policy_text, name="policy text", curie=GHGA.curie('policy_text'),
                   model_uri=GHGA.policy_text, domain=None, range=Optional[str])

slots.policy_url = Slot(uri=GHGA.policy_url, name="policy url", curie=GHGA.curie('policy_url'),
                   model_uri=GHGA.policy_url, domain=None, range=Optional[str])

slots.has_data_access_committee = Slot(uri=GHGA.has_data_access_committee, name="has data access committee", curie=GHGA.curie('has_data_access_committee'),
                   model_uri=GHGA.has_data_access_committee, domain=None, range=Optional[Union[str, DataAccessCommitteeId]])

slots.main_contact = Slot(uri=GHGA.main_contact, name="main contact", curie=GHGA.curie('main_contact'),
                   model_uri=GHGA.main_contact, domain=None, range=Optional[Union[str, MemberId]])

slots.has_members = Slot(uri=GHGA.has_members, name="has members", curie=GHGA.curie('has_members'),
                   model_uri=GHGA.has_members, domain=None, range=Optional[Union[str, List[str]]])

slots.telephone = Slot(uri=GHGA.telephone, name="telephone", curie=GHGA.curie('telephone'),
                   model_uri=GHGA.telephone, domain=None, range=Optional[str])

slots.organization = Slot(uri=GHGA.organization, name="organization", curie=GHGA.curie('organization'),
                   model_uri=GHGA.organization, domain=None, range=Optional[str])

slots.email = Slot(uri=GHGA.email, name="email", curie=GHGA.curie('email'),
                   model_uri=GHGA.email, domain=None, range=Optional[str])

slots.key = Slot(uri=GHGA.key, name="key", curie=GHGA.curie('key'),
                   model_uri=GHGA.key, domain=None, range=Optional[str])

slots.key_type = Slot(uri=GHGA.key_type, name="key type", curie=GHGA.curie('key_type'),
                   model_uri=GHGA.key_type, domain=None, range=Optional[str])

slots.value = Slot(uri=GHGA.value, name="value", curie=GHGA.curie('value'),
                   model_uri=GHGA.value, domain=None, range=Optional[str])

slots.value_type = Slot(uri=GHGA.value_type, name="value type", curie=GHGA.curie('value_type'),
                   model_uri=GHGA.value_type, domain=None, range=Optional[str])

slots.attribute_key = Slot(uri=GHGA.key, name="attribute_key", curie=GHGA.curie('key'),
                   model_uri=GHGA.attribute_key, domain=Attribute, range=str)

slots.attribute_value = Slot(uri=GHGA.value, name="attribute_value", curie=GHGA.curie('value'),
                   model_uri=GHGA.attribute_value, domain=Attribute, range=str)

slots.study_title = Slot(uri=GHGA.title, name="study_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.study_title, domain=Study, range=str)

slots.study_type = Slot(uri=GHGA.type, name="study_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.study_type, domain=Study, range=str)

slots.study_name = Slot(uri=GHGA.name, name="study_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.study_name, domain=Study, range=Optional[str])

slots.study_abstract = Slot(uri=GHGA.abstract, name="study_abstract", curie=GHGA.curie('abstract'),
                   model_uri=GHGA.study_abstract, domain=Study, range=str)

slots.study_publications = Slot(uri=GHGA.publications, name="study_publications", curie=GHGA.curie('publications'),
                   model_uri=GHGA.study_publications, domain=Study, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.study_attributes = Slot(uri=GHGA.attributes, name="study_attributes", curie=GHGA.curie('attributes'),
                   model_uri=GHGA.study_attributes, domain=Study, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.experiment_name = Slot(uri=GHGA.name, name="experiment_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.experiment_name, domain=Experiment, range=str)

slots.experiment_description = Slot(uri=GHGA.description, name="experiment_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.experiment_description, domain=Experiment, range=Optional[str])

slots.experiment_has_study = Slot(uri=GHGA.has_study, name="experiment_has study", curie=GHGA.curie('has_study'),
                   model_uri=GHGA.experiment_has_study, domain=Experiment, range=Union[str, StudyId])

slots.experiment_instrument_model = Slot(uri=GHGA.instrument_model, name="experiment_instrument model", curie=GHGA.curie('instrument_model'),
                   model_uri=GHGA.experiment_instrument_model, domain=Experiment, range=str)

slots.experiment_has_library = Slot(uri=GHGA.has_library, name="experiment_has library", curie=GHGA.curie('has_library'),
                   model_uri=GHGA.experiment_has_library, domain=Experiment, range=Union[str, LibraryId])

slots.experiment_has_sample = Slot(uri=GHGA.has_sample, name="experiment_has sample", curie=GHGA.curie('has_sample'),
                   model_uri=GHGA.experiment_has_sample, domain=Experiment, range=Union[str, SampleId])

slots.experiment_has_protocol = Slot(uri=GHGA.has_protocol, name="experiment_has protocol", curie=GHGA.curie('has_protocol'),
                   model_uri=GHGA.experiment_has_protocol, domain=Experiment, range=Optional[Union[str, ProtocolId]])

slots.library_name = Slot(uri=GHGA.name, name="library_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.library_name, domain=Library, range=Optional[str])

slots.library_layout = Slot(uri=GHGA.layout, name="library_layout", curie=GHGA.curie('layout'),
                   model_uri=GHGA.library_layout, domain=Library, range=str)

slots.library_source = Slot(uri=GHGA.source, name="library_source", curie=GHGA.curie('source'),
                   model_uri=GHGA.library_source, domain=Library, range=str)

slots.library_selection = Slot(uri=GHGA.selection, name="library_selection", curie=GHGA.curie('selection'),
                   model_uri=GHGA.library_selection, domain=Library, range=str)

slots.library_strategy = Slot(uri=GHGA.strategy, name="library_strategy", curie=GHGA.curie('strategy'),
                   model_uri=GHGA.library_strategy, domain=Library, range=str)

slots.sample_name = Slot(uri=GHGA.name, name="sample_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.sample_name, domain=Sample, range=Optional[str])

slots.sample_type = Slot(uri=GHGA.type, name="sample_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.sample_type, domain=Sample, range=Optional[str])

slots.sample_description = Slot(uri=GHGA.description, name="sample_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.sample_description, domain=Sample, range=Optional[str])

slots.sample_subject = Slot(uri=GHGA.subject, name="sample_subject", curie=GHGA.curie('subject'),
                   model_uri=GHGA.sample_subject, domain=Sample, range=Union[str, IndividualId])

slots.sample_biosample_accession = Slot(uri=GHGA.biosample_accession, name="sample_biosample accession", curie=GHGA.curie('biosample_accession'),
                   model_uri=GHGA.sample_biosample_accession, domain=Sample, range=Optional[str])

slots.sample_has_anatomical_site = Slot(uri=GHGA.has_anatomical_site, name="sample_has anatomical site", curie=GHGA.curie('has_anatomical_site'),
                   model_uri=GHGA.sample_has_anatomical_site, domain=Sample, range=Optional[Union[str, AnatomicalEntityId]])

slots.sample_has_cell_line = Slot(uri=GHGA.has_cell_line, name="sample_has cell line", curie=GHGA.curie('has_cell_line'),
                   model_uri=GHGA.sample_has_cell_line, domain=Sample, range=Optional[Union[str, CellLineId]])

slots.sample_geographical_region = Slot(uri=GHGA.geographical_region, name="sample_geographical region", curie=GHGA.curie('geographical_region'),
                   model_uri=GHGA.sample_geographical_region, domain=Sample, range=Optional[str])

slots.sample_has_disease_of_phenotypic_feature = Slot(uri=GHGA.has_disease_of_phenotypic_feature, name="sample_has disease of phenotypic feature", curie=GHGA.curie('has_disease_of_phenotypic_feature'),
                   model_uri=GHGA.sample_has_disease_of_phenotypic_feature, domain=Sample, range=Union[str, DiseaseOrPhenotypicFeatureId])

slots.sample_files = Slot(uri=GHGA.files, name="sample_files", curie=GHGA.curie('files'),
                   model_uri=GHGA.sample_files, domain=Sample, range=Union[Union[str, FileId], List[Union[str, FileId]]])

slots.individual_gender = Slot(uri=GHGA.gender, name="individual_gender", curie=GHGA.curie('gender'),
                   model_uri=GHGA.individual_gender, domain=Individual, range=str)

slots.individual_age = Slot(uri=GHGA.age, name="individual_age", curie=GHGA.curie('age'),
                   model_uri=GHGA.individual_age, domain=Individual, range=Optional[int])

slots.file_format = Slot(uri=GHGA.format, name="file_format", curie=GHGA.curie('format'),
                   model_uri=GHGA.file_format, domain=File, range=Optional[str])

slots.file_type = Slot(uri=GHGA.type, name="file_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.file_type, domain=File, range=Optional[str])

slots.file_size = Slot(uri=GHGA.size, name="file_size", curie=GHGA.curie('size'),
                   model_uri=GHGA.file_size, domain=File, range=Optional[str])

slots.file_md5sum = Slot(uri=GHGA.md5sum, name="file_md5sum", curie=GHGA.curie('md5sum'),
                   model_uri=GHGA.file_md5sum, domain=File, range=Optional[str])

slots.file_file_index = Slot(uri=GHGA.file_index, name="file_file_index", curie=GHGA.curie('file_index'),
                   model_uri=GHGA.file_file_index, domain=File, range=Optional[str])

slots.file_category = Slot(uri=GHGA.category, name="file_category", curie=GHGA.curie('category'),
                   model_uri=GHGA.file_category, domain=File, range=Optional[str])

slots.dataset_title = Slot(uri=GHGA.title, name="dataset_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.dataset_title, domain=Dataset, range=str)

slots.dataset_description = Slot(uri=GHGA.description, name="dataset_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.dataset_description, domain=Dataset, range=str)

slots.dataset_type = Slot(uri=GHGA.type, name="dataset_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.dataset_type, domain=Dataset, range=str)

slots.dataset_files = Slot(uri=GHGA.files, name="dataset_files", curie=GHGA.curie('files'),
                   model_uri=GHGA.dataset_files, domain=Dataset, range=Union[Union[str, FileId], List[Union[str, FileId]]])

slots.dataset_has_data_access_policy = Slot(uri=GHGA.has_data_access_policy, name="dataset_has data access policy", curie=GHGA.curie('has_data_access_policy'),
                   model_uri=GHGA.dataset_has_data_access_policy, domain=Dataset, range=Union[str, DataAccessPolicyId])

slots.data_access_policy_description = Slot(uri=GHGA.description, name="data access policy_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.data_access_policy_description, domain=DataAccessPolicy, range=str)

slots.data_access_policy_policy_text = Slot(uri=GHGA.policy_text, name="data access policy_policy text", curie=GHGA.curie('policy_text'),
                   model_uri=GHGA.data_access_policy_policy_text, domain=DataAccessPolicy, range=str)

slots.data_access_policy_policy_url = Slot(uri=GHGA.policy_url, name="data access policy_policy url", curie=GHGA.curie('policy_url'),
                   model_uri=GHGA.data_access_policy_policy_url, domain=DataAccessPolicy, range=Optional[str])

slots.data_access_policy_has_data_access_committee = Slot(uri=GHGA.has_data_access_committee, name="data access policy_has data access committee", curie=GHGA.curie('has_data_access_committee'),
                   model_uri=GHGA.data_access_policy_has_data_access_committee, domain=DataAccessPolicy, range=Union[str, DataAccessCommitteeId])

slots.data_access_committee_title = Slot(uri=GHGA.title, name="data access committee_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.data_access_committee_title, domain=DataAccessCommittee, range=str)

slots.data_access_committee_main_contact = Slot(uri=GHGA.main_contact, name="data access committee_main contact", curie=GHGA.curie('main_contact'),
                   model_uri=GHGA.data_access_committee_main_contact, domain=DataAccessCommittee, range=Optional[Union[str, MemberId]])

slots.data_access_committee_has_members = Slot(uri=GHGA.has_members, name="data access committee_has members", curie=GHGA.curie('has_members'),
                   model_uri=GHGA.data_access_committee_has_members, domain=DataAccessCommittee, range=Optional[Union[Union[str, MemberId], List[Union[str, MemberId]]]])

slots.member_name = Slot(uri=GHGA.name, name="member_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.member_name, domain=Member, range=str)

slots.member_telephone = Slot(uri=GHGA.telephone, name="member_telephone", curie=GHGA.curie('telephone'),
                   model_uri=GHGA.member_telephone, domain=Member, range=str)

slots.member_organization = Slot(uri=GHGA.organization, name="member_organization", curie=GHGA.curie('organization'),
                   model_uri=GHGA.member_organization, domain=Member, range=str)

slots.member_main_contact = Slot(uri=GHGA.main_contact, name="member_main contact", curie=GHGA.curie('main_contact'),
                   model_uri=GHGA.member_main_contact, domain=Member, range=Union[str, MemberId])

slots.publication_id = Slot(uri=GHGA.id, name="publication_id", curie=GHGA.curie('id'),
                   model_uri=GHGA.publication_id, domain=Publication, range=Union[str, PublicationId])
