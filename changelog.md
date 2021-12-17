## 0.4.0 release

- Added a `restricted` subset to the schema and tag slots that are
restricted to be part of the restricted subset
- Added `alias` to all entities
- Added `ega_accession` to all relevant entities

## 0.3.0 release

- Simplified the definition of `dataset` by combining slots from
`experiment dataset` and `analysis dataset`
- Removed `experiment dataset` and `analysis dataset`

## 0.2.0 release

- Rearranged fields that are likely to be sparse and unnecessary for
many of the entities
- Moved 'accession' slot to an 'accession mixin' that can be applied to only
those entities that are likely to be assigned an accession
- Removed 'accession' slot from 'named thing' entity to avoid it being inherited
by all of its descendant
- Created an 'ontology class mixin' to entities that are a proxy for ontology
terms/concepts like anatomical entity, disease, phenotypic feature
- Removed 'has study slot from project entity to avoid circular references

## 0.1.0 release

- Restructured the schema
- Added new entities
- Added new properties for entities
- Added mappings to ontologies
- Added Pydantic models to the list of generated artifacts
 

## 0.0.1 release

- First release of the GHGA Metadata Schema
