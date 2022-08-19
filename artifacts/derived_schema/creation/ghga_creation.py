# Auto generated from ghga_creation.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-08-19T14:52:39
# Schema: GHGA-Metadata-Schema
#
# id: https://w3id.org/GHGA-Metadata-Schema
# description: The metadata schema for the German Human Genome-Phenome Archive (GHGA).
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
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
version = "0.9.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CLO = CurieNamespace('CLO', 'http://purl.obolibrary.org/obo/CLO_')
COB = CurieNamespace('COB', 'http://purl.obolibrary.org/obo/COB_')
DUO = CurieNamespace('DUO', 'http://purl.obolibrary.org/obo/DUO_')
EFO = CurieNamespace('EFO', 'http://www.ebi.ac.uk/efo/EFO_')
GENEPIO = CurieNamespace('GENEPIO', 'http://purl.obolibrary.org/obo/GENEPIO_')
GHGA = CurieNamespace('GHGA', 'https://w3id.org/GHGA/')
HANCESTRO = CurieNamespace('HANCESTRO', 'http://purl.obolibrary.org/obo/HANCESTRO_')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
SEPIO = CurieNamespace('SEPIO', 'http://purl.obolibrary.org/obo/SEPIO_')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SNOMEDCT = CurieNamespace('SNOMEDCT', 'http://purl.bioontology.org/ontology/SNOMEDCT/')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
DEFAULT_ = GHGA


# Types

# Class references



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

    alias: str = None
    xref: Optional[Union[str, List[str]]] = empty_list()
    schema_type: Optional[str] = None
    schema_version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, str) else str(v) for v in self.xref]

        if self.schema_type is not None and not isinstance(self.schema_type, str):
            self.schema_type = str(self.schema_type)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

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
class CreateAgent(NamedThing):
    """
    An agent is something that bears some form of responsibility for an activity taking place, for the existence of an
    entity, or for another agent's activity. Agents include a Person, Organization, or Software that performs an
    activity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateAgent
    class_class_curie: ClassVar[str] = "GHGA:CreateAgent"
    class_name: ClassVar[str] = "create agent"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateAgent

    alias: str = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

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

    alias: str = None
    given_name: Optional[str] = None
    family_name: Optional[str] = None
    additional_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.given_name is not None and not isinstance(self.given_name, str):
            self.given_name = str(self.given_name)

        if self.family_name is not None and not isinstance(self.family_name, str):
            self.family_name = str(self.family_name)

        if self.additional_name is not None and not isinstance(self.additional_name, str):
            self.additional_name = str(self.additional_name)

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

    alias: str = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

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

    alias: str = None

@dataclass
class BiologicalQuality(NamedThing):
    """
    A biological quality is a quality held by a biological entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.BiologicalQuality
    class_class_curie: ClassVar[str] = "GHGA:BiologicalQuality"
    class_name: ClassVar[str] = "biological quality"
    class_model_uri: ClassVar[URIRef] = GHGA.BiologicalQuality

    alias: str = None

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

    alias: str = None

@dataclass
class PlannedProcess(NamedThing):
    """
    A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and
    depends on some entity during the time it occurs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.PlannedProcess
    class_class_curie: ClassVar[str] = "GHGA:PlannedProcess"
    class_name: ClassVar[str] = "planned process"
    class_model_uri: ClassVar[URIRef] = GHGA.PlannedProcess

    alias: str = None

@dataclass
class Investigation(PlannedProcess):
    """
    Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the
    object of study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Investigation
    class_class_curie: ClassVar[str] = "GHGA:Investigation"
    class_name: ClassVar[str] = "investigation"
    class_model_uri: ClassVar[URIRef] = GHGA.Investigation

    alias: str = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class DataTransformation(PlannedProcess):
    """
    A data transformation technique used to analyze and interpret data to gain a better understanding of it.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.DataTransformation
    class_class_curie: ClassVar[str] = "GHGA:DataTransformation"
    class_name: ClassVar[str] = "data transformation"
    class_model_uri: ClassVar[URIRef] = GHGA.DataTransformation

    alias: str = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class ResearchActivity(PlannedProcess):
    """
    A planned process executed in the performance of scientific research wherein systematic investigations are
    performed to establish facts and reach new conclusions about phenomena in the world.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.ResearchActivity
    class_class_curie: ClassVar[str] = "GHGA:ResearchActivity"
    class_name: ClassVar[str] = "research activity"
    class_model_uri: ClassVar[URIRef] = GHGA.ResearchActivity

    alias: str = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class CreateProject(ResearchActivity):
    """
    A high level organization for a collection of studies based on a research proposal that aims to achieve certain
    goals.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateProject
    class_class_curie: ClassVar[str] = "GHGA:CreateProject"
    class_name: ClassVar[str] = "create project"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateProject

    alias: str = None
    title: str = None
    description: str = None
    has_publication: Optional[Union[Union[dict, "CreatePublication"], List[Union[dict, "CreatePublication"]]]] = empty_list()
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()
    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.has_publication, list):
            self.has_publication = [self.has_publication] if self.has_publication is not None else []
        self.has_publication = [v if isinstance(v, CreatePublication) else CreatePublication(**as_dict(v)) for v in self.has_publication]

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, Attribute) else Attribute(**as_dict(v)) for v in self.has_attribute]

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class CreateStudy(Investigation):
    """
    Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and
    analysis of a subject to learn more about the phenomenon being studied.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateStudy
    class_class_curie: ClassVar[str] = "GHGA:CreateStudy"
    class_name: ClassVar[str] = "create study"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateStudy

    type: Union[str, "StudyTypeEnum"] = None
    affiliation: Union[str, List[str]] = None
    alias: str = None
    title: str = None
    description: str = None
    has_project: Optional[Union[dict, CreateProject]] = None
    has_file: Optional[Union[Union[dict, "CreateFile"], List[Union[dict, "CreateFile"]]]] = empty_list()
    has_publication: Optional[Union[Union[dict, "CreatePublication"], List[Union[dict, "CreatePublication"]]]] = empty_list()
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()
    release_status: Optional[Union[str, "ReleaseStatusEnum"]] = None
    accession: Optional[str] = None
    ega_accession: Optional[str] = None
    release_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, StudyTypeEnum):
            self.type = StudyTypeEnum(self.type)

        if self._is_empty(self.affiliation):
            self.MissingRequiredField("affiliation")
        if not isinstance(self.affiliation, list):
            self.affiliation = [self.affiliation] if self.affiliation is not None else []
        self.affiliation = [v if isinstance(v, str) else str(v) for v in self.affiliation]

        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.has_project is not None and not isinstance(self.has_project, CreateProject):
            self.has_project = CreateProject(**as_dict(self.has_project))

        if not isinstance(self.has_file, list):
            self.has_file = [self.has_file] if self.has_file is not None else []
        self.has_file = [v if isinstance(v, CreateFile) else CreateFile(**as_dict(v)) for v in self.has_file]

        if not isinstance(self.has_publication, list):
            self.has_publication = [self.has_publication] if self.has_publication is not None else []
        self.has_publication = [v if isinstance(v, CreatePublication) else CreatePublication(**as_dict(v)) for v in self.has_publication]

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, Attribute) else Attribute(**as_dict(v)) for v in self.has_attribute]

        if self.release_status is not None and not isinstance(self.release_status, ReleaseStatusEnum):
            self.release_status = ReleaseStatusEnum(self.release_status)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.ega_accession is not None and not isinstance(self.ega_accession, str):
            self.ega_accession = str(self.ega_accession)

        if self.release_date is not None and not isinstance(self.release_date, str):
            self.release_date = str(self.release_date)

        super().__post_init__(**kwargs)


@dataclass
class CreateExperiment(Investigation):
    """
    An experiment is an investigation that consists of a coordinated set of actions and observations designed to
    generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateExperiment
    class_class_curie: ClassVar[str] = "GHGA:CreateExperiment"
    class_name: ClassVar[str] = "create experiment"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateExperiment

    has_study: Union[dict, CreateStudy] = None
    has_sample: Union[Union[dict, "CreateSample"], List[Union[dict, "CreateSample"]]] = None
    has_protocol: Union[Union[dict, "CreateProtocol"], List[Union[dict, "CreateProtocol"]]] = None
    alias: str = None
    description: str = None
    type: Optional[str] = None
    biological_replicates: Optional[str] = None
    technical_replicates: Optional[str] = None
    experimental_replicates: Optional[str] = None
    has_file: Optional[Union[Union[dict, "CreateFile"], List[Union[dict, "CreateFile"]]]] = empty_list()
    has_experiment_process: Optional[Union[Union[dict, "CreateExperimentProcess"], List[Union[dict, "CreateExperimentProcess"]]]] = empty_list()
    title: Optional[str] = None
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()
    accession: Optional[str] = None
    ega_accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.has_study):
            self.MissingRequiredField("has_study")
        if not isinstance(self.has_study, CreateStudy):
            self.has_study = CreateStudy(**as_dict(self.has_study))

        if self._is_empty(self.has_sample):
            self.MissingRequiredField("has_sample")
        if not isinstance(self.has_sample, list):
            self.has_sample = [self.has_sample] if self.has_sample is not None else []
        self.has_sample = [v if isinstance(v, CreateSample) else CreateSample(**as_dict(v)) for v in self.has_sample]

        if self._is_empty(self.has_protocol):
            self.MissingRequiredField("has_protocol")
        if not isinstance(self.has_protocol, list):
            self.has_protocol = [self.has_protocol] if self.has_protocol is not None else []
        self.has_protocol = [v if isinstance(v, CreateProtocol) else CreateProtocol(**as_dict(v)) for v in self.has_protocol]

        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.biological_replicates is not None and not isinstance(self.biological_replicates, str):
            self.biological_replicates = str(self.biological_replicates)

        if self.technical_replicates is not None and not isinstance(self.technical_replicates, str):
            self.technical_replicates = str(self.technical_replicates)

        if self.experimental_replicates is not None and not isinstance(self.experimental_replicates, str):
            self.experimental_replicates = str(self.experimental_replicates)

        if not isinstance(self.has_file, list):
            self.has_file = [self.has_file] if self.has_file is not None else []
        self.has_file = [v if isinstance(v, CreateFile) else CreateFile(**as_dict(v)) for v in self.has_file]

        if not isinstance(self.has_experiment_process, list):
            self.has_experiment_process = [self.has_experiment_process] if self.has_experiment_process is not None else []
        self.has_experiment_process = [v if isinstance(v, CreateExperimentProcess) else CreateExperimentProcess(**as_dict(v)) for v in self.has_experiment_process]

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, Attribute) else Attribute(**as_dict(v)) for v in self.has_attribute]

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.ega_accession is not None and not isinstance(self.ega_accession, str):
            self.ega_accession = str(self.ega_accession)

        super().__post_init__(**kwargs)


@dataclass
class CreateExperimentProcess(PlannedProcess):
    """
    An Experiment Process is a process that describes how a Sample is transformed to a File via an assay. The
    Experiment Process also keeps track of the Protocol used and the Agent that is running the experiment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateExperimentProcess
    class_class_curie: ClassVar[str] = "GHGA:CreateExperimentProcess"
    class_name: ClassVar[str] = "create experiment process"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateExperimentProcess

    alias: str = None
    type: Optional[Union[str, "ExperimentProcessTypeEnum"]] = None
    title: Optional[str] = None
    has_input: Optional[Union[dict, "CreateSample"]] = None
    has_protocol: Optional[Union[dict, "CreateProtocol"]] = None
    has_agent: Optional[Union[dict, CreateAgent]] = None
    has_output: Optional[Union[Union[dict, "CreateFile"], List[Union[dict, "CreateFile"]]]] = empty_list()
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type is not None and not isinstance(self.type, ExperimentProcessTypeEnum):
            self.type = ExperimentProcessTypeEnum(self.type)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.has_input is not None and not isinstance(self.has_input, CreateSample):
            self.has_input = CreateSample(**as_dict(self.has_input))

        if self.has_protocol is not None and not isinstance(self.has_protocol, CreateProtocol):
            self.has_protocol = CreateProtocol(**as_dict(self.has_protocol))

        if self.has_agent is not None and not isinstance(self.has_agent, CreateAgent):
            self.has_agent = CreateAgent(**as_dict(self.has_agent))

        self._normalize_inlined_as_dict(slot_name="has_output", slot_type=CreateFile, key_name="name", keyed=False)

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, Attribute) else Attribute(**as_dict(v)) for v in self.has_attribute]

        super().__post_init__(**kwargs)


@dataclass
class CreateProtocol(InformationContentEntity):
    """
    A plan specification which has sufficient level of detail and quantitative information to communicate it between
    investigation agents, so that different investigation agents will reliably be able to independently reproduce the
    process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateProtocol
    class_class_curie: ClassVar[str] = "GHGA:CreateProtocol"
    class_name: ClassVar[str] = "create protocol"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateProtocol

    alias: str = None
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    has_file: Optional[Union[dict, "CreateFile"]] = None
    xref: Optional[Union[str, List[str]]] = empty_list()
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.has_file is not None and not isinstance(self.has_file, CreateFile):
            self.has_file = CreateFile(**as_dict(self.has_file))

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, str) else str(v) for v in self.xref]

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, Attribute) else Attribute(**as_dict(v)) for v in self.has_attribute]

        super().__post_init__(**kwargs)


@dataclass
class CreateLibraryPreparationProtocol(CreateProtocol):
    """
    Information about the library preparation of an Experiment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateLibraryPreparationProtocol
    class_class_curie: ClassVar[str] = "GHGA:CreateLibraryPreparationProtocol"
    class_name: ClassVar[str] = "create library preparation protocol"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateLibraryPreparationProtocol

    library_name: str = None
    library_layout: str = None
    library_type: str = None
    library_selection: str = None
    library_preparation: str = None
    library_preparation_kit_retail_name: str = None
    library_preparation_kit_manufacturer: str = None
    alias: str = None
    description: str = None
    primer: Optional[str] = None
    end_bias: Optional[str] = None
    target_regions: Optional[str] = None
    rnaseq_strandedness: Optional[str] = None
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.library_name):
            self.MissingRequiredField("library_name")
        if not isinstance(self.library_name, str):
            self.library_name = str(self.library_name)

        if self._is_empty(self.library_layout):
            self.MissingRequiredField("library_layout")
        if not isinstance(self.library_layout, str):
            self.library_layout = str(self.library_layout)

        if self._is_empty(self.library_type):
            self.MissingRequiredField("library_type")
        if not isinstance(self.library_type, str):
            self.library_type = str(self.library_type)

        if self._is_empty(self.library_selection):
            self.MissingRequiredField("library_selection")
        if not isinstance(self.library_selection, str):
            self.library_selection = str(self.library_selection)

        if self._is_empty(self.library_preparation):
            self.MissingRequiredField("library_preparation")
        if not isinstance(self.library_preparation, str):
            self.library_preparation = str(self.library_preparation)

        if self._is_empty(self.library_preparation_kit_retail_name):
            self.MissingRequiredField("library_preparation_kit_retail_name")
        if not isinstance(self.library_preparation_kit_retail_name, str):
            self.library_preparation_kit_retail_name = str(self.library_preparation_kit_retail_name)

        if self._is_empty(self.library_preparation_kit_manufacturer):
            self.MissingRequiredField("library_preparation_kit_manufacturer")
        if not isinstance(self.library_preparation_kit_manufacturer, str):
            self.library_preparation_kit_manufacturer = str(self.library_preparation_kit_manufacturer)

        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.primer is not None and not isinstance(self.primer, str):
            self.primer = str(self.primer)

        if self.end_bias is not None and not isinstance(self.end_bias, str):
            self.end_bias = str(self.end_bias)

        if self.target_regions is not None and not isinstance(self.target_regions, str):
            self.target_regions = str(self.target_regions)

        if self.rnaseq_strandedness is not None and not isinstance(self.rnaseq_strandedness, str):
            self.rnaseq_strandedness = str(self.rnaseq_strandedness)

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, Attribute) else Attribute(**as_dict(v)) for v in self.has_attribute]

        super().__post_init__(**kwargs)


@dataclass
class CreateSequencingProtocol(CreateProtocol):
    """
    Information about the sequencing of a sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateSequencingProtocol
    class_class_curie: ClassVar[str] = "GHGA:CreateSequencingProtocol"
    class_name: ClassVar[str] = "create sequencing protocol"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateSequencingProtocol

    instrument_model: str = None
    alias: str = None
    description: str = None
    sequencing_center: Optional[str] = None
    paired_or_single_end: Optional[Union[str, "PairedOrSingleEndEnum"]] = None
    forward_or_reverse: Optional[Union[str, "ForwardOrReverseEnum"]] = None
    sequencing_read_length: Optional[str] = None
    index_sequence: Optional[str] = None
    target_coverage: Optional[str] = None
    lane_number: Optional[str] = None
    flow_cell_id: Optional[str] = None
    flow_cell_type: Optional[str] = None
    umi_barcode_read: Optional[str] = None
    umi_barcode_size: Optional[str] = None
    umi_barcode_offset: Optional[str] = None
    cell_barcode_read: Optional[str] = None
    cell_barcode_offset: Optional[str] = None
    cell_barcode_size: Optional[str] = None
    sample_barcode_read: Optional[str] = None
    type: Optional[str] = None
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.instrument_model):
            self.MissingRequiredField("instrument_model")
        if not isinstance(self.instrument_model, str):
            self.instrument_model = str(self.instrument_model)

        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.sequencing_center is not None and not isinstance(self.sequencing_center, str):
            self.sequencing_center = str(self.sequencing_center)

        if self.paired_or_single_end is not None and not isinstance(self.paired_or_single_end, PairedOrSingleEndEnum):
            self.paired_or_single_end = PairedOrSingleEndEnum(self.paired_or_single_end)

        if self.forward_or_reverse is not None and not isinstance(self.forward_or_reverse, ForwardOrReverseEnum):
            self.forward_or_reverse = ForwardOrReverseEnum(self.forward_or_reverse)

        if self.sequencing_read_length is not None and not isinstance(self.sequencing_read_length, str):
            self.sequencing_read_length = str(self.sequencing_read_length)

        if self.index_sequence is not None and not isinstance(self.index_sequence, str):
            self.index_sequence = str(self.index_sequence)

        if self.target_coverage is not None and not isinstance(self.target_coverage, str):
            self.target_coverage = str(self.target_coverage)

        if self.lane_number is not None and not isinstance(self.lane_number, str):
            self.lane_number = str(self.lane_number)

        if self.flow_cell_id is not None and not isinstance(self.flow_cell_id, str):
            self.flow_cell_id = str(self.flow_cell_id)

        if self.flow_cell_type is not None and not isinstance(self.flow_cell_type, str):
            self.flow_cell_type = str(self.flow_cell_type)

        if self.umi_barcode_read is not None and not isinstance(self.umi_barcode_read, str):
            self.umi_barcode_read = str(self.umi_barcode_read)

        if self.umi_barcode_size is not None and not isinstance(self.umi_barcode_size, str):
            self.umi_barcode_size = str(self.umi_barcode_size)

        if self.umi_barcode_offset is not None and not isinstance(self.umi_barcode_offset, str):
            self.umi_barcode_offset = str(self.umi_barcode_offset)

        if self.cell_barcode_read is not None and not isinstance(self.cell_barcode_read, str):
            self.cell_barcode_read = str(self.cell_barcode_read)

        if self.cell_barcode_offset is not None and not isinstance(self.cell_barcode_offset, str):
            self.cell_barcode_offset = str(self.cell_barcode_offset)

        if self.cell_barcode_size is not None and not isinstance(self.cell_barcode_size, str):
            self.cell_barcode_size = str(self.cell_barcode_size)

        if self.sample_barcode_read is not None and not isinstance(self.sample_barcode_read, str):
            self.sample_barcode_read = str(self.sample_barcode_read)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, Attribute) else Attribute(**as_dict(v)) for v in self.has_attribute]

        super().__post_init__(**kwargs)


@dataclass
class CreateTechnology(InformationContentEntity):
    """
    A Technology is an abstraction that represents the instrument used for an assay. The Technology entity captures
    instrument-specific attributes that are relevant for an Experiment entity. The Technology entity may be further
    characterized by its children where each child has fields that are relevant to that particular technology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateTechnology
    class_class_curie: ClassVar[str] = "GHGA:CreateTechnology"
    class_name: ClassVar[str] = "create technology"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateTechnology

    alias: str = None

