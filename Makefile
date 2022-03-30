SRC_DIR = src
SCHEMA_DIR = $(SRC_DIR)/schema
SOURCE_FILES := $(shell find $(SCHEMA_DIR) -name '*.yaml')
SCHEMA_NAMES = $(patsubst $(SCHEMA_DIR)/%.yaml, %, $(SOURCE_FILES))

SCHEMA_NAME = ghga
SCHEMA_SRC = $(SCHEMA_DIR)/$(SCHEMA_NAME).yaml
TGTS = graphql jsonschema markdown shex owl csv graphql python pydantic rdf sql

# Optional arguments to supply to the generators
#For example, GEN_OPTS = --no-mergeimports
GEN_OPTS = 

# Make all targets
all: gen stage

# Generate target names based on TGTS
gen: $(patsubst %,gen-%,$(TGTS))

# Clean up
clean:
	rm -rf target/
	rm -rf docs/docs/

# List all available artifact-specific targets
echo:
	@ echo $(patsubst %,gen-%,$(TGTS))

# Install dependencies
install:
	. environment.sh
	pip install -r requirements.txt

# Create target folders
tdir-%:
	mkdir -p target/$*

# Create docs folder
docs:
	mkdir $@

# Stage artifacts
stage: $(patsubst %,stage-%,$(TGTS))
stage-%: gen-%
	cp -pr target/$* artifacts/

stage-derived-schemas:
	cp -pr target/derived_schema artifacts/

# Build and deploy docs locally with mkdocs
docserve:
	mkdocs serve

# Deploy documentation to gh-pages branch
gh-deploy: stage-markdown
	mkdocs gh-deploy

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Markdown docs
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

gen-markdown: target/markdown/index.md
.PHONY: gen-markdown
target/markdown/%.md: $(SCHEMA_SRC) tdir-markdown
	gen-markdown $(GEN_OPTS) --dir target/markdown $<
stage-markdown: gen-markdown
	cp -pr target/markdown docs/docs

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python dataclasses
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

gen-python: $(patsubst %, target/python/%.py, $(SCHEMA_NAMES))
.PHONY: gen-python
target/python/%.py: $(SCHEMA_DIR)/%.yaml  tdir-python
	gen-py-classes --no-mergeimports $(GEN_OPTS) $< > $@

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Pydantic classes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

gen-pydantic: $(patsubst %, target/pydantic/%_models.py, $(SCHEMA_NAMES))
.PHONY: gen-pydantic
target/pydantic/%_models.py: $(SCHEMA_DIR)/%.yaml  tdir-pydantic
	python scripts/custom_pydanticgen.py --no-mergeimports $(GEN_OPTS) $< > $@

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GraphQL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

gen-graphql:target/graphql/$(SCHEMA_NAME).graphql 
target/graphql/%.graphql: $(SCHEMA_DIR)/%.yaml tdir-graphql
	gen-graphql $(GEN_OPTS) $< > $@

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# JSONSchema
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

gen-jsonschema: target/jsonschema/$(SCHEMA_NAME).schema.json
target/jsonschema/%.schema.json: $(SCHEMA_DIR)/%.yaml tdir-jsonschema
	python scripts/custom_jsonschemagen.py --include-range-class-descendants $(GEN_OPTS) $< > $@

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ShEx
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

gen-shex: $(patsubst %, target/shex/%.shex, $(SCHEMA_NAMES))
target/shex/%.shex: $(SCHEMA_DIR)/%.yaml tdir-shex
	gen-shex --no-mergeimports $(GEN_OPTS) $< > $@

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CSV
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

gen-csv: $(patsubst %, target/csv/%.csv, $(SCHEMA_NAMES))
target/csv/%.csv: $(SCHEMA_DIR)/%.yaml tdir-csv
	gen-csv $(GEN_OPTS) $< > $@

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# OWL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

gen-owl: target/owl/$(SCHEMA_NAME).owl.ttl
.PHONY: gen-owl
target/owl/%.owl.ttl: $(SCHEMA_DIR)/%.yaml tdir-owl
	gen-owl $(GEN_OPTS) $< > $@

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# RDF
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

gen-rdf: target/rdf/$(SCHEMA_NAME).ttl
target/rdf/%.ttl: $(SCHEMA_DIR)/%.yaml tdir-rdf
	gen-rdf $(GEN_OPTS) $< > $@

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SQL DDL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

gen-sql: target/sql/$(SCHEMA_NAME).sql
target/sql/%.sql: $(SCHEMA_DIR)/%.yaml tdir-sql
	gen-sqlddl-legacy $(GEN_OPTS) --sqla-file  target/sql/$(SCHEMA_NAME)_models.py --dialect postgresql+psycopg2 $< > $@


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Derived schemas: creation
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

gen-creation-schema: target/derived_schema/creation/$(SCHEMA_NAME)_creation.yaml
target/derived_schema/creation/%_creation.yaml: $(SCHEMA_DIR)/%.yaml
	mkdir -p target/derived_schema/creation
	python scripts/generate_creation_schema.py --schema-yaml $< --output $@

gen-creation-schema-artifacts: gen-creation-schema gen-creation-schema-python-classes gen-creation-schema-pydantic-models gen-creation-schema-jsonschema

gen-creation-schema-python-classes: target/derived_schema/creation/$(SCHEMA_NAME)_creation.py
target/derived_schema/creation/%_creation.py: target/derived_schema/creation/$(SCHEMA_NAME)_creation.yaml
	gen-py-classes --no-mergeimports $(GEN_OPTS) $< > $@

gen-creation-schema-pydantic-models: target/derived_schema/creation/$(SCHEMA_NAME)_creation_models.py
target/derived_schema/creation/%_creation_models.py: target/derived_schema/creation/$(SCHEMA_NAME)_creation.yaml
	gen-pydantic --no-mergeimports $(GEN_OPTS) $< > $@

gen-creation-schema-jsonschema: target/derived_schema/creation/$(SCHEMA_NAME)_creation.schema.json
target/derived_schema/creation/%_creation.schema.json: target/derived_schema/creation/$(SCHEMA_NAME)_creation.yaml
	gen-json-schema --include-range-class-descendants $(GEN_OPTS) $< > $@
