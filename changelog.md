## 0.9.0 release

- Changed `has data access policy`, `has data access committee`, `has study` to multivalued for submission class
- Added updated version of the submission spreadhseet
- Fixed usage of `has member` and `has individual` fields

## 0.8.0 release

- Added `has dataset`, `has data access policy`, `has data access committee` and `has member` to the `submission` class
- Changed `size` slot for a `file` as required
- Added Submission spreadsheet template to repository
- Retired custom generators in favor of GHGA specific generators
- Updated documentation

## 0.7.0 release

- Fixed range for Dataset slots
- Added `case control status` slot to Sample
- Added enum for paired end/single end read status

## 0.6.0 release

- Added `type` to appropriate classes
- Removed redundant declaration of slots in class definitions
- Changed `has parameter` slot to `has workflow parameter`
- Added `data request form` slot to the `data access policy` class
- Added `ancestry`, `data use permission`, `data use modifier` classes
- Added `has data user permission` and `has data use modifier` slots to `data use permission` class
- Added `has ancestry` that refers to the ancestral group an individual is part of
- Reorganized classes that are ontology classes
- Added `metadata mixin` to `submission` class
- Changed `has anatomical entity` to a multivalued field
- Removed `has data access policy` from `submission` class
- Added `has protocol` and `has publication` to `submission` class
- Added `type` to `experiment process`
- Added `has attribute` to `experiment process`
- Added `concept identifier` and `concept name` to `ontology class mixin`
- Added enum for age range
- Normalized representation of enum values
- Added `affiliation` to `submission` class to track the data hub/institution that is making the submission
- Fixed `id` and `alias` for `publication` class
- Added `has file` to `individual` class and `study` class
- Added GWAS to `study type enum`
- Added `drs uri` to `file` class
- Changed `has output` of `experiment process` class to be multivalued
- Changed `has sample` of `experiment` class to be multivalued
- Added `has file` to `protocol` class
- Added `type` to `biospecimen` class
- Removed `has experiment` and `has analysis` from `study` class
- Added `has attribute` to `experiment`, `file`, `data access policy`, `data access committee clases
- Added `other` category for 'file type enum' and 'age range enum'
- Changed `has individual` to optional for `sample` class
- Changed `type` to optional for `dataset` class
- Fixed range of `size` to integer

## 0.5.0 release

- Deprecated `technology` class and `has technology` slot
- Added `has protocol` slot to `experiment` class to capture protocol at the experiment level
- Added fields to track schema specific metadata
- Categorized slots as `essential`, `recommended`, and `optional`
- Added scripts for generation of use-case specific artifacts to support metadata submission
- Added scripts for generation of a relaxed schema to support metadata submission

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
- Removed 'accession' slot from 'NamedThing' entity to avoid it being inherited
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