@dataclass
class CreateWorkflow(InformationContentEntity):
    """
    A Workflow is an abstraction that represents the workflow used to perform an analysis. The Workflow entity
    captures workflow-specific attributes that are relevant for an Analysis entity. The Workflow entity may be further
    characterized by its children where each child has fields that are relevant to that particular workflow.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateWorkflow
    class_class_curie: ClassVar[str] = "GHGA:CreateWorkflow"
    class_name: ClassVar[str] = "create workflow"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateWorkflow

    name: str = None
    alias: str = None
    has_workflow_step: Optional[Union[Union[dict, "CreateWorkflowStep"], List[Union[dict, "CreateWorkflowStep"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if not isinstance(self.has_workflow_step, list):
            self.has_workflow_step = [self.has_workflow_step] if self.has_workflow_step is not None else []
        self.has_workflow_step = [v if isinstance(v, CreateWorkflowStep) else CreateWorkflowStep(**as_dict(v)) for v in self.has_workflow_step]

        super().__post_init__(**kwargs)


@dataclass
class CreateWorkflowStep(InformationContentEntity):
    """
    A Workflow Step represents each individual step performed in a Workflow. If the Workflow is a single-step workflow
    then the Workflow has just one Workflow Step entity. If the Workflow is a multi-step workflow then the Workflow
    has a Workflow Step entity for each step. All Workflow step specific attributes like parameters, and metadata
    about execution environment are captured by the Workflow Step entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateWorkflowStep
    class_class_curie: ClassVar[str] = "GHGA:CreateWorkflowStep"
    class_name: ClassVar[str] = "create workflow step"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateWorkflowStep

    alias: str = None
    has_workflow_parameter: Optional[Union[Union[dict, "WorkflowParameter"], List[Union[dict, "WorkflowParameter"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.has_workflow_parameter, list):
            self.has_workflow_parameter = [self.has_workflow_parameter] if self.has_workflow_parameter is not None else []
        self.has_workflow_parameter = [v if isinstance(v, WorkflowParameter) else WorkflowParameter(**as_dict(v)) for v in self.has_workflow_parameter]

        super().__post_init__(**kwargs)


@dataclass
class WorkflowParameter(YAMLRoot):
    """
    A key/value pair that represents a parameter used in a Workflow Step.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.WorkflowParameter
    class_class_curie: ClassVar[str] = "GHGA:WorkflowParameter"
    class_name: ClassVar[str] = "workflow parameter"
    class_model_uri: ClassVar[URIRef] = GHGA.WorkflowParameter

    key: Optional[str] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.key is not None and not isinstance(self.key, str):
            self.key = str(self.key)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass
class CreateBiospecimen(MaterialEntity):
    """
    A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics,
    treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is
    derived.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateBiospecimen
    class_class_curie: ClassVar[str] = "GHGA:CreateBiospecimen"
    class_name: ClassVar[str] = "create biospecimen"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateBiospecimen

    alias: str = None
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    isolation: Optional[str] = None
    storage: Optional[str] = None
    has_individual: Optional[Union[dict, "CreateIndividual"]] = None
    has_anatomical_entity: Optional[Union[Union[dict, "CreateAnatomicalEntity"], List[Union[dict, "CreateAnatomicalEntity"]]]] = empty_list()
    has_disease: Optional[Union[Union[dict, "CreateDisease"], List[Union[dict, "CreateDisease"]]]] = empty_list()
    has_phenotypic_feature: Optional[Union[Union[dict, "CreatePhenotypicFeature"], List[Union[dict, "CreatePhenotypicFeature"]]]] = empty_list()
    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.isolation is not None and not isinstance(self.isolation, str):
            self.isolation = str(self.isolation)

        if self.storage is not None and not isinstance(self.storage, str):
            self.storage = str(self.storage)

        if self.has_individual is not None and not isinstance(self.has_individual, CreateIndividual):
            self.has_individual = CreateIndividual(**as_dict(self.has_individual))

        if not isinstance(self.has_anatomical_entity, list):
            self.has_anatomical_entity = [self.has_anatomical_entity] if self.has_anatomical_entity is not None else []
        self.has_anatomical_entity = [v if isinstance(v, CreateAnatomicalEntity) else CreateAnatomicalEntity(**as_dict(v)) for v in self.has_anatomical_entity]

        if not isinstance(self.has_disease, list):
            self.has_disease = [self.has_disease] if self.has_disease is not None else []
        self.has_disease = [v if isinstance(v, CreateDisease) else CreateDisease(**as_dict(v)) for v in self.has_disease]

        if not isinstance(self.has_phenotypic_feature, list):
            self.has_phenotypic_feature = [self.has_phenotypic_feature] if self.has_phenotypic_feature is not None else []
        self.has_phenotypic_feature = [v if isinstance(v, CreatePhenotypicFeature) else CreatePhenotypicFeature(**as_dict(v)) for v in self.has_phenotypic_feature]

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class CreateDiseaseOrPhenotypicFeature(BiologicalQuality):
    """
    Disease or Phenotypic Feature that the entity is associated with. This entity is a union of Disease and Phenotypic
    Feature and exists to accommodate situations where Disease concepts are used interchangeably with Phenotype
    concepts or vice-versa.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateDiseaseOrPhenotypicFeature
    class_class_curie: ClassVar[str] = "GHGA:CreateDiseaseOrPhenotypicFeature"
    class_name: ClassVar[str] = "create disease or phenotypic feature"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateDiseaseOrPhenotypicFeature

    alias: str = None
    concept_identifier: Optional[str] = None
    concept_name: Optional[str] = None
    description: Optional[str] = None
    ontology_name: Optional[str] = None
    ontology_version: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.concept_identifier is not None and not isinstance(self.concept_identifier, str):
            self.concept_identifier = str(self.concept_identifier)

        if self.concept_name is not None and not isinstance(self.concept_name, str):
            self.concept_name = str(self.concept_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ontology_name is not None and not isinstance(self.ontology_name, str):
            self.ontology_name = str(self.ontology_name)

        if self.ontology_version is not None and not isinstance(self.ontology_version, str):
            self.ontology_version = str(self.ontology_version)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class CreateSample(MaterialEntity):
    """
    A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation,
    demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateSample
    class_class_curie: ClassVar[str] = "GHGA:CreateSample"
    class_name: ClassVar[str] = "create sample"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateSample

    name: str = None
    description: str = None
    alias: str = None
    type: Optional[str] = None
    case_control_status: Optional[Union[str, "CaseControlStatusEnum"]] = None
    vital_status_at_sampling: Optional[Union[str, "VitalStatusEnum"]] = None
    isolation: Optional[str] = None
    storage: Optional[str] = None
    has_individual: Optional[Union[dict, "CreateIndividual"]] = None
    has_anatomical_entity: Optional[Union[Union[dict, "CreateAnatomicalEntity"], List[Union[dict, "CreateAnatomicalEntity"]]]] = empty_list()
    has_biospecimen: Optional[Union[dict, CreateBiospecimen]] = None
    xref: Optional[Union[str, List[str]]] = empty_list()
    accession: Optional[str] = None
    ega_accession: Optional[str] = None
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.case_control_status is not None and not isinstance(self.case_control_status, CaseControlStatusEnum):
            self.case_control_status = CaseControlStatusEnum(self.case_control_status)

        if self.vital_status_at_sampling is not None and not isinstance(self.vital_status_at_sampling, VitalStatusEnum):
            self.vital_status_at_sampling = VitalStatusEnum(self.vital_status_at_sampling)

        if self.isolation is not None and not isinstance(self.isolation, str):
            self.isolation = str(self.isolation)

        if self.storage is not None and not isinstance(self.storage, str):
            self.storage = str(self.storage)

        if self.has_individual is not None and not isinstance(self.has_individual, CreateIndividual):
            self.has_individual = CreateIndividual(**as_dict(self.has_individual))

        if not isinstance(self.has_anatomical_entity, list):
            self.has_anatomical_entity = [self.has_anatomical_entity] if self.has_anatomical_entity is not None else []
        self.has_anatomical_entity = [v if isinstance(v, CreateAnatomicalEntity) else CreateAnatomicalEntity(**as_dict(v)) for v in self.has_anatomical_entity]

        if self.has_biospecimen is not None and not isinstance(self.has_biospecimen, CreateBiospecimen):
            self.has_biospecimen = CreateBiospecimen(**as_dict(self.has_biospecimen))

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, str) else str(v) for v in self.xref]

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.ega_accession is not None and not isinstance(self.ega_accession, str):
            self.ega_accession = str(self.ega_accession)

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, Attribute) else Attribute(**as_dict(v)) for v in self.has_attribute]

        super().__post_init__(**kwargs)


@dataclass
class CreateIndividual(Person):
    """
    An Individual is a Person who is participating in a Study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateIndividual
    class_class_curie: ClassVar[str] = "GHGA:CreateIndividual"
    class_name: ClassVar[str] = "create individual"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateIndividual

    sex: Union[str, "BiologicalSexEnum"] = None
    age: Union[str, "AgeRangeEnum"] = None
    vital_status: Union[str, "VitalStatusEnum"] = None
    alias: str = None
    karyotype: Optional[str] = None
    geographical_region: Optional[str] = None
    has_ancestry: Optional[Union[Union[dict, "CreateAncestry"], List[Union[dict, "CreateAncestry"]]]] = empty_list()
    has_parent: Optional[Union[Union[dict, "CreateIndividual"], List[Union[dict, "CreateIndividual"]]]] = empty_list()
    has_children: Optional[Union[Union[dict, "CreateIndividual"], List[Union[dict, "CreateIndividual"]]]] = empty_list()
    has_disease: Optional[Union[Union[dict, "CreateDisease"], List[Union[dict, "CreateDisease"]]]] = empty_list()
    has_phenotypic_feature: Optional[Union[Union[dict, "CreatePhenotypicFeature"], List[Union[dict, "CreatePhenotypicFeature"]]]] = empty_list()
    has_file: Optional[Union[Union[dict, "CreateFile"], List[Union[dict, "CreateFile"]]]] = empty_list()
    accession: Optional[str] = None
    ega_accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sex):
            self.MissingRequiredField("sex")
        if not isinstance(self.sex, BiologicalSexEnum):
            self.sex = BiologicalSexEnum(self.sex)

        if self._is_empty(self.age):
            self.MissingRequiredField("age")
        if not isinstance(self.age, AgeRangeEnum):
            self.age = AgeRangeEnum(self.age)

        if self._is_empty(self.vital_status):
            self.MissingRequiredField("vital_status")
        if not isinstance(self.vital_status, VitalStatusEnum):
            self.vital_status = VitalStatusEnum(self.vital_status)

        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self.karyotype is not None and not isinstance(self.karyotype, str):
            self.karyotype = str(self.karyotype)

        if self.geographical_region is not None and not isinstance(self.geographical_region, str):
            self.geographical_region = str(self.geographical_region)

        if not isinstance(self.has_ancestry, list):
            self.has_ancestry = [self.has_ancestry] if self.has_ancestry is not None else []
        self.has_ancestry = [v if isinstance(v, CreateAncestry) else CreateAncestry(**as_dict(v)) for v in self.has_ancestry]

        if not isinstance(self.has_parent, list):
            self.has_parent = [self.has_parent] if self.has_parent is not None else []
        self.has_parent = [v if isinstance(v, CreateIndividual) else CreateIndividual(**as_dict(v)) for v in self.has_parent]

        if not isinstance(self.has_children, list):
            self.has_children = [self.has_children] if self.has_children is not None else []
        self.has_children = [v if isinstance(v, CreateIndividual) else CreateIndividual(**as_dict(v)) for v in self.has_children]

        if not isinstance(self.has_disease, list):
            self.has_disease = [self.has_disease] if self.has_disease is not None else []
        self.has_disease = [v if isinstance(v, CreateDisease) else CreateDisease(**as_dict(v)) for v in self.has_disease]

        if not isinstance(self.has_phenotypic_feature, list):
            self.has_phenotypic_feature = [self.has_phenotypic_feature] if self.has_phenotypic_feature is not None else []
        self.has_phenotypic_feature = [v if isinstance(v, CreatePhenotypicFeature) else CreatePhenotypicFeature(**as_dict(v)) for v in self.has_phenotypic_feature]

        if not isinstance(self.has_file, list):
            self.has_file = [self.has_file] if self.has_file is not None else []
        self.has_file = [v if isinstance(v, CreateFile) else CreateFile(**as_dict(v)) for v in self.has_file]

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.ega_accession is not None and not isinstance(self.ega_accession, str):
            self.ega_accession = str(self.ega_accession)

        super().__post_init__(**kwargs)


@dataclass
class CreateDonor(CreateIndividual):
    """
    A Donor is an Individual that participates in a research Study by donating a Biospecimen. The use of the
    Biospecimen is restricted to the consent provided by the Donor.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateDonor
    class_class_curie: ClassVar[str] = "GHGA:CreateDonor"
    class_name: ClassVar[str] = "create donor"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateDonor

    sex: Union[str, "BiologicalSexEnum"] = None
    age: Union[str, "AgeRangeEnum"] = None
    vital_status: Union[str, "VitalStatusEnum"] = None
    alias: str = None

