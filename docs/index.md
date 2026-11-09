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

Using the YAML, the [LinkML framework](https://github.com/linkml/linkml) and the
scripts in `scripts/`, we generate the following artifacts:

- Schema documentation
    - Markdown pages for every class, slot and enum in `docs/schema_markdown/`
- Entity relationship diagrams
    - Mermaid diagrams of the classes and their relations in `docs/entity_relations.md`
- Submission spreadsheet
    - The XLSX workbook used for metadata submission in `spreadsheets/`

