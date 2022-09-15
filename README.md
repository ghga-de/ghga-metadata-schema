# GHGA Metadata Schema

[![Build artifacts](https://github.com/ghga-de/ghga-metadata-schema/actions/workflows/build-artifacts.yml/badge.svg?branch=main)](https://github.com/ghga-de/ghga-metadata-schema/actions/workflows/build-artifacts.yml)
[![Build Documentation](https://github.com/ghga-de/ghga-metadata-schema/actions/workflows/build-documentation.yml/badge.svg?branch=main)](https://github.com/ghga-de/ghga-metadata-schema/actions/workflows/build-documentation.yml)

The [German Human Genome-Phenome Archive (GHGA)](https://www.ghga.de/) is
funded by the [German Research Foundation (DFG)](https://www.dfg.de/en/)
within the framework of the
[National Research Data Infrastructure (NFDI)](https://www.nfdi.de/en-gb).

The main goal of GHGA is to address the needs for establishing a national
genome archive for human genome data while tackling challenges in data
access, sharing, and privacy. GHGA aims to provide a national infrastructure
for secure and safe storage,access management, dissemination, and analysis of
human omics data under a coherent ethical-legal framework. 

This repository aims to serve as the source of truth for the metadata schema
used by the German Human Genome-Phenome Archive.

The schema is modeled using LinkML and exists as a YAML, which can be
found in `src/schema/`.

Using the YAML, and the [LinkML framework](https://github.com/linkml/linkml),
we autogenerate vendor/technology specific artifacts like:

- [JSON Schema](artifacts/jsonschema)
    - JSON Schema definitions of all classes and properties
- [Python Dataclasses](artifacts/python)
    - Python Dataclasses for each defined class
- [Pydantic models](artifacts/pydantic)
    - Pydantic models for each defined class
- [SQL DDL](artifacts/sql)
    - SQL Data Definition Language to create SQL tables for all classes
- [SQLAlchemy classes](artifacts/sql)
    - SQLAlchemy classes to map SQL tables and columns to each defined class and slot, respectively
- [GraphQL](artifacts/graphql)
    - GraphQL types for each defined class
- [ShEx](artifacts/shex)
    - Shape Expressions for each defined class
- [RDF](artifacts/rdf)
    - The model represented as RDF Turtle (TTL)
- [OWL](artifacts/owl)
    - The model in Web Ontology Language (OWL), serialized as RDF Turtle (TTL)
- [CSV](artifacts/csv)
    - A CSV summary of the model and its classes


Changes made
 - has_publication removed from Project
 - has_study made as list in Experiment
 - introduced target regions as mandatory in Library preparation protocol
 - Deleted has anatomical entity from Biospecimen
 - Deleted has disease from Biospecimen
 - Deleted has phenotypic feature from Biospecimen
 - Introduced lane number and sample index sequence to Sample
 - Introduced description to Analysis
 - Introduced type to Dataset
 - Introduced description as mandatory to Data Access Policy