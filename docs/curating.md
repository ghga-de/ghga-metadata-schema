# Curating the GHGA Metadata Schema

This document serves as a reference for curators of the GHGA Metadata Schema.

Following things to keep in mind:

- All changes to the schema should happen in the YAML
- When in doubt about LinkML vocabulary, refer to the [LinkML Quickstart Guide](linkml-quickstart.md)
- When in doubt about the syntax/format for defining class name and slot name, refer to [Style Guide](style-guide.md)

## Adding a class

It is recommended that curators take the following steps when creating or modifying a class in the schema:

- **Organization:** First determine where the class fits in the overall hierarchy. Is the class a sub-type of an existing class? Or is the class entirely new and trying to capture a different aspect of metadata?
- **Purpose:** Determine the information that the class is trying to capture. What fields would be required? What are the value types of these fields?
- **Linking:** Should fields of this class reference other classes? If so, the fields should be named appropriately
- **Naming:** In the schema YAML, the class name should be in `sentence case` and should be singular


## Adding a field

It is recommended that curators take the following steps when creating or modifying a field (slot) in the schema:

- **Organization:** First determine where the field fits in the overall schema. Is there a field already that is capturing similar information? Can that field be repurposed or modified to better suit a broader scope? Or is the field capturing something that is highly specific and thus needs to be added?
- **Purpose:** Determine the information that the field is trying to capture. And determine the value space for the field. This will help you define what the value (range) of the field is. By default, this is `string` but it certainly can be another class, a specific type, or an enum
- **Cardinality:** Determine if the slot is single-valued, multi-valued, or conditionally multi-valued
- **Naming:** In the schema YAML, the field name should be in `sentence case` and should be singular, regardless of cardinality. If the field is referencing another class then the field name should be of the format `has <DESTINATION_CLASS>` where `<DESTINATION_CLASS>` is the name of the class that this field is referring to. For example, `has experiment` or `has study`.

## Adding an enum type

It is recommended that curators take the following steps when creating or modifying an enum in the schema:

- **Organization:** First determine where the enum fits in the overall schema. Is there an existing enum that is already capturing similar information? Can an existing enum be extended with additional values to support a broader scope?
- **Purpose**: Determine the information that the enum is trying to capture, and which fields are going to use this enum. This will help you determine possible values that needs to be enumerated in the enum
- **Naming:** In the schema YAML, the enum name should be in `sentence case` and should be singular. Each enumerated value for an enum should have a description that explains the value


## Deprecating classes and fields

As a rule of thumb, do not immediately remove a class or a field (slot) from the schema. Instead, use the concept of deprecation to deprecate classes and fields that are no longer desired.

You can do so by adding `deprecated: true` to the class or slot definition.

These deprecated classes and slots should remain in the schema until the next **major** release. 

> The interpration of a major release is as per [SemVer guidelines](https://semver.org/)

Such an approach ensures that existing tools and software can still work with the deprecated classes and fields until they adapt to a major release of the schema.

