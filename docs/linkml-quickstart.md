# Quickstart guide for using LinkML

# Overview

The LinkML framework provides a variety of idioms, called slots, to define the
semantics of classes and slots.

This quickstart guide will provide a brief description of commonly used LinkML
slots to define various aspects of the GHGA Metadata Schema.

Please refer to 
[LinkML documentation](https://linkml.github.io/linkml-model/docs/) for an
exhaustive list of slots provided by the modeling language.

---

## Inheritance Related Slots

### is_a

The `is_a` slot can be used to define a hierarchy for your class, mixin
or slot where a new class, mixin or slot is defined as a subclass of another
defined class, mixin or slot.

Note that `is_a` has the characteristics of homeomorphicity.

i.e. `is_a` should be used to connect,

- two mixins
- two classes
- two slots

### abstract

A class (or slot) may be tagged with its `abstract` slot set to the boolean
value `true`, to define whether it is abstract in nature. This has comparable
meaning to that in the Object Oriented Programming where another
class can use the abstract class as part of its inheritance hierarchy,
but the abstract class itself cannot be directly instantiated.

### mixin

The `mixin:true` declaration is used to extend the properties (or slots) of
a class, without changing its position in the class hierarchy.

Mixins can be extremely helpful in a number of ways:

- to generalize a set of attributes that can apply to classes in different
parts of the class hierarchy
- to reduce duplication of shared attributes between classes that do not
inherit from one another
- to prevent the sometimes confusing nature of multiple inheritance
noted in the [diamond problem](https://tinyurl.com/4zdw9tsb)

Mixins provide the means for reusing semantics, generally by the inclusion
of specific property slots or other semantic constraint, in different classes
or slots, without the need to tie slots to the hierarchy of the class itself.

###  mixins

The `mixins` slot (not to be confused with [`mixin`](#mixin)) can be used to
specify a list of mixins that a class (or slot) can use to  include the added
semantics of the mixins.

The `mixins` are separate from the `is_a` hierarchy and the mixin classes do
not contribute to a classes inheritance hierarchy.

---

## Identification, Description, and Indexing Related Slots

### aliases

The `aliases` slot can be used to define a list of aliases for a class
(or slot). This is useful for adding synonymous names to your class (or slot).

### description

The `description` slot can be used to provide a human-readable description of
a class (or slot).

### slot_uri

The `slot_uri` slot can be used to define a canonical URI that is the true
representation for that particular slot. That is, the value of `slot_uri` can
be used interchangably with the slot being defined.

### in_subset

The `in_subset` slot can be used tag your class (or slot) to belong to a
pre-defined subset.

The actual subset names are defined as part of the Schema definition.

### id_prefixes

The `id_prefixes` slot can be used to define a list of valid ID prefixes that
instances of this class ought to have as part of their CURIE.

The order of the list matters since its a prioritized list where the prefix
with the highest priority appears at the top of the list.

---

## Class Composition Related Slots

### slots

The `slots` property enumerates the names of slots which a given class,
mixin, or its subclasses are generally permitted to have.
Unless it is designated as one of the [`defining_slots`](#defining_slots), or
[`slot_usage`](#slot_usage) specifies that a given slot is required,
then it is **not** mandatory that such a slot is instantiated in all instances
of the given class, mixin, or its subclasses.

### defining_slots

The `defining_slots` slot can be used to specify which slots of an instance are
necessary for defining an instance as a member of a class.

Listing a slot as one of the `defining_slots` slots effectively makes
it a required slot.

### slot_usage

The `slot_usage` slot can be used to specify how a particular slot ought to be
used in a class.

This is useful for documenting what a particular slot means for instances of a
particular class.

In the `slot_usage` section we define the range and provide a description for
the slot's `subject` and `object`, to better document what entities this slot
is supposed to link.

### required

The `required` slot can be used to define whether a slot is required.

When a slot is declared as required, via `required: true`, any class that uses
that slot must have a value for that slot.

---

## Slots Related to Constraints on Slot Composition

### domain

The `domain` slot mimics the idea of `rdfs:domain` where you constrain the type
of classes that a given slot can be a part of.

### range

The `range` slot mimics the idea of `rdfs:range` where you can constrain the
type of classes (or data types) a given slot can have as its
value.

---

## Slots Related to Semantic Mappings

### exact_mappings

The `exact_mappings` slot can be used to define external concepts, predicates,
or properties which are considered to be exact mappings to the class (or slot)
being defined.

### close_mappings

The `close_mappings` slot can be used to define external concepts, predicates,
or properties which are considered to be close mappings to the class (or slot)
being defined.

### narrow_mappings

The `narrow_mappings` slot can be used to define external concepts, predicates,
or properties which are considered to be narrow mappings to the class (or slot)
being defined.

### broad_mappings

The `broad_mappings` slot can be used to define external concepts, predicates,
or properties which are considered to be broad mappings to the class (or slot)
being defined.

### related_mappings

The `related_mappings` slot can be used to define external concepts, predicates,
or properties which are considered to be related mappings to the class (or slot)
being defined.
