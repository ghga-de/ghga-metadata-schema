# Style Guide for Curating the Schema

The GHGA metadata schema exists as a YAML and can be found at `src/schema/`.

The YAML is organized into 4 parts:

- **[Schema Properties](#schema-properties)**: Section that defines properties
regarding the schema
- **[Classes](#classes)**: Section that defines all the classes
- **[Slots](#slots)**: Section that defines all the slots
- **[Types](#types)**: Section that defines all the custom data types

## Schema Properties

In this section the following must be defined,

- Any property that describes the metadata schema
- Any schema imports
- Default CURI maps
- Prefix to IRI mappings that do not exist in the referenced
default CURI maps

## Classes

All classes in the schema must be defined in this section, where:

- Class names must be in `sentence case`
- Class names must be unambiguous and must be a noun
- A class should have a definition that describes the class and gives an
idea of its intended usage


## Slots

All slots (also known as fields or properties) must be defined in this
section, where:

- Slot names must be in `sentence case`
- Slot names must be unambiguous to avoid misuse
- A slot should have a definition that describes the slot and gives an
idea of its indended usage


## Types

All custom data types must be defined in this section, where:

- Type names must be in `sentence case`
- Type names must be unambiguous to avoid misuse
- A type must clarify what its value space is, by the way of inheritance
or by defining its `range`
- A type should have a definition that describes the type and gives an
idea of its indended usage