@dataclass
class Population(MaterialEntity):
    """
    A population is a collection of individuals from the same taxonomic class living, counted or sampled at a
    particular site or in a particular area.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Population
    class_class_curie: ClassVar[str] = "GHGA:Population"
    class_name: ClassVar[str] = "population"
    class_model_uri: ClassVar[URIRef] = GHGA.Population

    alias: str = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class CreateFamily(Population):
    """
    A domestic group, or a number of domestic groups linked through descent (demonstrated or stipulated) from a common
    ancestor, marriage, or adoption.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateFamily
    class_class_curie: ClassVar[str] = "GHGA:CreateFamily"
    class_name: ClassVar[str] = "create family"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateFamily

    alias: str = None
    has_individual: Optional[Union[Union[dict, CreateIndividual], List[Union[dict, CreateIndividual]]]] = empty_list()
    has_proband: Optional[Union[dict, CreateIndividual]] = None
    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.has_individual, list):
            self.has_individual = [self.has_individual] if self.has_individual is not None else []
        self.has_individual = [v if isinstance(v, CreateIndividual) else CreateIndividual(**as_dict(v)) for v in self.has_individual]

        if self.has_proband is not None and not isinstance(self.has_proband, CreateIndividual):
            self.has_proband = CreateIndividual(**as_dict(self.has_proband))

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class CreateCohort(Population):
    """
    A cohort is a collection of individuals that share a common characteristic/observation and have been grouped
    together for a research study/investigation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateCohort
    class_class_curie: ClassVar[str] = "GHGA:CreateCohort"
    class_name: ClassVar[str] = "create cohort"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateCohort

    alias: str = None
    has_individual: Optional[Union[Union[dict, CreateIndividual], List[Union[dict, CreateIndividual]]]] = empty_list()
    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.has_individual, list):
            self.has_individual = [self.has_individual] if self.has_individual is not None else []
        self.has_individual = [v if isinstance(v, CreateIndividual) else CreateIndividual(**as_dict(v)) for v in self.has_individual]

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class CreateAncestry(Population):
    """
    Population category defined using ancestry informative markers (AIMs) based on genetic/genomic data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateAncestry
    class_class_curie: ClassVar[str] = "GHGA:CreateAncestry"
    class_name: ClassVar[str] = "create ancestry"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateAncestry

    alias: str = None
    concept_identifier: Optional[str] = None
    concept_name: Optional[str] = None
    description: Optional[str] = None
    ontology_name: Optional[str] = None
    ontology_version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.concept_identifier is not None and not isinstance(self.concept_identifier, str):
            self.concept_identifier = str(self.concept_identifier)

        if self.concept_name is not None and not isinstance(self.concept_name, str):
            self.concept_name = str(self.concept_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ontology_name is not None and not isinstance(self.ontology_name, str):
            self.ontology_name = str(self.ontology_name)

        if self.ontology_version is not None and not isinstance(self.ontology_version, str):
            self.ontology_version = str(self.ontology_version)

        super().__post_init__(**kwargs)


@dataclass
class CreateFile(InformationContentEntity):
    """
    A file is an object that contains information generated from a process, either an Experiment or an Analysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateFile
    class_class_curie: ClassVar[str] = "GHGA:CreateFile"
    class_name: ClassVar[str] = "create file"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateFile

    name: str = None
    format: Union[str, "FileFormatEnum"] = None
    size: int = None
    checksum: str = None
    checksum_type: str = None
    alias: str = None
    drs_uri: Optional[str] = None
    accession: Optional[str] = None
    ega_accession: Optional[str] = None
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.format):
            self.MissingRequiredField("format")
        if not isinstance(self.format, FileFormatEnum):
            self.format = FileFormatEnum(self.format)

        if self._is_empty(self.size):
            self.MissingRequiredField("size")
        if not isinstance(self.size, int):
            self.size = int(self.size)

        if self._is_empty(self.checksum):
            self.MissingRequiredField("checksum")
        if not isinstance(self.checksum, str):
            self.checksum = str(self.checksum)

        if self._is_empty(self.checksum_type):
            self.MissingRequiredField("checksum_type")
        if not isinstance(self.checksum_type, str):
            self.checksum_type = str(self.checksum_type)

        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self.drs_uri is not None and not isinstance(self.drs_uri, str):
            self.drs_uri = str(self.drs_uri)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.ega_accession is not None and not isinstance(self.ega_accession, str):
            self.ega_accession = str(self.ega_accession)

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, Attribute) else Attribute(**as_dict(v)) for v in self.has_attribute]

        super().__post_init__(**kwargs)


@dataclass
class CreateAnalysis(DataTransformation):
    """
    An Analysis is a data transformation that transforms input data to output data. The workflow used to achieve this
    transformation and the individual steps are also captured.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateAnalysis
    class_class_curie: ClassVar[str] = "GHGA:CreateAnalysis"
    class_name: ClassVar[str] = "create analysis"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateAnalysis

    reference_genome: str = None
    reference_chromosome: str = None
    has_input: Union[Union[dict, CreateFile], List[Union[dict, CreateFile]]] = None
    has_workflow: Union[Union[dict, CreateWorkflow], List[Union[dict, CreateWorkflow]]] = None
    has_output: Union[Union[dict, CreateFile], List[Union[dict, CreateFile]]] = None
    alias: str = None
    type: Optional[str] = None
    has_study: Optional[Union[dict, CreateStudy]] = None
    has_analysis_process: Optional[Union[Union[dict, "CreateAnalysisProcess"], List[Union[dict, "CreateAnalysisProcess"]]]] = empty_list()
    description: Optional[str] = None
    accession: Optional[str] = None
    ega_accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.reference_genome):
            self.MissingRequiredField("reference_genome")
        if not isinstance(self.reference_genome, str):
            self.reference_genome = str(self.reference_genome)

        if self._is_empty(self.reference_chromosome):
            self.MissingRequiredField("reference_chromosome")
        if not isinstance(self.reference_chromosome, str):
            self.reference_chromosome = str(self.reference_chromosome)

        if self._is_empty(self.has_input):
            self.MissingRequiredField("has_input")
        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, CreateFile) else CreateFile(**as_dict(v)) for v in self.has_input]

        if self._is_empty(self.has_workflow):
            self.MissingRequiredField("has_workflow")
        if not isinstance(self.has_workflow, list):
            self.has_workflow = [self.has_workflow] if self.has_workflow is not None else []
        self.has_workflow = [v if isinstance(v, CreateWorkflow) else CreateWorkflow(**as_dict(v)) for v in self.has_workflow]

        if self._is_empty(self.has_output):
            self.MissingRequiredField("has_output")
        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, CreateFile) else CreateFile(**as_dict(v)) for v in self.has_output]

        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.has_study is not None and not isinstance(self.has_study, CreateStudy):
            self.has_study = CreateStudy(**as_dict(self.has_study))

        if not isinstance(self.has_analysis_process, list):
            self.has_analysis_process = [self.has_analysis_process] if self.has_analysis_process is not None else []
        self.has_analysis_process = [v if isinstance(v, CreateAnalysisProcess) else CreateAnalysisProcess(**as_dict(v)) for v in self.has_analysis_process]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.ega_accession is not None and not isinstance(self.ega_accession, str):
            self.ega_accession = str(self.ega_accession)

        super().__post_init__(**kwargs)


@dataclass
class CreateAnalysisProcess(PlannedProcess):
    """
    An analysis process is a process that describes how one or more Files, from a Study, are transformed to another
    set of Files via a Workflow. The analysis process also keeps track of the workflow metadata and the Agent that is
    running the Analysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateAnalysisProcess
    class_class_curie: ClassVar[str] = "GHGA:CreateAnalysisProcess"
    class_name: ClassVar[str] = "create analysis process"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateAnalysisProcess

    alias: str = None
    title: Optional[str] = None
    has_input: Optional[Union[Union[dict, CreateFile], List[Union[dict, CreateFile]]]] = empty_list()
    has_workflow: Optional[Union[dict, CreateWorkflow]] = None
    has_agent: Optional[Union[dict, CreateAgent]] = None
    has_output: Optional[Union[Union[dict, CreateFile], List[Union[dict, CreateFile]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, CreateFile) else CreateFile(**as_dict(v)) for v in self.has_input]

        if self.has_workflow is not None and not isinstance(self.has_workflow, CreateWorkflow):
            self.has_workflow = CreateWorkflow(**as_dict(self.has_workflow))

        if self.has_agent is not None and not isinstance(self.has_agent, CreateAgent):
            self.has_agent = CreateAgent(**as_dict(self.has_agent))

        if not isinstance(self.has_output, list):
            self.has_output = [self.has_output] if self.has_output is not None else []
        self.has_output = [v if isinstance(v, CreateFile) else CreateFile(**as_dict(v)) for v in self.has_output]

        super().__post_init__(**kwargs)


@dataclass
class CreateDataset(InformationContentEntity):
    """
    A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateDataset
    class_class_curie: ClassVar[str] = "GHGA:CreateDataset"
    class_name: ClassVar[str] = "create dataset"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateDataset

    title: str = None
    description: str = None
    has_file: Union[Union[dict, CreateFile], List[Union[dict, CreateFile]]] = None
    has_data_access_policy: Union[dict, "CreateDataAccessPolicy"] = None
    alias: str = None
    type: Optional[str] = None
    has_study: Optional[Union[Union[dict, CreateStudy], List[Union[dict, CreateStudy]]]] = empty_list()
    has_experiment: Optional[Union[Union[dict, CreateExperiment], List[Union[dict, CreateExperiment]]]] = empty_list()
    has_sample: Optional[Union[Union[dict, CreateSample], List[Union[dict, CreateSample]]]] = empty_list()
    has_analysis: Optional[Union[Union[dict, CreateAnalysis], List[Union[dict, CreateAnalysis]]]] = empty_list()
    has_publication: Optional[Union[Union[dict, "CreatePublication"], List[Union[dict, "CreatePublication"]]]] = empty_list()
    release_status: Optional[Union[str, "ReleaseStatusEnum"]] = None
    accession: Optional[str] = None
    ega_accession: Optional[str] = None
    release_date: Optional[str] = None
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.has_file):
            self.MissingRequiredField("has_file")
        if not isinstance(self.has_file, list):
            self.has_file = [self.has_file] if self.has_file is not None else []
        self.has_file = [v if isinstance(v, CreateFile) else CreateFile(**as_dict(v)) for v in self.has_file]

        if self._is_empty(self.has_data_access_policy):
            self.MissingRequiredField("has_data_access_policy")
        if not isinstance(self.has_data_access_policy, CreateDataAccessPolicy):
            self.has_data_access_policy = CreateDataAccessPolicy(**as_dict(self.has_data_access_policy))

        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.has_study, list):
            self.has_study = [self.has_study] if self.has_study is not None else []
        self.has_study = [v if isinstance(v, CreateStudy) else CreateStudy(**as_dict(v)) for v in self.has_study]

        if not isinstance(self.has_experiment, list):
            self.has_experiment = [self.has_experiment] if self.has_experiment is not None else []
        self.has_experiment = [v if isinstance(v, CreateExperiment) else CreateExperiment(**as_dict(v)) for v in self.has_experiment]

        if not isinstance(self.has_sample, list):
            self.has_sample = [self.has_sample] if self.has_sample is not None else []
        self.has_sample = [v if isinstance(v, CreateSample) else CreateSample(**as_dict(v)) for v in self.has_sample]

        if not isinstance(self.has_analysis, list):
            self.has_analysis = [self.has_analysis] if self.has_analysis is not None else []
        self.has_analysis = [v if isinstance(v, CreateAnalysis) else CreateAnalysis(**as_dict(v)) for v in self.has_analysis]

        if not isinstance(self.has_publication, list):
            self.has_publication = [self.has_publication] if self.has_publication is not None else []
        self.has_publication = [v if isinstance(v, CreatePublication) else CreatePublication(**as_dict(v)) for v in self.has_publication]

        if self.release_status is not None and not isinstance(self.release_status, ReleaseStatusEnum):
            self.release_status = ReleaseStatusEnum(self.release_status)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.ega_accession is not None and not isinstance(self.ega_accession, str):
            self.ega_accession = str(self.ega_accession)

        if self.release_date is not None and not isinstance(self.release_date, str):
            self.release_date = str(self.release_date)

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, Attribute) else Attribute(**as_dict(v)) for v in self.has_attribute]

        super().__post_init__(**kwargs)


@dataclass
class CreateDataUseCondition(InformationContentEntity):
    """
    Data Use Condition represents the use conditions associated with a policy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateDataUseCondition
    class_class_curie: ClassVar[str] = "GHGA:CreateDataUseCondition"
    class_name: ClassVar[str] = "create data use condition"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateDataUseCondition

    alias: str = None
    has_data_use_permission: Union[dict, "CreateDataUsePermission"] = None
    has_data_use_modifier: Optional[Union[dict, "CreateDataUseModifier"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.has_data_use_permission):
            self.MissingRequiredField("has_data_use_permission")
        if not isinstance(self.has_data_use_permission, CreateDataUsePermission):
            self.has_data_use_permission = CreateDataUsePermission(**as_dict(self.has_data_use_permission))

        if self.has_data_use_modifier is not None and not isinstance(self.has_data_use_modifier, CreateDataUseModifier):
            self.has_data_use_modifier = CreateDataUseModifier(**as_dict(self.has_data_use_modifier))

        super().__post_init__(**kwargs)


@dataclass
class CreateDataAccessPolicy(InformationContentEntity):
    """
    A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or
    more Datasets belonging to one or more Studies.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateDataAccessPolicy
    class_class_curie: ClassVar[str] = "GHGA:CreateDataAccessPolicy"
    class_name: ClassVar[str] = "create data access policy"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateDataAccessPolicy

    policy_text: str = None
    has_data_access_committee: Union[dict, "CreateDataAccessCommittee"] = None
    alias: str = None
    name: Optional[str] = None
    description: Optional[str] = None
    policy_url: Optional[str] = None
    has_data_use_condition: Optional[Union[Union[dict, CreateDataUseCondition], List[Union[dict, CreateDataUseCondition]]]] = empty_list()
    data_request_form: Optional[str] = None
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()
    accession: Optional[str] = None
    ega_accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.policy_text):
            self.MissingRequiredField("policy_text")
        if not isinstance(self.policy_text, str):
            self.policy_text = str(self.policy_text)

        if self._is_empty(self.has_data_access_committee):
            self.MissingRequiredField("has_data_access_committee")
        if not isinstance(self.has_data_access_committee, CreateDataAccessCommittee):
            self.has_data_access_committee = CreateDataAccessCommittee(**as_dict(self.has_data_access_committee))

        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.policy_url is not None and not isinstance(self.policy_url, str):
            self.policy_url = str(self.policy_url)

        if not isinstance(self.has_data_use_condition, list):
            self.has_data_use_condition = [self.has_data_use_condition] if self.has_data_use_condition is not None else []
        self.has_data_use_condition = [v if isinstance(v, CreateDataUseCondition) else CreateDataUseCondition(**as_dict(v)) for v in self.has_data_use_condition]

        if self.data_request_form is not None and not isinstance(self.data_request_form, str):
            self.data_request_form = str(self.data_request_form)

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, Attribute) else Attribute(**as_dict(v)) for v in self.has_attribute]

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.ega_accession is not None and not isinstance(self.ega_accession, str):
            self.ega_accession = str(self.ega_accession)

        super().__post_init__(**kwargs)


@dataclass
class CreateDataAccessCommittee(Committee):
    """
    A group of members that are delegated to grant access to one or more datasets after ensuring the minimum criteria
    for data sharing has been met, and request for data use does not raise ethical and/or legal concerns.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateDataAccessCommittee
    class_class_curie: ClassVar[str] = "GHGA:CreateDataAccessCommittee"
    class_name: ClassVar[str] = "create data access committee"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateDataAccessCommittee

    name: str = None
    alias: str = None
    description: Optional[str] = None
    main_contact: Optional[Union[dict, "CreateMember"]] = None
    has_member: Optional[Union[Union[dict, "CreateMember"], List[Union[dict, "CreateMember"]]]] = empty_list()
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()
    accession: Optional[str] = None
    ega_accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.main_contact is not None and not isinstance(self.main_contact, CreateMember):
            self.main_contact = CreateMember(**as_dict(self.main_contact))

        if not isinstance(self.has_member, list):
            self.has_member = [self.has_member] if self.has_member is not None else []
        self.has_member = [v if isinstance(v, CreateMember) else CreateMember(**as_dict(v)) for v in self.has_member]

        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, Attribute) else Attribute(**as_dict(v)) for v in self.has_attribute]

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.ega_accession is not None and not isinstance(self.ega_accession, str):
            self.ega_accession = str(self.ega_accession)

        super().__post_init__(**kwargs)


@dataclass
class CreateMember(Person):
    """
    Member of an Organization or a Committee.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateMember
    class_class_curie: ClassVar[str] = "GHGA:CreateMember"
    class_name: ClassVar[str] = "create member"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateMember

    alias: str = None
    email: str = None
    organization: str = None
    telephone: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.email):
            self.MissingRequiredField("email")
        if not isinstance(self.email, str):
            self.email = str(self.email)

        if self._is_empty(self.organization):
            self.MissingRequiredField("organization")
        if not isinstance(self.organization, str):
            self.organization = str(self.organization)

        if self.telephone is not None and not isinstance(self.telephone, str):
            self.telephone = str(self.telephone)

        super().__post_init__(**kwargs)


