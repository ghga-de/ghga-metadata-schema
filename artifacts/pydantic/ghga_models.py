from __future__ import annotations
from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel, Field

metamodel_version = "None"
version = "0.5.0"


class CaseControlEnum(str, Enum):
    
    control = "control"
    case = "case"
    
    

class BiologicalSexEnum(str, Enum):
    
    female = "female"
    male = "male"
    unknown = "unknown"
    
    

class UserRoleEnum(str, Enum):
    
    data_requester = "data_requester"
    data_steward = "data_steward"
    
    

class VitalStatusEnum(str, Enum):
    
    alive = "alive"
    deceased = "deceased"
    unknown = "unknown"
    
    

class StudyTypeEnum(str, Enum):
    
    whole_genome_sequencing = "whole_genome_sequencing"
    metagenomics = "metagenomics"
    transcriptome_analysis = "transcriptome_analysis"
    resequencing = "resequencing"
    epigenetics = "epigenetics"
    synthetic_genomics = "synthetic_genomics"
    forensic_paleo_genomics = "forensic_paleo_genomics"
    gene_regulation = "gene_regulation"
    cancer_genomics = "cancer_genomics"
    population_genomics = "population_genomics"
    rna_seq = "rna_seq"
    exome_sequencing = "exome_sequencing"
    pooled_clone_sequencing = "pooled_clone_sequencing"
    other = "other"
    
    

class FileFormatEnum(str, Enum):
    
    bam = "bam"
    complete_genomics = "complete_genomics"
    cram = "cram"
    fasta = "fasta"
    fastq = "fastq"
    pacbio_hdf5 = "pacbio_hdf5"
    sff = "sff"
    srf = "srf"
    vcf = "vcf"
    
    

class SubmissionStatusEnum(str, Enum):
    
    in_progress = "in_progress"
    completed = "completed"
    
    

class ReleaseStatusEnum(str, Enum):
    
    unreleased = "unreleased"
    released = "released"
    
    

class ExperimentProcessTypeEnum(str, Enum):
    
    sample_preparation = "sample_preparation"
    assay = "assay"
    
    

class AgeRangeEnum(str, Enum):
    
    number_0_5 = "0-5"
    number_6_10 = "6-10"
    number_11_15 = "11-15"
    number_16_20 = "16-20"
    number_21_25 = "21-25"
    number_26_30 = "26-30"
    number_31_35 = "31-35"
    number_36_40 = "36-40"
    number_41_45 = "41-45"
    number_46_50 = "46-50"
    number_51_55 = "51-55"
    number_56_60 = "56-60"
    number_61_65 = "61-65"
    number_66_70 = "66-70"
    number_71_75 = "71-75"
    number_76_80 = "76-80"
    number_80PLUS_SIGN = "80+"
    
    

class Attribute(BaseModel):
    """
    A key/value pair that further characterizes an entity.
    """
    key: str = Field(None, description="""The key for an attribute.""")
    key_type: Optional[str] = Field(None, description="""A semantic type that characterizes the attribute key. Usually this is a term from an ontology. For example, 'MAXO:0000616' indicates that the attribute is a measurement of oxygen saturation in the blood.""")
    value: str = Field(None, description="""The value for an attribute. Usually this is a numerical value (without the units).""")
    value_type: Optional[str] = Field(None, description="""The value type that characterizes the attribute value. Usually this is a term from an ontology that describes how to interpret the value. For example, 'SIO:001413' indicates that the value is to be interpreted as a percentage.""")
    


class WorkflowParameter(BaseModel):
    """
    A key/value pair that represents a parameter used in a Workflow Step.
    """
    key: Optional[str] = Field(None, description="""Key that represents the parameter name.""")
    value: Optional[str] = Field(None, description="""Value corresponding to the the parameter key.""")
    


class OntologyClassMixin(BaseModel):
    """
    Mixin for entities that represent an class/term/concept from an ontology.
    """
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    concept_identifier: Optional[str] = Field(None, description="""The Compact URI (CURIE) that uniquely identifies this ontology class.""")
    concept_name: Optional[str] = Field(None, description="""The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.""")
    description: Optional[str] = Field(None, description="""The description or definition of an ontology class.""")
    ontology_name: Optional[str] = Field(None, description="""The name of the ontology from which this ontology class was chosen.""")
    ontology_version: Optional[str] = Field(None, description="""The version of the ontology from which this ontology class was chosen.""")
    


