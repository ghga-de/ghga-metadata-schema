# GHGA Metadata Schema

This repository aims to serve as the source of truth for the GHGA Metadata schema.

The schema is modeled using [LinkML](https://github.com/biolink/biolinkml/) and exists
as a YAML, which can be found in [src/schema/](src/schema/ghga.yaml).

Using the YAML and the LinkML framework, we autogenerate downstream artifacts like:

- [JSON Schema](jsonschema/ghga.schema.json)
- [ShEx](shex/ghga.shex)
- [OWL](owl/ghga.owl.ttl)
- [RDF](rdf/ghga.rdf)
- [TSV/CSV reports](csv/)*


## GHGA Metadata Schema Overview

![GHGA Metadata Schema](ghga-overview.png "GHGA Metadata Schema")

