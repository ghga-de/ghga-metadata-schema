# Release Process

This section is relevant to core developers who are responsible for making
stable releases of the schema and its artifacts.

Following are the steps for making a new release of the GHGA Metadata Schema.

**Update Version**

First check whether the `version` in schema YAML matches with the
latest release tag. If the version is the same then bump the version
in preparation for a new release.

Follow [Versioning guidelines](versioning.md) to decide whether the bump in
version is major, minor, or patch.

**Update Changelog**

Update `changelog.md` and list all the new updates that constitutes
this release.

**Merge all changes from `dev` to `main`**

Merge the `dev` branch to the `main` branch to bring them in sync.

**Release on GitHub**

Go to [https://github.com/ghga-de/ghga-metadata-schema/releases](),
create a new release, and add the contents from `changelog.md`
corresponding to the new release.

**Announcement**

Announce the new release in relevant channels.
