# Maintaining the GHGA Metadata Schema

This document serves as a reference on how to maintain the schema.

## Making changes to the schema

Refer to the [Contributing Guidelines](contributing.md) and [Curation Guidelines](curating.md) to learn how to go about making changes to the schema.


## Generating Artifacts

Once the changes are made to the schema YAML, we need to generate artifacts. This ensures that the artifacts are up-to-date with the schema YAML.

### GitHub Actions

In GHGA Metadata Schema repository, we generate:

- Python dataclasses
- Python Pydantic classes
- JSON Schema
- GraphQL
- RDF

This generation of artifacts is automated and manged via GitHub Actions.

Thus, contributors to the repository should never commit any changes to the files in the `artifacts` folder. These changes will always be overwritten by GitHub Actions.

### Makefile

The repository has a `Makefile` that is used to generate all necessary artifacts from the YAML. You can use this `Makefile` to generate artifacts locally (to test whether your schema changes are giving outputs as expected; Just avoid committing these artifacts to your branch).

For example,

You can run the following to generate Pydantic classes from the schema YAML:

```sh
make gen-pydantic
```

Similarly for JSON Schema:

```sh
make gen-jsonschema
```

These Make targets should run successfully as long as the schema YAML is valid and consistent.


This Makefile is also used by GitHub Actions to,

- Build and test that the schema is valid
- Build artifacts and commit to the repository when there is a change to `src/schema/` folder

