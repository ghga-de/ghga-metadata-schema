# GHGA Metadata Schema

This repository aims to serve as the source of truth for the GHGA Metadata schema.

The schema itself is modeled using [LinkML](https://github.com/biolink/biolinkml/) where the schema is authored
as a YAML, which can be found in [src/schema/](src/schema/ghga.yaml).

Using the YAML and the LinkML framework, we autogenerate downstream artifacts like:

 * JSON Schema
 * ShEx
 * OWL
 * RDF
 * TSV/CSV reports


