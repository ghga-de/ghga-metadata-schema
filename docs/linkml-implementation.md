# Implementation of GHGA Metadata Schema using LinkML

## Overview

The GHGA Metadata Schema is implemented using LinkML. 

For a quick primer on LinkML refer to [linkml-quickstart.md](linkml-quickstart.md).

To learn about how to curate the GHGA Metadata Schema, refer to [Curating Guidelines](curating.md).


## Design Principles

If your entity is a real world entity then treat it as a class.

If you are adding a field/property as an attribute of a real world entity then treat it
as a slot.

If a field/property is a reference to one or more entities of another class then the
field should follow the following format: `has_<REFEREE_CLASS>`.

Whether or not this field is multivalued should be managed via `slot_usage`.


## Structure

The GHGA Metadata Schema is defined as a YAML and uses the LinkML vocabulary to define entities
in the schema.

The schema YAML has the following structure:

- [Schema Definition](#schema-definiton)
- Class Definition
- Slot Definition
- Enum Definition


### Schema Definiton

A [Schema Definition](https://linkml.io/linkml-model/docs/SchemaDefinition/) is used to describe
properties about your schema. For example, schema `id`, `name`, `description`, etc.

Using the Schema Definition, you can also define:

- schema imports (`imports`)
- any prefixes that may be used in the schema YAML (`prefixes`)
- define a default prefix (`default_prefix`)
- define a default range (`default_range`)


### Class Definition

A [Class Definition](https://linkml.io/linkml-model/docs/ClassDefinition/) is used to describe a class
in your schema. Typically a class is defined for any real-world entity. In the case of the GHGA Metadata Schema,
we define class for Sample, Experiment, File, Study, etc.

Using the Class Definition, you can define:

- the inheritance (`is_a`)
- mixins to apply (`mixins`)
- the class description (`description`)
- mappings (`exact_mappings`)
- fields of this class (`slots`)
- usage of fields (`slot_usage`)


### Slot Definition

A [Slot Definition](https://linkml.io/linkml-model/docs/SlotDefinition/) is used to describe a
slot (field) in your schema. Typically a slot is like a field for a class. In the case of GHGA Metadata Schema, we define slots like `id`, `name`, `title`, `alias`, etc.

Using the Slot Definition, you can define:

- the slot description (`description`)
- the slot is part of a subset (`in_subset`)
- mappings (`exact_mappings`)
- range or value space of a slot (`range`)


### Enum Definition

An [Enum Definition](https://linkml.io/linkml-model/docs/EnumDefinition/) is used to define an enum in your schema. Typically an enum is a clever way of constraining the value space of a field to a handful of values. In the case of GHGA Metadata Schema, we define enums like `biological sex enum`, `file type enum`, `study type enum`, etc.

Using the Enum Defintion, you can define:

- the enum description (`description`)
- enumerate all the possible values for this enum
