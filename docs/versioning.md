# Versioning

Typically we try to follow the [Semantic Versioning Guidelines](https://semver.org/) and try to apply these guidelines to the schema.

Following are a few scenarios to highlight what to do in terms of versioning.


### Adding classes and slots

When you add a class or a slot, you are adding something new with or without changing any existing classes or slots. If that is the case, then a minor version release (`0.1.0` to `0.2.0`) is appropriate. 


### Renaming classes (or slots)

When you are renaming a class (or a slot), you are introducing breaking changes. Ideally, you should never rename a class or slot directly. Instead, you should deprecate the previous class name (or slot name) and then create a new class (or slot) that is the renamed version of the previous class (or slot).

This ensures that the class and slot still exists in the schema (and deprecated), and a minor version release (`0.1.0` to `0.2.0`) is appropriate.


### Removing classes (or slots)

Just as mentioned in [section above](#renaming-classes-or-slots), do not delete a class (or slot) directly. You should deprecate the class (or slot) that is to be removed. 

This ensures that the class and slot still exists in the schema (and deprecated), and a minor version release (`0.1.0` to `0.2.0`) is appropriate.


**So when is a major version release justified?**

A major version release (`1.0.0` to `2.0.0`) signifies breaking changes that is incompatible with previous versions.

This should be done only after proper communication with the consortium, internal and external collaborators.

In the case of a major version release, you can remove all deprecated classes and/or slots since their removal from the schema is justified.

**So when is a patch version release justified?**

A patch version release (`0.0.1` to `0.0.2`) signifies small changes that are not functionally affecting the schema.

This should be done only if the changes made to the schema are superficial and not structural. For example, a change to a class or slot description is a superficial change.

