# Testing

When you make changes to the GHGA Metadata Schema, be sure to try and build
the schema using LinkML. This will surface any syntax or structural errors.

To build and validate schema-related artifacts, run the following:

```sh
# Install dependencies in the dev container
dev_install

# Validate schema linting and generated artifacts
./scripts/schema_linter.py
./scripts/generate_linkml_docs.py --check
./scripts/generate_xlsx.py --check
./scripts/update_entity_relations.py --check
```
