# Introduction

This repository aims to serve as the source of truth for the metadata model used by the German Human Genome-Phenome Archive.

The schema is modeled using LinkML and exists as a YAML, which can be found in src/schema/.

Using the YAML and the LinkML framework, we autogenerate vendor/technology specific artifacts like:

- JSON Schema
    - JSON Schema definitions of all classes and properties
- Python Dataclasses
    - Python Dataclasses for each defined class
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