@dataclass
class CreatePublication(InformationContentEntity):
    """
    The Publication entity represents a publication. While a publication can be any article that is published, the
    minimum expectation is that the publication has a valid DOI.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreatePublication
    class_class_curie: ClassVar[str] = "GHGA:CreatePublication"
    class_name: ClassVar[str] = "create publication"
    class_model_uri: ClassVar[URIRef] = GHGA.CreatePublication

    alias: str = None
    title: Optional[str] = None
    abstract: Optional[str] = None
    xref: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.alias):
            self.MissingRequiredField("alias")
        if not isinstance(self.alias, str):
            self.alias = str(self.alias)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, str) else str(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class CreateAnatomicalEntity(MaterialEntity):
    """
    Biological entity that is either an individual member of a biological species or constitutes the structural
    organization of an individual member of a biological species.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateAnatomicalEntity
    class_class_curie: ClassVar[str] = "GHGA:CreateAnatomicalEntity"
    class_name: ClassVar[str] = "create anatomical entity"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateAnatomicalEntity

    alias: str = None
    concept_identifier: Optional[str] = None
    concept_name: Optional[str] = None
    description: Optional[str] = None
    ontology_name: Optional[str] = None
    ontology_version: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.concept_identifier is not None and not isinstance(self.concept_identifier, str):
            self.concept_identifier = str(self.concept_identifier)

        if self.concept_name is not None and not isinstance(self.concept_name, str):
            self.concept_name = str(self.concept_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ontology_name is not None and not isinstance(self.ontology_name, str):
            self.ontology_name = str(self.ontology_name)

        if self.ontology_version is not None and not isinstance(self.ontology_version, str):
            self.ontology_version = str(self.ontology_version)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class CreateCellLine(MaterialEntity):
    """
    A cultured cell population that represents a genetically stable and homogenous population of cultured cells that
    shares a common propagation history.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateCellLine
    class_class_curie: ClassVar[str] = "GHGA:CreateCellLine"
    class_name: ClassVar[str] = "create cell line"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateCellLine

    alias: str = None

@dataclass
class CreateDisease(CreateDiseaseOrPhenotypicFeature):
    """
    A disease is a disposition to undergo pathological processes that exists in an organism because of one or more
    disorders in that organism.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateDisease
    class_class_curie: ClassVar[str] = "GHGA:CreateDisease"
    class_name: ClassVar[str] = "create disease"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateDisease

    alias: str = None

@dataclass
class CreatePhenotypicFeature(CreateDiseaseOrPhenotypicFeature):
    """
    The observable form taken by some character (or group of characters) in an individual or an organism, excluding
    pathology and disease. The detectable outward manifestations of a specific genotype.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreatePhenotypicFeature
    class_class_curie: ClassVar[str] = "GHGA:CreatePhenotypicFeature"
    class_name: ClassVar[str] = "create phenotypic feature"
    class_model_uri: ClassVar[URIRef] = GHGA.CreatePhenotypicFeature

    alias: str = None

@dataclass
class CreateUser(Person):
    """
    A user in GHGA.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateUser
    class_class_curie: ClassVar[str] = "GHGA:CreateUser"
    class_name: ClassVar[str] = "create user"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateUser

    alias: str = None
    email: Optional[str] = None
    role: Optional[Union[str, "UserRoleEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.role is not None and not isinstance(self.role, UserRoleEnum):
            self.role = UserRoleEnum(self.role)

        super().__post_init__(**kwargs)


@dataclass
class CreateSubmission(YAMLRoot):
    """
    A grouping entity that represents information about one or more entities. A submission can be considered as a set
    of inter-related (and inter-connected) entities that represent a data submission to GHGA.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateSubmission
    class_class_curie: ClassVar[str] = "GHGA:CreateSubmission"
    class_name: ClassVar[str] = "create submission"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateSubmission

    affiliation: Optional[str] = None
    has_study: Optional[Union[dict, CreateStudy]] = None
    has_project: Optional[Union[dict, CreateProject]] = None
    has_sample: Optional[Union[Union[dict, CreateSample], List[Union[dict, CreateSample]]]] = empty_list()
    has_biospecimen: Optional[Union[Union[dict, CreateBiospecimen], List[Union[dict, CreateBiospecimen]]]] = empty_list()
    has_individual: Optional[Union[Union[dict, CreateIndividual], List[Union[dict, CreateIndividual]]]] = empty_list()
    has_experiment: Optional[Union[Union[dict, CreateExperiment], List[Union[dict, CreateExperiment]]]] = empty_list()
    has_protocol: Optional[Union[Union[dict, CreateProtocol], List[Union[dict, CreateProtocol]]]] = empty_list()
    has_analysis: Optional[Union[Union[dict, CreateAnalysis], List[Union[dict, CreateAnalysis]]]] = empty_list()
    has_file: Optional[Union[Union[dict, CreateFile], List[Union[dict, CreateFile]]]] = empty_list()
    has_dataset: Optional[Union[Union[dict, CreateDataset], List[Union[dict, CreateDataset]]]] = empty_list()
    has_data_access_policy: Optional[Union[Union[dict, CreateDataAccessPolicy], List[Union[dict, CreateDataAccessPolicy]]]] = empty_list()
    has_data_access_committee: Optional[Union[Union[dict, CreateDataAccessCommittee], List[Union[dict, CreateDataAccessCommittee]]]] = empty_list()
    has_member: Optional[Union[Union[dict, CreateMember], List[Union[dict, CreateMember]]]] = empty_list()
    has_publication: Optional[Union[Union[dict, CreatePublication], List[Union[dict, CreatePublication]]]] = empty_list()
    submission_date: Optional[str] = None
    submission_status: Optional[Union[str, "SubmissionStatusEnum"]] = None
    schema_type: Optional[str] = None
    schema_version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.affiliation is not None and not isinstance(self.affiliation, str):
            self.affiliation = str(self.affiliation)

        if self.has_study is not None and not isinstance(self.has_study, CreateStudy):
            self.has_study = CreateStudy(**as_dict(self.has_study))

        if self.has_project is not None and not isinstance(self.has_project, CreateProject):
            self.has_project = CreateProject(**as_dict(self.has_project))

        if not isinstance(self.has_sample, list):
            self.has_sample = [self.has_sample] if self.has_sample is not None else []
        self.has_sample = [v if isinstance(v, CreateSample) else CreateSample(**as_dict(v)) for v in self.has_sample]

        if not isinstance(self.has_biospecimen, list):
            self.has_biospecimen = [self.has_biospecimen] if self.has_biospecimen is not None else []
        self.has_biospecimen = [v if isinstance(v, CreateBiospecimen) else CreateBiospecimen(**as_dict(v)) for v in self.has_biospecimen]

        if not isinstance(self.has_individual, list):
            self.has_individual = [self.has_individual] if self.has_individual is not None else []
        self.has_individual = [v if isinstance(v, CreateIndividual) else CreateIndividual(**as_dict(v)) for v in self.has_individual]

        if not isinstance(self.has_experiment, list):
            self.has_experiment = [self.has_experiment] if self.has_experiment is not None else []
        self.has_experiment = [v if isinstance(v, CreateExperiment) else CreateExperiment(**as_dict(v)) for v in self.has_experiment]

        if not isinstance(self.has_protocol, list):
            self.has_protocol = [self.has_protocol] if self.has_protocol is not None else []
        self.has_protocol = [v if isinstance(v, CreateProtocol) else CreateProtocol(**as_dict(v)) for v in self.has_protocol]

        if not isinstance(self.has_analysis, list):
            self.has_analysis = [self.has_analysis] if self.has_analysis is not None else []
        self.has_analysis = [v if isinstance(v, CreateAnalysis) else CreateAnalysis(**as_dict(v)) for v in self.has_analysis]

        if not isinstance(self.has_file, list):
            self.has_file = [self.has_file] if self.has_file is not None else []
        self.has_file = [v if isinstance(v, CreateFile) else CreateFile(**as_dict(v)) for v in self.has_file]

        if not isinstance(self.has_dataset, list):
            self.has_dataset = [self.has_dataset] if self.has_dataset is not None else []
        self.has_dataset = [v if isinstance(v, CreateDataset) else CreateDataset(**as_dict(v)) for v in self.has_dataset]

        if not isinstance(self.has_data_access_policy, list):
            self.has_data_access_policy = [self.has_data_access_policy] if self.has_data_access_policy is not None else []
        self.has_data_access_policy = [v if isinstance(v, CreateDataAccessPolicy) else CreateDataAccessPolicy(**as_dict(v)) for v in self.has_data_access_policy]

        if not isinstance(self.has_data_access_committee, list):
            self.has_data_access_committee = [self.has_data_access_committee] if self.has_data_access_committee is not None else []
        self.has_data_access_committee = [v if isinstance(v, CreateDataAccessCommittee) else CreateDataAccessCommittee(**as_dict(v)) for v in self.has_data_access_committee]

        if not isinstance(self.has_member, list):
            self.has_member = [self.has_member] if self.has_member is not None else []
        self.has_member = [v if isinstance(v, CreateMember) else CreateMember(**as_dict(v)) for v in self.has_member]

        if not isinstance(self.has_publication, list):
            self.has_publication = [self.has_publication] if self.has_publication is not None else []
        self.has_publication = [v if isinstance(v, CreatePublication) else CreatePublication(**as_dict(v)) for v in self.has_publication]

        if self.submission_date is not None and not isinstance(self.submission_date, str):
            self.submission_date = str(self.submission_date)

        if self.submission_status is not None and not isinstance(self.submission_status, SubmissionStatusEnum):
            self.submission_status = SubmissionStatusEnum(self.submission_status)

        if self.schema_type is not None and not isinstance(self.schema_type, str):
            self.schema_type = str(self.schema_type)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        super().__post_init__(**kwargs)


@dataclass
class CreateDataUsePermission(InformationContentEntity):
    """
    A data item that is used to indicate consent permissions for datasets and/or materials and relates to the purposes
    for which datasets and/or material might be removed, stored or used.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateDataUsePermission
    class_class_curie: ClassVar[str] = "GHGA:CreateDataUsePermission"
    class_name: ClassVar[str] = "create data use permission"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateDataUsePermission

    alias: str = None
    concept_identifier: Optional[str] = None
    concept_name: Optional[str] = None
    description: Optional[str] = None
    ontology_name: Optional[str] = None
    ontology_version: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.concept_identifier is not None and not isinstance(self.concept_identifier, str):
            self.concept_identifier = str(self.concept_identifier)

        if self.concept_name is not None and not isinstance(self.concept_name, str):
            self.concept_name = str(self.concept_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ontology_name is not None and not isinstance(self.ontology_name, str):
            self.ontology_name = str(self.ontology_name)

        if self.ontology_version is not None and not isinstance(self.ontology_version, str):
            self.ontology_version = str(self.ontology_version)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class CreateDataUseModifier(InformationContentEntity):
    """
    Data use modifiers indicate additional conditions for use.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CreateDataUseModifier
    class_class_curie: ClassVar[str] = "GHGA:CreateDataUseModifier"
    class_name: ClassVar[str] = "create data use modifier"
    class_model_uri: ClassVar[URIRef] = GHGA.CreateDataUseModifier

    alias: str = None
    concept_identifier: Optional[str] = None
    concept_name: Optional[str] = None
    description: Optional[str] = None
    ontology_name: Optional[str] = None
    ontology_version: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.concept_identifier is not None and not isinstance(self.concept_identifier, str):
            self.concept_identifier = str(self.concept_identifier)

        if self.concept_name is not None and not isinstance(self.concept_name, str):
            self.concept_name = str(self.concept_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ontology_name is not None and not isinstance(self.ontology_name, str):
            self.ontology_name = str(self.ontology_name)

        if self.ontology_version is not None and not isinstance(self.ontology_version, str):
            self.ontology_version = str(self.ontology_version)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class OntologyClassMixin(YAMLRoot):
    """
    Mixin for entities that represent an class/term/concept from an ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.OntologyClassMixin
    class_class_curie: ClassVar[str] = "GHGA:OntologyClassMixin"
    class_name: ClassVar[str] = "ontology class mixin"
    class_model_uri: ClassVar[URIRef] = GHGA.OntologyClassMixin

    concept_identifier: Optional[str] = None
    concept_name: Optional[str] = None
    description: Optional[str] = None
    ontology_name: Optional[str] = None
    ontology_version: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.concept_identifier is not None and not isinstance(self.concept_identifier, str):
            self.concept_identifier = str(self.concept_identifier)

        if self.concept_name is not None and not isinstance(self.concept_name, str):
            self.concept_name = str(self.concept_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ontology_name is not None and not isinstance(self.ontology_name, str):
            self.ontology_name = str(self.ontology_name)

        if self.ontology_version is not None and not isinstance(self.ontology_version, str):
            self.ontology_version = str(self.ontology_version)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class MetadataMixin(YAMLRoot):
    """
    Mixin for tracking schema specific metadata about an instance.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.MetadataMixin
    class_class_curie: ClassVar[str] = "GHGA:MetadataMixin"
    class_name: ClassVar[str] = "metadata mixin"
    class_model_uri: ClassVar[URIRef] = GHGA.MetadataMixin

    schema_type: Optional[str] = None
    schema_version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.schema_type is not None and not isinstance(self.schema_type, str):
            self.schema_type = str(self.schema_type)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        super().__post_init__(**kwargs)


@dataclass
class AccessionMixin(YAMLRoot):
    """
    Mixin for entities that can be assigned a GHGA accession.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.AccessionMixin
    class_class_curie: ClassVar[str] = "GHGA:AccessionMixin"
    class_name: ClassVar[str] = "accession mixin"
    class_model_uri: ClassVar[URIRef] = GHGA.AccessionMixin

    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class EgaAccessionMixin(YAMLRoot):
    """
    Mixin for entities that can be assigned an EGA accession, in addition to GHGA accession.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.EgaAccessionMixin
    class_class_curie: ClassVar[str] = "GHGA:EgaAccessionMixin"
    class_name: ClassVar[str] = "ega accession mixin"
    class_model_uri: ClassVar[URIRef] = GHGA.EgaAccessionMixin

    ega_accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.ega_accession is not None and not isinstance(self.ega_accession, str):
            self.ega_accession = str(self.ega_accession)

        super().__post_init__(**kwargs)


@dataclass
class AttributeMixin(YAMLRoot):
    """
    Mixin for entities that can have one or more attributes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.AttributeMixin
    class_class_curie: ClassVar[str] = "GHGA:AttributeMixin"
    class_name: ClassVar[str] = "attribute mixin"
    class_model_uri: ClassVar[URIRef] = GHGA.AttributeMixin

    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.has_attribute, list):
            self.has_attribute = [self.has_attribute] if self.has_attribute is not None else []
        self.has_attribute = [v if isinstance(v, Attribute) else Attribute(**as_dict(v)) for v in self.has_attribute]

        super().__post_init__(**kwargs)


@dataclass
class PublicationMixin(YAMLRoot):
    """
    Mixin for entities that can have one or more publications.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.PublicationMixin
    class_class_curie: ClassVar[str] = "GHGA:PublicationMixin"
    class_name: ClassVar[str] = "publication mixin"
    class_model_uri: ClassVar[URIRef] = GHGA.PublicationMixin

    has_publication: Optional[Union[dict, CreatePublication]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_publication is not None and not isinstance(self.has_publication, CreatePublication):
            self.has_publication = CreatePublication(**as_dict(self.has_publication))

        super().__post_init__(**kwargs)


@dataclass
class DeprecatedMixin(YAMLRoot):
    """
    Mixin for entities that can be deprecated.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.DeprecatedMixin
    class_class_curie: ClassVar[str] = "GHGA:DeprecatedMixin"
    class_name: ClassVar[str] = "deprecated mixin"
    class_model_uri: ClassVar[URIRef] = GHGA.DeprecatedMixin

    replaced_by: Optional[Union[dict, NamedThing]] = None
    deprecation_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.replaced_by is not None and not isinstance(self.replaced_by, NamedThing):
            self.replaced_by = NamedThing(**as_dict(self.replaced_by))

        if self.deprecation_date is not None and not isinstance(self.deprecation_date, str):
            self.deprecation_date = str(self.deprecation_date)

        super().__post_init__(**kwargs)


@dataclass
class ReleaseStatusMixin(YAMLRoot):
    """
    Mixin for entities that can be released at a later point in time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.ReleaseStatusMixin
    class_class_curie: ClassVar[str] = "GHGA:ReleaseStatusMixin"
    class_name: ClassVar[str] = "release status mixin"
    class_model_uri: ClassVar[URIRef] = GHGA.ReleaseStatusMixin

    release_status: Optional[str] = None
    release_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.release_status is not None and not isinstance(self.release_status, str):
            self.release_status = str(self.release_status)

        if self.release_date is not None and not isinstance(self.release_date, str):
            self.release_date = str(self.release_date)

        super().__post_init__(**kwargs)


# Enumerations
class BiologicalSexEnum(EnumDefinitionImpl):
    """
    The biological sex of an Individual as determined by their chromosomes.
    """
    female = PermissibleValue(text="female",
                                   description="Female")
    male = PermissibleValue(text="male",
                               description="Male")
    unknown = PermissibleValue(text="unknown",
                                     description="unspecified")

    _defn = EnumDefinition(
        name="BiologicalSexEnum",
        description="The biological sex of an Individual as determined by their chromosomes.",
    )

class UserRoleEnum(EnumDefinitionImpl):
    """
    Enum to capture the different roles a GHGA User can have.
    """
    data_requester = PermissibleValue(text="data_requester",
                                                   description="Role of a Data Requester where the user requests access to one or more Datasets.")
    data_steward = PermissibleValue(text="data_steward",
                                               description="Role of a Data Steward where the user is responsible for approving request from a user for one or more Datasets.")

    _defn = EnumDefinition(
        name="UserRoleEnum",
        description="Enum to capture the different roles a GHGA User can have.",
    )

class VitalStatusEnum(EnumDefinitionImpl):
    """
    Enum to capture the vital status of an individual.
    """
    alive = PermissibleValue(text="alive",
                                 description="Showing characteristics of life; displaying signs of life.")
    deceased = PermissibleValue(text="deceased",
                                       description="The cessation of life.")
    unknown = PermissibleValue(text="unknown",
                                     description="Vital status is unknown.")

    _defn = EnumDefinition(
        name="VitalStatusEnum",
        description="Enum to capture the vital status of an individual.",
    )

class StudyTypeEnum(EnumDefinitionImpl):
    """
    Enum to capture the type of a study.
    """
    whole_genome_sequencing = PermissibleValue(text="whole_genome_sequencing",
                                                                     description="Whole Genome Sequencing")
    metagenomics = PermissibleValue(text="metagenomics",
                                               description="Metagenomics")
    transcriptome_analysis = PermissibleValue(text="transcriptome_analysis",
                                                                   description="Transcriptome Analysis")
    resequencing = PermissibleValue(text="resequencing",
                                               description="Resequencing")
    epigenetics = PermissibleValue(text="epigenetics",
                                             description="Epigenetics")
    synthetic_genomics = PermissibleValue(text="synthetic_genomics",
                                                           description="Sythetic Genomics")
    forensic_paleo_genomics = PermissibleValue(text="forensic_paleo_genomics",
                                                                     description="Forensic or Paleo-genomics")
    gene_regulation = PermissibleValue(text="gene_regulation",
                                                     description="Gene Regulation Study")
    cancer_genomics = PermissibleValue(text="cancer_genomics",
                                                     description="Cancer Genomics")
    population_genomics = PermissibleValue(text="population_genomics",
                                                             description="Population Genomics")
    rna_seq = PermissibleValue(text="rna_seq",
                                     description="RNAseq")
    exome_sequencing = PermissibleValue(text="exome_sequencing",
                                                       description="Exome Sequencing")
    pooled_clone_sequencing = PermissibleValue(text="pooled_clone_sequencing",
                                                                     description="Pooled Clone Sequencing")
    genome_wide_association_study = PermissibleValue(text="genome_wide_association_study",
                                                                                 description="Genome-wide Association Study")
    other = PermissibleValue(text="other",
                                 description="Other study")

    _defn = EnumDefinition(
        name="StudyTypeEnum",
        description="Enum to capture the type of a study.",
    )

class FileFormatEnum(EnumDefinitionImpl):
    """
    Enum to capture file types.
    """
    bam = PermissibleValue(text="bam",
                             description="BAM File")
    complete_genomics = PermissibleValue(text="complete_genomics",
                                                         description="Complete Genomics File")
    cram = PermissibleValue(text="cram",
                               description="CRAM File")
    fasta = PermissibleValue(text="fasta",
                                 description="Fasta File")
    fastq = PermissibleValue(text="fastq",
                                 description="FastQ File")
    pacbio_hdf5 = PermissibleValue(text="pacbio_hdf5",
                                             description="PacBio HDF5 File")
    sff = PermissibleValue(text="sff",
                             description="Standard flowgram format used to encode results of pyrosequencing from the 454 Life Sciences platform.")
    srf = PermissibleValue(text="srf",
                             description="SRF is a generic format for DNA sequence data.")
    vcf = PermissibleValue(text="vcf",
                             description="VCF file for storing gene sequence variations.")
    txt = PermissibleValue(text="txt",
                             description="Text file.")
    pxf = PermissibleValue(text="pxf",
                             description="Phenopacket file.")
    other = PermissibleValue(text="other",
                                 description="Other format.")

    _defn = EnumDefinition(
        name="FileFormatEnum",
        description="Enum to capture file types.",
    )

class CaseControlStatusEnum(EnumDefinitionImpl):
    """
    Enum to capture whether a Sample in a Study is to be considered as Case or Control.
    """
    control = PermissibleValue(text="control",
                                     description="The Sample is to be treated as Control")
    case = PermissibleValue(text="case",
                               description="The Sample is to be treated as Case")

    _defn = EnumDefinition(
        name="CaseControlStatusEnum",
        description="Enum to capture whether a Sample in a Study is to be considered as Case or Control.",
    )

class PairedOrSingleEndEnum(EnumDefinitionImpl):
    """
    Enum to capture whether a sequencing experiment generates reads that are Paired-end or Single-end.
    """
    paired = PermissibleValue(text="paired",
                                   description="The reads are Paired-end")
    single = PermissibleValue(text="single",
                                   description="The reads are Single-end")

    _defn = EnumDefinition(
        name="PairedOrSingleEndEnum",
        description="Enum to capture whether a sequencing experiment generates reads that are Paired-end or Single-end.",
    )

class ForwardOrReverseEnum(EnumDefinitionImpl):
    """
    Enum to capture whether the reads from paired-end sequencing are forward (R1) or reverse (R2).
    """
    forward = PermissibleValue(text="forward",
                                     description="The reads are forward (R1) reads")
    reverse = PermissibleValue(text="reverse",
                                     description="The reads are reverse (R2) reads")

    _defn = EnumDefinition(
        name="ForwardOrReverseEnum",
        description="Enum to capture whether the reads from paired-end sequencing are forward (R1) or reverse (R2).",
    )

class SubmissionStatusEnum(EnumDefinitionImpl):
    """
    Enum to capture the status of a Submission.
    """
    in_progress = PermissibleValue(text="in_progress",
                                             description="Signifies that the Submission is in the process of being submitted.")
    completed = PermissibleValue(text="completed",
                                         description="Signifies that the Submission is completed.")

    _defn = EnumDefinition(
        name="SubmissionStatusEnum",
        description="Enum to capture the status of a Submission.",
    )

class ReleaseStatusEnum(EnumDefinitionImpl):
    """
    Enum to capture the release status of an entity.
    """
    unreleased = PermissibleValue(text="unreleased",
                                           description="signifies that the entity has not yet been release for public consumption.")
    released = PermissibleValue(text="released",
                                       description="signifies that the entity has been release for public consumption.")

    _defn = EnumDefinition(
        name="ReleaseStatusEnum",
        description="Enum to capture the release status of an entity.",
    )

class ExperimentProcessTypeEnum(EnumDefinitionImpl):
    """
    The different types of Experiment Processes.
    """
    sample_preparation = PermissibleValue(text="sample_preparation",
                                                           description="An Experiment Process that represents the transformation of a Sample in preparation for an assay. When an Experiment Process is of type 'sample preparation', both the input and output to the Experiment Process is a Sample.")
    assay = PermissibleValue(text="assay",
                                 description="An Experiment Process that represents an assay which performs measurement on a Sample to generate data. When an Experiemnt Process is of type 'assay', the input is a Sample and the output is a File.")

    _defn = EnumDefinition(
        name="ExperimentProcessTypeEnum",
        description="The different types of Experiment Processes.",
    )

class AgeRangeEnum(EnumDefinitionImpl):
    """
    Enum to capture the age range that an Indiviudal belongs to.
    """
    unknown = PermissibleValue(text="unknown",
                                     description="Age range unknown.")

    _defn = EnumDefinition(
        name="AgeRangeEnum",
        description="Enum to capture the age range that an Indiviudal belongs to.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0-5",
                PermissibleValue(text="0-5",
                                 description="Age between 0 to 5.") )
        setattr(cls, "6-10",
                PermissibleValue(text="6-10",
                                 description="Age between 6 to 10.") )
        setattr(cls, "11-15",
                PermissibleValue(text="11-15",
                                 description="Age between 11 to 15.") )
        setattr(cls, "16-20",
                PermissibleValue(text="16-20",
                                 description="Age between 16 to 20.") )
        setattr(cls, "21-25",
                PermissibleValue(text="21-25",
                                 description="Age between 21 to 25.") )
        setattr(cls, "26-30",
                PermissibleValue(text="26-30",
                                 description="Age between 26 to 30.") )
        setattr(cls, "31-35",
                PermissibleValue(text="31-35",
                                 description="Age between 31 to 35.") )
        setattr(cls, "36-40",
                PermissibleValue(text="36-40",
                                 description="Age between 36 to 40.") )
        setattr(cls, "41-45",
                PermissibleValue(text="41-45",
                                 description="Age between 41 to 45.") )
        setattr(cls, "46-50",
                PermissibleValue(text="46-50",
                                 description="Age between 46 to 50.") )
        setattr(cls, "51-55",
                PermissibleValue(text="51-55",
                                 description="Age between 51 to 55.") )
        setattr(cls, "56-60",
                PermissibleValue(text="56-60",
                                 description="Age between 56 to 60.") )
        setattr(cls, "61-65",
                PermissibleValue(text="61-65",
                                 description="Age between 61 to 65.") )
        setattr(cls, "66-70",
                PermissibleValue(text="66-70",
                                 description="Age between 66 to 70.") )
        setattr(cls, "71-75",
                PermissibleValue(text="71-75",
                                 description="Age between 71 to 75.") )
        setattr(cls, "76-80",
                PermissibleValue(text="76-80",
                                 description="Age between 76 to 80.") )
        setattr(cls, "80+",
                PermissibleValue(text="80+",
                                 description="Age above 80.") )

# Slots
class slots:
    pass

slots.schema_type = Slot(uri=GHGA.schema_type, name="schema type", curie=GHGA.curie('schema_type'),
                   model_uri=GHGA.schema_type, domain=None, range=Optional[str])

slots.schema_version = Slot(uri=GHGA.schema_version, name="schema version", curie=GHGA.curie('schema_version'),
                   model_uri=GHGA.schema_version, domain=None, range=Optional[str])

slots.alias = Slot(uri=GHGA.alias, name="alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.alias, domain=None, range=str)

slots.accession = Slot(uri=GHGA.accession, name="accession", curie=GHGA.curie('accession'),
                   model_uri=GHGA.accession, domain=None, range=Optional[str])

slots.ega_accession = Slot(uri=GHGA.ega_accession, name="ega accession", curie=GHGA.curie('ega_accession'),
                   model_uri=GHGA.ega_accession, domain=None, range=Optional[str])

slots.given_name = Slot(uri=GHGA.given_name, name="given name", curie=GHGA.curie('given_name'),
                   model_uri=GHGA.given_name, domain=None, range=Optional[str])

slots.family_name = Slot(uri=GHGA.family_name, name="family name", curie=GHGA.curie('family_name'),
                   model_uri=GHGA.family_name, domain=None, range=Optional[str])

slots.additional_name = Slot(uri=GHGA.additional_name, name="additional name", curie=GHGA.curie('additional_name'),
                   model_uri=GHGA.additional_name, domain=None, range=Optional[str])

slots.name = Slot(uri=GHGA.name, name="name", curie=GHGA.curie('name'),
                   model_uri=GHGA.name, domain=None, range=Optional[str])

slots.type = Slot(uri=GHGA.type, name="type", curie=GHGA.curie('type'),
                   model_uri=GHGA.type, domain=None, range=Optional[str])

slots.title = Slot(uri=GHGA.title, name="title", curie=GHGA.curie('title'),
                   model_uri=GHGA.title, domain=None, range=Optional[str])

slots.abstract = Slot(uri=GHGA.abstract, name="abstract", curie=GHGA.curie('abstract'),
                   model_uri=GHGA.abstract, domain=None, range=Optional[str])

slots.technical_replicates = Slot(uri=GHGA.technical_replicates, name="technical replicates", curie=GHGA.curie('technical_replicates'),
                   model_uri=GHGA.technical_replicates, domain=None, range=Optional[str])

slots.biological_replicates = Slot(uri=GHGA.biological_replicates, name="biological replicates", curie=GHGA.curie('biological_replicates'),
                   model_uri=GHGA.biological_replicates, domain=None, range=Optional[str])

slots.experimental_replicates = Slot(uri=GHGA.experimental_replicates, name="experimental replicates", curie=GHGA.curie('experimental_replicates'),
                   model_uri=GHGA.experimental_replicates, domain=None, range=Optional[str])

slots.xref = Slot(uri=GHGA.xref, name="xref", curie=GHGA.curie('xref'),
                   model_uri=GHGA.xref, domain=None, range=Optional[Union[str, List[str]]])

slots.url = Slot(uri=GHGA.url, name="url", curie=GHGA.curie('url'),
                   model_uri=GHGA.url, domain=None, range=Optional[str])

slots.has_attribute = Slot(uri=GHGA.has_attribute, name="has attribute", curie=GHGA.curie('has_attribute'),
                   model_uri=GHGA.has_attribute, domain=None, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.description = Slot(uri=GHGA.description, name="description", curie=GHGA.curie('description'),
                   model_uri=GHGA.description, domain=None, range=Optional[str])

slots.has_study = Slot(uri=GHGA.has_study, name="has study", curie=GHGA.curie('has_study'),
                   model_uri=GHGA.has_study, domain=None, range=Optional[Union[dict, CreateStudy]])

slots.has_project = Slot(uri=GHGA.has_project, name="has project", curie=GHGA.curie('has_project'),
                   model_uri=GHGA.has_project, domain=None, range=Optional[Union[dict, CreateProject]])

slots.has_publication = Slot(uri=GHGA.has_publication, name="has publication", curie=GHGA.curie('has_publication'),
                   model_uri=GHGA.has_publication, domain=None, range=Optional[Union[dict, CreatePublication]])

slots.has_sample = Slot(uri=GHGA.has_sample, name="has sample", curie=GHGA.curie('has_sample'),
                   model_uri=GHGA.has_sample, domain=None, range=Optional[Union[dict, CreateSample]])

slots.has_protocol = Slot(uri=GHGA.has_protocol, name="has protocol", curie=GHGA.curie('has_protocol'),
                   model_uri=GHGA.has_protocol, domain=None, range=Optional[Union[dict, CreateProtocol]])

slots.has_experiment = Slot(uri=GHGA.has_experiment, name="has experiment", curie=GHGA.curie('has_experiment'),
                   model_uri=GHGA.has_experiment, domain=None, range=Optional[Union[dict, CreateExperiment]])

slots.has_analysis = Slot(uri=GHGA.has_analysis, name="has analysis", curie=GHGA.curie('has_analysis'),
                   model_uri=GHGA.has_analysis, domain=None, range=Optional[str])

slots.has_sequencing_protocol = Slot(uri=GHGA.has_sequencing_protocol, name="has sequencing protocol", curie=GHGA.curie('has_sequencing_protocol'),
                   model_uri=GHGA.has_sequencing_protocol, domain=None, range=Optional[str])

slots.has_library_preparation_protocol = Slot(uri=GHGA.has_library_preparation_protocol, name="has library preparation protocol", curie=GHGA.curie('has_library_preparation_protocol'),
                   model_uri=GHGA.has_library_preparation_protocol, domain=None, range=Optional[str])

slots.has_technology = Slot(uri=GHGA.has_technology, name="has technology", curie=GHGA.curie('has_technology'),
                   model_uri=GHGA.has_technology, domain=None, range=Optional[Union[dict, CreateTechnology]])

slots.has_experiment_process = Slot(uri=GHGA.has_experiment_process, name="has experiment process", curie=GHGA.curie('has_experiment_process'),
                   model_uri=GHGA.has_experiment_process, domain=None, range=Optional[Union[dict, CreateExperimentProcess]])

slots.has_analysis_process = Slot(uri=GHGA.has_analysis_process, name="has analysis process", curie=GHGA.curie('has_analysis_process'),
                   model_uri=GHGA.has_analysis_process, domain=None, range=Optional[Union[dict, CreateAnalysisProcess]])

slots.has_file = Slot(uri=GHGA.has_file, name="has file", curie=GHGA.curie('has_file'),
                   model_uri=GHGA.has_file, domain=None, range=Optional[Union[dict, CreateFile]])

slots.has_input = Slot(uri=GHGA.has_input, name="has input", curie=GHGA.curie('has_input'),
                   model_uri=GHGA.has_input, domain=None, range=Optional[Union[dict, CreateFile]])

slots.has_output = Slot(uri=GHGA.has_output, name="has output", curie=GHGA.curie('has_output'),
                   model_uri=GHGA.has_output, domain=None, range=Optional[Union[dict, CreateFile]])

slots.has_agent = Slot(uri=GHGA.has_agent, name="has agent", curie=GHGA.curie('has_agent'),
                   model_uri=GHGA.has_agent, domain=None, range=Optional[Union[dict, CreateAgent]])

slots.has_workflow = Slot(uri=GHGA.has_workflow, name="has workflow", curie=GHGA.curie('has_workflow'),
                   model_uri=GHGA.has_workflow, domain=None, range=Optional[Union[dict, CreateWorkflow]])

slots.has_workflow_step = Slot(uri=GHGA.has_workflow_step, name="has workflow step", curie=GHGA.curie('has_workflow_step'),
                   model_uri=GHGA.has_workflow_step, domain=None, range=Optional[Union[dict, CreateWorkflowStep]])

slots.has_workflow_parameter = Slot(uri=GHGA.has_workflow_parameter, name="has workflow parameter", curie=GHGA.curie('has_workflow_parameter'),
                   model_uri=GHGA.has_workflow_parameter, domain=None, range=Optional[Union[dict, WorkflowParameter]])

slots.has_dataset = Slot(uri=GHGA.has_dataset, name="has dataset", curie=GHGA.curie('has_dataset'),
                   model_uri=GHGA.has_dataset, domain=None, range=Optional[Union[dict, CreateDataset]])

slots.has_biospecimen = Slot(uri=GHGA.has_biospecimen, name="has biospecimen", curie=GHGA.curie('has_biospecimen'),
                   model_uri=GHGA.has_biospecimen, domain=None, range=Optional[Union[dict, CreateBiospecimen]])

slots.has_individual = Slot(uri=GHGA.has_individual, name="has individual", curie=GHGA.curie('has_individual'),
                   model_uri=GHGA.has_individual, domain=None, range=Optional[Union[dict, CreateIndividual]])

slots.has_anatomical_entity = Slot(uri=GHGA.has_anatomical_entity, name="has anatomical entity", curie=GHGA.curie('has_anatomical_entity'),
                   model_uri=GHGA.has_anatomical_entity, domain=None, range=Optional[Union[dict, CreateAnatomicalEntity]])

slots.geographical_region = Slot(uri=GHGA.geographical_region, name="geographical region", curie=GHGA.curie('geographical_region'),
                   model_uri=GHGA.geographical_region, domain=None, range=Optional[str])

slots.has_disease = Slot(uri=GHGA.has_disease, name="has disease", curie=GHGA.curie('has_disease'),
                   model_uri=GHGA.has_disease, domain=None, range=Optional[Union[dict, CreateDisease]])

slots.has_phenotypic_feature = Slot(uri=GHGA.has_phenotypic_feature, name="has phenotypic feature", curie=GHGA.curie('has_phenotypic_feature'),
                   model_uri=GHGA.has_phenotypic_feature, domain=None, range=Optional[Union[dict, CreatePhenotypicFeature]])

slots.has_parent = Slot(uri=GHGA.has_parent, name="has parent", curie=GHGA.curie('has_parent'),
                   model_uri=GHGA.has_parent, domain=None, range=Optional[str])

slots.has_children = Slot(uri=GHGA.has_children, name="has children", curie=GHGA.curie('has_children'),
                   model_uri=GHGA.has_children, domain=None, range=Optional[str])

slots.has_data_use_condition = Slot(uri=GHGA.has_data_use_condition, name="has data use condition", curie=GHGA.curie('has_data_use_condition'),
                   model_uri=GHGA.has_data_use_condition, domain=None, range=Optional[str])

slots.role = Slot(uri=GHGA.role, name="role", curie=GHGA.curie('role'),
                   model_uri=GHGA.role, domain=None, range=Optional[Union[str, "UserRoleEnum"]])

slots.has_proband = Slot(uri=GHGA.has_proband, name="has proband", curie=GHGA.curie('has_proband'),
                   model_uri=GHGA.has_proband, domain=None, range=Optional[Union[dict, CreateIndividual]])

slots.has_data_use_permission = Slot(uri=GHGA.has_data_use_permission, name="has data use permission", curie=GHGA.curie('has_data_use_permission'),
                   model_uri=GHGA.has_data_use_permission, domain=None, range=Optional[Union[dict, CreateDataUsePermission]])

slots.has_data_use_modifier = Slot(uri=GHGA.has_data_use_modifier, name="has data use modifier", curie=GHGA.curie('has_data_use_modifier'),
                   model_uri=GHGA.has_data_use_modifier, domain=None, range=Optional[Union[dict, CreateDataUseModifier]])

slots.sex = Slot(uri=GHGA.sex, name="sex", curie=GHGA.curie('sex'),
                   model_uri=GHGA.sex, domain=None, range=Optional[Union[str, "BiologicalSexEnum"]])

slots.karyotype = Slot(uri=GHGA.karyotype, name="karyotype", curie=GHGA.curie('karyotype'),
                   model_uri=GHGA.karyotype, domain=None, range=Optional[str])

slots.age = Slot(uri=GHGA.age, name="age", curie=GHGA.curie('age'),
                   model_uri=GHGA.age, domain=None, range=Optional[Union[str, "AgeRangeEnum"]])

slots.tissue = Slot(uri=GHGA.tissue, name="tissue", curie=GHGA.curie('tissue'),
                   model_uri=GHGA.tissue, domain=None, range=Optional[str])

slots.isolation = Slot(uri=GHGA.isolation, name="isolation", curie=GHGA.curie('isolation'),
                   model_uri=GHGA.isolation, domain=None, range=Optional[str])

slots.storage = Slot(uri=GHGA.storage, name="storage", curie=GHGA.curie('storage'),
                   model_uri=GHGA.storage, domain=None, range=Optional[str])

slots.vital_status = Slot(uri=GHGA.vital_status, name="vital status", curie=GHGA.curie('vital_status'),
                   model_uri=GHGA.vital_status, domain=None, range=Optional[Union[str, "VitalStatusEnum"]])

slots.has_ancestry = Slot(uri=GHGA.has_ancestry, name="has ancestry", curie=GHGA.curie('has_ancestry'),
                   model_uri=GHGA.has_ancestry, domain=None, range=Optional[Union[Union[dict, CreateAncestry], List[Union[dict, CreateAncestry]]]])

slots.format = Slot(uri=GHGA.format, name="format", curie=GHGA.curie('format'),
                   model_uri=GHGA.format, domain=None, range=Optional[Union[str, "FileFormatEnum"]])

slots.size = Slot(uri=GHGA.size, name="size", curie=GHGA.curie('size'),
                   model_uri=GHGA.size, domain=None, range=Optional[int])

slots.checksum = Slot(uri=GHGA.checksum, name="checksum", curie=GHGA.curie('checksum'),
                   model_uri=GHGA.checksum, domain=None, range=Optional[str])

slots.checksum_type = Slot(uri=GHGA.checksum_type, name="checksum type", curie=GHGA.curie('checksum_type'),
                   model_uri=GHGA.checksum_type, domain=None, range=Optional[str])

slots.drs_uri = Slot(uri=GHGA.drs_uri, name="drs uri", curie=GHGA.curie('drs_uri'),
                   model_uri=GHGA.drs_uri, domain=None, range=Optional[str])

slots.category = Slot(uri=GHGA.category, name="category", curie=GHGA.curie('category'),
                   model_uri=GHGA.category, domain=None, range=Optional[str])

slots.has_data_access_policy = Slot(uri=GHGA.has_data_access_policy, name="has data access policy", curie=GHGA.curie('has_data_access_policy'),
                   model_uri=GHGA.has_data_access_policy, domain=None, range=Optional[Union[dict, CreateDataAccessPolicy]])

slots.policy_text = Slot(uri=GHGA.policy_text, name="policy text", curie=GHGA.curie('policy_text'),
                   model_uri=GHGA.policy_text, domain=None, range=Optional[str])

slots.policy_url = Slot(uri=GHGA.policy_url, name="policy url", curie=GHGA.curie('policy_url'),
                   model_uri=GHGA.policy_url, domain=None, range=Optional[str])

slots.has_data_access_committee = Slot(uri=GHGA.has_data_access_committee, name="has data access committee", curie=GHGA.curie('has_data_access_committee'),
                   model_uri=GHGA.has_data_access_committee, domain=None, range=Optional[Union[dict, CreateDataAccessCommittee]])

slots.main_contact = Slot(uri=GHGA.main_contact, name="main contact", curie=GHGA.curie('main_contact'),
                   model_uri=GHGA.main_contact, domain=None, range=Optional[Union[dict, CreateMember]])

slots.has_member = Slot(uri=GHGA.has_member, name="has member", curie=GHGA.curie('has_member'),
                   model_uri=GHGA.has_member, domain=None, range=Optional[str])

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

slots.affiliation = Slot(uri=GHGA.affiliation, name="affiliation", curie=GHGA.curie('affiliation'),
                   model_uri=GHGA.affiliation, domain=None, range=Optional[str])

slots.library_name = Slot(uri=GHGA.library_name, name="library name", curie=GHGA.curie('library_name'),
                   model_uri=GHGA.library_name, domain=None, range=Optional[str])

slots.library_layout = Slot(uri=GHGA.library_layout, name="library layout", curie=GHGA.curie('library_layout'),
                   model_uri=GHGA.library_layout, domain=None, range=Optional[str])

slots.library_type = Slot(uri=GHGA.library_type, name="library type", curie=GHGA.curie('library_type'),
                   model_uri=GHGA.library_type, domain=None, range=Optional[str])

slots.library_selection = Slot(uri=GHGA.library_selection, name="library selection", curie=GHGA.curie('library_selection'),
                   model_uri=GHGA.library_selection, domain=None, range=Optional[str])

slots.library_preparation = Slot(uri=GHGA.library_preparation, name="library preparation", curie=GHGA.curie('library_preparation'),
                   model_uri=GHGA.library_preparation, domain=None, range=Optional[str])

slots.library_preparation_kit_retail_name = Slot(uri=GHGA.library_preparation_kit_retail_name, name="library preparation kit retail name", curie=GHGA.curie('library_preparation_kit_retail_name'),
                   model_uri=GHGA.library_preparation_kit_retail_name, domain=None, range=Optional[str])

slots.library_preparation_kit_manufacturer = Slot(uri=GHGA.library_preparation_kit_manufacturer, name="library preparation kit manufacturer", curie=GHGA.curie('library_preparation_kit_manufacturer'),
                   model_uri=GHGA.library_preparation_kit_manufacturer, domain=None, range=Optional[str])

slots.primer = Slot(uri=GHGA.primer, name="primer", curie=GHGA.curie('primer'),
                   model_uri=GHGA.primer, domain=None, range=Optional[str])

slots.end_bias = Slot(uri=GHGA.end_bias, name="end bias", curie=GHGA.curie('end_bias'),
                   model_uri=GHGA.end_bias, domain=None, range=Optional[str])

slots.target_regions = Slot(uri=GHGA.target_regions, name="target regions", curie=GHGA.curie('target_regions'),
                   model_uri=GHGA.target_regions, domain=None, range=Optional[str])

slots.rnaseq_strandedness = Slot(uri=GHGA.rnaseq_strandedness, name="rnaseq strandedness", curie=GHGA.curie('rnaseq_strandedness'),
                   model_uri=GHGA.rnaseq_strandedness, domain=None, range=Optional[str])

slots.sequencing_center = Slot(uri=GHGA.sequencing_center, name="sequencing center", curie=GHGA.curie('sequencing_center'),
                   model_uri=GHGA.sequencing_center, domain=None, range=Optional[str])

slots.instrument_model = Slot(uri=GHGA.instrument_model, name="instrument model", curie=GHGA.curie('instrument_model'),
                   model_uri=GHGA.instrument_model, domain=None, range=Optional[str])

slots.sequencing_read_length = Slot(uri=GHGA.sequencing_read_length, name="sequencing read length", curie=GHGA.curie('sequencing_read_length'),
                   model_uri=GHGA.sequencing_read_length, domain=None, range=Optional[str])

slots.index_sequence = Slot(uri=GHGA.index_sequence, name="index sequence", curie=GHGA.curie('index_sequence'),
                   model_uri=GHGA.index_sequence, domain=None, range=Optional[str])

slots.paired_or_single_end = Slot(uri=GHGA.paired_or_single_end, name="paired or single end", curie=GHGA.curie('paired_or_single_end'),
                   model_uri=GHGA.paired_or_single_end, domain=None, range=Optional[Union[str, "PairedOrSingleEndEnum"]])

slots.forward_or_reverse = Slot(uri=GHGA.forward_or_reverse, name="forward or reverse", curie=GHGA.curie('forward_or_reverse'),
                   model_uri=GHGA.forward_or_reverse, domain=None, range=Optional[Union[str, "ForwardOrReverseEnum"]])

slots.reference_chromosome = Slot(uri=GHGA.reference_chromosome, name="reference chromosome", curie=GHGA.curie('reference_chromosome'),
                   model_uri=GHGA.reference_chromosome, domain=None, range=Optional[str])

slots.reference_genome = Slot(uri=GHGA.reference_genome, name="reference genome", curie=GHGA.curie('reference_genome'),
                   model_uri=GHGA.reference_genome, domain=None, range=Optional[str])

slots.lane_number = Slot(uri=GHGA.lane_number, name="lane number", curie=GHGA.curie('lane_number'),
                   model_uri=GHGA.lane_number, domain=None, range=Optional[str])

slots.target_coverage = Slot(uri=GHGA.target_coverage, name="target coverage", curie=GHGA.curie('target_coverage'),
                   model_uri=GHGA.target_coverage, domain=None, range=Optional[str])

slots.flow_cell_id = Slot(uri=GHGA.flow_cell_id, name="flow cell id", curie=GHGA.curie('flow_cell_id'),
                   model_uri=GHGA.flow_cell_id, domain=None, range=Optional[str])

slots.flow_cell_type = Slot(uri=GHGA.flow_cell_type, name="flow cell type", curie=GHGA.curie('flow_cell_type'),
                   model_uri=GHGA.flow_cell_type, domain=None, range=Optional[str])

slots.umi_barcode_read = Slot(uri=GHGA.umi_barcode_read, name="umi barcode read", curie=GHGA.curie('umi_barcode_read'),
                   model_uri=GHGA.umi_barcode_read, domain=None, range=Optional[str])

slots.umi_barcode_offset = Slot(uri=GHGA.umi_barcode_offset, name="umi barcode offset", curie=GHGA.curie('umi_barcode_offset'),
                   model_uri=GHGA.umi_barcode_offset, domain=None, range=Optional[str])

slots.umi_barcode_size = Slot(uri=GHGA.umi_barcode_size, name="umi barcode size", curie=GHGA.curie('umi_barcode_size'),
                   model_uri=GHGA.umi_barcode_size, domain=None, range=Optional[str])

slots.cell_barcode_read = Slot(uri=GHGA.cell_barcode_read, name="cell barcode read", curie=GHGA.curie('cell_barcode_read'),
                   model_uri=GHGA.cell_barcode_read, domain=None, range=Optional[str])

slots.cell_barcode_offset = Slot(uri=GHGA.cell_barcode_offset, name="cell barcode offset", curie=GHGA.curie('cell_barcode_offset'),
                   model_uri=GHGA.cell_barcode_offset, domain=None, range=Optional[str])

slots.cell_barcode_size = Slot(uri=GHGA.cell_barcode_size, name="cell barcode size", curie=GHGA.curie('cell_barcode_size'),
                   model_uri=GHGA.cell_barcode_size, domain=None, range=Optional[str])

slots.sample_barcode_read = Slot(uri=GHGA.sample_barcode_read, name="sample barcode read", curie=GHGA.curie('sample_barcode_read'),
                   model_uri=GHGA.sample_barcode_read, domain=None, range=Optional[str])

slots.case_control_status = Slot(uri=GHGA.case_control_status, name="case control status", curie=GHGA.curie('case_control_status'),
                   model_uri=GHGA.case_control_status, domain=None, range=Optional[Union[str, "CaseControlStatusEnum"]])

slots.vital_status_at_sampling = Slot(uri=GHGA.vital_status_at_sampling, name="vital status at sampling", curie=GHGA.curie('vital_status_at_sampling'),
                   model_uri=GHGA.vital_status_at_sampling, domain=None, range=Optional[Union[str, "VitalStatusEnum"]])

slots.submission_status = Slot(uri=GHGA.submission_status, name="submission status", curie=GHGA.curie('submission_status'),
                   model_uri=GHGA.submission_status, domain=None, range=Optional[str])

slots.submission_date = Slot(uri=GHGA.submission_date, name="submission date", curie=GHGA.curie('submission_date'),
                   model_uri=GHGA.submission_date, domain=None, range=Optional[str])

slots.release_status = Slot(uri=GHGA.release_status, name="release status", curie=GHGA.curie('release_status'),
                   model_uri=GHGA.release_status, domain=None, range=Optional[str])

slots.release_date = Slot(uri=GHGA.release_date, name="release date", curie=GHGA.curie('release_date'),
                   model_uri=GHGA.release_date, domain=None, range=Optional[str])

slots.deprecation_date = Slot(uri=GHGA.deprecation_date, name="deprecation date", curie=GHGA.curie('deprecation_date'),
                   model_uri=GHGA.deprecation_date, domain=None, range=Optional[str])

slots.replaced_by = Slot(uri=GHGA.replaced_by, name="replaced by", curie=GHGA.curie('replaced_by'),
                   model_uri=GHGA.replaced_by, domain=NamedThing, range=Optional[Union[dict, "NamedThing"]])

slots.replaces = Slot(uri=GHGA.replaces, name="replaces", curie=GHGA.curie('replaces'),
                   model_uri=GHGA.replaces, domain=NamedThing, range=Optional[Union[dict, "NamedThing"]])

slots.data_request_form = Slot(uri=GHGA.data_request_form, name="data request form", curie=GHGA.curie('data_request_form'),
                   model_uri=GHGA.data_request_form, domain=None, range=Optional[str])

slots.concept_identifier = Slot(uri=GHGA.concept_identifier, name="concept identifier", curie=GHGA.curie('concept_identifier'),
                   model_uri=GHGA.concept_identifier, domain=None, range=Optional[str])

slots.concept_name = Slot(uri=GHGA.concept_name, name="concept name", curie=GHGA.curie('concept_name'),
                   model_uri=GHGA.concept_name, domain=None, range=Optional[str])

slots.ontology_name = Slot(uri=GHGA.ontology_name, name="ontology name", curie=GHGA.curie('ontology_name'),
                   model_uri=GHGA.ontology_name, domain=None, range=Optional[str])

slots.ontology_version = Slot(uri=GHGA.ontology_version, name="ontology version", curie=GHGA.curie('ontology_version'),
                   model_uri=GHGA.ontology_version, domain=None, range=Optional[str])

slots.named_thing_alias = Slot(uri=GHGA.alias, name="named thing_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.named_thing_alias, domain=NamedThing, range=str)

slots.named_thing_xref = Slot(uri=GHGA.xref, name="named thing_xref", curie=GHGA.curie('xref'),
                   model_uri=GHGA.named_thing_xref, domain=NamedThing, range=Optional[Union[str, List[str]]])

slots.attribute_key = Slot(uri=GHGA.key, name="attribute_key", curie=GHGA.curie('key'),
                   model_uri=GHGA.attribute_key, domain=Attribute, range=str)

slots.attribute_key_type = Slot(uri=GHGA.key_type, name="attribute_key type", curie=GHGA.curie('key_type'),
                   model_uri=GHGA.attribute_key_type, domain=Attribute, range=Optional[str])

slots.attribute_value = Slot(uri=GHGA.value, name="attribute_value", curie=GHGA.curie('value'),
                   model_uri=GHGA.attribute_value, domain=Attribute, range=str)

slots.attribute_value_type = Slot(uri=GHGA.value_type, name="attribute_value type", curie=GHGA.curie('value_type'),
                   model_uri=GHGA.attribute_value_type, domain=Attribute, range=Optional[str])

slots.create_project_alias = Slot(uri=GHGA.alias, name="create project_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.create_project_alias, domain=CreateProject, range=str)

slots.create_project_title = Slot(uri=GHGA.title, name="create project_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.create_project_title, domain=CreateProject, range=str)

slots.create_project_description = Slot(uri=GHGA.description, name="create project_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.create_project_description, domain=CreateProject, range=str)

slots.create_project_has_publication = Slot(uri=GHGA.has_publication, name="create project_has publication", curie=GHGA.curie('has_publication'),
                   model_uri=GHGA.create_project_has_publication, domain=CreateProject, range=Optional[Union[Union[dict, "CreatePublication"], List[Union[dict, "CreatePublication"]]]])

slots.create_project_has_attribute = Slot(uri=GHGA.has_attribute, name="create project_has attribute", curie=GHGA.curie('has_attribute'),
                   model_uri=GHGA.create_project_has_attribute, domain=CreateProject, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.create_study_alias = Slot(uri=GHGA.alias, name="create study_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.create_study_alias, domain=CreateStudy, range=str)

slots.create_study_title = Slot(uri=GHGA.title, name="create study_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.create_study_title, domain=CreateStudy, range=str)

slots.create_study_description = Slot(uri=GHGA.description, name="create study_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.create_study_description, domain=CreateStudy, range=str)

slots.create_study_type = Slot(uri=GHGA.type, name="create study_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.create_study_type, domain=CreateStudy, range=Union[str, "StudyTypeEnum"])

slots.create_study_affiliation = Slot(uri=GHGA.affiliation, name="create study_affiliation", curie=GHGA.curie('affiliation'),
                   model_uri=GHGA.create_study_affiliation, domain=CreateStudy, range=Union[str, List[str]])

slots.create_study_has_publication = Slot(uri=GHGA.has_publication, name="create study_has publication", curie=GHGA.curie('has_publication'),
                   model_uri=GHGA.create_study_has_publication, domain=CreateStudy, range=Optional[Union[Union[dict, "CreatePublication"], List[Union[dict, "CreatePublication"]]]])

slots.create_study_has_project = Slot(uri=GHGA.has_project, name="create study_has project", curie=GHGA.curie('has_project'),
                   model_uri=GHGA.create_study_has_project, domain=CreateStudy, range=Optional[Union[dict, CreateProject]])

slots.create_study_has_attribute = Slot(uri=GHGA.has_attribute, name="create study_has attribute", curie=GHGA.curie('has_attribute'),
                   model_uri=GHGA.create_study_has_attribute, domain=CreateStudy, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.create_study_release_status = Slot(uri=GHGA.release_status, name="create study_release status", curie=GHGA.curie('release_status'),
                   model_uri=GHGA.create_study_release_status, domain=CreateStudy, range=Optional[Union[str, "ReleaseStatusEnum"]])

slots.create_study_has_file = Slot(uri=GHGA.has_file, name="create study_has file", curie=GHGA.curie('has_file'),
                   model_uri=GHGA.create_study_has_file, domain=CreateStudy, range=Optional[Union[Union[dict, "CreateFile"], List[Union[dict, "CreateFile"]]]])

slots.create_experiment_alias = Slot(uri=GHGA.alias, name="create experiment_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.create_experiment_alias, domain=CreateExperiment, range=str)

slots.create_experiment_title = Slot(uri=GHGA.title, name="create experiment_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.create_experiment_title, domain=CreateExperiment, range=Optional[str])

slots.create_experiment_description = Slot(uri=GHGA.description, name="create experiment_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.create_experiment_description, domain=CreateExperiment, range=str)

slots.create_experiment_type = Slot(uri=GHGA.type, name="create experiment_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.create_experiment_type, domain=CreateExperiment, range=Optional[str])

slots.create_experiment_has_study = Slot(uri=GHGA.has_study, name="create experiment_has study", curie=GHGA.curie('has_study'),
                   model_uri=GHGA.create_experiment_has_study, domain=CreateExperiment, range=Union[dict, CreateStudy])

slots.create_experiment_has_sample = Slot(uri=GHGA.has_sample, name="create experiment_has sample", curie=GHGA.curie('has_sample'),
                   model_uri=GHGA.create_experiment_has_sample, domain=CreateExperiment, range=Union[Union[dict, "CreateSample"], List[Union[dict, "CreateSample"]]])

slots.create_experiment_has_file = Slot(uri=GHGA.has_file, name="create experiment_has file", curie=GHGA.curie('has_file'),
                   model_uri=GHGA.create_experiment_has_file, domain=CreateExperiment, range=Optional[Union[Union[dict, "CreateFile"], List[Union[dict, "CreateFile"]]]])

slots.create_experiment_has_protocol = Slot(uri=GHGA.has_protocol, name="create experiment_has protocol", curie=GHGA.curie('has_protocol'),
                   model_uri=GHGA.create_experiment_has_protocol, domain=CreateExperiment, range=Union[Union[dict, "CreateProtocol"], List[Union[dict, "CreateProtocol"]]])

slots.create_experiment_has_experiment_process = Slot(uri=GHGA.has_experiment_process, name="create experiment_has experiment process", curie=GHGA.curie('has_experiment_process'),
                   model_uri=GHGA.create_experiment_has_experiment_process, domain=CreateExperiment, range=Optional[Union[Union[dict, "CreateExperimentProcess"], List[Union[dict, "CreateExperimentProcess"]]]])

slots.create_experiment_process_type = Slot(uri=GHGA.type, name="create experiment process_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.create_experiment_process_type, domain=CreateExperimentProcess, range=Optional[Union[str, "ExperimentProcessTypeEnum"]])

slots.create_experiment_process_title = Slot(uri=GHGA.title, name="create experiment process_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.create_experiment_process_title, domain=CreateExperimentProcess, range=Optional[str])

slots.create_experiment_process_has_input = Slot(uri=GHGA.has_input, name="create experiment process_has input", curie=GHGA.curie('has_input'),
                   model_uri=GHGA.create_experiment_process_has_input, domain=CreateExperimentProcess, range=Optional[Union[dict, "CreateSample"]])

slots.create_experiment_process_has_protocol = Slot(uri=GHGA.has_protocol, name="create experiment process_has protocol", curie=GHGA.curie('has_protocol'),
                   model_uri=GHGA.create_experiment_process_has_protocol, domain=CreateExperimentProcess, range=Optional[Union[dict, "CreateProtocol"]])

slots.create_experiment_process_has_agent = Slot(uri=GHGA.has_agent, name="create experiment process_has agent", curie=GHGA.curie('has_agent'),
                   model_uri=GHGA.create_experiment_process_has_agent, domain=CreateExperimentProcess, range=Optional[Union[dict, CreateAgent]])

slots.create_experiment_process_has_output = Slot(uri=GHGA.has_output, name="create experiment process_has output", curie=GHGA.curie('has_output'),
                   model_uri=GHGA.create_experiment_process_has_output, domain=CreateExperimentProcess, range=Optional[Union[Union[dict, "CreateFile"], List[Union[dict, "CreateFile"]]]])

slots.create_protocol_alias = Slot(uri=GHGA.alias, name="create protocol_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.create_protocol_alias, domain=CreateProtocol, range=str)

slots.create_protocol_name = Slot(uri=GHGA.name, name="create protocol_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.create_protocol_name, domain=CreateProtocol, range=Optional[str])

slots.create_protocol_type = Slot(uri=GHGA.type, name="create protocol_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.create_protocol_type, domain=CreateProtocol, range=Optional[str])

slots.create_protocol_description = Slot(uri=GHGA.description, name="create protocol_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.create_protocol_description, domain=CreateProtocol, range=Optional[str])

slots.create_protocol_url = Slot(uri=GHGA.url, name="create protocol_url", curie=GHGA.curie('url'),
                   model_uri=GHGA.create_protocol_url, domain=CreateProtocol, range=Optional[str])

slots.create_protocol_has_file = Slot(uri=GHGA.has_file, name="create protocol_has file", curie=GHGA.curie('has_file'),
                   model_uri=GHGA.create_protocol_has_file, domain=CreateProtocol, range=Optional[Union[dict, "CreateFile"]])

slots.create_protocol_xref = Slot(uri=GHGA.xref, name="create protocol_xref", curie=GHGA.curie('xref'),
                   model_uri=GHGA.create_protocol_xref, domain=CreateProtocol, range=Optional[Union[str, List[str]]])

slots.create_protocol_has_attribute = Slot(uri=GHGA.has_attribute, name="create protocol_has attribute", curie=GHGA.curie('has_attribute'),
                   model_uri=GHGA.create_protocol_has_attribute, domain=CreateProtocol, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.create_library_preparation_protocol_alias = Slot(uri=GHGA.alias, name="create library preparation protocol_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.create_library_preparation_protocol_alias, domain=CreateLibraryPreparationProtocol, range=str)

slots.create_library_preparation_protocol_description = Slot(uri=GHGA.description, name="create library preparation protocol_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.create_library_preparation_protocol_description, domain=CreateLibraryPreparationProtocol, range=str)

slots.create_library_preparation_protocol_library_name = Slot(uri=GHGA.library_name, name="create library preparation protocol_library name", curie=GHGA.curie('library_name'),
                   model_uri=GHGA.create_library_preparation_protocol_library_name, domain=CreateLibraryPreparationProtocol, range=str)

slots.create_library_preparation_protocol_library_layout = Slot(uri=GHGA.library_layout, name="create library preparation protocol_library layout", curie=GHGA.curie('library_layout'),
                   model_uri=GHGA.create_library_preparation_protocol_library_layout, domain=CreateLibraryPreparationProtocol, range=str)

slots.create_library_preparation_protocol_library_type = Slot(uri=GHGA.library_type, name="create library preparation protocol_library type", curie=GHGA.curie('library_type'),
                   model_uri=GHGA.create_library_preparation_protocol_library_type, domain=CreateLibraryPreparationProtocol, range=str)

slots.create_library_preparation_protocol_library_selection = Slot(uri=GHGA.library_selection, name="create library preparation protocol_library selection", curie=GHGA.curie('library_selection'),
                   model_uri=GHGA.create_library_preparation_protocol_library_selection, domain=CreateLibraryPreparationProtocol, range=str)

slots.create_library_preparation_protocol_library_preparation = Slot(uri=GHGA.library_preparation, name="create library preparation protocol_library preparation", curie=GHGA.curie('library_preparation'),
                   model_uri=GHGA.create_library_preparation_protocol_library_preparation, domain=CreateLibraryPreparationProtocol, range=str)

slots.create_library_preparation_protocol_library_preparation_kit_retail_name = Slot(uri=GHGA.library_preparation_kit_retail_name, name="create library preparation protocol_library preparation kit retail name", curie=GHGA.curie('library_preparation_kit_retail_name'),
                   model_uri=GHGA.create_library_preparation_protocol_library_preparation_kit_retail_name, domain=CreateLibraryPreparationProtocol, range=str)

slots.create_library_preparation_protocol_library_preparation_kit_manufacturer = Slot(uri=GHGA.library_preparation_kit_manufacturer, name="create library preparation protocol_library preparation kit manufacturer", curie=GHGA.curie('library_preparation_kit_manufacturer'),
                   model_uri=GHGA.create_library_preparation_protocol_library_preparation_kit_manufacturer, domain=CreateLibraryPreparationProtocol, range=str)

slots.create_library_preparation_protocol_has_attribute = Slot(uri=GHGA.has_attribute, name="create library preparation protocol_has attribute", curie=GHGA.curie('has_attribute'),
                   model_uri=GHGA.create_library_preparation_protocol_has_attribute, domain=CreateLibraryPreparationProtocol, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.create_sequencing_protocol_alias = Slot(uri=GHGA.alias, name="create sequencing protocol_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.create_sequencing_protocol_alias, domain=CreateSequencingProtocol, range=str)

slots.create_sequencing_protocol_instrument_model = Slot(uri=GHGA.instrument_model, name="create sequencing protocol_instrument model", curie=GHGA.curie('instrument_model'),
                   model_uri=GHGA.create_sequencing_protocol_instrument_model, domain=CreateSequencingProtocol, range=str)

slots.create_sequencing_protocol_type = Slot(uri=GHGA.type, name="create sequencing protocol_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.create_sequencing_protocol_type, domain=CreateSequencingProtocol, range=Optional[str])

slots.create_sequencing_protocol_description = Slot(uri=GHGA.description, name="create sequencing protocol_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.create_sequencing_protocol_description, domain=CreateSequencingProtocol, range=str)

slots.create_sequencing_protocol_has_attribute = Slot(uri=GHGA.has_attribute, name="create sequencing protocol_has attribute", curie=GHGA.curie('has_attribute'),
                   model_uri=GHGA.create_sequencing_protocol_has_attribute, domain=CreateSequencingProtocol, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.create_workflow_alias = Slot(uri=GHGA.alias, name="create workflow_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.create_workflow_alias, domain=CreateWorkflow, range=str)

slots.create_workflow_name = Slot(uri=GHGA.name, name="create workflow_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.create_workflow_name, domain=CreateWorkflow, range=str)

slots.create_workflow_has_workflow_step = Slot(uri=GHGA.has_workflow_step, name="create workflow_has workflow step", curie=GHGA.curie('has_workflow_step'),
                   model_uri=GHGA.create_workflow_has_workflow_step, domain=CreateWorkflow, range=Optional[Union[Union[dict, "CreateWorkflowStep"], List[Union[dict, "CreateWorkflowStep"]]]])

slots.create_workflow_step_has_workflow_parameter = Slot(uri=GHGA.has_workflow_parameter, name="create workflow step_has workflow parameter", curie=GHGA.curie('has_workflow_parameter'),
                   model_uri=GHGA.create_workflow_step_has_workflow_parameter, domain=CreateWorkflowStep, range=Optional[Union[Union[dict, "WorkflowParameter"], List[Union[dict, "WorkflowParameter"]]]])

slots.workflow_parameter_key = Slot(uri=GHGA.key, name="workflow parameter_key", curie=GHGA.curie('key'),
                   model_uri=GHGA.workflow_parameter_key, domain=WorkflowParameter, range=Optional[str])

slots.workflow_parameter_value = Slot(uri=GHGA.value, name="workflow parameter_value", curie=GHGA.curie('value'),
                   model_uri=GHGA.workflow_parameter_value, domain=WorkflowParameter, range=Optional[str])

slots.create_biospecimen_alias = Slot(uri=GHGA.alias, name="create biospecimen_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.create_biospecimen_alias, domain=CreateBiospecimen, range=str)

slots.create_biospecimen_type = Slot(uri=GHGA.type, name="create biospecimen_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.create_biospecimen_type, domain=CreateBiospecimen, range=Optional[str])

slots.create_biospecimen_has_individual = Slot(uri=GHGA.has_individual, name="create biospecimen_has individual", curie=GHGA.curie('has_individual'),
                   model_uri=GHGA.create_biospecimen_has_individual, domain=CreateBiospecimen, range=Optional[Union[dict, "CreateIndividual"]])

slots.create_biospecimen_has_anatomical_entity = Slot(uri=GHGA.has_anatomical_entity, name="create biospecimen_has anatomical entity", curie=GHGA.curie('has_anatomical_entity'),
                   model_uri=GHGA.create_biospecimen_has_anatomical_entity, domain=CreateBiospecimen, range=Optional[Union[Union[dict, "CreateAnatomicalEntity"], List[Union[dict, "CreateAnatomicalEntity"]]]])

slots.create_biospecimen_has_disease = Slot(uri=GHGA.has_disease, name="create biospecimen_has disease", curie=GHGA.curie('has_disease'),
                   model_uri=GHGA.create_biospecimen_has_disease, domain=CreateBiospecimen, range=Optional[Union[Union[dict, "CreateDisease"], List[Union[dict, "CreateDisease"]]]])

slots.create_biospecimen_has_phenotypic_feature = Slot(uri=GHGA.has_phenotypic_feature, name="create biospecimen_has phenotypic feature", curie=GHGA.curie('has_phenotypic_feature'),
                   model_uri=GHGA.create_biospecimen_has_phenotypic_feature, domain=CreateBiospecimen, range=Optional[Union[Union[dict, "CreatePhenotypicFeature"], List[Union[dict, "CreatePhenotypicFeature"]]]])

slots.create_sample_alias = Slot(uri=GHGA.alias, name="create sample_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.create_sample_alias, domain=CreateSample, range=str)

slots.create_sample_name = Slot(uri=GHGA.name, name="create sample_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.create_sample_name, domain=CreateSample, range=str)

slots.create_sample_type = Slot(uri=GHGA.type, name="create sample_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.create_sample_type, domain=CreateSample, range=Optional[str])

slots.create_sample_description = Slot(uri=GHGA.description, name="create sample_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.create_sample_description, domain=CreateSample, range=str)

slots.create_sample_has_individual = Slot(uri=GHGA.has_individual, name="create sample_has individual", curie=GHGA.curie('has_individual'),
                   model_uri=GHGA.create_sample_has_individual, domain=CreateSample, range=Optional[Union[dict, "CreateIndividual"]])

slots.create_sample_xref = Slot(uri=GHGA.xref, name="create sample_xref", curie=GHGA.curie('xref'),
                   model_uri=GHGA.create_sample_xref, domain=CreateSample, range=Optional[Union[str, List[str]]])

slots.create_sample_has_biospecimen = Slot(uri=GHGA.has_biospecimen, name="create sample_has biospecimen", curie=GHGA.curie('has_biospecimen'),
                   model_uri=GHGA.create_sample_has_biospecimen, domain=CreateSample, range=Optional[Union[dict, CreateBiospecimen]])

slots.create_sample_has_anatomical_entity = Slot(uri=GHGA.has_anatomical_entity, name="create sample_has anatomical entity", curie=GHGA.curie('has_anatomical_entity'),
                   model_uri=GHGA.create_sample_has_anatomical_entity, domain=CreateSample, range=Optional[Union[Union[dict, "CreateAnatomicalEntity"], List[Union[dict, "CreateAnatomicalEntity"]]]])

slots.create_individual_alias = Slot(uri=GHGA.alias, name="create individual_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.create_individual_alias, domain=CreateIndividual, range=str)

slots.create_individual_sex = Slot(uri=GHGA.sex, name="create individual_sex", curie=GHGA.curie('sex'),
                   model_uri=GHGA.create_individual_sex, domain=CreateIndividual, range=Union[str, "BiologicalSexEnum"])

slots.create_individual_age = Slot(uri=GHGA.age, name="create individual_age", curie=GHGA.curie('age'),
                   model_uri=GHGA.create_individual_age, domain=CreateIndividual, range=Union[str, "AgeRangeEnum"])

slots.create_individual_vital_status = Slot(uri=GHGA.vital_status, name="create individual_vital status", curie=GHGA.curie('vital_status'),
                   model_uri=GHGA.create_individual_vital_status, domain=CreateIndividual, range=Union[str, "VitalStatusEnum"])

slots.create_individual_has_parent = Slot(uri=GHGA.has_parent, name="create individual_has parent", curie=GHGA.curie('has_parent'),
                   model_uri=GHGA.create_individual_has_parent, domain=CreateIndividual, range=Optional[Union[Union[dict, "CreateIndividual"], List[Union[dict, "CreateIndividual"]]]])

slots.create_individual_has_children = Slot(uri=GHGA.has_children, name="create individual_has children", curie=GHGA.curie('has_children'),
                   model_uri=GHGA.create_individual_has_children, domain=CreateIndividual, range=Optional[Union[Union[dict, "CreateIndividual"], List[Union[dict, "CreateIndividual"]]]])

slots.create_individual_has_disease = Slot(uri=GHGA.has_disease, name="create individual_has disease", curie=GHGA.curie('has_disease'),
                   model_uri=GHGA.create_individual_has_disease, domain=CreateIndividual, range=Optional[Union[Union[dict, "CreateDisease"], List[Union[dict, "CreateDisease"]]]])

slots.create_individual_has_phenotypic_feature = Slot(uri=GHGA.has_phenotypic_feature, name="create individual_has phenotypic feature", curie=GHGA.curie('has_phenotypic_feature'),
                   model_uri=GHGA.create_individual_has_phenotypic_feature, domain=CreateIndividual, range=Optional[Union[Union[dict, "CreatePhenotypicFeature"], List[Union[dict, "CreatePhenotypicFeature"]]]])

slots.create_individual_has_file = Slot(uri=GHGA.has_file, name="create individual_has file", curie=GHGA.curie('has_file'),
                   model_uri=GHGA.create_individual_has_file, domain=CreateIndividual, range=Optional[Union[Union[dict, "CreateFile"], List[Union[dict, "CreateFile"]]]])

slots.create_family_has_individual = Slot(uri=GHGA.has_individual, name="create family_has individual", curie=GHGA.curie('has_individual'),
                   model_uri=GHGA.create_family_has_individual, domain=CreateFamily, range=Optional[Union[Union[dict, CreateIndividual], List[Union[dict, CreateIndividual]]]])

slots.create_family_has_proband = Slot(uri=GHGA.has_proband, name="create family_has proband", curie=GHGA.curie('has_proband'),
                   model_uri=GHGA.create_family_has_proband, domain=CreateFamily, range=Optional[Union[dict, CreateIndividual]])

slots.create_cohort_has_individual = Slot(uri=GHGA.has_individual, name="create cohort_has individual", curie=GHGA.curie('has_individual'),
                   model_uri=GHGA.create_cohort_has_individual, domain=CreateCohort, range=Optional[Union[Union[dict, CreateIndividual], List[Union[dict, CreateIndividual]]]])

slots.create_file_alias = Slot(uri=GHGA.alias, name="create file_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.create_file_alias, domain=CreateFile, range=str)

slots.create_file_name = Slot(uri=GHGA.name, name="create file_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.create_file_name, domain=CreateFile, range=str)

slots.create_file_format = Slot(uri=GHGA.format, name="create file_format", curie=GHGA.curie('format'),
                   model_uri=GHGA.create_file_format, domain=CreateFile, range=Union[str, "FileFormatEnum"])

slots.create_file_checksum = Slot(uri=GHGA.checksum, name="create file_checksum", curie=GHGA.curie('checksum'),
                   model_uri=GHGA.create_file_checksum, domain=CreateFile, range=str)

slots.create_file_checksum_type = Slot(uri=GHGA.checksum_type, name="create file_checksum type", curie=GHGA.curie('checksum_type'),
                   model_uri=GHGA.create_file_checksum_type, domain=CreateFile, range=str)

slots.create_file_size = Slot(uri=GHGA.size, name="create file_size", curie=GHGA.curie('size'),
                   model_uri=GHGA.create_file_size, domain=CreateFile, range=int)

slots.create_analysis_alias = Slot(uri=GHGA.alias, name="create analysis_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.create_analysis_alias, domain=CreateAnalysis, range=str)

slots.create_analysis_type = Slot(uri=GHGA.type, name="create analysis_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.create_analysis_type, domain=CreateAnalysis, range=Optional[str])

slots.create_analysis_description = Slot(uri=GHGA.description, name="create analysis_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.create_analysis_description, domain=CreateAnalysis, range=Optional[str])

slots.create_analysis_reference_genome = Slot(uri=GHGA.reference_genome, name="create analysis_reference genome", curie=GHGA.curie('reference_genome'),
                   model_uri=GHGA.create_analysis_reference_genome, domain=CreateAnalysis, range=str)

slots.create_analysis_reference_chromosome = Slot(uri=GHGA.reference_chromosome, name="create analysis_reference chromosome", curie=GHGA.curie('reference_chromosome'),
                   model_uri=GHGA.create_analysis_reference_chromosome, domain=CreateAnalysis, range=str)

slots.create_analysis_has_input = Slot(uri=GHGA.has_input, name="create analysis_has input", curie=GHGA.curie('has_input'),
                   model_uri=GHGA.create_analysis_has_input, domain=CreateAnalysis, range=Union[Union[dict, CreateFile], List[Union[dict, CreateFile]]])

slots.create_analysis_has_study = Slot(uri=GHGA.has_study, name="create analysis_has study", curie=GHGA.curie('has_study'),
                   model_uri=GHGA.create_analysis_has_study, domain=CreateAnalysis, range=Optional[Union[dict, CreateStudy]])

slots.create_analysis_has_workflow = Slot(uri=GHGA.has_workflow, name="create analysis_has workflow", curie=GHGA.curie('has_workflow'),
                   model_uri=GHGA.create_analysis_has_workflow, domain=CreateAnalysis, range=Union[Union[dict, CreateWorkflow], List[Union[dict, CreateWorkflow]]])

slots.create_analysis_has_analysis_process = Slot(uri=GHGA.has_analysis_process, name="create analysis_has analysis process", curie=GHGA.curie('has_analysis_process'),
                   model_uri=GHGA.create_analysis_has_analysis_process, domain=CreateAnalysis, range=Optional[Union[Union[dict, "CreateAnalysisProcess"], List[Union[dict, "CreateAnalysisProcess"]]]])

slots.create_analysis_has_output = Slot(uri=GHGA.has_output, name="create analysis_has output", curie=GHGA.curie('has_output'),
                   model_uri=GHGA.create_analysis_has_output, domain=CreateAnalysis, range=Union[Union[dict, CreateFile], List[Union[dict, CreateFile]]])

slots.create_analysis_process_has_input = Slot(uri=GHGA.has_input, name="create analysis process_has input", curie=GHGA.curie('has_input'),
                   model_uri=GHGA.create_analysis_process_has_input, domain=CreateAnalysisProcess, range=Optional[Union[Union[dict, CreateFile], List[Union[dict, CreateFile]]]])

slots.create_analysis_process_has_workflow = Slot(uri=GHGA.has_workflow, name="create analysis process_has workflow", curie=GHGA.curie('has_workflow'),
                   model_uri=GHGA.create_analysis_process_has_workflow, domain=CreateAnalysisProcess, range=Optional[Union[dict, CreateWorkflow]])

slots.create_analysis_process_has_agent = Slot(uri=GHGA.has_agent, name="create analysis process_has agent", curie=GHGA.curie('has_agent'),
                   model_uri=GHGA.create_analysis_process_has_agent, domain=CreateAnalysisProcess, range=Optional[Union[dict, CreateAgent]])

slots.create_analysis_process_has_output = Slot(uri=GHGA.has_output, name="create analysis process_has output", curie=GHGA.curie('has_output'),
                   model_uri=GHGA.create_analysis_process_has_output, domain=CreateAnalysisProcess, range=Optional[Union[Union[dict, CreateFile], List[Union[dict, CreateFile]]]])

slots.create_dataset_alias = Slot(uri=GHGA.alias, name="create dataset_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.create_dataset_alias, domain=CreateDataset, range=str)

slots.create_dataset_title = Slot(uri=GHGA.title, name="create dataset_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.create_dataset_title, domain=CreateDataset, range=str)

slots.create_dataset_description = Slot(uri=GHGA.description, name="create dataset_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.create_dataset_description, domain=CreateDataset, range=str)

slots.create_dataset_has_study = Slot(uri=GHGA.has_study, name="create dataset_has study", curie=GHGA.curie('has_study'),
                   model_uri=GHGA.create_dataset_has_study, domain=CreateDataset, range=Optional[Union[Union[dict, CreateStudy], List[Union[dict, CreateStudy]]]])

slots.create_dataset_has_experiment = Slot(uri=GHGA.has_experiment, name="create dataset_has experiment", curie=GHGA.curie('has_experiment'),
                   model_uri=GHGA.create_dataset_has_experiment, domain=CreateDataset, range=Optional[Union[Union[dict, CreateExperiment], List[Union[dict, CreateExperiment]]]])

slots.create_dataset_has_sample = Slot(uri=GHGA.has_sample, name="create dataset_has sample", curie=GHGA.curie('has_sample'),
                   model_uri=GHGA.create_dataset_has_sample, domain=CreateDataset, range=Optional[Union[Union[dict, CreateSample], List[Union[dict, CreateSample]]]])

slots.create_dataset_has_analysis = Slot(uri=GHGA.has_analysis, name="create dataset_has analysis", curie=GHGA.curie('has_analysis'),
                   model_uri=GHGA.create_dataset_has_analysis, domain=CreateDataset, range=Optional[Union[Union[dict, CreateAnalysis], List[Union[dict, CreateAnalysis]]]])

slots.create_dataset_has_file = Slot(uri=GHGA.has_file, name="create dataset_has file", curie=GHGA.curie('has_file'),
                   model_uri=GHGA.create_dataset_has_file, domain=CreateDataset, range=Union[Union[dict, CreateFile], List[Union[dict, CreateFile]]])

slots.create_dataset_has_data_access_policy = Slot(uri=GHGA.has_data_access_policy, name="create dataset_has data access policy", curie=GHGA.curie('has_data_access_policy'),
                   model_uri=GHGA.create_dataset_has_data_access_policy, domain=CreateDataset, range=Union[dict, "CreateDataAccessPolicy"])

slots.create_dataset_has_publication = Slot(uri=GHGA.has_publication, name="create dataset_has publication", curie=GHGA.curie('has_publication'),
                   model_uri=GHGA.create_dataset_has_publication, domain=CreateDataset, range=Optional[Union[Union[dict, "CreatePublication"], List[Union[dict, "CreatePublication"]]]])

slots.create_dataset_release_status = Slot(uri=GHGA.release_status, name="create dataset_release status", curie=GHGA.curie('release_status'),
                   model_uri=GHGA.create_dataset_release_status, domain=CreateDataset, range=Optional[Union[str, "ReleaseStatusEnum"]])

slots.create_data_use_condition_has_data_use_permission = Slot(uri=GHGA.has_data_use_permission, name="create data use condition_has data use permission", curie=GHGA.curie('has_data_use_permission'),
                   model_uri=GHGA.create_data_use_condition_has_data_use_permission, domain=CreateDataUseCondition, range=Union[dict, "CreateDataUsePermission"])

slots.create_data_use_condition_has_data_use_modifier = Slot(uri=GHGA.has_data_use_modifier, name="create data use condition_has data use modifier", curie=GHGA.curie('has_data_use_modifier'),
                   model_uri=GHGA.create_data_use_condition_has_data_use_modifier, domain=CreateDataUseCondition, range=Optional[Union[dict, "CreateDataUseModifier"]])

slots.create_data_access_policy_alias = Slot(uri=GHGA.alias, name="create data access policy_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.create_data_access_policy_alias, domain=CreateDataAccessPolicy, range=str)

slots.create_data_access_policy_name = Slot(uri=GHGA.name, name="create data access policy_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.create_data_access_policy_name, domain=CreateDataAccessPolicy, range=Optional[str])

slots.create_data_access_policy_description = Slot(uri=GHGA.description, name="create data access policy_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.create_data_access_policy_description, domain=CreateDataAccessPolicy, range=Optional[str])

slots.create_data_access_policy_policy_text = Slot(uri=GHGA.policy_text, name="create data access policy_policy text", curie=GHGA.curie('policy_text'),
                   model_uri=GHGA.create_data_access_policy_policy_text, domain=CreateDataAccessPolicy, range=str)

slots.create_data_access_policy_policy_url = Slot(uri=GHGA.policy_url, name="create data access policy_policy url", curie=GHGA.curie('policy_url'),
                   model_uri=GHGA.create_data_access_policy_policy_url, domain=CreateDataAccessPolicy, range=Optional[str])

slots.create_data_access_policy_has_data_access_committee = Slot(uri=GHGA.has_data_access_committee, name="create data access policy_has data access committee", curie=GHGA.curie('has_data_access_committee'),
                   model_uri=GHGA.create_data_access_policy_has_data_access_committee, domain=CreateDataAccessPolicy, range=Union[dict, "CreateDataAccessCommittee"])

slots.create_data_access_policy_has_data_use_condition = Slot(uri=GHGA.has_data_use_condition, name="create data access policy_has data use condition", curie=GHGA.curie('has_data_use_condition'),
                   model_uri=GHGA.create_data_access_policy_has_data_use_condition, domain=CreateDataAccessPolicy, range=Optional[Union[Union[dict, CreateDataUseCondition], List[Union[dict, CreateDataUseCondition]]]])

slots.create_data_access_policy_data_request_form = Slot(uri=GHGA.data_request_form, name="create data access policy_data request form", curie=GHGA.curie('data_request_form'),
                   model_uri=GHGA.create_data_access_policy_data_request_form, domain=CreateDataAccessPolicy, range=Optional[str])

slots.create_data_access_committee_alias = Slot(uri=GHGA.alias, name="create data access committee_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.create_data_access_committee_alias, domain=CreateDataAccessCommittee, range=str)

slots.create_data_access_committee_name = Slot(uri=GHGA.name, name="create data access committee_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.create_data_access_committee_name, domain=CreateDataAccessCommittee, range=str)

slots.create_data_access_committee_description = Slot(uri=GHGA.description, name="create data access committee_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.create_data_access_committee_description, domain=CreateDataAccessCommittee, range=Optional[str])

slots.create_data_access_committee_main_contact = Slot(uri=GHGA.main_contact, name="create data access committee_main contact", curie=GHGA.curie('main_contact'),
                   model_uri=GHGA.create_data_access_committee_main_contact, domain=CreateDataAccessCommittee, range=Optional[Union[dict, "CreateMember"]])

slots.create_data_access_committee_has_member = Slot(uri=GHGA.has_member, name="create data access committee_has member", curie=GHGA.curie('has_member'),
                   model_uri=GHGA.create_data_access_committee_has_member, domain=CreateDataAccessCommittee, range=Optional[Union[Union[dict, "CreateMember"], List[Union[dict, "CreateMember"]]]])

slots.create_member_email = Slot(uri=GHGA.email, name="create member_email", curie=GHGA.curie('email'),
                   model_uri=GHGA.create_member_email, domain=CreateMember, range=str)

slots.create_member_telephone = Slot(uri=GHGA.telephone, name="create member_telephone", curie=GHGA.curie('telephone'),
                   model_uri=GHGA.create_member_telephone, domain=CreateMember, range=Optional[str])

slots.create_member_organization = Slot(uri=GHGA.organization, name="create member_organization", curie=GHGA.curie('organization'),
                   model_uri=GHGA.create_member_organization, domain=CreateMember, range=str)

slots.create_publication_alias = Slot(uri=GHGA.alias, name="create publication_alias", curie=GHGA.curie('alias'),
                   model_uri=GHGA.create_publication_alias, domain=CreatePublication, range=str)

slots.create_publication_title = Slot(uri=GHGA.title, name="create publication_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.create_publication_title, domain=CreatePublication, range=Optional[str])

slots.create_publication_abstract = Slot(uri=GHGA.abstract, name="create publication_abstract", curie=GHGA.curie('abstract'),
                   model_uri=GHGA.create_publication_abstract, domain=CreatePublication, range=Optional[str])

slots.create_publication_xref = Slot(uri=GHGA.xref, name="create publication_xref", curie=GHGA.curie('xref'),
                   model_uri=GHGA.create_publication_xref, domain=CreatePublication, range=Optional[Union[str, List[str]]])

slots.create_user_role = Slot(uri=GHGA.role, name="create user_role", curie=GHGA.curie('role'),
                   model_uri=GHGA.create_user_role, domain=CreateUser, range=Optional[Union[str, "UserRoleEnum"]])

slots.create_submission_affiliation = Slot(uri=GHGA.affiliation, name="create submission_affiliation", curie=GHGA.curie('affiliation'),
                   model_uri=GHGA.create_submission_affiliation, domain=CreateSubmission, range=Optional[str])

slots.create_submission_has_study = Slot(uri=GHGA.has_study, name="create submission_has study", curie=GHGA.curie('has_study'),
                   model_uri=GHGA.create_submission_has_study, domain=CreateSubmission, range=Optional[Union[dict, CreateStudy]])

slots.create_submission_has_project = Slot(uri=GHGA.has_project, name="create submission_has project", curie=GHGA.curie('has_project'),
                   model_uri=GHGA.create_submission_has_project, domain=CreateSubmission, range=Optional[Union[dict, CreateProject]])

slots.create_submission_has_sample = Slot(uri=GHGA.has_sample, name="create submission_has sample", curie=GHGA.curie('has_sample'),
                   model_uri=GHGA.create_submission_has_sample, domain=CreateSubmission, range=Optional[Union[Union[dict, CreateSample], List[Union[dict, CreateSample]]]])

slots.create_submission_has_biospecimen = Slot(uri=GHGA.has_biospecimen, name="create submission_has biospecimen", curie=GHGA.curie('has_biospecimen'),
                   model_uri=GHGA.create_submission_has_biospecimen, domain=CreateSubmission, range=Optional[Union[Union[dict, CreateBiospecimen], List[Union[dict, CreateBiospecimen]]]])

slots.create_submission_has_individual = Slot(uri=GHGA.has_individual, name="create submission_has individual", curie=GHGA.curie('has_individual'),
                   model_uri=GHGA.create_submission_has_individual, domain=CreateSubmission, range=Optional[Union[Union[dict, CreateIndividual], List[Union[dict, CreateIndividual]]]])

slots.create_submission_has_experiment = Slot(uri=GHGA.has_experiment, name="create submission_has experiment", curie=GHGA.curie('has_experiment'),
                   model_uri=GHGA.create_submission_has_experiment, domain=CreateSubmission, range=Optional[Union[Union[dict, CreateExperiment], List[Union[dict, CreateExperiment]]]])

slots.create_submission_has_protocol = Slot(uri=GHGA.has_protocol, name="create submission_has protocol", curie=GHGA.curie('has_protocol'),
                   model_uri=GHGA.create_submission_has_protocol, domain=CreateSubmission, range=Optional[Union[Union[dict, CreateProtocol], List[Union[dict, CreateProtocol]]]])

slots.create_submission_has_analysis = Slot(uri=GHGA.has_analysis, name="create submission_has analysis", curie=GHGA.curie('has_analysis'),
                   model_uri=GHGA.create_submission_has_analysis, domain=CreateSubmission, range=Optional[Union[Union[dict, CreateAnalysis], List[Union[dict, CreateAnalysis]]]])

slots.create_submission_has_file = Slot(uri=GHGA.has_file, name="create submission_has file", curie=GHGA.curie('has_file'),
                   model_uri=GHGA.create_submission_has_file, domain=CreateSubmission, range=Optional[Union[Union[dict, CreateFile], List[Union[dict, CreateFile]]]])

slots.create_submission_has_dataset = Slot(uri=GHGA.has_dataset, name="create submission_has dataset", curie=GHGA.curie('has_dataset'),
                   model_uri=GHGA.create_submission_has_dataset, domain=CreateSubmission, range=Optional[Union[Union[dict, CreateDataset], List[Union[dict, CreateDataset]]]])

slots.create_submission_has_data_access_policy = Slot(uri=GHGA.has_data_access_policy, name="create submission_has data access policy", curie=GHGA.curie('has_data_access_policy'),
                   model_uri=GHGA.create_submission_has_data_access_policy, domain=CreateSubmission, range=Optional[Union[Union[dict, CreateDataAccessPolicy], List[Union[dict, CreateDataAccessPolicy]]]])

slots.create_submission_has_data_access_committee = Slot(uri=GHGA.has_data_access_committee, name="create submission_has data access committee", curie=GHGA.curie('has_data_access_committee'),
                   model_uri=GHGA.create_submission_has_data_access_committee, domain=CreateSubmission, range=Optional[Union[Union[dict, CreateDataAccessCommittee], List[Union[dict, CreateDataAccessCommittee]]]])

slots.create_submission_has_member = Slot(uri=GHGA.has_member, name="create submission_has member", curie=GHGA.curie('has_member'),
                   model_uri=GHGA.create_submission_has_member, domain=CreateSubmission, range=Optional[Union[Union[dict, CreateMember], List[Union[dict, CreateMember]]]])

slots.create_submission_has_publication = Slot(uri=GHGA.has_publication, name="create submission_has publication", curie=GHGA.curie('has_publication'),
                   model_uri=GHGA.create_submission_has_publication, domain=CreateSubmission, range=Optional[Union[Union[dict, CreatePublication], List[Union[dict, CreatePublication]]]])

slots.create_submission_submission_status = Slot(uri=GHGA.submission_status, name="create submission_submission status", curie=GHGA.curie('submission_status'),
                   model_uri=GHGA.create_submission_submission_status, domain=CreateSubmission, range=Optional[Union[str, "SubmissionStatusEnum"]])

slots.ontology_class_mixin_concept_identifier = Slot(uri=GHGA.concept_identifier, name="ontology class mixin_concept identifier", curie=GHGA.curie('concept_identifier'),
                   model_uri=GHGA.ontology_class_mixin_concept_identifier, domain=None, range=Optional[str])

slots.ontology_class_mixin_name = Slot(uri=GHGA.name, name="ontology class mixin_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.ontology_class_mixin_name, domain=None, range=Optional[str])

slots.ontology_class_mixin_description = Slot(uri=GHGA.description, name="ontology class mixin_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.ontology_class_mixin_description, domain=None, range=Optional[str])