class MetadataMixin(BaseModel):
    """
    Mixin for tracking schema specific metadata about an instance.
    """
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class NamedThing(BaseModel):
    """
    A databased entity, concept or class. This is a generic class that is the root of all the other classes.
    """
    id: str = Field(None, description="""The internal unique identifier for an entity.""")
    alias: Optional[str] = Field(None, description="""The alias (alternate identifier) for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Holds one or more database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Agent(NamedThing):
    """
    An agent is something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity. Agents include a Person, Organization, or Software that performs an activity.
    """
    name: Optional[str] = Field(None, description="""The name for an entity.""")
    description: Optional[str] = Field(None, description="""Description of an entity.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Person(NamedThing):
    """
    A member of the species Homo sapiens.
    """
    given_name: Optional[str] = Field(None, description="""First name.""")
    family_name: Optional[str] = Field(None, description="""Last name.""")
    additional_name: Optional[str] = Field(None, description="""Additional name(s).""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Committee(NamedThing):
    """
    A group of people organized for a specific purpose.
    """
    name: Optional[str] = Field(None, description="""The name for an entity.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class MaterialEntity(NamedThing):
    """
    A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has mass.
    """
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class BiologicalQuality(NamedThing):
    """
    A biological quality is a quality held by a biological entity.
    """
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class InformationContentEntity(NamedThing):
    """
    A generically dependent continuant that is about some thing.
    """
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class PlannedProcess(NamedThing):
    """
    A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and depends on some entity during the time it occurs.
    """
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Investigation(PlannedProcess):
    """
    Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.
    """
    title: Optional[str] = Field(None, description="""The title that describes an entity.""")
    description: Optional[str] = Field(None, description="""Description of an entity.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class DataTransformation(PlannedProcess):
    """
    A data transformation technique used to analyze and interpret data to gain a better understanding of it.
    """
    title: Optional[str] = Field(None, description="""The title that describes an entity.""")
    description: Optional[str] = Field(None, description="""Description of an entity.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class ResearchActivity(PlannedProcess):
    """
    A planned process executed in the performance of scientific research wherein systematic investigations are performed to establish facts and reach new conclusions about phenomena in the world.
    """
    title: Optional[str] = Field(None, description="""The title that describes an entity.""")
    description: Optional[str] = Field(None, description="""Description of an entity.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Technology(InformationContentEntity):
    """
    A Technology is an abstraction that represents the instrument used for an assay. The Technology entity captures instrument-specific attributes that are relevant for an Experiment entity. The Technology entity may be further characterized by its children where each child has fields that are relevant to that particular technology.
    """
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Workflow(InformationContentEntity):
    """
    A Workflow is an abstraction that represents the workflow used to perform an analysis. The Workflow entity captures workflow-specific attributes that are relevant for an Analysis entity. The Workflow entity may be further characterized by its children where each child has fields that are relevant to that particular workflow.
    """
    has_workflow_step: Optional[Union[List[WorkflowStep], List[str]]] = Field(None, description="""The individual workflow step that with other workflow step(s) collectively defines a Workflow entity.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class WorkflowStep(InformationContentEntity):
    """
    A Workflow Step represents each individual step performed in a Workflow. If the Workflow is a single-step workflow then the Workflow has just one Workflow Step entity. If the Workflow is a multi-step workflow then the Workflow has a Workflow Step entity for each step. All Workflow step specific attributes like parameters, and metadata about execution environment are captured by the Workflow Step entity.
    """
    has_workflow_parameter: Optional[Union[List[WorkflowParameter], List[str]]] = Field(None, description="""One or more parameters that are associated with this Workflow Step.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class DiseaseOrPhenotypicFeature(BiologicalQuality):
    """
    Disease or Phenotypic Feature that the entity is associated with. This entity is a union of Disease and Phenotypic Feature and exists to accommodate situations where Disease concepts are used interchangeably with Phenotype concepts or vice-versa.
    """
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    concept_identifier: Optional[str] = Field(None, description="""The Compact URI (CURIE) that uniquely identifies a concept from an ontology, thesaurus, or terminology.""")
    concept_name: Optional[str] = Field(None, description="""The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.""")
    description: Optional[str] = Field(None, description="""Description of an entity.""")
    ontology_name: Optional[str] = Field(None, description="""The name of the ontology from which this ontology class was chosen.""")
    ontology_version: Optional[str] = Field(None, description="""The version of the ontology from which this ontology class was chosen.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Population(MaterialEntity):
    """
    A population is a collection of individuals from the same taxonomic class living, counted or sampled at a particular site or in a particular area.
    """
    name: Optional[str] = Field(None, description="""The name for an entity.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Ancestry(Population):
    """
    Population category defined using ancestry informative markers (AIMs) based on genetic/genomic data.
    """
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    concept_identifier: Optional[str] = Field(None, description="""The Compact URI (CURIE) that uniquely identifies a concept from an ontology, thesaurus, or terminology.""")
    concept_name: Optional[str] = Field(None, description="""The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.""")
    description: Optional[str] = Field(None, description="""Description of an entity.""")
    ontology_name: Optional[str] = Field(None, description="""The name of the ontology from which this ontology class was chosen.""")
    ontology_version: Optional[str] = Field(None, description="""The version of the ontology from which this ontology class was chosen.""")
    name: Optional[str] = Field(None, description="""The name for an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class AnalysisProcess(PlannedProcess):
    """
    An analysis process is a process that describes how one or more Files, from a Study, are transformed to another set of Files via a Workflow. The analysis process also keeps track of the workflow metadata and the Agent that is running the Analysis.
    """
    title: Optional[str] = Field(None, description="""The title that describes an entity.""")
    has_input: Optional[Union[List[File], List[str]]] = Field(None, description="""The input data File entities used in the Analysis Process.""")
    has_workflow: Optional[Union[Workflow, str]] = Field(None, description="""The Workflow entity associated with this Analysis Process.""")
    has_agent: Optional[Union[Agent, str]] = Field(None, description="""The Agent - a software, institution, or human - that is executing or responsible for executing the workflow.""")
    has_output: Optional[Union[List[File], List[str]]] = Field(None, description="""The output data File entities generated by the Analysis Process.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class DataUseCondition(InformationContentEntity):
    """
    Data Use Condition represents the use conditions associated with a policy.
    """
    has_data_use_permission: Optional[Union[DataUsePermission, str]] = Field(None, description="""Data use permission associated with a policy. Typically one or more terms from DUO and should be descendants of 'DUO:0000001 data use permission'.""")
    has_data_use_modifier: Optional[Union[DataUseModifier, str]] = Field(None, description="""Modifier for Data use permission associated with a policy. Should be descendants of 'DUO:0000017 data use modifier'""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Member(Person):
    """
    Member of an Organization or a Committee.
    """
    email: str = Field(None, description="""The email of the Member.""")
    telephone: Optional[str] = Field(None, description="""The telephone number of the Member.""")
    organization: str = Field(None, description="""The organization that the Member is part of.""")
    given_name: Optional[str] = Field(None, description="""First name.""")
    family_name: Optional[str] = Field(None, description="""Last name.""")
    additional_name: Optional[str] = Field(None, description="""Additional name(s).""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Publication(InformationContentEntity):
    """
    The Publication entity represents a publication. While a publication can be any article that is published, the minimum expectation is that the publication has a valid DOI.
    """
    title: Optional[str] = Field(None, description="""The title for the Publication.""")
    abstract: Optional[str] = Field(None, description="""The study abstract that describes the goals. Can also hold abstract from a publication related to this study.""")
    id: str = Field(None, description="""A PMID or DOI for the Publication.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""One or more cross-references for this Publication.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class AnatomicalEntity(MaterialEntity):
    """
    Biological entity that is either an individual member of a biological species or constitutes the structural organization of an individual member of a biological species.
    """
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    concept_identifier: Optional[str] = Field(None, description="""The Compact URI (CURIE) that uniquely identifies a concept from an ontology, thesaurus, or terminology.""")
    concept_name: Optional[str] = Field(None, description="""The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.""")
    description: Optional[str] = Field(None, description="""Description of an entity.""")
    ontology_name: Optional[str] = Field(None, description="""The name of the ontology from which this ontology class was chosen.""")
    ontology_version: Optional[str] = Field(None, description="""The version of the ontology from which this ontology class was chosen.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class CellLine(MaterialEntity):
    """
    A cultured cell population that represents a genetically stable and homogenous population of cultured cells that shares a common propagation history.
    """
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Disease(DiseaseOrPhenotypicFeature):
    """
    A disease is a disposition to undergo pathological processes that exists in an organism because of one or more disorders in that organism.
    """
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    concept_identifier: Optional[str] = Field(None, description="""The Compact URI (CURIE) that uniquely identifies a concept from an ontology, thesaurus, or terminology.""")
    concept_name: Optional[str] = Field(None, description="""The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.""")
    description: Optional[str] = Field(None, description="""Description of an entity.""")
    ontology_name: Optional[str] = Field(None, description="""The name of the ontology from which this ontology class was chosen.""")
    ontology_version: Optional[str] = Field(None, description="""The version of the ontology from which this ontology class was chosen.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class PhenotypicFeature(DiseaseOrPhenotypicFeature):
    """
    The observable form taken by some character (or group of characters) in an individual or an organism, excluding pathology and disease. The detectable outward manifestations of a specific genotype.
    """
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    concept_identifier: Optional[str] = Field(None, description="""The Compact URI (CURIE) that uniquely identifies a concept from an ontology, thesaurus, or terminology.""")
    concept_name: Optional[str] = Field(None, description="""The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.""")
    description: Optional[str] = Field(None, description="""Description of an entity.""")
    ontology_name: Optional[str] = Field(None, description="""The name of the ontology from which this ontology class was chosen.""")
    ontology_version: Optional[str] = Field(None, description="""The version of the ontology from which this ontology class was chosen.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class User(Person):
    """
    A user in GHGA.
    """
    email: Optional[str] = Field(None, description="""Email of a person.""")
    role: Optional[UserRoleEnum] = Field(None, description="""The role of the user""")
    given_name: Optional[str] = Field(None, description="""First name.""")
    family_name: Optional[str] = Field(None, description="""Last name.""")
    additional_name: Optional[str] = Field(None, description="""Additional name(s).""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Submission(BaseModel):
    """
    A grouping entity that represents information about one or more entities. A submission can be considered as a set of inter-related (and inter-connected) entities that represent a data submission to GHGA.
    """
    id: str = Field(None, description="""A internal unique identifier for the Submission.""")
    has_study: Optional[Union[Study, str]] = Field(None, description="""Information about a Study entities associated with this submission.""")
    has_project: Optional[Union[Project, str]] = Field(None, description="""Information about a Project entity associated with this submission.""")
    has_sample: Optional[Union[List[Sample], List[str]]] = Field(None, description="""Information about one or more Sample entities associated with this submission.""")
    has_biospecimen: Optional[Union[List[Biospecimen], List[str]]] = Field(None, description="""Information about one or more Biospecimen entities associated with this submission.""")
    has_individual: Optional[Union[List[Individual], List[str]]] = Field(None, description="""Information about one or more Individual entities associated with this submission.""")
    has_experiment: Optional[Union[List[Experiment], List[str]]] = Field(None, description="""Information about one or more Experiment entities associated with this submission.""")
    has_protocol: Union[List[Protocol], List[str]] = Field(None, description="""One or more Protocol entities associated with this Submission.""")
    has_analysis: Optional[Union[List[Analysis], List[str]]] = Field(None, description="""Information about one or more Analysis entities associated with this submission.""")
    has_file: Optional[Union[List[File], List[str]]] = Field(None, description="""Information about one or more File entities associated with this submission.""")
    has_publication: Optional[Union[List[Publication], List[str]]] = Field(None, description="""One or more Publication entities associated with this Submission.""")
    submission_date: Optional[str] = Field(None, description="""The timestamp (in ISO 8601 format) when submission was marked completed.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the Submission was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the Submission was updated.""")
    submission_status: Optional[SubmissionStatusEnum] = Field(None, description="""The status of a Submission.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class DataUsePermission(InformationContentEntity):
    """
    A data item that is used to indicate consent permissions for datasets and/or materials and relates to the purposes for which datasets and/or material might be removed, stored or used.
    """
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    concept_identifier: Optional[str] = Field(None, description="""The Compact URI (CURIE) that uniquely identifies a concept from an ontology, thesaurus, or terminology.""")
    concept_name: Optional[str] = Field(None, description="""The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.""")
    description: Optional[str] = Field(None, description="""Description of an entity.""")
    ontology_name: Optional[str] = Field(None, description="""The name of the ontology from which this ontology class was chosen.""")
    ontology_version: Optional[str] = Field(None, description="""The version of the ontology from which this ontology class was chosen.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class DataUseModifier(InformationContentEntity):
    """
    Data use modifiers indicate additional conditions for use.
    """
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    concept_identifier: Optional[str] = Field(None, description="""The Compact URI (CURIE) that uniquely identifies a concept from an ontology, thesaurus, or terminology.""")
    concept_name: Optional[str] = Field(None, description="""The name or label (typically, rdfs:label) of concept from an ontology, thesaurus, or terminology.""")
    description: Optional[str] = Field(None, description="""Description of an entity.""")
    ontology_name: Optional[str] = Field(None, description="""The name of the ontology from which this ontology class was chosen.""")
    ontology_version: Optional[str] = Field(None, description="""The version of the ontology from which this ontology class was chosen.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class AccessionMixin(BaseModel):
    """
    Mixin for entities that can be assigned a GHGA accession.
    """
    accession: Optional[str] = Field(None, description="""A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.""")
    


class Biospecimen(MaterialEntity):
    """
    A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics, treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is derived.
    """
    name: Optional[str] = Field(None, description="""The name for an entity.""")
    description: Optional[str] = Field(None, description="""Description of an entity.""")
    isolation: Optional[str] = Field(None, description="""Method or device employed for collecting/isolating a biospecimen or a sample.""")
    storage: Optional[str] = Field(None, description="""Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).""")
    has_individual: Optional[Union[Individual, str]] = Field(None, description="""The Individual entity from which this Biospecimen was derived.""")
    has_anatomical_entity: Optional[Union[List[AnatomicalEntity], List[str]]] = Field(None, description="""The Anatomical entity, that represents the site, from which the Biospecimen was retrieved. Typically, a concept from Uber-anatomy Ontology (UBERON). For example, 'UBERON:0008307' indicates that the Biospecimen was extracted from the 'Heart Endothelium' of an Individual.""")
    has_disease: Optional[Union[List[Disease], List[str]]] = Field(None, description="""The Disease entity that is associated with the Individual. Typically, a concept from Mondo Disease Ontology. For example, 'MONDO:0005267' indicates that the Individual suffers from 'Heart Disease'.""")
    has_phenotypic_feature: Optional[Union[List[PhenotypicFeature], List[str]]] = Field(None, description="""The Phenotypic Feature entity that is associated with the Individual. Typically, a concept from Human Phenotype Ontology. For example, 'HP:0100244' indicates that the Individual exhibits 'Fibrosarcoma' as one of its phenotype.""")
    accession: Optional[str] = Field(None, description="""A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Family(Population):
    """
    A domestic group, or a number of domestic groups linked through descent (demonstrated or stipulated) from a common ancestor, marriage, or adoption.
    """
    has_member: Optional[Union[List[Individual], List[str]]] = Field(None, description="""One or more Individuals that collectively define this Family.""")
    has_proband: Optional[Union[Individual, str]] = Field(None, description="""The Individual that is reported to have a disorder which results in the Family being brought into a Study.""")
    accession: Optional[str] = Field(None, description="""A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.""")
    name: Optional[str] = Field(None, description="""The name for an entity.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Cohort(Population):
    """
    A cohort is a collection of individuals that share a common characteristic/observation and have been grouped together for a research study/investigation.
    """
    has_member: Optional[Union[List[Individual], List[str]]] = Field(None, description="""One or more Individuals that collectively define this Cohort.""")
    accession: Optional[str] = Field(None, description="""A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.""")
    name: Optional[str] = Field(None, description="""The name for an entity.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class EgaAccessionMixin(BaseModel):
    """
    Mixin for entities that can be assigned an EGA accession, in addition to GHGA accession.
    """
    ega_accession: Optional[str] = Field(None, description="""A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.""")
    


class Experiment(Investigation):
    """
    An experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
    """
    type: str = Field(None, description="""The type of Experiment.""")
    biological_replicates: Optional[str] = Field(None, description="""A biological replicate is a replicate role that consists of independent biological replicates made from different individual biosamples.""")
    technical_replicates: Optional[str] = Field(None, description="""A technical replicate is a replicate role where the same BioSample is use e.g. the same pool of RNA used to assess technical (as opposed to biological) variation within an experiment.""")
    experimental_replicates: Optional[str] = Field(None, description="""The replicate number of the assay, i.e. the numeric iteration for the assay that was repeated.""")
    has_study: Union[Study, str] = Field(None, description="""The Study entity associated with this Experiment.""")
    has_sample: Union[Sample, str] = Field(None, description="""The Sample entity associated with this Experiment.""")
    has_file: Optional[Union[List[File], List[str]]] = Field(None, description="""One or more Files entities that are generated as output of this Experiment.""")
    has_protocol: Union[List[Protocol], List[str]] = Field(None, description="""One or more Protocol entities associated with this Experiment.""")
    has_experiment_process: Optional[Union[List[ExperimentProcess], List[str]]] = Field(None, description="""One or more Experiment Processes entities associated with this Experiment.""")
    accession: Optional[str] = Field(None, description="""A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.""")
    ega_accession: Optional[str] = Field(None, description="""A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.""")
    title: Optional[str] = Field(None, description="""Name for the experiment (eg: GHGAE_PBMC_RNAseq).""")
    description: str = Field(None, description="""A detailed description of the Experiment.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: str = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Individual(Person):
    """
    An Individual is a Person who is participating in a Study.
    """
    sex: BiologicalSexEnum = Field(None, description="""The assemblage of physical properties or qualities by which male is distinguished from female; the physical difference between male and female; the distinguishing peculiarity of male or female.""")
    karyotype: Optional[str] = Field(None, description="""The karyotype of an individual if defined.""")
    age: AgeRangeEnum = Field(None, description="""Age of an individual.""")
    vital_status: VitalStatusEnum = Field(None, description="""Last known Vital Status of an Individual.""")
    geographical_region: Optional[str] = Field(None, description="""The geographical region where the Individual is located. Any demarcated area of the Earth; may be determined by both natural and human boundaries.""")
    has_ancestry: Optional[Union[List[Ancestry], List[str]]] = Field(None, description="""A person's descent or lineage, from a person or from a population. Typically this is a value from HANCESTRO (Human Ancestry Ontology).""")
    has_parent: Optional[Union[List[Individual], List[str]]] = Field(None, description="""One or more parent for this Individual.""")
    has_children: Optional[Union[List[Individual], List[str]]] = Field(None, description="""One or more children for this Individual.""")
    has_disease: Optional[Union[List[Disease], List[str]]] = Field(None, description="""The Disease entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Mondo Disease Ontology. For example, 'MONDO:0003742' indicates that the Individual - from which the Biospecimen was extracted from - suffers from 'Heart Fibrosarcoma'.""")
    has_phenotypic_feature: Optional[Union[List[PhenotypicFeature], List[str]]] = Field(None, description="""The Phenotypic Feature entity that is associated with this Biospecimen at the time of retrieval from the organism. Typically, a concept from Human Phenotype Ontology. For example, 'HP:0100244' indicates that the Individual - from which the Biospecimen was extracted from - exhibits 'Fibrosarcoma' as one of its phenotype.""")
    accession: Optional[str] = Field(None, description="""A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.""")
    ega_accession: Optional[str] = Field(None, description="""A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.""")
    given_name: Optional[str] = Field(None, description="""First name.""")
    family_name: Optional[str] = Field(None, description="""Last name.""")
    additional_name: Optional[str] = Field(None, description="""Additional name(s).""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: str = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Donor(Individual):
    """
    A Donor is an Individual that participates in a research Study by donating a Biospecimen. The use of the Biospecimen is restricted to the consent provided by the Donor.
    """
    sex: BiologicalSexEnum = Field(None, description="""The assemblage of physical properties or qualities by which male is distinguished from female; the physical difference between male and female; the distinguishing peculiarity of male or female.""")
    karyotype: Optional[str] = Field(None, description="""The karyotype of an individual if defined.""")
    age: AgeRangeEnum = Field(None, description="""Age of an individual.""")
    vital_status: VitalStatusEnum = Field(None, description="""The state or condition of being living or deceased; also includes the case where the vital status is unknown.""")
    geographical_region: Optional[str] = Field(None, description="""The geographical region where the Individual is located. Any demarcated area of the Earth; may be determined by both natural and human boundaries.""")
    has_ancestry: Optional[Union[List[Ancestry], List[str]]] = Field(None, description="""A person's descent or lineage, from a person or from a population. Typically this is a value from HANCESTRO (Human Ancestry Ontology).""")
    has_parent: Optional[Union[List[Individual], List[str]]] = Field(None, description="""The parent of an entity.""")
    has_children: Optional[Union[List[Individual], List[str]]] = Field(None, description="""The children of an entity.""")
    has_disease: Optional[Union[List[Disease], List[str]]] = Field(None, description="""Disease concept that the entity is associated with.""")
    has_phenotypic_feature: Optional[Union[List[PhenotypicFeature], List[str]]] = Field(None, description="""Phenotypic feature concept that the entity is associated with.""")
    accession: Optional[str] = Field(None, description="""A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.""")
    ega_accession: Optional[str] = Field(None, description="""A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.""")
    given_name: Optional[str] = Field(None, description="""First name.""")
    family_name: Optional[str] = Field(None, description="""Last name.""")
    additional_name: Optional[str] = Field(None, description="""Additional name(s).""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: str = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class File(InformationContentEntity):
    
    name: str = Field(None, description="""The given filename.""")
    format: FileFormatEnum = Field(None, description="""The format of the file: BAM, SAM, CRAM, BAI, etc.""")
    size: Optional[str] = Field(None, description="""The size of a file in bytes.""")
    checksum: str = Field(None, description="""A computed value which depends on the contents of a block of data and which is transmitted or stored along with the data in order to detect corruption of the data. The receiving system recomputes the checksum based upon the received data and compares this value with the one sent with the data. If the two values are the same, the receiver has some confidence that the data was received correctly.""")
    checksum_type: str = Field(None, description="""The type of algorithm used to generate the checksum of a file.""")
    accession: Optional[str] = Field(None, description="""A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.""")
    ega_accession: Optional[str] = Field(None, description="""A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: str = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Analysis(DataTransformation):
    """
    An Analysis is a data transformation that transforms input data to output data. The workflow used to achieve this transformation and the individual steps are also captured.
    """
    type: str = Field(None, description="""The type of the Analysis. Either Reference Alignment (BAM) or Sequence Variation (VCF)""")
    reference_genome: str = Field(None, description="""A published genetic sequence that is used as a reference sequence against which other sequences are compared. Reference genome(s) or annotation(s) used for prior analyses (eg: GRCh38.p13).""")
    reference_chromosome: str = Field(None, description="""The reference chromosome used for this Analysis.""")
    has_input: Union[List[File], List[str]] = Field(None, description="""The input data File entities used in the Analysis.""")
    has_study: Optional[Union[Study, str]] = Field(None, description="""The Study entity associated with this Analysis.""")
    has_workflow: Optional[Union[List[Workflow], List[str]]] = Field(None, description="""One or more Workflow entities associated with this Analysis.""")
    has_analysis_process: Optional[Union[List[AnalysisProcess], List[str]]] = Field(None, description="""One or more Analysis Process entities associated with this Analysis.""")
    has_output: Union[List[File], List[str]] = Field(None, description="""The output data File entities generated by this Analysis.""")
    accession: Optional[str] = Field(None, description="""A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.""")
    ega_accession: Optional[str] = Field(None, description="""A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.""")
    title: Optional[str] = Field(None, description="""The title that describes an entity.""")
    description: Optional[str] = Field(None, description="""Describing how an Analysis was carried out. (e.g.: computational tools, settings, etc.).""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: str = Field(None, description="""An alias uniquely identifying this Analysis entitiy.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class DataAccessPolicy(InformationContentEntity):
    """
    A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or more Datasets belonging to one or more Studies.
    """
    name: Optional[str] = Field(None, description="""A name for the Data Access Policy.""")
    description: str = Field(None, description="""A short description for the Data Access Policy.""")
    policy_text: str = Field(None, description="""The terms of data use and policy verbiage should be captured here.""")
    policy_url: Optional[str] = Field(None, description="""URL for the policy, if available. This is useful if the terms of the policy is made available online at a resolvable URL.""")
    has_data_access_committee: Union[DataAccessCommittee, str] = Field(None, description="""The Data Access Committee linked to this policy.""")
    has_data_use_condition: Optional[List[DataUseCondition]] = Field(None, description="""Data Use Condition entities that are associated with the Data Access Policy.""")
    data_request_form: Optional[str] = Field(None, description="""Data Request Form that is associated with this Data Access Policy.""")
    accession: Optional[str] = Field(None, description="""A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.""")
    ega_accession: Optional[str] = Field(None, description="""A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: str = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class DataAccessCommittee(Committee):
    """
    A group of members that are delegated to grant access to one or more datasets after ensuring the minimum criteria for data sharing has been met, and request for data use does not raise ethical and/or legal concerns.
    """
    name: str = Field(None, description="""The name for the Data Access Committee.""")
    description: Optional[str] = Field(None, description="""A description for the Data Access Committee.""")
    main_contact: Union[Member, str] = Field(None, description="""The main contact for the Data Access Committee.""")
    has_member: Optional[Union[List[Member], List[str]]] = Field(None, description="""All the members that are part of this Data Access Committee.""")
    accession: Optional[str] = Field(None, description="""A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.""")
    ega_accession: Optional[str] = Field(None, description="""A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: str = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class AttributeMixin(BaseModel):
    """
    Mixin for entities that can have one or more attributes.
    """
    has_attribute: Optional[List[Attribute]] = Field(None, description="""Key/value pairs corresponding to an entity.""")
    


class Project(ResearchActivity):
    """
    Any specifically defined piece of work that is undertaken or attempted to meet a single requirement.
    """
    accession: Optional[str] = Field(None, description="""A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.""")
    has_attribute: Optional[List[Attribute]] = Field(None, description="""Custom attributes for the Project  (eg: Cancer - Colon cancer, prostrate cancer, blood cancer etc)""")
    title: str = Field(None, description="""Comprehensive title for the project.""")
    description: str = Field(None, description="""Short textual description of the project (Some information on the protocol, sample used and collected etc)""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: str = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class ExperimentProcess(PlannedProcess):
    """
    An Experiment Process is a process that describes how a Sample is transformed to a File via an assay. The Experiment Process also keeps track of the Protocol used and the Agent that is running the experiment.
    """
    type: Optional[ExperimentProcessTypeEnum] = Field(None, description="""The type of experiment process.""")
    title: Optional[str] = Field(None, description="""A descriptive title that explains the step(s) involved in performing the experiment leading up to the sequencing of the sample and generation of raw data from the instrument. (eg: Sample extraction -> Target Enrichment)""")
    has_input: Optional[Union[Sample, str]] = Field(None, description="""The input to the Experiment Process. Usually a Sample entity.""")
    has_protocol: Optional[Union[Protocol, str]] = Field(None, description="""The Protocol entity used by this Experiment Process.""")
    has_agent: Optional[Union[Agent, str]] = Field(None, description="""The Agent - a software, institution, or human - that is executing or responsible for executing the Experiment Process.""")
    has_output: Optional[Union[File, str]] = Field(None, description="""The output of this Experiment Process. Usually a File entity.""")
    has_attribute: Optional[List[Attribute]] = Field(None, description="""Key/value pairs corresponding to an entity.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Protocol(InformationContentEntity):
    """
    A plan specification which has sufficient level of detail and quantitative information to communicate it between investigation agents, so that different investigation agents will reliably be able to independently reproduce the process.
    """
    name: Optional[str] = Field(None, description="""Name of the protocol (eg: Sample extraction_PCR amplification).""")
    type: Optional[str] = Field(None, description="""Type of the protocol (eg: Target enrichment).""")
    description: Optional[str] = Field(None, description="""Detailed description of the Protocol.""")
    url: Optional[str] = Field(None, description="""URL for the resource that describes this Protocol.""")
    has_attribute: Optional[List[Attribute]] = Field(None, description="""One or more attributes that further characterizes this Protocol.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""One or more cross-references for this Protocol.  (Eg: manufacturer protocol, protocol from publication etc )""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class LibraryPreparationProtocol(Protocol):
    """
    Information about the library preparation of an Experiment.
    """
    library_name: str = Field(None, description="""A short name identifying the library to potential users. The same name may refer to multiple versions of the same continually updated library.""")
    library_layout: str = Field(None, description="""Describe whether the library was sequenced in single-end (forward or reverse) or paired-end mode""")
    library_type: str = Field(None, description="""Describe the level of omics analysis (eg: Metagenome, transcriptome, etc)""")
    library_selection: str = Field(None, description="""Whether any method was used to select for or against, enrich, or screen the material being sequenced. Library Selection method (e.g. random, PCA, cDNA, etc )""")
    library_preparation: str = Field(None, description="""The general method for sequencing library preparation (e.g. KAPA PCR-free).""")
    library_preparation_kit_retail_name: str = Field(None, description="""A unique identifier for the kit used to construct a genomic library. This may include the vendor name, kit name and kit version  (e.g. Agilent sure select Human Exome V8, Twist RefSeq Exome, etc.)""")
    library_preparation_kit_manufacturer: str = Field(None, description="""Manufacturer of library preparation kit""")
    primer: Optional[str] = Field(None, description="""The type of primer used for reverse transcription, e.g. 'oligo-dT' or 'random' primer. This allows users to identify content of the cDNA library input e.g. enriched for mRNA.""")
    end_bias: Optional[str] = Field(None, description="""The end of the cDNA molecule that is preferentially sequenced, e.g. 3/5 prime tag or end, or the full-length transcript.""")
    target_regions: str = Field(None, description="""Subset of genes or specific regions of the genome, which are most likely to be involved in the phenotype under study.""")
    rnaseq_strandedness: Optional[str] = Field(None, description="""The strandedness of the library, whether reads come from both strands of the cDNA or only from the first (antisense) or the second (sense) strand.""")
    name: Optional[str] = Field(None, description="""The name for an entity.""")
    type: Optional[str] = Field(None, description="""The type of an entity.""")
    description: str = Field(None, description="""Description about how a sequencing library was prepared (eg: Library construction method).""")
    url: Optional[str] = Field(None, description="""A URL to a resource.""")
    has_attribute: Optional[List[Attribute]] = Field(None, description="""One or more attributes that further characterizes this Library Preparation Protocol.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class SequencingProtocol(Protocol):
    """
    Information about the sequencing of a sample.
    """
    sequencing_center: Optional[str] = Field(None, description="""Center where sample was sequenced.""")
    instrument_model: str = Field(None, description="""The name and model of the technology platform used to perform sequencing.""")
    paired_or_single_end: Optional[str] = Field(None, description="""Denotes whether a submitted FASTQ file contains forward (R1) or reverse (R2) reads for paired-end sequencing. The number that identifies each read direction in a paired-end nucleotide sequencing replications.""")
    sequencing_read_length: Optional[str] = Field(None, description="""Length of sequencing reads (eg: Long or short or actual number of the read length etc). The number of nucleotides successfully ordered from each side of a nucleic acid fragment obtained after the completion of a sequencing process""")
    index_sequence: Optional[str] = Field(None, description="""A unique nucleotide sequence that is added to a sample during library preparation to serve as a unique identifier for the sample.""")
    target_coverage: Optional[str] = Field(None, description="""Mean coverage for whole genome sequencing, or mean target coverage for whole exome and targeted sequencing. The number of times a particular locus (site, nucleotide, amplicon, region) was sequenced.""")
    lane_number: Optional[str] = Field(None, description="""The numerical identifier for the lane or machine unit where a sample was located during nucleotide sequencing.""")
    flow_cell_id: Optional[str] = Field(None, description="""Flow Cell ID (eg: Experiment ID_Cell 1_Lane_1). The barcode assigned to a flow cell used in nucleotide sequencing.""")
    flow_cell_type: Optional[str] = Field(None, description="""Type of flow cell used (e.g. S4, S2 for NovaSeq; PromethION, Flongle for Nanopore). Aparatus in the fluidic subsystem where the sheath and sample meet. Can be one of several types; jet-in-air, quartz cuvette, or a hybrid of the two. The sample flows through the center of a fluid column of sheath fluid in the flow cell.""")
    umi_barcode_read: Optional[str] = Field(None, description="""The type of read that contains the UMI barcode (Eg: index1/index2/read1/read2).""")
    umi_barcode_size: Optional[str] = Field(None, description="""The size of the UMI identifying barcode (Eg. '10').""")
    umi_barcode_offset: Optional[str] = Field(None, description="""The offset in sequence of the UMI identifying barcode. (E.g. '16').""")
    cell_barcode_read: Optional[str] = Field(None, description="""The type of read that contains the cell barcode (eg: index1/index2/read1/read2).""")
    cell_barcode_offset: Optional[str] = Field(None, description="""The offset in sequence of the cell identifying barcode. (Eg. '0').""")
    cell_barcode_size: Optional[str] = Field(None, description="""The size of the cell identifying barcode (E.g. '16').""")
    sample_barcode_read: Optional[str] = Field(None, description="""The type of read that contains the sample barcode (eg: index1/index2/read1/read2).""")
    name: Optional[str] = Field(None, description="""The name for an entity.""")
    type: Optional[str] = Field(None, description="""Name of the library preparation protocol (eg: mRNA-seq,Whole exome long-read sequencing etc).""")
    description: str = Field(None, description="""Description about the sequencing protocol (eg: mRNA-seq,Whole exome long-read sequencing etc).""")
    url: Optional[str] = Field(None, description="""A URL to a resource.""")
    has_attribute: Optional[List[Attribute]] = Field(None, description="""One or more attributes that further characterizes this Sequencing Protocol.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: Optional[str] = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Sample(MaterialEntity):
    """
    A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation, demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).
    """
    name: str = Field(None, description="""Name of the sample (eg:GHGAS_Blood_Sample1 or GHGAS_PBMC_RNAseq_S1).""")
    type: Optional[CaseControlEnum] = Field(None, description="""Type of sample: 'Case' or 'Control'.""")
    description: str = Field(None, description="""Short textual description of the sample (How the sample was collected, sample source, protocol followed for processing the sample etc).""")
    vital_status_at_sampling: Optional[str] = Field(None, description="""Vital Status of an Individual at the point of sampling (eg:'Alive', 'Deceased').""")
    isolation: Optional[str] = Field(None, description="""Method or device employed for collecting/isolating a biospecimen or a sample.""")
    storage: Optional[str] = Field(None, description="""Methods by which a biospecimen or a sample is stored (e.g. frozen in liquid nitrogen).""")
    has_individual: Union[Individual, str] = Field(None, description="""The Individual from which this Sample was derived from.""")
    has_anatomical_entity: Optional[Union[List[AnatomicalEntity], List[str]]] = Field(None, description="""Anatomical site associated with an entity.""")
    has_biospecimen: Optional[Union[Biospecimen, str]] = Field(None, description="""The Biospecimen from which this Sample was prepared from.""")
    accession: Optional[str] = Field(None, description="""A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.""")
    ega_accession: Optional[str] = Field(None, description="""A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.""")
    has_attribute: Optional[List[Attribute]] = Field(None, description="""Key/value pairs corresponding to an entity.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: str = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""One or more cross-references for this Sample. For example, this Sample may have an EBI BioSamples accession or an EGA Sample accession.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class PublicationMixin(BaseModel):
    """
    Mixin for entities that can have one or more publications.
    """
    has_publication: Optional[str] = Field(None, description="""The Publication associated with an entity.""")
    


class DeprecatedMixin(BaseModel):
    """
    Mixin for entities that can be deprecated.
    """
    replaced_by: Optional[str] = Field(None, description="""Refers to the entity which replaces a currently deprecated entity.""")
    deprecation_date: Optional[str] = Field(None, description="""The timestamp (in ISO 8601 format) when the entity was deprecated.""")
    


class ReleaseStatusMixin(BaseModel):
    """
    Mixin for entities that can be released at a later point in time.
    """
    release_status: Optional[str] = Field(None, description="""The release status of an entity.""")
    release_date: Optional[str] = Field(None, description="""The timestamp (in ISO 8601 format) when the entity was released for public consumption.""")
    


class Study(Investigation):
    """
    Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and analysis of a subject to learn more about the phenomenon being studied.
    """
    type: StudyTypeEnum = Field(None, description="""The type of Study. For example, 'Cancer Genomics', 'Epigenetics', 'Exome Sequencing'.""")
    affiliation: List[str] = Field(None, description="""Institutions associated with this study.""")
    has_experiment: Optional[Union[List[Experiment], List[str]]] = Field(None, description="""One or more Experiment entities associated with this Study.""")
    has_analysis: Optional[Union[List[Analysis], List[str]]] = Field(None, description="""One or more Analysis entities associated with this Study.""")
    has_project: Optional[Union[Project, str]] = Field(None, description="""The project associated with this Study.""")
    accession: Optional[str] = Field(None, description="""A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.""")
    ega_accession: Optional[str] = Field(None, description="""A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.""")
    has_publication: Optional[Union[List[Publication], List[str]]] = Field(None, description="""One or more Publication entities associated with this Study.""")
    has_attribute: Optional[List[Attribute]] = Field(None, description="""Custom key/value pairs that further characterizes the Study. (e.g.: approaches - single-cell, bulk etc)""")
    release_status: Optional[ReleaseStatusEnum] = Field(None, description="""The release status of a Study.""")
    release_date: Optional[str] = Field(None, description="""The timestamp (in ISO 8601 format) when the entity was released for public consumption.""")
    title: str = Field(None, description="""A comprehensive title for the study.""")
    description: str = Field(None, description="""A detailed description (abstract) that describes the goals of this Study.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: str = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    


class Dataset(InformationContentEntity):
    """
    A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
    """
    title: str = Field(None, description="""A title for the submitted Dataset.""")
    description: str = Field(None, description="""Description of an entity.""")
    type: str = Field(None, description="""The type of an entity.""")
    has_study: Union[List[Study], List[str]] = Field(None, description="""One or more Study entities that are referenced by this Dataset.""")
    has_experiment: Optional[Union[List[Analysis], List[str]]] = Field(None, description="""One or more Analysis entities that are referenced by this Dataset.""")
    has_sample: Union[List[Study], List[str]] = Field(None, description="""One or more Sample entities that are referenced by this Dataset.""")
    has_analysis: Optional[Union[List[Study], List[str]]] = Field(None, description="""One or more Analysis entities that are referenced by this Dataset.""")
    has_file: Union[List[File], List[str]] = Field(None, description="""One or more File entities that collectively are part of this Dataset.""")
    has_data_access_policy: Union[DataAccessPolicy, str] = Field(None, description="""The Data Access Policy that applies to this Dataset.""")
    accession: Optional[str] = Field(None, description="""A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.""")
    ega_accession: Optional[str] = Field(None, description="""A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.""")
    has_publication: Optional[Union[List[Publication], List[str]]] = Field(None, description="""One or more Publication entities associated with this Dataset.""")
    release_status: Optional[ReleaseStatusEnum] = Field(None, description="""The release status of a Dataset.""")
    release_date: Optional[str] = Field(None, description="""The timestamp (in ISO 8601 format) when the entity was released for public consumption.""")
    id: str = Field(None, description="""An identifier that uniquely represents an entity.""")
    alias: str = Field(None, description="""The alias for an entity.""")
    xref: Optional[List[str]] = Field(None, description="""Database cross references for an entity.""")
    creation_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was created.""")
    update_date: Optional[str] = Field(None, description="""Timestamp (in ISO 8601 format) when the entity was updated.""")
    schema_type: Optional[str] = Field(None, description="""The schema type an instance corresponds to.""")
    schema_version: Optional[str] = Field(None, description="""The version of the schema an instance corresponds to.""")
    



# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
Attribute.update_forward_refs()
WorkflowParameter.update_forward_refs()
OntologyClassMixin.update_forward_refs()
MetadataMixin.update_forward_refs()
NamedThing.update_forward_refs()
Agent.update_forward_refs()
Person.update_forward_refs()
Committee.update_forward_refs()
MaterialEntity.update_forward_refs()
BiologicalQuality.update_forward_refs()
InformationContentEntity.update_forward_refs()
PlannedProcess.update_forward_refs()
Investigation.update_forward_refs()
DataTransformation.update_forward_refs()
ResearchActivity.update_forward_refs()
Technology.update_forward_refs()
Workflow.update_forward_refs()
WorkflowStep.update_forward_refs()
DiseaseOrPhenotypicFeature.update_forward_refs()
Population.update_forward_refs()
Ancestry.update_forward_refs()
AnalysisProcess.update_forward_refs()
DataUseCondition.update_forward_refs()
Member.update_forward_refs()
Publication.update_forward_refs()
AnatomicalEntity.update_forward_refs()
CellLine.update_forward_refs()
Disease.update_forward_refs()
PhenotypicFeature.update_forward_refs()
User.update_forward_refs()
Submission.update_forward_refs()
DataUsePermission.update_forward_refs()
DataUseModifier.update_forward_refs()
AccessionMixin.update_forward_refs()
Biospecimen.update_forward_refs()
Family.update_forward_refs()
Cohort.update_forward_refs()
EgaAccessionMixin.update_forward_refs()
Experiment.update_forward_refs()
Individual.update_forward_refs()
Donor.update_forward_refs()
File.update_forward_refs()
Analysis.update_forward_refs()
DataAccessPolicy.update_forward_refs()
DataAccessCommittee.update_forward_refs()
AttributeMixin.update_forward_refs()
Project.update_forward_refs()
ExperimentProcess.update_forward_refs()
Protocol.update_forward_refs()
LibraryPreparationProtocol.update_forward_refs()
SequencingProtocol.update_forward_refs()
Sample.update_forward_refs()
PublicationMixin.update_forward_refs()
DeprecatedMixin.update_forward_refs()
ReleaseStatusMixin.update_forward_refs()
Study.update_forward_refs()
Dataset.update_forward_refs()

