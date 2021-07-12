# Versioning

We adopt the [Semantic Versioning guidelines](https://semver.org/) for managing
GHGA Metadata Schema.

An excerpt from SemVer guidelines is as follows.

Given a version number MAJOR.MINOR.PATCH, increment the:

- MAJOR version when you make incompatible changes
- MINOR version when you add functionality in a backwards compatible manner
- PATCH version when you make backwards compatible bug fixes


Small and incremental changes to the schema can be distributed via a
patch release.

Any structural changes to the schema must be distributed via a minor release,
provided that the changes are backwards compatible.

Any modification that leads to backwards incompatibility must be distributed
via a new major release.

**Note:** The versioning of the schema also applies to its derived artifacts.
