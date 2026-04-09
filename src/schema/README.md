## For contributors: Checking if YAML syntax is correct

Use the repository dev container for contributor setup. Once the dev container is running, install the required dependencies with:

```bash
dev_install
```

After that, the repository is ready to work on. To generate and validate the schema artifacts, run:

```bash
./scripts/schema_linter.py
./scripts/generate_linkml_docs.py --check
./scripts/generate_xlsx.py --check
./scripts/update_entity_relations.py --check
```

Conventions:

- Keep your schema in `src/schema`
- Use the `.yaml` suffix for all schema files
- Use the suggested directory layout here
