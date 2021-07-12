# Introduction

The [German Human Genome-Phenome Archive (GHGA)](https://ghga.dkfz.de/) is
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

- JSON Schema
    - JSON Schema definitions of all classes and properties
- Python Dataclasses
    - Python Dataclasses for each defined class
- SQL DDL
    - SQL Data Definition Language to create SQL tables for all classes
- SQLAlchemy classes
    - SQLAlchemy classes to map SQL tables and columns to each defined class
and slot, respectively
- GraphQL
    - GraphQL types for each defined class
- ShEx
    - Shape Expressions for each defined class
- RDF
    - The model represented as RDF Turtle (TTL)
- OWL
    - The model in Web Ontology Language (OWL), serialized as RDF Turtle (TTL)
- CSV
    - A CSV summary of the model and its classes

